# Direction 5, Quiet Editorial. Rationale

**Thesis: calm, expensive, unhurried, so the guide reads as a document rather than an offer.**

A cold Facebook reader who has driven past a model home arrives suspicious. Everything else they have seen about new construction was paid for by someone who wants the sale. So the persuasion is tonal: wide margins, one generous 62 character measure, almost no rules, numbers set as large standalone stat blocks. Someone laying out a page this slowly is not in a hurry to close you.

That is why page 20 is one paragraph, one very large callout, and a lot of paper. The fastest way to make a refusal read as generosity rather than a hole is to give it a whole page. Crammed under a table it would have looked like an apology.

## Who it persuades, who it loses

It wins the cash buyer, the out of state relocator with equity, and the analytical move up buyer who already assumes the internet is lying to them. They take restraint as proof.

It loses the impatient scanner. There is no colour coded urgency and nothing to skim in eight seconds. A first time buyer who is anxious rather than skeptical may read the air as coolness. That is the real cost. The only mitigation is the copy, already warm and second person, plus the clay accent, the one human colour on the page. If Ryan's lead mix skews first time and anxious, this is the wrong pick and tuning will not fix it.

## Ink and toner

Measured from the rasterised print PDF. Interior pages average **4.07 percent ink density**, under the 5 percent toner yield ratings assume. The cover, with its atmospheric field, is **37.65 percent**.

The default build keeps the atmosphere, because the PDF is mostly read on screen and it is what the lead receives. A documented `class="ink-lean"` build renders every field as a light wash and drops the cover to **5.16 percent**. Over 39 pages with six openers, the lean build averages 4.2 percent, roughly **33 standard coverage pages of toner, or 20 duplex sheets**. The rich build averages 9.2 percent, roughly **72 standard pages**, almost all of the difference in six sheets. Offering the lean PDF as the printer friendly download is the entire fix.

## Grayscale survival

Nothing breaks, and that is not luck. Every pair was computed from relative luminance, exactly what grayscale preserves, so all 38 ratios in `tokens.md` are unchanged in black and white. The lowest is 5.73:1.

One weakness was found and designed out. The aside tint `#F0EEE8` and the NOT FOUND sand `#F2EAE0` sit **three gray levels apart** and would have collapsed together on a home printer. The aside was stripped of its fill and now carries rules only, leaving the sand to mean exactly one thing across all 39 pages: a number we refused to invent. The 2pt clay rule reads as gray 98 against the aside's 1.25pt ink rule at gray 34, so the two stay apart by rule value too.

## The hero on a phone

At 1280 the hero is two columns, atmospheric field on the right, the three value prop numerals just breaking the fold. At 375 it stacks: masthead, eyebrow, headline at 31 to 40px, subhead, then a full width button and its microcopy, all above the fold at 812px. The field drops to a 168px band below the trust line. No horizontal scroll at any width.

## Three path wayfinding

Every page carries a 2.45in apparatus column on the **outer** edge, so an edge tab on pages 6 to 17 bleeds off the trim without colliding with text and the 5mm safety is free. The three tabs separate by **value, not hue**: ink at gray 34, muted at gray 90, rule-strong at gray 135, which survives a black and white print where three hues at one value would not. The running head is a single outer aligned line, so swapping in `Path A · Moving here from out of state` is a text change, and the folio takes the path letter as `6 · A`.

## What did not fit, named

The spread copy is about **1,378 set words** plus a twenty row table, against page-budget.md's **660 word two page allowance**. At 10.5pt over 1.55 with 0.75in margins, in one full width column with zero air between blocks, the floor is **3.1 pages for any direction**. Quiet Editorial sets it in **five**: 19 through 23. Nothing was cut, paraphrased or reordered; the copy runs in strict document order.

Two fixes. The nineteen entry source strip with full URLs is irreducibly about 5.3in tall and needs its own page here; moving the per page strips to one back of book register returns this section to four pages and four to five pages across the guide. And SVG-04 runs 4.54in, 48 percent of the text column against the 45 percent spec; cutting it to 30 percent returns another 1.7in.
