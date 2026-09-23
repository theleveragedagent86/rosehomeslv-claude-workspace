# Deliverables

Everything lands in
`SKOOL Community/Instagram/Competitor-Research/<Coach-Name>/`.

```
<Coach-Name>/
├── README.md                     index + caveats + the caution block
├── STRATEGY-TEARDOWN.md          the analysis, 10 sections
├── NEWSLETTER-TEARDOWN.md        only if there was email
├── POST-CATALOGUE-<year>.md      the full post table
├── MASTER-PEOPLE-LOG.csv
├── LIST-A-hot-AI-commenters.csv
├── LIST-B-business-commenters.csv
├── LIST-C-repeat-engagers.csv
├── LIST-D-RE-name-signal.csv
├── LIST-E-likers-only.csv
├── PER-POST-COMMENTER-LOG.csv
├── TOP-300-DM-TARGETS.csv
└── data/                         raw JSON so any list can be re-cut
```

## README.md

Opens with the account snapshot: followers, following, posts, verified, what they sell, and
one line on whether their audience is Ryan's avatar.

Then **Start here** with three links: the strategy teardown, the top 300, the post catalogue.
Then the newsletter teardown if it exists.

Then the list table, one row per CSV with the row count and who is in it.

Then **"What was captured, and what could not be."** Be specific and honest:
- likers capped at ~190 per post by Instagram, no pagination
- follower lists not exposed
- public comment counts roughly double the human count, and why
- date ranges actually covered

Then the data files, then the caution block, verbatim:

> These handles came from a public profile's public engagement. They are prospects, not
> leads. Follow first, engage on their content, then DM. Bulk-DMing 300 accounts in a day
> from a fresh account gets it restricted.

## STRATEGY-TEARDOWN.md, the 10 sections

1. **The one mechanic.** Whatever the account actually runs on. Lead with it. Prove it with
   the CTA lift table. End with "what Ryan should copy verbatim", 3 bullets.
2. **Format.** Which format converts, with the comment:like ratio, and by how much.
3. **Topics.** The performance table, and which topic is their best and their worst.
4. **Hooks.** The pattern in the winners, the pattern in the losers, and 3 hooks for Ryan
   in the same shape.
5. **Captions.** Length, structure, where the ask sits.
6. **Posting cadence and volume.** Including anything they have admitted publicly.
7. **The offer ladder.** Every keyword they use and what each one delivers.
8. **Month over month.** Are they growing, flat, or coasting.
9. **What to steal, in priority order.** Numbered, most valuable first.
10. **Where they are beatable.** Never skip this. What is shallow in public, what has no
    ladder, what is geographically anchored, what they are over-invested in, and what demand
    they have created but are not fulfilling.

## POST-CATALOGUE-<year>.md

One markdown table, one row per post, sorted by date desc:

`date | type | CTA keyword | topic | likes | comments | plays | link | hook`

The hook column is the first line of the caption, truncated to about 90 characters.

## The CSVs

`MASTER-PEOPLE-LOG.csv`
`handle, name, comments, likes, posts_touched, first_seen, last_seen, sample_1, sample_2, sample_3`

`PER-POST-COMMENTER-LOG.csv`
`post_code, post_date, post_hook, handle, name, comment_text, comment_date`

`TOP-300-DM-TARGETS.csv`
`rank, handle, name, score, ai_comments, biz_comments, likes, posts_touched, last_seen, sample_comment`

Lists A through E carry at minimum `handle, name, comments, likes, last_seen`.

## Writing rules, all files

- **No em-dashes.** Workspace rule.
- **NOT FOUND** for anything you do not have. Never estimate a price, a list size, or an
  open rate.
- Short sentences. Say the number, then say what it means.
- Every claim in the teardown traces to a table in the same file.
- Correct Ryan's stated assumptions when the data disagrees, plainly, with the number.

## Last step, always

Update the Folder Map in `SKOOL Community/CLAUDE.md` with the new teardown folder, the row
counts, and the one-line headline finding. Workspace maintenance rule, not optional.
