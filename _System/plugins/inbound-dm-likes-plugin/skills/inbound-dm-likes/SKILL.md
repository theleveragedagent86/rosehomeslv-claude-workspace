---
name: inbound-dm-likes
description: Use to DM people who liked @rosehomeslv's recent reels a rotated thank-you message. Works the unchecked likers in the shared research log, DMs up to ~15 per run with rotated variants, then checks each off so nobody is ever messaged twice. Run after inbound-research.
model: opus
---

## What This Plugin Does

DMs people who liked Ryan's recent reels a friendly thank-you, then checks each off in the shared research log. Once checked off they are done for good and never messaged again (this includes anyone already DMed as a follower).

Shared log: `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Inbound-Engagement/research-log.md`

## Per-Run Cap

**Up to 15 DMs per run.** Stop at 15 even if more are waiting.

## Start of Run

1. **Pause check:** if `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Inbound-Engagement/PAUSE` exists, STOP and report "Paused."
2. Read the shared log. Collect the **unchecked** `[ ]` items under `## Likers`, in list order (oldest first). Before DMing anyone, also confirm their handle is not already checked off anywhere in the log (followers or likers) — if it is, check this liker line off as `(already messaged)` and skip. If none are waiting, report and stop.
3. Read `./references/dm-templates.md` (the thank-you variants) and `./references/eligibility-and-browser.md` (filter + DM mechanics).
4. **Browser check:** you need Chrome control (Cowork). If not available, STOP.
5. Go to instagram.com, confirm you are logged in as `@rosehomeslv`.

## Send Loop (oldest first, max 15)

For each waiting liker until you hit 15:

1. **Re-confirm eligibility**: skip (and check off with a reason) realtors/brokers and obvious bots; keep regular people and non-competing businesses.
2. **Pick a variant.** Rotate through the thank-you variants, never the same one twice in a row. Personalize with the first name, or use a no-name variant. Never send a literal "[Name]".
3. **Send the DM** in Chrome: open `https://www.instagram.com/<handle>/`, confirm the handle matches, click Message, type, send, and **confirm it appears**. If unsure you are on the right person or that it sent, skip and leave it unchecked.
4. **Check it off** immediately: change the line from `- [ ]` to `- [x]` and append ` — DMed <today> (variant <k>)`. Append a row to `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Inbound-Engagement/dm-history.md`: `| <timestamp> | @handle | liker | <variant> |`.
5. **Pace:** 60 to 120 seconds (randomized) between DMs.

If a liker already replied to a past DM, do not re-DM; flag it in `leads.md`.

## Safety

- **Stop on any block/challenge** ("Action Blocked", "Try Again Later", verify-identity, logout, or a DM failing twice): STOP immediately, write a `PAUSE` file in the shared folder with the reason, tell Ryan.

## Report

```
Liker DMs complete
- Sent: [n] / cap 15
- Skipped (realtor/bot/already-messaged, checked off): [n]
- Replies noticed (flagged to leads.md): [n]
- Still waiting: [n]
```
