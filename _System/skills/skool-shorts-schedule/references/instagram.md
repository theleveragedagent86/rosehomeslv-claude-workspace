# Instagram: kit + calendar check

Account @the.leveraged.agent. Ryan schedules IG himself because every reel is over the 10 MB
`file_upload` cap (see SKILL.md hard rules). Reference kit: `Shorts-Build/IG-POSTING-KIT.md`.

## Build the kit: `Shorts-Build/IG-POSTING-KIT.md`

Header: `# Instagram Posting Kit (<N> Reels, @the.leveraged.agent)`, one line of how-to
(instagram.com/scheduled_content or Business Suite > Create reel: add video, paste caption, upload cover, schedule PT),
which reels were skipped as already posted, link to `POSTING-SCHEDULE.md`.

Per slot, in posting order:
~~~~
## N. Sun 9/27 at 5:00 AM | Weekly Seller Update 04

**Video:** [<file>.mp4](<../../Final Videos/<file>.mp4>)  
**Cover:** [cover-04.png](<weekly-seller-update/covers/cover-04.png>)  
**Post:** Sun 9/27, 5:00 AM PT

**Caption:**

```
<caption body from Scripts/<Series>-Instagram-Reel-Captions.md, Length/Clip lines removed>
```
~~~~

Build it with a script, not by hand: parse the schedule table, then for each slot join series + number to
(1) the MP4 in `Final Videos/`, (2) `<that series' slug>/covers/cover-NN.png`, (3) the caption block under
`### Reel N | <file>.mp4`. Assert every file exists and the cover folder belongs to the same series as the video.
Also print a cross-check table (slot, video file, cover path, caption first line) and read it before sending.

## Check the calendar (after Ryan schedules)

Check both, they do not mirror:
- `https://www.instagram.com/scheduled_content/` (week view; prev/next arrows top-left). Click each post: read cover, caption first line, time.
- Business Suite Planner (URL in SKILL.md). Opening a post goes to `.../insights/object_insights/?...&content_id=<id>`; `get_page_text` gives the caption and "Published on".

Per slot, compare to the kit: cover title matches the caption headline and the series, time within ~15 min, no second copy of the same reel anywhere (scheduled or already published). The scheduler preview will not play video (`duration NaN`), so state that the video itself was not verified.

Issues seen on the first run, check for these specifically:
- A reel already published the day before AND scheduled again.
- The same reel showing in both schedulers at slightly different times (possible duplicate).
- Covers from the other series in a slot (OH slots with W covers). Could mean the wrong video too.

## Automation that failed (do not retry)

- `file_upload` of MP4: 10 MB cap.
- Fetch from a localhost server inside business.facebook.com: "Failed to fetch" (cause not confirmed).
- Chunked upload reassembled in the page: denied by the permission classifier. Do not retry it or any equivalent. Only Ryan can change the permission.
