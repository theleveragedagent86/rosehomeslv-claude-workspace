# Golden Hour, design tokens

Direction 2 of 6. Warm Throughout family.
All contrast ratios below were **computed with python3** against the WCAG 2.1 relative luminance
formula, not asserted. Two decimals. Every pair used in `preview.html` appears in the table.
**Minimum ratio in the system: 4.89. Every pair passes AA at its actual size and weight.**

---

## 1. Palette

| Token | Hex | Role |
|---|---|---|
| `--paper` | `#FDF8F1` | Page ground. Warm cream, the base of every guide page and the value prop band. |
| `--sand` | `#F2E3D0` | First elevation. Checklist panel, landing value prop cards, diagram bars. |
| `--row-tint` | `#F8EFE3` | Table zebra row. Deliberately half a step above `--sand` so it never fights the type. |
| `--clay-panel` | `#EBD3C2` | The protective panel. NOT FOUND callout, cover credibility strip, NOT FOUND pills. |
| `--rose-panel` | `#EFD9D3` | Aside panel. Dusty rose, used for the "why you never voted on it" pull. |
| `--sage-panel` | `#DEE4D5` | Cool relief. Geography pills, phone block, "Matured" and "Paid off" pills. |
| `--terracotta` | `#93401E` | Primary accent **for type**. Question labels, superscript source numerals, running heads. |
| `--ember` | `#A94E2B` | Primary accent **for fills and rules**. Title rule, folio, checkbox stroke, diagram bar. |
| `--clay-deep` | `#6E3018` | Deepest warm dark. All display type, table header ground, phone numbers. |
| `--sage` | `#48583F` | Secondary accent. Sage type on sage panels only. |
| `--rose-dark` | `#874A44` | Aside label type on the rose panel only. |
| `--ink` | `#33241D` | Body copy. Warm near black, never a pure neutral. |
| `--ink-muted` | `#655045` | Attribution, captions, source pointers, compliance line. |
| `--rule` | `#D9C3AE` | Hairline, 1px, structural. |
| `--rule-soft` | `#E7D6C4` | Hairline, 1px, decorative. |

### Duotone pigments, photography only

| Token | Hex | Role |
|---|---|---|
| `--duo-dark` (cover) | `#54210E` | Shadow end of the cover duotone, applied with `mix-blend-mode: lighten`. |
| `--duo-light` (cover) | `#F9DDAE` | Highlight end of the cover duotone, applied with `mix-blend-mode: multiply`. |
| `--duo-dark` (interior band, hero card, prop cards) | `#6B2E13` / `#7A3A1C` | Lighter shadow end so interior photography stays legible on paper. |
| `--duo-light` (interior) | `#FAE1B4` / `#FBE5BC` | Golden highlight end. |
| `--duo-dark` (landing background) | `#48180A` | Deepest, because a scrim rides on top of it. |
| `--duo-light` (landing background) | `#F3D5AE` | |

### Derived surfaces used for contrast math

| Token | Hex | How it was derived |
|---|---|---|
| `--hero-floor` | `#522F1F` | Worst case composite behind the landing headline: the **lightest** duotone value `#F3D5AE`, plus the sunwash at its local alpha, under the `.lp-scrim` at its weakest point in the text column (alpha 0.87). Real backgrounds are darker than this; the ratios below are the floor, not the average. |
| `--hero-chip` | `#6C4C3D` | `rgba(253,243,229,.15)` eyebrow pill composited over `--hero-floor`. |
| `--btn-face` | `#F6DFC0` | Button ground. |
| `--btn-hover` | `#FFF0DA` | Button hover ground. |
| `--btn-ink` | `#5A2412` | Button label. |

---

## 2. Computed WCAG contrast table

Threshold column shows the AA requirement for that exact size and weight
(3.0 for large text, defined as 24px and up, or 18.66px and up at weight 700+; otherwise 4.5).

