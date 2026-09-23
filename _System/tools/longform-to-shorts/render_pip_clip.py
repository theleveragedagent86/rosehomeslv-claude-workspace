#!/usr/bin/env python3
"""PIP-hero short: dark canvas + enlarged webcam PIP + captions.

Use for stretches of a screen recording where the screen shows nothing worth
watching, so the webcam has to carry the clip alone. The PIP is small in the
source, so this upscales it; expect it to look softer than a true camera clip.

    python3 render_pip_clip.py SRC.mov CAPDIR OUT.mp4 T0 T1 [PIP_CROP]
"""
import json, subprocess, sys

if len(sys.argv) < 6:
    sys.exit(__doc__)

src, capdir, out = sys.argv[1], sys.argv[2], sys.argv[3]
t0, t1 = float(sys.argv[4]), float(sys.argv[5])
pip_crop = sys.argv[6] if len(sys.argv) > 6 else "316:394:46:645"

PIP_W, PIP_H = 830, 1035   # ~2.6x upscale of a ~316px-wide source PIP

ov = json.load(open(capdir + "/overlay.json"))

cmd = ["ffmpeg", "-v", "error", "-stats", "-ss", str(t0), "-to", str(t1), "-i", src]
for p in ov["pngs"]:
    cmd += ["-i", p]

stages = [
    # the canvas needs an explicit duration or the overlay chain never ends
    "color=c=0x0F0F11:s=1080x1920:r=30:d=%.2f[bg]" % (t1 - t0),
    "[0:v]crop=%s,scale=%d:%d:flags=lanczos,fps=30[pip]" % (pip_crop, PIP_W, PIP_H),
    "[bg][pip]overlay=%d:240,format=rgba[base]" % ((1080 - PIP_W) // 2),
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
print("pip-hero clip, %d captions -> %s" % (ov["count"], out))
sys.exit(subprocess.call(cmd))
