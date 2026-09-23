# Direction 3, Scrapbook. Design tokens

**Thesis:** a friend who already did this walked you through it and wrote in the margins.
**Rule that governs everything:** the data is crisp, the surroundings are handmade.

---

## 1. Palette

| token | hex | role |
|---|---|---|
| `--paper` | `#FBF4E6` | the stock. Every guide page, the landing hero. Warm cream, never white |
| `--paper-deep` | `#F3E7CF` | zebra tint source, mixed at 42 percent over `--card` |
| `--card` | `#FFFDF7` | anything laid ON the paper: index card asides, the table, the checklist, photo frames |
| `--ink` | `#33281C` | all body copy and all data. Warm near black, never `#000` |
| `--ink-soft` | `#6A5A45` | inline attribution, table caption, page foot, hero microcopy |
| `--pen` | `#22406B` | the handwriting. Margin notes, photo captions, hand drawn arrows. Ballpoint blue |
| `--redpen` | `#A6321F` | the second pen. Circles around a value, the diagram tick, value prop numerals |
| `--terracotta` | `#B2432A` | primary accent. Button, folio, `Real Broker, LLC`, the beat line, the assessment block |
| `--teal` | `#186670` | section subheads, the 215 in the doodle map, chip 1 |
| `--sage` | `#3F6E48` | chip 2, valley outline in the doodle map |
| `--plum` | `#7A3A63` | chip 3, the Strip marks in the doodle map |
| `--hi-yellow` | `#FFE49B` | highlighter swipe, and the two highlighted table rows |
| `--hi-mint` | `#C6E6CE` | second highlighter, used once per spread at most |
| `--hi-pink` | `#F9CDC2` | third highlighter, held in reserve |
| `--sticky` | `#FFE9A8` | sticky note stock. The NOT FOUND callout and value prop 1 |
| `--sticky-mint` | `#CFE6D4` | phone card, value prop 2 |
| `--sticky-blue` | `#CFE0EE` | value prop 3, escrow layers in the diagram |
| `--sticky-pink` | `#F9CDC2` | checklist card spine |
| `--kraft` | `#E8D5B0` | washi tape, HOA layers in the diagram |
| `--kraft-dark` | `#D9C29B` | computed dark end of the tape gradient, worst case background for tape labels |
| `--rule` | `rgba(51,40,28,.18)` | hairlines, card borders, dashed compliance rule |
| `--rule-soft` | `rgba(51,40,28,.10)` | table row rules |
| preview surround | `#8B8B87` | neutral gray behind the page boxes. Preview chrome only, never printed |

**Derived values** (computed, not eyeballed):
`--zebra` = `--paper-deep` at 42 percent over `--card` = **`#FAF4E6`**.
`--kraft-dark` = `#D6BE94` at 92 percent over `--paper` = **`#D9C29B`**.

**Off limits.** Rose Homes navy `#1C2333`, champagne `#C9A86E`, off white `#F7F5F0`. This lead magnet has its own conversion palette by design.

---

## 2. Contrast, computed with python3

Every pair below is one that actually appears in `preview.html`. Ratios are WCAG 2.x relative luminance, two decimals. AA threshold is 4.5 for normal text and 3.0 for large text, where large means 18pt or more, or 14pt or more at weight 700 plus.

