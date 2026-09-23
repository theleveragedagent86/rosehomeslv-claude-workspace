# Handback, diagram sizing remediation

**Brief:** four diagrams printed at 2.9 to 3.2pt and were illegible. Fix them without shrinking type,
without scaling a diagram below 85 percent of measure, without losing a fact, and without adding
clipping.

**Written against:** `build/design-system.md` ("Diagram sizing, the rule that was measured"),
`build/fragment-contract.md`, `outline/guide-outline.md`, `outline/page-budget.md`,
`build/svg/index.md`, `research/internal/voice-exemplars.md`.

**Files edited:** `p10.html`, `p11.html`, `p14.html`, `p15.html`, `p17.html`. **`p28.html` is
unchanged and unsolved, see section 4.** Nothing in `build/svg/` was touched.

**Em-dashes added: zero.** `qa-check.py` reports 183 source files clean and 0 in the PDF text layer.
Claim-ids: 364 citations, 364 unique, all validate. Page count still 39. No blank pages.
QA profile is byte-identical to before this pass: 26 pass, 3 warn, 4 fail, and all four fails are
pre-existing and on pages I did not touch (the 43rd image's alt, and the three disclosed
Pahrump/Mesquite/Boulder City mentions that the earlier handbacks already documented as intentional).

---

## 1. How this was measured

Assembled over HTTP, loaded headless over CDP, measured after `document.fonts.ready` and
`decode()` on all 42 images.

- **Diagram scale** = rendered `svg` width / its `viewBox` width. The printed measure is 710.4px, so
  full measure reads as 1.015 against a 700 viewBox. Smallest label = `6 x (W / 710)` points.
- **Clipping** = for every element in a `.page`, `bottom - .foot.top`, skipping `.foot` and anything
  inside an `svg`. Reported both leaf-only and all-elements; the two agree everywhere.

Scripts are throwaway and live in the session scratchpad, not in the repo.

---

## 2. Results, before and after

| Page | Diagram | Rendered before | Scale before | Label before | Rendered after | Scale after | Label after |
|---|---|---|---|---|---|---|---|
| p10 | SVG-13 | 316.8px | 0.453 | 2.68pt | diagram moved to p11 | n/a | n/a |
| p11 | SVG-13 | no diagram | n/a | n/a | **710.4px** | **1.015** | **6.00pt** |
| p14 | SVG-11 | 336.0px | 0.480 | 2.84pt | diagram moved to p15 | n/a | n/a |
| p15 | SVG-11 | no diagram | n/a | n/a | **643.2px** | **0.919** | **5.44pt** |
| p17 | SVG-12 | 343.2px | 0.490 | 2.90pt | **652.8px** | **0.933** | **5.52pt** |
| p28 | SVG-10 | 236.0px | 0.337 | 1.99pt | **unchanged** | **0.337** | **1.99pt** |

Clipping, `bottom - foot.top`, negative is clearance:

| Page | Clip before | Clip after |
|---|---|---|
| p10 | -14.2px, no clip | -182.7px, no clip |
| p11 | -411.8px, no clip | -32.2px, no clip |
| p14 | -25.0px, no clip | -248.7px, no clip |
| p15 | -390.4px, no clip | -10.7px, no clip |
| p17 | -192.0px, no clip | -24.9px, no clip |
| p28 | -54.2px, no clip | -54.2px, no clip |

**Zero pages in the whole guide clip after this pass**, under both the leaf-only and the
all-elements scan. p11, p15 and p17 are now the three tightest pages in the guide at 32, 11 and 25px
of clearance. **Re-measure those three after any copy edit;** 11px is under one line of body copy.

### A note on p18

The brief said p18 clips by 55px. **It does not reproduce.** p18 measures -63.1px leaf and -63.1px
all-elements, i.e. 63px of clearance. The most likely explanation is a detector counting `.op-body`,
which is `position:absolute; bottom:0`; on an opener that box ends at the bottom of `.body`, which is
exactly `foot.top`, so it registers 0 or, if measured against the page box instead of `.body`, 48px.
Either way I left p18 alone as instructed and its SVG-03 is still 0.823, just under the floor.

---

## 3. What changed on each page

### p10, Path B opener. SVG-13 moved off.

