---
name: coach-teardown
description: Use when Ryan wants a competitor teardown of a real estate coach, agent influencer, or agent-facing Instagram account. Give it a handle and it harvests every commenter and liker, catalogues the posts, reverse-engineers the funnel mechanic, and builds ranked DM lists of the realtors engaging with them. Those people are the exact avatar for The Leveraged Agent Skool. Also folds in their email newsletter if Ryan forwards one. NOT for Rose Homes LV buyer/seller prospecting, use ig-research for that.
argument-hint: "an Instagram handle, with or without the @ (e.g. @peyson.robertson)"
---

# Coach Teardown

Full-funnel teardown of a **real estate coach or agent influencer**. Two jobs at once:

1. **Steal the mechanics.** What makes their content convert, measured, not guessed.
2. **Take their audience.** Every realtor commenting on their posts is Ryan's avatar for
   The Leveraged Agent. Log the handles so Ryan can follow, engage, then DM.

**Brand:** The Leveraged Agent (Skool/coaching). Output lands in
`SKOOL Community/Instagram/Competitor-Research/<Name>/`. This is not Rose Homes LV work.

## Before you start

- **Ryan gives you a handle.** If he did not, ask for one, one line, then stop.
- **Chrome must be logged into Instagram.** The whole harvest runs through
  `mcp__claude-in-chrome__javascript_tool` against Instagram's own web API, from an
  authenticated page context. No login, no data.
- **The permission rule must be in place, or the harvest dies at pass B.** In auto and bypass
  modes the classifier denies any `javascript_tool` call containing a fetch loop, a scroll
  loop, or a `window.fetch` hook. Single one-shot fetches pass, worker pools do not. Check
  `permissions.allow` in `/Users/ryanrose/Downloads/Claude/.claude/settings.local.json` for:

  ```
  mcp__claude-in-chrome__javascript_tool
  ```

  Added 2026-09-09 and it takes effect immediately, no session restart. MCP tools cannot be
  scoped by argument, so this allows JS on any tab, not just instagram.com. If Ryan wants it
  gone after a teardown, remove that one line.

  **Even with the rule, some calls still get denied.** On the Kristi Jencks run, post metadata
  loops ran fine and the comment and liker loops (username, display name, comment text at
  scale) were refused twice. Do not reword the same operation to slip past it. Say plainly
  which half of the teardown is blocked, deliver the other half, and let Ryan decide.
- Read the reference files as you need them, not all at once:
  - `references/harvest.md` = the exact browser code. Copy it, do not improvise it.
  - `references/analysis.md` = the Python that turns raw JSON into the lists.
  - `references/newsletter.md` = the email half of the funnel.
  - `references/output-templates.md` = what the deliverables must contain.
- The reference teardown to match for depth and tone is
  `SKOOL Community/Instagram/Competitor-Research/Peyson-Robertson/`. Read
  `STRATEGY-TEARDOWN.md` there before writing your own analysis.

## Run order

### 1. Profile

Navigate to `https://www.instagram.com/<handle>/`. Capture followers, following, post count,
verified, bio, link, and whether anything is pinned. Get the numeric user id by regexing
`"profile_id":"(\d+)"` out of the page HTML. **`/api/v1/feed/user/?count=1` no longer works,
see harvest.md.** Read the coach's own website too, the offer ladder and the prices are
usually published there and it costs one page fetch.

Note pins honestly. On Peyson the grid pins were personal and there were **no pinned reels**,
which contradicted the assumption going in. Say what is actually there.

### 2. Harvest, in three passes

Follow `references/harvest.md` exactly. It solves four failures that will otherwise cost hours:

- **The 45 second CDP timeout.** Never `await` long work. Launch an async IIFE onto
  `window.__job` and poll it with short follow-up calls.
- **Comment pagination stops after one page** unless you also check
  `has_more_headload_comments`, not just `has_more_comments`.
- **Likers 403** without an `x-csrftoken` header.
- **Serial fetching takes 7 hours.** Use a 6-worker pool. ~16 req/s, no 429s observed.
- **The post-list endpoint is dead as of Sep 2026.** Pass A is now a grid scrape plus a
  shortcode decode. harvest.md carries the replacement.

Pass A: all posts. Pass B: all comments. Pass C: all likers.

