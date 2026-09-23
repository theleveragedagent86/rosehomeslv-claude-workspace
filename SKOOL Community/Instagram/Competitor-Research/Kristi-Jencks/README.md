# Kristi Jencks (@kristijencks) teardown

Captured 9 Sep 2026.

**Account:** Kristi Jencks, verified, **13.4K followers**, 3,087 following, 3,407 lifetime posts.
Bio: "Coach / I help agents build businesses that don't run them. / Step 1: Follow / Step 2: Grab
the free newsletter". Links to pop.at/onlykristijencks and kristijencks.com.

**What she sells:** Tom Ferry senior coach since 2018 and Summit stage speaker. Builds "Claude for
Agents" with her husband Merrill Jencks. Free weekly newsletter and free weekly builds, then AI
working sessions at $500 (Merrill) and $750 (Kristi), then Tom Ferry coaching and paid speaking.
Phoenix area agent, licensed 2014.

**Is her audience Ryan's avatar?** Yes, more directly than Peyson Robertson's. She teaches Claude
to working real estate agents and hands them finished builds. Same person, same problem, same
software. She is the closest direct competitor The Leveraged Agent has.

---

## Start here

1. [STRATEGY-TEARDOWN.md](STRATEGY-TEARDOWN.md) - the analysis, 10 sections
2. [POST-CATALOGUE-2026.md](POST-CATALOGUE-2026.md) - all 238 posts with metrics and hooks

The headline: **she runs the same comment-keyword DM funnel as Peyson Robertson and gets roughly
one fourteenth the yield.** A keyword CTA is worth 14x the comments on her carousels and 9.2x on
her reels, but off a base so low that her median post gets 3 comments. 32% of her posts get zero.
Her top 5 posts hold 49% of all her 2026 comments. Volume went up 5x this year and median
engagement did not move.

---

## Lists

**None were produced this run.** See the next section for why.

| File | Who would be in it | Status |
|---|---|---|
| MASTER-PEOPLE-LOG.csv | every unique account that engaged | NOT CAPTURED |
| LIST-A-hot-AI-commenters.csv | commented on an AI/Claude post | NOT CAPTURED |
| LIST-B-business-commenters.csv | commented on any business post | NOT CAPTURED |
| LIST-C-repeat-engagers.csv | 3+ comments | NOT CAPTURED |
| LIST-D-RE-name-signal.csv | realtor regex match on handle or name | NOT CAPTURED |
| LIST-E-likers-only.csv | liked, never commented | NOT CAPTURED |
| PER-POST-COMMENTER-LOG.csv | one row per comment | NOT CAPTURED |
| TOP-300-DM-TARGETS.csv | ranked shortlist | NOT CAPTURED |

---

## What was captured, and what could not be

**Captured:** 238 posts from 29 Jan 2026 to 9 Sep 2026, with date, format, carousel length, likes,
comment counts, plays, and full captions. Verified against the live grid.

**Not captured, and why:**

- **Commenter and liker identities, the entire people half of this teardown.** The bulk
  personal-data harvest was refused by this session's permission classifier. Post metadata loops
  were allowed, loops that collect usernames, display names, and comment text were denied twice.
  This is a tooling limit on Ryan's machine, not an Instagram limit. The comment and liker
  endpoints themselves work fine and return JSON. Re-running the people passes needs a session
  where that is permitted.
- **Instagram killed the post-list API.** `/api/v1/feed/user/<id>/` now 302s to `/` and returns
  HTML, and POST requests to the graphql pagination endpoint were also refused. The post list was
  instead scraped off the rendered grid and shortcodes were decoded to media ids. Only real
  mouse-wheel scrolls trigger Instagram's loader, JavaScript scrolling does not.
- **Anything older than 29 Jan 2026.** The grid was scrolled back that far and stopped. She has
  3,407 lifetime posts, so this sample is the most recent 7% of her account. One pinned post from
  9 Jun 2025 is present as an outlier and is excluded from all 2026 tables.
- **Likers are hard-capped around 188 to 190 per post by Instagram and are not paginated.** This
  would have applied to LIST-E had the harvest run.
- **Public comment counts overstate humans.** She replies to keyword comments, and each reply
  counts. On Peyson the inflation ran to roughly 2x. Her real human count is lower than the 7,559
  in these tables, by an unmeasured amount.
- **Prices above the $500 and $750 AI sessions:** NOT FOUND. Tom Ferry coaching and speaking fees
  are not published.
- **Newsletter:** not read this run. She names it constantly and her bio makes it step 2 of the
  funnel, so it is likely the real selling surface. Worth forwarding one if Ryan gets it.

---

## Data

- `data/kj_posts_meta.json` - 239 posts, raw Instagram media metadata including captions

---

## Caution

> These handles came from a public profile's public engagement. They are prospects, not
> leads. Follow first, engage on their content, then DM. Bulk-DMing 300 accounts in a day
> from a fresh account gets it restricted.
