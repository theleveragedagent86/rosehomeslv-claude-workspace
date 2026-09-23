# Direction 4: Postcard to Workbook, design tokens

> **Thesis.** The front half sells you on the valley. The back half hands you a pen and gets to work.
> The palette and the type do not change across the seam. Only the **layout behaviour** changes: the
> front half is photographic and celebratory, the back half is fillable.

All contrast ratios below were **computed with `python3`** against the WCAG 2.x relative luminance
formula, not asserted. Every text pair passes AA at the size and weight it is actually set at.
Every functional non text graphic passes 3.00.

---

## 1. Palette

| token | hex | role |
|---|---|---|
| `--ink` | `#2A1A20` | deep plum brown. All body prose, table cells, checklist copy. The warm near black that keeps the page from going newsprint cold. |
| `--ink-soft` | `#6B5560` | captions, running feet, figure captions, write in hint text, inline attributions. |
| `--paper` | `#FFF8ED` | postcard cream. Page stock for every page and the base of every panel. |
| `--paper-warm` | `#FDECD5` | one step deeper cream. Worksheet panels, the diagram box, the landing trust block. This is the "workbook page" surface. |
| `--rule` | `#9C8058` | **functional** ruled line. Every line a reader is meant to write on, plus the worksheet panel border. Deliberately dark enough to pass 3.00. |
| `--rule-soft` | `#DCC7AA` | **decorative only.** Table row separators, running foot hairline, the ruled paper texture on the divider page. Never carries an affordance. |
| `--sunset` | `#C22F17` | vermillion. The postcard red. Display type, tab chips, the divider band, the landing button, the write in panel border, checkbox outlines. |
| `--sunset-br` | `#E24A22` | brighter vermillion. **Graphics only, never carries type.** Stamp perforation ring, decorative rules. |
| `--marigold` | `#F5A517` | desert amber. Cover eyebrow chip, landing kicker, worksheet step numerals, the term bar in figure 4. |
| `--marigold-tint` | `#FCE9BE` | the write in field. Fill of the "I am not going to hand you a number" panel and of the NOT FOUND chips in the table. **In this system, amber means a blank you fill in.** |
| `--sky` | `#16697A` | dusty desert turquoise. Section subheads, table column headers, the escrow box in figure 4, checkbox outlines on page 19. |
| `--sky-lt` | `#59B3C4` | mid turquoise field. Property tax band in figure 4, cover sky gradient stop. |
| `--sky-tint` | `#D5EBEF` | the Q and A aside fill and the phone card fill. |
| `--cactus` | `#4C6B2F` | creosote green. Reserved for "this one is finished": the Matured and Paid off cells, and the third landing value prop. |
| `--plum` | `#6B2A5A` | canyon plum. Figure numbers, phone numbers, brokerage line on the cover, mountain shapes in the illustrated map. |

**Deliberately not used:** Rose Homes navy `#1C2333`, champagne `#C9A86E`, off white `#F7F5F0`.

---

## 2. Computed contrast, text

Large text threshold applied as WCAG defines it: 18pt regular or 14pt bold and above needs 3.00,
everything else needs 4.50.

