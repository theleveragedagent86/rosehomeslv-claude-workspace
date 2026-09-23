# Claude Design brief: "Sunrise to Sunset"

Paste this whole file into Claude Design to keep building the Las Vegas new construction buyer guide
in this direction. It is self contained. Do not go looking for the other five directions.

---

## The one sentence

**The book moves through a day.** Bright and open at the start, deeper and calmer by the end. The
palette does not switch at a section break, it drifts continuously across 44 pages, so the money and
contract pages arrive in warm indigo and ember that feel serious without ever feeling cold.

## What this guide is

A 44 page, print first PDF lead magnet for **Ryan Rose, Real Broker, LLC**, Las Vegas, Henderson and
Clark County, Nevada. It teaches a first time new construction buyer what the builder's sales rep is
not required to tell them. The register is **protective, warm and generous**, never alarming and never
salesy. Reference energy is Ken Pozek's "Moving to Orlando" relocation magazine: big photography,
confident colour blocking, friendly question headings. Not luxury, not minimal, not a spec sheet.

**The last round of this project was rejected by real testers as "too analytical and robotic."** If
anything you make looks like a newspaper, a field manual, a ledger or a data sheet, you have failed.

---

## Colour, exact hexes, do not substitute

Every value is a position on one day. Front of book uses the light end, back of book uses the dark
end, and pages in between interpolate.

```
--paper        #FFFCF6   first light paper, front half base
--wash-morning #FFEFDD   mid morning tinted panel
--wash-noon    #FBDCB4   full sun, darkest light ground, NOT FOUND chip field
--panel        #FFF7EC   the lit window, ivory panel inverted onto dark grounds
--panel-alt    #FFF1E0   table zebra row

--sky-dawn     #9EC4DE   the only cool value in the system, asides and dawn chips
--amber        #F2A03D   golden hour, accents on dark grounds, phone pills
--ember        #C9451B   sunset, FILLS ONLY plus display type over 18pt
--ember-ink    #AE3813   sunset for small text on warm grounds, exists to hold AA
--rose-dusk    #93304F   afterglow, the phone block field

--indigo-dusk  #3A2A63   dusk, lightest stop of a dark page ground
--indigo-night #1E1442   night, darkest stop, cover footer, hero prop 3

--ink          #2B1F30   body on light grounds, never pure black
--ink-soft     #6A5350   attributions, captions, legends
--on-dark      #FDF3E6   body on dark grounds, never pure white
--on-dark-soft #CFBFD6   secondary on indigo
--on-rose-soft #F0D9DE   secondary on the rose field only

--rule-warm    #E3CFB4   --rule-warm-2 #D8BF9E   --rule-dark rgba(253,243,230,.26)
```

**Banned, hard failure:** Rose Homes navy `#1C2333`, champagne `#C9A86E`, off white `#F7F5F0`.

**Page grounds.** Both use a 158 degree fall so a spread reads as one continuous canvas.

```
light page:  linear-gradient(158deg,#FFFDF9 0%,#FFFAF0 26%,#FFF1DF 52%,#FEE3C2 76%,#FBDCB4 100%)
dark page:   linear-gradient(158deg,#4A3573 0%,#3A2A63 24%,#2C1F58 54%,#22174B 78%,#1A1140 100%)
```

**The signature device, the horizon in the gutter.** On any spread where the light half meets the dark
half, put a 0.17in full height strip on the inner edge of each page:

```
verso inner edge: linear-gradient(180deg,#F9C97F,#F2A03D 26%,#C9451B 62%,#93304F 100%)
recto inner edge: linear-gradient(180deg,#93304F,#6C2A55 34%,#43265F 68%,#2A1B50 100%)
```

---

## Type

One Google Fonts request:

```
https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1&family=Onest:wght@100..900&display=swap
```

**Fraunces** is display only. Always set `opsz`, `SOFT` and `WONK` explicitly. `SOFT` is the warmth
dial: 40 to 44 on covers and callouts, 28 to 36 on headings, 0 to 20 when a heading must be quiet.
`WONK` is 1 everywhere except folio numerals.

**Onest** is text and interface. Never set a display line in it.

