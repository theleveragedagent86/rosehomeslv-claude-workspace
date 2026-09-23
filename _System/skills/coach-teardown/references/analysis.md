# Analysis recipes

Run all of this in Python via Bash, reading from `data/`. **Never load the raw JSON into the
conversation.** Print only aggregates and small tables.

## Realtor detection

Used for `LIST-D` and for the +25 scoring bonus. Matches handle or display name.

```python
import re
RE_PAT = re.compile(
  r'realtor|real ?estate|\brealty\b|broker|\bagent\b|homes?\b|properties|property|'
  r're/?max|remax|keller ?williams|\bkw\b|compass|coldwell|century ?21|\bc21\b|\bexp\b|'
  r'sotheby|berkshire|\bbhhs\b|elliman|listing|\bmls\b|sells|selling|\bloan|mortgage|'
  r'lender|\bnmls\b|escrow|realestate|\bsold\b|relocat|dre ?#|lic ?#', re.I)
```

It over-matches slightly on `\bagent\b` and `homes?\b`. That is deliberate, a false positive
costs a follow, a false negative costs a prospect.

## Topic classifier

Runs on the caption. Tune the buckets to the coach, keep `AI/Claude` first, it is the one
that matters for Ryan.

```python
def topic(c):
    c = (c or '').lower()
    if re.search(r'claude|chatgpt|\bai\b|prompt|automat|cowork|agent os', c): return 'AI/Claude'
    if 'open house' in c: return 'Open House'
    if re.search(r'listing|seller|commission|price|cma|expired', c): return 'Listing/Seller'
    if re.search(r'buyer|nar |representation', c): return 'Buyer'
    if re.search(r'follow up|crm|database|lead|script|cold call|prospect', c): return 'Leads/Followup'
    if re.search(r'team|hire|scale|recruit', c): return 'Team/Scale'
    if re.search(r'instagram|content|reel|social|funnel|linktree|youtube', c): return 'Content/Social'
    if re.search(r'wife|baby|family|friend|gym|birthday', c): return 'Personal'
    return 'Mindset/Other'
```

## Keyword CTA detection

The single most important extraction. Find the word people are told to comment.

```python
CTA = re.compile(r'comment\s+["“]?([A-Za-z][A-Za-z0-9 ]{1,24})["”]?', re.I)
def cta(caption):
    m = CTA.search(caption or '')
    return m.group(1).strip().upper() if m else None
```

Then build two tables:

1. **The lift table.** For each format, median comments with a CTA versus without.
   Report it as a multiple. This is the headline number of the whole teardown.
2. **The keyword frequency list.** Count what commenters actually typed across the whole
   comment corpus, not just what the captions asked for. Their offer ladder, in public.

```python
from collections import Counter
words = Counter()
for row in comments:
    t = (row[4] or '').strip().lower()
    if 1 <= len(t.split()) <= 3:
        words[t] += 1
```

## The coach's own replies

Filter them out of the people lists, then count them separately. On Peyson, 7,370 of 45,969
comment rows were his own replies ("Sent!", "Just sent it"). That number IS a finding: it
proves he answers every keyword by hand or by automation, and it explains why the public
comment count is roughly double the number of real humans.

## Scoring for TOP-300

```
score = ai_comments      * 12
      + biz_comments     *  4
      + biz_likes        *  1
      + 25 if realtor name signal
      + 15 if active in the last 60 days
      + 15 if active in the last 30 days
```

Sort desc, take 300. Columns: handle, name, score, ai_comments, biz_comments, likes,
posts_touched, first_seen, last_seen, sample_comment.

## Tables the teardown must contain

| Table | Columns |
|---|---|
| CTA lift | format, n, median comments with CTA, without, multiple |
| Format | format, n, share of posts, share of comments, median comment:like ratio |
| Topic | topic, n, median comments, median likes, median plays |
| Month | month, posts, % with CTA, median comments, total comments |
| Top 20 posts | date, format, topic, comments, likes, hook, link |
| Bottom 20 posts | same, to show what does not work |
| Keywords | keyword, times typed |

## Hook analysis

Take the first line of the top 20 and the bottom 20 posts and compare. Look for:

- Does the hook end in a question mark? (On Peyson, the winners never did.)
- Does it lead with a number or a receipt?
- Is it a claim, a confession, or a promise?
- Does it name the enemy ("prompt library", "just wait for rates")?
- Is there a "prove me wrong" style provocation, and what did it earn?

Report the pattern, then give Ryan three hooks in the same shape for his own brand.

## Sanity checks before writing

- Harvested comment rows should be roughly **half** the sum of public `comment_count`. If it
  is much less, pagination broke. If it is close to equal, you probably counted the coach's
  replies as humans.
- Unique accounts should be far smaller than total rows. If they are close, dedupe failed.
- Spot check three handles by opening their profile. If they are not agents, the topic
  classifier or the list cut is wrong.
