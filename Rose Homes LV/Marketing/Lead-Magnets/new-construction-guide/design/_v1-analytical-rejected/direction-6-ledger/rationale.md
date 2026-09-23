# Direction 6 · Ledger · Rationale

**Thesis: new construction is a series of line items, and this guide prices every one.**

Every page is a general ledger row. Reference numerals in a rail on the left, the plain English description in the middle, the amount in a tinted column on the right, on both verso and recto, never mirrored. A brought forward total sits at the head of each page and a carried forward total is bottom anchored to the foot of the figures rail, so the reader watches the real cost of a new home assemble itself across the core chapters.

## Why this serves a scared, skeptical buyer

A person who has just walked out of a model home is not confused about feelings. They are confused about money, and they suspect they were shown a number that is not the number. A ledger answers that suspicion with form rather than reassurance. It says: here is every line, here is what each one costs, here is the running total, and here is the audit trail underneath. Nothing is asserted without a reference numeral pointing at a URL and a verification date.

The honesty problem is the whole design. Because 114 cells in this guide are NOT FOUND, the unknown has to be a first class amount, not a hole. So the figures column posts it as a line item with its own treatment: a hatched ground, a hairline border, and the literal words. The carried forward total is deliberately two numbers, priced items and unpriced items, and the dollar total on page 20 reads `NOT FOUND`. A ledger whose bottom line is an honest unknown is a stronger conversion object than a ledger full of invented figures, because it proves the guide will not lie to you about the things it does know.

## Who it persuades, who it loses

It persuades anyone who has ever read a closing disclosure, a 401k statement, or a P&L. Cash buyers, move up owners, and engineers respond to it immediately. It also persuades the person who was quoted a monthly payment at the sales desk and wants to check the arithmetic.

It loses the browser. Somebody who wants to feel excited about a new house will find this cold. There are no photographs, no lifestyle, no warmth in the layout, only in the writing. If the guide's job were aspiration, this is the wrong direction. Its job is to be believed.

## Print ink

Measured directly off the rendered pages, not estimated: **cover 7.79 percent, page 19 8.36 percent, page 20 7.90 percent mean ink coverage.** Weighted across 39 pages that is **8.12 percent**. Only 4.7 to 5.6 percent of pixels sit below 50 percent reflectance, so there is almost no solid black. The heaviest fills in the system are three small reversed bands per page and the 7 percent ledger tint on a 210px rail.

Against the ISO 5 percent coverage reference, this runs about 1.6 times the rated rate. A 3,000 page mono cartridge yields roughly 1,850 pages at this density, so **one 39 page copy costs about 2 percent of a cartridge, on 20 duplex sheets.** That is cheap for a print first guide, and it is cheap on purpose: the tint is a rail, not a background.

## Grayscale

It survives, and I tested it rather than asserting it. The full grayscale render is legible end to end. Two collisions exist and both are designed around. `--ledger` at 92.7 percent gray and `--unknown` at 92.3 percent are indistinguishable in black and white, which is exactly why every unknown carries a hatch, a border, and the words. `--debit` rust at 37.2 percent and `--muted` at 36.5 percent are also identical in gray.

What actually breaks: the marginal reference numerals lose their rust and read as ordinary gray numerals. Meaning survives because they sit in a dedicated 34px rail that holds nothing else. Retired districts keep their 2px credit rule under `Matured` and `Paid off June 1, 2025`, which reads as an underline in gray and stays distinct from a plain date. Nothing in the system is encoded by hue alone.

## Mobile hero

DOM order is already mobile order: headline, subhead, button, microcopy, statement card, trust line. At 900px the statement card drops below the button, the page reference moves out of the amount column onto its own line under each prop, and the cover thumbnail placeholder is removed. At 375px the button sits about 420px down the document, well above the fold, and the layout produces zero horizontal overflow. The three value props keep their `01 / 02 / 03` line numbers, so the statement reading survives the loss of the column.

## Three path wayfinding

The system already has the two slots this needs. The running head carries the path label on pages 6 to 17 in the same mono caps used for `SID and LID` here. The figures rail carries the folio letter and, critically, **three parallel running totals**: a Path A reader, a Path B reader, and a Path C reader each see a different carried forward figure arriving at page 18, and page 18 reconciles them. That is a wayfinding device no other structure gets for free. Edge tabs use the value ladder, not hue: `--ink` 9.6 percent, `--muted` 36.5 percent, `--rule-strong` 57.7 percent gray, three clearly separated values.

## What did not fit, named

The spread as written is **1,091 set words plus a 510 word source strip.** At the specified 10.5pt over 1.52, these two Letter pages hold **612 of those 1,091 words plus all 510 audit trail words.** The remaining **479 words are overset** and are rendered below the spread in the same system rather than cut: numbered list items 4 and 5, the prepayment paragraph, the entire NOT FOUND disclosure, figure SVG-04, the Cadence and Wellston Ridge paragraph, the four step checklist, and the soft close. The copy is **1.78 times** what two pages hold here.

Note the budget conflict too: `page-budget.md` allocates 320 words to page 19 and 340 to page 20, a 660 word spread, while `design-sample-content.md` states 900 against a budget of 840. The actual sample copy is 1,601 words including the strip. **The SID and LID section needs four Letter pages, not two.** The cheapest fix is already on the architect's own cut list: page 35 can shed its third party record column and free a full page.

**The cost of this direction, stated plainly.** The figures rail needs row labels, and those labels are new text, about 90 words per spread. Every figure in them is drawn from facts already in the body, and not one word of the supplied copy was changed, trimmed, or reordered. But if Ryan does not want any new text in the guide, this direction cannot exist. That is the trade.