| Pair | Hex on hex | Where it is used | Size / weight | Ratio | Needs | Result |
|---|---|---|---|---|---|---|
| `--ink` on `--paper` | #33241D on #FDF8F1 | Guide body prose, 8.3pt / 11.1px | 11.1px / 400 | 14.09 | 4.5 | PASS |
| `--ink` on `--paper` | #33241D on #FDF8F1 | Table data cells, 7.3pt / 9.7px | 9.7px / 400 | 14.09 | 4.5 | PASS |
| `--ink` on `--row-tint` | #33241D on #F8EFE3 | Table data cells on tinted row | 9.7px / 400 | 13.08 | 4.5 | PASS |
| `--ink` on `--sand` | #33241D on #F2E3D0 | Checklist steps, 7.8pt / 10.4px | 10.4px / 400 | 11.82 | 4.5 | PASS |
| `--ink` on `--clay-panel` | #33241D on #EBD3C2 | NOT FOUND callout body, 8.1pt / 10.8px | 10.8px / 400 | 10.37 | 4.5 | PASS |
| `--ink` on `--rose-panel` | #33241D on #EFD9D3 | Pull aside body, 8.1pt / 10.8px | 10.8px / 400 | 11.01 | 4.5 | PASS |
| `--ink` on `--sage-panel` | #33241D on #DEE4D5 | Phone block body, 7.4pt / 9.9px | 9.9px / 400 | 11.46 | 4.5 | PASS |
| `--ink` on `--paper` | #33241D on #FDF8F1 | Landing value prop body, 15px | 15px / 400 | 14.09 | 4.5 | PASS |
| `--ink` on `--sand` | #33241D on #F2E3D0 | Landing value prop body on card, 15px | 15px / 400 | 11.82 | 4.5 | PASS |
| `--ink-muted` on `--paper` | #655045 on #FDF8F1 | Inline attribution and source note, 6.8pt / 9.1px | 9.1px / 400 | 7.13 | 4.5 | PASS |
| `--ink-muted` on `--paper` | #655045 on #FDF8F1 | Figure caption, 6.5pt / 8.7px | 8.7px / 400 | 7.13 | 4.5 | PASS |
| `--ink-muted` on `--paper` | #655045 on #FDF8F1 | Cover compliance line, 7.4pt / 9.9px | 9.9px / 400 | 7.13 | 4.5 | PASS |
| `--ink-muted` on `--sand` | #655045 on #F2E3D0 | Checklist deck, 7.8pt / 10.4px | 10.4px / 400 | 5.98 | 4.5 | PASS |
| `--ink-muted` on `--paper` | #655045 on #FDF8F1 | Map card caption, 6.4pt / 8.5px | 8.5px / 800 | 7.13 | 4.5 | PASS |
| `--clay-deep` on `--paper` | #6E3018 on #FDF8F1 | Cover title, 45pt / 60px | 60px / 590 | 9.47 | 3.0 | PASS |
| `--clay-deep` on `--paper` | #6E3018 on #FDF8F1 | Question heads, 14pt / 18.7px | 18.7px / 600 | 9.47 | 4.5 | PASS |
| `--clay-deep` on `--sand` | #6E3018 on #F2E3D0 | Question head inside checklist panel, 14pt | 18.7px / 600 | 7.94 | 4.5 | PASS |
| `--clay-deep` on `--clay-panel` | #6E3018 on #EBD3C2 | NOT FOUND headline, 18pt / 24px | 24px / 560 | 6.97 | 3.0 | PASS |
| `--clay-deep` on `--sand` | #6E3018 on #F2E3D0 | Phone numbers, 12pt / 16px | 16px / 640 | 7.94 | 4.5 | PASS |
| `--clay-deep` on `--sage-panel` | #6E3018 on #DEE4D5 | Phone numbers on sage panel, 12pt / 16px | 16px / 640 | 7.70 | 4.5 | PASS |
| `--clay-deep` on `--paper` | #6E3018 on #FDF8F1 | Landing value prop headline, 23px | 23px / 590 | 9.47 | 3.0 | PASS |
| `--clay-deep` on `--sand` | #6E3018 on #F2E3D0 | Landing value prop headline on card, 23px | 23px / 590 | 7.94 | 3.0 | PASS |
| `--terracotta` on `--paper` | #93401E on #FDF8F1 | Superscript source numerals, 5.8pt / 7.7px | 7.7px / 800 | 6.64 | 4.5 | PASS |
| `--terracotta` on `--paper` | #93401E on #FDF8F1 | Value prop question label, 11px caps | 11px / 800 | 6.64 | 4.5 | PASS |
| `--terracotta` on `--paper` | #93401E on #FDF8F1 | Cover brokerage line, 8.4pt / 11.2px caps | 11.2px / 800 | 6.64 | 4.5 | PASS |
| `--terracotta` on `--clay-panel` | #93401E on #EBD3C2 | NOT FOUND callout label, 7.2pt / 9.6px caps | 9.6px / 800 | 4.89 | 4.5 | PASS |
| `--terracotta` on `--clay-panel` | #93401E on #EBD3C2 | NOT FOUND pill in table, 6.6pt / 8.8px | 8.8px / 800 | 4.89 | 4.5 | PASS |
| `--terracotta` on `--sand` | #93401E on #F2E3D0 | Superscript numerals inside checklist panel | 7.7px / 800 | 5.57 | 4.5 | PASS |
| `--terracotta` on `--paper` | #93401E on #FDF8F1 | Page 20 running head, 7.6pt / 10.1px caps | 10.1px / 800 | 6.64 | 4.5 | PASS |
| `--terracotta` on `--paper` | #93401E on #FDF8F1 | Soft close offer line, 9.6pt / 12.8px italic | 12.8px / 500 | 6.64 | 4.5 | PASS |
| `--ember` on `--paper` | #A94E2B on #FDF8F1 | Folio number, 15pt / 20px | 20px / 600 | 5.21 | 3.0 | PASS |
| `--sage` on `--paper` | #48583F on #FDF8F1 | Sage type on plain paper | 11.2px / 700 | 7.24 | 4.5 | PASS |
| `--sage` on `--sage-panel` | #48583F on #DEE4D5 | Geography pills, 8.4pt / 11.2px caps | 11.2px / 700 | 5.89 | 4.5 | PASS |
| `--sage` on `--sage-panel` | #48583F on #DEE4D5 | "Two numbers worth saving" label, 7.2pt caps | 9.6px / 800 | 5.89 | 4.5 | PASS |
| `--sage` on `--sage-panel` | #48583F on #DEE4D5 | "Matured" and "Paid off" pills, 6.9pt / 9.2px | 9.2px / 800 | 5.89 | 4.5 | PASS |
| `--rose-dark` on `--rose-panel` | #874A44 on #EFD9D3 | Pull aside label, 7.2pt / 9.6px caps | 9.6px / 800 | 5.02 | 4.5 | PASS |
| `--paper` on `--clay-deep` | #FDF8F1 on #6E3018 | Table header row, 6.9pt / 9.2px caps | 9.2px / 800 | 9.47 | 4.5 | PASS |
| `--paper` on `--ember` | #FDF8F1 on #A94E2B | Diagram assessment bar label | 11px / 800 | 5.21 | 4.5 | PASS |
| `--cream-hi` on `--hero-floor` | #FFF7EC on #522F1F | Landing headline, 57px | 57px / 570 | 11.07 | 3.0 | PASS |
| `--cream-sub` on `--hero-floor` | #F1DCC4 on #522F1F | Landing subhead, 17.5px | 17.5px / 400 | 8.84 | 4.5 | PASS |
| `--cream-trust` on `--hero-floor` | #EBD5BC on #522F1F | Landing trust line, 13.5px | 13.5px / 400 | 8.28 | 4.5 | PASS |
| `--cream-micro` on `--hero-floor` | #E7CEB2 on #522F1F | Button microcopy, 14px | 14px / 400 | 7.77 | 4.5 | PASS |
| `--gold-hi` on `--hero-floor` | #F6C99B on #522F1F | "Real Broker, LLC" in the trust line, 12px caps | 12px / 800 | 7.70 | 4.5 | PASS |
| `--cream` on `--hero-chip` | #FDF3E5 on #6C4C3D | Landing eyebrow pill, 12px caps | 12px / 700 | 6.98 | 4.5 | PASS |
| `--cream` on `--hero-floor` | #FDF3E5 on #522F1F | Cover eyebrow and interior running head | 11.5px / 700 | 10.72 | 4.5 | PASS |
| `--btn-ink` on `--btn-face` | #5A2412 on #F6DFC0 | Button label, 17px | 17px / 800 | 9.57 | 4.5 | PASS |
| `--btn-ink` on `--btn-hover` | #5A2412 on #FFF0DA | Button label on hover, 17px | 17px / 800 | 11.04 | 4.5 | PASS |

