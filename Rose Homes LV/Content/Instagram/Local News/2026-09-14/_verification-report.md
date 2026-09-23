# Verification Report, Week of 2026-09-14

Auditor: Verification Agent. Run date 2026-09-14.
Scope: all deliverables in `/2026-09-14/`, including `blogs/` (30) and `blogs/bonus/` (29).

## Summary

| Audit | Result |
|---|---|
| 1. Source link verification | PASS with advisories |
| 2. Blocked sources | PASS |
| 3. Blocked topics | PASS |
| 4. Em-dashes | PASS |
| 5. File completeness | **FAIL** (2 missing deliverables) |
| 6. Fact spot check | PASS, 5 of 5 hold |

Only one hard failure: `story-spreadsheet.md` and `weekly-summary.md` do not exist.

---

## AUDIT 1, Source Link Verification

38 unique source URLs were extracted from `research.md` and fetched individually.

**Result: zero dead links. Zero redirects to unrelated pages. Zero contradictions between a live source and the figure cited.**

### Blocked to automated fetch, needs a human eyeball (13)

These returned an empty body. They are the known bot-blocking Las Vegas outlets, not dead links.

- lasvegassun.com, CCSD pre-K expansion (Sep 8)
- lasvegassun.com, former Fiesta Henderson site (Sep 8)
- lasvegassun.com, Waymo rides to public (Sep 14)
- reviewjournal.com, Switch $196M land buy
- reviewjournal.com, builder opens community at former mining site in Henderson
- reviewjournal.com, high-rise condos record year
- reviewjournal.com, SafeKey enrollment changes
- reviewjournal.com, teachers union data centers school funding
- reviewjournal.com, former casino site Henderson redevelopment
- reviewjournal.com, Waymo limited robotaxi rides
- reviewjournal.com, special ed teacher lawsuit
- reviewjournal.com, Road Warrior Vegas Loop expansion
- reviewjournal.com, 5 questions before training camp

Mitigating note: every one of these blocked RJ and Sun items is paired in `research.md` with at least one independently fetchable source carrying the same figures (FOX5, News 3, Nevada Current, SinBin, KTNV, City of Henderson, CCSD). Nothing rests on a blocked source alone.

The package already discloses this correctly. `blogs/story-30` carries an explicit "[NOT VERIFIED, ... behind the Review-Journal's automated access block]" note on its RJ citation, which is the right handling.

### Loaded with real matching content (25)

Spot-verified headline and figure match on all of them. Notable confirmations:

- neon.reviewjournal.com, Smoke & Fire BBQ, 3315 E. Russell Rd., last service Sep 26, 2026. Matches story 5.
- nevadabusiness.com, LVR August, $475,000 median SFR down 1.0 percent, $299,900 condo, 2,252 sales, 7,590 listings without offers. Matches.
- nevadacurrent.com, CCEA plan, $2B over four years, $240M abated 2023-24, 2 percent rate, 75 percent personal property abatement. Matches story 3.
- nevadacurrent.com, Boulder City Question 1, 14,000 acres inside the 100,000-acre Eldorado Valley Transfer Area, 86,000 acres under easement. Matches story 23.
- news3lv.com, 1,700 Nevada Ready! Pre-K seats, 28 schools, $2M+. Matches story 16.
- news3lv.com, DMV registration spotter 50,000+ reports. Matches story 20.
- thenevadaindependent.com, hearing masters petition filed Sep 4, ~78,000 summary evictions statewide 2025, 53,600 in LV Justice Court. Matches story 24.
- ccsd.net board recap Sep 10, 2026. Loads, primary source, matches.
- cityofhenderson.com Fiesta Henderson release. Headline loads; body is JavaScript-rendered so figures were not retrievable by fetch. Not dead. Flagged as needing a human eyeball if any Henderson-specific number is load-bearing.
- fox5vegas.com Waymo, Parade of Mischief, Foodie Fest, DMV closures, LVR report. All load and match.
- ktnv.com VGK Golf Classic. Loads and matches.
- sinbin.vegas rookie games and goalie rotation. Both load and match.
- vegashockeyknight.com Piiparinen. Loads and matches.
- freddiemac.gcs-web.com, nar.realtor, prnewswire (Realtor.com), redfin.com. All load, all primary, all match.
- seeingorangenv.com traffic alerts. Loads. Caveat: it is a rolling RTC page updated Thursdays, so some entries are stale July and August items. Story 29 should be treated as perishable.

