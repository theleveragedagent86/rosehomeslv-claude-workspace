# The back-catalog refresh loop

New thumbnails are the obvious use. The money is in the old ones: a video with high
impressions and low click-through is an audience that already found you and declined.

## The loop

1. **Audit**: rank every published video by click-through rate.
2. **Diagnose**: for each low performer, name *why* it loses the click. One reason.
3. **Redesign**: build two concepts that fix that specific flaw.
4. **Approve**: Ryan picks. Nothing publishes without that.
5. **Prove**: record CTR before and after, with the date of the swap.

Revival priority is **high impressions + low CTR**, not lowest CTR. A video nobody is
being shown will not be saved by a new thumbnail; a video shown 40,000 times at 2% is
money on the table.

## Getting the CTR data

Click-through rate is owner-only. No scraper or third-party tool can see it, so it has to
come out of Ryan's own account. Two routes:

**Manual (works today).** YouTube Studio → Analytics → Content → set the date range →
export the table as CSV. Save it as `ctr-export-YYYY-MM-DD.csv` in the working folder.
The columns that matter are video title, impressions, impressions CTR, and views.

**Connected (not wired yet).** The YouTube Data API lists the back catalog and can set a
new thumbnail on a video directly; the YouTube Analytics API returns per-video CTR. Both
are reachable through Composio, which is free. Wiring that up turns steps 1 and 4 into
one command instead of a CSV round-trip. Until then this skill reads the CSV.

## Diagnosis checklist

Work down it and stop at the first one that is true. That is the flaw to fix.

1. **Unreadable at 120px**: too many words, or type too small. Most common by far.
2. **No face, or a face with no expression**: nothing to react to.
3. **Expression contradicts the claim**: smiling under a warning headline. The viewer
   reads the mismatch as inauthentic before they read the words.
4. **Blends with the category**: same colour and layout as everything around it.
5. **Thumbnail repeats the title**: the pair wastes half its surface area.
6. **Generic location**: an anonymous skyline where a local expected somewhere they know.

## Logging

Append every swap to `refresh-log.md` in the channel folder:

```
| Date | Video | Old CTR | Flaw fixed | New CTR (30d) |
```

Without the log there is no way to tell whether a redesign worked or the algorithm
just moved, and the whole loop becomes superstition.
