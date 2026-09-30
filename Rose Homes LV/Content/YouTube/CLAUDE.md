# CLAUDE.md — YouTube Video Domain

This folder holds long-form YouTube video output for Ryan Rose's channel. Read this before doing work inside `YouTube/`.

## What lives here

Two skills write into this folder:

1. **`/yt-long <topic>`** (the `yt-long` skill at `~/.claude/skills/yt-long/`) produces 5 to 15 minute long-form videos on any topic. Each run creates a topic folder with research, a teleprompter script, a QA fact-check report, a YouTube description and SEO package, and a HyperFrames graphics shot list. This is the primary producer of content here.
2. **`/youtube-manager`** produces weekly MLS market-update packages in dated folders (e.g. `[YYYY-MM-DD] Weekly Package/`). That is a separate, real-estate-specific weekly flow. Do not confuse the two.

One skill publishes from here:

3. **`/yt-shorts-publish [path]`** (`~/.claude/skills/yt-shorts-publish/`) takes a folder or file of Shorts titles/descriptions/tags, normalizes them, writes a `schedule.md` next to the source from the publish times Ryan gives, then fills and schedules each already-uploaded draft in YouTube Studio through claude-in-chrome. Ryan uploads the MP4s himself; filename is the join key.

## Output layout (`/yt-long`)

Single video:
```
YouTube/<topic-slug>/
  research-report.md      research with sourced facts
  script.md               word-for-word teleprompter script with graphics cues
  qa-report.md            fact-check, ends in PASS or FAIL
  description.md          5 titles + recommended, description, chapters, tags, thumbnail text
  hyperframes-prompt.md   detailed prompt to paste into a separate session to build the graphics
  summary.md              package summary + next steps
```

Series or batch:
```
YouTube/<topic-slug>/
  series-plan.md          the episode arc (series) or angle list (batch)
  summary.md              top-level summary across episodes
  01-<episode-slug>/      one folder per episode, same files as a single video
  02-<episode-slug>/
  ...
```

## How videos are made

The production model is a **graphics package**, not a full machine render. Ryan films himself on camera reading `script.md` from a teleprompter. The graphics (intro, lower-thirds, stat and quote cards, charts, B-roll motion graphics, transitions, outro and CTA) get cut into his footage.

This skill does not build the graphics. It writes `hyperframes-prompt.md`, a detailed, self-contained prompt. Ryan opens a separate Claude Code session (one with the HyperFrames skills) and pastes that prompt in. That session scaffolds the project inside the student kit at `/Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/video-projects/ytlong-<slug>/` (so the CLI, registry blocks, brand assets, and preview server all work), builds the elements, honors the live-preview and visual-verification gates, and renders. Captions are best generated from the real recorded audio after filming.

## Content rules (inherited)

All content follows `~/.claude/skills/yt-long/content-rules.md` and the workspace root `CLAUDE.md`:

- **No em-dashes.** Commas, periods, or "and."
- **Factual only.** Every spoken claim is sourced and QA-verified. Gaps are marked `NOT FOUND`, never guessed.
- **6th grade reading level, warm and conversational.** Soft CTAs, never salesy.
- **Local info wins** when the topic is Las Vegas, Henderson, or Clark County.
- **Ryan Rose:** Real Broker, LLC | 702-747-5921 | ryan@rosehomeslv.com | rosehomeslv.com

## Channel intro (post-hook)

The intro that plays after Ryan's cold-open hook on every long-form upload lives in
`SKOOL Community/hyperframes-student-kit/video-projects/rose-homes-yt-intro/renders/`:
`rose-homes-yt-intro.mp4` (7.5s), `rose-homes-yt-intro-10s.mp4`, `rose-homes-yt-intro-15s.mp4`
(15s adds Summerlin / Southwest / Henderson / Spring Valley cards to the flurry)
(built 2026-09-28 with HyperFrames + the motion-showreel skill, Vector palette). YouTube only.
