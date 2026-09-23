# Direction 6: Sunrise to Sunset, design tokens

**Thesis.** The book moves through a day. Bright and open at the start, deeper and calmer by the end.
The palette is a single continuous arc from first light to night. Nothing in the system is a neutral
gray. Every value is a time of day.

---

## 1. Palette

Every token is one position on the arc. Read the table top to bottom and you are reading the book
front to back.

### The light end of the day

| token | hex | role |
|---|---|---|
| `--paper` | `#FFFCF6` | First light. Base paper for the front half of the guide and the top of every page. |
| `--wash-morning` | `#FFEFDD` | Mid morning wash. Tinted panels in the front half, hero value prop 1. |
| `--wash-noon` | `#FBDCB4` | Full sun. The darkest point of the page 19 ground, and the NOT FOUND chip field. |
| `--panel` | `#FFF7EC` | The lit window. Inverted ivory panel used for the table and the checklist on dark grounds. |
| `--panel-alt` | `#FFF1E0` | Zebra row inside a lit panel. Deliberately near invisible. |

### The colour of the day

| token | hex | role |
|---|---|---|
| `--sky-dawn` | `#9EC4DE` | The one cool value in the system. Dawn sky. Asides, the "fair question" panel, the Las Vegas chip. |
| `--amber` | `#F2A03D` | Golden hour. Value prop 2 field, phone number pills, all accents on dark grounds, the brokerage rule. |
| `--ember` | `#C9451B` | Sunset. Fills only: table header, step numerals, the NOT FOUND callout border, the hero button, chips. Also the cover title accent at display size. |
| `--ember-ink` | `#AE3813` | Sunset for **small text on warm grounds**. Never use `--ember` for text under 18pt. This token exists solely to hold AA. |
| `--rose-dusk` | `#93304F` | Afterglow. The phone block field on page 20 and the second stop of the gutter horizon. |

### The dark end of the day

| token | hex | role |
|---|---|---|
| `--indigo-dusk` | `#3A2A63` | Dusk. Figure number tags, MATURED chip text, and the lightest stop of the page 20 ground. |
| `--indigo-night` | `#1E1442` | Night. The cover footer, hero value prop 3, and the darkest stop of the page 20 ground. |

### Ink

| token | hex | role |
|---|---|---|
| `--ink` | `#2B1F30` | Warm plum near black. All body copy on light grounds. Never pure black. |
| `--ink-soft` | `#6A5350` | Warm brown gray. Inline attributions, captions, legends, microcopy. |
| `--on-dark` | `#FDF3E6` | Warm ivory. Body copy on indigo and rose grounds. Never pure white for prose. |
| `--on-dark-soft` | `#CFBFD6` | Lavender cream. Secondary copy on indigo. |
| `--on-rose-soft` | `#F0D9DE` | Secondary copy on the rose field only. |

### Rules and gradients

| token | value | role |
|---|---|---|
| `--rule-warm` | `#E3CFB4` | Hairline on light grounds, low contact. |
| `--rule-warm-2` | `#D8BF9E` | Hairline on light grounds, structural (running head, figure top). |
| `--rule-dark` | `rgba(253,243,230,.26)` | Hairline on indigo grounds. |
| page 19 ground | `linear-gradient(158deg, #FFFDF9 0%, #FFFAF0 26%, #FFF1DF 52%, #FEE3C2 76%, #FBDCB4 100%)` | The day falling across the page, top left to bottom right. |
| page 20 ground | `linear-gradient(158deg, #4A3573 0%, #3A2A63 24%, #2C1F58 54%, #22174B 78%, #1A1140 100%)` | Continues the same 158 degree fall. Top left is the lightest so the two pages read as one. |
| horizon right, p19 | `linear-gradient(180deg, #F9C97F, #F2A03D 26%, #C9451B 62%, #93304F 100%)`, 0.17in wide | The sun sets in the gutter. Signature device. |
| horizon left, p20 | `linear-gradient(180deg, #93304F, #6C2A55 34%, #43265F 68%, #2A1B50 100%)`, 0.17in wide | Picks the horizon up on the other side. |
| cover sky | `linear-gradient(178deg, #FFFCF6, #FFFCF6 22%, #FFEFDD 56%, #FBDCB4 84%, #F6C88E 100%)` | `#F6C88E` carries no text. It exists only to hand off to the photograph. |

**Off brand, confirmed.** Rose Homes navy `#1C2333`, champagne `#C9A86E`, and off white `#F7F5F0`
appear nowhere in this system. Grep the preview for those three strings and you get zero hits.

