# Peyson Robertson (@peyson.robertson), competitor research

Harvested 2026-09-01 from a logged-in Instagram session, via Instagram's own web API.
Account snapshot: 29.8K followers, 2,390 following, 556 posts, verified, Coachella Valley
real estate team + "Obsidian" agent bootcamps. Same avatar as The Leveraged Agent: producing
agents who want systems and AI.

## Start here

- **[STRATEGY-TEARDOWN.md](STRATEGY-TEARDOWN.md)** what works, what does not, and the measured
  reason why. Read this first. Covers Instagram only.
- **[NEWSLETTER-TEARDOWN.md](NEWSLETTER-TEARDOWN.md)** the other half of the funnel. His weekly
  email "IN THE TRENCHES", 8 issues, Jul to Aug 2026. Instagram acquires, the email sells: three
  stacked paid offers every week, a fixed 9-block template, and a paid mastermind that has been
  teaching Claude Code, Cowork and ManyChat all summer. Read it right after the strategy teardown.
- **[TOP-300-DM-TARGETS.csv](TOP-300-DM-TARGETS.csv)** the 300 highest-signal people to follow
  and DM, ranked. Start at row 1.
- **[POST-CATALOGUE-2026.md](POST-CATALOGUE-2026.md)** all 319 of his 2026 posts with date,
  format, keyword CTA, topic, likes, comments, plays, link and hook.

## The people lists

Every list is a CSV with `handle` and `profile_url` so it drops straight into an outreach sheet.

| File | Rows | What it is |
|---|---|---|
| `MASTER-PEOPLE-LOG.csv` | 33,738 | Every unique account that commented on or liked anything. Comments, likes, posts touched, first/last seen, 3 sample comments. |
| `LIST-A-hot-AI-commenters.csv` | 8,689 | Commented on one of his AI/Claude posts. **Highest realtor + AI-intent overlap. This is the list.** |
| `LIST-B-business-commenters.csv` | 18,032 | Commented on any real-estate business/strategy post (excludes personal + pure-motivation posts). |
| `LIST-C-repeat-engagers.csv` | 3,094 | Commented 3+ times. Warm, habitual, will recognise a DM. |
| `LIST-D-RE-name-signal.csv` | 12,828 | Handle or display name contains a real-estate signal (realtor, realty, broker, brokerage name, NMLS, DRE, etc). |
| `LIST-E-likers-only.csv` | 14,867 | Liked but never commented. Coldest tier, follow-only. |
| `PER-POST-COMMENTER-LOG.csv` | 37,967 | The raw log: one row per comment, with the post it was on, the hook, the exact comment text and date. Use this to see what a specific person asked for before you DM them. |
| `TOP-300-DM-TARGETS.csv` | 300 | Ranked shortlist. Scoring: AI-post comments x12, business-post comments x4, business-post likes x1, +25 real-estate name signal, +15 active since July, +15 active since August. |

### Column notes
- `RE_name_signal` = `Y` means the name or handle pattern-matches real estate. It is a strong
  filter, not proof. Roughly 38% of the total pool flags.
- `top_keyword_typed` = the keyword they typed at his CTA ("open house", "ai", "prompts"). This is
  the single most useful DM opener you have: they already told you what problem they have.
- `last_active` = date of their most recent comment. Anything from 2026-07 onward is live.

## What was captured, and what could not be

- **Comments: 45,969 rows harvested**, of which 37,967 are third-party (7,370 are Peyson's own
  replies, 632 are pre-2026 fill). Instagram reports 69,234 total comments across the account;
  roughly half of that number is his own replies, and deep reply threads under individual comments
  were not expanded. **Every top-level commenter on every post from 2026 plus every pre-2026 post
  with comments was captured.**
- **Likes: 49,709 liker rows, 19,417 unique accounts.** Instagram caps the public liker list at
  roughly 190 accounts per post regardless of the real like count, so this is the top ~190 likers
  of each of 542 posts, not every liker. There is no way around that cap from outside the account.
- **Not captured:** his follower list (not exposed), DM contents, story/highlight viewers.

## Data files

`data/` holds the raw JSON so any of the lists can be rebuilt or re-cut differently:
`peyson_posts_raw.json` (556 posts, full captions + metrics), `peyson_comments_v2.json`,
`peyson_likers_v2.json`, `peyson_queue.json`, `posts.tsv`.

`data/newsletter_2026-09-01_raw.txt` is the plain-text body of the forwarded Gmail thread holding
8 issues of his newsletter, the source for NEWSLETTER-TEARDOWN.md. Links are not preserved in it;
re-pull the thread as FULL_CONTENT if the button URLs are ever needed.

## Caution

These handles came from a public profile's public engagement. They are prospects, not leads.
Follow first, engage on their content, then DM. Bulk-DMing 300 accounts in a day from
@the.leveraged.agent will get the account actioned.
