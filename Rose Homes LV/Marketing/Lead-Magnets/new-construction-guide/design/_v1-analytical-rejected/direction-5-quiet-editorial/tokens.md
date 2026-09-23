# Direction 5, Quiet Editorial. Design tokens

**Thesis:** calm, expensive, unhurried. The opposite of a sales flyer.
**Deliberately off brand.** No Rose Homes LV navy, champagne gold, or warm off-white. No Playfair Display, no Montserrat, no Bebas Neue.
**Em-dashes in this file: zero.**

---

## 1. Colour

Every value below appears in `preview.html` as a CSS custom property.

| token | hex | role |
|---|---|---|
| `--paper` | `#FCFBF9` | page stock. A cool white, deliberately a different temperature from the Rose Homes off-white |
| `--paper-tint` | `#F0EEE8` | one step up from paper. Diagram layer blocks only |
| `--sand` | `#F2EAE0` | **reserved system-wide for one meaning: a number we refused to invent.** The NOT FOUND callout and nothing else |
| `--print-wash` | `#EDEAE3` | the ink-lean substitute for an atmospheric field |
| `--ink` | `#1D2321` | primary text. A deep graphite green, not a navy and not a black |
| `--ink-2` | `#3D4642` | secondary text. Decks, table data cells, hero subhead |
| `--muted` | `#545C58` | apparatus. Running heads, folios, source register, table column heads, captions |
| `--caption-field` | `#EDEAE3` | caption text set over an atmospheric field |
| `--clay` | `#9C4A2C` | the single accent. List markers, prop numerals, the button, the one heavy rule |
| `--clay-deep` | `#7E3A20` | accent at small sizes and on hover, where `--clay` needs more weight |
| `--rule` | `#C9C7BE` | hairline separators. Decorative only |
| `--rule-strong` | `#86887F` | meaningful graphics. Checkbox borders, the diagram's dashed escrow boundary |
| `--field-1` | `#232B28` | atmospheric field, darkest stop |
| `--field-2` | `#38423B` | atmospheric field |
| `--field-3` | `#55503F` | atmospheric field, turning warm |
| `--field-4` | `#6A5E4E` | atmospheric field, warmest stop |

### Why this palette

Cold Facebook traffic reading about a hidden thirty year bill needs to believe the writer is not selling. Saturated conversion colour reads as a pitch, so the accent is a **single desert clay**, used four times per page at most, against a **graphite green ink** that is warm enough to feel like a book and cold enough to feel like a document. The field stops move from a pre dawn green black to a low warm horizon, which is what a Las Vegas construction site actually looks like at 6 a.m., and it gives the openers a mood no stock brand palette would.

The clay is doing conversion work. It is the only warm thing on a page of near neutrals, so the eye finds the list markers, the source numerals, and the button without any of them being loud.

### One structural colour rule

`--sand` is never decorative. It marks a NOT FOUND callout and nothing else, across all 39 pages. A reader who meets it on page 19 recognises it on page 33 without being told. The aside callout that used to share a tint was moved to **rules only, no fill**, because in grayscale `--paper-tint` and `--sand` are three gray levels apart and would have collapsed into each other.

---

## 2. Computed WCAG contrast table

Ratios computed from relative luminance with `python3`, not asserted. AA thresholds: 4.5:1 normal text, 3:1 for large text at 18.66px bold or 24px regular and above.

**Because WCAG contrast is a pure luminance ratio, every number below is identical in grayscale.** Converting this document to black and white changes no value in this table.

