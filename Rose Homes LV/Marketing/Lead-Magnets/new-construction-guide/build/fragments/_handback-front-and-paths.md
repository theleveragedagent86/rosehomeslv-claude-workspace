# Handback: front matter and the three paths, p1 to p17

**Writer:** Chapter Writer 1
**Files:** `build/fragments/p01.html` through `p17.html`
**Written against:** `build/fragment-contract.md`, `outline/guide-outline.md` (BLOCKS 1 to 4), `outline/page-budget.md`,
`outline/audience-path-map.md`, `build/design-system.md`, `research/fact-ledger.md`, `research/internal/voice-exemplars.md`,
`assets/image-manifest.md`, `build/svg/index.md`, `build/shell.html`.

**Em-dashes in these 17 fragments: zero.** Checked in source, as entities, and as U+2013 as well.
**HTML entities used: `&nbsp;` and `&middot;` only.** Verified mechanically.
**`position:fixed`: none.** **Hex codes: none** except the four `.seam` bars on the cover, which are the
documented exception and are copied verbatim from the frozen preview.
**Claim-ids: all 148 unique ids validate against the ledger.** `assemble.py` runs clean over p1 to p17;
its only hard stop today is `cft-la-vegas-realtors-domain` on p37, which is not my block.

---

## 1. Word count against budget

Counted after tag stripping, with `&nbsp;` and `&middot;` resolved, on the whole set page (prose plus
tables, checklists, captions, callouts and the contents block), which is the "total set words" column
in `page-budget.md`.

| Page | Section | Budget | Actual | Verdict |
|---|---|---|---|---|
| 1 | Cover | 40 | **86** | **OVER, see the note below. Not editable.** |
| 2 | How this guide works, contents | 300 | 297 | ok |
| 3 | Who works for whom | 260 | 258 | ok |
| 4 | Register before the first visit | 330 | 325 | ok |
| 5 | Which of these sounds like you | 250 | 232 | ok |
| 6 | Path A opener | 300 | 256 | ok |
| 7 | Path A, buying from a distance | 330 | 330 | ok, at the line |
| 8 | Path A, paying cash | 320 | 320 | ok, at the line |
| 9 | Path A close, before you book the trip | 330 | 330 | ok, at the line |
| 10 | Path B opener, you already own | 280 | 271 | ok |
| 11 | Path B, selling while you build | 340 | 339 | ok |
| 12 | Path B, your cap does not move | 340 | 337 | ok |
| 13 | Path B close, what your equity buys | 340 | 340 | ok, at the line |
| 14 | Path C opener, "included" | 300 | 258 | ok |
| 15 | Path C, down payment help | 350 | 348 | ok |
| 16 | Path C, the Loan Estimate | 330 | 330 | ok, at the line |
| 17 | Path C close, monthly cost | 300 | 300 | ok, at the line |
| **Total** | | **5,040** | **4,957** | under |

**p1 is the one overrun and it is not mine to fix.** The cover markup is the frozen preview markup,
lifted verbatim per the contract, and it sets 86 words: eyebrow, title, subtitle, three geography
chips, the credential pill, byline, brokerage, edition block and the two line compliance strip.
`page-budget.md` allots 40. Nothing in that 86 is discretionary copy; every line is either the title
system or an NRS 645 compliance string. Either the budget row is wrong or the frozen cover is, and
that is a decision above a chapter writer. I changed only the image path, to `assets/img/cover.jpg`,
and added `id="p1"`.

**Do not add `gp` to p1.** `.gp p` is (0,1,1) and uses the `font` shorthand, so it beats `.cover-sub`
(0,1,0) and would silently reset the cover subtitle to 9.5pt body. The frozen preview omits `gp` on
the cover for that reason and I kept it omitted.

---

## 2. Page fit, measured

`.page` is `overflow:hidden`, so overset copy disappears with no error. I measured every page in the
assembled shell over CDP after `document.fonts.ready` and image `decode()`, comparing the bottom of
the last content block against the top of the `.foot`. Negative means clearance.

```
p1 -42  p2 -22  p3 -243  p4 -329  p5 -239  p6 -175  p7 -425  p8 -446  p9 -381
p10 -14 p11 -399 p12 -525 p13 -438 p14 -25 p15 -388 p16 -473 p17 -179
```

Nothing clips. The three tight pages are the section openers that also carry a diagram, p10 and p14,
plus p2 with the contents block. If anyone edits copy on p2, p10 or p14, re-measure; they have 14 to
22px of room, which is one line of body copy.

---

