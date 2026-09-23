# Handback: the rejoined core, pages 18 to 27

**Writer:** Chapter Writer 2
**Files:** `build/fragments/p18.html` through `p27.html`, ten files, 634 lines of markup.
**Em-dashes in this file and in all ten fragments: zero.**

---

## 1. Word count against budget

Counted as **total set words**: all rendered text including headings, table cells, checklist items,
callouts, figure captions and the pull line. Excluded: HTML comments, `alt` attributes, the inlined
SVG `<title>`/`<desc>` (they ship inside the diagram files, not in my copy), and the literal `*` of
each citation marker.

| Page | Budget row | Actual | Delta | 360 ceiling |
|---|---|---|---|---|
| 18 | 250 | **252** | +2 | pass |
| 19 | 320 | **310** | -10 | pass |
| 20 | 340 | **356** | +16 | pass |
| 21 | 350 | **356** | +6 | pass |
| 22 | 350 | **360** | +10 | pass |
| 23 | 330 | **358** | +28 | pass |
| 24 | 330 | **351** | +21 | pass |
| 25 | 330 | **360** | +30 | pass |
| 26 | 350 | **360** | +10 | pass |
| 27 | 330 | **359** | +29 | pass |
| **Block** | **3,280** | **3,422** | **+142** | every page inside the hard ceiling |

**Why the block runs 4 percent over its row budget.** Rule 7 sets the hard gate at 360 total set
words per page and every page here clears it. The row targets could not all be met because the
outline gives p22 seven dense numbered points, p23 six, and p26 six, each of which names five to
fifteen ledger claims that have to be stated to be citable. I cut content rather than type, in
three passes, and logged every claim I had to drop in section 4. If the executive editor wants the
row numbers hit exactly, the cheapest remaining cuts are named in section 4.4.

---

## 2. Page fit, measured

