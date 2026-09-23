# Handback: areas, builders, snapshot, back matter (p28 to p39)

**Writer:** Chapter Writer 3
**Files delivered:** `p28.html` through `p39.html`, twelve files, one per printed page.
**Em-dashes:** zero. Checked in prose, comments, attributes, and every string carried across from
builder-sourced text.
**Entities used:** `&nbsp;` and `&middot;` only. No other entity appears.
**Hex codes:** none. Only inline `style` is `padding-top:16pt` on `.pad`, which is the pattern the
fragment contract's own skeleton B uses.

---

## 1. Word count against budget

Counted on rendered text only: alt text, `href` values, `data-claim` values and the generated `*`
marker are excluded, because none of them set type on the page. A `tok-nf` token counts as two words
("Not found", which the class uppercases to NOT FOUND). Bracketed builder footnote numbers count as
one word each.

| Page | Actual | Budget | Result |
|---|---|---|---|
| 28 | 309 | 360 | ok, 51 under |
| 29 | 340 | 360 | ok, 20 under |
| 30 | 356 | 360 | ok |
| 31 | 359 | 360 | ok |
| 32 | 429 | 430 | ok, approved exception |
| 33 | 400 | 400 | ok, at ceiling, approved exception |
| 34 | 400 | 400 | ok, at ceiling, approved exception |
| 35 | 340 | 340 | ok, at ceiling |
| 36 | 331 | 360 | ok |
| 37 | 340 | 340 | ok, at ceiling |
| 38 | 328 | 330 | ok |
| 39 | 360 | 360 | ok, at ceiling |
| **Total** | **4,292** | **4,400** | 108 under |

### Page fit, measured rather than assumed

`.page` is a fixed box with `overflow:hidden`, so overset text disappears silently. Every page was
spliced into `build/shell.html` (with `svg-10.svg` inlined) and measured in a browser after
`document.fonts.ready`. Bottom of the last content child, against the 1008px limit above the 48px
foot:

| Page | Content bottom | Slack |
|---|---|---|
| 28 | 974 | 34 |
| 29 | 700 | 308 |
| 30 | 665 | 343 |
| 31 | 646 | 362 |
| 32 | 975 | 33 |
| 33 | 591 | 417 |
| 34 | 632 | 376 |
| 35 | 566 | 442 |
| 36 | 804 | 204 |
| 37 | 604 | 404 |
| 38 | 877 | 131 |
| 39 | 600 | 408 |

Nothing overflows. Horizontal overflow past the page right edge measured 0px on all twelve, and
`scrollWidth == clientWidth` on all five `table.sid` elements, so no table and no long URL is
clipped. **p28 and p32 are the two tight pages, at 34 and 33px of slack.** Adding a sentence to
either one needs a re-measure, not an estimate.

---

## 2. Claim-ids used

166 unique, every one verified present in the data tables of `research/fact-ledger.md` (the check
excluded the conflicts table, so a conflict-id cannot sneak in as a `data-claim`).

**p28:** `sid-lookup-steps`, `area-hoa-resale-package-rights`, `area-ccsd-verify-by-address`,
`area-ccsd-phone`, `area-ccsd-search-tips`, `mkt-resale-median-june-2026`, `mkt-mls-caveat`,
`area-summerlin-acres`, `area-summerlin-inception`, `area-summerlin-population`,
`area-summerlin-future-land`, `area-summerlin-parks-trails`, `area-summerlin-downtown`,
`area-summerlin-active-villages`, `area-summerlin-roundup-date`, `area-summerlin-price-band`,
`area-summerlin-no-sub-500k`, `area-summerlin-hoa-structure`, `sid-summerlin-819`,
`sid-summerlin-mesa-retired`

**p29:** `area-skyecanyon-location`, `area-skyecanyon-builders`, `bld-century-skyeview`,
`area-skyecanyon-toll-price`, `area-skyecanyon-price-from`, `area-skyecanyon-amenities-open`,
`area-skyecanyon-no-lots`, `sid-skye-canyon-609`, `sid-skye-canyon-610`, `sid-skye-hills-612`,
`area-centennial-hills-is-district`, `area-providence-built-out`, `sid-providence-607-matured`,
`area-enterprise-size`, `area-enterprise-boundaries`, `area-enterprise-growth`,
`area-enterprise-population`, `tax-rate-enterprise-630`, `tax-rate-enterprise-635`,
`area-mountainsedge-start`, `area-mountainsedge-parks`, `area-mountainsedge-regional-park`,
`area-mountainsedge-hoa-phone`