**All pairs PASS. Lowest ratio in the system: 4.89** (`--terracotta` on `--clay-panel`, which is the
NOT FOUND label and the NOT FOUND pill, both small bold caps). Nothing was tuned after the fact:
`--terracotta` was darkened from a first draft of `#A94E2B` to `#93401E` specifically so that this
pair cleared 4.5 at small size, and `--ember` was kept as the lighter of the two for fills only.

**No meaning is carried by color alone anywhere.** The NOT FOUND cell always prints the words
NOT FOUND. The retired districts always print "Matured" or "Paid off June 1, 2025". The special
assessment layer in the diagram is both outside the dotted box and labelled "Billed separately.
Outside the box."

---

## 3. Type

### Google Fonts URL, exactly as used

```html
<link href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,300..900;1,300..900&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,300..900,0..100,0..1;1,9..144,300..900,0..100,0..1&display=swap" rel="stylesheet">
```

### Pairing

**Fraunces** (variable: `opsz`, `wght`, `SOFT`, `WONK`) for display and voice.
It is a warm old style serif with a soft axis and a wonky axis, so the same family can be
generous and rounded at large sizes and quiet at small ones. `WONK 1` turns on the swashed
`g` and `y`, which is what stops the guide reading like a legal notice.

**Figtree** for body, labels, tables, and interface.
A soft geometric sans with a tall x height and open apertures. It sets small and stays legible
at 7.3pt in the district table.

