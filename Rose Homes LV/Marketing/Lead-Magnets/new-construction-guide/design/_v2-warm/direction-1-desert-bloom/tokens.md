# Desert Bloom, design tokens

Direction 1 of 6. Warm Throughout family.
**Thesis:** the Pozek energy translated to the Mojave. Sunbaked, saturated, and cheerful the whole way through.

All ratios below were computed with `python3` against the WCAG 2.1 relative luminance formula, not asserted. Two decimals. Nothing in this direction ships at a FAIL.

---

## 1. Palette

| Token | Hex | Role |
|---|---|---|
| `--sand` | `#FDF4E3` | the paper. Full bleed on every page of the guide and the landing background. |
| `--sand-2` | `#F7E7C9` | second surface. Table zebra, quiet cards, the map card ground. |
| `--sand-3` | `#F2D9AE` | third surface. Hairlines, the term bar ground in SVG-04, landing rules. |
| `--ink` | `#2A1712` | warm near black. All body text, the soft close strip, the brokerage lockup. |
| `--ink-soft` | `#6E4632` | warm brown. Inline attributions, captions, folio notes, landing subhead. |
| `--white` | `#FFFFFF` | reversed type on the four saturated solids, checkbox interiors. |
| `--magenta` | `#C21A63` | prickly pear. The loud one. NOT FOUND callout, table header band, folio 19, landing button. |
| `--magenta-d` | `#9E1450` | prickly pear, text weight. Question subheads, table row headers, map chips. |
| `--magenta-tint` | `#FBDFEA` | prickly pear at card weight. Landing value prop 1. |
| `--coral` | `#E2542B` | sunset. Borders, the I-15 ribbon, block fills in SVG-04. |
| `--coral-d` | `#C6421C` | sunset, text weight. Edition label, pull quote accent, NOT FOUND pill rule. |
| `--coral-tint` | `#FBE3D6` | sunset at card weight. The "any with none at all" card, NOT FOUND cell pills. |
| `--turq` | `#0E7C8A` | spring water. Solid cards, folio 20, landing eyebrow chip. |
| `--turq-d` | `#0A616D` | spring water, text weight. Question subheads, 215 shield, retired-district rule. |
| `--turq-tint` | `#DCF0F0` | spring water at card weight. Matured and Paid off cell pills. |
| `--yellow` | `#FFC42E` | sunshine. Chips, the credibility band, the NOT FOUND ribbon, the grayscale tell. |
| `--yellow-tint` | `#FFEDBE` | sunshine at card weight. The checklist card, the valley floor in the map. |
| `--cactus` | `#3F7A4E` | one green. Map hill and golf flag only. Never carries text. |

**Rules of use.** Four saturated solids exist: magenta, coral-d, turquoise, ink. Reversed type only ever sits on those four. Coral `#E2542B` is a fill for graphics, never a background for small type, and never a text color on paper. Every tint card carries `--ink` type.

---

## 2. Computed contrast, every pair actually used

WCAG AA. Normal text needs 4.50. Large text (18pt regular or 14pt bold and up) needs 3.00.

