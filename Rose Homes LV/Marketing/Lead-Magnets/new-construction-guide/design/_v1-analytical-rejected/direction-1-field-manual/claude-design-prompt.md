# Field Manual, standalone design brief

Paste this whole file into Claude Design. It assumes no other context.

---

## What you are building

A 39 page, print-first Letter buyer guide for people buying newly built homes in Las Vegas,
Henderson and Clark County, plus a matching landing page hero. The author is Ryan Rose of
Real Broker, LLC. The reader is a nervous, skeptical buyer who has already driven past a model
home and has not talked to an agent yet.

**Thesis, do not drift from it: a tool you carry into the model home, not a brochure you read
on the couch.** Utilitarian, high contrast, unfussy. Inspection clipboard, aviation checklist,
military field guide. The cover looks like equipment. Every page is designed for a pen.

This guide is deliberately **off-brand** for Rose Homes LV. Never use navy `#1C2333`, champagne
gold `#C9A86E`, or warm off-white `#F7F5F0`. Never use Playfair Display, Montserrat, or
Bebas Neue.

---

## Palette, exact hexes

```css
--ink:            #101418;  /* bars, display type, heavy rules, checkbox strokes */
--text:           #2A3138;  /* the only color running prose is ever set in */
--muted:          #5A646D;  /* source log, URLs, field labels, captions */
--signal:         #8F2D08;  /* signal on LIGHT ground only */
--signal-bright:  #E8641A;  /* signal on DARK ground only */
--signal-tint:    #F7E9DF;  /* field for asides and the NOT FOUND callout */
--paper:          #FFFFFF;  /* interior page stock */
--rail:           #EFEEE9;  /* the note rail field */
--zebra:          #F5F4F0;  /* table alternate row */
--rule:           #C6C4BC;  /* ruled writing lines, hairlines, figure frames */
--night:          #14181D;  /* cover ground and landing hero ground, nothing else */
--night-muted:    #C9D0D7;  /* secondary text on --night */
```

Two ink colors and one paper. Everything else is a tint or a rule weight.

**Pairs that must never be made:** `--signal` on `--night` (2.20:1) and `--signal-bright` on
`--paper` (3.54:1). The signal has a light-ground variant and a dark-ground variant and they
do not swap. Lowest ratio in the approved system is 5.20:1, so every combination in use clears
WCAG AA with margin.

---

## Type