### Primary-source advisories

The instruction asks that a government agency, an MLS or REALTOR association, or a federal data release be cited over an aggregator where it is the true origin. Six cases where an aggregator is cited instead. None is a factual error; all are citation-hygiene items.

1. **Las Vegas REALTORS August median sale price.** True origin is the Las Vegas REALTORS monthly release. Cited as Nevada Business Magazine and FOX5. Appears in stories 2, 6, 13, 14, 15, 30, and bonus 20 and 21. This is the most repeated instance in the package. Recommend adding the LVR release itself alongside the carrier.
2. **Nevada DMV office closures (story 10).** True origin is the Nevada DMV announcement of Sep 8. Cited as FOX5 only.
3. **Nevada DMV registration spotter 50,000 reports (story 20).** True origin is the Nevada DMV. Cited as News 3 only.
4. **Switch $196M Apex land purchase (story 22).** Transaction of record. Cited as the Review-Journal, which is also the blocked-fetch outlet. A Clark County Assessor or recorder reference would harden it.
5. **Boulder City Question 1 (story 23).** True origin is the Boulder City ballot question text and city charter. Cited as Nevada Current. The Nevada Current reporting is accurate; a link to the city's own measure text would be stronger.
6. **CCEA data center tax plan (story 3).** True origin is the CCEA proposal document. Cited as Nevada Current and RJ. Acceptable, since the proposal is not a formal public filing.

Good practice already present: Freddie Mac PMMS, NAR, Realtor.com via PR Newswire, CCSD board recap, and City of Henderson are all cited at the primary source. Stories 4 and 16 pair the local outlet with the government primary, which is the pattern the other six should follow.

---

## AUDIT 2, Blocked Sources

**PASS. Zero violations.**

Searched every deliverable, including `blogs/` and `blogs/bonus/`, for the eight named blocked domains, for competing brokerage and team names, and for individual agents credited as sources.

Every hit on a named blocked domain is an explicit exclusion note in the research or selection files, documenting that the source was found and deliberately not used:

- `_research/local-events.md:258` veryvintagevegas.com found on the Waymo story, not used, Waymo sourced to FOX5 instead.
- `_research/real-estate-local.md:154` lists 22 blocked Clark County seller domains encountered and ignored.
- `_research/real-estate-national.md:177` names nine more, plus a Stacker home-equity item set aside as lender-sponsored content.
- `_research/gov-dev.md:220-221` veryvintagevegas.com and nevadarealestategroup.com encountered, neither used.
- `top-stories.md:555` confirms no competing brokerage, team or agent blog is cited in any selected story, and records that the LVR August rental release was dropped entirely because every outlet carrying it is a Clark County property management company or brokerage.

No blocked domain appears as a link, a citation, or a named source in any published deliverable. No individual competing agent is credited anywhere.

**Advisory, not a violation.** Realtor.com and Zillow appear as data sources across several blogs. Neither is a Clark County brokerage, and both are cited through their own published national reports (PR Newswire releases), so neither falls under the named block or the catch-all. Noting it only so the call is on the record.

---

## AUDIT 3, Blocked Topics

**PASS. Nothing in the 30 selected or 29 bonus stories reads as a blocked topic.**

Keyword sweep across `top-stories.md`, `bonus-stories.md`, `instagram-captions.md`, `video-transcripts.md`, `reddit-posts.md`, `youtube-descriptions.md` and all 59 blogs for racial, ethnic and identity conflict, discrimination accusations, identity-based protest, immigration enforcement, partisan fights, election scandals, culture-war flashpoints, and book or curriculum fights. Every hit was either an exclusion note or an unrelated word sense.

