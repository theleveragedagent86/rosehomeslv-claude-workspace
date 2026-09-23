# The email half of the funnel

Instagram is acquisition. **Coaches sell in email.** A teardown that stops at Instagram will
conclude the coach has no offer, which is usually wrong.

## Getting it

Ryan forwards it, or it is already in his Gmail. Ask once, do not go digging unprompted.

```
mcp__6d26fa00-271c-46cd-8609-101a9f9f3951__search_threads
  query: "<coach last name> OR \"<Newsletter Title>\""
```

Then `get_thread` with `messageFormat: PLAIN_TEXT`. A forwarded bundle of many issues will
blow the token cap and get written to a file instead. That is fine, parse the file.

**Plain text loses every URL.** Anchor text survives, hrefs do not. If the button targets
matter, re-pull with `messageFormat: FULL_CONTENT` and parse the HTML.

## Splitting a bundle

A forwarded chain is usually one thread with all issues concatenated. Split on the masthead:

```python
parts = body.split('<MASTHEAD TEXT>')[1:]   # e.g. 'IN THE TRENCHES'
```

Date each issue from its own content: the Freddie Mac figure with its date, a Fed meeting
date, an event reference. Do not guess from headers, forwarded mail loses them.

## What to extract per issue

| Extract | Why it matters |
|---|---|
| The block structure | Coaches use a fixed template. Find the slots. |
| Every offer, and where it sits | How many asks per issue, and in what order |
| The scarcity device | Seat counters, deadlines, "final spots" |
| The reply trigger | "Reply and I will send it" is the email version of a comment keyword |
| What the paid room was taught | **The most valuable column in the whole file** |
| The market/data block | The retention device that makes it get opened |
| Personal narrative threads | The parasocial hook, tracked across issues |
| Named guests | Their bench, and who else to research |
| Free lead magnets | The top of their ladder |
| Sending platform | From the footer |

## The one column that matters most

Build a table of **what the paid mastermind or group covered each week**. Coaches recap it in
the newsletter to sell the room, which means they publish their own curriculum. On Peyson,
eight weeks of that column showed Claude Code, Cowork, ManyChat twice, and AI clones. That is
Ryan's course being taught live to a paying audience, and nothing on the coach's Instagram
would ever have told you.

## Structure of NEWSLETTER-TEARDOWN.md

1. Source and capture caveats, including what the plain text lost
2. The headline finding, usually "Instagram acquires, email sells", with a funnel diagram
3. The template table, one row per block, with how many issues it held in
4. The paid-room curriculum table, dated
5. The market/data block, its exact shape, with the numbers tracked across issues
6. What they do that Ryan does not, numbered, with a quote for each
7. Where they are beatable, updated against the Instagram teardown
8. What to copy, in priority order
9. Gaps, with everything unknown marked NOT FOUND

Then cross-link it from the README and add a note at the top of the "where they are beatable"
section of `STRATEGY-TEARDOWN.md`, because the email will usually contradict it.
