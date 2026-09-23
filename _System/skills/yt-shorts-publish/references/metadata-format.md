# Shorts metadata format (Rose Homes LV)

## Per-Short fields

| field | rule |
|---|---|
| filename | exact MP4 name Ryan uploaded (join key to the draft). Keep the extension. |
| title | ≤ 100 chars, aim ≤ 60. One hook, plain words, no em-dashes, no ALL CAPS, no "premier"/"exclusive". Name the area (Las Vegas, Henderson, Summerlin, etc.) when it fits. |
| description | see template below. Hook first 2 lines, then 1-3 short paragraphs, footer, hashtags. |
| tags | comma-separated, no `#`, total ≤ 500 chars. 8-15 tags. Always include: las vegas real estate, las vegas realtor, las vegas homes, ryan rose. |
| hashtags | 3-6 at the end of the description. Always include `#Shorts` and `#LasVegasRealEstate`. |

## Description template

```
[Hook line 1: the promise of the Short, plain and specific]
[Hook line 2: why it matters to a Vegas buyer/seller]

[1-3 short paragraphs. 6th-grade reading level. Neighborhood names, price ranges, and numbers ONLY if they are in the script. Soft CTA: "Send me a message if you want the full list."]

Free buyer/seller resources: rosehomeslv.com
Have questions? Text or call: 702-747-5921

Ryan Rose | Real Broker, LLC
Las Vegas Real Estate
ryan@rosehomeslv.com
rosehomeslv.com

#Shorts #LasVegasRealEstate #LasVegasHomes [2-3 topic hashtags]
```

## Accepted source layouts

- **Folder of .md files:** one Short per file. Filename of the .md (or a `Filename:` / `File:` line inside) maps to the MP4.
- **Single file with headings:** each `## <something>` block is one Short. Look for `Title:`, `Description:`, `Tags:`, `File:` labels. If labels are missing, first line = title, rest = description.
- **CSV/XLSX:** headers matched case-insensitively: file/filename/video, title, description/desc, tags, hashtags.
- **/yt-long or /local-news output:** `shorts/` subfolder with `short-NN.md` or a `shorts-package.md`. Use them as-is, then normalize.

## schedule.md layout

```
# Shorts schedule - <batch name>
Source: <path>
Timezone: America/Los_Angeles
AI disclosure: No | Yes (<reason>)
Related video (every Short): <long-form title>

| # | filename | title | date | time | status | link |
|---|---|---|---|---|---|---|
| 1 | short-01.mp4 | ... | 2026-09-02 | 09:00 | pending | |
```

Status values: `pending`, `scheduled`, `published`, `no-draft`, `needs-input`, `failed`.

## Scheduling rules

- Timezone default America/Los_Angeles. Confirm if Ryan is traveling.
- Never schedule in the past. If the first slot is already past, shift the whole batch forward one cadence step and tell Ryan.
- Keep the order Ryan's source uses unless he says otherwise.
- Never touch the Time zone control in the schedule picker. Leave it at its default.