| fg | bg | where | size and weight | ratio | needs | result |
|---|---|---|---|---|---|---|
| `#2A1712` | `#FDF4E3` | guide body text on paper | 8.5pt regular | **15.63** | 4.5 | PASS |
| `#2A1712` | `#FDF4E3` | table cell, odd row is paper | 7.6pt regular | **15.63** | 4.5 | PASS |
| `#2A1712` | `#F7E7C9` | table cell, even row is sand-2 | 7.6pt regular | **14.01** | 4.5 | PASS |
| `#2A1712` | `#F2D9AE` | term bar ground in SVG-04 | 7.5pt bold | **12.45** | 4.5 | PASS |
| `#6E4632` | `#FDF4E3` | inline attribution, figure caption, table caption, folio note | 6.6pt bold | **7.44** | 4.5 | PASS |
| `#6E4632` | `#F7E7C9` | attribution inside the sand map card | 6.6pt bold | **6.66** | 4.5 | PASS |
| `#9E1450` | `#FDF4E3` | question subhead q-magenta, table row header | 7.8pt bold caps | **7.20** | 4.5 | PASS |
| `#C21A63` | `#FDF4E3` | "Often that somebody is you." lead hit | 10.4pt bold | **5.31** | 4.5 | PASS |
| `#C21A63` | `#FDF4E3` | cover title accent, "Model Home" | 53pt bold | **5.31** | 3.0 | PASS |
| `#0A616D` | `#FDF4E3` | question subhead q-turq, SVG-04 escrow label | 8.6pt bold caps | **6.53** | 4.5 | PASS |
| `#C6421C` | `#FDF4E3` | edition label, pull quote accent | 8.0pt bold caps | **4.58** | 4.5 | PASS |
| `#2A1712` | `#FFC42E` | yellow chip, kicker, NOT FOUND ribbon, credibility band | 7.2pt bold caps | **10.72** | 4.5 | PASS |
| `#2A1712` | `#FFEDBE` | checklist card, prepayment card | 7.7pt regular | **14.73** | 4.5 | PASS |
| `#2A1712` | `#FBE3D6` | coral card body, NOT FOUND cell pill | 6.6pt bold caps | **13.87** | 4.5 | PASS |
| `#2A1712` | `#DCF0F0` | Matured and Paid off cell pills | 6.6pt bold caps | **14.45** | 4.5 | PASS |
| `#2A1712` | `#FBDFEA` | landing value prop 1 card | 13px regular | **13.70** | 4.5 | PASS |
| `#2A1712` | `#E2542B` | property tax block label in SVG-04 | 9px bold | **4.50** | 4.5 | PASS |
| `#FFFFFF` | `#C21A63` | NOT FOUND callout body, table header band, folio 19, landing button | 8.5pt regular | **5.80** | 4.5 | PASS |
| `#FFEDBE` | `#C21A63` | NOT FOUND callout kicker line | 8.5pt bold | **5.00** | 4.5 | PASS |
| `#FFFFFF` | `#0E7C8A` | turquoise card body and subhead, folio 20, landing eyebrow chip | 8.4pt regular | **4.92** | 4.5 | PASS |
| `#FFFFFF` | `#0A616D` | 215 shield in the valley map, sub association block | 8px bold | **7.13** | 4.5 | PASS |
| `#FFFFFF` | `#C6421C` | Henderson chip, 15 shield, prop 3 icon tile | 8.4pt bold caps | **5.00** | 4.5 | PASS |
| `#FDF4E3` | `#2A1712` | soft close strip, brokerage lockup, cover wordmark pill | 8.0pt regular | **15.63** | 4.5 | PASS |
| `#FFC42E` | `#2A1712` | soft close emphasis, term tick, SVG-04 note | 8.0pt bold | **10.72** | 4.5 | PASS |
| `#9E1450` | `#FDF4E3` | map place chips, Summerlin and Henderson | 8px bold | **7.20** | 4.5 | PASS |
| `#0A616D` | `#FDF4E3` | map place chip, Skye Canyon | 8px bold | **6.53** | 4.5 | PASS |
| `#C6421C` | `#FDF4E3` | map place chip, North LV | 8px bold | **4.58** | 4.5 | PASS |
| `#FFFFFF` | `#513127` | page 19 headline over photo, worst case composite | 27pt bold | **11.55** | 3.0 | PASS |
| `#FDF4E3` | `#614D39` | landing photo caption over scrim, worst case composite | 12px bold caps | **7.31** | 4.5 | PASS |

**Minimum ratio in the whole system: 4.50. Fails: none.**

### How the two over-photo pairs were computed

Text over a photograph cannot be asserted, so both were computed against the **worst case a pure white photograph** would produce after the tint layers.

- **Page 19 headline.** White photo, then the multiply tone `rgba(158,20,80,.74)`, then the scrim `rgba(42,23,18,.58)`. Composite is `#513127`. White on `#513127` is **11.55**.
- **Landing photo caption.** White photo, then the multiply tone `rgba(255,196,46,.42)`, then the top scrim `rgba(42,23,18,.74)`. Composite is `#614D39`. Sand on `#614D39` is **7.31**.

If either scrim is ever reduced, recompute. The landing scrim was raised from `.58` to `.74` specifically because `.58` computed to 4.07 and failed.

### Colors that were tested and rejected