**p30:** `area-cadence-location`, `area-cadence-acres`, `area-cadence-units`,
`area-cadence-commercial`, `area-cadence-timeline`, `area-cadence-builders`,
`area-cadence-price-band`, `area-cadence-central-park`, `area-cadence-fire-station`,
`sid-cadence-none`, `area-cadence-hoa-amount`, `area-cadence-hoa-structure`,
`sid-absence-not-proof`, `area-inspirada-location`, `area-inspirada-developer`,
`area-inspirada-buildout-homes`, `area-inspirada-seven-parks`, `area-inspirada-has-lid`,
`sid-henderson-inspirada-t18`, `tax-rate-henderson-505`

**p31:** `area-nlv-is-own-city`, `tax-rate-northlasvegas-250`, `area-nlv-valleyvista-start`,
`area-nlv-valleyvista-completion`, `area-nlv-valleyvista-homes`, `area-nlv-valleyvista-built`,
`area-nlv-valleyvista-still-planned`, `bld-drhorton-concentration`,
`area-nlv-tulesprings-village2`, `area-nlv-kb-approval`, `sid-nlv-valley-vista-64`,
`sid-nlv-tule-springs-66`, `sid-nlv-aliante-60-matured`, `area-unionvillage-hospital`,
`area-unionvillage-built`, `area-unionvillage-planned`, `area-unionvillage-park-dispute`,
`area-unionvillage-no-active-builder`

**p32:** `rep-bbb-not-government`, `rep-entity-name-warning`, `rep-jdpower-discontinued`,
`law-nrs645-advertising`

**p33:** `bld-kb-homesite-premium` (the table body uses the builder footnote run, not `data-claim`;
see section 5)

**p34:** `war-regional-builders-blank`, `bld-storybook-is-toll`, `war-storybook-routes-to-toll`,
`bld-trust-entity`, `bld-signature-entity`, `bld-touchstone-price-band`,
`bld-touchstone-second-loan`, `bld-blueheron-model`, `bld-blueheron-no-lender`, `bld-edward-scale`,
`bld-trust-serene-no-hoa`, `bld-harmony-office-closed`, `rep-harmony-license-expiring`,
`rep-landonmiller-license`

**p35:** `rep-lifestory-method`, `rep-zonda-method`, `rep-avidcx-method`, `bld-meritage-not-nevada`,
`bld-meritage-10k-states`, `rep-meritage-license-cancelled`, `bld-brooks-unverifiable`,
`rep-brooks-no-record`, `rep-lgi-no-lv-bbb`, `rep-lgi-bbb-texas`, `rep-lgi-bbb-reasons`,
`rep-lgi-lifestory`, `rep-touchstone-bbb`, `rep-touchstone-bbb-reasons`, `rep-touchstone-license`,
`rep-toll-citation`, `rep-trust-citation`, `rep-trust-license`, `rep-nscb-search-link`,
`rep-nscb-discipline-link`, `rep-entity-name-warning`

**p36:** `mkt-new-median-february-2026`, `mkt-new-median-march-2026`, `mkt-new-median-april-2026`,
`mkt-new-median-june-2026`, `mkt-median-source`, `mkt-median-caution`, `mkt-smaller-homes`,
`mkt-net-sales-h1-2026`, `mkt-closings-h1-2026`, `mkt-permits-h1-2026`, `mkt-june-2026-detail`,
`mkt-2025-full-year`, `mkt-census-permits-h1-2026`, `mkt-census-series`, `mkt-months-supply-resale`,
`mkt-standing-inventory-question`, `mkt-rate-july-2-2026`, `mkt-rate-july-9-2026`,
`mkt-rate-july-16-2026`, `mkt-rate-july-23-2026`, `mkt-rate-15yr`, `mkt-rate-year-ago`,
`mkt-rate-is-national-average`