| fg | bg | used for | size | weight | AA needs | ratio | result |
|---|---|---|---|---|---|---|---|
| `#1D2321` | `#FCFBF9` | Cover title | 42pt / 56px | 300 | 3.0:1 | **15.45:1** | PASS |
| `#1D2321` | `#FCFBF9` | Page headline | 27pt / 36px | 300 | 3.0:1 | **15.45:1** | PASS |
| `#1D2321` | `#FCFBF9` | Body prose | 10.5pt / 14px | 400 | 4.5:1 | **15.45:1** | PASS |
| `#1D2321` | `#FCFBF9` | Subhead | 14.5pt / 19.3px | 500 | 4.5:1 | **15.45:1** | PASS |
| `#1D2321` | `#FCFBF9` | List and checklist item text | 10.5pt / 14px | 400 | 4.5:1 | **15.45:1** | PASS |
| `#1D2321` | `#FCFBF9` | Table row header, district number | 8.5pt / 11.3px | 600 | 4.5:1 | **15.45:1** | PASS |
| `#1D2321` | `#FCFBF9` | Phone number stat block | 20pt / 26.7px | 300 | 3.0:1 | **15.45:1** | PASS |
| `#1D2321` | `#FCFBF9` | Brokerage slot, cover | 9.5pt / 12.7px | 600 | 4.5:1 | **15.45:1** | PASS |
| `#1D2321` | `#FCFBF9` | Hero h1 | 50px | 300 | 3.0:1 | **15.45:1** | PASS |
| `#1D2321` | `#FCFBF9` | Value prop title | 18.5px | 500 | 4.5:1 | **15.45:1** | PASS |
| `#1D2321` | `#FCFBF9` | Brokerage slot, hero trust line | 12.5px | 600 | 4.5:1 | **15.45:1** | PASS |
| `#3D4642` | `#FCFBF9` | Deck, cover subtitle | 12.5pt / 16.7px | 300 italic | 4.5:1 | **9.43:1** | PASS |
| `#3D4642` | `#FCFBF9` | Table data cells | 8.5pt / 11.3px | 400 | 4.5:1 | **9.43:1** | PASS |
| `#3D4642` | `#FCFBF9` | Hero subhead | 18px | 300 | 4.5:1 | **9.43:1** | PASS |
| `#3D4642` | `#FCFBF9` | Value prop body | 15.5px | 400 | 4.5:1 | **9.43:1** | PASS |
| `#3D4642` | `#FCFBF9` | License slot `[NOT FOUND]` | 7.5pt / 10px | 600 | 4.5:1 | **9.43:1** | PASS |
| `#545C58` | `#FCFBF9` | Running head | 7pt / 9.3px | 500 | 4.5:1 | **6.66:1** | PASS |
| `#545C58` | `#FCFBF9` | Source register entry text | 7pt / 9.3px | 400 | 4.5:1 | **6.66:1** | PASS |
| `#545C58` | `#FCFBF9` | Table column headers | 6.6pt / 8.8px | 600 | 4.5:1 | **6.66:1** | PASS |
| `#545C58` | `#FCFBF9` | NOT FOUND cells inside the table | 6.6pt / 8.8px | 600 | 4.5:1 | **6.66:1** | PASS |
| `#545C58` | `#FCFBF9` | Folio | 9.5pt / 12.7px | 400 | 4.5:1 | **6.66:1** | PASS |
| `#545C58` | `#FCFBF9` | Edition and compliance block | 7.5pt / 10px | 400 | 4.5:1 | **6.66:1** | PASS |
| `#545C58` | `#FCFBF9` | Diagram tags and term labels | 6 to 6.5pt / 8 to 8.7px | 400 to 600 | 4.5:1 | **6.66:1** | PASS |
| `#545C58` | `#FCFBF9` | Hero microcopy and trust line | 13px | 400 | 4.5:1 | **6.66:1** | PASS |
| `#9C4A2C` | `#FCFBF9` | Numbered list markers | 18pt / 24px | 200 | 3.0:1 | **5.92:1** | PASS |
| `#9C4A2C` | `#FCFBF9` | Value prop index numerals | 38px | 200 | 3.0:1 | **5.92:1** | PASS |
| `#7E3A20` | `#FCFBF9` | Cover eyebrow, hero eyebrow | 8.5pt / 11.3px | 500 to 600 | 4.5:1 | **8.08:1** | PASS |
| `#7E3A20` | `#FCFBF9` | Source register numerals | 7pt / 9.3px | 600 | 4.5:1 | **8.08:1** | PASS |
| `#7E3A20` | `#FCFBF9` | Superscript source refs | 6.2pt / 8.3px | 600 | 4.5:1 | **8.08:1** | PASS |
| `#7E3A20` | `#FCFBF9` | Diagram label SVG-04 | 7pt / 9.3px | 600 | 4.5:1 | **8.08:1** | PASS |
| `#1D2321` | `#F2EAE0` | NOT FOUND callout headline | 26pt / 34.7px | 300 italic | 3.0:1 | **13.40:1** | PASS |
| `#1D2321` | `#F2EAE0` | NOT FOUND callout body | 10pt / 13.3px | 400 | 4.5:1 | **13.40:1** | PASS |
| `#7E3A20` | `#F2EAE0` | NOT FOUND register line | 7pt / 9.3px | 600 | 4.5:1 | **7.01:1** | PASS |
| `#1D2321` | `#F0EEE8` | Diagram layer labels | 7pt / 9.3px | 400 | 4.5:1 | **13.77:1** | PASS |
| `#FCFBF9` | `#9C4A2C` | Button label, rest state | 15px | 600 | 4.5:1 | **5.92:1** | PASS |
| `#FCFBF9` | `#7E3A20` | Button label, hover state | 15px | 600 | 4.5:1 | **8.08:1** | PASS |
| `#1D2321` | `#EDEAE3` | Body over an ink-lean wash | 10.5pt / 14px | 400 | 4.5:1 | **13.30:1** | PASS |
| `#545C58` | `#EDEAE3` | Field caption, ink-lean build | 7.5pt / 10px | 400 | 4.5:1 | **5.73:1** | PASS |

