# Claude Design brief: "Wayfinding"

Paste this whole file. It assumes you know nothing else.

---

## What you are building

A print-first, 39-page Letter-size buyer guide PDF plus a matching web landing page hero, for a Las Vegas real estate agent. The guide splits into three reader paths at page 5 and rejoins at page 18. The design system is a **transit signage system**: the three paths are three subway lines, the shared pages are a trunk line, and the reader always knows which line they are on.

**Thesis, do not drift from it:** find your line and ride it to the end.

**References:** Massimo Vignelli's NYC subway diagram, airport terminal signage, the US Web Design System, a printed rail timetable. Not editorial magazines, not real estate brochures, not luxury.

---

## Non-negotiables

1. **Zero em-dashes (U+2014) anywhere,** including CSS comments. Use commas, periods or "and".
2. **`Real Broker, LLC` gets a designed slot,** never shrunk to fine print. Nevada law requires a licensee's advertising to carry the brokerage name and licence number. On the cover it is a **solid ink plate, white caps, 10.5pt, +0.13em tracking**, sitting directly under the agent name. In the web trust line it is set at 800 weight inside a bordered plate.
3. **`[NOT FOUND]` renders literally** where the licence number goes, in a fixed-width slot: `display:inline-block; min-width:15ch; font-variant-numeric:tabular-nums`. A real number must drop in without reflowing the cover. Keep the compliance block at `min-height:0.46in`.
4. **No `position: fixed` anywhere in the guide file.** A fixed element repeats on every printed page. Use `position:absolute` inside a `position:relative` page box. `position: fixed` is allowed on the landing page only.
5. **Bullets and numbered items use `display:flex` with the marker as a real flex child.** Never `li::before { position:absolute }`. Under CSS multi-column an absolute bullet lands on the first letter.
6. **Tables carry `<caption>`, `<th scope="col">`, and `thead { display: table-header-group }`.**
7. **Never encode meaning in colour alone.** Every path marker carries a letter, a shape and an ink outline before it carries a hue.
8. **Factual only.** Never invent a price, fee, rate, incentive, school rating or HOA amount. Mark gaps `NOT FOUND` and give the reader a lookup instead.

---

## Palette, exact hex

```css
--paper:      #FFFFFF;  /* page stock, only background on any printed page */
--platform:   #EDF0F2;  /* tinted panel: aside, phone block, overset plate */
--platform-2: #DDE3E6;  /* table header band, diagram term bar */
--rule:       #B9C1C6;  /* table row hairlines, decorative only */
--ink:        #15181B;  /* body text, trunk rail, all outlines, CTA button */
--ink-soft:   #3D454B;  /* deck, table cells, structured lists */
--muted:      #59616A;  /* source strip, running head, folio label, captions */

--line-a:     #073B4C;  /* Path A, circle,  solid rail  */
--line-b:     #C74B21;  /* Path B, square,  dashed rail */
--line-c:     #F0B000;  /* Path C, diamond, dotted rail */
--top-dim:    #D8DDE0;  /* secondary text in the ink concourse bar, web only */
```

**Contrast rules, already computed. Do not re-derive.**
- Lowest ratio used anywhere is 4.71 (`--paper` on `--line-b`). Everything passes AA.
- `--line-c` on `--paper` is 1.92. **Amber is never text on white and never a shape edge on its own.** Every amber shape carries a 0.75pt `--ink` hairline.
- All three marker shapes carry that same 0.75pt ink hairline so they are built identically.

---

## The line system

| Path | Letter | Shape | Rail pattern | Fill | Letter colour | Pages |
|---|---|---|---|---|---|---|
| A | `A` | circle | solid band | `--line-a` | `--paper` | 6 to 9 |
| B | `B` | square | dashed band | `--line-b` | `--paper` | 10 to 13 |
| C | `C` | diamond (square rotated 45, letter counter-rotated upright) | dotted band | `--line-c` | `--ink` | 14 to 17 |
| Trunk | none | solid band with a **continuous 1.1pt paper-white centreline** | `--ink` | `--paper` | 1 to 5, 18 to 39 |

**Priority of identification: letter, then shape, then rail pattern, then colour.** In grayscale the trunk band and Line A are only 1.48 apart, so **the trunk centreline is load bearing.** Never remove it.

Marker geometry: 13pt box. `display:inline-flex`, centred, `font: 800 7.4pt/1 "Public Sans"`, `border: 0.75pt solid var(--ink)`.

---

## Type

**Signage is sans. Speech is serif.** Headlines, subheads, tables, checklists, numbered lists, source strips, tabs, folios, running heads, labels and CTAs are Public Sans. Body paragraphs, decks, callout prose and the soft close are Source Serif 4.

```html
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&display=swap" rel="stylesheet">
```

**Guide scale, points:** cover title 50/0.95/-0.032em 800 · cover subtitle 14.5/1.42 serif · brokerage plate 10.5 caps +0.13em 700 · page headline 19.5/0.99/-0.030em 800 · deck 10.2/1.27 serif · subhead 11.4/1.06 800 · **body prose 9/1.32 serif** · **structured lists 7.7/1.29 sans** · callout heading 10.6/1.03 800 · callout body 9/1.32 serif · soft close 8.6/1.29 serif · **table cells 7/1.06 tabular** · table header 6.6 caps +0.13em 700 · NOT FOUND chip 6.2 caps 700 · **source strip 7/1.26** · running head 7.2 caps +0.16em 600 · folio 9 800 · diagram caption 5.5/1.24.

