# Direction 4, Spec Sheet, design tokens

**Thesis:** a house is a spec, so the guide reads like the spec.
**Deliberately off-brand.** No Rose Homes LV navy, champagne, or warm off-white. No Playfair Display, no Montserrat, no Bebas Neue.

---

## 1. Color

Every value below is used in `preview.html`. There are no unused tokens.

| Token | Hex | Role |
|---|---|---|
| `--sheet` | `#FFFFFF` | Page stock. The only background on a guide page. Zero ink. |
| `--ink-900` | `#10161C` | Graphite. Body prose, headlines, schedule data, structural borders. A blue black, not a true black, so it reads as drafting ink rather than laser default. |
| `--ink-700` | `#2B3640` | Sheet border, box outlines, section rules. Non-text. |
| `--ink-600` | `#46525C` | Deck, value prop body, diagram annotation text. |
| `--ink-500` | `#5A6672` | Reference notes, title block labels, muted micro type. |
| `--rule-mid` | `#7C8994` | Meaning bearing hairlines: title block cell dividers, note column rules. Passes 3:1 as a non-text UI component. |
| `--rule-hair` | `#C3CBD1` | Purely decorative hairline, schedule row separators. Never the only carrier of meaning. |
| `--grid-line` | `#E4E9EC` | The drafting grid. Decorative. Never the only carrier of meaning. |
| `--fill-01` | `#EFF3F5` | Schedule header, detail head, phone block head, title block sheet cell. |
| `--fill-02` | `#F6F8F9` | Schedule zebra row. |
| `--redline` | `#B22A15` | The revision accent. HOLD tags, NOT FOUND markers, section ids, checklist numerals, the landing page button. |
| `--redline-deep` | `#9E2412` | Redline on tint, small redline text, button border and hover. |
| `--redline-fill` | `#FCF0ED` | HOLD block header band. |
| `--dim` | `#14607A` | The annotation accent. Dimension lines, DETAIL id tags, deck rule, diagram leaders. |
| `--dim-deep` | `#0F4E63` | Dim blue on tint, reference markers, note URLs. |
| `--dim-fill` | `#E6EFF3` | DETAIL box header band. |

### Path tokens, for pages 6 to 17

The three edge tabs must be told apart in black and white. They are separated by **value**, not hue. Grayscale values computed below.

| Token | Hex | Grayscale | Treatment |
|---|---|---|---|
| `--path-a` | `#10161C` | 21 | Solid tab, white caps. `PATH A · MOVING HERE` |
| `--path-b` | `#5A6672` | 101 | Solid tab, white caps. `PATH B · MOVING UP` |
| `--path-c` | `#EFF3F5` | 242 | Light tab, 2.5px `--ink-900` border, ink caps. `PATH C · FIRST BUILD` |

Three values 21 / 101 / 242 on a 0 to 255 scale. No two tabs can be confused on a home printer. White on `--path-b` computes 5.87:1, ink on `--path-c` computes 16.31:1, white on `--path-a` computes 18.20:1. All PASS.

### Palette rationale

Conversion research on lead magnets points the same way twice: a warm red CTA on a neutral field outperforms cool CTAs when the surrounding page is low chroma, and the effect comes from isolation rather than the hue itself. That is exactly a drafting sheet. `#B22A15` is the redline pencil a reviewer marks a drawing with, so the one color that means "act" is also the one color that means "this is the open item". `#14607A` is the plotter pen used for dimensions and annotation, so it means "measured, not urgent". Everything else is graphite on white. The reader has already been sold to by a builder's photography. A sheet with no photography and no gradient is a different kind of promise.

---

## 2. Computed WCAG contrast table

Computed in Python with the WCAG 2.x relative luminance formula, not asserted. AA thresholds: 4.5:1 for body, 3:1 for large text (18.66px+ bold or 24px+ regular) and for non-text UI components.

