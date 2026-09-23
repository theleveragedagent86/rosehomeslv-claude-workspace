# Golden Hour, standalone brief for Claude Design

Paste this whole file. It is self contained. It describes one design direction for a 44 page
Las Vegas new construction buyer guide (print PDF) plus its landing page. Keep exploring inside
this system. Do not invent a new one.

---

## 1. The one sentence

Warm the way late desert light is warm: soft, generous, photographic, and grown up.

The reference register is a relocation magazine, not a luxury brochure and not a field manual.
Warm and inviting, but never carnival. Every page should look like the last hour of sun over the
valley. Photography is the warmth. Typography is the voice. Color is the reassurance.

The content is **protective**: it warns a buyer that the person at the model home works for the
builder, that a special assessment can ride along for thirty years, and that some numbers cannot be
verified at all. The design's job is to make that feel generous rather than alarming. If a
treatment makes hard information feel sold past the reader, it has failed.

---

## 2. Palette, exact hexes. Do not substitute.

```
--paper       #FDF8F1   page ground, warm cream
--sand        #F2E3D0   first elevation, checklist panels, cards, diagram bars
--row-tint    #F8EFE3   table zebra row
--clay-panel  #EBD3C2   the protective panel: NOT FOUND callouts, credibility strips
--rose-panel  #EFD9D3   aside panel, dusty rose
--sage-panel  #DEE4D5   cool relief: geography pills, phone blocks, retired-district pills
--terracotta  #93401E   accent TYPE only: question labels, superscript numerals, running heads
--ember       #A94E2B   accent FILLS and rules only: title rule, folio, checkbox stroke
--clay-deep   #6E3018   deepest warm dark: all display type, table header ground, phone numbers
--sage        #48583F   secondary accent type, only on --sage-panel
--rose-dark   #874A44   aside label type, only on --rose-panel
--ink         #33241D   body copy, warm near black
--ink-muted   #655045   attribution, captions, source pointers, compliance line
--rule        #D9C3AE   1px structural hairline
--rule-soft   #E7D6C4   1px decorative hairline
```

Duotone pigments for photography:
- Cover: dark `#54210E`, light `#F9DDAE`
- Interior bands and cards: dark `#6B2E13` or `#7A3A1C`, light `#FAE1B4` or `#FBE5BC`
- Landing background (a scrim rides over it): dark `#48180A`, light `#F3D5AE`

Landing hero text colors, over the scrimmed photo:
`#FFF7EC` headline, `#F1DCC4` subhead, `#EBD5BC` trust line, `#E7CEB2` microcopy,
`#F6C99B` brokerage line. Button `#5A2412` on `#F6DFC0`, hover ground `#FFF0DA`.

**Contrast floor is 4.89.** Every pair used passes WCAG AA at its real size and weight. If you add a
pair, compute it. `--terracotta` on `--clay-panel` is the tightest at 4.89, so never lighten
`--terracotta` and never darken `--clay-panel`.

---

## 3. Type

```html
<link href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,300..900;1,300..900&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,300..900,0..100,0..1;1,9..144,300..900,0..100,0..1&display=swap" rel="stylesheet">
```

**Fraunces** for all display and voice. Always set `font-variation-settings`. Raise `SOFT` as size
drops (32 at cover scale, 44 to 56 at callout and heading scale). Keep `WONK 1` on headings and
italics for the swashed `g` and `y`; use `WONK 0` for names, numerals, and table row labels.

**Figtree** for body, labels, tables, and interface. Never for headings.

Scale, print sizes in pt and screen in px:

