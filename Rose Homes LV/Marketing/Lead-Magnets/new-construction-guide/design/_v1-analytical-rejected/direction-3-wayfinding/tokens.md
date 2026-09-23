# Direction 3, Wayfinding, design tokens

**Thesis:** Find your line and ride it to the end.
**Model:** transit signage. Vignelli, airport terminals, subway diagrams.
**Deliberately off brand.** No Rose Homes navy, no champagne gold, no Playfair, no Montserrat, no Bebas Neue.

---

## 1. Colour

Every colour as `--token | #hex | role`.

### Neutrals

| Token | Hex | Role |
|---|---|---|
| `--paper` | `#FFFFFF` | page stock. The only background on any printed page. |
| `--platform` | `#EDF0F2` | tinted panel. Aside, phone block, overset plate, hero station panel text. |
| `--platform-2` | `#DDE3E6` | one step deeper. Table header band, diagram term bar. |
| `--rule` | `#B9C1C6` | hairline between table rows and under the running head. Decorative only, never carries meaning. |
| `--ink` | `#15181B` | body text, the trunk rail, every solid marker outline, the CTA button. |
| `--ink-soft` | `#3D454B` | deck, table cells, structured lists, hero subhead. |
| `--muted` | `#59616A` | source strip, running head, folio label, captions. |

### Lines, the three reader paths

Values are chosen so the three lines separate as grey patches, not only as hues.

| Token | Hex | Luminance | Shape | Rail pattern | Letter colour | Role |
|---|---|---|---|---|---|---|
| `--line-a` | `#073B4C` | 0.037 | circle | solid band | `--paper` | Path A, moving here from out of state, pages 6 to 9 |
| `--line-b` | `#C74B21` | 0.173 | square | dashed band | `--paper` | Path B, moving up inside the valley, pages 10 to 13 |
| `--line-c` | `#F0B000` | 0.496 | diamond | dotted band | `--ink` | Path C, first new build, pages 14 to 17 |
| `--ink` (trunk) | `#15181B` | 0.009 | none | solid band with a continuous paper centreline | `--paper` | shared pages, 1 to 5 and 18 to 39 |

**The redundancy rule, in priority order.** A path is identified by its **letter** first, its **shape** second, its **rail pattern** third, and its **colour** last. Colour is never the only carrier. If you remove all colour from this system it still works.

### Hero only

| Token | Hex | Role |
|---|---|---|
| `--top-dim` | `#D8DDE0` | secondary text in the ink concourse bar |

**Scaffolding, not palette:** the preview page sits on `#6b6b6b` so white stock reads as paper. That grey is not part of the design.

---

## 2. Computed WCAG contrast table

Computed with `python3`, sRGB relative luminance, `(L1 + 0.05) / (L2 + 0.05)`, rounded to two decimals. Large text is 18.66px bold or 24px regular and above.

