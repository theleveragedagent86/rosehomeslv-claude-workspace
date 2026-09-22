---
name: inbound-scout
description: Use to harvest inbound Instagram activity for @rosehomeslv before replying or DMing. Reads new comments on Ryan's reels, new followers, and likers of flagged reels, then writes a deduped work-list. The research step the orchestrator runs first.
argument-hint: "[preview|live] (defaults to preview)"
model: sonnet
---

## What This Skill Does

This is the **researcher**. It opens `@rosehomeslv` once, reads three inbound surfaces, removes anything already handled, and writes a structured work-list that `comment-replies` and `auto-dmer` consume. It does **not** post or DM anything. Harvest only.

It is normally run by the `inbound-engage` orchestrator, but can run standalone to preview what is waiting.

## Read First (session start)

1. Read `../../CLAUDE.md` (this plugin's safety contract).
2. Read the inherited guardrails: `/Users/ryanrose/.claude/skills/ig-engage/CLAUDE.md` and `/Users/ryanrose/.claude/skills/ig-engage/comment-guidelines.md`.
3. Read `./references/browser-playbook.md` (the UI flows and the real-follower filter).
4. **Check for pause:** if `../../state/PAUSE` exists, STOP and report "Paused, skipping run." Do nothing else.
5. **Detect browser tools:** confirm `browser_navigate`, `browser_snapshot`, `browser_click` (Playwright MCP) exist. If not, STOP and tell Ryan the MCP is not connected (see README setup).
6. Load state files from `../../state/` (create empty defaults if missing):
   - `replied-comments.json` — list of comment fingerprints already replied to.
   - `dmed-users.json` — handles already DMed (with date and trigger).
   - `last-run.json` — `{ "last_follower_watermark": "@handle", "last_run_date": "..." }`.
   - `target-reels.md` — reel URLs flagged for liker-DM (may be empty).

## Open Instagram

1. Navigate to `https://www.instagram.com`.
2. Verify you are logged in as `@rosehomeslv` (profile icon / username visible). If not, STOP and tell Ryan to log into the `~/.cache/playwright-instagram-profile` browser.

## Harvest 1: New Comments on Ryan's Reels (for Build A)

1. Go to `https://www.instagram.com/rosehomeslv/reels/` (and the main grid if needed).
2. Open the most recent reels, newest first. Cover up to the last ~8 reels, or stop earlier once you reach reels older than ~14 days with no new comments.
3. For each reel, read the visible comments. Use `browser_snapshot` (accessibility tree) so you capture commenter handle + comment text reliably.
4. For each comment build a **fingerprint** = `reel_url + "|" + commenter_handle + "|" + sha-ish hash of comment_text`. Skip the comment if its fingerprint is already in `replied-comments.json`.
5. **Screen each new comment** against the guardrails. Mark `safe: false` with a `skip_reason` for anything political, LGBTQ+, religious, controversial, or a comment Ryan himself left. Do not collect Ryan's own comments as reply targets.
6. Respect the per-reel cap: collect at most the **5** best reply candidates per reel (prioritize real questions and substantive comments over one-word reactions).

## Harvest 2: New Followers (for Build B)

1. Open `https://www.instagram.com/rosehomeslv/followers/`. The list is newest-first at the top.
2. Scroll from the top and collect candidates down to a depth of about **75 followers** (scroll as needed). **Do not stop at the watermark.** For each, skip anyone already in `dmed-users.json` (match canonically: lowercase, ignore a leading `@`). Collect every remaining (not-yet-DMed) follower in this window. This window approach is deliberate: anyone you could not DM yet (deferred over the daily cap) stays visible on the next run until they are reached, instead of being skipped forever. The `dmed-users.json` ledger is the real boundary, not the watermark.
3. For each new follower, apply the **real-follower filter** (see browser-playbook). Record `passes_filter` and a `filter_reason` when skipped. Capture the display name so the DMer can extract a first name.
4. Remember the topmost handle seen this run, it becomes the new watermark (the orchestrator/DMer writes it after the run).

## Harvest 3: Likers of Recent Reels (for Build C)

Ryan wants to DM people who like his reels (the way the phone notifications show every liker). Instagram **web** has no reliable aggregated likes-notification feed, so harvest likers from the **likes lists of his recent reels**, which captures the same people per reel.

1. Decide which reels to read:
   - If `target-reels.md` lists active reel URLs, use those (a focused push).
   - Otherwise default to his **most recent ~6 reels**, so liker-DM is active by default and not gated on flagging.
2. For each reel, open it and open its likes list (the "liked by" list).
3. Also check the web notifications/activity panel (the heart / activity icon, or `https://www.instagram.com/notifications/`) for recent "liked your reel" entries and add any likers it surfaces. Web coverage here is thin, so treat the per-reel likes lists as the primary source and this as a bonus.
4. Collect liker handles, drop anyone whose `handle` is already in `dmed-users.json`, and apply the same DM eligibility filter (skip realtors/brokers; other businesses are fine). Tag each with the source `reel_url`.
5. Collect up to ~60 liker candidates per run. The DMer enforces the real daily cap (the shared 50 to 75 budget).

## Write the Work-list

Write `../../output/worklist-YYYY-MM-DD.json` with this shape:

```json
{
  "date": "YYYY-MM-DD",
  "mode": "preview|live",
  "comments": [
    {"reel_url": "...", "reel_caption_snippet": "...", "commenter": "@h", "comment_text": "...", "fingerprint": "...", "safe": true, "skip_reason": null}
  ],
  "new_followers": [
    {"handle": "@h", "display_name": "First Last", "passes_filter": true, "filter_reason": null}
  ],
  "likers": [
    {"handle": "@h", "display_name": "First Last", "reel_url": "...", "passes_filter": true, "filter_reason": null}
  ],
  "topmost_follower_seen": "@h"
}
```

## Update last-run.json (clean scout only)

After the work-list is written and only if the scout completed without hitting a block, update `../../state/last-run.json`:
- `last_run_date` = today.
- `last_follower_watermark` = `topmost_follower_seen` (**informational only**, the newest handle seen this run). This is a record, NOT a harvest stop.

Harvesting is bounded by the ~75-deep window and deduped against `dmed-users.json`, so deferred followers are never permanently skipped. Do not use the watermark to limit the next harvest.

## Report

Print a short summary:

```
Scout complete (mode: [preview|live])
- Reels scanned: [n]
- New safe comments: [n] (skipped charged: [n])
- New followers: [n] (passed filter: [n], bots skipped: [n])
- Likers on flagged reels: [n] (flagged reels: [n])
- Work-list: output/worklist-YYYY-MM-DD.json
```

## Pacing and Safety

- This is read-only browsing, but still pace gently: 3 to 8 seconds between reels and list scrolls. Do not hammer.
- Apply the rate-limit/block protocol from `CLAUDE.md`. If Instagram challenges you, STOP and report.
- Do not like, comment, or DM in this skill. Harvest only.