| Role | Family | Size | Line | Variation | Track |
|---|---|---|---|---|---|
| Cover title | Fraunces | 45pt | .99 | opsz 144, wght 590, SOFT 32, WONK 1 | -.03em |
| Landing headline | Fraunces | 57px | 1.02 | opsz 144, wght 570, SOFT 36, WONK 1 | -.032em |
| Section opener headline | Fraunces | 31pt | 1.00 | opsz 120, wght 560, SOFT 44, WONK 1 | -.028em |
| Callout headline | Fraunces | 18pt | 1.06 | opsz 72, wght 560, SOFT 56, WONK 1 | -.022em |
| Card headline | Fraunces | 23px | 1.12 | opsz 48, wght 590, SOFT 44, WONK 1 | -.022em |
| Name | Fraunces | 17pt | 1.10 | opsz 48, wght 600, SOFT 30, WONK 0 | -.015em |
| Question head | Fraunces | 14pt | 1.14 | opsz 36, wght 600, SOFT 50, WONK 1 | -.018em |
| Phone number | Fraunces | 12pt | 1.00 | opsz 36, wght 640, SOFT 30, WONK 0 | -.01em |
| Pull italic | Fraunces italic | 9.6 to 11.5pt | 1.34 to 1.40 | opsz 24 to 30, wght 460 to 500, SOFT 60 | 0 |
| Body | Figtree | 8.3pt / 15px | 1.45 to 1.62 | 400 | 0 |
| Deck on photo | Figtree | 9.6pt | 1.50 | 400 | 0 |
| List and checklist | Figtree | 7.8 to 8.2pt | 1.38 to 1.42 | 400, lead-in 750 | 0 |
| Table data | Figtree | 7.3pt | 1.20 | 400 | 0 |
| Table header | Figtree | 6.9pt caps | 1.20 | 800 | .13em |
| Question label caps | Figtree | 7.2pt caps | 1.35 | 800 | .15 to .18em |
| Running head | Figtree | 7.6pt caps | 1.00 | 800 | .24em |
| Attribution, caption, source pointer | Figtree | 6.5 to 6.8pt | 1.42 to 1.50 | 400 | 0 |
| Superscript numeral | Figtree | 5.8pt | 0 | 800 | .02em |

---

## 4. Layout system

- Trim 8.5in x 11in. Interior live margin **0.52in**. Cover margin **0.55in**.
- Body engine is **CSS `column-count: 2`, gutter 0.3in**. Full width objects (callouts, tables,
  panels, figures) break out of the column flow.
- Radii: `8px` small, `16px` inner chips, `26px` asides and cards, `40px` hero objects,
  `999px` pills. **Nothing in this system has a hard corner.**
- Spacing inside pages is in inches so it survives print scaling:
  `.02 .055 .07 .09 .12 .18 .26 .36 .48in`. Screen spacing scale:
  `4 8 12 18 26 38 54 76 104px`.
- Section opener pages get an **inset duotone photo band**, margin `.36in .48in .18in`,
  height `1.5in`, radius 40px, with the running head, headline, and deck set in cream over it.
- Folios sit at the **gutter**, so 19 and 20 face each other and the spread reads as one canvas.

### Duotone recipe, use this exactly

```css
.duo { position: relative; overflow: hidden; background: var(--clay-deep); }
.duo > img { width:100%; height:100%; object-fit:cover;
             filter: grayscale(1) contrast(1.24) brightness(.99); }
.duo .duo-dark  { position:absolute; inset:0; background: var(--duo-dark);  mix-blend-mode: lighten; }
.duo .duo-light { position:absolute; inset:0; background: var(--duo-light); mix-blend-mode: multiply; }
```

Plus the golden hour signature wash, layered over the duotone:

```css
.sunwash { position:absolute; inset:0; background:
  radial-gradient(110% 68% at 78% 34%, rgba(255,190,104,.52) 0%, rgba(255,190,104,0) 64%),
  radial-gradient(90% 62% at 10% 4%, rgba(96,40,20,.44) 0%, rgba(96,40,20,0) 70%),
  radial-gradient(100% 55% at 30% 104%, rgba(96,40,20,.40) 0%, rgba(96,40,20,0) 68%); }
/* .horizon variant moves the glow to 72% 58% for full bleed covers */
```

---

## 5. Component list

1. **Cover.** Full bleed duotone photo, eyebrow with sun arc mark top left, edition tag top right,
   and a floating cream card inset 0.55in from left, right, bottom, radius 40px. Card holds: title,
   1.5in ember title rule, subtitle, three sage geography pills, a clay credibility strip in
   Fraunces italic, then a footer row of byline plus edition notes, then the compliance line.
2. **Section opener band.** Inset duotone photo, 1.5in, radius 40px, with a horizontal scrim
   `linear-gradient(94deg, rgba(46,17,7,.90) 0%, .80 38%, .30 68%, .12 100%)` so the left holds
   type and the right holds photograph.
3. **Question head.** Small terracotta sun arc SVG plus a Fraunces question in `--clay-deep`.
   This is the repeating device. Every section head in the guide is a reader's question.