`.page` is a fixed box with `overflow:hidden`, so overset copy disappears with no error. I assembled
the ten fragments into `build/shell.html` with the real SVGs inlined, served it over HTTP, waited on
`document.fonts.ready`, and measured content bottom against the **print** box (10.96in, so the body
is 1004px, and 732px for the opener's `.op-body` which starts at top 272px).

| Page | Content bottom | Available | Slack |
|---|---|---|---|
| 18 | 706 | 732 | **26** |
| 19 | 873 | 1004 | 131 |
| 20 | 867 | 1004 | 137 |
| 21 | 913 | 1004 | 91 |
| 22 | 864 | 1004 | 140 |
| 23 | 947 | 1004 | 57 |
| 24 | 901 | 1004 | 103 |
| 25 | 619 | 1004 | **385** |
| 26 | 974 | 1004 | **30** |
| 27 | 690 | 1004 | **314** |

**p18 overflowed by 91px on the first build and is fixed.** Skeleton A only leaves 732px under the
photograph, and a full-width SVG-03 plus a two column row would not fit. It now runs head, one
paragraph, the diagram at `max-width:6.0in`, then one full-width card with a two column checklist.
**The figure's `max-width` is the lever on this page.** At 6.5in the slack drops to 3px, which is
inside font-loading variance, so do not enlarge it without re-measuring.

**p26 has 30px of slack.** It is the second tightest page in the block. Any copy added to it, or any
increase to the display tracking, needs a re-measure.

**p25 and p27 are underfull and I could not fix that with copy.** Both sit at the 360 word ceiling
already, so there is nothing to add. The cause is structural: a two column page at 9.5pt over 1.55
fits far more than 360 words, and p25 is a checklist page (type CL) whose body is almost entirely
two column. Three options for the design gate, none of which a chapter writer should pick alone:
1. Give p25 and p27 a photographic inset, the way p28 to p31 get one. This is the cheapest fix and
   it matches an existing pattern in the document.
2. Raise the leading on those two pages only. Type size must not move.
3. Accept the white space. p27 ends on the boxed CTA, and white space under a CTA is not a defect.

---

## 3. Mechanical gates, all run against the ten files

| Gate | Result |
|---|---|
| Em-dash and en-dash, source | **0** |
| HTML entities other than `&nbsp;` and `&middot;` | **0** |
| `data-claim` values not in the fact ledger | **0** of 160 |
| Classes outside the `design-system.md` inventory | **0** |
| `<img src="...svg">` | **0**. All seven diagrams are `<!-- SVG-nn -->` inside a `.fig` with a `.figcap` |
| `position:fixed` or `position:absolute` in a fragment | **0** |
| Hex codes | only inside the end-mark `<svg class="mk">` on p20, which is the pattern the winning preview already uses |
| `.srcnote` empty and present exactly once per page | **10 of 10** |
| Citation marker content is a literal `*`, never a digit or URL | **pass** |
| `/blog/` singular | **pass**, zero `/blogs/` |
| Clark County only, no Pahrump, Mesquite or Boulder City | **pass** |
| Foot class alternation | odd `foot-l`, even `foot-r`, folio on the outside edge |
| Path edge tab | **none on any page 18 to 27**, as briefed |

---

## 4. Claim-ids used, per page

160 unique ids. Every one resolves in `research/fact-ledger.md`.

**p18** (6): `proc-register-agent-first-contact`, `proc-loan-estimate-timing`, `proc-5-day-cancel-window`, `proc-year-one-45-day-window`, `proc-tax-postcard-after-july1`, `proc-warranty-clock-punch-list`

**p19** (7): `sid-definition`, `sid-term-length`, `sid-billed-semiannually`, `sid-separate-bill`, `sid-late-penalty`, `sid-delinquency-foreclosure`, `sid-apportionment`

**p20** (17): `sid-developer-method`, `sid-prepay-unincorporated`, `sid-summerlin-819`, `sid-summerlin-mesa-retired`, `sid-summerlin-centre-128a`, `sid-skye-canyon-610`, `sid-henderson-inspirada-t18`, `sid-nlv-valley-vista-64`, `sid-providence-607-matured`, `sid-cadence-none`, `sid-wellston-ridge-none`, `sid-absence-not-proof`, `sid-parcel-search`, `sid-henderson-billed-by-amg`, `sid-lookup-steps`, `sid-amg-phone`, `sid-closing-timing-trap`

**p21** (25): `tax-assessment-ratio`, `tax-taxable-value-method`, `tax-cost-service`, `tax-math-example`, `tax-rate-lasvegas-200`, `tax-rate-northlasvegas-250`, `tax-rate-henderson-505`, `tax-rate-enterprise-630`, `tax-rate-enterprise-635`, `tax-rates-vary-by-parcel`, `tax-statutory-rate-cap`, `tax-cap-3-percent-primary`, `tax-cap-8-percent-other`, `tax-newbuild-no-cap-year-one`, `tax-cap-statutory-reason`, `tax-lien-date-july-1`, `tax-late-improvement-unsecured-roll`, `tax-due-third-monday-august`, `tax-four-installments`, `tax-installment-dates`, `tax-bill-mailing-check`, `tax-grace-10-days`, `tax-late-penalties`, `proc-escrow-on-full-tax`, `proc-tax-postcard-after-july1`

**p22** (29): `fin-ipc-cap-over-90-ltv`, `fin-ipc-cap-75-to-90-ltv`, `fin-ipc-cap-under-75-ltv`, `fin-ipc-cap-investment`, `fin-ipc-includes-buydowns`, `fin-ipc-not-down-payment`, `fin-ipc-hoa-dues-limit`, `fin-va-concession-cap`, `fin-temp-buydown-mechanic`, `fin-temp-buydown-segregated-funds`, `fin-temp-buydown-note-rate-unchanged`, `fin-temp-buydown-limits`, `fin-temp-buydown-common-structures`, `bld-pulte-buydown-cost-example`, `bld-century-lender-split`, `bld-century-lender-cap`, `bld-drhorton-lender-conditioned`, `bld-taylormorrison-two-affiliates`, `bld-taylormorrison-preapply`, `bld-toll-lender-conditioned`, `bld-lennar-lender-conditioned`, `bld-beazer-no-lender`, `bld-beazer-mortgage-choice`, `bld-beazer-choice-conditioned`, `fin-respa-required-use`, `fin-aba-disclosure-required`, `fin-aba-disclosure-timing`, `fin-compare-same-day`, `mkt-incentive-climate`

**p23** (18): `proc-most-builders-no-timeline`, `proc-kb-build-time`, `proc-kb-preconstruction`, `proc-kb-total-published`, `proc-toll-build-time`, `law-lennar-two-year-completion`, `mkt-rate-july-2-2026`, `mkt-rate-july-9-2026`, `mkt-rate-july-16-2026`, `mkt-rate-july-23-2026`, `mkt-rate-range-july-2026`, `mkt-rate-15yr`, `mkt-rate-year-ago`, `mkt-rate-is-national-average`, `fin-forward-commitment-definition`, `bld-drhorton-rate-pool`, `bld-taylormorrison-rate-pool`, `fin-conforming-limit-clark-2026`

**p24** (10): `bld-kb-homesite-premium`, `bld-richmond-upgrade-limit`, `fin-insurance-flood-excluded`, `fin-insurance-rating-factors`, `law-lennar-amenities-not-promised`, `law-lennar-substitution`, `law-lennar-price-change`, `area-nlv-valleyvista-still-planned`, `area-nlv-valleyvista-completion`, `area-unionvillage-park-dispute`

**p25** (15): `rep-entity-name-warning`, `bld-lennar-entities`, `bld-pulte-entity`, `bld-signature-entity`, `bld-trust-entity`, `rep-nscb-search-link`, `rep-nscb-discipline-link`, `rep-harmony-license-expiring`, `rep-bbb-not-government`, `rep-pulte-bbb`, `rep-jdpower-discontinued`, `rep-not-checked`, `law-nrs624602-rights-sheet`, `area-hoa-resale-package-rights`, `fin-aba-disclosure-required`

**p26** (25): `insp-four-checkpoints`, `insp-predrywall-purpose`, `insp-kb-predrywall-verification`, `insp-punch-list-written`, `insp-11-month-reason`, `insp-no-statutory-right`, `insp-city-inspection-difference`, `law-nrs624602-written-warranty`, `law-nrs624602-clock-start`, `law-nrs624602-scope`, `law-nrs624602-transferable`, `law-nrs624602-no-waiver`, `law-1-2-10-not-required`, `law-no-2-year-statute`, `law-ten-year-is-deadline-not-warranty`, `law-nrs11202-repose`, `law-nrs11-2055-clock-start`, `law-repose-history`, `law-nrs40672-45-day-clock`, `law-nrs40672-discipline`, `law-nrs645d-inspector-license`, `law-nrs645d-inspector-insurance`, `law-arbitration-preempted`, `proc-warranty-clock-punch-list`, `proc-year-one-45-day-window`

**p27** (21): `fin-nevada-escrow-state`, `fin-nevada-escrow-regulator`, `fin-transfer-tax-rate`, `fin-transfer-tax-liability`, `fin-title-custom-nevada`, `fin-insurance-rebuild-basis`, `fin-insurance-rating-factors`, `fin-insurance-flood-excluded`, `fin-insurance-doi-tool`, `sid-closing-timing-trap`, `proc-assessment-closing-timing`, `proc-tax-postcard-after-july1`, `proc-warranty-clock-punch-list`, `proc-year-one-45-day-window`, `insp-11-month-reason`, `tax-installment-dates`, `law-nrs40-pursue-warranty`, `proc-register-agent-first-contact`, `law-buyer-agreement-2024`, `law-nrs645-compensation-disclosure`, `law-lennar-not-all-communities`

---

## 5. Blog slugs linked, the build-blocking gate

17 slugs, all recorded as NOT FOUND for publish status in `blog-corpus-map.md`. **Every one has to be
loaded live and confirmed to resolve before the guide ships.** All are written `/blog/<slug>`,
singular. Each appears in the corpus map, so none is invented.

| Page | Slug |
|---|---|
| 20 | `sid-lid-taxes-explained-las-vegas-new-construction` |
| 21 | `property-tax-new-construction-nevada` |
| 22 | `builder-incentives-las-vegas-2026` |
| 22 | `how-to-negotiate-las-vegas-home-builders` |
| 22 | `builders-preferred-lender-las-vegas` |
| 23 | `when-refinance-after-builder-lender` |
| 24 | `lot-premiums-explained-las-vegas-new-construction` |
| 24 | `covered-patio-options-las-vegas-new-construction` |
| 25 | `file-complaint-nevada-contractors-board` |
| 25 | `builder-complaints-las-vegas-protect-yourself` |
| 26 | `pre-drywall-inspection-las-vegas` |
| 26 | `blue-tape-walkthrough-checklist-las-vegas` |
| 26 | `11-month-warranty-inspection-las-vegas` |
| 26 | `nevada-warranty-law-1-2-10-explained` |
| 27 | `first-30-days-post-closing-las-vegas` |
| 27 | `new-construction-closing-costs-las-vegas` |
| 27 | `builder-wont-tell-first-year-new-home` |

p18 and p19 carry no blog link. p19 is the first half of a spread and p20 carries the spread's link.

---

## 6. Conflicts honored

| Conflict | What I did |
|---|---|
| `cft-sid-prepay-penalty` | p20 prints 3 percent **only** for unincorporated Clark County, cited to the Treasurer's payment options page, then prints the `Not found` token for city district terms and tells the reader to request a written payoff quote. Never presented as a valley wide rule. |
| `cft-cadence-sid` | p20 uses the developer's statement and immediately prints `sid-absence-not-proof` plus the parcel lookup, in the same card. |
| `cft-skye-canyon-sid-number` | p20's table row for 610 reads "Skye Canyon area" with the AMG dates. It does not describe what the district covers. |
| `cft-sid-159-final-date` | District 159 is not printed at all, so the conflict cannot leak. |
| `cft-fha-ipc-limit` | **No FHA contribution percentage appears anywhere on p22.** The prose says the cap exists, that it is lower at a small down payment, prints the `Not found` token, and sends the reader to their lender. The figcap prints only the conventional ladder. |
| `cft-arbitration-statute` | p26 writes it the second way: assume the clause is enforceable, cited to `law-arbitration-preempted`, and ask a Nevada attorney. **`law-arbitration-nrs597995` is deliberately not cited** and the guide nowhere says Nevada law voids an uninitialed clause. |

**Low-confidence claims, hedged in the sentence as required:**
`fin-title-custom-nevada` on p27 is introduced as "one general Nevada custom, per a State Bar
brochure" and immediately followed by "a builder contract overrides it". `insp-city-inspection-difference`
on p26 is stated as what a municipal inspection is, not as a claim about any Las Vegas builder.
`insp-builder-objections` was **dropped**, see 4.1. `mkt-design-center-markup` and
`mkt-builder-lender-rate-caution` were **not used**; p22 uses the CFPB comparison method
(`fin-compare-same-day`) instead, which is what the outline's hedge-or-drop line asks for.
`fin-forward-commitment-bulk-buydown` was **not used**; p23 describes the mechanism generically from
`fin-forward-commitment-definition` only.

---

## 7. NOT FOUND tokens printed

Nine `tok tok-nf` tokens across six pages, each with a plain statement of what is missing and what to
do about it instead:

| Page | Subject | Register item |
|---|---|---|
| 20 | Prepayment terms for city districts | 15 |
| 22 | The FHA interested party contribution percentage | 7, and conflict `cft-fha-ipc-limit` |
| 23 | Builder forward commitment rates and terms, lock extension and float down fee schedules | 12 |
| 23 | How often new construction appraises below contract, and who absorbs it | named gap in the outline, not in the register |
| 24 | What lot orientation costs in utility bills or comfort in Clark County | named gap in the outline |
| 24 | Any Las Vegas builder phase pricing schedule | named gap in the outline |
| 27 | Who pays the transfer tax on a builder contract | 10 |
| 27 | Whether any specific builder follows the title custom | 11 |
| 27 | A verified 2026 Clark County average homeowners premium | 13 |

p19 and p20 also carry the spread's real refusal: the `.refuse` panel on p20 states that no
government office and no developer publishes a per home or per community assessment amount, that
third party sites disagree by more than five times for the same master plan, and hands over the
lookup instead. That is register item 14, and it is the emotional center of the spread as briefed.

---

## 8. Things I could not do, and why

### 8.1 Claim-ids the outline names for my pages that I did not use

All were cut for the word ceiling, not because the ledger failed. None was replaced with an invented
number. Ranked by what I would restore first if the ceiling moves.

| Claim-id | Outline page | Why it is out | Where it still lands |
|---|---|---|---|
| `sid-summerlin-818`, `sid-summerlin-817`, `sid-summerlin-village16a-159`, `sid-southern-highlands-121`, `sid-skye-canyon-609`, `sid-skye-hills-612`, `sid-sunstone-613`, `sid-nlv-tule-springs-66`, `sid-nlv-aliante-60-matured`, `sid-henderson-black-mountain-t21`, `sid-henderson-rainbow-canyon-t20`, `sid-henderson-rainbow-canyon-t22`, `sid-henderson-matured-list`, `sid-henderson-loan-districts`, `sid-administrator-amg` | 19 and 20 | The outline lists 38 `sid-*` ids for a spread budgeted at 660 words. A 20 row table is roughly 100 table words on its own. I cut to a 7 row table chosen to prove the point the outline actually asks for: 151 retired in 2025 and 819 runs to 2055, same master plan, thirty years apart. | The area block. `guide-outline.md` lists `sid-summerlin-*`, `sid-skye-canyon-*`, `sid-nlv-*` and `sid-henderson-*` under p28 to p31, so Chapter Writer 3 carries the per-area districts. **This is the right division and not a loss, but somebody should confirm the area pages actually used them.** |
| `sid-county-public-works-phone` | 19 and 20 | 7 words. The AMG billing number survived; the county number did not. | Nowhere. Restore it to p20 checklist step 3 first if any words free up. |
| `fin-temp-buydown-early-exit` | 22 | 14 words. Sell or refinance early and the leftover goes against your balance, not back to you as cash. | Nowhere. This is the single most useful fact I dropped in the whole block. **Restore it to p22 first.** |
| `bld-beazer-choice-share` | 22 | 10 words, the "roughly 80 percent of buyers use one" figure. | Nowhere. |
| `bld-century-concession-warning` | 22 | 20 words. Century's written warning that combined incentives may exceed your loan program's limits. | p13, which the outline also assigns it to. Path B readers get it. Path A and C readers do not. |
| `fin-points-*` | 22 | The outline lists them, but points are fully treated on p16 and p22 had no room to repeat them. | p16. |
| `proc-blueheron-start-window`, `proc-blueheron-closing-window`, `proc-christopher-windows` | 23 | 32 words for one sentence about two regional builders' published windows. Cut in the final pass to bring p23 from 443 to 358. | p10 lists the same ids, so Path B readers may get them. Path A and C readers do not. |
| `insp-builder-objections` | 26 | Low confidence, national sourcing, and it needed a full attributing clause to be usable. Dropping it was cheaper than hedging it. | Nowhere, deliberately. |
| `law-repose-ab125`, `law-repose-ab421` | 26 | The bill numbers. p26 keeps the fact that it was six years from 2015 to 2019 via `law-repose-history`. | Nowhere. |
| `law-nrs113-newbuild-exempt`, `law-nrs6243017-workmanship` | 26 | Both were in an earlier draft and were cut in the final pass. | Nowhere. |
| `mkt-cash-share`, `tax-cap-one-property-rule`, `tax-false-claim-penalty`, `tax-recording-removes-cap`, `tax-postcard-claim` | 21 | The one-property rule, the recording trigger and the three-times-deficiency penalty are the move-up framing, and the outline assigns them to p12. p21 carries the reset, the rate table and the calendar. | p12. |

### 8.2 Image alt text is not in the manifest

The contract says alt text comes from `assets/image-manifest.md` **verbatim**. That file has no alt
text column and no alt text section; it carries the generation prompts, the review column and the
job IDs. I derived the alt for `open-core.jpg` from the IMG-06 prompt sentence, which is the closest
reviewed description that exists:

> The Las Vegas valley at dusk from a low ridge, dense city lights spreading to the horizon under a
> deep blue sky, the last warm light on the mountains at the right edge.

It matches the phrasing Chapter Writer 1 used for `open-path-c.jpg` on p14 and p17. Chapter Writer 3
used the fuller prompt form including the "Wide documentary photograph of" prefix on p28. **The three
blocks are inconsistent in that one respect.** Somebody should either add an alt column to the
manifest or normalize all fifteen at assembly. It is a real accessibility gate and it should not be
decided by three writers separately.

### 8.3 Two upstream inconsistencies I had to rule on

**The p18 foot class.** `fragment-contract.md` gives a rule table (odd right-hand page takes
`foot-l`, even left-hand takes `foot-r`, so the folio sits on the outside edge) and then shows a p18
skeleton whose foot is `foot-l`. p18 is even, so those two disagree. `page-budget.md` adds a third
input by declaring p18 a right-hand page while also stating that odd pages are right-hand, and it
flags that tension as a design gate item rather than solving it. **I used `foot-r` on p18**, because
both other chapter writers alternated strictly on odd and even across p2 to p34 and a single page
breaking the alternation is the one outcome the rule's own rationale forbids. If the executive
editor wants the contract's literal skeleton instead, p18 flips to `foot-l` and p19 to `foot-r`, and
the whole document shifts with it.

**The chapter number in the opener eyebrow.** The contract's p18 skeleton reads "Chapter three".
Chapter Writer 3 shipped "Chapter six" on p28 and "Chapter seven" on p32, which numbers by block, so
the core block is five. **I used "Chapter five."** If the intended scheme is "front matter, your one
path, then the core" the core is three and both p28 and p32 also have to change.

### 8.4 Requests to `design-system.md`, not local improvisations

1. **`.tok` needs a right side correction when punctuation follows it.** The token is `inline-flex`
   with 4pt of right padding, so `<span class="tok tok-nf">...</span>.` renders with a visible gap
   before the period. It reads as a typo at 100 percent. I reordered five instances so the token
   leads its sentence and is followed by a word, which is free and reads better anyway. Four
   instances remain where reordering would cost words I do not have: p22 once, p27 three times.
   **A `margin-right:-1.5pt` on `.tok`, or a `.tok-tight` modifier, fixes it document wide in one
   line and would let all three writers stop working around it.**
2. **There is no class for a soft close that is not the full `.close` bar.** p20 wanted one and used
   `.close` with the end mark, copying the winning preview. That works, but it is the only place in
   my block where a fragment carries inline SVG markup of its own, which sits oddly next to the rule
   that diagrams are placeholder comments. A `close` variant with the mark baked in would remove the
   inline SVG from the fragment.
3. **Nothing else.** No new class, hex or type size was invented in these ten pages.

### 8.5 What I checked and could not verify myself

`build/shell.html` changed under me mid-build. It gained a `.gp a, .close a, .card a` rule about
fifteen minutes after I first read it, which is what makes the blog links render clay and gold
instead of browser blue. My final fit measurements are against the shell as of that change. **If the
shell changes again, re-run the fit measurement**, because p18 has 26px of slack and p26 has 30px
and either one will overset silently.

---

## 9. Notes for the fact auditor

- Repeated claim-ids across pages are intentional, not copy-paste. `proc-warranty-clock-punch-list`
  appears on p18, p26 and p27 because the sequence names it, the warranty page proves it, and the
  first-year calendar dates it. Same for `proc-tax-postcard-after-july1`, `proc-year-one-45-day-window`,
  `insp-11-month-reason`, `sid-closing-timing-trap` and `fin-insurance-*`. If `assemble.py` numbers
  markers globally, each repeat gets its own marker number pointing at the same URL, which is
  correct behavior for a per-page source strip.
- `sid-separate-bill` is cited twice on p19, on item 2 for the separate billing and on item 3 for the
  lien, because the ledger row carries both facts.
- Every dated figure carries its date in the sentence: May 2026 for the incentive climate, July 2026
  for the four weekly rates, fiscal 2026-2027 for the tax rates, 2026 for the conforming limit.
- The compensation caveat is on p27 inside the CTA, in the required form: how compensation is
  documented (`law-buyer-agreement-2024`, `law-nrs645-compensation-disclosure`), that builder-paid
  compensation is common **and not universal**, and the named builder that says in writing it does
  not pay cooperating brokers everywhere (`law-lennar-not-all-communities`). **The guide nowhere says
  representation is free.**
