# Claude Design brief. Direction 3, Scrapbook

Paste this whole file into Claude Design to keep building pages in this direction.

---

## What you are making

Pages for a 44 page print-first buyer guide, **Before You Walk Into the Model Home**, plus its landing page. It is a Las Vegas, Henderson and Clark County new construction guide by **Ryan Rose, Real Broker, LLC**, Nevada license **S.0185572**.

The content is protective, not aspirational. It tells a buyer that the person at the model home works for the builder, that a special assessment can ride along for thirty years, and that a builder incentive has a cap. The design job is to make that feel generous instead of alarming.

## The thesis, do not drift from it

**A friend who already did this walked you through it and wrote in the margins.**

One rule governs every page:

> **The data is crisp. Everything around the data is handmade.**

Tables, numbers, dates, phone numbers and checklists are set clean, square, unrotated and quiet. The arrows, circles, highlighter swipes, margin notes, taped photos and sticky notes around them are the handmade layer. If a handmade element ever sits on top of data, you have broken the direction.

---

## Exact palette

```css
--paper:#FBF4E6;      /* the stock, every page */
--paper-deep:#F3E7CF; /* zebra source, 42% over --card = #FAF4E6 */
--card:#FFFDF7;       /* anything laid on the paper */
--ink:#33281C;        /* all body copy and all data */
--ink-soft:#6A5A45;   /* attribution, captions, page foot */
--pen:#22406B;        /* handwriting and hand drawn arrows */
--redpen:#A6321F;     /* circles, ticks, numerals */
--terracotta:#B2432A; /* primary accent, button, folio, Real Broker LLC */
--teal:#186670;       /* section subheads, chip 1 */
--sage:#3F6E48;       /* chip 2 */
--plum:#7A3A63;       /* chip 3 */
--hi-yellow:#FFE49B;  /* highlighter, highlighted table rows */
--hi-mint:#C6E6CE;    /* second highlighter, once per spread max */
--hi-pink:#F9CDC2;    /* third highlighter, reserve */
--sticky:#FFE9A8;     /* sticky note stock */
--sticky-mint:#CFE6D4;
--sticky-blue:#CFE0EE;
--sticky-pink:#F9CDC2;
--kraft:#E8D5B0;      /* washi tape */
--rule:rgba(51,40,28,.18);
--rule-soft:rgba(51,40,28,.10);
```

Banned: Rose Homes navy `#1C2333`, champagne `#C9A86E`, off white `#F7F5F0`. Never pure `#000` or pure `#FFF`.

Every pair in use clears WCAG AA. The lowest ratio in the system is 5.14 (terracotta on paper). Recompute before adding any new pair.

## Type

```html
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700;800&family=Caveat:wght@400;600;700&family=Nunito:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
```

- **Baloo 2** 700/800: display, headlines, subheads, table headers, numerals, buttons, `Real Broker, LLC`.
- **Nunito** 400/600/700/800: all body copy and all table data.
- **Caveat** 400/700: annotation only. Margin notes, photo captions, sticky note headlines, diagram ticks, signatures. **Never body copy. Never more than about 12 words at a time.**

Interior scale, in points because the guide is a print object:
headline 24 / deck 10.8 (600) / subhead 14.5 (800, teal) / body 9.2 on 1.45 / list 8.6 / aside 8.8 / table cell 7.5 on 1.18 / table col head 7.2 (800, reversed) / caption and page foot 6.9 / attribution 7 italic / margin note 14 Caveat / sticky headline 25 Caveat / folio 10 (800, terracotta).

Landing page in px: h1 `clamp(30px,4.1vw,52px)` 800 / sub 17 / button 19 / prop title 19 / prop body 14.5 / trust 13.5 / microcopy 14.

## Layout system

- Page trim `8.5in x 11in`. Padding `.40in` top, `.48in` outer, `.27in` bottom, `.40in` gutter side.
- Every interior page is **one text column plus one margin lane**. Verso: `5.15in + .20in + 1.95in`. Recto: `5.60in + .20in + 1.52in`. The lane holds annotations, a small photo, or a diagram. Nothing in the lane is required reading.
- Elements may span both columns: the sticky note, a full width table, a toolkit row.
- Two column flow is the release valve for long copy: use `column-count:2` on lists, sticky note bodies, and runs of short paragraphs.
- Rotation budget: tape -9 to +5 deg, photo frames -2.2 to +3.2, cards and stickies -1.1 to +0.9, margin notes -2 to +1.4. **Tables, checklists and diagrams never rotate.**

