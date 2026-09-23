---
name: yt-shorts-publish
description: Use when Ryan asks to publish, schedule, or fill in the titles/descriptions/tags on his Rose Homes LV realtor YouTube Shorts drafts, schedule a batch of Shorts, or "do the YouTube Shorts metadata". Realtor channel only (not Codename History, use /codename-history publish for that).
argument-hint: "path to the Shorts metadata folder/file, optional. Add 'plan' to build the schedule file without touching YouTube."
---

# /yt-shorts-publish - Rose Homes LV YouTube Shorts metadata + scheduling

You fill in and schedule Ryan's already-uploaded YouTube Shorts drafts on the **Rose Homes LV realtor channel**. Ryan uploads the MP4s to YouTube Studio as drafts himself (the skill cannot upload video, see `references/publish-automation.md`). You do the rest: title, description, tags, audience, AI disclosure, and a scheduled publish time per Short.

Modeled on Phase B of `/codename-history`, adapted for the real-estate channel. Workspace content rules apply: no em-dashes, factual only, warm 6th-grade voice, soft CTAs, Ryan's contact block.

## Inputs you must have before doing anything

1. **Where the metadata lives.** If `$ARGUMENTS` does not contain a path, **ask Ryan** (AskUserQuestion, free text via "Other" is fine): "Where are the Shorts titles/descriptions? Give me a folder or file path." Accept any of:
   - a folder of per-Short `.md` files (one file per Short)
   - one `.md` / `.txt` with several Shorts separated by headings
   - a `.csv` / `.xlsx` with columns like filename, title, description, tags
   - a `/yt-long` or `/local-news` output folder (look for `description.md`, `shorts/`, `seo-*.md`)
   Do not guess a folder. If the path does not exist, ask again.
2. **The schedule.** Ryan gives the times. Before assigning slots, read the Shorts list in YouTube Studio: skip any Short already Public, keep any already Scheduled at its existing slot, and never double-book a slot that already has a Short. After parsing, **ask** for: first publish date, cadence (e.g. daily, Mon/Wed/Fri, 2 per day), publish time(s), timezone (default **America/Los_Angeles**, Las Vegas). Never invent a schedule. If he gives a single sentence like "one a day at 9am starting Monday", expand that yourself and show him the table for a yes.

## Workflow

### Step 1 - Parse and normalize (no browser yet)

Read every source file. Build one row per Short with: `filename` (the MP4 name, this is the join key to the YouTube draft), `title`, `description`, `tags`, `hashtags`, `source_file`.

Normalize each row per `references/metadata-format.md`:
- Title ≤ 100 chars (aim ≤ 60), no em-dashes, no ALL CAPS, one hook, Las Vegas / neighborhood name when relevant.
- Description: 2-line hook, 1-3 short paragraphs, footer block with Ryan's contact, then hashtags. `#Shorts` is always included.
- Tags: parse them from the source for the record, but they are NOT written to YouTube (see Step 3).
- Missing title/description/tags: write them from the Short's script or transcript if one is in the folder. If there is nothing to write from, list the gaps and ask Ryan rather than making up facts.
- Strip any em-dash the source still has. Never leave one in.

### Step 2 - Build the schedule and confirm

Write `schedule.md` **next to the source metadata** (or in the folder Ryan names) using the table in `references/metadata-format.md` (`#`, filename, title, publish date, time, tz, status). Status starts as `pending`.

Show Ryan the table and get an explicit **yes** before touching YouTube. If `$ARGUMENTS` contains `plan`, stop here and report the file path.

### Step 3 - Fill and schedule in YouTube Studio

Follow `references/publish-automation.md` exactly, using **claude-in-chrome** (computer-use only has read tier on browsers). For each `pending` row:
1. Open YouTube Studio > Content > filter Shorts / drafts, find the draft by **filename**.
2. Details: title and description. **Do NOT touch tags.** Ryan's upload template auto-fills tags and he wants them left as-is (his call, 2026-09-01). Verify field-scoped focus before any `cmd+a`. Read each value back.
3. Audience: **"No, it's not made for kids"**. Always.
4. AI-content disclosure: **"No"** unless the batch uses an AI voice clone or an AI-generated likeness of Ryan. Ask Ryan **once per batch** if the source folder does not make that obvious, then apply the same answer to every Short.
4b. **Related video**: set it on every Short to the current week's long-form "Las Vegas News <date> | ..." video (the newest one on the channel). Ask Ryan which one if more than one candidate exists, then reuse the answer for the whole batch. Record it in `schedule.md`.
5. Visibility > **Schedule** > set the row's date + time > Schedule. Confirm the "Scheduled" state on screen.
6. Update that row in `schedule.md` to `scheduled` with the video link. Save after every Short so a crash resumes cleanly.

If a draft cannot be found by filename, mark the row `no-draft` and keep going. Never publish anything as Public unless Ryan explicitly said Public.

### Step 4 - Report

One table: filename, final title, scheduled date/time, link, status. Then list any `no-draft` or `needs-input` rows. Keep it short.

## Guardrails

- **No em-dashes** anywhere. Use commas, periods, or "and".
- **Factual only.** No invented prices, rates, school ratings, or program details. If the source is thin, keep the description general.
- **Contact block** is fixed: Ryan Rose | Real Broker, LLC | 702-747-5921 | ryan@rosehomeslv.com | rosehomeslv.com. Blog links use `/blog/<slug>` (singular).
- **Ask, don't assume,** for the metadata path, the schedule, and the AI-disclosure answer.
- Do all metadata first; scheduling (the irreversible-ish step) last for each Short.
- Retry a failed Short twice, then move on and report it.
