#!/usr/bin/env python3
"""Render each caption line as a transparent PNG, and emit the ffmpeg overlay filtergraph.

Needed because this machine's ffmpeg is built without libass/freetype, so the
ass/subtitles/drawtext filters are unavailable.
"""
import json, os, sys, textwrap
from PIL import Image, ImageDraw, ImageFont

src, outdir, t0, t1 = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
BM_OVERRIDE = int(sys.argv[5]) if len(sys.argv) > 5 else None
os.makedirs(outdir, exist_ok=True)

W = 1080
FONT = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
SIZE = 62
STROKE = 9
MAX_CHARS = 22          # wrap width; keeps lines punchy
BOTTOM_MARGIN = 470     # px from frame bottom, clears the Reels UI

if BM_OVERRIDE:
    BOTTOM_MARGIN = BM_OVERRIDE
font = ImageFont.truetype(FONT, SIZE)
segs = json.load(open(src))["transcription"]

events = []
for s in segs:
    a, b = s["offsets"]["from"] / 1000.0, s["offsets"]["to"] / 1000.0
    if b <= t0 or a >= t1:
        continue
    txt = " ".join(s["text"].split()).upper()
    if not txt:
        continue
    a, b = max(a, t0) - t0, min(b, t1) - t0
    if b - a < 0.10:
        continue
    events.append((a, b, txt))

# merge very short fragments into the previous line so captions don't strobe
merged = []
for a, b, txt in events:
    if merged and (b - a) < 1.0 and len(merged[-1][2]) + len(txt) < 62:
        pa, pb, ptxt = merged[-1]
        merged[-1] = (pa, b, ptxt + " " + txt)
    else:
        merged.append((a, b, txt))

MAX_W = 960   # measured px; leaves a real margin inside the 1080 frame
_probe = Image.new("RGBA", (10, 10))
d0 = ImageDraw.Draw(_probe)


def wrap_to_width(txt, draw, font):
    """Greedy wrap on measured pixel width, not character count."""
    words, lines, cur = txt.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        bb = draw.textbbox((0, 0), trial, font=font, stroke_width=STROKE)
        if bb[2] - bb[0] > MAX_W and cur:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines or [txt]


paths = []
for i, (a, b, txt) in enumerate(merged):
    lines = wrap_to_width(txt, d0, font)
    lh = SIZE + 18
    h = lh * len(lines) + STROKE * 2 + 20
    img = Image.new("RGBA", (W, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for j, line in enumerate(lines):
        bbox = d.textbbox((0, 0), line, font=font, stroke_width=STROKE)
        x = (W - (bbox[2] - bbox[0])) // 2
        d.text((x, 10 + j * lh), line, font=font, fill=(255, 255, 255, 255),
               stroke_width=STROKE, stroke_fill=(0, 0, 0, 255))
    p = os.path.join(outdir, "cap_%03d.png" % i)
    img.save(p)
    paths.append((p, a, b, h))

# filtergraph: chain one timed overlay per caption
parts, cur = [], "[base]"
for i, (p, a, b, h) in enumerate(paths):
    nxt = "[v%d]" % i
    y = 1920 - BOTTOM_MARGIN - h
    parts.append("%s[%d:v]overlay=0:%d:enable='between(t,%.2f,%.2f)'%s"
                 % (cur, i + 1, y, a, b, nxt))
    cur = nxt
graph = ";".join(parts)

json.dump({"pngs": [p for p, _, _, _ in paths], "graph": graph, "last": cur,
           "count": len(paths)}, open(os.path.join(outdir, "overlay.json"), "w"))
print("rendered %d caption PNGs" % len(paths))
