# Build pipeline (what build.py does, and why)

Reference: `SKOOL Community/Scripts/Shorts-Build/weekly-seller-update/build.py`. Copy it, edit the top half.

## What to edit per video

| Name | What |
|---|---|
| `CAM`, `SCR` | source paths (SCR by glob) |
| `OFF` | `{"scr1": 49.52}` from offset.py (cam time minus screen time) |
| crop boxes | `(w, h, x, y)` on the screen recording, **1.08 aspect** so it scales to 1080x1000. WSU on a 3024x1964 screen: REPORT (1862,1724,380,240), PLAN (1800,1667,1224,100), PROMPT (1800,1667,870,297), LOFTY (1800,1667,612,150). Find new boxes by pulling a frame and looking. |
| `CLIPS` | `n: (output name, [segments])`. Segment = `(cam_in, cam_out, layout)`. Layout `None` = face only, or `(screen_key, "sync" or fixed screen seconds, crop)`. |
| `FIX` | whisper mishears for captions: school→Skool, cloud/claw/claude→Claude, clawcode→Claude Code, formosie→Hormozi, surhan→Serhant, mac→Mack, crm→CRM. |

Clip boundaries use spoken phrases, not raw numbers: `start("so here it just has", 137)` finds the phrase nearest 137s. `end()` caps the last word at 0.8s + 0.3s because whisper stretches a last word across the silence after it.

Fixed screen time (not "sync") = B-roll. Use it when the synced screen shows private info or jumps around.

## Layout

- Split: screen on top 1080x1000, face below `crop=1268:1080:326:0,scale=1080:920`. Captions at y 1000 (the seam).
- Face only: `crop=608:1080:656:0,scale=1080:1920`. Captions at y 1480.
- Face crops assume a 1920x1080 camera with Ryan centered. Check a frame if the framing differs.
- A screen crop that is mostly empty space: make that clip face only.

## Traps already solved in build.py (do not undo)

- **VFR screen recordings** write no frames while the screen is still, so a seek lands blank. Seek up to 30s early, then `fps=30,trim=start=<pre>:duration=<d>,setpts=PTS-STARTPTS`.
- **Join with the concat filter**, never the concat demuxer: the demuxer drifted audio by 11s.
- **Captions**: build.py writes 3-word states (active word in `<b>`), caps.mjs renders transparent PNGs (Barlow 800, 84px, uppercase, white, 14px black stroke, active word #5B9BFF), then an ffconcat image track is overlaid with `format=rgba ... overlay=0:0:eof_action=pass`.
- **Loudness**: `loudnorm=I=-14:TP=-1.5:LRA=11`, aac 48k stereo.
- **Bumper**: 3s silent `bumper-9x16.mp4`, concatenated with a 3s `anullsrc` track. Final encode x264 crf 18, yuv420p, `+faststart`.
- Temp files go to `<slug>/tmp/` (delete after QA).

## QA commands

```bash
# durations must match
for f in "SKOOL Community/Final Videos/<Series>-Reel-"*.mp4; do ffprobe -v error -show_entries stream=codec_type,duration -of csv=p=0 "$f"; done
# 6-frame strip of one reel
ffmpeg -v error -y -i reel.mp4 -vf "fps=1/8,scale=270:-1,tile=6x1" -frames:v 1 -update 1 strip.png
```

Multi-arg shell loops: zsh does not word-split `"6675 5"`, loop in python instead.
SendUserFile caps at 30MB, so full reels cannot be sent to Ryan's phone; send a strip or cover instead.

Not this: `_System/tools/longform-to-shorts/` is an older generic cutter (single source, no screen sync, no Leveraged Agent captions/bumper). The Sept 2026 batches used build.py above.
