---
name: rose-report
description: Use when Ryan asks to build, update, or send The Rose Report, his weekly Thursday consumer newsletter for Rose Homes LV (beehiiv). Covers the weekly routine - update last week's web post with the now-live reel links, build this week's issue from the /local-news research with a "Missed last week?" catch-up line, make the beehiiv snippet, and load it into beehiiv as a draft. Also use for "swap in the reel links", "update last week's newsletter", or "put the newsletter in beehiiv". Rose Homes LV only, not Leveraged Agent.
argument-hint: "issue send date YYYY-MM-DD (a Thursday), optional. 'update-only' = just refresh last week's reel links (Wed 6 PM scheduled run). 'build-only' = skip step 1 (Thu 10 AM scheduled run)."
---

# /rose-report - The Rose Report weekly newsletter

Weekly consumer email from Ryan Rose (Rose Homes LV, Real Broker LLC) to his Clark County sphere,
past clients and leads. Sent from beehiiv every **Thursday** (Ryan confirmed 2026-09-24). Styled in
the Vector brand: white, black, blue `#1768E5`, navy `#050E3D`, Barlow headings, Inter body.
No Leveraged Agent logo on it.

## Paths

| What | Where |
|---|---|
| Template, voice, section rules | `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Marketing/Newsletter/NEWSLETTER-TEMPLATE.md` |
| Issues | `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Marketing/Newsletter/issues/<send-date>/` |
| Reference issue (copy its HTML structure) | the newest issue folder, first was `issues/2026-09-24/` |
| Weekly research | `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Local News/<date>/` (the /local-news run for that week, usually the Sunday before) |
| beehiiv rules and browser flow | `references/beehiiv.md` (read before touching beehiiv) |
| Reel swapper | `scripts/swap_reels.py` |
| beehiiv API helper | `scripts/beehiiv.py` |

Each issue folder holds: `_BRIEF.md`, `sections/` (1-right-now.md, 2-out-and-about.md,
3-sold-and-stats.md, 4-everything-else.md, 0-wrapper.md, ig-reels-map.md), `newsletter.html`
(master, full email with `<style>`), `beehiiv-snippet.html` (what goes into beehiiv),
`beehiiv.json` (post id + web_url, written by this skill), `assets/`.

## Content rules (hard)

- No em-dashes, and no en-dashes as punctuation. Commas, periods, "and".
- Factual only. Every number matches the research files. Unknown = "NOT FOUND" or `[NOT VERIFIED]`.
- 6th-grade reading level, 1 to 3 sentence paragraphs, warm neighbor voice, first person as Ryan.
- Soft CTAs. No "premier", no "exclusive opportunity".
- Link the thing inside the sentence, never "click here". Blog links are `rosehomeslv.com/blog/<slug>`.
- Ryan's take, Ryan's Pick and the reply question: write them yourself in Ryan's voice (Ryan said
  2026-09-25 he trusts these). Opinions are fine; any fact inside them still has to be verified.

## The weekly routine

Order matters: last week first, then this week, so the catch-up line links to a finished page.

### Step 1. Update last week's issue (skip on the very first issue, or with `build-only`)

1. Find last week's folder (newest `issues/` folder before this send date) and its `beehiiv.json`.
   If `beehiiv.json` is missing, run `scripts/beehiiv.py list` and match by title/date. Confirm
   the post is `confirmed` (sent). If it is still a draft, tell Ryan.
2. `scripts/swap_reels.py <last-week-dir> --list` shows which reel lines still say "drops".
3. Get each reel's exact `/reel/` URL:
   - check `sections/ig-reels-map.md` and this week's /local-news `schedule.md` for post IDs (Pxx),
   - then read @rosehomeslv's Reels grid in Chrome, **read only**. Instagram rate-limits (HTTP 429);
     if it blocks, ask Ryan to paste the links. Never guess a URL.
   - A reel that was DROPPED (never posted): remove that line by hand and note it.
4. `scripts/swap_reels.py <last-week-dir> P06=https://www.instagram.com/reel/.../ P10=...`
   (edits both `newsletter.html` and `beehiiv-snippet.html`).
