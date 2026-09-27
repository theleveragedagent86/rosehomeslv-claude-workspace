---
name: skool-reels
description: Use when Ryan wants a Leveraged Agent long-form video (Skool lesson / YouTube walkthrough recording) cut into vertical Reels/Shorts, e.g. "make reels from my long form", "clip this into shorts", "turn the <topic> video into reels". Produces the MP4s (screen over face, word captions, bumper), standalone covers (9:16 + 16:9), long IG captions, YouTube Shorts metadata and a posting schedule. The Leveraged Agent only, never Rose Homes LV. Hands off to /skool-shorts-schedule.
argument-hint: "topic name and/or paths to the raw camera + screen recordings"
---

# /skool-reels: long-form recording to a full Reels/Shorts batch

Reference build (copy it, do not start from scratch):
`/Users/ryanrose/Downloads/Claude/SKOOL Community/Scripts/Shorts-Build/weekly-seller-update/`
(build.py, caps.mjs, words.json, README.md). Second example: `open-house-lead-automation/` (face-only set).

```
/skool-reels (this)  ->  /skool-shorts-schedule
```

## Paths

| What | Where |
|---|---|
| Build root | `SKOOL Community/Scripts/Shorts-Build/<slug>/` |
| Output MP4s | `SKOOL Community/Final Videos/<Series>-Reel-NN-<Hook-Words>.mp4` (git-ignored) |
| Bumper | `SKOOL Community/Brandkit/YouTube-Bumpers/renders/bumper-9x16.mp4` (3s, silent) |
| Fonts | `SKOOL Community/Brandkit/Design-System/fonts/fonts.css` |
| Cover template | `Shorts-Build/reel-covers/` (cover.html SETS + shoot.mjs DIRS) |
| IG captions | `SKOOL Community/Scripts/<Series>-Instagram-Reel-Captions.md` |
| YT metadata | `Shorts-Build/YOUTUBE-SHORTS-METADATA.md`, `yt_manifest.json` |
| Schedule | `Shorts-Build/POSTING-SCHEDULE.md` |
| Helpers | `scripts/transcribe.py`, `scripts/offset.py` (this skill) |

Environment: ffmpeg has **no drawtext/libass** (captions are PNG overlays), python is **stdlib only** (no numpy/PIL), Playwright comes from `SKOOL Community/hyperframes-student-kit/node_modules/playwright`, whisper-cli is in `/opt/homebrew/bin`. `sleep` is blocked, use background runs.

## Step 1: Find the RAW sources (not the edited long form)

Ask Ryan for the camera file and screen recordings if not given. Usual spots: `~/Downloads/IMG_*.MOV` + `~/Downloads/Screen Recording <date>*.mov`, or inside a Final Cut library at `~/Movies/*.fcpbundle/*/Original Media/`. Screen recording names hide a U+202F before "AM": always glob (`Screen*9.08.47*`), never type the name. ffprobe each file (size, fps, duration). Screen recordings are VFR.

## Step 2: Transcribe and sync

```bash
python3 ~/.claude/skills/skool-reels/scripts/transcribe.py "<build>/<slug>" cam=<camera> scr1="<glob>" scr2="<glob>"
python3 ~/.claude/skills/skool-reels/scripts/offset.py "<build>/<slug>/words.json" cam scr1 scr2
```

Writes `words.json` (`{"key":[[from,to,"word"],...]}`) and readable `<key>.txt` dumps. Run in the background for long files. offset.py prints cam minus screen seconds (median of matching 6-word runs); fewer than ~5 matches means sync by eye. Delete the `.txt` and whisper `.json` dumps after the build if not needed.

## Step 3: Cut list, approved before building (gate)

Read the cam dump end to end. Pick **as many clips as the video genuinely supports** (5 is not a cap). Each clip:
- One idea, a hook in the first 3 seconds, 33 to 67s. Multi-segment joins are fine.
- Ryan's real on-camera words only, never unrecorded scripts.
- Named after its own hook (`Reel-04-Youre-Using-AI-Backwards`), never template labels (Teaser, Quick Win, Before/After, Hot Take, Promise).

Show Ryan a table (#, hook title, cam timestamps, length, layout) and get a yes.

## Step 4: Build

Copy the reference `build.py` + `caps.mjs` into `<slug>/`, then edit only: source paths, `OFF`, crop boxes, `CLIPS`, `FIX`. Details and the traps it already solves: [references/build-pipeline.md](references/build-pipeline.md).

`python3 build.py` (all) or `python3 build.py 3 7`. Output lands in `Final Videos/`.

## Step 5: Privacy pass (gate, every build)

No offer amounts, buyer or prospect names, visitor names/phones, seller contact info, or the Plan Mode prompt, on screen **or** spoken.
1. Contact sheet of every screen segment: `ffmpeg -i reel.mp4 -vf "fps=1/3,crop=1080:1000:0:0,scale=360:-1,tile=6x4" -frames:v 1 -update 1 sheet.png`, then Read it.
2. Re-transcribe each output MP4 and grep for names/numbers.
3. Fix: swap the segment to unsynced B-roll (fixed screen time), go face-only, or cut the word at hard timestamps. Rebuild, re-check.

## Step 6: QA

ffprobe every output: video and audio durations match (within 0.1s), 1080x1920, 30fps. Tile 6 frames per reel and look at them. Check caption spelling (Skool, Claude, Claude Code).

## Step 7: Covers

Add a set to `SETS` in `reel-covers/cover.html` (titles, accent word in `<em>`, one subline) and to `DIRS` in `shoot.mjs`. Each series gets a fixed color (existing: wsu black, oh white) so interleaved posting alternates the grid; pick the color that keeps the alternation. Then:
```bash
node "SKOOL Community/Scripts/Shorts-Build/reel-covers/shoot.mjs" <set>          # 9:16, IG + YouTube Shorts
node "SKOOL Community/Scripts/Shorts-Build/reel-covers/shoot.mjs" <set> --16x9   # 1280x720
```
Covers are standalone title graphics, never video frames. Read 2 or 3 PNGs before moving on.

## Step 8: Copy

Formats in [references/copy-formats.md](references/copy-formats.md):
- **IG captions** `.md`: 250 to 400 words each, local-news format. Subagents in parallel are fine, then read every one.
- **YouTube Shorts metadata**: title (45 chars or fewer), description + fixed footer, one tag block per series under 500 chars (print the count). Append to `YOUTUBE-SHORTS-METADATA.md` and regenerate `yt_manifest.json`.
- **Posting schedule**: interleave with any series already queued. Get Ryan's yes on the table.

Rules for all copy: no em dashes, only numbers said on camera or in the real source, Plan Mode prompt never given away or linked, no Rose Homes LV contact block, no ManyChat keyword unless Ryan asks.

## Step 9: Docs and hand-off

- Write `<slug>/README.md` (clip table with cam times, layout, privacy notes, rebuild command), matching the reference README.
- Update the Folder Map in `SKOOL Community/CLAUDE.md`.
- Report (extremely concise): reel count, lengths, file paths, privacy fixes made. Offer `/skool-shorts-schedule`.
- Commit only if asked.