---

## 2. Computed WCAG contrast

Every pair below is a pair that actually appears in `preview.html`. Ratios computed with python3 to
two decimals against the WCAG 2.1 relative luminance formula, not asserted. Threshold is 4.50 for
normal text and 3.00 for large text, where large means 18pt or 14pt bold and up.

| foreground | background | where it is used | size | weight | ratio | AA |
|---|---|---|---|---|---|---|
| `#2B1F30` | `#FFFCF6` | p19 body prose | 8.7pt | 400 | **15.29** | PASS |
| `#2B1F30` | `#FBDCB4` | p19 body over the darkest point of the page gradient | 8.7pt | 400 | **11.93** | PASS |
| `#2B1F30` | `#FFF7EC` | district table cell on the lit panel | 8pt | 400 | **14.74** | PASS |
| `#2B1F30` | `#FFF1E0` | district table zebra row | 8pt | 400 | **14.10** | PASS |
| `#2B1F30` | `#FFF9F0` | NOT FOUND callout body, light end | 8.1pt | 400 | **14.95** | PASS |
| `#2B1F30` | `#FFE9D2` | NOT FOUND callout body, dark end | 8.1pt | 400 | **13.30** | PASS |
| `#2B1F30` | `#9EC4DE` | aside body on dawn blue | 8pt | 400 | **8.50** | PASS |
| `#2B1F30` | `#F2A03D` | phone number pill; hero value prop 2 body | 8.2pt / 14.5px | 800 / 300 | **7.36** | PASS |
| `#6A5350` | `#FFFCF6` | inline attribution on p19; cover credibility line | 6.5pt / 9.6pt | 500 | **6.91** | PASS |
| `#6A5350` | `#FBDCB4` | inline attribution over the darkest ground | 6.5pt | 500 | **5.39** | PASS |
| `#6A5350` | `#FFF7EC` | table caption and NOT FOUND legend | 5.9pt | 500 | **6.66** | PASS |
| `#6A5350` | `#FFF4E6` | hero microcopy and trust meta | 12.5px | 400 | **6.52** | PASS |
| `#AE3813` | `#FFFCF6` | p19 running head caps; section kickers | 7pt | 700 | **6.08** | PASS |
| `#AE3813` | `#FBDCB4` | running head over the darkest ground; NOT FOUND chip | 7pt / 6pt | 700 | **4.74** | PASS |
| `#AE3813` | `#FFF7EC` | checklist step label; lit panel tag | 7.2pt | 700 | **5.86** | PASS |
| `#AE3813` | `#FFE9D2` | NOT FOUND callout closing line | 8.1pt | 600 | **5.29** | PASS |
| `#AE3813` | `#FFEFDD` | hero value prop 1 time label | 10.5px | 700 | **5.52** | PASS |
| `#AE3813` | `#FFF4E6` | hero eyebrow | 11px | 700 | **5.73** | PASS |
| `#FFFFFF` | `#C9451B` | table header; step numerals; callout kicker; hero button; Figure 4 label | 5.9pt to 16px | 700 / 400 | **4.83** | PASS |
| `#FFFFFF` | `#3A2A63` | Figure 4 number tag | 6pt | 700 | **12.42** | PASS |
| `#3A2A63` | `#E4DCEF` | MATURED and PAID OFF chip | 6pt | 700 | **9.33** | PASS |
| `#3A2A63` | `#FBDCB4` | Figure 4 tick label on the page ground | 8px | 400 | **9.46** | PASS |
| `#FDF3E6` | `#4A3573` | p20 body at the lightest point of the ground | 8.5pt | 400 | **9.35** | PASS |
| `#FDF3E6` | `#1E1442` | p20 body at the darkest point of the ground | 8.5pt | 400 | **15.51** | PASS |
| `#CFBFD6` | `#4A3573` | p20 folio note and soft close body | 6.4pt | 400 | **5.90** | PASS |
| `#CFBFD6` | `#1E1442` | hero value prop 3 body; cover compliance line | 14.5px / 6.9pt | 300 / 400 | **9.79** | PASS |
| `#F2A03D` | `#4A3573` | p20 running head and folio numeral | 7pt | 700 | **4.82** | PASS |
| `#F2A03D` | `#1E1442` | hero value prop 3 time label; cover brokerage lockup | 10.5px / 9.4pt | 700 | **8.00** | PASS |
| `#FFFFFF` | `#93304F` | phone block heading and organisation names | 7.2pt to 9.6pt | 700 | **7.56** | PASS |
| `#F0D9DE` | `#93304F` | phone block descriptions and source refs | 6.6pt | 400 | **5.65** | PASS |
| `#2B1F30` | `#FFEFDD` | Figure 4 stack label; hero value prop 1 body | 8.6px / 14.5px | 400 | **13.90** | PASS |
| `#2B1F30` | `#FDE2C2` | Figure 4 stack label | 8.6px | 400 | **12.55** | PASS |
| `#2B1F30` | `#F7CE9A` | Figure 4 stack label | 8.6px | 400 | **10.62** | PASS |
| `#2B1F30` | `#F2BE80` | Figure 4 stack label | 8.6px | 400 | **9.28** | PASS |
| `#2B1F30` | `#FFFDF9` | cover title; hero headline | 58pt / 50px | 500 / 600 | **15.41** | PASS |
| `#C9451B` | `#FFFCF6` | cover title accent; hero headline accent | 58pt / 50px | 500 / 700 | **4.71** | PASS |
| `#FDF3E6` | `#1E1442` | cover byline on the night footer | 20pt | 600 | **15.51** | PASS |
| `#2B1F30` | `#9EC4DE` | cover Las Vegas chip | 7.6pt | 700 | **8.50** | PASS |

