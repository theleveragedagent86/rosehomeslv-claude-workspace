---
name: comment-replies
description: Use to reply to comments on Ryan's own @rosehomeslv reels to keep conversations going and expand reach. Max 5 replies per reel, own reels only, reuses the ig-engage guardrails. Build A of the inbound-engagement plugin.
argument-hint: "[preview|live] (defaults to preview)"
model: sonnet
---

## What This Skill Does

Replies, as Ryan, to comments people leave on **his own reels**. The goal is to keep each thread alive (every creator reply nudges the comment back up and signals engagement to the algorithm). This is the safe, high-value piece of the plugin.

**Hard rule: only Ryan's own reels. Never reply on anyone else's post.** Outbound commenting is a different skill (`ig-engage`).

## Read First

1. `../../CLAUDE.md` (safety contract).
2. `/Users/ryanrose/.claude/skills/ig-engage/CLAUDE.md` and `/Users/ryanrose/.claude/skills/ig-engage/comment-guidelines.md` (the inherited guardrails, non-negotiable).
3. `./references/reply-philosophy.md` (how to reply as the creator, including the two rules Ryan requires).
4. The deal records in `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Clients/Transactions/*/transaction.json`, so you can verify anyone who claims they were part of a deal (reply-philosophy Rule 1).
5. Determine **mode** from `$ARGUMENTS`: `preview` (default) drafts only, `live` posts.
6. If `../../state/PAUSE` exists, STOP.
7. Confirm Playwright MCP tools exist, else STOP.

## Get the Work-list

- Prefer the comments in today's `../../output/worklist-YYYY-MM-DD.json` (written by `inbound-scout`), using only entries with `safe: true`.
- If no work-list exists for today, run the comment-harvest yourself (see `inbound-scout`'s browser-playbook) before replying.

## Reply Loop

Process reel by reel. **Cap: at most 5 replies per reel.** Within a reel, prioritize real questions and substantive comments over one-word reactions.

For each target comment:

1. **Re-screen** against the guardrails. If anything is political, LGBTQ+, religious, charged, or hostile, **skip it** and log the skip. When in doubt, skip.
2. **Write the reply** following `reply-philosophy.md`. Two checks first:
   - **Participation claims (Rule 1):** if the comment implies the person was part of the deal (teamwork, congrats on the close), match the reel to its property and verify the commenter against that `transaction.json`'s participants before affirming. No clear name/business match means NOT verified, so reply with a neutral thanks and never claim teamwork.
   - **Leads / help requests (Rule 2):** if they need a realtor or ask for help (or it is turning into a real lead), invite them to DM Ryan directly so it does not get buried.
   Otherwise: 1 to 2 sentences, Ryan's warm local voice, keep the thread going. No em-dashes, no links, no hashtags, one emoji max, vary openings.
3. **Preview mode:** append the drafted reply to `../../output/PREVIEW-YYYY-MM-DD.md` (reel URL, the comment, your drafted reply). Do NOT post. Continue.
4. **Live mode:** post it (mechanics below), verify it appears, then **immediately** append the fingerprint to `../../state/replied-comments.json`. Never batch this write.

### Posting mechanics (live mode)

1. Open the reel, find the target comment in the snapshot.
2. Click "Reply" under that comment. A reply box opens, usually pre-filled with `@commenter`.
3. Type your reply after the mention.
4. Click "Post" (or press Enter where that is the submit action).
5. Wait 2 to 3 seconds, snapshot, and **verify your reply appears nested under the comment.**
6. **Abort on uncertainty:** if you cannot confirm you are replying to the correct comment, or cannot confirm the reply posted, skip it, log it, and move on. Never guess.

### Pacing

- 8 to 20 seconds between reply actions (randomize).
- A few seconds between reels.
- Apply the rate-limit/block protocol from `CLAUDE.md`. On any "Action Blocked" / "Try Again Later" / challenge, STOP immediately, save state, report, wait 24h+.

## Log

Append to `../../output/YYYY-MM-DD.md` (create if missing):

```markdown
## Comment Replies — [date] (mode: [preview|live])
- Reels with replies: [n]
- Replies posted: [n]
- Comments skipped (guardrails): [n]
- Hit 5/reel cap on: [list reel urls or "none"]

### Detail
- [reel url]
  - "[comment]" -> "[your reply]" (posted | drafted | skipped: reason)
```

Then print the same summary to the terminal.

## Reminders

- Max **5 replies per reel**. Stop at 5 even if more safe comments exist.
- Own reels only.
- Incremental state writes after every posted reply.
- No em-dashes, ever.