4. **Pull aside.** `--rose-panel`, radius 26px, caps label in `--rose-dark`.
5. **NOT FOUND callout.** `--clay-panel`, radius 40px, full text width, caps label in
   `--terracotta`, 18pt Fraunces headline, body in 3 columns, and a cream inner chip labelled
   "WHAT YOU GET INSTEAD" that hands the reader the substitute. **This must be the largest and
   warmest object on its page.**
6. **Numbered list.** Flex rows, numeral in a `--sand` pill with `--terracotta` type.
7. **Data table.** `<caption>` visible above holding the attribution, `--clay-deep` header row with
   `--paper` caps, `--row-tint` zebra, `<th scope="col">` on every column and `<th scope="row">` on
   the identifier. NOT FOUND cells get a `--clay-panel` pill; retired districts get a `--sage-panel`
   pill. Words always carry the meaning, never the color.
8. **Checklist panel.** `--sand`, radius 40px, two columns, checkbox is a 13px square with a 1.5px
   `--ember` border and 4px radius, as a real flex child.
9. **Phone block.** `--sage-panel`, radius 26px, caps label in a narrow left column, numbers at
   12pt Fraunces.
10. **Illustrated valley map.** Flat inline SVG: sun disc, sage ridge shapes, sand basin ellipse,
    I-15 as a straight ribbon and the 215 as a loop, both drawn as a wide `--clay-panel` casing with
    a thin terracotta line on top, plus a few tiny house silhouettes. Charming and simple, never
    photorealistic. On working spreads it is a 1.5in card; on section openers it can run half a page.
11. **Diagram.** Wide short band, viewBox around 760 x 132. Pale stacked bars inside a dotted
    `--ink-muted` box, one `--ember` bar outside it, and a term bar on the right.
12. **Landing hero.** Full bleed duotone photo, left column of eyebrow pill, headline, subhead,
    pill button, microcopy, trust line; right column a rounded duotone photo card with a floating
    cream chip. Below it, a full width `--paper` band with 40px top radius holding three value prop
    cards, each with a duotone photo strip, a terracotta question label, a Fraunces headline, and
    body.

---

## 6. What must never change

1. **Zero em dashes (U+2014) and zero en dashes anywhere**, including CSS comments. Hard failure.
2. **Off brand.** Never `#1C2333`, `#C9A86E`, or `#F7F5F0`. Never Playfair Display, Montserrat,
   Bebas Neue, Barlow Condensed, IBM Plex, Newsreader, Source Serif, Public Sans, or Instrument Sans.
3. **`Real Broker, LLC` is designed for**, never tolerated. It gets its own letterspaced terracotta
   caps line directly under "Ryan Rose", on the cover and in the landing trust line. Nevada law
   requires the brokerage on a licensee's advertising.
4. **License number `S.0185572`** appears on the cover compliance line and in the landing trust line.
   Contact block: Ryan Rose, Real Broker, LLC, 702-747-5921, ryan@rosehomeslv.com, rosehomeslv.com.
5. **No `position: fixed`** in any guide page. It repeats on every printed sheet.
6. **Bullets and checkboxes are flex children in the markup.** Never
   `li::before { position: absolute }`.
7. **Print first.** `@page { size: letter; margin: 0 }`, `print-color-adjust: exact` globally,
   `thead { display: table-header-group }`, and `break-inside: avoid` on every callout, card, table,
   panel, figure, and list item.
8. **Accessibility.** Real alt text on every image, describing the place and the light, never the
   community or the builder. Every meaningful inline SVG carries `role="img"` with
   `aria-labelledby` pointing at a `<title>` and a `<desc>`. Decorative marks carry
   `aria-hidden="true"`. Never encode meaning in color alone.
9. **Fair housing.** Imagery is architecture, landscape, and place only. No depictions of people.
   Never imply an image is a specific named community or a specific builder's home.
10. **Facts are load bearing.** You may rewrite headings into the reader's questions and invent
    callout labels. You may never change, drop, or invent a number, date, statute, phone number,
    or source. Where a figure does not exist, print NOT FOUND and hand the reader the lookup.
11. **Sourcing pattern.** A superscript terracotta numeral where the fact lands, a short human
    attribution near the block ("Clark County Treasurer, verified July 25, 2026"), and one quiet
    `--ink-muted` pointer per page to the numbered source appendix in the back. No source strip at
    the foot of every page.
12. **Warmth is structural, not decorative.** No red, no amber, no warning colors. Severe facts sit
    as plain type on plain paper. The single loud object per spread is reserved for the one thing
    that genuinely deserves it.