**p37:** `mkt-gap-same-month`, `mkt-gap-clever-study`, `mkt-gap-clever-rank`,
`mkt-new-share-of-market`, `mkt-condo-median-june-2026`, `mkt-existing-sales-june-2026`,
`mkt-sf-inventory-june-2026`, `mkt-condo-inventory-june-2026`, `mkt-60-day-share`,
`mkt-cash-share`, `mkt-mls-caveat`, `mkt-incentive-climate`, `mkt-nahb-national-context`,
`mkt-design-center-markup`, `mkt-builder-lender-rate-caution`

**p38:** `sid-lookup-steps`, `fin-loan-estimate-page3`, `fin-ipc-cap-over-90-ltv`,
`proc-escrow-on-full-tax`, `bld-no-design-credit-published`, `bld-no-upgrade-financing-published`,
`law-nrs624602-rights-sheet`, `area-hoa-resale-package-rights`

**p39:** `law-arbitration-nrs597995`, `law-arbitration-preempted`, `law-nrs645-advertising`,
`law-chapter40-prevails`

---

## 3. Blog slugs linked, all on p39, all `/blog/` singular

Build-blocking gate input. `blog-corpus-map.md` records all 110 as NOT FOUND for publish status, so
every one of these ten has to be loaded live and confirmed before the guide ships.

1. `summerlin-new-construction-2026-guide`
2. `every-builder-summerlin-2026`
3. `skye-canyon-vs-summerlin-northwest-las-vegas`
4. `mountains-edge-new-construction-family-friendly`
5. `southern-highlands-new-construction-luxury`
6. `cadence-henderson-master-planned-community`
7. `inspirada-henderson-last-chance-buildout`
8. `henderson-new-construction-2026-guide`
9. `north-las-vegas-new-construction-value`
10. `henderson-vs-las-vegas-vs-north-las-vegas`

**Two slugs carry words the guide bans, and they are in the URL only.** Slug 4 contains
"family-friendly", which the fair housing gate forbids, and slug 5 contains "luxury", which the
banned-words table forbids. **Neither string appears in visible link text or anywhere else in my
twelve pages**; the anchors read "Mountain's Edge" and "Southern Highlands". Flagging it because a
naive grep of the assembled HTML will hit both, and because if either post is ever renamed on the
site this is the moment to do it.

**Also linked, not a blog slug:** `rosehomeslv.com/moving-to-las-vegas`, once on p39, as the
relocation-guide cross-link for readers who skipped Path A.

---

## 4. The p32 disclaimer: it fit, and it forced the p35 reflow

**The standing disclaimer prints word for word.** All 365 words of it, in order, from paragraph one
("About the information in this table") through the contact line, including the three lookup URLs.
Nothing was shortened, merged, or moved to a footnote. Verified against `disclaimer` in
`build/data/builder-table.json`, which is byte-identical to lines 32 to 50 of
`research/builder-table.md`. That source text contains zero em-dashes, so nothing needed sanitizing.

**The escape hatch in `page-budget.md` was used.** 365 disclaimer words against a 430 word ceiling
leaves 65 for the opener and the five other points the outline puts on p32. That is not enough, so
**the two named-study paragraphs moved to p35 and p35 reflowed**, exactly as the budget authorizes.
What p32 now carries: opener eyebrow, headline, deck, the verbatim disclaimer, and one `.attr` line
holding the NOT FOUND instruction, the J.D. Power point, and the NRS 645 brokerage and license
block. p32 lands at 429 of 430.

**What p32 gave up to make room.** The `.op-line` element. Skeleton A allows it and every other
opener in my block uses it; on p32 the 19pt line cost 44px on a page with 33px of slack. Its content
("NOT FOUND is your cue to ask, in writing") survives in the `.attr` line.

**p35 reflowed by shedding the third-party record column**, which is cut number 1 on the
`page-budget.md` cut list and is the only way both the studies and the must-print-in-full entries fit
in 340 words. p35 now says the full column lives in the online edition, and prints in full the four
things that are print-in-full-or-not-at-all: the LGI Homes pair, the Touchstone Living pair, and both
board citations verbatim.

### Two deviations inside the disclaimer block, both deliberate

1. **Type size.** `research/builder-table.md` says print the disclaimer "at the same type size as the
   table body", which is 8pt (`table.sid td`). `design-system.md` says never set body copy below
   9.5pt to solve a fit problem, and forbids inventing a type size. I put the disclaimer in
   `.card card-agave`, whose `.card p` is **9.4pt over 1.44**. Larger than the instruction, inside
   the frozen system, and it fits with 33px to spare. **If a design director wants the literal 8pt,
   that is a change to `design-system.md`, not something a fragment should improvise.**