One Google Fonts request:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
```

- **Barlow Condensed** 500/600/700: cover title, headlines, subheads, rail headings, beat
  lines, table column headers, buttons, value prop titles. Usually uppercase.
- **IBM Plex Sans** 400/500/600/700: all running prose, decks, callout body, table cells,
  checklist text.
- **IBM Plex Mono** 400/500/600: source log, URLs, dates, phone numbers, district ids, every
  small caps label, the license slot, figure captions. Monospace is structural here, not
  decorative: it is what makes a blank field look like a field.

### Scale, px over line-height

| Use | Family | Size | Leading | Tracking |
|---|---|---|---|---|
| Cover title | Barlow Cond 700 caps | 98 | 0.86 | -0.005em |
| Page headline | Barlow Cond 700 | 34 | 0.93 | -0.008em |
| Callout head | Barlow Cond 700 | 26 | 0.94 | -0.005em |
| Beat line | Barlow Cond 700 caps | 21 | 1.04 | 0.005em |
| Subhead | Barlow Cond 700 caps | 19 | 1.0 | 0.09em |
| Rail heading | Barlow Cond 700 caps | 15.5 | 1.04 | 0.03em |
| Deck | Plex Sans 500 | 14.5 | 1.36 | 0 |
| **Body prose** | **Plex Sans 400** | **14 (10.5pt)** | **1.45** | **0** |
| Aside / callout body | Plex Sans 400 | 11.5 | 1.40 | 0 |
| Table cell | Plex Sans 400 | 11.5 | 1.15 | 0 |
| Rail list / checklist | Plex Sans 400 | 10.5 | 1.30 to 1.34 | 0 |
| **Source log entry** | **Plex Sans 400** | **9.33 (7pt)** | **1.32** | **0** |
| Source log URL | Plex Mono 400 | 8.3 | 1.32 | 0 |
| Citation numeral | Plex Mono 600 sup | 8.5 | 0 | 0 |
| Labels, field labels | Plex Mono 600 caps | 7.5 to 8.5 | 1.0 | 0.16 to 0.22em |
| Figure caption | Plex Mono 600 caps | 7.2 | 1.42 | 0.04em |
| Hero headline | Barlow Cond 700 caps | clamp(40, 4.9vw, 70) | 0.94 | -0.01em |
| Hero subhead | Plex Sans 400 | 18 | 1.58 | 0 |
| Hero button | Barlow Cond 700 caps | 22 | 1.0 | 0.09em |

**Body prose never sets below 14px.** If a page overruns, cut content or take leading from
1.45 to 1.42. Do not shrink the body.

---

## Layout system

```
trim            8.5in x 11in
margins         top 0.34  bottom 0.30  outer 0.36  inner 0.50
live            7.64in x 10.36in
rail column     2.47in   (36 percent) always on the OUTER edge, mirrors verso/recto
gap             0.22in
main column     4.95in   (64 percent) always toward the gutter
running head    0.34in band with a 2px --ink rule beneath
source log      1.24 to 1.52in band at the foot, 3px --ink rule above, 2 columns
```

Page stack, top to bottom: **running head band / [rail | main] / full-width foot panel /
source log band.** The foot panel is what carries the spread across the gutter: on a left page
it is the big callout, on a right page it is the closing prose plus the soft offer.

**The rail is the point.** It holds structured, annotatable content: numbered lists, checklists
with real checkboxes, labeled blank fields, ruled writing lines, phone blocks, asides. It is
tinted `--rail` with a 3px `--ink` top rule. It is never a decorative margin and never holds
running prose.

Spacing scale, 4pt base: `4 / 8 / 12 / 16 / 22 / 30 / 40 / 56`.
Rule weights, and each means something: `0.5pt` data hairline, `1px` writing line and frame,
`2px` block boundary, `3px` column boundary, `5px` signal bar.
Radii: `0` everywhere except `2px` on the landing button.

---

## Component list

1. **Cover.** Full bleed `--night` with a 0.25in hairline registration grid at 5.5 percent
   white. Black masthead strip with a 5px `--signal-bright` rule under it. 98px title. 3px
   orange kicker. Subtitle, geography line in `--signal-bright` caps, credibility line in mono.
   A CSS-only hatched placeholder block with a visible caption naming what belongs there.
   Bottom: a **nameplate** bordered 2px in `--signal-bright`, split into a `PREPARED BY` cell
   (name at 38px, `Real Broker, LLC` at 14px mono in the accent) and an `EDITION` cell, with a
   full-width compliance strip beneath carrying the license and contact lines.
2. **Running head band.** Section name left in Barlow Condensed 700 caps 15px, document
   reference right in 9px mono muted, 2px `--ink` rule beneath.
3. **Kicker + headline.** 5px x 1.2in `--signal` bar, then the headline.
4. **Deck.** 14.5px, closed by a 1px `--rule` hairline.
5. **Beat line.** A one sentence pull set in Barlow Condensed caps `--signal` with a 3px
   `--signal` left bar. Used for lines like "Often that somebody is you."
6. **Aside.** `--signal-tint` ground, 1px `--ink` border, 5px `--signal` left bar, an `ASIDE`
   mono label in `--signal`.
7. **NOT FOUND callout.** The most important component in the guide and it must read as
   generosity. Full measure. 2px `--ink` border. Solid `--ink` header bar with `NOT FOUND`
   left and the register item right in `--signal-bright`. Inside, a 3 cell grid: the refusal
   headline plus its explanation, then a divider, then a bordered **write-in block** labeled
   `YOUR LOT, YOUR NUMBER` with ruled blanks. The callout that will not print a number gives
   the reader the line to write their own on. Never apologize in this component's design.
8. **NOT FOUND table cell.** Inline mono 10px `--signal` caps, 1px `--signal` border, plus a
   45 degree hatch at 13 percent. Never color alone.
9. **State cell** (`Matured`, `Paid off`). Mono 11px `--ink` with a 2px `--ink` underline.
10. **Data table.** `table-layout: fixed`. `--ink` header bar, white Barlow Condensed 700 caps
    12px. Cells 11.5px, 1px vertical padding, 0.5pt `--rule` row rules, `--zebra` on even rows.
    Dates and district ids in mono. Visible `<caption>` set as `TABLE 19.1 · DISTRICT PAYMENT
    SCHEDULE`. `<th scope="col">` and `thead { display: table-header-group }` are mandatory.
11. **Checklist.** Flex row. Marker is a 14px white square with a 2px `--ink` border, sized for
    a ballpoint. Bold step name, then explanation.
12. **Numbered list.** Same flex pattern, marker is a 16px solid `--ink` square with a white
    mono numeral.
13. **Fill-in field.** 7.5px mono `--muted` caps label over a 13px tall box with a 1px
    `--muted` bottom rule. Ruled note lines are 14px tall with a 1px `--rule` bottom.
14. **Phone block.** 2px `--ink` border, white ground, Barlow Condensed caps head with an
    underline, numbers in 12.5px mono `--signal`.
15. **Foot panel.** 2px `--ink` top rule, closing prose left, the soft offer right behind a 3px
    `--signal` left bar. Never a boxed CTA.
16. **Source log band.** 3px `--ink` top rule. Head row: a solid `--ink` folio square, the log
    title in mono caps, the verification date right. Two columns with a 0.5pt column rule.
    Entries are flex rows with a `--signal` mono numeral as a real flex child. URLs in 8.3px
    mono with `overflow-wrap: anywhere`.
17. **Figure.** 1px `--ink` frame, mono caption prefixed `[ SVG-04 ]`, `role="img"` with
    `<title>` and `<desc>`. **Give a figure at least 2.1in of width** or its labels drop under
    6pt and it stops being readable.
18. **Landing hero.** `--night` ground, 34px hairline grid, a 6px `--signal-bright` bar down
    the left edge. Grid 1.32/1. Left: mono eyebrow with a trailing rule, headline, subhead,
    button, microcopy, trust plate. Right: a white card bordered 3px `--ink` with an `--ink`
    label bar, the value props set as checklist entries on a `--rail` ground, and a mono foot
    strip. The card is literally a page torn out of the manual.
19. **Trust plate.** 2px `--signal-bright` border, a solid `--signal-bright` label bar reading
    `LICENSED NEVADA BROKERAGE`, then the three trust lines in 13px mono with `Real Broker, LLC`
    set at 600 in the accent, tracked open and uppercase.
20. **Path tab** (pages 6 to 17). A bleed block on the rail's outer edge at one of three
    stepped vertical positions. A solid `--ink`, B `--muted` with a 45 degree hatch, C
    `--paper` with a 2px `--ink` border and a dot grid. Text bottom-to-top, Barlow Condensed
    700, 11px, 0.22em tracking, 5mm off trim.

---

## Motion rules

Print has no motion. The landing page has exactly one interactive element and it gets:

- `transition: transform .16s cubic-bezier(.2,.9,.3,1.2), background-color .16s ease, box-shadow .16s ease`
- Rest: `--signal-bright` fill, `--ink` label, `box-shadow: 0 3px 0 0 var(--signal)`. A hard
  offset shadow, not a blur. It reads as a physical key, not a card.
- Hover: `translateY(-2px)`, fill lightens to `#F5772C`, shadow grows to `0 5px 0 0`.
- Active: `translateY(1px)`, shadow collapses to `0 1px 0 0`.
- Focus-visible: `outline: 3px solid var(--paper); outline-offset: 3px`.
- **Only `transform`, `opacity`, `background-color` and `box-shadow` animate. Never
  `transition: all`.** No scroll animations, no reveals, no parallax, no counters.