## Component list

1. **Washi tape** `.tape`. Absolute, `1.05in x .26in`, kraft gradient, irregular `clip-path`, small shadow. Two or three per page maximum.
2. **Polaroid** `.polaroid`. White card frame, `.13in` sides, caption in Caveat below the image in flow. Optional `.corners` for photo mount corners instead of tape. A warm multiply overlay sits on the image.
3. **Highlighter swipe** `.hl`. A marker stripe, not a filled block: `background-size:100% .62em; background-position:0 .50em; background-repeat:no-repeat`, uneven `border-radius`, `box-decoration-break:clone`.
4. **Index card aside** `.aside`. Card background, thin border, `--sticky-blue` spine on the left, lead in phrase in Baloo 2 pen blue.
5. **Sticky note** `.notefound`. Yellow stock, slight rotation, folded corner via a corner gradient, tape strip on top, terracotta sticker label, Caveat headline, two column Nunito body. **Reserved for the NOT FOUND moment.**
6. **Numbered token** `.five .num`. `.215in` circle, sticky yellow fill, 1.5px ink border, Baloo 2 numeral. Flexbox row, never `::before` absolute.
7. **Checklist card** `.checkcard`. Card background, `--sticky-pink` spine, real `.14in` checkbox squares, bold step label then explanation.
8. **Phone card** `.phones`. Mint stock, Caveat title, Baloo 2 numbers.
9. **Data table** `.sid`. Card background, reversed ink header row, zebra at 42 percent, `.019in` cell padding, `<caption>` above in ink-soft, `th scope` on both axes, `thead{display:table-header-group}`.
10. **NOT FOUND chip** `.nf`. Dashed ink-soft outline pill, 6.8pt Baloo 2, transparent fill. Used inside table cells.
11. **Hand drawn SVG** circles, arrows, brackets. `--pen` or `--redpen`, `stroke-width` 2 to 2.6, `stroke-linecap:round`, deliberately imperfect bezier. Always `aria-hidden` when decorative.
12. **Geography chips** `.sticker`. Full pill, 8pt Baloo 2 caps, paper text on teal, sage or plum.
13. **Doodle map**. Inline SVG, dashed sage basin, teal 215 arc, terracotta 15 diagonal, plum Strip marks, ink ridgeline, Caveat labels. Flat shapes only, no more than about eight paths.
14. **Value prop sticker cards** `.prop`. Landing page only. Yellow, mint and blue, small rotations, Caveat numeral in redpen at the top right.

## Rules that must never change

1. **Zero em-dashes** anywhere, including CSS comments. Commas, periods or "and".
2. **Never invent a fact.** No price, rate, incentive, assessment amount, square footage or school rating. Gaps are marked `NOT FOUND` and the copy says out loud why.
3. `Real Broker, LLC` and license `S.0185572` are designed elements, not fine print. They appear on the cover, in the recto running head, and in the landing hero trust line.
4. Print rules: `@page{size:letter;margin:0}`, `print-color-adjust:exact`, `break-inside:avoid` on every card, table, callout and list item, `break-after:page` on each page box.
5. **No `position:fixed` in the guide.** It repeats on every printed page. The landing page may use it.
6. Bullets and checkboxes are flexbox rows with a fixed basis marker span. Never `li::before{position:absolute}`.
7. Real alt text on every image. Inline SVG that carries meaning needs `role="img"`, `<title>` and `<desc>`.
8. **Never encode meaning in color alone.** A highlighted row also gets a solid inset bar. A NOT FOUND cell also gets the literal words and a dashed outline.
9. **No people in any image.** This is housing advertising. Architecture, landscape and place only, and never imply a photo is a specific named community or a specific builder's home.
10. Caveat is annotation only. If it is more than about 12 words, it is Nunito.
11. Sources are a superscript numeral plus a short inline attribution such as "Clark County Treasurer, verified July 2026". Full URLs live in a numbered appendix, never in a footer strip.
12. Photography stays large and frequent. A page with no photograph, no annotation and no color object has failed this direction.

## Voice for headings you write

Reframe headings as something a friend would say out loud. Questions and plain statements, sixth grade reading level, no hype.

Examples already in use: "Wait. What is this second bill?", "Five things I would tell a friend first", "Which district will your lot be in?", "Do this before you sign. Five minutes, tops.", "Put these two in your phone."

Never reframe a fact. Only the packaging.