Neither face was in the rejected round. Neither is a cold grotesque.

### Scale

| Role | Family | Size | Line | Variation | Tracking |
|---|---|---|---|---|---|
| Cover title | Fraunces | 45pt | 0.99 | `opsz 144, wght 590, SOFT 32, WONK 1` | -0.03em |
| Landing headline | Fraunces | 57px | 1.02 | `opsz 144, wght 570, SOFT 36, WONK 1` | -0.032em |
| Spread headline | Fraunces | 31pt | 1.00 | `opsz 120, wght 560, SOFT 44, WONK 1` | -0.028em |
| NOT FOUND headline | Fraunces | 18pt | 1.06 | `opsz 72, wght 560, SOFT 56, WONK 1` | -0.022em |
| Landing prop headline | Fraunces | 23px | 1.12 | `opsz 48, wght 590, SOFT 44, WONK 1` | -0.022em |
| Byline name | Fraunces | 17pt | 1.10 | `opsz 48, wght 600, SOFT 30, WONK 0` | -0.015em |
| Question head | Fraunces | 14pt | 1.14 | `opsz 36, wght 600, SOFT 50, WONK 1` | -0.018em |
| Phone number | Fraunces | 12pt | 1.00 | `opsz 36, wght 640, SOFT 30, WONK 0` | -0.01em |
| Credibility strip | Fraunces italic | 11.5pt | 1.40 | `opsz 24, wght 460, SOFT 60, WONK 0` | 0 |
| Soft close offer | Fraunces italic | 9.6pt | 1.34 | `opsz 30, wght 500, SOFT 60, WONK 1` | 0 |
| Table row label | Fraunces | 7.9pt | 1.20 | `opsz 14, wght 700, SOFT 30, WONK 0` | 0 |
| Cover subtitle | Figtree | 12pt | 1.62 | 400 | 0 |
| Landing subhead | Figtree | 17.5px | 1.65 | 400 | 0 |
| Landing prop body | Figtree | 15px | 1.62 | 400 | 0 |
| Deck on photo | Figtree | 9.6pt | 1.50 | 400 | 0 |
| Guide body | Figtree | 8.3pt | 1.45 | 400 | 0 |
| Pull aside body | Figtree | 8.1pt | 1.46 | 400 | 0 |
| NOT FOUND body | Figtree | 8.1pt | 1.45 | 400 | 0 |
| Numbered list | Figtree | 8.2pt | 1.42 | 400, bold lead in at 750 | 0 |
| Checklist step | Figtree | 7.8pt | 1.38 | 400, bold lead in at 750 | 0 |
| Table data | Figtree | 7.3pt | 1.20 | 400 | 0 |
| Table header | Figtree | 6.9pt | 1.20 | 800 caps | 0.13em |
| Question label caps | Figtree | 7.2pt | 1.35 | 800 caps | 0.15em to 0.18em |
| Running head | Figtree | 7.6pt | 1.00 | 800 caps | 0.24em |
| Inline attribution | Figtree | 6.8pt | 1.45 | 400 | 0.02em |
| Figure caption | Figtree | 6.5pt | 1.42 | 400 | 0 |
| Source pointer | Figtree | 6.8pt | 1.50 | 400 | 0 |
| Superscript numeral | Figtree | 5.8pt | 0 | 800 | 0.02em |