| foreground | background | size, weight | ratio | AA needs | result | where |
|---|---|---|---|---|---|---|
| `--ink` #33281C | `--paper` #FBF4E6 | 9.2pt / 400 | 13.13 | 4.5 | PASS | body prose, guide pages |
| `--ink` #33281C | `--paper` #FBF4E6 | 10.8pt / 600 | 13.13 | 4.5 | PASS | deck under the page headline |
| `--ink` #33281C | `--paper` #FBF4E6 | 24pt / 800 | 13.13 | 3.0 | PASS | page headline, Baloo 2 |
| `--ink` #33281C | `--paper` #FBF4E6 | 44pt / 800 | 13.13 | 3.0 | PASS | cover title, Baloo 2 |
| `--ink` #33281C | `--paper` #FBF4E6 | 29px / 800 | 13.13 | 3.0 | PASS | hero h1 at 375px |
| `--ink` #33281C | `--card` #FFFDF7 | 8.6pt / 400 | 14.13 | 4.5 | PASS | aside prose, checklist prose |
| `--ink` #33281C | `--card` #FFFDF7 | 9.8pt / 800 | 14.13 | 4.5 | PASS | aside lead in |
| `--ink` #33281C | `--card` #FFFDF7 | 8.2pt / 800 | 14.13 | 4.5 | PASS | table row header, district number |
| `--ink` #33281C | `--card` #FFFDF7 | 7.5pt / 400 | 14.13 | 4.5 | PASS | table body cells |
| `--ink` #33281C | `--zebra` #FAF4E6 | 7.5pt / 400 | 13.11 | 4.5 | PASS | table body cells on the zebra tint |
| `--ink` #33281C | `--hi-yellow` #FFE49B | 7.5pt / 400 | 11.51 | 4.5 | PASS | the two highlighted table rows |
| `--ink` #33281C | `--hi-yellow` #FFE49B | 9.2pt / 400 | 11.51 | 4.5 | PASS | highlighter swipe over body prose |
| `--ink` #33281C | `--hi-mint` #C6E6CE | 9.2pt / 400 | 10.68 | 4.5 | PASS | mint swipe, one line on page 20 |
| `--ink` #33281C | `--sticky` #FFE9A8 | 8.7pt / 400 | 11.96 | 4.5 | PASS | NOT FOUND sticky note body |
| `--ink` #33281C | `--sticky` #FFE9A8 | 25pt / 700 | 11.96 | 3.0 | PASS | NOT FOUND sticky note headline, Caveat |
| `--ink` #33281C | `--sticky` #FFE9A8 | 14.5px / 400 | 11.96 | 4.5 | PASS | value prop card 1 body |
| `--ink` #33281C | `--sticky-mint` #CFE6D4 | 8.1pt / 400 | 10.90 | 4.5 | PASS | phone card body |
| `--ink` #33281C | `--sticky-blue` #CFE0EE | 8pt / 400 | 10.64 | 4.5 | PASS | diagram escrow block labels |
| `--ink` #33281C | `--kraft` #E8D5B0 | 8pt / 400 | 9.98 | 4.5 | PASS | diagram HOA block labels |
| `--ink` #33281C | `--kraft-dark` #D9C29B | 10.5pt / 700 | 8.31 | 4.5 | PASS | cover eyebrow on washi tape |
| `--ink` #33281C | `--kraft-dark` #D9C29B | 13px / 700 | 8.31 | 4.5 | PASS | hero eyebrow tape |
| `--ink-soft` #6A5A45 | `--paper` #FBF4E6 | 6.9pt / 400 | 6.07 | 4.5 | PASS | page foot source pointer |
| `--ink-soft` #6A5A45 | `--paper` #FBF4E6 | 7pt / 400 | 6.07 | 4.5 | PASS | inline attribution line |
| `--ink-soft` #6A5A45 | `--paper` #FBF4E6 | 6.9pt / 400 | 6.07 | 4.5 | PASS | table caption |
| `--ink-soft` #6A5A45 | `--paper` #FBF4E6 | 14px / 400 | 6.07 | 4.5 | PASS | hero microcopy under the button |
| `--ink-soft` #6A5A45 | `--card` #FFFDF7 | 14px / 400 | 6.53 | 4.5 | PASS | closing strip, right side |
| `--pen` #22406B | `--paper` #FBF4E6 | 14pt / 400 | 9.53 | 4.5 | PASS | margin notes, Caveat |
| `--pen` #22406B | `--paper` #FBF4E6 | 17pt / 400 | 9.53 | 4.5 | PASS | cover margin note, Caveat |
| `--pen` #22406B | `--card` #FFFDF7 | 13pt / 400 | 10.25 | 4.5 | PASS | photo captions, Caveat |
| `--pen` #22406B | `--card` #FFFDF7 | 11.5pt / 400 | 10.25 | 4.5 | PASS | lane photo caption, Caveat |
| `--pen` #22406B | `--card` #FFFDF7 | 9.8pt / 800 | 10.25 | 4.5 | PASS | aside lead in |
| `--pen` #22406B | `--sticky-blue` #CFE0EE | 9pt / 400 | 7.72 | 4.5 | PASS | note written on a blue sticker |
| `--redpen` #A6321F | `--paper` #FBF4E6 | 13.5pt / 400 | 6.19 | 4.5 | PASS | red pen margin note |
| `--redpen` #A6321F | `--paper` #FBF4E6 | 30px / 700 | 6.19 | 3.0 | PASS | value prop numerals |
| `--redpen` #A6321F | `--card` #FFFDF7 | 12px / 400 | 6.67 | 4.5 | PASS | diagram tick label, Caveat |
| `--redpen` #A6321F | `--sticky` #FFE9A8 | 30px / 700 | 5.64 | 3.0 | PASS | value prop 1 numeral on yellow |
| `--terracotta` #B2432A | `--paper` #FBF4E6 | 11.5pt / 700 | 5.14 | 4.5 | PASS | beat line |
| `--terracotta` #B2432A | `--paper` #FBF4E6 | 10pt / 800 | 5.14 | 4.5 | PASS | folio numeral |
| `--terracotta` #B2432A | `--paper` #FBF4E6 | 9.5pt / 700 | 5.14 | 4.5 | PASS | `Real Broker, LLC` on the byline card |
| `--terracotta` #B2432A | `--paper` #FBF4E6 | 12.5px / 700 | 5.14 | 4.5 | PASS | `Real Broker, LLC` in the hero trust line |
| `--teal` #186670 | `--paper` #FBF4E6 | 14.5pt / 800 | 6.05 | 3.0 | PASS | section subheads |
| `--teal` #186670 | `--paper` #FBF4E6 | 20pt / 800 | 6.05 | 3.0 | PASS | page 20 opening subhead |
| `--paper` #FBF4E6 | `--ink` #33281C | 7.2pt / 800 | 13.13 | 4.5 | PASS | table column headers, reversed |
| `--paper` #FBF4E6 | `--terracotta` #B2432A | 19px / 800 | 5.14 | 3.0 | PASS | primary button label |
| `--paper` #FBF4E6 | `--terracotta` #B2432A | 8pt / 700 | 5.14 | 4.5 | PASS | NOT FOUND ON PURPOSE sticker |
| `--paper` #FBF4E6 | `--terracotta` #B2432A | 8.6pt / 800 | 5.14 | 4.5 | PASS | special assessment label in the diagram |
| `--paper` #FBF4E6 | `--teal` #186670 | 8pt / 700 | 6.05 | 4.5 | PASS | geography chip, Las Vegas |
| `--paper` #FBF4E6 | `--sage` #3F6E48 | 8pt / 700 | 5.43 | 4.5 | PASS | geography chip, Henderson |
| `--paper` #FBF4E6 | `--plum` #7A3A63 | 8pt / 700 | 7.34 | 4.5 | PASS | geography chip, Clark County |

