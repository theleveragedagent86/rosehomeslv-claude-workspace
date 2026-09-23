# Claude Design brief · Direction 5 · Magazine to Briefing

Paste this whole file into Claude Design to keep building pages in this direction. It is standalone.
Everything below is the locked system. Nothing here is a suggestion.

---

## 1. What you are building

A 44 page print-first buyer guide plus one web landing hero for **Ryan Rose, Real Broker, LLC**, Las
Vegas new construction. The reader has already driven past a model home and has nobody on their side.

**The design thesis, in one line:** a lifestyle magazine that quietly turns into the clearest briefing
document you have ever been handed.

**The book has two halves and a hinge.**

| | Part one, pages 1 to 17 | Page 18, the hinge | Part two, pages 19 to 44 |
|---|---|---|---|
| register | lifestyle magazine | the handover | warm briefing |
| colour | all six magazine hues, saturated | photo dissolving to paper | clay and plum only, lower saturation |
| photography | full bleed, full page, leads | one large photo, top 4.15in | a 0.78in band per spread, supports |
| type size | large display, generous | 36pt statement | tighter, denser, same faces |
| grid | 1 or 2 loose columns | free | 2 to 3 tight columns, paired tables |
| what survives | round corners, Petrona, warmth, colour | round corners, Petrona, warmth, colour |

**Never make part two cold.** It gets denser, quieter and more useful. It does not get clinical. If a
page in part two would look at home in a bank statement, it is wrong.

---

## 2. Exact palette

```css
:root{
  /* part one, the magazine half */
  --mag-sunset:#D24018;   /* primary saturated block; carries white text at 4.68 */
  --mag-coral:#E9714A;    /* secondary block; INK TEXT ONLY */
  --mag-ochre:#EFA00B;    /* seals, chips, arrows; INK TEXT ONLY; never text on light paper */
  --mag-agave:#166A62;    /* the cool note; light text only */
  --mag-dusk:#4A2B52;     /* the deep block; same hue as --brief-plum */
  --mag-sand:#F8EFE2;     /* magazine paper, reverse text on dusk */
  --mag-cream:#FDF8F1;    /* brightest paper, landing hero ground */

  /* part two, the briefing half: TWO HUES ONLY */
  --brief-paper:#FBF6ED;
  --brief-clay:#9E3A1F;
  --brief-plum:#4A2B52;
  --brief-tint:#F3E6D6;        /* clay tint */
  --brief-plum-tint:#EDE6EE;   /* plum tint */
  --brief-muted:#6B584E;       /* attributions, folios, the NOT FOUND token */

  /* shared */
  --ink:#2B1D23;          /* all body text, a warm plum-black, never neutral */
  --white:#FFFFFF;
  --rule:#977C61;         /* every visible border, drawn at 0.5pt to 0.75pt */
  --rule-strong:#7C6349;  /* checkbox squares, phone box, table foot rule */

  --r-chip:3pt; --r-card:7pt; --r-big:12pt;
  --pad-page:0.5in; --gutter:0.32in;
}
```

**Colour laws.**

1. White never sits on `--mag-coral` (3.03) or on `--mag-ochre` (1.79). Ink only.
2. `--mag-ochre` is never text on any light paper (2.01 on brief-paper). It is a fill.
3. `--brief-tint` and `--brief-plum-tint` are grayscale identical. They may never appear in the same
   component or be used to distinguish two things.
4. Part two may use `--mag-ochre` for exactly one job: the arrow and eyebrow chip that mark the
   handoff from a NOT FOUND callout to its remedy. Nowhere else.
5. Nothing is encoded in colour alone, ever.

Verified: **81 computed WCAG pairs, zero FAIL, worst normal-text ratio 4.68.** Recompute in Python if
you add a pair. Do not assert a ratio.

---

## 3. Type

```html
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:ital,wght@0,300..800;1,400..600&family=Petrona:ital,wght@0,400..800;1,400..600&display=swap" rel="stylesheet">
```