| foreground | background | where it is used | size | weight | ratio | needs | verdict |
|---|---|---|---|---|---|---|---|
| `--ink` `#2A1A20` | `--paper` `#FFF8ED` | guide body prose, pages 19 and 20 | 9.1pt | 400 | **15.71** | 4.50 | PASS |
| `--ink` `#2A1A20` | `--paper` `#FFF8ED` | district table cell text | 7.4pt | 400 | **15.71** | 4.50 | PASS |
| `--ink` `#2A1A20` | `--paper-warm` `#FDECD5` | worksheet steps, figure 4 labels | 7.95pt | 400 | **14.31** | 4.50 | PASS |
| `--ink` `#2A1A20` | `--marigold-tint` `#FCE9BE` | NOT FOUND chip in the table | 6.5pt | 700 | **13.84** | 4.50 | PASS |
| `--ink` `#2A1A20` | `--marigold-tint` `#FCE9BE` | write in panel body copy | 8.2pt | 400 | **13.84** | 4.50 | PASS |
| `--ink` `#2A1A20` | `--marigold` `#F5A517` | cover eyebrow chip, landing kicker, step numerals | 8.6pt | 700 | **8.11** | 4.50 | PASS |
| `--ink` `#2A1A20` | `--sky-tint` `#D5EBEF` | Q and A aside body copy | 8.6pt | 400 | **13.38** | 4.50 | PASS |
| `--ink` `#2A1A20` | `--sky-lt` `#59B3C4` | property tax band label, figure 4 | 8.3pt | 500 | **6.84** | 4.50 | PASS |
| `--ink-soft` `#6B5560` | `--paper` `#FFF8ED` | figure caption, running foot, table caption | 6.4pt | 400 | **6.43** | 4.50 | PASS |
| `--ink-soft` `#6B5560` | `--paper-warm` `#FDECD5` | write in field hint text | 6.0pt | 400 | **5.86** | 4.50 | PASS |
| `--ink-soft` `#6B5560` | `--marigold-tint` `#FCE9BE` | write in blank field labels | 6.2pt | 700 | **5.67** | 4.50 | PASS |
| `--ink-soft` `#6B5560` | `--sky-tint` `#D5EBEF` | worksheet mini blank labels | 5.9pt | 700 | **5.48** | 4.50 | PASS |
| `--sunset` `#C22F17` | `--paper` `#FFF8ED` | cover title, page headlines, lead in | 20pt to 46pt | 400 | **5.36** | 3.00 | PASS |
| `--sunset` `#C22F17` | `--paper` `#FFF8ED` | soft close signature line | 8.1pt | 700 | **5.36** | 4.50 | PASS |
| `--sunset` `#C22F17` | `--paper-warm` `#FDECD5` | write in panel headline | 15pt | 400 | **4.88** | 4.50 | PASS |
| `--sunset` `#C22F17` | `--marigold-tint` `#FCE9BE` | write in panel headline on its own fill | 15pt | 400 | **4.72** | 4.50 | PASS |
| `--paper` `#FFF8ED` | `--sunset` `#C22F17` | tab chips, flags, divider band, landing button | 6.8pt to 38pt | 700 | **5.36** | 3.00 | PASS |
| `--paper` `#FFF8ED` | `--sky` `#16697A` | table column headers, worksheet flag | 7.0pt | 700 | **5.97** | 4.50 | PASS |
| `--paper` `#FFF8ED` | `--sky` `#16697A` | principal and interest band, figure 4 | 8.3pt | 500 | **5.97** | 4.50 | PASS |
| `--paper` `#FFF8ED` | `--plum` `#6B2A5A` | postmark ring text | 7.0pt | 700 | **9.46** | 4.50 | PASS |
| `--paper` `#FFF8ED` | `--ink` `#2A1A20` | landing headline and subhead on the scrim | 15px to 58px | 400 | **15.71** | 4.50 | PASS |
| `--sky` `#16697A` | `--paper` `#FFF8ED` | section subheads, page 20 headline | 12.6pt to 20pt | 700 | **5.97** | 3.00 | PASS |
| `--sky` `#16697A` | `--paper-warm` `#FDECD5` | figure 4 escrow box label | 10 units | 700 | **5.44** | 4.50 | PASS |
| `--sky` `#16697A` | `--sky-tint` `#D5EBEF` | Q and A aside heading | 10.4pt | 700 | **5.08** | 4.50 | PASS |
| `--cactus` `#4C6B2F` | `--paper` `#FFF8ED` | Matured and Paid off cells | 7.4pt | 600 | **5.77** | 4.50 | PASS |
| `--plum` `#6B2A5A` | `--paper-warm` `#FDECD5` | figure number, phone numbers | 7pt to 9pt | 700 | **8.62** | 3.00 | PASS |
| `--marigold` `#F5A517` | `--ink` `#2A1A20` | landing prop numerals on the scrim | 12px | 700 | **8.11** | 4.50 | PASS |

**Lowest text ratio anywhere in the system: 4.72.** No FAIL.

### Contrast, non text graphics (WCAG 1.4.11, needs 3.00)

| pair | where | ratio | needs | verdict |
|---|---|---|---|---|
| `--rule` `#9C8058` on `--paper` `#FFF8ED` | ruled write on lines, worksheet border | **3.53** | 3.00 | PASS |
| `--rule` `#9C8058` on `--paper-warm` `#FDECD5` | worksheet panel border on its own fill | **3.21** | 3.00 | PASS |
| `--rule` `#9C8058` on `--marigold-tint` `#FCE9BE` | dashed divider inside the write in panel | **3.11** | 3.00 | PASS |
| `--sunset` `#C22F17` on `--paper` `#FFF8ED` | write in panel border, checkbox outlines | **5.36** | 3.00 | PASS |
| `--sunset` `#C22F17` on `--marigold-tint` `#FCE9BE` | write in blank underlines | **4.72** | 3.00 | PASS |
| `--sky` `#16697A` on `--paper-warm` `#FDECD5` | worksheet mini blank underlines | **5.44** | 3.00 | PASS |
| `--sunset-br` `#E24A22` on `--paper` `#FFF8ED` | stamp perforation, purely decorative | **3.80** | 3.00 | PASS |
| `--marigold` `#F5A517` on `--ink` `#2A1A20` | landing prop numeral disc | **8.11** | 3.00 | PASS |