2. **The three-link bullet list rendered as three paragraphs.** The disclaimer's markdown has a
   bullet list. The class inventory's only list components are `.nlist` (numbered circles) and
   `.chk` (checkboxes), and neither is right for three URLs. Each link is its own `<p>` inside the
   card, so word order and wording are untouched. The longest URL is 107 characters; at the full
   7.4in measure it sets on one line and measured 0px of horizontal overflow. **This is why the
   disclaimer is one full-width card and not split across `.cols`.** In a 3.6in column that URL has
   no break opportunity and would have been clipped by `overflow:hidden` with no error anywhere.

---

## 5. The builder table footnote run: what I did, and the one thing I could not do

**The cells use the `builder-table.md` numbering, not the `data-claim` scheme**, as instructed. Every
data cell on p33 and p34 resolves to either a bracketed footnote number from that run or the literal
`NOT FOUND` token. No cell is bare.

**What I could not do: typeset the footnote URLs on the page.** The verification gate asks for a URL
and a verified date per footnote. p33 and p34 cite roughly 45 unique footnotes between them. At 7pt,
45 URLs is about 1.4 Letter pages of type, on two pages already at their 400 word ceiling. That is
the same arithmetic that produced the companion source list for the other 254 URLs in
`design-system.md`. So:

- **The date half is printed on the page.** Each table `<caption>` states the footnote numbers were
  read on July 25, 2026, and the disclaimer on p32 states the same date twice.
- **The URL half routes to the companion source list**, keyed by builder-table footnote number.
- **`assemble.py` needs a small addition:** emit the `builder-table.md` footnote list (its own
  numbering, 1 to 150, or at minimum the subset cited on p33 and p34) into the companion source list
  as a separate numbered block, so a bracketed `[101]` on p33 resolves. It is a straight copy from
  `build/data/builder-table.json` `footnotes[]`, which already carries `n`, `url` and `verified`.
  **Until that block exists, the bracketed numbers on p33 and p34 resolve to nothing.** This is the
  single most important open item in my block.

**Nothing else about the table drifted from source.** Every cell was compressed from
`build/data/builder-table.json` rather than retyped from the prose file, so no figure could drift.
The compression is severe: 48 data cells on p33 inside a 400 word ceiling is about 6 words a cell.
No aggregate score, no ranking, no rank order other than A to Z, and no adjective authored by Ryan
appears in any cell. No advertised builder rate or promotion is printed as current; where an offer
conditioned an incentive, the cell says "Offer conditioned, July 2026" and prints no rate.

### The spread mechanics

Both halves carry a full `<thead>` with `<th scope="col">` on all five headers, a `<caption>`, and
`<th scope="row">` on every builder name. `thead { display: table-header-group }` is already in the
stylesheet, so the header repeats across the break. Column set is identical on both pages: Builder /
Warranty as published / Lender tie / Upgrades / Price band and count. **No column was cut and no
builder was dropped.**

---

## 6. p36 and p37, severable and dated

One date stamp governs both and it is printed on the page: p36's eyebrow reads "Data current as of
July 25, 2026" and its deck says pages 36 and 37 share it and get rebuilt every quarter. p37 repeats
that it is rebuilt each quarter. Nothing anywhere else in my block depends on a number that lives
only on these two pages: p28's valleywide `$490,000` and p31's tax rate both carry their own ledger
claim-ids and their own dates in the sentence.

`refresh` mode regenerates p33, p34, p36 and p37. p36 and p37 are self-contained. **p33 and p34 are
not fully self-contained for a refresh**: their footnote numbering comes from `builder-table.md`, so
a quarterly refresh that re-pulls builder pages must renumber that run and the companion source
block together, or the brackets go stale silently.

---

## 7. p38 as a physical tear-out

- Carries the `.tearout` element with its cut line and label, placed as a direct child of `.page`
  after `.body` so it paints above the opener photograph.
- **No back-reference anywhere.** Nothing says "as we saw on page 22". The page-number tags after
  each question, `(p4)`, `(p19)` and so on, are forward pointers for a reader who still has the
  guide, and every question reads correctly with the tag ignored.