**49 pairs, 0 failures. Lowest ratio in the system is 5.14** (`--terracotta` on `--paper`), which clears the strict 4.5 threshold even where it is only asked to clear 3.0. Nothing in this direction sits near the line.

Text is never set on a photograph. Photographs carry captions on the white frame below them, which is why no image contrast pair appears above.

---

## 3. Type

```
https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700;800&family=Caveat:wght@400;600;700&family=Nunito:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap
```

| role | face | why |
|---|---|---|
| display and structure | **Baloo 2** 700 / 800 | rounded, chunky, friendly. Reads as a person, not a firm. Carries a 44pt cover title without shouting |
| body and data | **Nunito** 400 / 600 / 700 / 800 | humanist rounded sans, open counters, holds legibility down to 7.5pt in a table |
| annotation only | **Caveat** 400 / 700 | a real handwriting face. Margin notes, photo captions, the NOT FOUND headline, diagram ticks. **Never body copy** |

**The hand face rule.** Caveat appears only where a person would actually write by hand: in a margin, on a photo, on a sticky note headline, on a diagram tick. The moment a reader has to read more than about 12 words, it becomes Nunito. The NOT FOUND callout is the boundary case and it is deliberate: the headline is in the hand, the four paragraphs under it are not.

### Full scale

**Cover**
| element | size / line height / weight | face |
|---|---|---|
| eyebrow on tape | 10.5pt / 1 / 700, tracking .055em, caps | Baloo 2 |
| title | 44pt / 1.02 / 800, tracking -.018em | Baloo 2 |
| subtitle | 13pt / 1.5 / 400 | Nunito |
| geography chips | 8pt / 1 / 700, tracking .09em, caps | Baloo 2 |
| credibility line | 10pt / 1.4 / 600 | Nunito |
| margin note | 17pt / 1.1 / 400 | Caveat |
| byline name | 17pt / 1.1 / 800 | Baloo 2 |
| `Real Broker, LLC` | 9.5pt / 1.2 / 700, tracking .15em, caps | Baloo 2 |
| edition note | 14.5pt / 1.12 / 400 and 700 | Caveat |
| compliance line | 8pt / 1.5 / 400 | Nunito |

