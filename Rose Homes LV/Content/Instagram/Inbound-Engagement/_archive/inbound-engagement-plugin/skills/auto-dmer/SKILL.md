---
name: auto-dmer
description: Use to DM new followers and likers of flagged reels on @rosehomeslv. The single unified DMer for the inbound-engagement plugin (Builds B and C). Rotates message variants, applies a real-follower filter, and enforces hard daily caps and a warm-up ramp.
argument-hint: "[preview|live] (defaults to preview)"
model: sonnet
---

## What This Skill Does

One DMer, two triggers:
- **B. New followers** get a rotated welcome DM.
- **C. Likers of flagged reels** get a rotated thank-you DM.

It sends as Ryan via the logged-in browser. It is the highest-risk part of the plugin (proactively messaging strangers), so the caps, the real-follower filter, the message variation, and the pacing in `./references/safety-and-caps.md` are mandatory, not suggestions.

## Read First

1. `../../CLAUDE.md` (safety contract).
2. `./references/safety-and-caps.md` (caps, ramp, pacing, dedupe, crash-safety). **Load the numbers before sending anything.**
3. `./references/dm-templates.md` (Ryan's templates and the rotated variants).
4. `./references/browser-playbook.md` (DM compose mechanics, abort-on-uncertainty).
5. Determine **mode** from `$ARGUMENTS`: `preview` (default, draft only) or `live`.
6. If `../../state/PAUSE` exists, STOP.
7. Confirm Playwright MCP tools exist, else STOP.

## Load State and Compute Today's Budget

From `../../state/`:
- `dmed-users.json` — the authoritative ledger of everyone already DMed, stored as timestamped objects (`handle`, `trigger`, `dmed_at`, `variant`, `mode`, `display_name`). Match on the `handle` field. **Never DM a handle that already appears here, ever.** This is the record that stops repeat-DMing the same people.
- `daily-budget.json` — `{ "date", "daily_cap", "follower_dms_sent_today", "liker_dms_sent_today" }`. If the stored `date` is not today, OR `daily_cap` is missing, choose a fresh `daily_cap` = a random whole number from **50 to 75** (per `safety-and-caps.md`), reset both counters to 0, and set `date` to today.
- `last-run.json` — informational watermark (not a harvest stop).

The cap is a **single combined ceiling** for followers + likers. Remaining budget = `daily_cap - (follower_dms_sent_today + liker_dms_sent_today)`. Stop when it reaches 0.

## Get Targets

From today's `../../output/worklist-YYYY-MM-DD.json`:
- `new_followers` where `passes_filter == true`, not in `dmed-users.json`.
- `likers` where `passes_filter == true`, not in `dmed-users.json` (from recent reels, or flagged reels if `target-reels.md` is set).

If no work-list exists, run the relevant harvest from `inbound-scout`'s playbook first. **Re-confirm the eligibility filter** on each target before DMing: skip realtors/brokers, keep non-competing businesses (referral sources). The filter is the report protection, never skip it.

## Send Loop

Process followers first, then likers. Respect the remaining daily budget for each. Stop when the budget is hit.

**Order followers oldest-first.** The work-list `new_followers` are listed newest-first, so iterate them in reverse (oldest follower in the harvested window first). This drains any backlog left over from a previous day's cap before messaging brand-new followers, so nobody who followed earlier is left waiting indefinitely. Likers can stay in list order.

For each target:

1. **Pick a variant.** Rotate through the variants for that trigger (follower vs liker). Never use the same variant twice in a row. Track the last-used index in memory for the run.
2. **Personalize.** Extract the first name from the target's display name. If there is no usable personal first name (missing, business name, all emoji), use the **no-name variant**. Never send a literal "[Name]".
3. **Preview mode:** append to `../../output/PREVIEW-YYYY-MM-DD.md` (handle, trigger, the exact message you would send). Do NOT open a DM thread. Continue.
4. **Live mode:** open the DM thread, type the message, send, and **verify it appears in the thread** (mechanics in browser-playbook). The instant it is verified, write the record to BOTH logs and bump the counter (never batch, a crash must not double-send):
   - Get the timestamp from the system clock: run `date "+%Y-%m-%dT%H:%M:%S%z"` (macOS-safe ISO 8601 with offset).
   - Append a timestamped object to `../../state/dmed-users.json`: `{ "handle": "@h", "trigger": "follower|liker", "dmed_at": "<that timestamp>", "variant": "<variant id>", "mode": "live", "display_name": "<name or null>" }`.
   - Append a row to `../../output/dm-history.md` (the human-readable cumulative log): `| <timestamp> | @h | follower/liker | <variant> | live |`.
   - Increment the counter in `../../state/daily-budget.json`.
5. **Abort on uncertainty:** if you cannot confirm you opened the correct person's thread, or cannot confirm the message sent, do NOT retry blindly. Skip, log it, move on. A wrong-person DM is worse than a miss.
6. **Pace:** wait 45 to 90 seconds (randomized) before the next DM. Longer gaps between followers and likers.

## Block Protocol

On any "Action Blocked", "Try Again Later", message-send failure repeated twice, challenge/verify redirect, or unexpected logout: **STOP immediately**, save state, report, and do not run again for 24h+. This is non-negotiable, a block is Instagram warning you before a ban.

## Log

Append to `../../output/YYYY-MM-DD.md`:

```markdown
## Auto-DMer — [date] (mode: [preview|live])
- Follower DMs: [n] sent / cap [n]
- Liker DMs: [n] sent / cap [n]
- Skipped (already DMed): [n]
- Skipped (failed filter): [n]
- Variant usage: follower [v1:n, v2:n, ...], liker [...]

### Detail
- @handle (follower) -> variant [k]: "[message]" (sent | drafted | skipped: reason)
```

Print the same summary to the terminal. Flag in the log any thread where the person had already replied to a past DM (potential live lead for Ryan to handle personally).

## Reminders

- Real-follower filter on every target. No exceptions.
- Rotate variants, never identical sends.
- Hard caps and ramp from `safety-and-caps.md`.
- Incremental dedupe writes after every send.
- No em-dashes, ever.