| foreground | background | ratio | used at | class | AA |
|---|---|---|---|---|---|
| `--ink` #15181B | `--paper` #FFFFFF | **17.82** | cover title, 50pt / 66.7px, 800 | large (needs 3.0) | PASS |
| `--ink` #15181B | `--paper` #FFFFFF | **17.82** | page headline, 19.5pt / 26px, 800 | large (needs 3.0) | PASS |
| `--ink` #15181B | `--paper` #FFFFFF | **17.82** | hero H1, 60px, 800 | large (needs 3.0) | PASS |
| `--ink` #15181B | `--paper` #FFFFFF | **17.82** | subhead, 11.4pt / 15.2px, 800 | normal (needs 4.5) | PASS |
| `--ink` #15181B | `--paper` #FFFFFF | **17.82** | body prose, 9pt / 12px, 400 serif | normal (needs 4.5) | PASS |
| `--ink` #15181B | `--paper` #FFFFFF | **17.82** | NOT FOUND callout body, 9pt, 400 serif | normal (needs 4.5) | PASS |
| `--ink` #15181B | `--paper` #FFFFFF | **17.82** | table NOT FOUND plate, 6pt, 800, plate ground is paper | normal (needs 4.5) | PASS |
| `--ink` #15181B | `--paper` #FFFFFF | **17.82** | soft close, 8.6pt, 400 serif | normal (needs 4.5) | PASS |
| `--ink` #15181B | `--paper` #FFFFFF | **17.82** | hero trust line brokerage, 13px, 800 | normal (needs 4.5) | PASS |
| `--ink` #15181B | `--platform` #EDF0F2 | **15.57** | aside body, 8.8pt, 400 serif | normal (needs 4.5) | PASS |
| `--ink` #15181B | `--platform` #EDF0F2 | **15.57** | overset plate lead, 6.7pt, 800 | normal (needs 4.5) | PASS |
| `--ink` #15181B | `--platform-2` #DDE3E6 | **13.75** | table header, 6.6pt, 700 caps | normal (needs 4.5) | PASS |
| `--ink-soft` #3D454B | `--paper` #FFFFFF | **9.76** | deck, 10.2pt / 13.6px, 400 serif | normal (needs 4.5) | PASS |
| `--ink-soft` #3D454B | `--paper` #FFFFFF | **9.76** | table cells, 7pt, 400 | normal (needs 4.5) | PASS |
| `--ink-soft` #3D454B | `--paper` #FFFFFF | **9.76** | checklist and numbered list, 7.7pt, 400 | normal (needs 4.5) | PASS |
| `--ink-soft` #3D454B | `--paper` #FFFFFF | **9.76** | hero subhead, 19px, 400 serif | normal (needs 4.5) | PASS |
| `--ink-soft` #3D454B | `--paper` #FFFFFF | **9.76** | hero trust lines, 13px, 500 | normal (needs 4.5) | PASS |
| `--ink-soft` #3D454B | `--platform` #EDF0F2 | **8.53** | overset plate body, 6.7pt, 400 | normal (needs 4.5) | PASS |
| `--muted` #59616A | `--paper` #FFFFFF | **6.28** | source strip entries, 7pt over 1.26, 400 | normal (needs 4.5) | PASS |
| `--muted` #59616A | `--paper` #FFFFFF | **6.28** | running head, 7.2pt, 600 caps | normal (needs 4.5) | PASS |
| `--muted` #59616A | `--paper` #FFFFFF | **6.28** | folio label, 6.6pt, 600 caps | normal (needs 4.5) | PASS |
| `--muted` #59616A | `--paper` #FFFFFF | **6.28** | diagram caption, 5.5pt, 400 | normal (needs 4.5) | PASS |
| `--muted` #59616A | `--paper` #FFFFFF | **6.28** | hero microcopy, 13px, 500 | normal (needs 4.5) | PASS |
| `--muted` #59616A | `--platform` #EDF0F2 | **5.49** | aside label, 6.5pt, 700 caps | normal (needs 4.5) | PASS |
| `--paper` #FFFFFF | `--ink` #15181B | **17.82** | NOT FOUND chip, 6.2pt, 700 caps | normal (needs 4.5) | PASS |
| `--paper` #FFFFFF | `--ink` #15181B | **17.82** | numbered list markers, 6.6pt, 800 | normal (needs 4.5) | PASS |
| `--paper` #FFFFFF | `--ink` #15181B | **17.82** | source strip numerals, 5.4pt, 700 | normal (needs 4.5) | PASS |
| `--paper` #FFFFFF | `--ink` #15181B | **17.82** | brokerage plate, 10.5pt, 700 caps | normal (needs 4.5) | PASS |
| `--paper` #FFFFFF | `--ink` #15181B | **17.82** | CTA button label, 17px, 800 | normal (needs 4.5) | PASS |
| `--paper` #FFFFFF | `--ink` #15181B | **17.82** | hero station body, 15px, 400 serif | normal (needs 4.5) | PASS |
| `--platform` #EDF0F2 | `--ink` #15181B | **15.57** | hero station body at container width, 14px, 400 serif | normal (needs 4.5) | PASS |
| `--top-dim` #D8DDE0 | `--ink` #15181B | **13.02** | concourse bar secondary, 12px, 500 caps | normal (needs 4.5) | PASS |
| `--line-c` #F0B000 | `--ink` #15181B | **9.26** | hero station numerals, 15px, 800 | normal (needs 4.5) | PASS |
| `--paper` #FFFFFF | `--line-a` #073B4C | **12.08** | marker letter A, 7.4pt, 800 | normal (needs 4.5) | PASS |
| `--paper` #FFFFFF | `--line-b` #C74B21 | **4.71** | marker letter B, 7.4pt, 800 | normal (needs 4.5) | PASS |
| `--ink` #15181B | `--line-c` #F0B000 | **9.26** | marker letter C, 7.4pt, 800 | normal (needs 4.5) | PASS |
| `--line-a` #073B4C | `--paper` #FFFFFF | **12.08** | `PATH A` label on path pages, 8.5pt, 700 caps | normal (needs 4.5) | PASS |
| `--line-b` #C74B21 | `--paper` #FFFFFF | **4.71** | `PATH B` label on path pages, 8.5pt, 700 caps | normal (needs 4.5) | PASS |