**Lowest text ratio anywhere in the system: 5.73:1.** Nothing sits close to the 4.5 line.

### Captions over a gradient, measured from rendered pixels

A gradient has no single background hex, so these two were measured by rasterising the page with the caption hidden and taking the worst pixel inside the caption's exact bounding box.

| fg | worst background pixel | used for | size | AA needs | ratio | result |
|---|---|---|---|---|---|---|
| `#EDEAE3` | `#333125` | Cover field caption | 7.5pt / 10px | 4.5:1 | **10.88:1** | PASS |
| `#EDEAE3` | `#474131` | Hero field caption | 11px | 4.5:1 | **8.45:1** | PASS |

Both numbers depend on the **caption scrim**, a `linear-gradient(to top, rgba(8,12,10,.82) 0%, rgba(8,12,10,.68) 20%, rgba(8,12,10,0) 42%)` laid over the field. Without it the cover caption measured 4.17:1 and failed. Any real photograph dropped into these fields needs the same scrim, so it is part of the field component, not a patch.

### Non-text contrast, WCAG 1.4.11

| fg | bg | used for | needs | ratio | result |
|---|---|---|---|---|---|
| `#86887F` | `#FCFBF9` | Checklist checkbox border, a real control affordance | 3:1 | **3.48:1** | PASS |
| `#86887F` | `#FCFBF9` | Diagram dashed escrow boundary and layer stems | 3:1 | **3.48:1** | PASS |
| `#9C4A2C` | `#F2EAE0` | The 2pt clay rule that signals a NOT FOUND callout | 3:1 | **5.14:1** | PASS |

`#C9C7BE` hairlines measure 1.64:1 on paper. They are **purely decorative separators**, exempt from 1.4.11: every table cell is a real `<td>` or `<th scope>`, and no hairline carries meaning that is not also in the text.

### Grayscale separation of the fills

