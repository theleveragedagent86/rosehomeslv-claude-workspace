# Codename History - channel-wide Shorts queue

**The rule (Ryan, 27 Aug 2026): exactly 3 Shorts per day, at 12:00 AM, 12:00 PM and 6:00 PM
local (GMT-7), and never two Shorts from the same story on the same day.** This replaces the
old 2-per-day rule from 12 Aug 2026, which applies only to Aug 13 through Aug 27.

## Status as of 8 Sep 2026 (Popski's Private Army batch)

**Sep 19 - Oct 8: the 20 Popski Shorts, one per day at 6:00 PM local (GMT-7).** Ryan raised the
daily ceiling to 4 Shorts a day for this batch, with the standing rule kept: never two Shorts
from the same story on one day. The Fujita batch already holds 12:00 PM on Sep 21, 24, 27, 30,
Oct 3 and Oct 6, so 6:00 PM keeps the two batches apart on those dates. No day in the run
exceeds 2 Shorts once this batch is layered on.

All 20 are confirmed Scheduled in Studio with title, description, tags (482 to 500 of 500 as
Studio counts them), audience set to not made for kids, and AI disclosure No. Parent long form:
https://youtu.be/TrAmdteTmLA.

Grid, per-Short titles and paste-ready descriptions:
[`_schedule/shorts-schedule-2026-09-08.md`](_schedule/shorts-schedule-2026-09-08.md).

**Studio counts tag characters differently than a plain join.** Its counter charges each tag its
own length, plus 2 more if the tag contains a space, plus 1 separator between tags. A set that
measures 497 by plain `", ".join` can read 516/500 in Studio and block the Next button. Size tag
sets with that rule, or drop tags from the tail until the counter reads under 500.

**The channel now goes dry after Mon Nov 2 2026** (unchanged, the Fujita batch runs latest).

## Status as of 5 Sep 2026 (Nobuo Fujita batch)

**Sep 6 - Nov 2: the 20 Fujita Shorts, one every third day.** Ryan set this slower spacing on
5 Sep 2026 to stretch the last inventory, since the channel was otherwise dry after Fri Sep 18.
Sep 6 through Sep 18 already carry 3 Shorts a day from the 2026-08-27 grid, so on those five
dates the Fujita Short is simply a 4th upload that day, which Ryan approved. All 20 are
confirmed Scheduled in Studio with title, description, 30 tags (477/500), audience set to not
made for kids, AI disclosure No, and Related video pointed at the Fujita long form
(https://youtu.be/xy5hVRHxWwE).

Grid, per-Short titles and paste-ready descriptions:
[`_schedule/shorts-schedule-2026-09-05.md`](_schedule/shorts-schedule-2026-09-05.md).

Dates: Sep 6, 9, 12, 15, 18 at 6:00 AM, then Sep 21, 24, 27, 30, Oct 3, 6, 9, 12, 15, 18, 21,
24, 27, 30 and Nov 2 at 12:00 PM.

**The channel goes dry after Mon Nov 2 2026.** Unshipped local Shorts that could extend it:
`midway-fuchida/shorts/` 6 (no parent long video on the channel yet, so the "Full video:" line
would break), plus whatever the next build produces.

## Status as of 27 Aug 2026

**Aug 13 - Aug 27: 2 per day** (the old rule), left as scheduled. Those are already in flight.

**Aug 28 - Sep 18: 3 per day, all 66 slots filled and verified in Studio.** The full grid, with
video IDs, titles and paste-ready descriptions, is in
[`_schedule/shorts-schedule-2026-08-27.md`](_schedule/shorts-schedule-2026-08-27.md). Every one
of the 22 days carries exactly three Shorts from three different stories.

Inventory used: SS Ohio 16, Wooden Horse 20, Juan Pujol Garcia 20, Operation Mincemeat 5,
Battle of Castle Itter 3, Operation Postmaster 1, Final Minutes of WW1 1.

**The channel goes dry after Fri Sep 18.** Three per day burns inventory 50% faster than the
old rule. At 3 a day, one more episode of 20 Shorts buys about a week. Unshipped local Shorts
that could extend it: `midway-fuchida/shorts/` 6 (no parent long video on the channel yet, so
the "Full video:" line would break), plus whatever the next build produces.

**Duplicate uploads.** The SS Ohio batch was uploaded to YouTube twice. The 16 duplicates are
listed as COPY B in [`_schedule/draft-ids.md`](_schedule/draft-ids.md) and are left as
unscheduled drafts, so nothing double-publishes. Deleting them is Ryan's click to make.

## How to read or change a Short's scheduled time

Studio's content list shows only the date, never the time, and its DOM exposes no time value.
The only reliable read is the Schedule panel on the edit page:

1. Go to `https://studio.youtube.com/video/<ID>/edit`, wait for load.
2. Run `document.querySelector('ytcp-video-metadata-visibility').scrollIntoView({block:'center'})`.
   The Visibility card is in the right sidebar, not the main column.
3. Real mouse click on that card. A programmatic `.click()` does not open the panel.
4. The panel toggles on each click and the first click does not always open it, so click,
   screenshot, click, screenshot. One of the two shows the Schedule block with the date and
   time pills.
5. To change the time, edit the time input with `document.execCommand('insertText', ...)`,
   click Done, then Save. Save greying out means it persisted.

Within one date the list sorts by exact timestamp descending, so the 12:00 PM Short always
renders above the 12:00 AM one. That was confirmed against 11 direct time reads.

## Long videos on the channel

| ID | Title | State |
|---|---|---|
| TrAmdteTmLA | He Talked His Way Into His Own Army | Sep 12 scheduled |
| xy5hVRHxWwE | The Only Pilot Who Ever Bombed America | Sep 5 published |
| itIyHizIjRQ | The Dead Man Who Fooled the Nazis | Aug 22 scheduled |
| IlZsqP_bAwI | He Died 1 Minute Before Peace | Aug 15 scheduled |
| vhtZtImNvJk | One Bicycle. 14 Hostages. WW2's Strangest Battle | Aug 12 published |
| I0F6TYnfT6o | The Biggest Bluff of World War 2 | Aug 8 published |
| gOXAt0nX3GQ | Who Really Killed the Red Baron | Aug 1 published |
| RpjuLUDv8Yk | A Toilet Sank This Nazi Submarine | Jul 25 published |
| 8zAeX7wOOZI | Britain's Ten Foot Flaming Bomb Wheel | Jul 18 published |
| **-oNmjLhOC50** | **Britain Stole 3 Ships...then Denied It** | **Jul 11 published** |
| syw7qgmtg_8 | The Pigeon That Saved 500 WW1 Soldiers | Jul 4 published |
