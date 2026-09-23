# Direction 4, Spec Sheet, rationale

**Thesis: a house is a spec, so the guide reads like the spec.**

A scared, skeptical buyer has just left a model home where every surface was staged and every number was verbal. The counter to staging is not warmth, it is documentation. So this direction hands the reader construction documents: drawing border, coordinate margin, numbered details, callout leaders into the diagram, hairline rules, and a title block in every footer carrying sheet number, revision, and verified-as-of date. Somebody wrote this down and dated it.

The move that earns the direction is the **HOLD block**. On a drawing, a HOLD tag means an item is known, tracked, and deliberately unresolved. So the NOT FOUND callout is not a gap, it is a drafting convention doing its job: redline border, hatch band, tag reading `HOLD · NOT FOUND REGISTER · ITEM 14`. It scales down to the five NOT FOUND cells in the schedule: triangle glyph, dotted underline, literal words. A reader handed six confident numbers by a builder now sees the one document saying which numbers do not exist. That reads as generosity because it is registered, not apologised for.

**Persuades:** engineers, contractors, repeat buyers, cash buyers, and Path B move-up buyers who already suspect they are being handled. The schedule is their hero object. **Loses:** an intimidated first-time buyer may find a drawing sheet cold, so Path C is the weakest fit. The fix is the DETAIL box, a friendly aside in a numbered blue frame, a note from whoever drew the sheet.

## Print ink

Roughly **5 to 6 percent coverage on an interior sheet, 3.5 percent on the cover**, estimated from area. Pure white stock, no full bleed panels, no dark headers, no photography, no gradients. Ink is type, hairlines, three light tints, a few small solid tags. That is the industry standard 5 percent test page, so 39 duplex pages cost about **43 rated pages of toner**: roughly 34 copies from a 1,500 page cartridge, or **$1.10 to $1.70 per copy**. Both accents are thin rules and short strings, never fills, so a color inkjet adds little.

## Grayscale survival

Computed: `--redline #B22A15` renders at 8 bit gray 94, `--dim #14607A` at gray 89. **In black and white the two accents are the same gray.** So the system never carries meaning in hue. HOLD is a 2.5px border plus a hatch band plus the word HOLD. DETAIL is a 1px border plus a flat tint plus the word DETAIL. NOT FOUND is a triangle plus a dotted underline plus the words. Nothing collapses. The three path tabs are separated by value, gray 21, 101, and 242, which no home printer can merge.

## Mobile hero

Argument left, three value props as a numbered schedule right. Below 1024px they stack: headline, button, schedule, trust block. Below 480px the button goes full width. The 375px frame shows the production sticky action bar, `position: fixed` on the live page, legal there and forbidden in the guide. The schedule survives reflow because it was never a grid, only numbered rows.

## Three path wayfinding

The title block does work no other direction gets free. Every footer is already a labelled cell grid, so pages 6 to 17 add one cell, `PATH`, reading `A · MOVING HERE`, and the sheet cell becomes `07 · A`. The running head repeats it. Edge tabs bleed at three vertical positions in three values. Four redundant signals per path page, for one grid column.

## What did not fit, named

Nothing was cut, every word renders, and holding two Letter pages cost typographic spec. Measured price of restoring it, at sources 7pt over 1.35, prose 10.5pt over 1.55, structured 9pt, schedule 7pt:

- **Sheet 19 runs 2.64 inches long. Sheet 20 runs 1.57 inches long.**
- Total **4.2 inches of column, about 22 percent over the spread.**
- The source strip alone accounts for 1.81 inches of that.

To land it: prose 9.7pt over 1.35, structured 8.25pt, schedule 6.5pt, notes 5.3pt over 1.26. **The 5.3pt notes strip is the honest weak point.** Reference material, not reading material, and it still computes 5.87:1, but it is small.

Three more deviations:

1. **SVG-04 renders at about 20 percent of the page 19 column height, not 45 percent.** Full size costs an inch.
2. **The 19 entry strip is split, 01 to 10 on sheet 19, 11 to 19 on sheet 20**, cross referenced in each header. Every marker resolves on its own sheet, which `page-budget.md` requires, so this is a correction, not a compromise.
3. **The sample sets page 19 on the left, `page-budget.md` makes odd pages recto.** I followed the sample. Flag before build.

**Recommendation: give this section three sheets, 19, 20, and 20A.** One extra sheet buys back 7pt sources, 10.5pt prose, and the full size diagram, and this direction absorbs a continuation sheet without looking padded. Continuation sheets are what drawing sets do.