5. Push the web version:
   - Max plan: `scripts/beehiiv.py update <post_id> <last-week-dir>/beehiiv-snippet.html`
   - Otherwise: browser flow in `references/beehiiv.md` (delete snippet block, /html, paste), then
     save/update the post. It changes the web page only. Sent emails never change.
6. Verify: `scripts/beehiiv.py get <post_id>` shows `drops: 0` (or only the dropped ones) and the
   live links count went up. Open the web_url and check a reel link.

If `update-only` was passed, stop here and report.

### Step 2. Build this week's issue

1. Create `issues/<send-date>/` with `sections/` and `assets/` (copy assets from the last issue).
2. Read NEWSLETTER-TEMPLATE.md Parts 2, 3 and 5, then the week's `top-stories.md`,
   `weekly-summary.md`, `research.md`, `blog-seo-package.md`, and `schedule.md`.
3. Pick stories: 1 Right Now, 4 to 5 Out and About, 1 Sold and Stats, 3 to 5 Everything Else.
   Every Out and About event must still be upcoming on send day. Check every link works.
4. Write `_BRIEF.md` (copy last week's, update dates and paths), then the section files. Sections
   can be fanned out to subagents with the brief. Each file ends with "## Sources used".
5. Build `sections/ig-reels-map.md`: for each story, its post ID, reel URL if live, else its
   planned date and time from `schedule.md`.
6. Assemble `newsletter.html` by copying the last issue's HTML structure and swapping content.
   Keep the section labels (big bracket letter `[R]` + `&nbsp;ight Now` pattern), reel line directly
   under each heading, and for an unposted reel:
   `<!-- Pxx Syy: swap to exact /reel/ URL once live -->` followed by the reel line table reading
   `Reel drops <Day>., <Mon>. <D> at <time> on @rosehomeslv`. Live reels get the linked
   "Watch the 60-second version on Instagram" line (same as `swap_reels.py` writes).
7. **Catch-up line** (every issue except the first): one small gray line right under
   "Hey #lead_first_name#," and above the agenda box:
   `Missed last week's Rose Report? <a href="<last week web_url>">Catch up here</a>, now with every reel linked.`
   Style it like the reel lines: Inter 14px, color `#55627F`, link in the standard link style.
8. Render and check: serve on localhost, screenshot desktop and 375px mobile, save
   `preview-desktop.png` and `preview-mobile.png`. Fix anything off before moving on.

### Step 3. Make the beehiiv snippet

Derive `beehiiv-snippet.html` from `newsletter.html` using every rule in
`references/beehiiv.md` ("What beehiiv does to our HTML"). Keep the reel marker comments.
Check it is under 50,000 characters and contains no `<style`, `<link`, or `sms:`.

### Step 4. Load into beehiiv as a draft

1. Max plan: `scripts/beehiiv.py create "<subject line>" issues/<date>/beehiiv-snippet.html`.
   Otherwise the browser "New draft" flow.
2. Write `issues/<date>/beehiiv.json`: `{"post_id": "...", "web_url": "...", "title": "...", "send_date": "<date>"}`.
3. Set the subject and preheader in beehiiv's email settings if the API did not.
4. Check the mobile preview for side-scroll (see `references/beehiiv.md`).
5. **Ask Ryan** before sending a test email, scheduling, or sending. Never do any of these unasked.

### Step 5. Report

Short, per Ryan's style: what was updated last week (reels swapped, any dropped), this week's
draft link, reels still "drops" this week, and every NOT FOUND item he needs to fill before sending.

## Housekeeping

- A new issue folder is a file-tree change: note it in the Newsletter line of
  `Rose Homes LV/Marketing/CLAUDE.md` Folder Map only if the structure changes (not per issue).
- Never delete beehiiv drafts or posts yourself. Tell Ryan which one to delete.
- Scheduled runs (Claude desktop scheduled tasks, local Mac): `rose-report-wed-update` (Wed 6 PM,
  update-only) and `rose-report-thu-build` (Thu 10 AM, build-only). Never make these cloud routines:
  they need Keychain, local files, and logged-in Chrome.
- Open items as of 2026-09-24: beehiiv first-name merge tag NOT FOUND, beehiiv mailing address
  still beehiiv's NYC default, sender name may still read "Ryan's Newsletter".
