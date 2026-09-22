# CLAUDE.md — Inbound Engagement Plugin

**IMPORTANT: Read this entire file before running anything in this plugin. It is the master playbook and the safety contract.**

## Who You Are Working For

- **Name:** Ryan Rose
- **Business:** Rose Homes LV, Real Broker LLC (Las Vegas real estate)
- **Instagram account:** `@rosehomeslv` (his real business brand and lead source)
- **Contact:** 702-747-5921, ryan@rosehomeslv.com, rosehomeslv.com

## What This Plugin Does

This is **inbound** Instagram automation. It works on Ryan's OWN account `@rosehomeslv`, not on other people's posts. (His separate `ig-engage` skill does outbound commenting on other Vegas accounts. Do not confuse the two.)

Three jobs, all driven by Playwright MCP browser automation against a logged-in `@rosehomeslv` session:

1. **Reply to comments on Ryan's own reels** to keep conversations going and expand reach. Max 5 replies per reel.
2. **DM new followers** with a rotated welcome message.
3. **DM people who liked his recent reels** with a rotated thank-you message.

There is no Instagram API involved. Everything is a real browser logged in as Ryan.

## The Risk Reality (do not soften this)

Proactively DMing strangers violates Instagram's Terms of Service and can get `@rosehomeslv` shadowbanned or disabled. Ryan has knowingly accepted this. Your job is to run as conservatively as the rules below allow so the account survives as long as possible. **When any safety rule and "more reach" conflict, safety wins.**

## Non-Negotiable Rules (every comment and DM)

These are inherited from Ryan's `ig-engage` skill. The canonical sources are:
- `/Users/ryanrose/.claude/skills/ig-engage/CLAUDE.md`
- `/Users/ryanrose/.claude/skills/ig-engage/comment-guidelines.md`

Read those at session start. The short version:

1. **NO EM-DASHES EVER.** Use commas, periods, or "and". This is the #1 rule.
2. **Sound like a real person**, specifically like Ryan. Not a brand, not a bot.
3. **Skip charged content entirely.** Political, LGBTQ+, religious, or controversial comments get no reply and the commenter gets no DM. When in doubt, skip.
4. **No links, no hashtags, no @mentions** of other accounts in replies.
5. **Short.** Replies are 1 to 2 sentences. One emoji max, zero is fine.
6. **Vary the wording.** Never send the same text twice in a row. DM templates are rotated through 3 to 5 variants (see `auto-dmer/references/dm-templates.md`).
7. **Factual only.** Never invent prices, programs, or claims.

## Hard Safety Limits

| Action | Cap | Notes |
|--------|-----|-------|
| Comment replies | **5 per reel** | Only on Ryan's own reels. |
| Follower + liker DMs (combined) | **Randomized 50 to 75 per day** (Ryan's choice, no warm-up ramp) | Eligibility filter required. Followers DMed first (oldest-first), then likers, sharing the daily cap. |
| Pacing (DMs) | 45 to 90s between sends, randomized | Longer between batches. |
| Pacing (replies) | 8 to 20s between actions | |

**DM eligibility filter (required before any DM):** skip the user unless they have a profile picture AND at least one post AND a handle that is not an obvious bot pattern AND are not a zero-info private account AND are not a real estate agent or broker (Ryan does not DM competitors). Non-competing businesses and service providers (lenders, attorneys, contractors, photographers) are allowed as referral sources. Bot/spam accounts are the most likely to report Ryan, which drives bans; this filter is the primary report protection and is never disabled.

## Crash Safety and Correctness

- **Write state incrementally.** The instant a DM or reply is verified as sent, record it in the relevant `state/` file. Never batch state writes to the end of a run. A mid-run crash must never cause a double-send.
- **Abort on uncertainty.** If you cannot positively confirm you are on the correct DM thread, or cannot positively identify the correct send control, **skip that item** and log it. Never guess. A wrong-person DM or a reply on the wrong comment is worse than a miss.
- **Never DM the same handle twice** across followers and likers, ever. The `state/dmed-users.json` ledger records every DM with a timestamp (`dmed_at`), and `output/dm-history.md` is the readable cumulative log. Before every send, check whether the target is already in the ledger; if so, skip. Match handles **canonically** (lowercase, ignore a leading `@`) so there is no format-driven duplicate. Because the ledger is written the instant each DM is verified, a handle DMed as a follower earlier in the same run is also skipped if they reappear as a liker. Once someone gets a follow or like DM, they are off the list for good. **Never reply to the same comment twice** (check `state/replied-comments.json`).

## Kill-Switch and Pause

- **Pause for one run:** create the file `state/PAUSE`. The orchestrator checks for it at start and exits immediately if present. Delete it to resume.
- **Full stop:** unload the scheduled job: `launchctl unload ~/Library/LaunchAgents/com.rosehomeslv.inbound-engage.plist`. See README.

## Rate-Limit / Block Protocol

If Instagram shows any of these, **STOP THE RUN IMMEDIATELY**, save state, report to Ryan, and do not run again for at least 24 hours:
- "Try Again Later"
- "Action Blocked"
- A "verify your identity" / challenge redirect
- DMs or replies fail to send multiple times
- The page refreshes or logs out unexpectedly

## Preview Mode vs Live Mode

The orchestrator supports a preview mode. In preview, the scout harvests real work-lists and every reply and DM is **drafted to `output/PREVIEW-YYYY-MM-DD.md` without posting anything**. Run preview until Ryan approves the variants and the harvested targets, then switch to live. Default the first several scheduled runs to preview.

## File Map

- `skills/inbound-engage/` — orchestrator, the daily entry point.
- `skills/inbound-scout/` — harvester (the "researcher").
- `skills/comment-replies/` — Build A.
- `skills/auto-dmer/` — Builds B (followers) and C (likers), unified.
- `state/` — runtime state, never committed. `dmed-users.json` is the timestamped dedupe ledger (who was DMed and when).
- `output/` — daily logs, preview drafts, and `dm-history.md` (readable cumulative DM log).

## What Was Deliberately Cut

Sharer-DM (DMing people who share Ryan's videos) is NOT built. Instagram does not expose who shares a reel via DM, so it was impossible to target. Do not try to add it back without a real detection method.