`--rule-soft` `#DCC7AA` measures **1.62** on paper and is intentionally below 3.00. It only ever
draws table row separators, the running foot hairline, and the ruled paper texture on the divider
page. It never draws a line a reader writes on and it never bounds a component. Every affordance
uses `--rule`, `--sunset`, or `--sky`.

### Grayscale luminance, for the home printer test

| token | relative luminance | approximate gray |
|---|---|---|
| `--paper` | 0.945 | 249 |
| `--paper-warm` | 0.857 | 238 |
| `--marigold-tint` | 0.827 | 234 |
| `--sky-tint` | 0.798 | 230 |
| `--rule-soft` | 0.590 | 201 |
| `--marigold` | 0.464 | 180 |
| `--sky-lt` | 0.383 | 165 |
| `--rule` | 0.232 | 131 |
| `--sunset-br` | 0.212 | 126 |
| `--sunset` | 0.136 | 103 |
| `--cactus` | 0.123 | 98 |
| `--sky` | 0.117 | 96 |
| `--ink-soft` | 0.105 | 91 |
| `--plum` | 0.055 | 68 |
| `--ink` | 0.013 | 36 |

`--sunset` 103, `--cactus` 98 and `--sky` 96 collapse to almost the same gray. That is handled, not
ignored: see the grayscale section of `rationale.md`. Short version, nothing in this direction is
distinguished by hue alone.

---

## 3. Type

**Google Fonts URL, exactly as used:**

```
https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Bitter:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Rubik:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap
```

**Three families, three jobs, no overlap.**

| family | job | never used for |
|---|---|---|
| **Alfa Slab One** 400 | postcard display only. Cover title, divider statement, page headlines, the write in panel headline, folios, big values, phone numbers. It has one weight and no italic, which is why it must never be asked to do subhead work. | anything under 9pt except phone numbers, and any running text |
| **Bitter** 400 / 500 / 600 / 700 + italic | the connective voice. Question subheads, deck lines, tab chips, flags, field labels, checklist step names, table headers, the soft close. | body prose |
| **Rubik** 300 / 400 / 500 / 600 / 700 | everything a reader reads at length or scans as data. Body prose, table cells, captions, hints, landing body. | headlines |

**Print scale (pt), pages 1, 18, 19, 20**

| role | family | size | line height | tracking |
|---|---|---|---|---|
| cover title | Alfa Slab One | 46 | 0.92 | -0.014em |
| divider statement | Alfa Slab One | 38 | 0.94 | -0.014em |
| page headline | Alfa Slab One | 20 | 1.00 | -0.012em |
| write in headline | Alfa Slab One | 15 | 1.04 | -0.010em |
| compare card value | Alfa Slab One | 12.5 | 1.00 | 0 |
| folio | Alfa Slab One | 13 | 1.00 | 0 |
| phone number | Alfa Slab One | 9 | 1.00 | -0.010em |
| cover subtitle | Bitter 500 | 13.4 | 1.34 | 0 |
| cover postcard message | Bitter 500 italic | 10.6 | 1.42 | 0 |
| deck line | Bitter 500 italic | 10 | 1.30 | 0 |
| section subhead | Bitter 700 | 12.6 | 1.16 | -0.004em |
| Q and A heading | Bitter 700 | 10.4 | 1.20 | 0 |
| lead in | Bitter 700 | 9.4 | inherit | 0 |
| phone card heading | Bitter 700 | 8.8 | 1.20 | 0 |
| checklist step name | Bitter 700 | 8.6 | inherit | 0 |
| soft close | Bitter 500 italic | 8.1 | 1.32 | 0 |
| table row header | Bitter 700 | 7.9 | 1.07 | 0 |
| tab chip and flag | Bitter 700 caps | 6.8 to 7.4 | 1.15 | 0.15em |
| table column header | Bitter 700 caps | 7 | 1.15 | 0.10em |
| NOT FOUND chip | Bitter 700 | 6.5 | 1.10 | 0.06em |
| field label | Bitter 700 caps | 5.9 to 6.6 | 1.15 | 0.08em to 0.16em |
| body prose | Rubik 400 | 9.1 | 1.45 | 0 |
| Q and A body | Rubik 400 | 8.6 | 1.44 | 0 |
| write in body | Rubik 400 | 8.2 | 1.38 | 0 |
| body tight | Rubik 400 | 8.0 | 1.34 | 0 |
| checklist body | Rubik 400 | 7.95 | 1.33 | 0 |
| compare card body | Rubik 400 | 7.5 | 1.28 | 0 |
| table cell | Rubik 400 | 7.4 | 1.07 | 0 |
| compliance line | Rubik 400 | 7.4 | 1.42 | 0 |
| phone card body | Rubik 400 | 7.0 | 1.28 | 0 |
| inline attribution | Rubik 400 italic | 6.9 | 1.34 | 0 |
| running foot, figure caption | Rubik 400 | 6.4 to 6.9 | 1.32 | 0.03em |
| source superscript | Rubik 600 | 6.2 | 0 | 0 |

