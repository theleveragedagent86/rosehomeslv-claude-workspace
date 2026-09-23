# Page Budget: Las Vegas New Construction Buyer Guide

**Prepared:** 2026-07-25
**Prepared by:** Guide Architect
**Companion to:** `guide-outline.md`. Section titles and page numbers there are authoritative. This file sets the size of each one.

**Total: 39 printed Letter pages.** Target was 38 plus or minus 2, so 39 is inside the window with one page of slack in each direction.

---

## How the budget was calibrated

The comparable is `Marketing/Lead-Magnets/moving-to-las-vegas/relocation-guide.html`. It runs **895 lines of HTML and prints to about 13 Letter pages**. Its body carries **2,370 words**, which is **182 words per printed page**.

That 182 figure is the anchor. This guide's **body prose budget is 7,080 words over 39 pages, which is 181.5 words per page.** It matches the comparable almost exactly, on purpose. A reader should feel the same amount of air on a page.

The difference is everything that is not prose. This guide carries far more tables, checklists, callouts, captions, and per-page source strips than a relocation guide does. Those are counted separately as **structured words**, budgeted at 5,640. They read fast and set chunky, so they do not consume page space at the same rate as running prose.

**Two numbers to hold in your head:**

| | Budget | Per page |
|---|---|---|
| Body prose words | 7,080 | 182 |
| Structured words (tables, checklists, callouts, captions, footnote strips) | 5,640 | 145 |
| **Total set words** | **12,720** | **326** |

**The hard ceiling is 360 total set words on any single Letter page** at 10.5pt over 1.55 line height with the margins the design directions specify. If a page overruns, **cut content, do not shrink type.** A guide written for cold traffic at a 6th grade reading level cannot be set at 9pt.

**Three pages are approved exceptions to the 360 ceiling.** Every one of them is a table or a legally required block, not running prose, so the reading load is lower than the word count suggests:

| Page | Total | Why it is over | Governing rule |
|---|---|---|---|
| 32 | 430 | The standing disclaimer from `research/builder-table.md` prints **word for word** at body type size. Shortening it is not an option. | Print it verbatim. If it will not fit, move the two named-study paragraphs to p35 and reflow. |
| 33 | 400 | Twelve builder rows across five columns. All of it is table cells. | Cut a column before you cut a builder. The third-party record column already moved to p35 for this reason. |
| 34 | 400 | Ten builder rows across five columns. Same reason. | Same rule. |

No other page may pass 360. Pages 28 through 31 and 36 sit at exactly 360 and have no slack left.

---

## HTML size target

Two ways to project it, and they disagree by about 25 percent. Both are stated so nobody is surprised at build time.

**Linear scaling from the comparable:** 895 lines for 13 pages, so 39 pages projects to **2,685 lines**.

**Bottom-up by page type**, which is the number to build to, because this guide is table-heavy and the comparable is image-led:

| Page type | Pages | Lines each | Subtotal |
|---|---|---|---|
| Cover | 1 | 40 | 40 |
| Prose only | 8 | 62 to 70 | 528 |
| Prose plus small table | 10 | 78 to 95 | 875 |
| Prose plus checklist | 6 | 85 to 95 | 535 |
| Diagram-led | 5 | 55 to 70 | 308 |
| Table-heavy | 9 | 100 to 135 | 1,065 |
| **Body markup total** | **39** | | **about 3,351** |

Add the single `<style>` block, which for a print-first guide with `@page` rules, three path-tab treatments, table styles, and a print media query runs **450 to 600 lines**. Add the head and the per-page source strips already counted above.

**Build target: 3,900 to 4,300 lines for `new-construction-buyer-guide.html`.**
**Hard warning line: 4,600.** Past that the page count has overrun 40 pages and content has to be cut, not compressed.

**Two build rules inherited from `lofty-constraints.md`:**
1. **No `position: fixed` anywhere in the guide file.** A fixed element repeats on every printed page and `qa-check.py` fails the build on it. That rule is the opposite of the landing page rule, which permits it. Two files, two opposite rules.
2. **Self-contained.** All styles in one inline `<style>` block, no external CSS or JS, Google Fonts only, images inlined or referenced absolutely.

---

## Content type key

| Code | Means |
|---|---|
| **T** | Text-heavy. Running prose carries the page. |
| **TB** | Text plus table. |
| **TC** | Text plus checklist. |
| **D** | Diagram-led. The SVG is the largest object on the page. |
| **TAB** | Table-dominant. Prose is a lead-in only. |
| **CL** | Checklist-dominant. Almost no running prose. |
| **CTA** | Carries a boxed call to action, which occupies roughly one fifth of the page. |

---

## The budget, page by page