## 3. Claim-ids used, by page

| Page | Claim-ids |
|---|---|
| p1 | none. `law-nrs645-advertising` is satisfied by the printed `Real Broker, LLC` and license `S.0185572`, and the outline marks the page as carrying no source marker. See item 6 below. |
| p2 | none. The page states method, not facts, per the outline. |
| p3 | `law-lennar-nhc-not-your-agent`, `law-nrs645-compensation-disclosure`, `law-duties-owed-form`, `law-nrs645-client-duties`, `law-nrs645-duties-nonwaivable`, `law-buyer-agreement-2024`, `proc-buyer-agreement-before-touring` |
| p4 | `proc-register-agent-first-contact`, `law-lennar-broker-registration`, `law-lennar-appointment-not-registration`, `law-lennar-registration-term`, `law-richmond-broker-policy`, `law-tripointe-registration-each-community`, `law-lennar-not-all-communities`, `law-nrs645-compensation-disclosure`, `law-buyer-agreement-2024` |
| p5 | none. Navigation page. |
| p6 | `fin-nevada-escrow-state`, `fin-nevada-escrow-regulator`, `proc-lennar-closing-estimate`, `proc-richmond-closing-not-guaranteed`, `law-lennar-two-year-completion` |
| p7 | `insp-four-checkpoints`, `insp-predrywall-purpose`, `law-nrs645d-inspector-license`, `law-nrs645d-inspector-insurance`, `insp-no-statutory-right`, `fin-nevada-escrow-state` |
| p8 | `mkt-cash-share`, `bld-century-lender-split`, `bld-century-lender-cap`, `bld-drhorton-lender-conditioned`, `bld-lennar-lender-conditioned`, `fin-respa-required-use`, `fin-aba-disclosure-required`, `fin-aba-disclosure-timing`, `bld-century-concession-warning`, `law-nrs116-5-day-cancel`, `law-nrs116-cancel-refund`, `law-nrs116-cancel-condition` |
| p9 | `tax-assessment-ratio`, `tax-taxable-value-method`, `tax-cap-3-percent-primary`, `tax-cap-8-percent-other`, `tax-cap-one-property-rule`, `tax-newbuild-no-cap-year-one`, `fin-worker-advantage-residency`, `fin-worker-advantage-jobs`, `area-commute-valleywide`, `area-ccsd-verify-by-address` |
| p10 | `proc-most-builders-no-timeline`, `proc-kb-build-time`, `proc-kb-preconstruction`, `proc-kb-total-published`, `proc-toll-build-time`, `bld-kb-selections-deadline`, `proc-selections-before-build`, `law-lennar-two-year-completion`, `proc-lennar-outside-completion`, `proc-lennar-closing-estimate`, `proc-richmond-closing-not-guaranteed` |
| p11 | `law-no-earnest-money-statute`, `proc-lennar-closing-estimate`, `mkt-resale-median-june-2026`, `mkt-60-day-share`, `mkt-months-supply-resale`, `mkt-sf-inventory-june-2026`, `mkt-mls-caveat` |
| p12 | `tax-newbuild-no-cap-year-one`, `tax-cap-statutory-reason`, `tax-recording-removes-cap`, `tax-postcard-claim`, `proc-tax-postcard-after-july1`, `tax-cap-one-property-rule`, `tax-cap-3-percent-primary`, `tax-cap-8-percent-other`, `tax-false-claim-penalty`, `tax-lien-date-july-1`, `proc-escrow-on-full-tax` |
| p13 | `fin-ipc-cap-over-90-ltv`, `fin-ipc-cap-75-to-90-ltv`, `fin-ipc-cap-under-75-ltv`, `fin-ipc-cap-investment`, `fin-ipc-includes-buydowns`, `fin-ipc-not-down-payment`, `fin-ipc-hoa-dues-limit`, `bld-century-concession-warning`, `mkt-new-median-june-2026`, `mkt-resale-median-june-2026`, `mkt-gap-same-month`, `mkt-gap-clever-study`, `mkt-gap-clever-rank` |
| p14 | `bld-lgi-no-upgrades`, `bld-lennar-upgrade-model`, `bld-signature-standards`, `bld-beazer-solar`, `bld-pulte-design-center`, `bld-kb-design-studio`, `bld-richmond-design-center`, `bld-toll-design-collections`, `bld-kb-selections-deadline`, `proc-selections-before-build`, `bld-richmond-upgrade-limit`, `bld-no-design-credit-published`, `bld-no-upgrade-financing-published`, `insp-kb-predrywall-verification` |
| p15 | `fin-hip-ftb-amount`, `fin-hip-ftb-structure`, `fin-hip-ftb-definition`, `fin-hip-ftb-credit-score`, `fin-hip-ftb-limits-date`, `fin-hip-ftb-clark-price-limit`, `fin-hip-ftb-clark-income-small`, `fin-hip-ftb-clark-income-large`, `fin-hip-standard-amount`, `fin-hip-standard-income-cap`, `fin-hip-standard-price-cap`, `fin-worker-advantage-amount`, `fin-worker-advantage-structure`, `fin-worker-advantage-buydown-option`, `fin-worker-advantage-jobs`, `fin-worker-advantage-residency`, `fin-worker-advantage-launch`, `fin-worker-advantage-funding`, `fin-worker-advantage-clear-to-close`, `proc-dpa-clear-to-close`, `fin-teacher-dpa-amount`, `fin-teacher-dpa-forgivable`, `fin-teacher-dpa-expiration`, `bld-touchstone-second-loan`, `bld-touchstone-conditioned`, `fin-ipc-not-down-payment`, `fin-clark-clt-not-builder-program`, `fin-clark-clt-down-payment`, `fin-rural-programs-not-valley` |
| p16 | `fin-loan-estimate-3-days`, `proc-loan-estimate-timing`, `fin-loan-estimate-page3`, `fin-compare-same-day`, `mkt-rate-range-july-2026`, `mkt-rate-is-national-average`, `fin-points-definition`, `fin-points-no-fixed-ratio`, `fin-points-compare-method`, `fin-conforming-limit-clark-2026`, `fin-conforming-increase-2026`, `fin-conforming-announced-date`, `fin-conforming-highcost-ceiling-2026`, `fin-fha-limit-clark-1unit-2026`, `fin-fha-clark-at-national-floor`, `fin-fha-clark-median-basis`, `fin-fha-2026-effective-date`, `fin-va-no-loan-limit`, `fin-va-zero-down`, `fin-va-full-entitlement-marker`, `fin-va-entitlement-not-approval` |
| p17 | `bld-lgi-payment-footnote`, `bld-kb-homesite-premium`, `bld-richmond-upgrade-limit`, `tax-newbuild-no-cap-year-one`, `area-summerlin-hoa-structure`, `area-cadence-hoa-structure`, `area-cadence-hoa-amount`, `sid-separate-bill`, `area-hoa-resale-package-rights`, `fin-insurance-flood-excluded`, `fin-insurance-rebuild-basis`, `fin-insurance-rating-factors`, `fin-insurance-doi-tool` |