| pair | ratio | verdict |
|---|---|---|
| `#FFC42E` on `#0E7C8A` | 3.09 | rejected. Yellow type on solid turquoise. Replaced with white. |
| `#FFC42E` on `#C21A63` | 3.64 | rejected. Yellow type on solid magenta. Replaced with `#FFEDBE`. |
| `#FFEDBE` on `#0E7C8A` | 4.24 | rejected. Still short of 4.50. |
| `#C6421C` on `#FBE3D6` | 4.06 | rejected. Coral type on its own tint. Replaced with ink. |
| `#E2542B` on `#FDF4E3` | 3.47 | rejected as a text color anywhere. Coral is a fill only. |
| `#0E7C8A` on `#F7E7C9` | 4.04 | rejected. Turquoise type on sand-2. Use `--turq-d`. |

---

## 3. Type

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Nunito+Sans:ital,opsz,wght@0,6..12,300..1000;1,6..12,300..1000&display=swap" rel="stylesheet">
```

- **Display: Fraunces.** Variable, with `SOFT` and `WONK` pushed on. Soft ball terminals and the wonky italic-ish `g` are what make it cheerful rather than editorial. Set with `font-variation-settings:"SOFT" 45,"WONK" 1,"opsz" <size>`.
- **Text: Nunito Sans.** Humanist, round-shouldered, high x-height, holds up at 7.6pt on paper. Optical size axis set by the browser.
- Neither face was used in the rejected round. Neither is Playfair, Montserrat, Bebas, Barlow Condensed, IBM Plex, Newsreader, Source Serif 4, Public Sans, or Instrument Sans.

### Guide scale, points, print 1:1

| role | face | size / leading | tracking | notes |
|---|---|---|---|---|
| Cover title | Fraunces 900 | 53 / 0.94 | -0.024em | `SOFT 45 WONK 1 opsz 120` |
| Cover byline name | Fraunces 800 | 21 / 1.0 | -0.015em | |
| Cover subtitle | Nunito Sans 400 | 12.6 / 1.42 | 0 | |
| Cover eyebrow | Nunito Sans 900 | 8.6 / 1.0 | 0.20em caps | |
| Cover credibility band | Nunito Sans 900 | 9.4 / 1.25 | 0.005em | on the bleeding yellow band |
| Page headline | Fraunces 900 | 27 / 1.02 | -0.022em | reversed over photo |
| Section title | Fraunces 800 | 14.2 to 17 / 1.12 | -0.018em | `.qt` |
| Pull quote | Fraunces 900 | 13.6 / 1.02 | -0.024em | |
| NOT FOUND callout head | Fraunces 900 | 16.4 / 1.06 | -0.020em | `SOFT 55` |
| Deck | Nunito Sans 600 | 10.6 / 1.38 | 0 | |
| Question subhead | Nunito Sans 900 | 8.6 / 1.25 | 0.13em caps | with a 10pt color swatch |
| Body | Nunito Sans 400 | 8.5 / 1.44 | 0 | 8.1pt in narrow columns |
| Numbered list | Nunito Sans 400 | 8.3 / 1.38 | 0 | |
| Checklist | Nunito Sans 400 | 7.7 / 1.33 | 0 | |
| Table header | Nunito Sans 900 | 6.8 / 1.0 | 0.13em caps | |
| Table row header | Nunito Sans 900 | 7.8 / 1.14 | 0 | |
| Table cell | Nunito Sans 400 | 7.6 / 1.14 | 0 | |
| Cell pill | Nunito Sans 900 | 6.6 / 1.0 | 0.10em caps | |
| Inline attribution | Nunito Sans 700 | 6.6 / 1.35 | 0.03em | |
| Superscript source numeral | Nunito Sans 800 | 6.0 / 1.0 | 0.02em | `--turq-d` |
| Running head | Nunito Sans 900 | 7.6 / 1.0 | 0.19em caps | |
| Folio | Fraunces 900 | 19 / 1.0 | 0 | in a colored tile |

### Landing scale, px and container query units

| role | face | size |
|---|---|---|
| H1 | Fraunces 900 | `clamp(34px, 4.6cqw, 58px) / 1.00`, `-0.028em` |
| Subhead | Nunito Sans 400 | `clamp(15px, 1.35cqw, 18px) / 1.55` |
| Value prop title | Nunito Sans 900 | 14 / 1.25 |
| Value prop body | Nunito Sans 400 | 13 / 1.5 |
| Button | Nunito Sans 900 | 17 / 1.0 |
| Microcopy | Nunito Sans 800 | 13 / 1.4 |
| Trust line | Nunito Sans 600 | 12.5 / 1.5 |
| Eyebrow chip, brokerage pill | Nunito Sans 900 | 10 to 11, 0.14em to 0.16em caps |

---

## 4. Spacing, radii, shape

**Spacing scale, points, guide.** 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16. Nothing between blocks under 6pt and nothing over 16pt. Page margin is `.55in` left and right, a `.26in` full bleed color band at the head, and a `.54in` foot.

**Spacing scale, px, landing.** 8, 10, 12, 14, 16, 18, 24, 26. Section padding is `clamp(24px, 3.4cqw, 46px)`.

**Radii.**

| token | value | used on |
|---|---|---|
| `--r-sm` | 4pt | table header corners, phone number chips |
| `--r-md` | 9pt | standard cards, soft close strip |
| `--r-lg` | 16pt | photo header, the NOT FOUND callout |
| `--r-xl` | 26pt | the cover panel top corners |
| pill | 999px | every chip, every badge, the button, the folio-adjacent lockups |

Roundness is the direction's friendliness carrier. Nothing in Desert Bloom has a square corner except the color band at the head of a page and the swatch squares in the question subheads.

**Shadow.** None on paper. On the landing page only: the button carries a hard `0 6px 0 var(--magenta-d)` offset plus a tinted `rgba(158,20,80,.28)` drop, and cards carry `rgba(42,23,18,.2)`. No neutral gray shadows anywhere.

---

## 5. Print rules

```css
@page { size: letter; margin: 0; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
```

- Page boxes are exactly `8.5in x 11in` with `overflow:hidden`. Measured content height at build: cover panel 520/520 px, page 19 body 1004/1004 px, page 20 body 1004/1004 px. Zero clipped elements.
- `break-inside: avoid` and `page-break-inside: avoid` on `.card`, `.nf-callout`, `.tbl-wrap`, `.fig`, `.chk li`, `.nlist li`, `.close`, `.prop`.
- `thead { display: table-header-group }` so the district table repeats its header if it ever splits.
- **No `position: fixed` anywhere in the guide panels.** The landing panel does not use it either, so the whole file is safe to print.
- Bullets and checkboxes are flexbox rows with a real `<span>` marker. No `li::before { position:absolute }` anywhere.
- Every `<img>` carries real alt text. Every inline `<svg>` carries `role="img"`, `<title>`, and `<desc>`. The table carries `<caption>` and `<th scope>`.
- Meaning is never carried by color alone. NOT FOUND cells say NOT FOUND and carry a heavy coral left rule. Retired districts say Matured or Paid off and carry a turquoise left rule.

### Grayscale

| token | 8 bit gray |
|---|---|
| `--sand` | 245 |
| `--sand-2` | 233 |
| `--yellow-tint` | 238 |
| `--turq-tint` | 236 |
| `--coral-tint` | 232 |
| `--magenta-tint` | 230 |
| `--sand-3` | 220 |
| `--yellow` | 205 |
| `--coral` | 131 |
| `--turq` | 112 |
| `--coral-d` | 111 |
| `--magenta` | 101 |
| `--turq-d` | 88 |
| `--magenta-d` | 82 |
| `--ink-soft` | 80 |
| `--ink` | 28 |

The two solid saturated fills, magenta at 101 and turquoise at 112, are eleven levels apart and are **not** distinguishable on a monochrome laser. That is why every solid turquoise card carries a `3.5pt` `--yellow` left edge, which drops to gray 205 and separates it from the magenta callout by shape and tone rather than by hue.

### Ink

Every solid is under a 190 percent total area coverage, so nothing on this direction risks set-off or slow drying on a digital duplex run.

| token | CMYK | TAC |
|---|---|---|
| `--sand` | 0 / 4 / 10 / 1 | 15% |
| `--yellow` | 0 / 23 / 82 / 0 | 105% |
| `--turq` | 90 / 10 / 0 / 46 | 146% |
| `--coral` | 0 / 63 / 81 / 11 | 155% |
| `--magenta` | 0 / 87 / 49 / 24 | 160% |
| `--magenta-d` | 0 / 87 / 49 / 38 | 174% |
| `--coral-d` | 0 / 67 / 86 / 22 | 175% |
| `--ink` | 0 / 45 / 57 / 84 | 186% |

An economy override for a home printer is one rule: set `--sand` and `--sand-2` to `#FFFFFF`, which removes the flood tint from all 44 pages and cuts about 40 percent of the toner without touching a single color block or contrast ratio. Every ratio above still passes on white, because white is lighter than sand in every pair.