- 22 questions in five groups matching p18's five stages. Three are prefixed `Lender:` because they
  go to the lender, not the sales office.
- The four questions off the NOT FOUND register are all present: the per-lot assessment with balance,
  payoff year and prepayment penalty; the design center spend requirement and credit; whether
  upgrades can be financed; and the warranty document with its term lengths.
- Primary CTA #5 of 5 sits in a `.close` at the foot with the phone number. p39 carries the final
  soft close, also in a `.close`, plus the full contact and license block, which is what you want on
  the back of a page somebody is holding in a sales office.
- 328 of 330 words and 131px of vertical slack. **Adding a question needs a re-measure.**

**Compliance on p39:** `Real Broker, LLC`, Nevada license `S.0185572`, Ryan Rose, 702-747-5921,
ryan@rosehomeslv.com, rosehomeslv.com, in a `.phone-row`. Plus the third-party-findings disclaimer,
the verify-before-relying disclaimer, and the pointer to the companion source list. Same brokerage
and license strings also appear on p32.

**Compensation caveat honored.** Nothing in my twelve pages says representation is free, costs the
buyer nothing, or is builder-paid. The word "compensation" does not appear. p38 asks how registration
works and how long it lasts; it never asserts who pays.

---

## 8. Geography

**Nothing surviving had to be stripped.** Every excluded row in the `guide-outline.md` geography log
and the `builder-table.md` geography log was already absent from the material I drew on:
`build/data/builder-table.json` is post-strip, and `snapshot/market-snapshot-2026-Q3.md` records
"Rows actually stripped: none" because no source produced a city-level table.

Three deliberate mentions of the excluded cities remain, all of them required disclosures, not
content:

1. **p28 figure caption:** "Pahrump, Mesquite and Boulder City sit outside this guide and are not
   drawn." Required by SVG-10's own description in `build/svg/index.md`.
2. **p37:** the disclosed limitation that Mesquite and Boulder City sit inside the valleywide medians
   and cannot be separated out. Required by outline p37 point 6.
3. Nothing else. No community, price, builder row, district or amenity from any of the three cities
   appears.

A keyword sweep will flag those two. They are the guide keeping its promise, not breaking it.

**Signature Homes' "Mesquite" floor plan** is not named anywhere in my pages, so the known false
positive from the ledger's judgment call 3 does not arise here.

---

## 9. Conflicts honored

| Conflict | How |
|---|---|
| `cft-summerlin-buildout-percent` | p28 prints "Percent built out: NOT FOUND" and uses the 5,000 acre reserve figure instead |
| `cft-sid-159-final-date` | district 159 is not printed at all, so the disputed date never appears |
| `cft-pulte-lennar-skye-canyon` | p29 names only Century Communities, Toll Brothers and LGI Homes at Skye Canyon |
| `cft-skye-canyon-sid-number` | p29's table prints district numbers and dates only. It never says what 609 or 610 covers |
| `cft-providence-scale`, `cft-mountains-edge-scale` | acreage and home counts printed as NOT FOUND. No magnet high school claim |
| `cft-toll-beazer-at-cadence` | p30's Cadence builder list is the developer's seven. Toll Brothers is not among them |
| `cft-cadence-richmond-prices` | the three Richmond American Cadence prices are not printed |
| `cft-cadence-sid` | the developer's own no-SID statement is used, immediately followed by `sid-absence-not-proof` and the parcel lookup |
| `cft-inspirada-buildout` | 7,500 homes and 18,000 residents, dated "a September 2024 report" in the sentence |
| `cft-name-collision-verona` | p30 names Beazer's Henderson Verona and Taylor Morrison's Verona at Lake Las Vegas side by side |
| `cft-union-village-townes` | Union Village gets no price and no named community. Active for-sale communities: zero |
| `cft-lennar-community-count` | p33 prints "34 stated, 26 rendered". Century 13 of 14, Pulte 18 of 19, Tri Pointe 6 of 15, Beazer "10 shown" |
| `cft-meritage-nevada` | p35 states Meritage does not build in Nevada, on its own site, its annual report, and a cancelled license |
| `cft-lgi-reputation` | p35 prints the no-Las-Vegas-profile fact, the Texas F with its stated reasons, and the 114.0 score, in one breath |
| `cft-toll-license-status` | the Active licenses are the operative record. The suspended older licenses are **not printed** (see gap 4) |
| `cft-touchstone-similar-name` | the revoked Touchstone Development Corp record appears nowhere near Touchstone Living |
| `cft-storybook-license-link` | no StoryBook license number is printed, and nothing implies StoryBook is unlicensed |
| `cft-trust-calico-sqft` | neither square footage is printed |
| `cft-pinnacle-sales-center-zip` | no Pinnacle address and no ZIP is printed |
| `cft-months-supply` | 3.5 months, the association's own release figure |
| `cft-new-vs-resale-gap` | p37 prints both measurements, says the subtraction is mine, and says why they differ |
| `cft-arbitration-statute` | p39 says assume an arbitration clause is enforceable because federal law preempts NRS 597.995 |
| `cft-la-vegas-realtors-domain` | p37 prints the domain problem in prose (see gap 3) |