```css
--serif:"Petrona",Georgia,"Times New Roman",serif;
--sans:"Hanken Grotesk","Helvetica Neue",Arial,sans-serif;
```

**The split is semantic. Prose is Petrona. Apparatus is Hanken Grotesk.** Labels, eyebrows, tables,
lists, checklists, attributions, folios, diagram callouts and all landing UI are sans. Everything the
reader hears as Ryan's voice is serif.

Print scale (pt): cover title 50/0.95/-0.028em/800 · transition headline 36/1.02/700 · section headline
26/1.04/700 · deck 10.9/1.46 sans · subhead 14 to 17/1.12/700 serif · body prose 9.5/1.48 serif · beat
line 14 serif italic 700 · aside body 8.3/1.46 sans · list item 8.3/1.44 sans · callout heading
20/1.06/700 serif · callout body 8/1.44 sans · eyebrow 7 to 7.4 caps 800 at 0.14 to 0.19em · table
caption 6.6 caps 800 · table head 6.4 caps 800 · table cell 7.3/1.22 tabular-nums, row head 7.6/800 ·
NOT FOUND token 7.1 italic 600 · checklist 7.3/1.36 · phone number 10.8 serif 700 tabular-nums · soft
close 9/1.4 serif · attribution 7.1/1.4 sans 500 · superscript ref 6.4 sans 800 · folio 12 serif 700
plus 7 caps sans 800.

Web scale (px): H1 `clamp(34px,3.5vw,54px)`/1.02/-0.028em/800, 30px under 560px · subhead 17/1.58 max
44ch · prop heading 18/1.18 serif 700 · prop body 13.5/1.52 · button 17/800 · trust name 19 serif 700 ·
brokerage 11.5 caps 800 at 0.19em · trust detail 12.5/1.65 · pull quote 19/1.34 serif italic 600.

---

## 4. Component list

**Part one.**
`cover` (photo top 5.9in, dusk block bottom 5.55in overlapping 0.35in, eyebrow flag straddling the seam
at 5.18in, ochre seal on the photo at 3.72in, byline lockup, compliance line, 0.3in two-part strip on
the bottom edge) · `full-bleed photo spread` · `saturated colour block page` · `illustrated valley map`
(inline SVG, flat shapes, stylized valley outline, the 215 as an ochre ribbon loop, the 15 as an agave
diagonal, mountain triangles, rooftop chevrons, park dots; charming, never photoreal) · `Q and A area
template` (question headings in coloured caps plus a "why locals love it here" callout).

**The hinge, page 18.** `transition page`: photo top 4.15in dissolving to `--brief-paper`, eyebrow
"END OF PART ONE", 36pt statement with an italic clay phrase, three white "what changes / what stays"
cards, three lettered reader-path chips, a map thumbnail with a caption, folio.

**Part two.**
`photo band` (0.78in, full bleed, ONE image split across the gutter: `width:17.32in`, verso offset 0,
recto `margin-left:-8.82in`; recto copy is `alt="" aria-hidden="true"`) · `running head chips` ·
`prose column` · `beat line` (short clay serif italic sentence used as a paragraph break) ·
`aside` (plum tint, 3pt plum left border, named label such as "Between us") ·
`numbered list` (flex rows, clay disc numerals) ·
`NOT FOUND callout` (clay panel, `--r-big`, ochre eyebrow pill with ink text, 20pt serif heading, sans
body, a white 62 percent rule, an ochre arrow disc, one handoff line) ·
`figure card` (white, 0.6pt rule, `--r-card`, eyebrow, serif title, inline SVG, muted foot) ·
`paired data table` (two side-by-side tables, `table-layout:fixed`, colgroup 15.5/36.5/24/24, plum
header band, `--brief-tint` zebra, 0.5pt rules, `--rule-strong` foot) ·
`NOT FOUND cell token` (literal words, italic, dotted underline, hollow-circle glyph, plus a legend) ·
`compare cards` (white, district label caps, serif value, inline sans note) ·
`checklist panel` (`--brief-tint`, `--r-big`, ochre arrival arrow on the gutter edge, 2x2 flex steps,
`--rule-strong` checkbox squares) ·
`phone box` (white, 1.4pt `--rule-strong`, serif numbers in clay) ·
`soft close` (3pt clay top rule, serif, offer set in clay italic) ·
`folio` (outer numeral in clay serif, centre appendix pointer, inner running head; reads across the gutter).