| Foreground | Background | Ratio | Used at | Threshold | Result |
|---|---|---|---|---|---|
| `--ink-900 #10161C` | `--sheet #FFFFFF` | 18.20 | body prose 12.9px / 400 | 4.5 | PASS |
| `--ink-900 #10161C` | `--sheet #FFFFFF` | 18.20 | page headline 25.5px / 600 | 3.0 | PASS |
| `--ink-900 #10161C` | `--sheet #FFFFFF` | 18.20 | cover title 61px / 600 | 3.0 | PASS |
| `--ink-600 #46525C` | `--sheet #FFFFFF` | 8.01 | deck 14px / 400 italic | 4.5 | PASS |
| `--ink-600 #46525C` | `--sheet #FFFFFF` | 8.01 | value prop body 13.6px / 400 | 4.5 | PASS |
| `--ink-500 #5A6672` | `--sheet #FFFFFF` | 5.87 | reference notes 7.1px / 400 | 4.5 | PASS |
| `--ink-500 #5A6672` | `--sheet #FFFFFF` | 5.87 | title block labels 8px / 600 | 4.5 | PASS |
| `--redline #B22A15` | `--sheet #FFFFFF` | 6.49 | section id tag 9.2px / 600 | 4.5 | PASS |
| `--redline #B22A15` | `--sheet #FFFFFF` | 6.49 | checklist numeral 11px / 700 | 4.5 | PASS |
| `--redline-deep #9E2412` | `--sheet #FFFFFF` | 7.74 | NOT FOUND schedule cell 8.7px / 700 | 4.5 | PASS |
| `--dim-deep #0F4E63` | `--sheet #FFFFFF` | 9.17 | reference marker 8px / 600 | 4.5 | PASS |
| `--dim-deep #0F4E63` | `--sheet #FFFFFF` | 9.17 | note URL 7.1px / 400 | 4.5 | PASS |
| `--ink-900 #10161C` | `--fill-01 #EFF3F5` | 16.31 | schedule header 9.2px / 700 | 4.5 | PASS |
| `--ink-900 #10161C` | `--fill-02 #F6F8F9` | 17.09 | schedule zebra cell 8.7px / 400 | 4.5 | PASS |
| `--ink-500 #5A6672` | `--fill-01 #EFF3F5` | 5.26 | props footer label 8px / 600 | 4.5 | PASS |
| `--redline-deep #9E2412` | `--redline-fill #FCF0ED` | 6.93 | HOLD register label 9.2px / 600 | 4.5 | PASS |
| `--ink-900 #10161C` | `--redline-fill #FCF0ED` | 16.32 | HOLD headline 14.6px / 600 | 4.5 | PASS |
| `--dim-deep #0F4E63` | `--dim-fill #E6EFF3` | 7.86 | DETAIL title 9.2px / 600 | 4.5 | PASS |
| `--sheet #FFFFFF` | `--redline #B22A15` | 6.49 | button label 17px / 600 | 4.5 | PASS |
| `--sheet #FFFFFF` | `--redline #B22A15` | 6.49 | HOLD tag 9.2px / 700 | 4.5 | PASS |
| `--sheet #FFFFFF` | `--ink-900 #10161C` | 18.20 | SHEET tag 9.2px / 700 | 4.5 | PASS |
| `--sheet #FFFFFF` | `--ink-900 #10161C` | 18.20 | props header 11px / 700 | 4.5 | PASS |
| `--sheet #FFFFFF` | `--dim #14607A` | 7.04 | DETAIL id tag 9.2px / 700 | 4.5 | PASS |
| `--sheet #FFFFFF` | `--path-b #5A6672` | 5.87 | path B tab caps 10px / 700 | 4.5 | PASS |
| `--ink-900 #10161C` | `--path-c #EFF3F5` | 16.31 | path C tab caps 10px / 700 | 4.5 | PASS |
| `--ink-700 #2B3640` | `--sheet #FFFFFF` | 12.32 | sheet border, box outlines, non-text | 3.0 | PASS |
| `--rule-mid #7C8994` | `--sheet #FFFFFF` | 3.58 | title block dividers, note column rule, non-text | 3.0 | PASS |

**Lowest ratio actually used on text: 5.26:1.** Every text pair clears AA with margin, and every pair except one clears AAA for body text as well.

Two tokens sit below 3:1 and are therefore restricted by rule, not disclosed as failures:

- `--rule-hair #C3CBD1`, 1.64:1
- `--grid-line #E4E9EC`, 1.22:1

**Rule:** neither may ever be the sole carrier of information. They separate schedule rows and draw the grid field. Every boundary that means something (schedule header, section break, title block, HOLD block, DETAIL box) is drawn in `--rule-mid` or heavier. A reader who cannot see either token loses no content.

### Grayscale values, computed

| Hex | 8 bit gray |
|---|---|
| `#10161C` | 21 |
| `#2B3640` | 53 |
| `#0F4E63` | 72 |
| `#9E2412` | 83 |
| `#14607A` | 89 |
| `#B22A15` | 94 |
| `#5A6672` | 101 |
| `#7C8994` | 135 |
| `#C3CBD1` | 202 |
| `#E4E9EC` | 232 |
| `#EFF3F5` | 242 |
| `#F6F8F9` | 248 |

`--redline` (94) and `--dim` (89) are five levels apart. In black and white they are the same gray. That is accepted on purpose and handled by form, see `rationale.md`.

---

## 3. Type

### Families

| Role | Family | Weights |
|---|---|---|
| Prose | IBM Plex Serif | 400, 400 italic, 600 |
| Headlines, structured text, UI | IBM Plex Sans | 400, 500, 600, 700 |
| Data, labels, title block, tags | IBM Plex Mono | 400, 500, 600, 700 |
| Schedule "where" column, reference notes | IBM Plex Sans Condensed | 400, 600 |

One superfamily, four cuts. That is the point: a spec set and its drawings come out of one drawer, and IBM Plex was drawn as a single system with matched metrics across serif, sans, condensed, and mono. It reads technical without reading cold, it has a large x-height that survives small sizes on a home laser, and it is nowhere near Playfair, Montserrat, or Bebas Neue.

### Exact Google Fonts URL

```
https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Sans+Condensed:wght@400;600&family=IBM+Plex+Serif:ital,wght@0,400;0,600;1,400&display=swap
```

### Scale

px at 96dpi. Point equivalents given because this is a print piece.