**Low-confidence claims hedged, not dropped:** `area-centennial-hills-is-district` and
`area-providence-built-out` are used for the structural point only, with no numbers attached.
`mkt-design-center-markup` and `mkt-builder-lender-rate-caution` are attributed in the sentence as
"a competing brokerage's own survey, not a neutral source". `area-cadence-schools-planned` was
**omitted**, which the outline authorizes, so the guide prints nothing sourced to a paid advertising
feature.

**Schools:** no rating and no assignment anywhere in twelve pages. p28 states out loud that the guide
rates no school and prints no assignment, and hands over the district's own tool plus 702-799-7678
and the district's search tips. Corpus gap 11 stays visible.

**Fair housing:** areas are described by acreage, dates, what is physically built, what is documented
and what is not. No demographic characterization, no "family friendly", no "good area", no coded
language. Banned-words sweep is clean across all twelve pages.

---

## 10. Gaps, and things I could not write

### 1. `assets/image-manifest.md` has no alt text column. I wrote the alt text.

The fragment contract says alt text comes from the manifest "verbatim" and that it was
"human-reviewed against the fair housing gate". **The manifest has no alt text.** It has an ID table,
a job ID table, and a prompt list. Grepping `alt` across `assets/` returns nothing.

So each `<img>` alt is the manifest's **own prompt description for that image, condensed to the
sentence that describes what is in the frame**, because that text is the closest thing in the repo to
a reviewed description and it was written under the no-people, no-signage, no-identifiable-community
rules. Example, `open-areas.jpg`: "Wide documentary photograph of the Las Vegas valley at midday from
the west, red rock formations in the foreground, the basin and its far mountain wall under a bright
dry sky."

**This is authored alt text, not reviewed alt text.** It needs the same human pass the manifest
claims to have had, and the manifest needs a real alt column added. Six images are involved:
`open-areas.jpg`, `open-builders.jpg`, `open-snapshot.jpg`, `open-back.jpg`, `area-northwest.jpg`,
`area-henderson.jpg`, `area-north-lv.jpg`.

### 2. `area-summerlin.jpg` is not placed. p28 had no room for it.

The manifest assigns IMG-11 to p28. p28 is a section opener: the photograph and dissolve take the top
320px, `.op-body` starts at 272px, and SVG-10 is also assigned to p28. In a 3.6in grid column a 4:3
inset renders 2.7in tall, and there is no way to constrain it without an inline `style` on an `img`,
which the rules do not allow. The page already lands at 974 of 1008px carrying SVG-10, the three
shared rules, the valleywide figure and the Summerlin card.

I chose the diagram over the photograph, because SVG-10 is the only diagram in my block and it is the
orientation device the whole area section depends on. **`area-summerlin.jpg` therefore ships
uninstalled.** Three ways to fix it, all above a fragment writer's pay grade: give p28 a second page,
add a constrained image class to `design-system.md`, or accept the loss and note it in the manifest.
p29, p30 and p31 all carry their assigned insets.

### 3. `cft-la-vegas-realtors-domain` cannot be a `data-claim`.

Outline p37 point 7 asks for the association-domain note and names that id. It is a **conflict-id**,
not a row in a ledger data table, so `assemble.py` would fail the build on it. **The fact is printed
in prose on p37 with no marker.** If the fact auditor wants it cited, the conflict needs promoting to
a ledger row.

