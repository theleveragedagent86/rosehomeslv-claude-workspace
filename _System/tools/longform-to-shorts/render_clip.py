#!/usr/bin/env python3
"""Talking-head short: trim -> crop to 9:16 -> burn captions -> normalize audio.

Use when the source frame is a full-screen camera shot.

    python3 render_clip.py SRC.mov CAPDIR OUT.mp4 T0 T1 [CROP]

CROP is an ffmpeg crop spec "w:h:x:y" against the source frame. Default assumes
a 1920x1080 source and takes a full-height 9:16 slice near centre.
"""
import json, subprocess, sys

if len(sys.argv) < 6:
    sys.exit(__doc__)

src, capdir, out = sys.argv[1], sys.argv[2], sys.argv[3]
t0, t1 = float(sys.argv[4]), float(sys.argv[5])
crop = sys.argv[6] if len(sys.argv) > 6 else "608:1080:643:0"

ov = json.load(open(capdir + "/overlay.json"))

cmd = ["ffmpeg", "-v", "error", "-stats", "-ss", str(t0), "-to", str(t1), "-i", src]
for p in ov["pngs"]:
    cmd += ["-i", p]

stages = [
    "[0:v]crop=%s,scale=1080:1920:flags=lanczos,fps=30,format=rgba[base]" % crop,
    ov["graph"],
    ov["last"] + "format=yuv420p[vout]",
]

cmd += [
    "-filter_complex", ";".join(stages),
    "-map", "[vout]", "-map", "0:a:0",
    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
    "-c:v", "libx264", "-preset", "medium", "-crf", "21",
    "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.1",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    "-movflags", "+faststart", out, "-y",
]
print("talking-head clip, %d captions -> %s" % (ov["count"], out))
sys.exit(subprocess.call(cmd))
