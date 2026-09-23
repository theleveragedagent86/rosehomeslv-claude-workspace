# Desert Bloom, standalone brief for Claude Design

Paste this whole file into Claude Design to keep exploring this direction. It is self contained. Do not assume any other file is loaded.

---

## What you are making

A 44 page Las Vegas new construction buyer guide, print first at US Letter, plus a matching landing page hero. It is a lead magnet for Ryan Rose, a Las Vegas realtor at Real Broker, LLC. The content is **protective**: the person at the model home works for the builder, a special assessment can ride along with a home for thirty years, and a builder incentive tied to their lender has a cap. The design job is to make that content feel warm and generous, never cold or alarming, and never like it is being sold past the reader.

**Register reference:** Ken Pozek's "Moving to Orlando" guide. A relocation magazine, not a luxury brochure. Big photography, saturated color blocking, hand drawn cartoon maps, and a friendly repeating question and answer template. **Do not copy its palette, copy, or layouts.** Orlando is tropical. This is desert.

**Direction name: Desert Bloom.** Sunbaked, saturated, cheerful the whole way through. There is no serious half of this book. The hardest data page is styled with the same energy as the cover.

---

## Palette, exact hexes, do not substitute

| token | hex | role |
|---|---|---|
| `--sand` | `#FDF4E3` | the paper, full bleed on every page |
| `--sand-2` | `#F7E7C9` | second surface, table zebra, quiet cards |
| `--sand-3` | `#F2D9AE` | hairlines, chart grounds |
| `--ink` | `#2A1712` | warm near black, all body text |
| `--ink-soft` | `#6E4632` | attributions, captions, subheads on the landing page |
| `--white` | `#FFFFFF` | reversed type on solids only |
| `--magenta` | `#C21A63` | prickly pear, the loud one |
| `--magenta-d` | `#9E1450` | prickly pear at text weight |
| `--magenta-tint` | `#FBDFEA` | prickly pear at card weight |
| `--coral` | `#E2542B` | sunset, fills and borders only |
| `--coral-d` | `#C6421C` | sunset at text weight |
| `--coral-tint` | `#FBE3D6` | sunset at card weight |
| `--turq` | `#0E7C8A` | spring water, solid cards |
| `--turq-d` | `#0A616D` | spring water at text weight |
| `--turq-tint` | `#DCF0F0` | spring water at card weight |
| `--yellow` | `#FFC42E` | sunshine, the author's own voice |
| `--yellow-tint` | `#FFEDBE` | sunshine at card weight |
| `--cactus` | `#3F7A4E` | one green, illustration only, never behind type |

**Color laws.**
1. Reversed white type only ever sits on `--magenta`, `--coral-d`, `--turq`, or `--ink`. Never on `--coral`.
2. `--coral` `#E2542B` is a fill. It is never a text color on paper and never a background for small type.
3. Never set `--yellow` type on `--magenta` (3.64) or on `--turq` (3.09). Use `--yellow-tint` on magenta (5.00) or white on turquoise (4.92).
4. Never set `--coral-d` type on `--coral-tint` (4.06) or `--turq` type on `--sand-2` (4.04). Use ink, or the deep variant.
5. Every tint card carries `--ink` type.
6. Minimum contrast anywhere in this system is 4.50. Recompute with python before shipping any new pair.

---

