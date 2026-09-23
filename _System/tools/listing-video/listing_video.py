#!/usr/bin/env python3
"""
listing_video.py — turn a handful of listing photos into a vertical short-form reel.

Output: 1080x1920, 30fps, H.264 / yuv420p MP4 with a silent audio track,
sized for Instagram Reels, TikTok, and YouTube Shorts.

Default layout is split: photos move in the top 1080x960, the bottom 1080x960
stays pure black so Ryan can drop a green-screen talking head over it.
`--layout full` fills the whole frame with photos instead.

No AI, no credits, no network. Just ffmpeg camera moves.

Typical use (the skill picks the photos, this script renders them):

    python3 listing_video.py --photos a.jpg b.jpg c.jpg ... --out reel.mp4

Per-photo treatment and motion can be overridden with --manifest.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

# ---------------------------------------------------------------------------
# Output spec
# ---------------------------------------------------------------------------

W, H = 1080, 1920
FPS = 30

# Work at 4x before the final downscale. Both zoompan and crop quantize their
# window to whole input pixels, so moving across a 1080-wide source steps a
# full pixel at a time and visibly stutters. At 4x each step is a quarter pixel
# once scaled back down, which reads as smooth motion.
UPSCALE = 4

# Instagram lays its header over the top of the video. Full-layout blur cards
# stay below it.
SAFE_TOP = 250

PANS = ("pan_left", "pan_right", "pan_up", "pan_down")

# Source photos are JPEGs, which are full-range. Encoding those samples while
# tagging the file limited-range is what makes an export look washed out or
# crushed once a phone plays it back, so convert explicitly on the way out.
OUT = "scale=in_range=full:out_range=tv,format=yuv420p,setsar=1"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def run(cmd: list[str]) -> None:
    proc = subprocess.run(cmd, stdout=subprocess.DEVNULL,
                          stderr=subprocess.PIPE, text=True)
    if proc.returncode != 0:
        sys.stderr.write("\nffmpeg failed:\n" + " ".join(cmd) + "\n\n")
        sys.stderr.write((proc.stderr or "")[-4000:] + "\n")
        raise SystemExit(1)


def probe_size(path: str) -> tuple[int, int]:
    """Displayed dimensions, with EXIF/container rotation applied."""
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height:stream_side_data=rotation",
         "-of", "json", path],
        capture_output=True, text=True,
    )
    streams = (json.loads(out.stdout or "{}").get("streams") or [])
    if not streams:
        raise SystemExit(f"Could not read image: {path}")
    st = streams[0]
    w, h = int(st["width"]), int(st["height"])
    for sd in st.get("side_data_list", []) or []:
        if "rotation" in sd and abs(int(sd["rotation"])) % 180 == 90:
            w, h = h, w
    return w, h


def black_pad(args) -> str:
    """Filter fragment that extends a top-half panel to the full frame in black.
    Empty in full layout, where the panel already is the frame."""
    if args.layout != "split":
        return ""
    return f"pad={W}:{H}:0:0:color=black,"


def even(n: float) -> int:
    """libx264 wants even dimensions."""
    i = int(round(n))
    return i if i % 2 == 0 else i + 1


# ---------------------------------------------------------------------------
# Camera moves
# ---------------------------------------------------------------------------

def zoom_expr(motion: str, frames: int, zoom: float) -> tuple[str, str, str]:
    """(z, x, y) for a zoompan push or pull, held on the frame center."""
    span = max(frames - 1, 1)
    cx, cy = "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    if motion == "pull":
        return (f"{zoom:.4f}-{zoom - 1:.4f}*on/{span}", cx, cy)
    return (f"1+{zoom - 1:.4f}*on/{span}", cx, cy)


def pan_expr(motion: str, frames: int, pan_range: float) -> tuple[str, str]:
    """(x, y) for a crop-filter pan across an oversized source.

    The window travels `pan_range` of the available slack, centered on the
    photo, so a pan samples the middle of the room rather than swinging from
    one wall to the other.
    """
    span = max(frames - 1, 1)
    r = max(0.0, min(1.0, pan_range))
    start = (1.0 - r) / 2.0
    fwd = f"({start:.4f}+{r:.4f}*n/{span})"
    rev = f"({start:.4f}+{r:.4f}*(1-n/{span}))"
    cx, cy = "(in_w-out_w)/2", "(in_h-out_h)/2"

    if motion == "pan_right":
        return (f"(in_w-out_w)*{fwd}", cy)
    if motion == "pan_left":
        return (f"(in_w-out_w)*{rev}", cy)
    if motion == "pan_down":
        return (cx, f"(in_h-out_h)*{fwd}")
    return (cx, f"(in_h-out_h)*{rev}")  # pan_up


# ---------------------------------------------------------------------------
# Planning
# ---------------------------------------------------------------------------

@dataclass
class Shot:
    path: str
    treatment: str   # "crop" = full-bleed, "blur" = photo on a blurred fill
    motion: str
    seconds: float


def panel_size(args) -> tuple[int, int]:
    """Where the photos render. Split mode keeps the bottom half black for a
    green-screen talking head, so photos only get the top 1080x960."""
    return (W, H // 2) if args.layout == "split" else (W, H)


def choose_motion(index: int, treatment: str, aspect: float, panel_aspect: float) -> str:
    """Rotate through moves so no two neighbors drift the same way.

    Which pans are even available depends on how the photo's shape compares to
    the panel's. Wider than the panel means horizontal slack to pan across;
    taller means vertical slack; a near match only has room to zoom. A photo on
    the blurred fill has no slack at all, so it only zooms.
    """
    if treatment == "blur":
        return ("push", "pull")[index % 2]
    if aspect > panel_aspect * 1.05:
        return ("pan_right", "push", "pan_left", "pull")[index % 4]
    if aspect < panel_aspect / 1.05:
        return ("push", "pan_down", "pull", "pan_up")[index % 4]
    return ("push", "pull")[index % 2]


def build_shots(args) -> list[Shot]:
    pw, ph = panel_size(args)
    panel_aspect = pw / ph
    split = args.layout == "split"

    if args.manifest:
        raw = json.loads(Path(args.manifest).read_text())
        entries = raw["photos"] if isinstance(raw, dict) else raw
        shots = []
        for i, e in enumerate(entries):
            if isinstance(e, str):
                e = {"path": e}
            path = os.path.expanduser(e["path"])
            if not os.path.exists(path):
                raise SystemExit(f"Photo not found: {path}")
            w, h = probe_size(path)
            treatment = "crop" if split else (e.get("treatment") or "crop")
            shots.append(Shot(
                path=path,
                treatment=treatment,
                motion=e.get("motion") or choose_motion(i, treatment, w / h, panel_aspect),
                seconds=float(e.get("seconds") or args.seconds),
            ))
        return shots

    paths = [os.path.expanduser(p) for p in args.photos]
    for p in paths:
        if not os.path.exists(p):
            raise SystemExit(f"Photo not found: {p}")
    if not paths:
        raise SystemExit("No photos given. Pass --photos or --manifest.")

    shots = []
    for i, p in enumerate(paths):
        w, h = probe_size(p)
        aspect = w / h
        if split:
            # A 3:2 photo in a 9:8 panel keeps 75% of its width full-bleed, so
            # the blurred-fill workaround has nothing left to solve.
            treatment = "crop"
        elif args.fit != "auto":
            treatment = args.fit
        else:
            # Full-bleed is the better-looking default: it fills the phone and
            # a sideways pan still shows the whole room over the clip. Two
            # exceptions get the blurred fill instead. Anything ultra-wide,
            # where even a panning crop would never show the space as one
            # image; and every `blur_every`-th shot, purely for rhythm, so a
            # ten-shot reel isn't ten identical full-bleed pushes.
            wide = aspect >= args.blur_min_aspect
            rhythm = args.blur_every > 0 and i > 0 and i % args.blur_every == 0
            treatment = "blur" if (wide or rhythm) else "crop"
        # Forcing the hero to a push consumes the first slot of the rotation,
        # so offset everything after it or shot two repeats the same move.
        slot = i + 1 if args.hero_push and i > 0 else i
        shots.append(Shot(p, treatment, choose_motion(slot, treatment, aspect, panel_aspect),
                          args.seconds))

    # Open on the hero with a slow push. It's the shot people judge in half a second.
    if shots and args.hero_push:
        if args.fit == "auto" or split:
            shots[0].treatment = "crop"
        shots[0].motion = "push"
    return shots


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_clip(shot: Shot, index: int, tmp: Path, args) -> Path:
    frames = max(int(round(shot.seconds * FPS)), 2)
    out = tmp / f"clip_{index:03d}.mp4"
    pw, ph = panel_size(args)
    bw, bh = pw * UPSCALE, ph * UPSCALE
    pad = black_pad(args)

    if shot.treatment == "crop" and shot.motion in PANS:
        # Cover the panel at 4x, then slide a panel-shaped window across the
        # oversized source. Unlike zoompan this keeps the window's aspect
        # fixed, so the photo never stretches while it travels.
        x, y = pan_expr(shot.motion, frames, args.pan_range)
        vf = (
            f"scale={bw}:{bh}:force_original_aspect_ratio=increase:flags=lanczos,"
            f"crop=w={bw}:h={bh}:x='{x}':y='{y}',"
            f"scale={pw}:{ph}:flags=lanczos,{pad}{OUT}"
        )
        filter_flag = "-vf"

    elif shot.treatment == "crop":
        z, x, y = zoom_expr(shot.motion, frames, args.zoom)
        vf = (
            f"scale={bw}:{bh}:force_original_aspect_ratio=increase:flags=lanczos,"
            f"crop={bw}:{bh},"
            f"zoompan=z='{z}':x='{x}':y='{y}':d=1:s={pw}x{ph}:fps={FPS},{pad}{OUT}"
        )
        filter_flag = "-vf"

    else:
        # Not a letterboxed photo floating in the middle. A 3:2 shot pillared
        # into 9:16 fills barely 40% of the screen and reads small and smeary.
        # Instead crop to a tall-but-not-extreme 4:5 card, which still keeps
        # ~83% of the room's width, and sit that on the blurred fill.
        fg_w = W
        fg_h = even(fg_w / args.blur_aspect)
        y_off = max(SAFE_TOP - 40, (H - fg_h) // 2 - 35)

        z, x, y = zoom_expr(shot.motion, frames, args.zoom)
        bz, bx, by = zoom_expr("push", frames, 1.06)
        vf = (
            f"[0:v]split=2[bg][fg];"
            f"[bg]scale={W * 2}:{H * 2}:force_original_aspect_ratio=increase:flags=lanczos,"
            f"crop={W * 2}:{H * 2},"
            f"zoompan=z='{bz}':x='{bx}':y='{by}':d=1:s={W}x{H}:fps={FPS},"
            f"boxblur=34:2,eq=brightness=-0.24:saturation=0.5[bgv];"
            f"[fg]scale={fg_w * UPSCALE}:{fg_h * UPSCALE}:force_original_aspect_ratio=increase:flags=lanczos,"
            f"crop={fg_w * UPSCALE}:{fg_h * UPSCALE},"
            f"zoompan=z='{z}':x='{x}':y='{y}':d=1:s={fg_w}x{fg_h}:fps={FPS}[fgv];"
            f"[bgv][fgv]overlay=x=(W-w)/2:y={y_off},{OUT}"
        )
        filter_flag = "-filter_complex"

    run(["ffmpeg", "-y", "-loop", "1", "-framerate", str(FPS), "-i", shot.path,
         filter_flag, vf, "-frames:v", str(frames), "-r", str(FPS),
         "-c:v", "libx264", "-preset", "medium", "-crf", "18",
         "-pix_fmt", "yuv420p", str(out)])
    return out


def stitch(clips: list[Path], durations: list[float], out_path: Path,
           transition: str, xfade_seconds: float) -> None:
    """Join the clips, then mux in silent audio.

    Reels handles a video-only MP4 inconsistently, so every export carries a
    real (silent) AAC track.
    """
    tmp = out_path.parent / f".{out_path.stem}.video.mp4"

    if transition == "cut" or len(clips) == 1:
        listfile = out_path.parent / f".{out_path.stem}.concat.txt"
        listfile.write_text("".join(f"file '{c.as_posix()}'\n" for c in clips))
        run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(listfile),
             "-c", "copy", str(tmp)])
        listfile.unlink(missing_ok=True)
    else:
        t = xfade_seconds
        inputs = []
        for c in clips:
            inputs += ["-i", str(c)]
        # Each xfade overlaps its pair by t, so every join pulls the timeline
        # back by t. Offset is "everything joined so far, minus the overlaps".
        chain, prev, elapsed = [], "[0:v]", durations[0]
        for i in range(1, len(clips)):
            label = f"[v{i}]"
            chain.append(f"{prev}[{i}:v]xfade=transition={transition}:"
                         f"duration={t}:offset={elapsed - t:.4f}{label}")
            prev = label
            elapsed = elapsed - t + durations[i]
        run(["ffmpeg", "-y", *inputs, "-filter_complex", ";".join(chain),
             "-map", prev, "-r", str(FPS),
             "-c:v", "libx264", "-preset", "medium", "-crf", "18",
             "-pix_fmt", "yuv420p", str(tmp)])

    run(["ffmpeg", "-y", "-i", str(tmp),
         "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-shortest",
         "-movflags", "+faststart", str(out_path)])
    tmp.unlink(missing_ok=True)


# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="Render a 9:16 listing reel from photos.")
    ap.add_argument("--photos", nargs="*", default=[],
                    help="Ordered photo paths (8-10 is the sweet spot)")
    ap.add_argument("--manifest", help="JSON with per-photo treatment/motion/seconds")
    ap.add_argument("--out", required=True, help="Output .mp4 path")
    ap.add_argument("--seconds", type=float, default=2.6, help="Seconds per photo")
    ap.add_argument("--zoom", type=float, default=1.12, help="Push/pull extent")
    ap.add_argument("--layout", choices=("split", "full"), default="split",
                    help="split = photos top half, black bottom half for green screen (default)")
    ap.add_argument("--pan-range", type=float, default=None,
                    help="Fraction of available travel a pan covers (default 0.8 split, 0.5 full)")
    ap.add_argument("--fit", choices=("auto", "crop", "blur"), default="auto")
    ap.add_argument("--blur-min-aspect", type=float, default=2.0,
                    help="Photos wider than this always get the blurred fill")
    ap.add_argument("--blur-every", type=int, default=3,
                    help="Every Nth shot uses the blurred fill for rhythm (0 disables)")
    ap.add_argument("--blur-aspect", type=float, default=0.8,
                    help="Aspect of the card on the blurred fill (default 0.8 = 4:5)")
    ap.add_argument("--transition", default="fade", help="xfade name, or 'cut'")
    ap.add_argument("--xfade-seconds", type=float, default=0.35)
    ap.add_argument("--hero-push", action="store_true", default=True)
    ap.add_argument("--no-hero-push", dest="hero_push", action="store_false")
    ap.add_argument("--dry-run", action="store_true", help="Print the plan, render nothing")
    args = ap.parse_args()

    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            raise SystemExit(f"{tool} not found. Install with: brew install ffmpeg")

    shots = build_shots(args)

    if args.pan_range is None:
        # The split panel is only 9:8, so a 3:2 photo has far less sideways
        # slack than it does in full 9:16. Use more of it or pans barely move.
        args.pan_range = 0.8 if args.layout == "split" else 0.5

    total = sum(s.seconds for s in shots)
    joins = len(shots) - 1
    if args.transition != "cut":
        total -= max(joins, 0) * args.xfade_seconds

    print(f"{len(shots)} photos  ·  {total:.1f}s  ·  {W}x{H} @ {FPS}fps")
    for i, s in enumerate(shots, 1):
        print(f"  {i:2}. {s.treatment:5} {s.motion:9} {s.seconds:.1f}s  {Path(s.path).name}")
    if args.dry_run:
        return

    out_path = Path(os.path.expanduser(args.out)).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="listing-video-") as td:
        tmp = Path(td)
        clips, durations = [], []
        for i, shot in enumerate(shots):
            print(f"  rendering {i + 1}/{len(shots)}...", flush=True)
            clips.append(render_clip(shot, i, tmp, args))
            durations.append(shot.seconds)
        print("  stitching...", flush=True)
        stitch(clips, durations, out_path, args.transition, args.xfade_seconds)

    print(f"\n{out_path}  ({out_path.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