**Lowest ratio actually used: 4.71.** Nothing fails. Nothing was disclosed as a known issue.

### The one pair that is banned, written down so nobody reaches for it

`--line-c` #F0B000 on `--paper` #FFFFFF computes to **1.92**. Amber is **never** used as text on paper, and never as a shape edge on its own. Every amber shape in this system carries a **0.75pt `--ink` hairline**, which is 17.82 against paper and 9.26 against the amber, so the boundary clears the 3.0 non-text requirement by a wide margin. The same hairline is applied to the Line A circle and the Line B square so all three markers are built identically.

---

## 3. Grayscale values

Home printers. This is the number that decides whether the direction survives.

| token | hex | luminance | vs paper |
|---|---|---|---|
| `--ink` | #15181B | 0.0089 | 17.82 |
| `--line-a` | #073B4C | 0.0369 | 12.08 |
| `--line-b` | #C74B21 | 0.1728 | 4.71 |
| `--line-c` | #F0B000 | 0.4958 | 1.92 |
| `--muted` | #59616A | 0.1171 | 6.28 |
| `--rule` | #B9C1C6 | 0.5253 | 1.83 |
| `--platform-2` | #DDE3E6 | 0.7602 | 1.30 |
| `--platform` | #EDF0F2 | 0.8674 | 1.14 |

**Line against line, as grey patches:**

| pair | ratio | verdict |
|---|---|---|
| A vs B | 2.56 | clearly different tones |
| B vs C | 2.45 | clearly different tones |
| A vs C | 6.28 | unmistakable |
| trunk (ink) vs A | **1.48** | **the weak point.** In grayscale the trunk band and the Line A band are close to the same black. |

The trunk vs Line A collision is solved by pattern, not tone: **the trunk band always carries a continuous 1.1pt paper-white centreline down its middle and Line A never does.** A trunk page and a Path A page are still distinguishable on a black and white printer at arm's length.

---

## 4. Type

### Families

| Role | Family | Why |
|---|---|---|
| Signage, display, all structured content | **Public Sans** | the typeface of the US Web Design System. It is literally a government signage and forms face: neutral, large x-height, tight apertures, reads clean at 6pt in a table and at 60px on a hero. It is a Libre Franklin derivative, so it carries the American public-signage lineage this direction is built on. |
| Running prose, human voice | **Source Serif 4** | optical sizes, large x-height, designed for screen and print at small sizes. It puts warmth back into a system that is otherwise all signage, and it holds up at 9pt in a 3.49in column. |

**The system rule: signage is sans, speech is serif.** Headlines, subheads, tables, checklists, numbered lists, source strips, tabs, folios, running heads, labels and the CTA are Public Sans. Body paragraphs, decks, callout prose and the soft close are Source Serif 4. This is a rule a builder can apply without asking.

### Google Fonts URL, exact

```
https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&display=swap
```

