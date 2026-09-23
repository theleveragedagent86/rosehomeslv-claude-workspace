# Kimberly Prince, @kindlykimberly

Competitor teardown for The Leveraged Agent. Captured 10 Sep 2026.

## Snapshot

| | |
|---|---|
| Handle | [@kindlykimberly](https://www.instagram.com/kindlykimberly/) |
| Name | Kimberly Prince, SACRAMENTO REALTOR |
| Followers / following / posts | 11.5K / 2,533 / 1,337 |
| Verified | yes |
| Brokerage | eXp Realty, DRE 01977518 |
| Bio | Luxury + Relocation. Serving Sacramento + OC. Host of In Your Neighborhood @gooddaysac. Download the Relocation Realtor Playbook |
| Link | stan.store/KPrinceHomes |
| Highlights | Join, REDD Group, Sales, About, REDD Retreat |
| Pinned | 3 pinned grid posts, all REDD Group / brand, no separate pinned reels |
| What she sells | $17 agent transaction checklist, $34 Relocation Realtor Playbook, $97/month Powerhouse Try On challenge, and the real offer: join eXp under The REDD Group |

**Is her audience Ryan's avatar?** Partly, and the part that is, is very good. 19% of her 1,136
commenters carry a realtor signal in the handle or name. On her agent-facing posts it rises to
26%. The rest are Sacramento consumers looking at luxury listings. Work LIST-B and
TOP-300-DM-TARGETS, not the master log.

## Start here

1. [STRATEGY-TEARDOWN.md](STRATEGY-TEARDOWN.md) ,  the analysis, 10 sections. The headline: one property, one made-up keyword, 4x.
2. [TOP-300-DM-TARGETS.csv](TOP-300-DM-TARGETS.csv) ,  ranked shortlist, agent-facing engagement weighted heaviest.
3. [POST-CATALOGUE-2026.md](POST-CATALOGUE-2026.md) and [POST-CATALOGUE-2025.md](POST-CATALOGUE-2025.md) ,  every captured post.

No newsletter teardown. Ryan has not forwarded an email from her and no Gmail check was run.

## The lists

| file | rows | who is in it |
|---|---|---|
| MASTER-PEOPLE-LOG.csv | 1,136 | every unique commenter, with counts, dates and 3 sample comments |
| LIST-A-hot-AI-commenters.csv | 21 | commented on one of her 7 AI posts. Thin on purpose, see below |
| LIST-B-business-commenters.csv | 367 | commented on an agent-facing post (Recruiting/REDD or AI). **The best list on this account.** 97 carry a realtor signal |
| LIST-C-repeat-engagers.csv | 107 | 3 or more comments, habitual |
| LIST-D-RE-name-signal.csv | 219 | handle or display name matches the realtor regex |
| LIST-E-likers-only.csv | 4,784 | liked, never commented. Coldest. 657 carry a realtor signal |
| PER-POST-COMMENTER-LOG.csv | 1,821 | one row per comment with the post hook and the comment text |
| TOP-300-DM-TARGETS.csv | 300 | ranked shortlist |

**LIST-A is deliberately small.** The standard list definition is "commented on an AI or Claude
post". Kimberly has posted about AI seven times in 216 posts. That is itself the most important
competitive finding on this account, so the list is reported honestly rather than padded.
LIST-B is the equivalent hot list here.

**Scoring for TOP-300 was adapted** because the AI bucket is too thin to rank on. Used:
`ai_comments x12 + agent_facing_comments x8 + consumer_comments x4 + likes x1 + 25 if realtor
name signal + 15 if active in 60 days + 15 if active in 30 days`. Score range in the file: 358
down to 30. The top 13 are all named, verified-looking California realtors.

## What was captured, and what could not be

Be careful with these. Three of them change how the numbers read.

- **216 of her 1,337 posts.** The post-list API endpoint is dead, so the catalogue comes from scraping the rendered grid. Instagram virtualises that grid, so rows that scroll far out of view get dropped from the DOM before they can be read. Captured range is 24 Jan 2025 to 9 Sep 2026, and **Feb to Apr 2025 and Sep 2025 are missing entirely** from that range. Recent months are the most complete. Treat month-over-month totals as directional, not exact.
- **Like counts are hidden on this account.** 192 of 216 posts return `like_count: 3`, which is the friends facepile, not the real number. Every "likes" column in these files is the **harvested liker sample**, median 61 per post, max 102. It is a floor and a relative signal, not the true like count. Her real like counts are NOT FOUND.
- **Comment threads were not fetched.** The harvest pulled 1,821 human top-level comments against a public comment_count sum of 3,167, so roughly 42% of the public number is replies inside threads. Only 17 top-level rows are hers, so unlike most coaches she is not visibly replying in public. Fulfilment happens in DM.
- **Likers are not paginated by Instagram** and are capped per post. On this account the cap landed lower than usual, median 61 and max 102 per post, so a reel with tens of thousands of plays contributes at most ~100 liker rows.
- **Follower lists are not exposed.** There is no way to get "everyone who follows her."
- 7 of the 216 posts are collabs owned by other accounts (kpastortrinidad, angie.counts.realtor, caylajordan_realestate). They are flagged in the raw data and counted in the totals.

## Data files

`data/posts_meta.json` (216 posts, full captions), `data/comments_0.json` (1,838 raw comment
rows including her own), `data/likers_0.json` and `data/likers_1.json` (13,205 liker rows).
Every list above can be re-cut from these without touching Instagram again.

## Caution

> These handles came from a public profile's public engagement. They are prospects, not
> leads. Follow first, engage on their content, then DM. Bulk-DMing 300 accounts in a day
> from a fresh account gets it restricted.