| pair | 8 bit gray delta | how they stay apart in black and white |
|---|---|---|
| paper `#FCFBF9` vs sand `#F2EAE0` | 16 | visible as a tone |
| paper vs paper-tint `#F0EEE8` | 13 | visible as a tone |
| **paper-tint vs sand** | **3** | **not separable by fill.** This is why the aside carries no fill at all and the sand is reserved for one meaning |
| clay `#9C4A2C` (gray 98) vs ink `#1D2321` (gray 34) | 64 | the 2pt clay rule reads as a clearly lighter rule than the 1.25pt ink rule |

---

## 3. Type

### Families

| role | family | why |
|---|---|---|
| Display and body | **Newsreader** | a text serif with a real optical size axis, drawn for reading rather than for headlines. At 10.5pt it sets warm and even; at 42pt the light weight goes thin and expensive without becoming a fashion serif. It is not Playfair, which is a display face pretending to be a text face |
| Data, apparatus, labels | **Instrument Sans** | a slightly humanist grotesque that holds up at 6.6pt in table headers and 7pt in the source register, where Montserrat's wide geometric forms would fall apart. It is quiet next to a serif instead of competing with it |

Serif carries every word a reader actually reads. Sans is confined to things a reader looks up: table cells, running heads, folios, source URLs, phone labels, the button. That division is the whole typographic idea.

### Exact Google Fonts URL

```
https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..700&family=Newsreader:ital,opsz,wght@0,6..72,200..600;1,6..72,200..600&display=swap
```

Weights loaded: Newsreader variable 200 to 600 with italics and optical sizes 6 to 72. Instrument Sans variable 400 to 700 with italics. Optical sizing is left on `auto`, which is why the 7pt source register and the 42pt cover title are the same family without looking like the same font.

Fallbacks: `Newsreader, Georgia, "Times New Roman", serif` and `Instrument Sans, "Helvetica Neue", Arial, sans-serif`.

### Type scale, print pages

| element | size | line height | tracking | family and weight |
|---|---|---|---|---|
| Cover title | 42pt | 1.04 | -0.021em | Newsreader 300 |
| Cover eyebrow | 8.5pt | 1.2 | 0.22em, uppercase | Instrument Sans 500 |
| Cover subtitle | 12.5pt | 1.5 | 0 | Newsreader 300 |
| Geography line | 8.5pt | 1.4 | 0.17em, uppercase | Instrument Sans 500 |
| Credibility line | 10pt | 1.5 | 0 | Newsreader 400 italic |
| Byline name | 15pt | 1.2 | 0 | Newsreader 400 |
| **Brokerage slot** | 9.5pt | 1.3 | 0.155em, uppercase | Instrument Sans 600 |
| Edition block | 7.5pt | 1.8 | 0 | Instrument Sans 400 |
| Compliance line | 7.5pt | 1.8 | 0 | Instrument Sans 400 |
| Running head | 7pt | 1 | 0.185em, uppercase | Instrument Sans 500 |
| Folio | 9.5pt | 1 | 0 | Newsreader 400 |
| Page headline | 27pt | 1.06 | -0.018em | Newsreader 300 |
| Deck | 12.5pt | 1.42 | 0 | Newsreader 300 italic |
| **Body prose** | **10.5pt** | **1.55** | 0 | Newsreader 400 |
| Subhead | 14.5pt | 1.2 | -0.008em | Newsreader 500 |
| Numbered list marker | 18pt | 1 | 0, tabular | Newsreader 200 |
| Aside label | 7pt | 1.2 | 0.2em, uppercase | Instrument Sans 600 |
| Aside body | 9.5pt | 1.48 | 0 | Newsreader 400 |
| NOT FOUND headline | 26pt | 1.12 | -0.016em | Newsreader 300 italic |
| NOT FOUND body | 10pt | 1.52 | 0 | Newsreader 400 |
| NOT FOUND register line | 7pt | 1.3 | 0.18em, uppercase | Instrument Sans 600 |
| Table column head | 6.6pt | 1.2 | 0.15em, uppercase | Instrument Sans 600 |
| Table row head | 8.5pt | 1.25 | 0, tabular | Instrument Sans 600 |
| Table data cell | 8.5pt | 1.25 | 0, tabular | Instrument Sans 400 |
| NOT FOUND table cell | 6.6pt | 1.2 | 0.14em, uppercase | Instrument Sans 600 |
| Checklist item | 10.5pt | 1.5 | 0 | Newsreader 400, step name 600 |
| Phone label | 7pt | 1.2 | 0.2em, uppercase | Instrument Sans 600 |
| Phone who | 9pt | 1.42 | 0 | Newsreader 400, org name 600 |
| **Phone number stat** | 20pt | 1 | -0.012em, tabular | Newsreader 300 |
| Soft close | 10.5pt | 1.5 | 0 | Newsreader 400, second line italic |
| **Source register entry** | **7pt** | **1.3** | 0 | Instrument Sans 400 |
| Source register numeral | 7pt | 1.3 | 0, tabular | Instrument Sans 600 |
| Superscript source ref | 6.2pt | 0 | 0 | Instrument Sans 600 |
| Diagram label | 7pt | 1.2 | 0.2em, uppercase | Instrument Sans 600 |
| Diagram layer | 7pt | 1.25 | 0 | Instrument Sans 400 |
| Field caption | 7.5pt | 1.5 | 0.09em | Instrument Sans 400 |