Weights loaded: Public Sans 400, 500, 600, 700, 800 and 400 italic. Source Serif 4 variable optical size 8 to 60 at 400, 600, 700 and 400 italic.

### Type scale, guide panels, in points

| Role | Size | Line height | Tracking | Family / weight |
|---|---|---|---|---|
| Cover title | 50pt | 0.95 | -0.032em | Public Sans 800 |
| Cover subtitle | 14.5pt | 1.42 | 0 | Source Serif 4 400 |
| Cover byline name | 23pt | 1.02 | -0.022em | Public Sans 800 |
| Brokerage plate | 10.5pt | 1.0 | +0.13em, caps | Public Sans 700 on ink |
| Cover eyebrow | 8.4pt | 1.0 | +0.20em, caps | Public Sans 700 |
| Geography stations | 8.6pt | 1.0 | +0.15em, caps | Public Sans 700 |
| Credibility line | 9.4pt | 1.5 | +0.005em | Public Sans 500 |
| Edition block | 8.4pt | 1.55 | 0 | Public Sans 400 / 700 |
| Compliance block | 8.2pt | 1.6 | 0 | Public Sans 400 |
| Page headline | 19.5pt | 0.99 | -0.030em | Public Sans 800 |
| Deck | 10.2pt | 1.27 | 0 | Source Serif 4 400 |
| Subhead | 11.4pt | 1.06 | -0.014em | Public Sans 800 |
| Section marker | 7.6pt | 1.0 | +0.18em, caps | Public Sans 700 |
| **Body prose** | **9pt** | **1.32** | 0 | Source Serif 4 400 |
| **Structured lists** | **7.7pt** | **1.29** | 0 | Public Sans 400 / 700 |
| Callout heading | 10.6pt | 1.03 | -0.022em | Public Sans 800 |
| Callout and aside body | 8.8pt to 9pt | 1.31 to 1.32 | 0 | Source Serif 4 400 |
| Soft close | 8.6pt | 1.29 | 0 | Source Serif 4 400 / 600 |
| **Table cells** | **7pt** | **1.06** | 0, tabular figures | Public Sans 400 |
| Table header | 6.6pt | 1.0 | +0.13em, caps | Public Sans 700 |
| Table caption | 6.9pt | 1.3 | +0.16em, caps | Public Sans 700 |
| NOT FOUND chip | 6.2pt | 1.0 | +0.10em, caps | Public Sans 700 |
| NOT FOUND table plate | 6pt | 1.12 | +0.05em, caps | Public Sans 800 |
| **Source strip** | **7pt** | **1.26** | 0 | Public Sans 400 |
| Running head | 7.2pt | 1.0 | +0.16em, caps | Public Sans 600 |
| Folio numeral | 9pt | 1.0 | +0.02em | Public Sans 800 |
| Folio label | 6.6pt | 1.0 | +0.16em, caps | Public Sans 600 |
| Diagram caption | 5.5pt | 1.24 | 0 | Public Sans 400 |
| Source marker `[1]` | 6.4pt | superscript | +0.02em | Public Sans 700 |

**Body prose is 9pt, not the 10.5pt the page budget specifies.** That is a real deviation and it is argued in `rationale.md`. Source Serif 4 at 9pt has an x-height of about 4.28pt, roughly a 9.5pt Times equivalent.

### Type scale, landing page hero, in pixels

| Role | Mobile | 860px container and up | Line height | Tracking |
|---|---|---|---|---|
| Concourse bar | 10px | 12px | 1.0 | +0.14em to +0.18em, caps |
| Eyebrow | 11px | 11px | 1.0 | +0.20em, caps |
| H1 | 40px | 60px | 1.02 / 0.99 | -0.035em |
| Subhead | 17px | 19px | 1.55 | 0 |
| CTA button | 15px to 17px | 17px | 1.0 | +0.01em |
| Microcopy | 13px | 13px | 1.5 | 0 |
| Station label | 11px | 11px | 1.0 | +0.20em, caps |
| Station numeral | 15px | 15px | 1.0 | 0, tabular |
| Station title | 16px | 17px | 1.2 | -0.012em |
| Station body | 14px | 14px | 1.5 | 0 |
| Trust line | 13px | 13px | 1.62 | 0 |