**Guide interior**
| element | size / line height / weight | face |
|---|---|---|
| running head | 8.5pt / 1.2 / 700, tracking .14em, caps | Baloo 2 |
| page headline | 24pt / 1.05 / 800, tracking -.015em | Baloo 2 |
| deck | 10.8pt / 1.38 / 600 | Nunito |
| section subhead | 14.5pt / 1.14 / 800, teal | Baloo 2 |
| opening subhead, page 20 | 20pt / 1.14 / 800, teal | Baloo 2 |
| body | 9.2pt / 1.45 / 400 | Nunito |
| beat line | 11.5pt / 1.2 / 700, terracotta | Baloo 2 |
| aside lead in | 9.8pt / 1.2 / 800, pen | Baloo 2 |
| aside body | 8.8pt / 1.44 / 400 | Nunito |
| numbered list | 8.6pt / 1.4 / 400, bold lead in at 800 | Nunito |
| numbered token | 8pt / 1 / 800 in a .215in circle | Baloo 2 |
| sticky headline | 25pt / 1 / 700 | Caveat |
| sticky body | 8.7pt / 1.44 / 400, two columns | Nunito |
| table column head | 7.2pt / 1.2 / 800, tracking .05em, caps, reversed | Baloo 2 |
| table row head | 8.2pt / 1.2 / 800 | Baloo 2 |
| table cell | 7.5pt / 1.18 / 400 | Nunito |
| table caption | 6.9pt / 1.32 / 400, ink-soft | Nunito |
| NOT FOUND chip | 6.8pt / 1 / 700, tracking .06em, dashed outline | Baloo 2 |
| checklist title | 12.5pt / 1.14 / 800 | Baloo 2 |
| checklist item | 8pt / 1.36 / 400, bold lead in at 800 | Nunito |
| phone card title | 17pt / 1 / 700 | Caveat |
| phone number | 10.5pt / 1.2 / 800 | Baloo 2 |
| soft close | 8.6pt / 1.44 / 400, offer line at 800 | Nunito |
| signature | 19pt / 1 / 400, pen | Caveat |
| margin note | 14pt / 1.08 / 400, pen or redpen | Caveat |
| inline attribution | 7pt / 1.35 / 400 italic, ink-soft | Nunito |
| page foot | 6.9pt / 1.4 / 400, ink-soft | Nunito |
| folio | 10pt / 1 / 800, terracotta | Baloo 2 |
| superscript source numeral | .62em / 700, ink-soft, `vertical-align:super` | Nunito |

**Landing hero** (px, because it is a web surface)
| element | size / line height / weight | face |
|---|---|---|
| eyebrow tape | 13px / 1 / 700, tracking .09em, caps | Baloo 2 |
| h1 | clamp(30px, 4.1vw, 52px) / 1.04 / 800, tracking -.02em | Baloo 2 |
| subhead | 17px / 1.6 / 400 | Nunito |
| button | 19px / 1 / 800 | Baloo 2 |
| hand note beside button | 22px / 1.06 / 400, pen | Caveat |
| microcopy | 14px / 1.4 / 400, ink-soft | Nunito |
| trust line | 13.5px / 1.65 / 400, name at 15px 800, brokerage at 12.5px 700 caps | Nunito and Baloo 2 |
| value prop title | 19px / 1.2 / 800 | Baloo 2 |
| value prop body | 14.5px / 1.6 / 400 | Nunito |
| value prop numeral | 30px / 1 / 700, redpen | Caveat |
| closing strip hand line | 20px / 1.3 / 400, pen | Caveat |

