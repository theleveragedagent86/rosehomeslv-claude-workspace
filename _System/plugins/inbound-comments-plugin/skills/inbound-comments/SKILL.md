---
name: inbound-comments
description: Use to reply to comments on Ryan Rose's own @rosehomeslv reels. Works the unchecked comments in the shared research log, replies (5 per reel, ig-engage guardrails, verifies any teamwork claim, sends leads to DMs), then checks each off. Run after inbound-research.
model: opus
---

## What This Plugin Does

Replies as Ryan to comments on **his own reels**, then checks each one off in the shared research log so it is never worked again. Only Ryan's own reels, never anyone else's post.

Shared log: `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Inbound-Engagement/research-log.md`

## Start of Run

1. **Pause check:** if `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Inbound-Engagement/PAUSE` exists, STOP and report "Paused."
2. Read the shared log. Collect the **unchecked** `[ ]` items under `## Comments`. If there are none, report "nothing waiting" and stop.
3. Read `./references/reply-rules.md` (the voice and the two required rules).
4. Read the inherited guardrails at `/Users/ryanrose/.claude/skills/ig-engage/comment-guidelines.md`.
5. Read the deal records `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Clients/Transactions/*/transaction.json` so you can verify any teamwork claim.
6. **Browser check:** you need Chrome control (Cowork). If not available, STOP.
7. Go to instagram.com, confirm you are logged in as `@rosehomeslv`.

## Reply Loop

Group the waiting comments by reel. **Cap: 5 replies per reel** (prioritize real questions and substantive comments). For each comment you reply to:

1. **Re-screen** against the guardrails. If it is political, LGBTQ+, religious, charged, or hostile, do NOT reply: just check it off with a note `(skipped: charged)` and move on.
2. **Apply the two rules** from `reply-rules.md`:
   - **Rule 1 (teamwork):** if the comment implies the person was part of the deal, match the reel to its property and verify them against that `transaction.json`. No clear name/business match = neutral thanks, never claim teamwork.
   - **Rule 2 (leads):** if it is a help request or lead ("need an agent", "where do I apply", "looking to buy/sell"), invite them to DM Ryan directly so it does not get buried. Also append the lead to `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Inbound-Engagement/leads.md` (create if missing) so Ryan can follow up.
   - Otherwise: warm, 1 to 2 sentences, keep the thread going. No em-dashes, no links, no hashtags, one emoji max, vary openings.
3. **Post the reply** in Chrome: open the reel, click Reply under that comment, type, submit, and **confirm it appears**.
   - **If it posts:** go to step 4.
   - **If Instagram says "Couldn't post comment" (or the reply never appears):** this is a *single-comment* failure, not an account block. Retry once. If it still fails, check that comment off with a note ` — (skipped: couldn't post <today>)` and move to the next comment. **Do NOT write a PAUSE file for this.** One comment that will not post (deleted comment, restricted replies, duplicate text) must never stop the whole run.
   - **Count consecutive failures:** only if **3 comments in a row** fail to post do you treat it as a likely account-level soft block and follow the Safety rule below. A single failure, or failures with a success in between, never trigger PAUSE.
4. **Check it off** in the shared log: change that line from `- [ ]` to `- [x]` and append ` — replied <today>`. Do this immediately after each post.

## Safety

- 8 to 20 seconds between replies, randomized.
- **A single "Couldn't post comment" is NOT a block.** Handle it in the reply loop (retry once, then skip that one comment and keep going). Never PAUSE the whole system over one comment, since doing so silently kills research and both DM tasks too (they all share the same `PAUSE` gate).
- **PAUSE only on an account-level block/challenge:** "Action Blocked", "Try Again Later", verify-identity / "confirm it's you", a forced logout, **or 3 comment posts failing in a row**. In that case only: STOP, write a `PAUSE` file at `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Inbound-Engagement/PAUSE` with the reason and date, and tell Ryan. This is the sole condition that writes PAUSE.
- Deleting the `PAUSE` file (once commenting is confirmed working) resumes all four scheduled tasks.

## Report

```
Comments complete
- Replied: [n]  (reels: [n])
- Skipped charged (checked off): [n]
- Leads flagged to leads.md: [n]
- Still waiting: [n]
```