---

## 5. Spacing, rules, radii

**Spacing scale, points, guide panels:** 3, 5, 8, 12, 18, 26, 38. Every vertical gap in the guide is one of these or a documented half step.

**Page geometry, Letter:**

| Item | Value |
|---|---|
| Trim | 8.5in x 11in |
| Rail band, outer edge, bleeds to trim | 0.28in |
| Margin, outer (rail side) | 0.60in total |
| Margin, inner (gutter) | 0.64in |
| Margin, top | 0.40in |
| Margin, bottom | 0.26in |
| Text measure | 7.26in |
| Columns | 2 at 3.49in, 0.28in gutter |
| Running head band | 0.20in |
| Folio band | 0.19in |
| Main content height | 7.22in |
| Source strip band | 2.64in on p19, 2.52in on p20, auto height, never clipped |
| Thumb tab plate | 0.28in wide x 0.46in tall, at 1.30in, 5.05in and 8.80in from the head |

**Rule weights:**

| Weight | Use |
|---|---|
| 0.5pt `--rule` | table row separators |
| 0.6pt `--rule` | under the running head |
| 0.75pt `--ink` | outline on every path marker shape |
| 1.0pt `--ink` | dashed placeholder frame, phone block |
| 1.2pt `--ink` | checkbox squares |
| 1.4pt `--ink` | NOT FOUND callout border, subhead top rule, table head and foot rules |
| 1.6pt `--ink` | headline rule, geography line |
| 2.2pt `--ink` | source strip top rule |
| 2.4pt `--ink` | cover byline plate rule |
| 3.2pt `--ink` | aside left edge |
| 4.0pt `--ink` | overset plate left edge |

**Radii: zero everywhere except the Line A circle.** Signage is square. The only round object in the system is the Path A marker, and its roundness is information, not decoration.

**Marker geometry:** 13pt square box. Circle is a 13pt disc. Square is a 13pt square. Diamond is a 13pt square rotated 45 degrees with the letter counter-rotated so it stays upright.

---

## 6. Print rules

```css
@page { size: letter; margin: 0; }
.page { -webkit-print-color-adjust: exact; print-color-adjust: exact;
        page-break-after: always; break-after: page; }
.aside, .nfbox, .phone, .dgm, .movep, .close,
.strip li, table.tt tr, .chk li, .nlist li { break-inside: avoid; }
table.tt thead { display: table-header-group; }
```

**Hard rules for the guide file:**

1. **No `position: fixed` anywhere in the guide.** A fixed element repeats on every printed page. The rail, the tab plates and the frame are `position: absolute` inside a `position: relative` page box, which does not repeat. `position: fixed` is permitted on the landing page only.
2. **Bullets and numbered items use `display: flex` with the marker as a real flex child.** Never `li::before { position: absolute }`. Under CSS multi-column an absolutely positioned bullet lands on the first letter. That bug has shipped twice in this workspace.
3. **Tables carry `<caption>`, `<th scope="col">` and `thead { display: table-header-group }`** so the header repeats when a long table breaks.
4. **No text within 5mm of the trim.** The rail band bleeds; nothing set inside it does.
5. **The rail bleeds and home printers cannot bleed.** A home print loses about 3mm of the band. The tab plates sit 0.28in in from the trim precisely so a trim variance never eats a marker.
6. **Ink option.** `--rail-solid` (default) prints the trunk and path bands as solid ink. `--rail-outline` prints them as a 1.2pt outline with solid marker plates only. The outline variant removes about 2.2 square inches of solid ink per page, roughly 2.4 points of page coverage, at the cost of a weaker closed-stack thumb read. Offer it as a "print friendly" toggle on the download page.
7. **Zero em-dashes.** Checked mechanically in `preview.html`: 0 occurrences of U+2014, 0 of U+2013.