The upstream research agents excluded, and documented excluding: the CCSD police use-of-force racial disparity stories, three Nevada immigration and public charge items, the ICE-at-polling-places lawsuit, the campaign-sign swastika plea deal, the Lone Mountain temple neighborhood fight, the federal sex discrimination suit against a Las Vegas homebuilder, and all 2026 Nevada election and candidate coverage. None was pulled back in at selection, and none received a bonus blog.

### Close read, GD-05 / story 23, Boulder City Question 1

**Clean.** Written as a land-use and city-revenue question throughout. The framing is whether data centers become an approved land use inside the Eldorado Valley Transfer Area, how many acres are involved, what the charter requires, and the lease-rate comparison against solar. No candidate, no party, no campaign, no identity angle. The selection note in `top-stories.md:388` and the rule check at line 554 both state the reasoning explicitly and instruct covering the land use and city revenue, not the campaign around it. The blog follows that instruction.

### Close read, SB-01 / story 3, CCEA data center tax

**Clean.** Written as tax policy. The content is the Local School Support Tax abatement, the 75 percent personal property abatement, the 2 percent reduced sales and use rate, the $240 million abated in 2023-24, and the $2 billion four-year estimate into the pupil-centered funding formula. Opposition is presented as the Nevada State Education Association and the Sierra Club Toiyabe Chapter, which is institutional disagreement over tax design, not a partisan contest. No party, candidate, or election frame anywhere in the story, the transcript, the caption, or the blog.

---

## AUDIT 4, Em-Dashes

**PASS.**

```
grep -rl ', ' /2026-09-14/
```

returned no files. Zero deliverables contain the em-dash character.

One en-dash file exists, `_previously-covered.md`, which is an internal tracking file and not a deliverable. No action needed.

---

## AUDIT 5, File Completeness

**FAIL. Two required deliverables are missing.**

### Missing

| File | Status |
|---|---|
| `story-spreadsheet.md` | **MISSING** |
| `weekly-summary.md` | **MISSING** |

Both are still owned by the in-progress task "Reddit posts, spreadsheet, summary." `reddit-posts.md` from that same task did land, so only the two are outstanding.

### Present and non-trivial

| File | Bytes |
|---|---|
| research.md | 56,942 |
| top-stories.md | 47,918 |
| posting-schedule.md | 20,977 |
| video-transcripts.md | 48,145 |
| instagram-captions.md | 73,000 |
| youtube-descriptions.md | 29,459 |
| blog-seo-package.md | 40,626 |
| bonus-stories.md | 43,406 |
| bonus-blog-seo-package.md | 36,931 |
| reddit-posts.md | 17,830 |

### Blog counts

- `blogs/` contains exactly 30 HTML files, story-01 through story-30. Correct.
- `blogs/bonus/` contains exactly 29 HTML files, bonus-01 through bonus-29. Correct.

### Blog structural checks, all 59 files

Every one of the 59 blogs passes all five requirements. Zero failures.

- `<article>` block: 59 of 59 present.
- `<script type="application/ld+json">` block: 59 of 59 present.
- At least 4 `<img>` tags: 59 of 59 pass. Distribution is 43 files with 5 images and 16 files with exactly 4.
- Contact CTA with 702-747-5921: 59 of 59 present.
- Exactly 3 related blog links: 59 of 59 pass. Counted inside the `<h2>Related Stories</h2>` section up to the closing `<hr>`, which is the correct boundary. Raw counts of `rosehomeslv.com/blog` links per file run higher (4 to 6) because the CTA and in-body links also point at the blog, but the Related Stories block itself is exactly 3 everywhere.

---

## AUDIT 6, Fact Spot Check

All five claims hold against the live source.

### (a) Freddie Mac 30-year fixed, week of September 10, 2026

**HOLDS.** Freddie Mac PMMS release dated Sept. 10, 2026 states the 30-year FRM averaged **6.76%** as of September 10, 2026, up from 6.71% the prior week, against 6.35% a year earlier. The 15-year averaged 6.09%. The package cites 6.76 percent and links the primary Freddie Mac release. Exact match, primary source, correct week.