**Landing scale (px)**

| role | family | size | line height |
|---|---|---|---|
| hero headline | Alfa Slab One | `clamp(32px, 4.35vw, 58px)` | 0.99, tracking -0.016em |
| hero subhead | Rubik 400 | `clamp(15px, 1.35vw, 18px)` | 1.62 |
| kicker chip | Bitter 700 caps | 12 | 1.2, tracking 0.15em |
| value prop title | Bitter 700 | 17 | 1.22 |
| value prop body | Rubik 400 | 14 | 1.52 |
| button | Bitter 700 | 19 | 1.0 |
| microcopy | Rubik 400 | 14 | 1.4 |
| trust field label | Bitter 700 caps | 11 | 1.15, tracking 0.14em |
| trust field value | Bitter 600 | 15, brokerage 16, contact 13 | 1.15 to 1.35 |

At 420px and below the headline is pinned to 31px so it never drops below three readable lines.

---

## 4. Spacing, radii, and the grid

**Print spacing scale, in inches.** Every vertical gap on the guide pages is one of these.

| token | value |
|---|---|
| `--s1` | 0.06in |
| `--s2` | 0.10in |
| `--s3` | 0.14in |
| `--s4` | 0.20in |
| `--s5` | 0.28in |
| `--s6` | 0.40in |

**Page geometry.** Trim 8.5in by 11in. Cover margin 0.40in. Guide page live area is
`padding: .38in .48in .3in`, giving a 7.54in measure. Two column blocks use a `.26in` gutter.
The running foot is pinned with `margin-top:auto`, never with `position:fixed`.

**Radii.** `--r-chip: 3px` for tab chips and flags. `--r-card: 8px` for panels and cards.
`--r-pill: 999px` for the geography chips and step numerals. Stamps, postmarks, the write in rules
and the table are square, on purpose. The workbook half is squarer than the postcard half.

**Elevation.** Only three levels exist. Paper (`--paper`). Panel (`--paper-warm`, `--sky-tint`,
`--marigold-tint`, no shadow, bounded by a border). Floating (the cover photo and the divider
postcards, which carry a real drop shadow because they are pretending to be physical objects). Guide
body panels never float. Shadow is a postcard device, not a workbook device.

---

## 5. Print rules

```css
@page { size: letter; margin: 0; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
```

- `break-inside: avoid` and `page-break-inside: avoid` on `.qa`, `.writein`, `.worksheet`,
  `.phonecard`, `.diagram`, `.tablewrap`, `.cc`, `.softclose`, and every `<tr>`.
- `thead { display: table-header-group }` so the district table repeats its header if it is ever
  reflowed onto a second page.
- **`position: fixed` appears nowhere in the guide pages.** The divider page foot uses
  `position: absolute` inside an already absolutely positioned block, which is safe.
- Page boxes carry `overflow:hidden` in the preview so any overrun is caught at the gate rather than
  spilling silently. Both guide pages currently fit with room to spare: page 19 has about 24px of
  slack, page 20 about 6px.
- Photography is placed with `object-fit: cover` inside fixed boxes so a 300dpi swap needs no layout
  change. Supply the print PDF with the full resolution originals from
  `assets/img/`, not the preview copies.
- Ink: the divider band and the tab chips are the only full bleed saturated fields in the guide
  body. See the ink coverage section in `rationale.md` for the honest 44 page number.

## 6. Accessibility contract

- Every `<img>` carries real alt text describing the place, never a community or builder name.
- Every meaningful inline SVG carries `role="img"`, `<title>`, and `<desc>`. The two pencil icons
  are `aria-hidden="true"` because the adjacent words already say "Bring a pen".
- The district table has a `<caption>`, `<th scope="col">` on all four columns, and
  `<th scope="row">` on the district number.
- Bullets and checklists are **flexbox rows with a real element for the marker**. There is no
  `li::before { position:absolute }` anywhere in this file.
- Nothing is distinguished by color alone. NOT FOUND cells carry the literal words plus a dotted
  underline. Matured and Paid off carry a check glyph plus the word. The three landing props carry
  numerals. The compare cards carry district numbers.