- Removed `<figure class="fig" style="width:3.3in; ...">` and its `<!-- SVG-13 -->` placeholder.
- Added one clause of wayfinding to the last paragraph of the right column: **"The two clocks are
  drawn on page 11."**

**Prose cut: none. Claim-ids moved or dropped: none.** All five of the outline's numbered points and
all eleven of p10's claim-ids stay on p10, untouched.

**Why moved rather than cut.** Full measure needs 345px of svg plus a 21px caption. p10's `.op-body`
gets 736px, the locked headline block (`op-eyebrow`, `op-h`, `op-line`, `op-deck`) eats 226px of it
before any content, and the `.cols` block measures 321px with column contents of 227 and 312. To buy
the 177px the diagram needed, the grid would have to come down to 144px, which means deleting roughly
nine lines from each column. Every paragraph in that grid is claim-bearing, so the cut loses facts.
The brief's own test, "worth real prose cuts if the cuts do not lose a fact", therefore selects the
move. This is also the option the original writer named in
`_handback-front-and-paths.md` section c.

p10 now carries 183px of trailing clearance on the opener. That is inside the existing range for this
skeleton; p6, the Path A opener, carries 194px.

### p11. SVG-13 installed at full measure.

- Inserted a full-measure `<figure class="fig" style="margin:8pt auto 9pt">` between
  `h2.a` ("Both cost something. Neither one is a rule.") and the `.cols`, **above** the two cards, so
  the seller CTA keeps the bottom of the page and the visual weight the outline gives it.
- Caption: "From page 10. Four places the two clocks can collide."

**Prose cut: none. Claim-ids: none added, none moved.**

**Outline deviation, declared.** `guide-outline.md` p11 says "**SVG: none.** The seller CTA block owns
the visual weight on this page." The brief overrides that by naming "move the diagram to the following
interior page (p11, p15)" as an option. Placing the figure above the cards rather than below them is
how I tried to honour the outline's intent inside the override. **If the outline owner wants the
original rule enforced, the diagram has nowhere else legible to go and p14/p10 come back into play.**

### p14, Path C opener. SVG-11 moved off.

- Removed `<figure class="fig" style="width:3.5in; ...">` and its `<!-- SVG-11 -->` placeholder.
- Added **"The three models are drawn on page 15."** to the end of the left column's last paragraph.
- Fixed a stray indent on the left column's closing `</div>`.

**Prose cut: none. Claim-ids moved or dropped: none.**

**Why moved.** Same arithmetic, worse. Full measure is 402px of svg plus a 21px caption, a 212px
increase over what was there, against 25px of clearance. The `.cols` measures 274px with column
contents of 265 and 264, so the grid would have to come down to 87px. Even at the 0.85 floor the page
is still 127px over. p14 cannot hold SVG-11 at a legible size under any arrangement.

p14 now carries 245px of trailing clearance.

**Opportunity, not acted on.** `_handback-front-and-paths.md` records `law-lennar-substitution` as a
good fact cut from p14 purely for space and left homeless. p14 now has 245px. Re-homing it is a
content decision, not a layout one, so I did not take it, but the room exists.

### p15. SVG-11 installed at 0.919.

- Inserted `<figure class="fig" style="max-width:6.7in; margin:8pt auto 0">` after the `.cols`, at the
  foot of the page.
- Caption: "From page 14, left to right: less choice and more certainty, toward more choice."
- **Prose cut, two sentences, both carrying no `data-claim`,** from the `.card card-clay` in the right
  column:
  - "Ask the rate and term on every loan in the stack." The card's own heading, "Read the second loan,
    not the headline", already carries that instruction.
  - "Pages 16 and 22." A cross-reference. This is the one genuine loss on the page: the pointer from
    the builder-second-loan trap to the Loan Estimate page and the incentives page is gone.

  **No claim-id was dropped or moved.** Every `fin-*`, `bld-touchstone-*` and `proc-*` id on p15 is
  still there, and `qa-check.py` and `assemble.py` both agree at 364 unique ids document-wide.