### Type scale, landing hero

| element | size | line height | tracking | family and weight |
|---|---|---|---|---|
| Masthead | 12px | 1.3 | 0.19em, uppercase | Instrument Sans 600 |
| Eyebrow | 11.5px | 1.3 | 0.22em, uppercase | Instrument Sans 600 |
| H1 | `clamp(34px, 3.95vw, 50px)` | 1.06 | -0.022em | Newsreader 300 |
| Subhead | 18px | 1.6 | 0 | Newsreader 300 |
| Button | 15px | 1 | 0.075em, uppercase | Instrument Sans 600 |
| Microcopy | 13px | 1.6 | 0 | Instrument Sans 400 |
| Trust line | 13px | 1.85 | 0 | Instrument Sans 400 |
| Trust brokerage slot | 12.5px | 1.85 | 0.09em, uppercase | Instrument Sans 600 |
| Value prop index | 38px | 1 | 0, tabular | Newsreader 200 |
| Value prop title | 18.5px | 1.3 | -0.012em | Newsreader 500 |
| Value prop body | 15.5px | 1.6 | 0 | Newsreader 400 |
| Field caption | 11px | 1.55 | 0.08em | Instrument Sans 400 |

---

## 4. Space, rules, radii

### Spacing scale, 3pt base

`--s1 3pt` · `--s2 6pt` · `--s3 9pt` · `--s4 12pt` · `--s5 18pt` · `--s6 24pt` · `--s7 36pt` · `--s8 48pt` · `--s9 72pt`

Nothing in the guide uses a value outside this scale.

### Page geometry

| token | value |
|---|---|
| trim | 8.5in x 11in |
| margin top | 0.80in |
| margin bottom | 0.72in |
| margin outer | 0.75in |
| margin inner | 0.75in |
| text width | 7.00in |
| text height | 9.48in |
| **main measure** | **4.20in, about 62 characters at 10.5pt Newsreader** |
| gutter | 0.35in |
| outer margin column | 2.45in |

The main measure sits **toward the spine** and the 2.45in apparatus column sits **on the outer edge**, mirrored across the gutter. On a facing spread the two reading columns meet in the middle, which is what carries a reader across the gutter, and every callout, diagram, phone block and note lives out at the trim where it can be ignored.

### Rules