**Minimum ratio anywhere in the system: 4.71. Zero FAIL.**

Two pairs failed on the first pass and were fixed rather than waived:

1. `#AE3813` on `#FBD2A0` measured **4.39**. The page 19 gradient was ending too deep. The final stop
   was lightened to the existing `--wash-noon` token `#FBDCB4`, which lands the same pair at **4.74**.
   This also removed an off system hex.
2. `#FFE7D6` on `#C9451B` in the Figure 4 sub label measured **4.06**. Changed to `#FFFFFF`, **4.83**.

A third pair, `--amber` on `--rose-dusk`, measured **3.56** and was never shipped. The source
reference numerals inside the phone block use `--on-rose-soft` at **5.65** instead.

---

## 3. Type

**Google Fonts, one request, two families:**

```
https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1&family=Onest:wght@100..900&display=swap
```

### Fraunces, display

Chosen for the brief's requirement of real optical range. Fraunces is a variable face with four axes.
`opsz` lets the same family be delicate at 58pt on a cover and sturdy at 10pt in a panel heading.
`SOFT` rounds the terminals, which is the single most important warmth lever in the whole system.
`WONK` swaps in the alternate wonky italic-flavoured shapes on `g`, `y` and `w`, which is what stops
this reading as a luxury serif.

Standing settings by role:

| role | size | weight | `opsz` | `SOFT` | `WONK` | tracking | leading |
|---|---|---|---|---|---|---|---|
| cover title | 58pt | 500, accent line 700 | 144 | 40 | 1 | -0.03em | 0.96 |
| hero headline | clamp(32px, 3.4vw, 50px) | 600, accent 700 | 144 | 38 | 1 | -0.03em | 1.02 |
| page question head | 24.5pt | 600 | 72 | 36 | 1 | -0.026em | 1.04 |
| NOT FOUND callout head | 17.5pt | 700 | 60 | 44 | 1 | -0.022em | 1.04 |
| section subhead | 13pt | 600 | 36 | 30 | 1 | -0.012em | 1.08 |
| pull line, "Same master plan" | 11.6pt | 600 | 36 | 34 | 1 | 0 | 1.16 |
| panel heading, lit and phone | 9.6 to 10.4pt | 600 | 24 to 30 | 28 to 30 | 1 | 0 | 1.1 |
| aside heading | 10.6pt | 600 | 30 | 34 | 1 | 0 | 1.12 |
| cover byline | 20pt | 600 | 48 | 30 | 1 | 0 | 1.0 |
| folio numeral | 12pt | 600 | 30 | 0 | 0 | 0 | 1.0 |

### Onest, text and interface

Chosen against Schibsted Grotesk and General Sans because Onest has slightly rounder terminals and a
taller x height, which is what keeps 8pt table text legible while still feeling friendly. It never
reads like a spec sheet.