---

## 4. Spacing, radii, rotation

**Spacing scale, in inches**, because the guide is a print object first:
`--s1 .06` `--s2 .10` `--s3 .16` `--s4 .24` `--s5 .34` `--s6 .50`

| measure | value |
|---|---|
| guide page trim | 8.5in x 11in |
| guide page padding | .40in top, .48in outer, .27in bottom, .40in gutter side |
| cover padding | .62in all round, .5in bottom |
| page 19 grid | 5.15in text column + .20in gutter + 1.95in margin lane |
| page 20 grid | 5.60in table column + .20in gutter + 1.52in margin lane |
| toolkit row, page 20 | 4.45in checklist + .20in + 2.50in phone card |
| body measure | 62 to 70 characters at 9.2pt |
| table row height | about .155in at 7.5pt with .019in cell padding |
| hero max width | 1180px, 44px / 40px padding, 40px column gap |
| hero grid | 1.06fr text, .94fr collage. Single column under 900px |

**Radii.** Almost none. Cards and stickers are square, because paper is square. The only rounded things are the numbered tokens and the geography chips (`.5in`, full pill), the button (44px), and the highlighter swipe, which uses an uneven `border-radius` so the swipe ends look hand pulled.

**Rotation budget.** Nothing rotates more than 4 degrees, and nothing that holds data rotates at all.

| object | rotation |
|---|---|
| tape strips | -9 to +5 deg |
| photo frames | -2.2 to +3.2 deg |
| sticky notes and cards | -1.1 to +0.9 deg |
| margin notes | -2 to +1.4 deg |
| **the table, the checklist text, the diagram** | **0 deg, always** |

At 375px all card rotations are reduced or zeroed so the stack does not look broken on a phone.

---

## 5. Print rules

- `@page { size: letter; margin: 0; }`, and `print-color-adjust: exact` on every element in the print block.
- Each `.page` gets `break-after: page` so panel B prints as two sheets, not a spread on one sheet. Verified: Chrome headless produces exactly three 8.5 x 11.0 pages.
- `break-inside: avoid` on `.aside`, `.notefound`, `.figure`, `.checkcard`, `.phones`, `.tablewrap`, `table.sid`, `.polaroid`, `.byline`, `.prop`, and on every `li`.
- `thead { display: table-header-group }` so the district table repeats its header if it ever splits.
- **No `position: fixed` anywhere in the guide panels.** Every annotation that is absolutely positioned is absolutely positioned inside its own page or lane, never inside the viewport. The landing panel is allowed `fixed` and does not currently use it.
- The preview surround, panel captions, and the landing hero are hidden at print.
- Bullets and checkboxes are flexbox rows with a fixed-basis marker span. There is no `li::before { position: absolute }` in this file.
- Table markup carries `<caption>`, `<th scope="col">`, `<th scope="row">`.
- Every `img` has real alt text. Every meaningful inline SVG has `role="img"` with a `<title>` and a `<desc>`. Purely decorative SVG (circles, arrows, the button ring) is `aria-hidden="true" focusable="false"`.
- **Meaning is never carried by color alone.** The two highlighted table rows also carry a solid `--redpen` inset bar on the row header, so they survive a grayscale print. NOT FOUND cells carry the literal words plus a dashed outline. Matured and Paid off cells carry the words in bold.

---

## 6. Measured page fit

Measured in a headless browser at the real 8.5in x 11in box, content bottom against the page bottom:

| page | slack |
|---|---|
| cover | 49px, about .51in |
| page 19 | 11px, about .11in |
| page 20 | 27px, about .28in |

Page 19 is the tightest page in the guide and it is at the limit. See `rationale.md` for what had to move to get there.