**Why 0.919 and not 1.015.** Full measure needs 439px including its top margin. After the two
sentence cuts p15 had 406px. The remaining 33px would have had to come out of either the trailing
`.attr` NOT FOUND enumeration, which is required by the outline's "NOT FOUND to print: register items
2, 3, 4, 5, 6", or the "Read that twice. Only one of the four below is forgiven." lead-in, which is
the sentence that makes the table legible. **I traded 0.096 of scale, 0.56pt of label, for keeping
both.** 5.44pt is comfortably above the 5.1pt floor. If the editor would rather have full measure,
deleting the "Read that twice" line plus about 5px more gets there.

**Same outline deviation as p11:** `guide-outline.md` p15 says "SVG: none. This is a comparison table
plus prose."

### p17. SVG-12 promoted out of the grid column.

- The figure left the right-hand `.cols` column and became a full-measure sibling
  `<figure class="fig" style="max-width:6.8in; margin:8pt auto 0">` **after** the `.cols` and before
  the `card card-agave` CTA. The right column is now just the `card card-clay`, which no longer needs
  its `margin-top:10pt`.
- **`p.hit` "Two HOAs is normal here, not a mistake." was demoted, not deleted.** The sentence is now
  the opening sentence of the paragraph it introduced. It survives verbatim; only the 14.5pt display
  styling is gone. That converted a 45px two-line display block plus 16px of margin into about 19px
  of body copy inside an existing paragraph, worth 42px, which is what made the promotion fit.

**No prose deleted on p17. No claim-id moved or dropped.** All of outline points 1 to 7 stay.

