#!/usr/bin/env python3
"""Screen-demo short: dark canvas + small crisp webcam PIP + screen panel + captions.

Use when the screen content is the payoff. The screen is cropped at close to
native resolution so UI text stays readable; the webcam sits small on top rather
than being upscaled.

    python3 render_screen_clip.py SRC.mov CAPDIR OUT.mp4 T0 T1 [SCREEN_CROP] [PIP_CROP]

Pick SCREEN_CROP by sampling frames across the window first — panel layout
shifts when panes are resized, and a crop that is clean at T0 may not be at T1.
"""
import json, subprocess, sys

if len(sys.argv) < 6:
    sys.exit(__doc__)

src, capdir, out = sys.argv[1], sys.argv[2], sys.argv[3]
t0, t1 = float(sys.argv[4]), float(sys.argv[5])
screen_crop = sys.argv[6] if len(sys.argv) > 6 else "920:767:1000:150"
pip_crop = sys.argv[7] if len(sys.argv) > 7 else "353:425:30:622"

ov = json.load(open(capdir + "/overlay.json"))

cmd = ["ffmpeg", "-v", "error", "-stats", "-ss", str(t0), "-to", str(t1), "-i", src]
for p in ov["pngs"]:
    cmd += ["-i", p]

stages = [
    # the canvas needs an explicit duration or the overlay chain never ends
    "color=c=0x0F0F11:s=1080x1920:r=30:d=%.2f[bg]" % (t1 - t0),
    "[0:v]crop=%s,scale=1080:900:flags=lanczos,fps=30[scr]" % screen_crop,
    "[0:v]crop=%s,scale=300:361:flags=lanczos,fps=30[pip]" % pip_crop,
    "[bg][scr]overlay=0:410[s1]",
    "[s1][pip]overlay=390:25,format=rgba[base]",
    ov["graph"],
    ov["last"] + "format=yuv420p[vout]",
]

cmd += [
    "-filter_complex", ";".join(stages),
    "-map", "[vout]", "-map", "0:a:0",
    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
    "-c:v", "libx264", "-preset", "medium", "-crf", "20",
    "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.1",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    "-movflags", "+faststart", out, "-y",
]
print("screen-demo clip, %d captions -> %s" % (ov["count"], out))
sys.exit(subprocess.call(cmd))
