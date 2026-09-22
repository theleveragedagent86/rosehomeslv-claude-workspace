---
name: inbound-engage
description: Daily inbound Instagram routine for @rosehomeslv. Orchestrates scout, comment-replies, and auto-dmer in one browser session. This is the entry point the scheduler calls. Use to run the full inbound engagement routine.
argument-hint: "[preview|live] (defaults to preview)"
model: sonnet
---

## What This Skill Does

The daily orchestrator. In **one logged-in browser session**, it runs the three phases in order:

1. **Scout** (`inbound-scout`) harvests the work-list.
2. **Comment-replies** (`comment-replies`) replies to comments on Ryan's reels.
3. **Auto-DMer** (`auto-dmer`) DMs new followers and reel-likers.

One session, sequential. The phases share the same browser, so they never run in parallel. This is the only skill the schedule needs to call.

## Mode

Read `$ARGUMENTS`. `preview` (default) drafts everything to `output/PREVIEW-<date>.md` and posts nothing. `live` posts. The mode is passed to every phase. **Default to preview if unsure.**

## Preflight (do all of this before touching Instagram)

1. Read `../../CLAUDE.md` (safety contract). This governs every phase.
2. **Pause check:** if `../../state/PAUSE` exists, print "Paused, skipping run." and STOP. Do nothing else.
3. **Browser tools:** confirm Playwright MCP tools (`browser_navigate`, `browser_snapshot`, `browser_click`, `browser_type`) exist. If not, STOP and tell Ryan the MCP is not connected.
4. Read the inherited guardrails once: `/Users/ryanrose/.claude/skills/ig-engage/CLAUDE.md` and `comment-guidelines.md`.
5. Open `https://www.instagram.com`, confirm you are logged in as `@rosehomeslv`. If not, STOP and tell Ryan to log into the persistent profile.

## Phase 1: Scout

Execute the `inbound-scout` skill (read `../inbound-scout/SKILL.md` and follow it) in the current session and mode. It writes `../../output/worklist-YYYY-MM-DD.json`. If scout hits a block/challenge, the run stops here (see Global Stop).

## Phase 2: Comment Replies

Execute the `comment-replies` skill (read `../comment-replies/SKILL.md` and follow it), consuming today's work-list. Honor the 5-per-reel cap and the guardrails. In preview, it drafts. In live, it posts and writes `replied-comments.json` incrementally.

## Phase 3: Auto-DMer

Execute the `auto-dmer` skill (read `../auto-dmer/SKILL.md` and follow it), consuming today's work-list. Honor the ramp, caps, real-follower filter, variant rotation, and pacing in its `safety-and-caps.md`. In preview, it drafts. In live, it sends and writes `dmed-users.json` and `daily-budget.json` incrementally.

## After The Run

- The watermark in `../../state/last-run.json` is updated by the scout phase itself (on a clean scout). You do not need to touch it here.
- Write a combined summary block to the top of `../../output/YYYY-MM-DD.md`:

```markdown
# Inbound Engage — [date] (mode: [preview|live])
- Replies: [n] posted/drafted
- Follower DMs: [n] / cap [n]
- Liker DMs: [n] / cap [n]
- Stopped early: [no | reason]
- Live leads to handle (DM replies): [handles or none]
```

- Print the same summary to the terminal.

## Global Stop Protocol

If ANY phase trips the block protocol ("Action Blocked", "Try Again Later", a challenge/verify redirect, repeated send/post failures, unexpected logout):
- Stop the entire routine immediately. Do not start the next phase.
- Make sure all incremental state already written is saved.
- Report what completed and what stopped it.
- Do not run again for at least 24 hours.

## Order And Idempotency Notes

- Scout first so replies and DMs work from a fresh, deduped list.
- Every phase dedupes against state, so a re-run on the same day will not double-act.
- Keep this routine on a different time of day than the outbound `ig-engage` run.
- Default first several scheduled runs to **preview** until Ryan approves the output.

### Single session vs split sessions

This orchestrator runs all three phases in **one** session, which is best for **manual / interactive** runs (one browser launch).

The **scheduled** runner (`scripts/run-inbound-engage.sh`) instead invokes each phase as its **own** `claude` session, in order: `inbound-scout`, then `comment-replies`, then `auto-dmer`. Each fresh session starts with clean context (stronger than a mid-run `/compact`), and the phases hand off through the work-list and state files on disk. The trade is one browser launch per phase instead of one total, which is fine and a bit more isolated. Either path produces the same result because all state lives on disk.
