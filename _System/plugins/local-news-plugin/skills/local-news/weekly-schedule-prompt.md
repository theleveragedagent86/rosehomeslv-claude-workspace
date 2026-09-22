# Local News, Weekly Schedule

Use these settings when creating or updating the weekly scheduled task / routine that runs this skill.

## Schedule

- **Frequency:** Weekly, every Thursday
- **Time:** 9:15 AM Pacific
- **Cron:** `15 9 * * 4`  (set the routine timezone to America/Los_Angeles so it fires at 9:15 AM PT, not UTC)

## Description

Weekly Las Vegas local news roundup for Clark County, NV (@rosehomeslv). Researches Government/Development, School Board, Real Estate Market, and Local News and Events, plus a hockey beat that condenses into one weekly roundup, and a national-to-local real estate agent that reframes national headlines against local Vegas numbers. Ranks stories by viral potential, then builds a posting schedule from the account's real Instagram analytics, and produces the full content package: green-screen video transcripts, blogs, Instagram captions, YouTube descriptions, real-estate Reddit posts, and a story spreadsheet.

## Prompt

Run this week's Clark County, NV local news roundup for @rosehomeslv using the local-news skill. Use today's date as the target week. Run the full pipeline autonomously from research through the final content package: the posting schedule, video transcripts, blogs, Instagram captions, YouTube descriptions, real-estate Reddit posts, and the story spreadsheet. Every transcript and caption must carry its posting day, clock time, and trial reel call. Do not stop to ask between steps. Save everything to the dated output folder and end with the summary report.

/local-news

## Setup notes

- **Working directory:** point the routine at the workspace root `/Users/ryanrose/Downloads/Claude` so `/local-news` and the output paths resolve reliably.
- The skill writes to `Rose Homes LV/Content/Instagram/Local News/[YYYY-MM-DD]/` using an absolute path, so output does not depend on the working directory. Keeping the working directory at the workspace root still avoids the routine-path breakage seen during the reorg.
- The run is heavy (6 research agents, then batched blog agents). Expect a long execution; make sure the machine or cloud environment stays awake for the window.
- **Posting cadence:** three news posts a day, weekdays at 9:45 AM, 2:30 PM, and 6:30 PM Pacific, weekends at 9:30 AM, 2:30 PM, and 6:15 PM. The one exception is the weekly hockey roundup, `HK-WEEK`, which is an extra fourth post in the morning slot on a single weak day and never takes a news slot. These come from the account's verified analytics in `account-analytics.md`, not from generic advice. Re-pull that data roughly every 90 days and update the file when you do.
- Because the routine fires Thursday, the schedule it produces covers the following seven days. Stories beyond 21 land in the overflow pool with no date.