**148 unique claim-ids.** Every one resolves in `research/fact-ledger.md`.

### Claim-ids the outline listed for my pages that I did not use, and why

| Claim-id | Outline page | Why not used |
|---|---|---|
| `law-nrs645-advertising` | p1 | The cover is frozen markup and carries no source marker. The compliance strings it requires are printed. |
| `area-summerlin-to-strip`, `area-skyecanyon-to-downtown` | p9 | The outline names them only to explain the refusal. Printing either would print a drive time, which the ledger's low-confidence table forbids. p9 prints the `NOT FOUND` token instead, and cites `area-commute-valleywide` named in the sentence as a survey, which is exactly the handling the ledger prescribes. |
| `bld-beazer-choice-plans` | p14 | Not in any of p14's six numbered points, and the page was 55 words over before trimming. |
| `law-lennar-substitution` | p14 | Same reason. It was written, then cut when the page needed 35 more words removed to let SVG-11 render at a legible size. **This is a good fact and it is homeless.** It belongs on p22 or p26 if either has room. |
| `mkt-cash-share` | p8 | Used. Noting only that it is the one market figure in Path A, and it is labeled June 2026. |

---

## 4. Blog slugs linked, 19 total

**Every one is a build-blocking gate.** `blog-corpus-map.md` records publish status as NOT FOUND for
all 110 slugs. These 19 have to be loaded live and confirmed to resolve before the guide ships. All
are written as `https://rosehomeslv.com/blog/<slug>`, singular.

