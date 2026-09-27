---
name: skool-shorts-schedule
description: Use when Ryan wants a finished batch of Leveraged Agent Reels scheduled, e.g. "schedule the shorts", "put these on YouTube", "link them to the long form", "make me the IG kit", "check the IG calendar". Schedules YouTube Shorts drafts on The Leveraged Agent channel (title, description, tags, 9:16 cover, date/time, related long-form video) via claude-in-chrome, builds the Instagram posting kit Ryan schedules by hand, then verifies both calendars. The Leveraged Agent only; for Rose Homes LV Shorts use /yt-shorts-publish.
argument-hint: "series slug(s), e.g. weekly-seller-update open-house-lead-automation. Add 'ig-kit' or 'check' to run one phase."
---

# /skool-shorts-schedule: YouTube scheduling + IG kit + calendar check

Runs after `/skool-reels`. Inputs it expects (all in `SKOOL Community/Scripts/Shorts-Build/`):
`POSTING-SCHEDULE.md`, `YOUTUBE-SHORTS-METADATA.md` / `yt_manifest.json`, `<slug>/covers/cover-NN.png`,
MP4s in `SKOOL Community/Final Videos/`, IG captions in `SKOOL Community/Scripts/<Series>-Instagram-Reel-Captions.md`.

## Hard rules

- **Channel:** The Leveraged Agent, `UCJ_t1LMeHXO2iTx1YLMs1OA`. Studio has opened on the wrong channel before. Check the URL first; if wrong, switch via avatar > Switch account. **Never post to Rose Homes LV.** IG account: **@the.leveraged.agent** only.
- **Scheduled, never Public**, unless Ryan typed "Public" for that Short.
- **Uploads over 10 MB cannot go through claude-in-chrome `file_upload`** (every reel is 18 to 70 MB). Ryan drags the MP4s in himself. Do NOT work around the cap (chunked uploads, local servers, fetch tricks). The chunked route was denied by the permission classifier. Only Ryan can change that, by switching to Ask permissions or allow-listing `mcp__claude-in-chrome__file_upload`; never change your own permissions. Covers (under 1 MB) upload fine.
- No em dashes. Plan Mode prompt never linked. No offer amounts, buyer/prospect/visitor names, seller contact info.
- Report extremely concisely.

## Phase 0: Inventory (before any slot is used)

1. **YouTube:** read the Shorts list (`studio.youtube.com/channel/UCJ_t1LMeHXO2iTx1YLMs1OA/videos/short`). Note Public / Scheduled / Draft per title.
2. **Instagram:** check what is already published or scheduled in BOTH places, because they do not mirror each other:
   - Business Suite Planner: `business.facebook.com/latest/content_calendar?business_id=1750591132637932&asset_id=1156601044211510&calendar_type=MONTH`
   - `instagram.com/scheduled_content` (posts scheduled here do not show in Business Suite)
   - and the profile grid for anything already live.
3. Anything from this batch already posted on a platform: ask Ryan (AskUserQuestion) whether to skip it there and shift the rest earlier, or keep slots. Update `POSTING-SCHEDULE.md` to match his answer.

## Phase 1: YouTube

1. Ask Ryan to upload the MP4s: Studio > Create > Upload videos, Cmd+Shift+G, paste `/Users/ryanrose/Downloads/Claude/SKOOL Community/Final Videos/`, select the batch. Close the dialog once they are Drafts. Wait for his "done".
2. Get draft IDs, then fill + schedule each draft in schedule order. Exact JS, selectors and the render quirk: [references/youtube-studio.md](references/youtube-studio.md). Per draft: title, description (body + footer), tags (typed on the first reel of a series, then "Reuse details" for the rest), **9:16** cover from `<slug>/covers/`, audience "not made for kids", Schedule date/time from `POSTING-SCHEDULE.md` (YouTube column, PT). Confirm the "Video scheduled" dialog.
3. **Related video** on every Short = its series' long-form video. Ask Ryan which long-form if it is not obvious from the channel. Verify `saved=true | Related video <title>`.
4. Verify the list: count of Scheduled equals the batch size; spot-check dates.
5. Record video IDs (Short + long-form) in `POSTING-SCHEDULE.md` or the series README.

## Phase 2: Instagram kit (Ryan schedules by hand)

Write `Shorts-Build/IG-POSTING-KIT.md`, every IG slot in posting order. Format: [references/instagram.md](references/instagram.md). Each entry = video link, cover link, date + time PT, caption in a code block (Length/Clip lines stripped). **Check each entry's cover folder matches its series** (a mismatch here shipped 10 wrong covers once). Send the kit with SendUserFile. Update the Folder Map in `SKOOL Community/CLAUDE.md`.

## Phase 3: Check ("check the calendar")

After Ryan says he is done, verify per [references/instagram.md](references/instagram.md): each slot has the right reel (cover + caption first line match the kit), the right time (a few minutes off is fine), no duplicates, nothing double-posted against what already went live. The IG scheduler will not play the video, so say that only cover and caption were checked. Report issues as a short list; Ryan fixes IG himself.

## Report

One line per platform: scheduled count, first and last slot, issues. List any row that failed twice (retry twice, then move on).