---

## Things that must never change

1. **Body prose never sets below 14px (10.5pt).** Cut content instead.
2. **No `position: fixed` anywhere in the guide file.** It repeats on every printed page and
   the build's `qa-check.py` fails on it. The landing page file may use it.
3. **Bullets and numbered markers use flexbox**, marker as a real flex child. Never
   `li::before { position: absolute }`. Under CSS multi-column an absolute marker lands on the
   first letter.
4. **Never encode meaning in color alone.** Every NOT FOUND, every state cell, every path tab
   carries a pattern or a literal word as well as a tone.
5. **Keep the 2px `--ink` border on every tinted panel.** In grayscale `--signal-tint` (L\* 93.2)
   and `--rail` (L\* 94.0) are the same gray; the border is the only thing separating them.
6. **`Real Broker, LLC` keeps its designed slot** on the cover nameplate and in the hero trust
   plate. Nevada law requires a licensee's advertising to name the brokerage. Never shrink it
   toward invisibility, never move it into a footnote.
7. **The license number renders literally as `[NOT FOUND]`** inside `.slot`
   (`display:inline-block; min-width:10.5ch; monospace`) so a real number drops in without
   reflowing the cover or the hero.
8. **The rail is never decorative.** If a page has nothing structured to put in the rail, put
   ruled note lines in it. Do not let it become a pull-quote gutter.
9. **The NOT FOUND callout is never apologetic.** Black header bar, biggest object on its page,
   and it always hands the reader a lookup or a blank to fill in.
10. **No em-dashes anywhere**, including CSS comments. Use commas, periods, or "and".
11. **No external image URLs.** No `placehold.co`. Placeholders are CSS only with a visible
    caption naming what belongs there and an `aria-label` on the block.
12. **No hardcoded GA or Pixel tags on the landing page.** Lofty injects those at publish.
13. **No form inside the landing hero.** The button is `<a href="#contact">` and page JS
    scrolls to the bottom. Lofty appends its own form below the embed.
14. **Never write "Download now", "Instant access", a countdown, a deadline, or scarcity
    language.** The button says `Send me the guide`. The only promise is `The PDF comes by
    email.`

---

## Known constraint to design around

The per-page source strip is the hardest element in this guide. At 7pt with full URLs, 19
entries need about 4.79in of two column band across a spread, which is roughly a quarter of
every page it appears on, and it appears on 34 of 39 pages. Before extending this direction,
decide one of: move the log to a shared endnote section with numeric markers only on the page,
grow the page count, or accept that dense pages carry a partial log. Do not solve it by
setting the strip below 7pt.

Likewise, give any figure at least 2.1in of width. Below that its labels fall under 6pt and it
stops earning its space.