| role | family | size | weight | axes | tracking | leading |
|---|---|---|---|---|---|---|
| cover title | Fraunces | 58pt | 500, accent 700 | opsz 144, SOFT 40, WONK 1 | -0.03em | 0.96 |
| hero headline | Fraunces | clamp(32px,3.4vw,50px) | 600, accent 700 | opsz 144, SOFT 38, WONK 1 | -0.03em | 1.02 |
| page question head | Fraunces | 24.5pt | 600 | opsz 72, SOFT 36, WONK 1 | -0.026em | 1.04 |
| NOT FOUND head | Fraunces | 17.5pt | 700 | opsz 60, SOFT 44, WONK 1 | -0.022em | 1.04 |
| section subhead | Fraunces | 13pt | 600 | opsz 36, SOFT 30, WONK 1 | -0.012em | 1.08 |
| panel heading | Fraunces | 9.6 to 10.4pt | 600 | opsz 24 to 30, SOFT 28 | 0 | 1.10 |
| deck | Onest | 10.6pt | 300 | | 0 | 1.38 |
| body prose | Onest | 8.5 to 8.7pt | 400 | | 0 | 1.44 to 1.46 |
| callout body | Onest | 8.1pt | 400, close 600 | | 0 | 1.44 |
| checklist body | Onest | 7.2pt | 400, label 700 | | 0 | 1.36 |
| table cell | Onest | 8pt | 400, district 700 | | 0 | 1.15 |
| table header | Onest | 5.9pt | 700 caps | | 0.10em | 1.0 |
| caption, legend | Onest | 5.9pt | 500 | | 0 | 1.32 |
| attribution | Onest | 6.5pt | 500 | | 0.02em | inherit |
| running head | Onest | 7pt | 700 caps | | 0.20em | 1.0 |
| time of day label | Onest | 6.6pt | 700 caps | | 0.18em | 1.0 |
| hero body | Onest | 17px sub, 14.5px props | 300, emphasis 600 | | 0 | 1.60 to 1.62 |

Spacing scale, 4pt base: `4 8 12 16 22 30 40 54`. Radii: 3pt chips, 7pt small panels, 14pt lit panels
and callouts, pill for chips and buttons.

---

## Layout system

**Guide page**, 8.5in by 11in, margins 0.44 top, 0.40 outer, 0.30 to 0.34 bottom, 0.58 gutter, plus
the 0.17in horizon strip on the inner edge.

Vertical order on a light page: running head with time marker, question headline, deck, two column
body at 0.26in gutter, full width callout, full width figure pinned to the bottom, folio.

Vertical order on a dark page: running head with time marker, question headline, intro, full width lit
panel, two column zone below it, folio. The soft close always sits bottom right of the recto, so it is
the last thing the eye lands on.

**Landing page**, two column hero at `1.12fr .88fr` with three equal value prop cards below. One
breakpoint at 860px: photo moves above the copy with `order:-1`, props stack, button goes full width.

---

## Component list

1. **Day arc marker.** Inline SVG, 120 by 22 viewBox. Dotted arc `M4 20 A 56 18 0 0 1 116 20`, plus a
   sun dot positioned by section, plus a caps label (FIRST LIGHT, MID MORNING, FULL SUN, GOLDEN HOUR,
   LATE LIGHT, DUSK, LAST LIGHT). On dusk and later, add a solid horizon line so the dot reads as
   setting. Needs `role="img"`, `<title>`, `<desc>`.
2. **Running head.** Section name in `--ember-ink` or `--amber` caps, reader path dots plus written
   label, day arc marker. Hairline underneath.
3. **Lit panel.** `--panel` ivory, 14pt radius, `0 3pt 0 rgba(0,0,0,.16)` shadow, a Fraunces heading
   plus a small caps tag on the right. Used for any object that must stay readable and writable on a
   dark ground.
4. **District table.** Full page width inside a lit panel. `table-layout: fixed`, colgroup at
   9 / 39 / 26 / 26 percent, `<caption>`, `scope="col"`, `thead { display: table-header-group }`,
   `white-space: nowrap` on cells so every row is exactly one line. Ember header row with white caps.
   Zebra in `--panel-alt`.
5. **Status chips.** `NOT FOUND` in `--ember-ink` on `--wash-noon`. `MATURED` and `PAID OFF` in
   `--indigo-dusk` on `#E4DCEF`. Always followed by a plain language legend under the table.