### 4. Toll Brothers' suspended older licenses are not printed.

Outline p35 point 5 says they print "only with the verbatim reason and the fact that Active licenses
exist alongside them". Both conditions plus the two verbatim citations plus the studies plus the name
collisions do not fit in 340 words. Since the outline makes printing conditional rather than
mandatory, **I omitted the suspended-license sentence** and printed the 08/06/2024 citation in full
instead. `rep-toll-suspended-licenses` and `rep-toll-active-licenses` are consequently unused in my
block. If the online edition carries the full third-party column, that is where they belong.

### 5. Two places the outline and the data disagree, resolved toward the data.

- **p34 point 1 lists ten builders for an "eight rows" table.** Harmony Homes and Landon Miller Homes
  are in `builder-table.md`'s "checked but not shown" section, explicitly because "the columns in the
  table above cannot be filled" for them, and neither is in the 20 builder JSON. **The p34 table has
  the eight real rows; Harmony and Landon Miller are named in p34 prose with the reason they have no
  row.** No builder was cut to make room.
- **`builder-table.md` header says 114 NOT FOUND cells; `builder-table.json` `counts` says 39.** A
  literal grep of the prose file returns exactly 114 occurrences of the string, so the JSON count is
  counting whole cells that are nothing but NOT FOUND, not occurrences. Neither number is wrong, they
  measure different things. Worth reconciling so the two files stop appearing to disagree.

### 6. p39's link index only covers my block.

The outline wants "a compact grouped list of the blog articles the guide links to". I only know the
ten slugs on p28 to p31. p39 prints those ten by title and then says every article linked anywhere in
the guide is listed again in the companion source list. **Somebody has to assemble the full index
from all three writers' blocks**, either into p39 (which is already at 360 of 360, so something has
to give) or into the companion file. I recommend the companion file, and the sentence on p39 is
already written to point there.

### 7. Structured versus prose split not reported separately.

`page-budget.md` splits each page into prose and structured words. My counts are totals. Drawing the
line inside, for example, a `.card` that holds three sentences of running prose would be arbitrary,
and the binding gate is the 360 or 430 total. Totals are what I measured and totals are what I am
reporting.

---

## 11. Notes for the assembler

1. **`<!-- SVG-10 -->` on p28** is the only diagram placeholder in my block. It sits inside
   `<figure class="fig narrow">`; at 236px the 700x450 viewBox renders 152px tall, which is what the
   p28 fit measurement assumed.
2. **Every `.srcnote` is left empty** with the bare `data-srcnote` attribute, on all twelve pages.
3. **Foot classes alternate correctly:** `foot-r` on even pages 28, 30, 32, 34, 36, 38 and `foot-l`
   on odd pages 29, 31, 33, 35, 37, 39, so the folio always sits on the outside edge.
4. **No path edge tabs** anywhere in p28 to p39, per the block spec.
5. **Skeleton A on p28, p32, p36, p38.** Skeleton B on the rest. p32 is the one opener with no
   `.op-line`; the reason is in section 4.
6. **`.rh-b` carries the block running head** ("Six areas", "Builders, A to Z", "The numbers, Q3
   2026", "Before you sign") and `.rh-a` carries the per-page topic. The fragment contract's own p20
   example has that relationship the other way round. I followed the block table I was given. **If
   the contract's example is authoritative, swap the two spans on the eight interior pages**; it is a
   mechanical change and nothing else depends on it.
7. **Classes used, all from the inventory:** `page gp body pad cols two sm` / `band tone head rh-a
   rh-b foot foot-l foot-r folio srcnote` / `op-eyebrow op-h op-line op-deck op-body hit a attr src`
   / `q q-agave` / `card card-agave chk box t` / `refuse ribbon beat split` / `tbl-wrap sid tok
   tok-nf` / `fig figcap narrow` / `phone-row who phone-num close mk` / `opener opener-chip dissolve`
   / `tearout`. No class invented. No `position:fixed`. No `li::before`. No hex code.
8. **A temporary preview** was written to `build/_preview-ch3.html` for the fit measurement and
   deleted afterward. `build/fragments/` gains twelve `pNN.html` files and this note, which is the
   layout `build/fragment-contract.md` already specifies, so no Folder Map change is needed.
