# Whitney Bartlette, competitor teardown

Captured **9 Sep 2026** for The Leveraged Agent. Not Rose Homes LV work.

## Account snapshot

| field | value |
|---|---|
| handle | [@whitneybartlette.social](https://www.instagram.com/whitneybartlette.social/) |
| followers | 932,603 |
| posts on profile | 994 |
| verified | no |
| what she sells | a Skool community at $29/mo, 133 members (checked 9 Sep 2026) |
| implied MRR | roughly $3,857/mo, so a **0.014% follower-to-member conversion** |
| pinned | three pins, all keyword sales posts |
| is this Ryan's avatar | **partly.** 3.8% of her engaged accounts carry a realtor or lender name signal. This is a mechanics steal first, an audience steal second. |

## Start here

1. **[STRATEGY-TEARDOWN.md](STRATEGY-TEARDOWN.md)** the analysis, ten sections. Read
   section 1 and section 10 if you read nothing else.
2. **[TOP-300-DM-TARGETS.csv](TOP-300-DM-TARGETS.csv)** the ranked shortlist.
3. **[POST-CATALOGUE-2026.md](POST-CATALOGUE-2026.md)** all 228 posts with keyword, topic,
   likes, comments, plays, hook.

Newsletter teardown: **NOT FOUND**. No email captured. Ask Ryan whether to check Gmail.

## The headline

She runs a keyword-to-DM machine and nothing else is the business. **58% of every human
comment on the account is a person typing a trigger word.** She replied by hand **17 times
in 18,149 comment rows**. Her AI posts convert 4.4x her median topic and she sells no AI
product. That gap is the opening.

## The lists

| file | rows | who is in it |
|---|---|---|
| `MASTER-PEOPLE-LOG.csv` | 28,461 | every unique account seen, with counts and first/last seen |
| `LIST-A-hot-AI-commenters.csv` | 2,690 | commented on an AI/Tools post. **The best list.** |
| `LIST-B-business-commenters.csv` | 10,479 | commented on any business, growth, or craft post |
| `LIST-C-repeat-engagers.csv` | 506 | 3 or more comments, habitual |
| `LIST-D-RE-name-signal.csv` | 1,089 | handle or display name matches the realtor/lender regex |
| `LIST-E-likers-only.csv` | 13,610 | liked, never commented, coldest |
| `PER-POST-COMMENTER-LOG.csv` | 18,132 | one row per human comment, with the post hook and the comment text |
| `TOP-300-DM-TARGETS.csv` | 300 | ranked shortlist, scoring in the skill's `analysis.md` |

## What was captured, and what could not be

Be specific about this before quoting any number from here.

- **228 of 994 posts, so 23% of the account.** Instagram killed
  `GET /api/v1/feed/user/<id>/` (it 302s to the app shell), so posts had to be enumerated by
  scraping the rendered profile grid. Only real mouse-wheel scrolls load more of that grid;
  JavaScript scrolling moves the viewport and loads nothing. **This method never reaches the
  full account.**
- **Date range covered: 18 Feb 2025 to 9 Sep 2026.** Dense from Dec 2025 forward. The single
  Feb 2025 post is a pin, not evidence of coverage of early 2025. Anything older than
  Dec 2025 is **not** in this capture.
- **Comments: 18,149 rows against 31,518 public comment_count, so 58%.** The gap is threaded
  replies, which were not fetched. On the biggest posts the shortfall is larger: the 3,962
  comment reel yielded 2,400 rows.
- **Likers are capped.** Median 100 rows per post, max 201, and Instagram does not paginate
  them. On a reel with 473,106 likes this capture holds about 100 of them. Liker counts here
  are a sample, never a total.
- **48 of 228 posts report a like_count of 3**, which is Instagram hiding the number, not a
  real value (those same posts return up to 101 liker rows). Every likes-based statistic in
  the teardown **excludes** those 48 posts, and the post catalogue shows them as `NOT FOUND`.
- **Follower lists are not exposed.** There is no way to get everyone who follows her.
- **DM payloads are not visible.** What each keyword actually delivers is **NOT FOUND**. Only
  the demand is measurable.

## Data files

`data/` holds the raw JSON so any list can be re-cut without touching Instagram again.

| file | contents |
|---|---|
| `wb_meta_228.json` | 228 posts, full metadata and captions |
| `wb_comments_228_0.json`, `wb_comments_228_1.json` | 18,149 comment rows |
| `wb_likers_228_0.json`, `wb_likers_228_1.json` | 22,568 liker rows |
| `posts_derived.json` | the derived post table (format, topic, CTA keyword) |
| `wb_info_1.json`, `wb_comments_1.json`, `wb_likers_1.json` | the earlier 12 post partial capture, superseded |

`build.py` re-cuts every CSV, the post catalogue and all the analysis tables from `data/`.
Run it from this folder with `python3 build.py`.

## Caution

> These handles came from a public profile's public engagement. They are prospects, not
> leads. Follow first, engage on their content, then DM. Bulk-DMing 300 accounts in a day
> from a fresh account gets it restricted.