6. **The NOT FOUND callout.** The most important object in the book. `--ember` 1.5pt border, 14pt
   radius, warm gradient fill `#FFF7EC` to `#FFE9D2`, a 3.5pt sunset ribbon along the top
   (`#F2A03D` to `#C9451B` to `#93304F`), a filled ember pill kicker, a Fraunces headline, and a two
   column body.
7. **Aside.** `--sky-dawn` field, 7pt radius, small caps label plus a Fraunces question heading.
8. **Numbered steps and checklist.** Flexbox rows. Numerals are ember filled circles with white text.
   Checkboxes are 10pt white squares with a 1.2pt ember border, real enough to tick with a pen.
9. **Phone block.** `--rose-dusk` field, white organisation names, amber pills for the numbers.
10. **Soft close.** Hairline above, quiet body, then one Fraunces line with the offer in `--amber`.
11. **Figure.** Ember number tag on `--indigo-dusk`, Fraunces caption, then a wide flat SVG band.
12. **Brokerage lockup.** `Ryan Rose` in Fraunces, an amber rule, then `REAL BROKER, LLC` in Onest 700
    caps at 0.20em, then the compliance line. This is a designed object, not a footer afterthought.
13. **Hero value prop card.** Day arc marker plus phase label, Fraunces heading, Onest 300 body. Three
    across, stepping `--wash-morning` to `--amber` to `--indigo-night`.

---

## Content rules that override any design idea

- **Zero em-dashes.** U+2014 anywhere, including CSS comments, is a hard failure.
- **Never invent or alter a fact, number, date, statute, phone number or source.** You may rewrite
  headings, callout labels and connective phrases only.
- Reframe headings as friendly questions in a plain, sixth grade voice. No hype, no superlatives, no
  "premier" or "exclusive". Soft CTAs only, never a deadline or scarcity.
- **Nevada advertising law:** `Real Broker, LLC` and license `S.0185572` must appear on the cover and
  in the landing hero trust line. Also: `Ryan Rose · 702-747-5921 · ryan@rosehomeslv.com ·
  rosehomeslv.com`.
- **Fair housing:** photography is architecture, landscape and place only. No people. Never imply an
  image is a specific named community or a specific builder's home.
- Clark County only. Never Pahrump, Mesquite or Boulder City.
- Sourcing: short inline attribution where a fact lands, for example "Clark County Treasurer, verified
  July 2026", plus a small superscript numeral. Full URLs live only in a numbered appendix on page 41.

---

## Print and accessibility, non negotiable

- `@page { size: letter; margin: 0 }`, `print-color-adjust: exact` on page boxes and on `*` inside
  `@media print`.
- `break-inside: avoid` on every panel, callout, table, figure and list item.
- **No `position: fixed` in the guide.** It is allowed on the landing page only.
- **Bullets are flexbox.** Never `li::before { position: absolute }`.
- Direct children of a page box get `flex: 0 0 auto` so content can never silently compress to fit.
- Every pair of colours you use must be computed with python3 against WCAG AA and must pass. The
  current system's minimum is 4.71 with zero failures. Do not ship an assertion, ship a calculation.
- Alt text on every photograph. `role="img"`, `<title>` and `<desc>` on every meaningful SVG.
  `aria-hidden="true"` on decorative ones.
- Never encode meaning in colour alone.

---

## What must never change

1. **The drift.** One continuous day, no hard section break in the palette. If a page needs to be dark
   before its place in the arc, the arc is wrong, not the page.
2. **`--ember` is never small text.** Use `--ember-ink` below 18pt. This is what holds AA.
3. **Working objects invert.** Any table, checklist or form on a dark ground becomes a `--panel` lit
   panel. Never set a data table in `--on-dark` on indigo.
4. **The NOT FOUND callout stays the warmest object on its page.** It is the guide's whole argument.
   It may never be shrunk, greyed, footnoted or moved below the fold.
5. **Two families only**, Fraunces and Onest. Banned everywhere: Playfair Display, Montserrat, Bebas
   Neue, Barlow Condensed, IBM Plex, Newsreader, Source Serif 4, Source Sans, Public Sans, Instrument
   Sans.
6. **The brokerage lockup and the license number are designed elements**, never fine print.
7. **The economy print variant exists.** Keep a print only override that drops a full page dark flood
   to `--panel` with a 0.5in indigo header band, so a reader on a home inkjet is not punished.