| Page | Slug |
|---|---|
| p3 | `do-you-need-realtor-new-construction-las-vegas` |
| p4 | `bring-realtor-first-visit-model-homes` |
| p6 | `moving-california-las-vegas-new-construction` |
| p6 | `new-construction-buying-process-las-vegas` |
| p8 | `builders-preferred-lender-las-vegas` |
| p10 | `new-construction-timeline-las-vegas` |
| p10 | `construction-delays-las-vegas` |
| p11 | `cancel-new-construction-contract-las-vegas` |
| p12 | `property-tax-new-construction-nevada` |
| p14 | `design-center-experience-las-vegas` |
| p14 | `builder-upgrade-markup-las-vegas` |
| p14 | `structural-upgrades-cannot-change-las-vegas` |
| p15 | `down-payment-assistance-las-vegas-2026` |
| p16 | `fha-loan-new-construction-las-vegas-2026` |
| p16 | `va-loan-new-construction-las-vegas` |
| p17 | `true-monthly-cost-new-construction-las-vegas` |
| p17 | `hoa-fees-las-vegas-new-construction` |
| p17 | `why-las-vegas-two-three-hoa-fees` |
| p17 | `lot-premiums-explained-las-vegas-new-construction` |

Plus the external relocation guide, linked exactly twice as the path map requires: `https://rosehomeslv.com/moving-to-las-vegas` on **p6** and **p9**.

---

## 5. CTA and path plumbing, as built

- **Primary CTA:** p4 (full treatment, boxed, with the phone chip), p9 (Path A close), p17 (Path C close). Three of the five. Wording differs on all three: p4 asks for the community and the day, p9 asks for travel dates and budget, p17 asks for the community and plan name.
- **Seller CTA:** p11 only. One artifact offered, a one page value range with the three closest sales behind it. No deadline, no scarcity, no second appearance anywhere in p1 to p17.
- **The compensation caveat** is on p4 in its own card. It never says representation is free. It names `law-lennar-not-all-communities` out loud, then describes documentation via `law-nrs645-compensation-disclosure` and `law-buyer-agreement-2024`.
- **Rejoin sign** set verbatim at the foot of p9, p13 and p17.
- **p5 branch copy** set verbatim from `audience-path-map.md` section 1, including both sentences of each of the three self-descriptions.
- **Edge tabs** on p6 to p17 only, as the last child of `.page`, after the foot. `tab-a` 6 to 9, `tab-b` 10 to 13, `tab-c` 14 to 17. Nothing else carries one.
- **Path label on screen** is carried by `.rh-b` in the band on interior path pages and by the `.opener-chip` on the openers, so it is real text and not print-only.
- **Foot alternation:** odd pages `foot-l` (folio outside right), even pages `foot-r`. Openers p2, p6, p10, p14 are all even and use `foot-r`.
- **Path A restates nothing** from the relocation guide. Neighborhoods, cost of living, schools and the case for the valley get one paragraph and a link on p6.
- **Cross-references** are all "see page N" or "page N". No path page points sideways at another path page.

---

## 6. Things I could not do, or did differently. Read this part.

**a. `assets/image-manifest.md` contains no alt text.** The contract says alt text comes from that
file verbatim and that it was human-reviewed against the fair housing gate. The file has an ID table,
a resolution policy, job IDs and the generation prompts, and **no alt column anywhere.** I wrote alt
text myself, derived sentence by sentence from each image's own prompt in that file, and it is
identical on every page inside a block so a screen reader hears the same band described the same way.
It is **not reviewed.** Someone has to review these four strings and then add them to the manifest so
the next writer does not invent a second set:

- `open-front.jpg`: "An empty graded home pad at first light, survey stakes and string lines in compacted caliche soil, with a bare rocky Mojave ridge in the middle distance."
- `open-path-a.jpg`: "The Las Vegas basin seen from high on a mountain road at mid morning, the whole valley laid out flat to a far range, Joshua trees and creosote in the foreground."
- `open-path-b.jpg`: "Established desert suburban rooftops in warm late afternoon light, tile roofs and mature landscaping receding toward a bare rocky Mojave mountain range."
- `open-path-c.jpg`: "New stick framing against an open sky at golden hour, raw lumber studs and trusses with plywood sheathing, desert ground and a distant ridge beyond."

The cover alt is the frozen preview's own string and was not touched.

**b. The folio cannot hold "6 &middot; A".** `audience-path-map.md` section 3 and its build checklist
require the path letter on the folio for p6 to p17. `.folio` is a fixed 0.48in by 0.40in box at 15pt
Bodoni with `overflow:hidden` on the page, so "10 &middot; B" clips silently. I set **`6A`, `7A` ...
`17C`**, two or three glyphs, which fits and still gives a reader who set the guide down the letter
they need. If the design owner wants the interpunct, `.folio` has to get wider, and that is a
design-system change, not a fragment change.