| role | size | weight | leading |
|---|---|---|---|
| deck | 10.6pt | 300 | 1.38 |
| p19 body prose | 8.7pt | 400 | 1.44 |
| p20 body prose | 8.5pt | 400 | 1.46 |
| p20 intro | 9.2pt | 300 | 1.42 |
| NOT FOUND callout body | 8.1pt | 400, close line 600 | 1.44 |
| aside body | 8pt | 400 | 1.42 |
| numbered step body | 8.1pt | 400, label 700 | 1.40 |
| checklist body | 7.2pt | 400, label 700 | 1.36 |
| district table cell | 8pt | 400, district numeral 700 | 1.15 |
| district table header | 5.9pt | 700, 0.10em, caps | 1.0 |
| table caption and legend | 5.9pt | 500 | 1.30 to 1.34 |
| inline attribution | 6.5pt | 500 | inherits |
| source superscript | 5.6pt | 700 | 0 |
| running head | 7pt | 700, 0.20em, caps | 1.0 |
| time of day label | 6.6pt | 700, 0.18em, caps | 1.0 |
| chips and status pills | 6 to 7.6pt | 700, 0.10 to 0.13em, caps | 1.0 |
| hero subhead | 17px | 300, emphasis 600 | 1.62 |
| hero button | 16px | 700 | 1.0 |
| hero value prop body | 14.5px | 300 | 1.60 |
| trust lockup name | 13px | 800, 0.13em, caps | 1.2 |

**Rule.** Fraunces never sets more than three lines in a row. Onest never sets a display line. If a
heading needs to be quiet, drop its `SOFT` toward 20 rather than switching family.

---

## 4. Spacing, radii, layout

**Scale**, 4pt base, exposed as custom properties: `4 · 8 · 12 · 16 · 22 · 30 · 40 · 54`. Everything
between elements is drawn from this or from a documented optical exception in the 5 to 11pt range
inside dense panels.

**Radii:** `--r-sm 3pt` chips and tags, `--r-md 7pt` phone and aside panels, `--r-lg 14pt` lit panels
and the NOT FOUND callout, `--r-pill 999px` chips, buttons, status pills.

**Page grid.**

| | page 19 | page 20 |
|---|---|---|
| trim | 8.5in by 11in | 8.5in by 11in |
| margins | 0.44 top, 0.40 outer, 0.34 bottom, 0.58 gutter | 0.44 top, 0.40 outer, 0.30 bottom, 0.58 gutter |
| horizon strip | 0.17in on the right edge | 0.17in on the left edge |
| body columns | 2 at 0.26in gutter | 1 full width above the table, 2 at 0.24in below |
| full bleed objects | NOT FOUND callout, Figure 4 | lit table panel |

**Landing page.** Two column hero at `1.12fr .88fr`, three equal value prop cards below. Single
breakpoint at 860px. Below it the photo moves above the copy with `order:-1`, the value props stack,
and the button goes full width.

---

## 5. Print rules

- `@page { size: letter; margin: 0 }`.
- `print-color-adjust: exact` and `-webkit-print-color-adjust: exact` on every page box and, inside
  `@media print`, on `*`. The whole direction is colour dependent.
- `break-inside: avoid` and `page-break-inside: avoid` on the lit panels, the NOT FOUND callout, the
  aside, the phone block, the figure, the table, the soft close, and every `li` in both lists.
- `thead { display: table-header-group }` so a table that ever does split repeats its header.
- **No `position: fixed` anywhere in the guide panels.** Verified: zero occurrences in the file. The
  horizon strips and the cover footer use `position: absolute` inside a `position: relative` page box,
  which does not repeat.
- **Bullets and checkboxes are flexbox**, `display:flex` with a `flex:none` marker span. There is no
  `li::before { position: absolute }` in this file. Verified: zero occurrences.
- Direct children of both page boxes carry `flex: 0 0 auto` so nothing can silently compress to fit.
  If content overruns, it overruns visibly and gets fixed, it does not quietly shrink.
- Page boxes carry `flex: 0 0 auto` in the preview so paper never squashes at narrow viewport widths.

## 6. Accessibility

- Both photographs carry descriptive alt text naming the place and the light.
- All six functional inline SVGs carry `role="img"` plus `<title>` and `<desc>`. Figure 4's `<desc>`
  describes the whole diagram in prose, including the fact that no dollar figures appear in it.
- The cover arc and the horizon strips are decorative and carry `aria-hidden="true"`.
- The district table has a `<caption>`, `scope="col"` on all four headers, and a `<colgroup>`.
- Nothing encodes meaning in colour alone. The NOT FOUND chip says NOT FOUND. The MATURED chip says
  MATURED. The reader path indicator has a written label next to its three dots. The escrow diagram
  labels every band in words.
- The hero button has hover, focus-visible with a 3px `--indigo-dusk` outline at 3px offset, and
  active states. Only `transform`, `opacity`, `box-shadow` and `background-color` are transitioned.
  There is no `transition: all`.