**Hero scale, pixels:** H1 60 (40 mobile) /0.99/-0.035em 800 · subhead 19 (17) /1.55 serif · CTA 17/1.0 800 · microcopy 13/1.5 · station numeral 15 800 tabular · station title 17 (16) /1.2 800 · station body 14/1.5 serif · trust line 13/1.62.

---

## Layout system, Letter page

Trim 8.5 x 11in. Rail band 0.28in on the **outer** edge, bleeding to trim. Outer margin 0.60in, inner 0.64in, top 0.40in, bottom 0.26in. Text measure 7.26in. **Two columns of 3.49in with a 0.28in gutter.** Running head band 0.20in, folio band 0.19in, main content 7.22in.

Thumb tab plates are 0.28in x 0.46in at **1.30in, 5.05in and 8.80in from the head**. On pages 6 to 17 exactly one prints. On trunk pages all three print at those same heights against the ink band, so a closed stack always reads.

Radii are **zero everywhere** except the Path A circle, whose roundness is information.

---

## Component list

1. **Rail** absolute, full height, outer edge, `--ink` or line colour, with pattern.
2. **Tab plate** paper plate flush to trim carrying one marker.
3. **Station marker** 13pt letter + shape + ink hairline.
4. **Running head** muted caps, 0.6pt rule under, section name on recto, book title on verso.
5. **Folio** bottom outer corner, numeral plus a small label (`TRUNK`, or `6 · A` on path pages).
6. **Headline block** section marker row, headline, deck, 1.6pt ink rule.
7. **Aside** `--platform` fill, 3.2pt ink left edge, small ink chevron marker, caps label.
8. **NOT FOUND callout** 1.4pt ink border, a 0.13in **45-degree ink hatch band** across the top, a solid ink `NOT FOUND` chip, then heading and serif body. This is the guide's signature object. It must read as generosity, never as a hole.
9. **NOT FOUND table plate** in a table cell it becomes an outlined plate: 0.7pt ink border, a 7pt hatched swatch with an ink divider, then `NOT FOUND` at 6pt 800 on paper. Never the solid chip inside a table row.
10. **End-of-line cap** a 6.6pt x 2pt ink bar before `Matured` or `Paid off`.
11. **Timetable** 7pt tabular, 0.5pt row hairlines, `--platform-2` header band with 1.4pt ink rules above and below, `white-space:nowrap` on cells, **no zebra striping**.
12. **Numbered list** flex, solid ink numeral square 10.5pt.
13. **Checklist** flex, 8.6pt open ink checkbox square, bold step name then explanation.
14. **Phone block** 1.2pt ink border on `--platform`, numbers set as solid ink plates, tabular figures.
15. **Soft close** 1.4pt ink top rule, small ink diamond marker, two serif paragraphs, second at 600 weight. Never a boxed CTA.
16. **Source strip** 2.2pt ink top rule, caps label left with a continuation note right, three columns, each entry a flex row with a solid ink numeral square. **Auto height, never clipped.** Give it whatever room it needs, roughly 2.6in on a dense page.
17. **Overset plate** when a block does not fit, print a plate that names it and where it went: 4pt ink left edge, an arrow, `OVERSET, RUNS TO PAGE N`. The system says so out loud rather than dropping content quietly.
18. **Route map** inline SVG, `role="img"` with `<title>` and `<desc>`. Trunk with white centreline, three coloured branches with solid, dashed and dotted patterns, ink halo under every coloured stroke, interchange nodes as white squares, stations as white circles with ink rings, a pattern legend across the foot.
19. **Landing hero** ink concourse bar, ink trunk rail down the left of the copy, H1, serif subhead, ink CTA button with an amber arrow, microcopy, bordered trust plate. Right side is a solid ink panel with three numbered stops, `01 02 03` in amber with amber ticks.

**The A, B and C marker shapes never appear on the landing page.** The hero uses plain numerals so the two systems are not confused.

---

## Motion, web only

Animate `transform` and `opacity` only. Never `transition-all`. CTA: `transition: transform .16s cubic-bezier(.2,.9,.3,1.2), background-color .16s ease`, `hover` nudges 3px right and goes to `#000`, `active` 1px, `focus-visible` gets a 3px `--line-c` outline at 3px offset. Nothing else moves. The guide has no motion at all.

## Responsive, web only

Use **container queries**, not viewport queries, so the hero reflows correctly inside a Lofty embed. Mobile-first base, then `@container (min-width: 860px)` for the desktop split. Below 860px the ink panel stacks under the copy and a bottom action bar pins with `position: fixed`.

## Print CSS

```css
@page { size: letter; margin: 0; }
.page { -webkit-print-color-adjust:exact; print-color-adjust:exact; page-break-after:always; break-after:page; }
.aside,.nfbox,.phone,.dgm,.movep,.close,.strip li,table tr,.chk li,.nlist li { break-inside: avoid; }
table thead { display: table-header-group; }
```

Ship a `--rail-outline` print option that draws the rail as a 1.2pt outline instead of a solid band. It saves about 2.4 points of page ink coverage at the cost of the closed-stack thumb read.

---

## Things that must never change

- The trunk rail's continuous paper-white centreline. It is the only thing separating the trunk from Line A in grayscale.
- The 0.75pt ink hairline on every path marker and every amber shape.
- Letter before shape before pattern before colour.
- Sans for signage, serif for speech.
- Zero radii except the Path A circle.
- The source strip is a designed feature with a heavy rule and numbered ink squares, never grey fine print. A guide that hides its sources is a brochure.
- `Real Broker, LLC` on its own line, at a real size, on the cover and in the trust line.
- The `[NOT FOUND]` fixed-width slot.
- No em-dashes.