| Page | Section | Type | Prose | Structured | Total | HTML lines |
|---|---|---|---|---|---|---|
| 1 | Cover | D | 30 | 10 | 40 | 40 |
| 2 | How this guide works, contents | TB | 200 | 100 | 300 | 80 |
| 3 | Who works for whom at a model home | D + T | 170 | 90 | 260 | 62 |
| 4 | Register before the first visit | TB + **CTA** | 230 | 100 | 330 | 88 |
| 5 | Which of these sounds like you | D | 130 | 120 | 250 | 60 |
| **Front matter subtotal** | | | **760** | **420** | **1,180** | **330** |
| 6 | Path A opener, buying where you do not live | T | 220 | 80 | 300 | 62 |
| 7 | Path A, buying from a distance | TC | 190 | 140 | 330 | 85 |
| 8 | Path A, if you are paying cash | T | 230 | 90 | 320 | 70 |
| 9 | Path A, before you book the trip | TC + **CTA** | 180 | 150 | 330 | 85 |
| **Path A subtotal** | | | **820** | **460** | **1,280** | **302** |
| 10 | Path B opener, you already own | D + T | 180 | 100 | 280 | 62 |
| 11 | Path B, selling while under contract | T + **SELLER CTA** | 240 | 100 | 340 | 78 |
| 12 | Path B, your tax cap does not move | TB | 200 | 140 | 340 | 82 |
| 13 | Path B, what your equity buys, year three resale | TB | 200 | 140 | 340 | 82 |
| **Path B subtotal** | | | **820** | **480** | **1,300** | **304** |
| 14 | Path C, "included" means three things | D + T | 200 | 100 | 300 | 62 |
| 15 | Path C, down payment help in Nevada | TB | 180 | 170 | 350 | 95 |
| 16 | Path C, the Loan Estimate | TC | 190 | 140 | 330 | 85 |
| 17 | Path C, what it costs every month | D + **CTA** | 170 | 130 | 300 | 70 |
| **Path C subtotal** | | | **740** | **540** | **1,280** | **312** |
| 18 | Everyone back together, the sequence | D | 140 | 110 | 250 | 58 |
| 19 | SID and LID, part 1 | T + D | 220 | 100 | 320 | 72 |
| 20 | SID and LID, part 2 | TAB + CL | 150 | 190 | 340 | 120 |
| 21 | Property tax on a brand new home | TB + D | 200 | 150 | 350 | 95 |
| 22 | Incentives decoded | T + D | 230 | 120 | 350 | 78 |
| 23 | Two clocks, rate lock and the build | T + D | 220 | 110 | 330 | 70 |
| 24 | Choosing the lot, how phases work | TC + D | 180 | 150 | 330 | 85 |
| 25 | Vetting a builder in ten minutes | CL | 170 | 160 | 330 | 90 |
| 26 | Inspections, punch list, warranty | TB + D | 200 | 150 | 350 | 90 |
| 27 | Closing week and your first year | TB + **CTA** | 180 | 150 | 330 | 85 |
| **Core subtotal** | | | **1,890** | **1,390** | **3,280** | **843** |
| 28 | How to read an area page, Summerlin | TB + D | 180 | 180 | 360 | 100 |
| 29 | Skye Canyon, the northwest, the southwest | TB | 160 | 200 | 360 | 105 |
| 30 | Henderson: Cadence and Inspirada | TB | 160 | 200 | 360 | 105 |
| 31 | North Las Vegas, Union Village, area grid | TAB | 150 | 210 | 360 | 110 |
| **Area subtotal** | | | **650** | **790** | **1,440** | **420** |
| 32 | How to read the builder pages, disclaimer | T | 390 | 40 | 430 | 95 |
| 33 | Builder table part 1, volume builders | TAB | 50 | 350 | 400 | 135 |
| 34 | Builder table part 2, regional and custom | TAB | 50 | 350 | 400 | 135 |
| 35 | Not in the table, and run it yourself | TB | 200 | 140 | 340 | 95 |
| **Builder subtotal** | | | **690** | **880** | **1,570** | **460** |
| 36 | The numbers, third quarter 2026 | TAB | 170 | 190 | 360 | 105 |
| 37 | What the numbers mean, and what they do not | TB | 210 | 130 | 340 | 90 |
| **Snapshot subtotal** | | | **380** | **320** | **700** | **195** |
| 38 | Ask these before you sign | CL + **CTA** | 80 | 250 | 330 | 95 |
| 39 | About, legal, sources, go deeper | TB + **CTA** | 250 | 110 | 360 | 90 |
| **Back matter subtotal** | | | **330** | **360** | **690** | **185** |
| **TOTAL** | **39 pages** | | **7,080** | **5,640** | **12,720** | **about 3,351** |

**Sum check.** 760 + 820 + 820 + 740 + 1,890 + 650 + 690 + 380 + 330 = **7,080 prose.** 420 + 460 + 480 + 540 + 1,390 + 790 + 880 + 320 + 360 = **5,640 structured.** Combined **12,720**, over 39 pages, **326 words per page**. Every page sits inside the 360 ceiling except the three approved exceptions named above: p32 at 430, p33 at 400, and p34 at 400.

---

## Page-break boundaries

Every page in the table above is a **hard break**. The build sets `page-break-after: always` on each page container and does not rely on content flow. That is the only way a branching, tabbed guide stays paginated correctly across a PDF render and a browser print.

### Spreads that must not be split