**Why 0.933 and not 1.015.** After the `p.hit` demotion the grid's first row is set by the
`card card-clay`, at 270px, not by the prose column, at 256px. So further prose cuts buy nothing:
the only levers left are the card, whose two paragraphs are the outline's NOT FOUND register items 13
and 51 and cannot be trimmed without losing disclosure, or the furniture below the grid. The furniture
is the primary CTA (#3 of 5) and the `.close` path terminator, "That is the end of your path. Turn to
page 18." Dropping `.close` would have bought exactly the 51px needed for full measure, but p9 and
p13 carry the identical block and it is the only signal a Path C reader gets to rejoin the core, so I
kept it. **The trade is 0.082 of scale, 0.48pt of label, for the path terminator.** Say the word and I
will drop it for full measure.

### Inline `max-width` on p15 and p17, and why that is not the thing the rule forbids

`design-system.md` forbids `style="width:3.3in"` as a way to **shrink** a diagram to fit a crowded
page. Both figures here are `width:100%` of the measure with a `max-width` ceiling that holds them at
0.92 to 0.93, above the 0.85 floor, and the pattern is already the established one on p3 (6.9in),
p5 (6.6in), p21 (6.2in) and p23 (6.2in). No figure I touched uses `narrow`, and none sits in a
`.cols` column.

---

## 4. p28. NOT SOLVED. The 10px shortfall in the brief is off by a factor of forty-five.

**p28 is unchanged.** SVG-10 is still `fig narrow` at 236px, 0.337, 1.99pt.

### The measurement

I built the restructure the brief implies, figure out of the column and spanning the measure, and
measured it. **p28 overran its `.op-body` by 286px with the svg rendering at only 451px**, which
extrapolates to a **453px shortfall at full measure.** Not 10px.

The arithmetic, all measured:

| Item | Height |
|---|---|
| `.op-body` available | **736px** |
| locked headline block, `op-eyebrow` to `op-deck` | 237px |
| gap | 18px |
| `.cols`, three shared rules plus the valleywide median | 238px |
| `card card-agave`, the Summerlin profile | 208px |
| SVG-10 at full measure plus its caption | **478px** |
| **total required** | **1,177px** |

p28 is carrying 1.6 pages of content. The 446px "room for svg" in the brief is the raw distance from
the figure's own top to the foot; it does not subtract the 238px grid the figure shares a page with,
or the 208px Summerlin card below it. That is the same error mode as the p17 "866px below figure top"
note, which was really 77px once siblings were counted.

### Every arrangement I tested, and where it tops out

| Arrangement | Max scale for SVG-10 |
|---|---|
| as shipped, `fig narrow` in a grid column | 0.337 |
| `narrow` removed, still in the grid column | 0.490, still forbidden and still illegible |
| figure spans the measure, everything else stays | 0.03 |
| Summerlin card relocated to p29, rest stays | 0.47 |
| Summerlin card relocated, shared rules run full width | 0.69 |
| headline plus shared rules only, card and median relocated | 0.78 |
| **headline plus figure alone, everything else relocated** | **1.015** |

**Only the last one clears the floor**, and it requires moving 341px of content off p28. Chapter six
has 244px free on p29, 317px on p30 and 288px on p31, so the bytes would fit, but the content will
not: the "three shared rules, printed once" is outline point 1 and has to precede the area pages, and
the Summerlin profile is outline points 3 to 6 and has to be the first area profile. Putting either on
p29 contradicts p29's own title and running head, "Skye Canyon and the northwest, and the southwest".

I also checked whether SVG-10 could simply live somewhere else. At 700x450 it needs 425px at the floor
and 494px at full measure. Nothing in chapter six has it (p29 244, p30 317, p31 288). The only pages in
the guide with that much clearance are p7 (482), p8 (459) and p12 (461), all path-specific pages read
by one reader in three, and none of them about geography.

### The two real fixes, both above a fragment writer

1. **A compact SVG-10 from `build-svg.py`.** The six-area map is authored 700x450, the tallest aspect
   in the set. Re-laid out at roughly 700x260 it would fit p28 beside its existing content at full
   measure with room to spare. I did not touch `build-svg.py` or `build/svg/`, per the brief.
2. **A fifth page for chapter six.** Clean editorially, but it renumbers p29 to p39, the p2 contents,
   every folio, and the cross-references that name pages 28 to 31.

Until one of those happens, p28 ships a diagram whose smallest label prints at 1.99pt, in violation of
`design-system.md`'s own rule. **I left it in place rather than deleting it,** because removing
chapter six's orientation device is an editorial call, the outline requires it, and
`_handback-areas-builders-back.md` records that `area-summerlin.jpg` was already sacrificed to make
room for it. Deleting the diagram would make that sacrifice pointless as well as leaving the chapter
without a map. **Flagging it is the honest move; say the word and I will strip it.**

---

## 5. One more thing that will bite the next person: the diagrams are page-stamped

Every diagram prints its own page number as a `sv-k` eyebrow, generated by `build-svg.py`:

```
svg-01 "Page 5"   svg-04 "Pages 19 and 20"   svg-10 "Page 28"   svg-13 "Page 10"
```

So **moving a diagram between pages leaves a stale page number printed inside it.** SVG-13 now sits on
p11 and prints "Page 10"; SVG-11 sits on p15 and prints "Page 14".

I could not fix it without editing `build/svg/`, which the brief forbids, so I made the captions agree
with the stamp instead of contradicting it: p11 reads "From page 10." and p15 reads "From page 14.",
which frames both as a deliberate carry-over from the opener whose argument they illustrate. It reads
as intentional rather than wrong, and the p10 and p14 pointer sentences close the loop from the other
side.

**The clean fix is two string literals in `build-svg.py`** plus `python3 build-svg.py 11 13`:

| Line | Now | Should be |
|---|---|---|
| ~982 | `heading(0, 14, "Page 10", "The two clocks of a move-up")` | `"Page 11"` |
| ~913 | `heading(0, 14, "Page 14", '"Included" means three ...')` | `"Page 15"` |

That regenerates two reviewed SVGs, so it needs a re-run of `_contact.html` and `_gray.html`. Once
done, the "From page 10." and "From page 14." prefixes can come off both captions and
`build/svg/index.md`'s page column needs updating for SVG-11 and SVG-13.

---

## 6. Diagrams still under the 0.85 floor after this pass, none of them mine

Reported so the next pass has an input. All four are close to the floor rather than illegible.

| Page | Diagram | Scale | Label | Clearance on the page |
|---|---|---|---|---|
| p18 | SVG-03 | 0.823 | 4.87pt | 63px |
| p22 | SVG-06 | 0.837 | 4.95pt | 147px |
| p24 | SVG-08 | 0.837 | 4.95pt | 110px |
| p26 | SVG-09 | 0.837 | 4.95pt | 36px |

p22 and p24 have enough clearance to go to full measure by relaxing their inline `max-width:6.1in`
alone, with no copy change at all. p18 and p26 do not.
