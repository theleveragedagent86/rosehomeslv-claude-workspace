# longform-to-shorts

Cut vertical shorts (1080x1920, burned captions, normalized audio) out of a long
recording. Built for screen-recorded walkthroughs that mix full-camera talking
head with screen share.

This is **not** the same thing as the `claude-shorts` plugin. That one builds
teleprompter videos from scratch with HyperFrames/HTML. This one carves clips out
of footage that already exists.

## Why this exists rather than an off-the-shelf tool

Tested Kinocut (the "guardrailed video editing MCP for agents") on a 12-minute
walkthrough. Its `repurpose` command letterboxes 16:9 into black bars, ignores
its own `max_duration`, and has no clip selection at all. Its quality gate
reported `all_passed: True` with a 9.7/10 while every individual check failed.
Doing it directly with ffmpeg is faster and the output is actually usable.

## Requirements

- `ffmpeg` / `ffprobe`
- `whisper-cli` (brew `whisper-cpp`). Brew ships only test models; a real one is
  already downloaded at `~/.cache/whisper-models/ggml-base.en.bin` (kept outside
  the repo because it is 141 MB).
- Python 3 with Pillow

**Note:** the Homebrew ffmpeg on this machine is built without libass/freetype,
so the `ass`, `subtitles`, and `drawtext` filters do not exist. That is why
captions are rendered as PNGs and composited with `overlay`. If ffmpeg is ever
rebuilt with libass, a normal subtitle burn would be simpler.

## Pipeline

1. **Extract audio**

       ffmpeg -i SRC.mov -vn -ac 1 -ar 16000 -c:a pcm_s16le audio.wav

2. **Transcribe** (word-split segments, short lines)

       whisper-cli -m ~/.cache/whisper-models/ggml-base.en.bin \
         -f audio.wav -oj -ojf -of transcript -ml 42 -sow

3. **Choose clips.** Read the transcript and pick segments that stand alone and
   end on a clean beat. This is the judgment step; no tool does it well.

4. **Sample frames across each window** before choosing a crop. Panel layouts
   shift mid-clip, and stray hover tooltips show up in the recording.

       ffmpeg -ss T -i SRC.mov -frames:v 1 -vf "crop=W:H:X:Y,scale=540:-1" probe.jpg

5. **Render captions**

       python3 make_caption_pngs.py transcript.json CAPDIR T0 T1 [BOTTOM_MARGIN]

6. **Render the clip** with whichever layout fits:

   | Source looks like | Script |
   |---|---|
   | Full-screen camera | `render_clip.py` |
   | Screen share, screen matters | `render_screen_clip.py` |
   | Screen share, screen is idle | `render_pip_clip.py` |

       python3 render_clip.py SRC.mov CAPDIR out.mp4 0 31.92
       python3 render_screen_clip.py SRC.mov CAPDIR out.mp4 500.36 521.24 "705:588:1215:60"
       python3 render_pip_clip.py SRC.mov CAPDIR out.mp4 170.92 180.60

## Things worth knowing

- **The webcam PIP is small** (~350x400 in a 1920x1080 recording). Blowing it up
  to full width is a 3x upscale and looks bad. `render_pip_clip.py` caps at about
  2.6x, which is the most it takes before falling apart.
- **Captions wrap on measured pixel width**, not character count. Character
  wrapping ran lines edge to edge in Arial Black.
- **`color=` sources need an explicit duration.** Without `d=`, the overlay chain
  never terminates and ffmpeg renders forever.
- **Bottom margin** defaults to 470px to clear the Instagram Reels UI. Composed
  layouts pass 300 and make room above instead.
- Output is CRF 20-21. Instagram re-encodes anyway, so pushing quality higher
  mostly just costs file size.