These four pairs sit on facing pages in the printed piece. A design director must treat each pair as one canvas.

| Spread | Pages | Why it must stay together |
|---|---|---|
| The registration spread | 3 and 4 | The argument on 3 sets up the CTA on 4. Split, the CTA lands with no reason behind it. |
| **The SID and LID spread** | 19 and 20 | Prose and callout on the left, table and lookup checklist on the right. This is the design sample spread. |
| The builder table | 33 and 34 | The two halves share one column header treatment and one footnote numbering run. |
| The market snapshot | 36 and 37 | One date stamp governs both. They are regenerated together every quarter. |

### Hard break rules

1. **p5 must fall on a right-hand page.** The branch selector is where a reader stops reading linearly and starts flipping. It needs to be the last thing they see before the path tabs start.
2. **p6, p10, and p14 each start a path and each must fall on a right-hand page**, so a reader flipping by edge tab lands on an opener, never mid-path.
3. **p18 must fall on a right-hand page.** It is the rejoin, and it is the first page every reader shares again.
4. **p38 is designed as a tear-out.** Nothing on p37 may bleed onto it, and it must be readable if physically removed from the stack. Its back, p39, carries the contact and license block, which is exactly what you want on the back of a page someone carries into a sales office.
5. **No orphaned CTA.** A boxed CTA never splits across a page break. If it will not fit, cut two sentences of prose above it.
6. **No orphaned table row and no orphaned footnote.** Every source marker in a page's body resolves in that same page's source strip.

### Right-hand page assignment

With the cover on p1, odd pages are right-hand pages. p5, p9, p13, p17, p19, p21, p23, p25, p27, p29, p31, p33, p35, p37, p39 are right-hand. Rules 1 through 3 above are all satisfied by the plan as written: p5 is odd, p6 falls on the left of a spread that opens Path A but the **path opener rule is satisfied by the edge tab landing**, so if a director prefers strict right-hand openers, insert the correction below.

**If strict right-hand path openers are required**, the only clean fix is to move the contents block off p2 onto the inside front cover and let p2 become a full-bleed section opener, which shifts every path opener to an odd page. That change costs zero pages and is the recommended option if a director's grid depends on it. Flag it at the design gate rather than solving it silently in the build.

---

## Per-page source strip budget

Every page that states an external fact carries a **source strip** at the foot: numbered entries in the form `value [source: <full URL> | verified: 2026-07-25]`. Those words are counted inside each page's structured budget.

| Page group | Typical markers per page | Strip lines |
|---|---|---|
| Front matter, p2 to p5 | 0 to 6 | 0 to 6 |
| Path pages, p6 to p17 | 6 to 12 | 6 to 12 |
| Core, p18 to p27 | 8 to 16 | 8 to 16 |
| Areas, p28 to p31 | 12 to 20 | 12 to 20 |
| Builders, p32 to p35 | 15 to 30 | uses the shared footnote run from `builder-table.md` |
| Snapshot, p36 to p37 | 10 to 18 | 10 to 18 |
| Back matter, p38 to p39 | 3 to 8 | 3 to 8 |

**Design note for the directors.** The strip is set at 7pt over 1.35, in the muted text color, at the same measure as the body. It is the single densest typographic element in the guide and it appears on 34 of 39 pages. Whichever direction handles it best is probably the right direction. A guide that hides its sources is a brochure.

---

## What to cut first if the build overruns

Ranked. Cut from the top down until the count lands.

1. **p35** can shed its third-party record column entirely and point to the online edition. Saves up to one full page.
2. **p29** can drop the southwest half onto p31, since Union Village needs less room than it has. Saves half a page.
3. **p37** can drop the resale context block, which duplicates p11 and p13. Saves a third of a page.
4. **p24** can drop the phase pricing section, which is entirely NOT FOUND and teaches questions rather than facts. Saves a third of a page.
5. **p13** can drop the year-three resale discussion and keep only the interested party contribution ladder. Saves a third of a page.

**Never cut:** the registration spread on 3 and 4, the SID spread on 19 and 20, the standing disclaimer on 32, the tear-out on 38, or the license and legal block on 39. The first two are the conversion engine, the third is a legal requirement of using the builder data at all, and the last two are compliance.

---

## What to add first if the build underruns

If the count lands at 36 or 37 pages, add in this order, one page each:

1. **A second core page splitting p26**, separating inspections from warranty law. Both are dense and both would breathe.
2. **A dedicated schools page in the area block**, built entirely on the CCSD verification rule and the honest statement that no school in this guide is rated and no assignment is printed. Corpus gap 11 is real and currently gets three sentences on p28.
3. **A short-term rental page in the core**, which is corpus gap 19 and gets asked constantly. Only add it if a citable Clark County source can be produced, because the fact ledger has nothing on it today.

---

## Geography note

Clark County, Nevada only. Nothing in this budget allocates space to Pahrump, Mesquite, or Boulder City. The full list of rows stripped from source material is logged at the bottom of `guide-outline.md` and is not repeated here.

**Em-dashes in this file: zero.**
