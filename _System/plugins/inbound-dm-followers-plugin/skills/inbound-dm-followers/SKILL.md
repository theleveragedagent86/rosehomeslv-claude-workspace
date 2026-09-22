---
name: inbound-dm-followers
description: Use to DM new followers of @rosehomeslv a rotated welcome message. Works the unchecked followers in the shared research log, DMs up to ~30 per run with rotated variants, then checks each off so nobody is ever messaged twice. Run after inbound-research.
model: opus
---

## What This Plugin Does

DMs Ryan's new followers a warm welcome, then checks each off in the shared research log. Once someone is checked off they are done for good and never messaged again.

Shared log: `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Inbound-Engagement/research-log.md`

## Per-Run Cap

**Up to 30 DMs per run.** Stop at 30 even if more are waiting (the rest stay `[ ]` for next run).

## Start of Run

1. **Pause check:** if `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Inbound-Engagement/PAUSE` exists, STOP and report "Paused."
2. Read the shared log. Collect the **unchecked** `[ ]` items under `## Followers`, in list order (oldest first). If none, report "nothing waiting" and stop.
3. Read `./references/dm-templates.md` (the welcome variants) and `./references/eligibility-and-browser.md` (filter + DM mechanics).
4. **Browser check:** you need Chrome control (Cowork). If not available, STOP.
5. Go to instagram.com, confirm you are logged in as `@rosehomeslv`.

## Send Loop (oldest first, max 30)

For each waiting follower until you hit 30:

1. **Re-confirm eligibility** by glancing at their profile: skip (and check off with `(skipped: realtor)` or `(skipped: bot)`) anyone who is a real estate agent/broker or an obvious bot. Keep regular people and non-competing businesses (referral sources).
2. **Pick a variant.** Rotate through the welcome variants, never the same one twice in a row. Fill in the first name from their display name; if there is no usable first name, use a no-name variant. Never send a literal "[Name]".
3. **Send the DM** in Chrome: open `https://www.instagram.com/<handle>/`, confirm the handle on the page matches, click Message, type, send, and **confirm the message appears in the thread**. If you cannot confirm you are on the right person or that it sent, skip and leave it unchecked.
4. **Check it off** immediately: change that follower's line from `- [ ]` to `- [x]` and append ` — DMed <today> (variant <k>)`. Also append a row to `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Inbound-Engagement/dm-history.md` (create with a header if missing): `| <timestamp> | @handle | follower | <variant> |`.
5. **Pace:** wait 60 to 120 seconds (randomized) before the next DM. DMing strangers is the most sensitive action, so go slow.

If a follower already replied to a past DM, do not re-DM; note it in `leads.md` for Ryan.

## Safety

- **Stop on any block/challenge** ("Action Blocked", "Try Again Later", verify-identity, logout, or a DM failing twice): STOP immediately, write a `PAUSE` file in the shared folder with the reason and time, and tell Ryan. Do not keep sending.

## Report

```
Follower DMs complete
- Sent: [n] / cap 30
- Skipped (realtor/bot, checked off): [n]
- Replies noticed (flagged to leads.md): [n]
- Still waiting: [n]
```