**c. Diagrams on the two section openers render small, and this needs a design decision.**
`.op-body` is a flex column that gets 736px of height, and the opener headline block (eyebrow,
`op-h`, `op-line`, `op-deck`) eats 226px of it before any content. That leaves about 510px for the two
prose columns plus the diagram. A 700px-wide SVG at full column width would be 402px tall, which
leaves five lines per column for content the outline locks at six numbered points.

Also worth knowing, because it will bite the next writer: **an inlined `<svg>` inside a flex column
shrinks to its 300px default intrinsic width and ignores a larger `max-width`.** You have to set an
explicit `width` to get past 300px. I did:

| Page | Diagram | Rendered width | Share of its 700px design width |
|---|---|---|---|
| p10 | SVG-13 | 3.3in, 317px | 45 percent |
| p14 | SVG-11 | 3.5in, 336px | 48 percent |
| p3 | SVG-02 | 6.9in, 662px | 95 percent, block context, fine |
| p5 | SVG-01 | 6.6in, 634px | 91 percent, block context, fine |
| p17 | SVG-12 | column width, 343px | 49 percent, but it is a vertical stack and reads at that size |

SVG-11 and SVG-13 are wide diagrams with internal labels. At 45 to 48 percent their label type lands
around 4pt in print, which is under the design system's own floor for anything a reader has to read.
I did not shrink them further and I did not drop them. **Two clean options for the design owner:**
move SVG-11 and SVG-13 onto the interior page that follows each opener, where there is block context
and 6.9in of width, or have `build-svg.py` emit a compact opener variant of those two at a taller
aspect. Either is a decision above a chapter writer, so I flagged it rather than solving it.

**d. Anchors have no style rule.** `design-system.md` has no class for a link and `shell.html` has no
`a` selector, so all 21 links in my block render as default browser blue with a default underline,
which is off-palette in print. I did not invent a class. This is a request to the design system: it
needs one link treatment, probably `--navy-700` with a thin underline.

**e. Builders are not named in body copy on p1 to p17.** The outline's own wording for these pages is
anonymized throughout ("one large builder", "a second builder", "a third builder", "another says"),
and the standing disclaimer that governs using builder data sits on p32. I followed the outline's
wording exactly rather than naming Lennar, Richmond American, Tri Pointe, Century, D.R. Horton, KB,
Pulte, Toll, LGI, Beazer, Signature or Touchstone in prose. The generated source strip and the
companion source list will name every organization, which is where a reader who wants the name will
look. **If the executive editor wants builders named in the path pages, that is a one pass edit to
p4, p6, p8, p10, p14, p15 and p17, but it should be decided against the p32 disclaimer, not by me.**

**f. The p2 contents merges the back matter into one row.** "Ask before you sign, about, legal" points
at page 38. The two column contents block was 22px too tall with p38 and p39 on separate rows and the
page has no other slack. p38 and p39 are one physical spread, so a reader who turns to 38 has 39 in
hand. Say the word and I will restore the two rows if a row can come out somewhere else.

**g. Conflicts honored, explicitly.**
- `cft-worker-advantage-price-cap`: p15 prints **no** hard price cap. It says the cap is tied to the conforming limit and to confirm with a participating lender.
- `cft-fha-clark-limit`: p16 prints $541,287 and nothing else. **$552,000 appears nowhere.**
- `cft-fha-ipc-limit`: p16 prints **no** FHA contribution percentage, prints the `NOT FOUND` token, and sends the reader to their lender.
- `cft-new-vs-resale-gap`: p13 prints both measurements, the June 2026 same month $35,000 gap and the June 22, 2026 study's $79,460, and says in plain words why they differ.
- `cft-months-supply`: p11 prints about 3.5 months, the association's own figure, and nothing else.
- `area-commute-valleywide` is named as a survey in the sentence, per the low-confidence table.

**h. NOT FOUND tokens printed, and where.** p2 (explaining the convention), p9 (drive times), p11
(no statutory late delivery remedy and no obtained purchase agreement, and no earnest money statute),
p14 (design center spend and credit, upgrade financing), p15 (the 5 percent structure, funds
remaining, the Clark County income cap detail, the land trust status, city programs), p16 (the FHA
contribution cap), p17 (HOA amounts for seven communities, and the Clark County insurance premium).
Every one of them is followed by how to go get the answer, per voice exemplar 3.

**i. p6 and p14 finished under budget** at 256 of 300 and 258 of 300. Both cover all of their numbered
points. p14's 42 words of headroom exist because I traded copy for diagram size, per item c. If item c
is solved by moving SVG-11, that space should go back to the substitution fact in item 3.