**Landing hero.** `flag chip` · `H1 with italic clay phrase` · `subhead` · `three value-prop cards` on
`--mag-sand` with coral, ochre and agave numeral chips · `pill button` on `--mag-sunset` · `microcopy` ·
`trust lockup` (name, coloured bar, `REAL BROKER, LLC` in caps, contact, license) · `art column` with a
tinted photo, three colour bars and a floating pull-quote card.

---

## 5. What must never change

1. **The two-half structure and the page 18 hinge.** This is the direction. Remove it and there is no
   direction left.
2. **Part two runs on clay and plum only,** plus paper, tints, ink and muted. No new hue enters after
   page 18. The single ochre exception is the NOT FOUND handoff.
3. **Petrona and Hanken Grotesk**, with the prose-serif / apparatus-sans split.
4. **Round corners survive into part two.** `--r-card` and `--r-big` are the warmth carriers. Never
   square a card to look serious.
5. **Every NOT FOUND is a handoff, never an apology.** It gets a coloured panel, an eyebrow that names
   what the reader is getting instead, and a pointer at the remedy.
6. **`Real Broker, LLC` and license `S.0185572` are designed lockups**, on the cover and in the landing
   trust line. Nevada law requires them; the design treats them as content, not as a disclaimer.
7. **Facts are load bearing.** Never invent or adjust a price, date, statute, phone number, district
   row or source. Reframe headings and labels freely; reframe substance never.
8. **No em-dashes anywhere,** including CSS comments. Checked mechanically.
9. **No Rose Homes navy `#1C2333`, champagne `#C9A86E` or off-white `#F7F5F0`.** No Playfair Display,
   Montserrat, Bebas Neue, Barlow Condensed, IBM Plex, Newsreader, Source Serif 4, Public Sans or
   Instrument Sans.
10. **Print hygiene.** `@page{size:letter;margin:0}`, `print-color-adjust:exact`, `break-inside:avoid`
    on every card, table and callout, `thead{display:table-header-group}`, guide pages set to
    `height:10.96in` in print (11in pushes a blank sheet after every page), zero padding and
    `line-height:0` on any preview wrapper in print, and **no `position:fixed` in the guide**. The
    landing page may use it; the guide never may.
11. **Bullets are flexbox.** Never `li::before{position:absolute}`.
12. **Every grid track is `minmax(0, ...)`.** Plain `1fr` carries `min-width:auto` and breaks the
    landing hero at 375px.
13. **Alt text on every image; `role="img"`, `<title>` and `<desc>` on every inline SVG.** The `<desc>`
    describes the argument the drawing makes, not its shapes.
14. **Sourcing:** short inline attribution where the fact lands, set at 7.1pt in `--brief-muted`, with a
    superscript numeral. Full URLs live only in a numbered appendix at the back. Never a source strip at
    the foot of a page.

## 6. Voice rules for any new copy

Headings are things a person says out loud, often a question. "Let's talk about the bill nobody
mentions." "So which districts are out there?" "Five minutes, four steps. Do this before you sign."
"Save these two numbers." Sidebars get names, not labels: *Between us*, *the part where I hand you a
tool instead*, *here it is, the tool from the facing page*. Sixth grade reading level, short sentences,
soft CTAs, no superlatives, no scarcity, no deadlines.