| use | weight | colour |
|---|---|---|
| hairline separators, running head, table rows, source register top | 0.5pt | `--rule` |
| aside callout top | 1.25pt | `--ink` |
| brokerage slot underline, cover | 1.25pt | `--clay` |
| table head underline and table foot | 0.75pt | `--ink` |
| checkbox and diagram boundary | 0.75pt | `--rule-strong` |
| **NOT FOUND callout top, the heaviest rule in the system** | **2pt** | `--clay` |
| hero trust block top | 2px | `--clay` |
| horizon line inside an atmospheric field | 0.5pt | `rgba(237,234,227,.24)` |

Seven rule weights across a 39 page guide, and only one of them is heavier than a hairline plus a little. That is the "very few rules" part of the thesis, and it is what lets the single 2pt clay rule mean something.

### Radii and shadows

**Radius 0 everywhere. No shadow anywhere in the guide.** The only `box-shadow` in the file is on `.page` inside `@media screen`, and it exists purely so the paper trim reads on a gray screen background. It never prints.

### Print rules

- `@page { size: letter; margin: 0 }`. The page's own 0.80 / 0.72 / 0.75 insets are the live margin.
- `print-color-adjust: exact` and `-webkit-print-color-adjust: exact` on `body` and on every tinted surface.
- `break-inside: avoid` on the aside, the NOT FOUND callout, the diagram, the phone block, the soft close, every `li` in all three list types, and every table row.
- `thead { display: table-header-group }` so the four column headers repeat if the district table ever breaks.
- The table carries a real `<caption>`, `th scope="col"` on all four headers, and `th scope="row"` on all twenty district numbers.
- **No `position: fixed` anywhere in the file.** The landing hero is allowed to use it and does not.
- **Bullets use the flex pattern.** Every marker in `.numlist`, `.checklist` and `.sources` is a real flex child with `flex: 0 0 auto`. Nothing uses `li::before { position: absolute }`, which is why the source register survives `columns: 2` without a marker landing on the first letter of a column.
- `.page { height: 10.99in }` in print. Exactly 11in rounds onto a second sheet and emits a blank page after every page. `.page:last-of-type { break-after: auto }`.
- `.panel, .stage, .spread { display: contents }` in print, so no wrapper contributes height. **Verified: `preview.html` prints to exactly 6 letter sheets, no blanks.**

### The ink-lean build

Add `class="ink-lean"` to `<html>`. Every atmospheric field becomes a `--print-wash` panel inside a hairline and the caption drops to `--muted`. No type is ever reversed out of a field, so the swap loses nothing but the mood.

| build | cover ink density | interior mean | 6 sheet mean |
|---|---|---|---|
| default, the delivered PDF | 37.65% | 4.07% | 9.66% |
| `ink-lean` | 5.16% | 4.07% | 4.25% |

Measured by rasterising the printed PDF at 45dpi and averaging `(252 - gray) / 252` per pixel.

---

## 5. The two blocks that are load bearing

### `Real Broker, LLC`

Nevada requires a licensee's advertising to identify the brokerage. It gets a designed slot in three places, never a footnote:

1. **Cover byline**, 9.5pt Instrument Sans 600 at 0.155em uppercase, sitting on a 1.25pt clay rule directly under `Ryan Rose`. It is the only clay rule on the cover.
2. **Cover compliance line**, inside the verbatim legal sentence.
3. **Hero trust line**, set in `--ink` at 600 weight inside the verbatim line, with the block's 2px clay top rule marking it. Also repeated in the masthead at the top of the page.

### The `[NOT FOUND]` license slot

```css
.lic-slot{
  display:inline-block; min-width:11ch; text-align:left;
  font-variant-numeric:tabular-nums; font-weight:600;
}
```

`[NOT FOUND]` is 11 characters, longer than any real Nevada license number, and it ends its own line so nothing follows it horizontally. **Verified empirically:** substituting `S.0198736` and `BS.0012345` produces byte-identical geometry for the cover title, foot block, compliance block, brokerage slot, hero trust block and button. Zero reflow.

---

**Em-dashes in this file: zero.**