## Type

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Nunito+Sans:ital,opsz,wght@0,6..12,300..1000;1,6..12,300..1000&display=swap" rel="stylesheet">
```

- **Fraunces** for display, always with `font-variation-settings:"SOFT" 45,"WONK" 1,"opsz" <size>`. The soft terminals and the wonky glyphs are the whole point. `SOFT 55` on the NOT FOUND callout, `SOFT 60` on pull quotes.
- **Nunito Sans** for everything else.
- **Banned:** Playfair Display, Montserrat, Bebas Neue, Barlow Condensed, IBM Plex anything, Newsreader, Source Serif 4, Public Sans, Instrument Sans.

**Guide scale, points, prints 1:1.** Cover title 53/0.94 at -0.024em. Page headline 27/1.02 at -0.022em. Section title 14.2 to 17/1.12. Pull quote 13.6/1.02. NOT FOUND head 16.4/1.06. Deck 10.6/1.38 in Nunito Sans 600. Question subhead 8.6 at 0.13em caps in Nunito Sans 900. Body 8.5/1.44, dropping to 8.1 in narrow columns. Numbered list 8.3/1.38. Checklist 7.7/1.33. Table header 6.8 caps, row header 7.8, cell 7.6/1.14. Cell pill 6.6 caps. Attribution 6.6/1.35. Source superscript 6.0 in `--turq-d`. Running head 7.6 at 0.19em caps. Folio 19pt Fraunces in a colored tile.

**Landing scale, container query units.** H1 `clamp(34px,4.6cqw,58px)/1.00` at -0.028em. Subhead `clamp(15px,1.35cqw,18px)/1.55`. Prop title 14/1.25 at 900. Prop body 13/1.5. Button 17 at 900. Trust line 12.5 at 600.

---

## Layout system

**Guide page.** Full bleed `.26in` four color band at the head. Running head under it at `.55in` side margins. Body at `.55in` margins. `.54in` foot holding the source appendix pointer and the folio tile. Page box is exactly `8.5in x 11in` with `overflow:hidden`. Content must measure to fit, not spill.

**Spacing.** Points: 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16. Nothing between blocks under 6 or over 16.

**Radii.** `--r-sm` 4pt, `--r-md` 9pt, `--r-lg` 16pt, `--r-xl` 26pt, plus 999px pills. Roundness carries the friendliness. Nothing has a square corner except the head band and the swatch squares in question subheads.

**Shadow.** None on paper. On the landing page only: a hard `0 6px 0 var(--magenta-d)` offset under the button plus a tinted drop, and `rgba(42,23,18,.2)` under cards. Never a neutral gray shadow.

---

## Component list

1. **Head band.** Four full bleed segments, magenta, coral, yellow, turquoise. The active reader path's segment runs wide, the others compress. Mirror the order on a verso page so a spread reads as one canvas.
2. **Photo headline block.** A `1.66in` rounded photo with a multiply tone `linear-gradient(100deg, rgba(158,20,80,.74), rgba(226,84,43,.40) 52%, rgba(255,196,46,.20))` plus a left scrim `linear-gradient(90deg, rgba(42,23,18,.58), rgba(42,23,18,.10) 60%, transparent)`. A yellow kicker chip and a reversed Fraunces headline sit bottom left.
3. **Question subhead.** Nunito Sans 900 caps at 0.13em with a 10pt rounded color swatch before it. Colors key to the reader path.
4. **Solid card.** Turquoise or magenta ground, reversed type, `--r-md`. Solid turquoise cards **must** carry a `3.5pt --yellow` left edge. That edge is the grayscale tell that keeps them apart from magenta on a monochrome printer.
5. **Tint card.** Yellow tint, coral tint or magenta tint ground, ink type, 1.6pt border in the parent hue.
6. **NOT FOUND callout.** Solid magenta, `--r-lg`, a yellow ribbon label, a Fraunces head, and one line pulled out in `--yellow-tint`. It is the largest object on its page. It must read as generosity, never as an error state.
7. **Data table.** Magenta header band, alternating sand and sand-2 rows, magenta row headers. `<caption>`, `<th scope>`, `thead { display:table-header-group }` required.
8. **Cell pills.** NOT FOUND is coral tint with a 2.4pt `--coral-d` left rule. Matured and Paid off are turquoise tint with a `--turq-d` left rule. The words always appear. Never color alone.
9. **Checklist.** Yellow tint card, flexbox rows, an 11pt square with a 1.8pt ink border as the checkbox.
10. **Numbered list.** Flexbox rows with a 13pt magenta disc holding a white numeral.
11. **Phone block.** Turquoise solid card with numbers on white `--r-sm` chips.
12. **Soft close.** Ink strip, sand type, one yellow sun icon, the offer emphasized in yellow. One line. Never a boxed CTA.
13. **Folio pair.** Colored `.44in` tiles at the inner edge of each page so the two numbers meet across the gutter.
14. **Illustrated valley map.** Inline SVG, flat vector. A sand-yellow valley bowl, coral and magenta mountain ranges, the 215 as a turquoise ellipse ribbon, I-15 as a coral diagonal, black tower shapes for the Strip, and every place labeled in a rounded sand chip. Full page as a section divider, or a 1.1in locator inline. Always tagged "Schematic, not to scale".
15. **Landing hero.** Container query at 760px. Desktop: copy left, photo right, map card overlapping up into the photo. Mobile: `.hero-art { display:contents }` so the photo reorders above the copy and the map falls below.

---

## Content rules that override design

- **Zero em-dashes.** Checked mechanically. Hard failure.
- **Never invent a fact.** No price, rate, incentive, square footage, HOA amount, or program detail. Gaps are marked NOT FOUND and designed, not hidden.
- Rewrite headings as friendly questions. Never rewrite a number, date, statute, phone number, or source.
- Short attribution inline where a fact lands, for example "Clark County Treasurer, verified July 2026". Superscript numerals point at a numbered source appendix in the back. There is no source strip at the foot of a page.
- Nevada law requires the brokerage name and license number on a licensee's advertising. `Real Broker, LLC` and `S.0185572` appear on the cover and in the landing trust line, designed as an ink pill with a yellow disc, never as an afterthought.
- Ryan Rose, Real Broker, LLC, 702-747-5921, ryan@rosehomeslv.com, rosehomeslv.com.
- Fair housing: architecture, landscape and place only. No depictions of people. Never imply an image is a specific named community or a specific builder's home.
- Clark County only. Never Pahrump, Mesquite, or Boulder City.

---

## What must never change

1. The four saturated hues and the sand paper. Adding a fifth hue breaks the path system.
2. Yellow is never a reader path. Yellow is always the author speaking directly.
3. The NOT FOUND callout stays the loudest object on its page.
4. Solid turquoise cards keep the yellow left edge.
5. Coral is never a text color and never a small-type background.
6. Question subheads stay in colored caps with a swatch.
7. Page boxes stay exactly `8.5in x 11in` with `overflow:hidden`, and content is measured to fit.
8. `@page { size: letter; margin: 0 }`, `print-color-adjust: exact`, `break-inside: avoid` on cards, tables, callouts and list rows.
9. No `position: fixed` anywhere.
10. Bullets and checkboxes are flexbox rows with a real marker element. Never `li::before { position: absolute }`.
11. Every image has real alt text. Every inline SVG has `role="img"`, `<title>`, `<desc>`.
12. Minimum computed contrast 4.50. Compute with python, never assert.