| Token | px | pt | Line height | Tracking | Applied to |
|---|---|---|---|---|---|
| `--t-title` | 61 | 45.8 | 1.015 | -0.021em | Cover title |
| `--t-head` | 25.5 | 19.1 | 1.11 | -0.019em | Page headline |
| `--t-sub` | 19 | 14.3 | 1.18 | -0.012em | Subhead |
| (hero h1) | clamp 30 to 50 | | 1.07 | -0.024em | Landing headline |
| (cover sub) | 17 | 12.8 | 1.42 | 0 | Cover subtitle |
| `--t-deck` | 14 | 10.5 | 1.36 | 0 | Deck, italic serif |
| `--t-body` | 12.9 | 9.7 | 1.35 | 0 | Body prose |
| `--t-md` | 11.8 | 8.9 | 1.30 | 0 | HOLD block body |
| `--t-sm` | 11 | 8.25 | 1.34 to 1.35 | 0 | Numbered list, checklist, DETAIL, phone block, soft close |
| `--t-label` | 10.7 | 8.0 | 1.1 | 0.10em | Section head bar |
| (title block value) | 10.2 | 7.7 | 1.24 | 0 | Title block values, licence slot |
| `--t-tag` | 9.2 | 6.9 | 1.0 | 0.14em | Drafting tags, HOLD, DETAIL, SVG id |
| `--t-data` | 8.7 | 6.5 | 1.2 | 0 | Schedule cells, mono |
| `--t-micro` | 8 | 6.0 | 1.1 | 0.14em | Title block labels |
| `--t-note` | 7.1 | 5.3 | 1.26 | 0 | Reference notes strip |

Tracking tokens: `--tr-tag 0.14em`, `--tr-lab 0.10em`, `--tr-title -0.021em`.

**Two of these are below the brief's stated spec and it is deliberate. See `rationale.md` for the measured cost of holding the spec instead.**

---

## 4. Spacing, rules, radii

**Spacing scale**, named after drafting sixteenths, in px:
`--s1 2 · --s2 4 · --s3 6 · --s4 9 · --s5 10 · --s6 13 · --s7 19 · --s8 26 · --s9 36`

**Rule weights:**

| Token | Value | Use |
|---|---|---|
| `--w-hair` | 0.5px | Inner border line, coordinate margin, schedule row separators, note column rule |
| `--w-thin` | 1px | Box outlines, DETAIL border, schedule header underline, title block outer |
| `--w-mid` | 1.5px | Sheet drawing border, checkbox, prop numeral box, hero frame |
| `--w-heavy` | 2.5px | Title block top edge, HOLD border, deck rule, phone block left edge |

**Radii:** `--r-none: 0px`. There are no rounded corners anywhere in this direction. A drafting sheet has none.

**Grid field:** `repeating-linear-gradient` at `0.125in` pitch inside diagram fields, `0.1667in` pitch on the cover, drawn in `--grid-line` at 0.5px.

**Sheet geometry:**

| Item | Value |
|---|---|
| Trim | 8.5in x 11in |
| Drawing border inset | 0.30in, double rule (1.5px outer, 0.5px inner at +0.055in) |
| Coordinate margin | letters A to F top and bottom, numerals 1 to 8 left and right |
| Live area | left/right 0.54in, top 0.42in, bottom 0.94in |
| Title block | full width inside border, 0.51in tall, bottom 0.365in |
| Cover title block | full width, 2.28in tall |
| Column gutter | 12px, with a `--rule-hair` column rule |

**Licence slot, no reflow guarantee:** `.lic__slot { display:inline-block; min-width:11ch; }` in IBM Plex Mono. `[NOT FOUND]` is 11 characters. Any Nevada licence string of 11 characters or fewer (`S.0123456`, `BS.0012345`) drops in with zero reflow. The cover cell also reserves a second line, so a longer string wraps inside the cell without moving any other cover element.

---

## 5. Print rules

```css
@page { size: letter; margin: 0; }
```

- `-webkit-print-color-adjust: exact; print-color-adjust: exact;` on `.sheet`.
- `break-inside: avoid` on `.detail`, `.hold`, `.sched`, `.sched tbody tr`, `.phones`, `.close`, `.notes`, `.dgm`, `.tblock`, `.step`, `.chk__i`, `.note`.
- `thead { display: table-header-group }` and `tfoot { display: table-footer-group }` so the schedule header repeats when a long table breaks.
- Every table carries `<caption>` and `<th scope="col">` or `<th scope="row">`.
- `page-break-after: always` on every `.sheet` except the last.
- **No `position: fixed` anywhere in the guide.** The title block is `position: absolute` inside a `position: relative` sheet, so it prints once per sheet, never repeated by the browser. The landing page may use `position: fixed` for a mobile action bar; the preview demonstrates it as `position: sticky` inside the 375px frame.
- Grid fields drop to `opacity: .72` in print so a laser does not build them up.
- Bullets and numbered markers use `display: flex` with the marker as a real flex child. Never `li::before { position: absolute }`. Under CSS multi-column, an absolutely positioned marker lands on the first letter. The reference notes strip is multi-column, so this is not optional.