---

## 4. Spacing, radii, grid

### Spacing scale
`--s1 4px`, `--s2 8px`, `--s3 12px`, `--s4 18px`, `--s5 26px`, `--s6 38px`, `--s7 54px`,
`--s8 76px`, `--s9 104px`.
Inside the guide pages, spacing is expressed in inches so it survives print scaling:
`.02in .055in .07in .09in .12in .18in .26in .36in .48in`.

### Radii
`--r-sm 8px` (table header caps), `--r-md 16px` (inner chips), `--r-lg 26px`
(asides, phone block, map card, prop cards), `--r-xl 40px` (photo band, cover card, NOT FOUND
callout, checklist panel, landing hero card, value prop band), `--r-pill 999px`
(geography pills, NOT FOUND pills, button, list numerals).
**Big soft radii are the direction.** Nothing in the system is a hard cornered box.

### Page grid
- Trim: 8.5in x 11in. Live margin: **0.52in** left and right on interior pages, **0.55in** on the cover.
- Photo band on an interior opener: inset `.36in .48in .18in`, height **1.5in**, radius `--r-xl`.
- Body engine: **two columns, 0.3in gutter** using CSS `column-count`. Full width objects
  (callouts, tables, panels, figures) break out of the column flow.
- Cover photo is full bleed. The cover card floats `0.55in` from left, right, and bottom.

### Print rules
```css
@page { size: letter; margin: 0; }
* { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
thead { display: table-header-group; }
.aside, .notfound, .tablewrap, .checkblock, .phones, .figure,
.numlist li, table.sid tr { break-inside: avoid; page-break-inside: avoid; }
.page { break-after: page; }
```
- **No `position: fixed` anywhere in the guide panels.** The landing panel does not use it either.
- Bullets and checkboxes are **flex children in the markup** (`<span class="n">`, `<span class="box">`).
  There is no `li::before { position: absolute }` in this file.
- Every table carries a visible `<caption>`, `<th scope="col">` on all four headers and
  `<th scope="row">` on the district number.
- Both inline SVGs carry `role="img"`, `<title id>` and `<desc id>` wired through `aria-labelledby`.
  The decorative sun arc marks carry `aria-hidden="true"`.
- Verified: headless Chrome print produces exactly **3 pages at 8.5 x 11 in**, colors intact,
  landing panel and preview chrome suppressed.