### (b) Las Vegas REALTORS August 2026 median single-family sale price

**HOLDS.** LVR reported the median price of existing single-family homes sold through its MLS in August 2026 at **$475,000**, down 1.0% from August 2025 and down from the all-time high of $490,000 set in May and June. Condos and townhomes were $299,900, up 0.6%. The package cites $475,000 and down 1.0 percent. Exact match.

Citation advisory carried forward from Audit 1: this is sourced through Nevada Business Magazine and FOX5 rather than the LVR release itself. The number is right; the origin should be named.

### (c) Redfin sellers versus buyers gap

**HOLDS, both figures.** Redfin's August 2026 buyers-vs-sellers report states Las Vegas had **117% more sellers than buyers, up from 102%** the month before, and names Las Vegas among the metros that set record gaps in August. Nationally, **57.9% more sellers than buyers**, up from 52.1% in July, the biggest in records back to 2013. The package's ranking claim also checks out: Nashville 139, Miami 138, Houston 131, Orlando 122, Las Vegas 117, which puts Las Vegas fifth as stated. The claim that only five seller's markets remain is also correct per the source (Nassau County, Newark, Montgomery County PA, Milwaukee, San Francisco).

### (d) Nevada DMV closing dates, Henderson and North Las Vegas

**HOLDS, both dates.** The source states the Commercial Driver License office on **Donovan Way in North Las Vegas closes at end of business Friday, October 9**, and the **Henderson office on American Pacific Drive closes Wednesday, October 14**. Both consolidate into the new Silverado facility. The 350+ parking spaces and six self-service kiosks figures also match.

The package states both dates correctly and consistently across `research.md`, `top-stories.md`, and `blogs/story-10`, including the meta description and the JSON-LD description. No date drift anywhere.

### (e) Vegas Golden Knights goaltender depth chart, Carter Hart starter and Adin Hill backup

**HOLDS as of today's live source.** This was flagged because an earlier weekly run carried a different status for Carter Hart, so the live page was read directly rather than relying on prior context.

The SinBin.vegas article, published September 9, 2026 by Ken Boehlke, states in its live body text that the Golden Knights enter the season with Carter Hart, after starting all 22 playoff games, as the clear starter, with Adin Hill serving as his backup. The same language appears in the page's own meta description. The article further notes that last season Hill was the starter with Schmid behind him, which is likely the different status the earlier run captured. **That has changed. The current source says Hart is the starter.**

Supporting details also check out: Sean Burke as Director of Goaltending since before 2022-23, the roughly 65/35 starter-to-backup split, goalie swaps on every back-to-back, two back-to-backs in the first 20 games (Oct 13 at Nashville, Nov 3 at Pittsburgh) both projected to Hill, and the note that only Hill in 2024-25 and Marc-Andre Fleury in 2018-19 have reached 50 starts in franchise history.

One wording note, not an error. The source says "Season 10." The package says "Season X." X is the Roman numeral for 10 and appears to be a deliberate stylistic choice, used consistently in the story title, the slug, and the blog filename. Flagging only so it is a conscious decision rather than a typo.

---

## Action Items

1. **Create `story-spreadsheet.md` and `weekly-summary.md`.** These are the only two required deliverables missing. Everything else in the package is complete.
2. **Optional, citation hygiene.** Add the Las Vegas REALTORS release itself alongside the Nevada Business Magazine and FOX5 carriers wherever the August median is used, which is stories 2, 6, 13, 14, 15, 30 and bonus 20 and 21. Same pattern for the two Nevada DMV items in stories 10 and 20.
3. **Optional, human eyeball.** The 13 RJ and Sun links are unverifiable by automated fetch. Each is backed by a fetchable second source, so this is low risk, but a quick manual open would close it out. Same for the City of Henderson release, whose body is JavaScript-rendered.
4. **Perishable.** Story 29 rests on the RTC rolling traffic-alerts page, which is overwritten weekly and currently carries some stale July and August entries. Post it early in the week or re-check before posting.

No content rewrites were made. This report is the only file written.