**Never print raw data into the conversation.** Write it to disk with the Blob download
helper, then `mv` from `~/Downloads` into `data/`. A full harvest is ~100K rows and will
destroy the context window if you read it.

### 3. Known limits, state them, do not paper over them

- **Likers are hard-capped around 188-190 per post.** Instagram does not paginate them.
  On a post with 500 likes you get the first ~190. Say so in the README.
- **Follower lists are not exposed.** You cannot get "everyone who follows them."
- `web_profile_info` and `users/<id>/info/` may return `[BLOCKED: Cookie/query string data]`.
  Fall back to `find` + a screenshot to read the profile.
- Instagram's public `comment_count` roughly **doubles** the real number of humans, because
  the coach replies to nearly every keyword comment and each reply counts.

### 4. Analysis

Run `references/analysis.md`. It produces:

- **Post catalogue** with date, format, keyword CTA, topic, likes, comments, plays, hook.
- **The CTA lift number.** Median comments on posts WITH a keyword CTA versus without, split
  by format. On Peyson this was 12x on carousels and 11x on reels, and it was the finding
  that made the whole account make sense.
- **Topic performance table.** Which subject earns comments, which earns only reach.
- **Format table.** Carousels versus reels versus single images.
- **The keyword frequency list.** Every word people are told to comment, ranked. This is
  their offer ladder in public.
- **Hook patterns.** What the first line of the best posts has in common.
- **Month over month trend.** Are they growing or coasting.

### 5. The lists

Cut these every time, same names, so teardowns stay comparable:

| File | Who is in it |
|---|---|
| `MASTER-PEOPLE-LOG.csv` | every unique account, with counts and first/last seen |
| `LIST-A-hot-AI-commenters.csv` | commented on an AI/Claude post. **The best list.** |
| `LIST-B-business-commenters.csv` | commented on any business/strategy post |
| `LIST-C-repeat-engagers.csv` | 3+ comments, habitual |
| `LIST-D-RE-name-signal.csv` | handle or name matches the realtor regex |
| `LIST-E-likers-only.csv` | liked, never commented, coldest |
| `PER-POST-COMMENTER-LOG.csv` | one row per comment with post hook and comment text |
| `TOP-300-DM-TARGETS.csv` | ranked shortlist, scoring in `references/analysis.md` |

### 6. The newsletter, if there is one

Coaches sell in email, not on Instagram. If Ryan forwards an email, or if a newsletter shows
up in his Gmail, run `references/newsletter.md`. On Peyson this changed the conclusion: his
Instagram never asks for money and his newsletter asks three times a week.

Ask once, one line, at the end of the IG work: "want me to check Gmail for their newsletter?"
Do not go digging through Ryan's inbox unprompted.

### 7. Write the deliverables

Per `references/output-templates.md`:

- `README.md`, the index, with the capture caveats up top
- `STRATEGY-TEARDOWN.md`, the analysis, 10 sections
- `POST-CATALOGUE-<year>.md`, the table
- `NEWSLETTER-TEARDOWN.md`, only if there was email
- the CSVs, and `data/` with the raw JSON

Then **update the Folder Map** in `SKOOL Community/CLAUDE.md`. Not optional, it is the
workspace maintenance rule.

## How to write the analysis

**Lead with the mechanic, not the metrics.** Most agent-facing accounts run exactly one
engine and everything else is decoration. Find it, name it in the first section, prove it
with a table, and say what to copy verbatim.

**Correct Ryan's premises when the data disagrees.** He will come in with an assumption. On
Peyson: he assumed the reels were the business content, and they were not, the carousels were.
Say so plainly and show the number.

**Always answer "where are they beatable."** A teardown that only says "they are good" is
useless. Look for: what they teach shallow in public, what has no ladder, what is
geographically anchored, what they are over-invested in, and what demand they are not
fulfilling. That last one is the opening.

**Never invent a number.** If a price, a list size or an open rate is not in the data, write
**NOT FOUND**. Workspace rule, no exceptions.

**No em-dashes.** Workspace rule, applies to every file this skill writes.

## Ethics, keep this line

These are handles from a public profile's public engagement. In every README, keep the
caution block: **prospects, not leads.** Follow first, engage on their content, then DM.
Bulk-DMing 300 accounts in a day gets an account restricted and reads like a bot. Never
scrape anything behind a private account or a login the user does not own.
