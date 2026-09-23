# Direction 2: Broadsheet, Rationale

**Thesis: this is reporting on builders, not marketing from a realtor.**

## Why this serves a skeptical buyer

The reader has already driven past a model home and been handed something glossy. Every persuasion signal a realtor reaches for is one they have learned to discount. So this direction removes them all and substitutes what a brochure cannot fake: visible apparatus. Kickers over rules, a dateline in the running head, a verification stamp on the tail of all nineteen citations, a table caption ending in a date. The reader does not have to trust Ryan. They can check him.

That is why the NOT FOUND callout is the largest object on page 19 and the only place the spot colour is spent at scale. A brochure buries the gap. A reversed register stamp, a 5px oxblood rule, and a display-italic head reading "I am not going to hand you a number" turn the absence into the strongest evidence on the spread. One hundred and fourteen honest NOT FOUND cells stop being a weakness the moment the design treats them as the product.

## Who it persuades, who it loses

It persuades the analytical buyer, the engineer relocating from California, the second-time buyer who has been burned. It loses the browser. No photography carries the emotional case, no lifestyle, no warmth beyond the writing. Anyone who wants to feel excited about a house will find it austere. Likely the least likable of the six and the most believable.

## Ink coverage

About **8 to 10 percent** of page area on interior pages: 7 percent type, 1.4 percent source-strip agate, under 2 percent tints and rules. The cover runs about **11 percent** because of the photo well. No heavy dark fills: the NOT FOUND panel is a 4 percent wash, the table header band a 10 percent tint, and the only reversed elements are three stamps plus the CTA, which never prints.

A mono cartridge is rated at 5 percent coverage. At roughly 9 percent, a 39-page duplex print consumes about **70 rated pages of toner, near 4 percent of a 1,500 to 2,000 page cartridge**. Cheap, and a direct consequence of building structure from rule weight instead of fill.

## Grayscale survival

The three path tabs convert to greyscale bytes 23, 65 and 229. Each is also backed by the folio letter and the running head, so a tab that fails to print costs nothing.

**What breaks:** the spot `#7A2019` converts to `#414141` and the secondary ink `#333A40` to `#393939`. Eight grey levels apart, so the oxblood stops reading as a distinct ink. Survivable only because the spot never carries meaning alone: NOT FOUND cells print the words in tracked caps with an underline, kickers sit above a rule, footnote figures are superior and bracketed. Nothing becomes ambiguous, but the page loses its one note of warmth. That is the cost of a one-spot system.

## Mobile hero

At 375px, CSS `order` puts headline, subhead, button and trust line **above the fold**, value props below. The lead photo well is hidden because it would push the ask down a screen. No horizontal overflow. The button goes full width; the `Real Broker, LLC` plate and `[NOT FOUND]` slot survive at full size.

## Three-path wayfinding

Value first, then three redundancies: a bleeding edge tab stepped to one of three bands, a folio carrying the path letter, a running head naming the path. On screen the tab becomes a text label that is never print-only.

## What did not fit

1. **The spread overruns badly.** Page 19 carries about 500 set words against a 320 word budget; page 20 about 530 plus a 20 row table. Measured in the browser, the copy needs roughly **1.5 Letter pages per leaf** at 10.5pt. It fits only at **9.8pt body.** Fix: split into pages 19, 20 and 21, or cut about 250 words.
2. **The source strip is set at 4.7pt, not 7pt.** Nineteen full-path entries at 7pt need 1.9in on a page with 0.9in to give.
3. **URLs print without `https://` or `www.`,** full path retained.
4. **The diagram gets about 13 percent of the page 19 column height, not the specified 45 percent.** It is a figure band at the foot, not a tall column object.
5. **The 20 row table is doubled up** as two 10 row tables side by side, each with its own `thead` and caption, at 6.5pt. One full-width run needed 100px more.
6. **The standing note** beginning "No per-home or per-community annual dollar amount appears in this spread" reads like a note to directors, not reader copy. I set it visibly rather than drop it.
7. **Pagination conflict.** `page-budget.md` makes odd pages right-hand, so 19 and 20 are not a physical spread. I rendered 19 left, 20 right per the brief.
