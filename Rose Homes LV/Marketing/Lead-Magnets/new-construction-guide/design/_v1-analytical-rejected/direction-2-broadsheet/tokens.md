# Direction 2: Broadsheet, Design Tokens

**Thesis:** This is reporting on builders, not marketing from a realtor.

One spot colour. Everything else is ink weight, rule weight, and position. Radii are zero everywhere.
Em-dashes in this file: zero.

---

## 1. Colour tokens

| Token | Hex | Role |
|---|---|---|
| `--paper` | `#FFFFFF` | Page stock. Pure white, deliberately not a tinted brand off-white. |
| `--newsprint` | `#F2F2EF` | Light band. Table zebra rows, figure stack layers. |
| `--stock` | `#E5E6E1` | Heavy band. Table header, phone block, figure well, Path C tab. |
| `--ink` | `#14171A` | Primary text, headlines, heavy rules, Path A tab. |
| `--ink-2` | `#333A40` | Decks, table body, callout body, cover subtitle. |
| `--ink-3` | `#5C646C` | Agate. Source strip, datelines, running heads, folios, cutlines. |
| `--rule-hair` | `#BFC3BE` | Decorative hairline only. Never the sole carrier of meaning. |
| `--rule` | `#8E938D` | Functional rule. Table borders, section rules. |
| `--rule-heavy` | `#14171A` | Banner rules, headline rules, kicker rules. |
| `--spot` | `#7A2019` | The one spot colour. Oxblood. Kickers, NOT FOUND, footnote figures, CTA. |
| `--spot-deep` | `#5E1C16` | CTA hover and pressed. |
| `--spot-wash` | `#F7EFED` | NOT FOUND panel wash. Used once per page, at most. |
| `--path-a` | `#14171A` | Path A edge tab. Grayscale byte 23. |
| `--path-b` | `#7A2019` | Path B edge tab. Grayscale byte 65. |
| `--path-c` | `#E5E6E1` | Path C edge tab, carries ink text. Grayscale byte 229. |

**Scaffolding, not part of the palette:** preview page background `#5F5F5F`, preview caption `#F4F4F2`, caption note `#EAEAE6`. These exist only in `preview.html` and never ship.

### Why this palette

Three constraints drove it. It has to be **far from Rose Homes LV** (no navy `#1C2333`, no champagne `#C9A86E`, no warm off-white `#F7F5F0`). It has to **survive a home laser printer**, which rules out large saturated fills. And it has to **read as a record, not a brochure**, which rules out any second accent competing for attention.

Oxblood `#7A2019` is the answer to all three. It is the ink a newspaper uses for a correction stamp and a section flag: serious, not alarming, and old enough to feel like a printing convention rather than a marketing choice. It is nowhere near navy or gold. At `10.25:1` on white it clears AA as **body text**, not just as large text, so it can carry 6.2px verification stamps and 7px NOT FOUND cells without a second thought. And because it is dark, a solid CTA in it costs less toner than a mid-tone fill would.

---

## 2. Computed WCAG contrast table

Every ratio below was computed with the WCAG 2.x relative-luminance formula in `python3`, not asserted. AA thresholds: **4.5:1** for body text, **3:1** for large text (18.66px+ bold or 24px+ regular) and for non-text graphical objects.

| Foreground | Background | Used at | Ratio | Target | Result |
|---|---|---|---|---|---|
| `--ink #14171A` | `--paper #FFFFFF` | body prose 13.1px / 400 | **17.99** | AA body | PASS |
| `--ink #14171A` | `--paper #FFFFFF` | interior headline 35px / 700 | **17.99** | AA large | PASS |
| `--ink #14171A` | `--paper #FFFFFF` | cover title 68px / 700 | **17.99** | AA large | PASS |
| `--ink #14171A` | `--paper #FFFFFF` | brokerage plate 11.5px / 600 caps | **17.99** | AA body | PASS |
| `--ink #14171A` | `--newsprint #F2F2EF` | figure stack labels 6.4px / 600 caps | **16.04** | AA body | PASS |
| `--ink #14171A` | `--stock #E5E6E1` | table `th` 7px / 700 caps | **14.34** | AA body | PASS |
| `--ink #14171A` | `--stock #E5E6E1` | phone block heading 7.5px / 700 caps | **14.34** | AA body | PASS |
| `--ink #14171A` | `--spot-wash #F7EFED` | NOT FOUND head 19.5px / 700 italic | **15.87** | AA large | PASS |
| `--ink-2 #333A40` | `--paper #FFFFFF` | deck 14.5px / 400 italic | **11.54** | AA body | PASS |
| `--ink-2 #333A40` | `--paper #FFFFFF` | cover subtitle 19px / 400 italic | **11.54** | AA body | PASS |
| `--ink-2 #333A40` | `--paper #FFFFFF` | table `td` 8.6px / 400 | **11.54** | AA body | PASS |
| `--ink-2 #333A40` | `--newsprint #F2F2EF` | table `td` on zebra row 8.6px / 400 | **10.29** | AA body | PASS |
| `--ink-2 #333A40` | `--stock #E5E6E1` | phone block body 11.5px / 400 | **9.20** | AA body | PASS |
| `--ink-2 #333A40` | `--spot-wash #F7EFED` | NOT FOUND body 11.6px / 400 | **10.18** | AA body | PASS |
| `--ink-3 #5C646C` | `--paper #FFFFFF` | source strip agate 6.2px / 400 | **6.01** | AA body | PASS |
| `--ink-3 #5C646C` | `--paper #FFFFFF` | running head 7.5px / 600 caps | **6.01** | AA body | PASS |
| `--ink-3 #5C646C` | `--paper #FFFFFF` | cutline 8.5px / 400 | **6.01** | AA body | PASS |
| `--ink-3 #5C646C` | `--paper #FFFFFF` | edition block 9.5px / 400 | **6.01** | AA body | PASS |
| `--ink-3 #5C646C` | `--newsprint #F2F2EF` | figure term labels 6.5px / 600 caps | **5.36** | AA body | PASS |
| `--spot #7A2019` | `--paper #FFFFFF` | kicker 8.5px / 700 caps | **10.25** | AA body | PASS |
| `--spot #7A2019` | `--paper #FFFFFF` | cover eyebrow 10px / 700 caps | **10.25** | AA body | PASS |
| `--spot #7A2019` | `--paper #FFFFFF` | footnote figures 7.5px / 600 | **10.25** | AA body | PASS |
| `--spot #7A2019` | `--paper #FFFFFF` | NOT FOUND table cell 7px / 700 caps | **10.25** | AA body | PASS |
| `--spot #7A2019` | `--paper #FFFFFF` | phone numbers 12px / 700 | **10.25** | AA body | PASS |
| `--spot #7A2019` | `--paper #FFFFFF` | soft close closer 12.3px / 400 italic | **10.25** | AA body | PASS |
| `--spot #7A2019` | `--paper #FFFFFF` | VERIFIED stamps 6.2px / 700 caps | **10.25** | AA body | PASS |
| `--spot #7A2019` | `--newsprint #F2F2EF` | NOT FOUND cell on zebra row 7px / 700 | **9.14** | AA body | PASS |
| `--spot #7A2019` | `--spot-wash #F7EFED` | figure "special assessment" layer 6.4px / 600 | **9.04** | AA body | PASS |
| `--paper #FFFFFF` | `--spot #7A2019` | CTA button 16px / 700 caps | **10.25** | AA body | PASS |
| `--paper #FFFFFF` | `--spot #7A2019` | NOT FOUND register stamp 7px / 700 caps | **10.25** | AA body | PASS |
| `--paper #FFFFFF` | `--spot-deep #5E1C16` | CTA hover 16px / 700 caps | **12.70** | AA body | PASS |
| `--paper #FFFFFF` | `--ink #14171A` | photo well tag 8.5px / 600 caps | **17.99** | AA body | PASS |
| `--rule #8E938D` | `--paper #FFFFFF` | functional hairline, non-text | **3.13** | 3:1 non-text | PASS |
| scaffold `#F4F4F2` | scaffold `#5F5F5F` | preview caption 11px / 600 caps | **5.80** | AA body | PASS |
| scaffold `#EAEAE6` | scaffold `#5F5F5F` | preview caption note 11px / 400 | **5.29** | AA body | PASS |

**Lowest ratio in use anywhere: 3.13**, and that is a non-text hairline against a 3:1 target. **Lowest ratio on any text: 5.29**, in the preview scaffolding. **Lowest ratio on any shipping text: 5.36.** No FAIL anywhere.

`--rule-hair #BFC3BE` computes at **1.78:1** on paper and is therefore restricted by rule: it may only appear where an adjacent stronger rule, a zebra band, or the text itself already carries the structure. It is never the only thing telling a reader that two rows are different rows.

### Grayscale conversion of every ink

Computed by gamma-encoding the relative luminance.

| Token | Colour | Grayscale |
|---|---|---|
| `--ink` | `#14171A` | `#171717` |
| `--ink-2` | `#333A40` | `#393939` |
| `--spot` | `#7A2019` | `#414141` |
| `--spot-deep` | `#5E1C16` | `#333333` |
| `--ink-3` | `#5C646C` | `#636363` |
| `--rule` | `#8E938D` | `#929292` |
| `--rule-hair` | `#BFC3BE` | `#C2C2C2` |
| `--stock` | `#E5E6E1` | `#E5E5E5` |
| `--newsprint` | `#F2F2EF` | `#F2F2F2` |
| `--spot-wash` | `#F7EFED` | `#F1F1F1` |

**The three path tabs land at 23, 65 and 229.** That is the separation the wayfinding depends on, and it survives.

**Known collapse, disclosed:** `--spot` (`#414141`) and `--ink-2` (`#393939`) are eight grey levels apart. In black and white they are effectively the same tone. This is acceptable only because the spot never carries meaning alone: NOT FOUND cells also print the words NOT FOUND in caps with an underline, kickers also sit above a rule in tracked caps, footnote figures are also superior and bracketed, and the CTA is a reversed solid block. See `rationale.md` for the full grayscale audit.

---

## 3. Type

### Families

| Role | Family | Why |
|---|---|---|
| Display | **Newsreader** | A news serif with real ink-trap-era character and a variable optical-size axis, so a 68px cover title and a 19.5px callout head are drawn differently rather than scaled. High contrast, editorial, and nothing like Playfair Display. |
| Body | **Source Serif 4** | Low-contrast, large x-height, sturdy at 8pt to 10pt on a home laser printer. Its neutrality is the point: it lets Newsreader do all the shouting. |
| Furniture | **IBM Plex Sans** | Kickers, running heads, datelines, table headers, source strip, folios, buttons. Plex reads as a technical record, has an unambiguous `l` and `1`, and sets narrow enough to survive nineteen full URLs at 6.2px. |

Pairing a **high-contrast display serif over a low-contrast text serif**, with a technical sans doing every piece of furniture, is exactly how a serious newspaper is built. None of the three is on the forbidden list.

### Exact Google Fonts URL

```
https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,600;1,6..72,700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&display=swap
```

Weights loaded: Newsreader 400/500/600/700 roman and 400/600/700 italic across `opsz 6..72`; Source Serif 4 400/600/700 roman and 400 italic across `opsz 8..60`; IBM Plex Sans 400/500/600/700.

Fallback stacks: `Newsreader, Georgia, "Times New Roman", serif` / `"Source Serif 4", Georgia, "Times New Roman", serif` / `"IBM Plex Sans", "Helvetica Neue", Arial, sans-serif`.

### Type scale

Sizes are px at 96dpi, which is what an 8.5in page box uses. The point equivalent is given because print is the primary medium.

| Element | Family | px | pt | Line height | Tracking |
|---|---|---|---|---|---|
| Cover title | Newsreader 700 | 68 | 51.0 | 0.96 | -0.028em |
| Cover subtitle | Newsreader 400 italic | 19 | 14.3 | 1.36 | 0 |
| Cover credibility strapline | Newsreader 600 italic | 16.5 | 12.4 | 1.35 | 0 |
| Cover byline name | Newsreader 600 | 25 | 18.8 | 1.0 | -0.012em |
| Cover eyebrow | Plex Sans 700 caps | 10 | 7.5 | 1.0 | 0.30em |
| Cover geography line | Plex Sans 600 caps | 10.5 | 7.9 | 1.0 | 0.24em |
| Brokerage plate | Plex Sans 600 caps | 11.5 | 8.6 | 1.0 | 0.17em |
| Edition block | Plex Sans 400 | 9.5 | 7.1 | 1.62 | 0.03em |
| Compliance line | Plex Sans 400 | 9 | 6.8 | 1.70 | 0.02em |
| Interior headline | Newsreader 700 | 35 | 26.3 | 1.02 | -0.024em |
| Page 20 section head | Newsreader 700 | 24 | 18.0 | 1.10 | -0.012em |
| Deck | Newsreader 400 italic | 14.5 | 10.9 | 1.33 | 0 |
| Subhead | Newsreader 700 | 16.5 | 12.4 | 1.10 | -0.012em |
| **Body prose** | **Source Serif 4 400** | **13.1** | **9.8** | **1.39** | **0** |
| Beat line | Newsreader 600 | 14.2 | 10.7 | 1.39 | 0 |
| Pull callout | Newsreader 400/700 | 13 | 9.8 | 1.36 | 0 |
| NOT FOUND head | Newsreader 700 italic | 19.5 | 14.6 | 1.04 | -0.02em |
| NOT FOUND body | Source Serif 4 400 | 11.6 | 8.7 | 1.36 | 0 |
| Table body | Source Serif 4 400 | 8.6 | 6.5 | 1.20 | 0 |
| Table district id | Plex Sans 700 | 9.4 | 7.1 | 1.20 | 0 |
| Table header | Plex Sans 700 caps | 7 | 5.3 | 1.20 | 0.11em |
| Table caption | Plex Sans 700 caps | 7.2 | 5.4 | 1.30 | 0.16em |
| Phone block body | Source Serif 4 400 | 11.5 | 8.6 | 1.34 | 0 |
| Phone number | Plex Sans 700 | 12 | 9.0 | 1.34 | 0.01em |
| Soft close | Newsreader 400 | 12.3 | 9.2 | 1.31 | 0 |
| Kicker | Plex Sans 700 caps | 8.5 | 6.4 | 1.0 | 0.22em |
| Running head | Plex Sans 600 caps | 7.5 | 5.6 | 1.0 | 0.19em |
| Folio | Plex Sans 700 caps | 9 | 6.8 | 1.0 | 0.14em |
| **Source strip agate** | **Plex Sans 400** | **6.2** | **4.7** | **1.23** | **0** |
| Source strip head | Plex Sans 700 caps | 6.8 | 5.1 | 1.0 | 0.22em |
| VERIFIED stamp | Plex Sans 700 caps | 6.2 | 4.7 | 1.23 | 0.08em |
| Footnote figure | Plex Sans 600 | 7.5 | 5.6 | 0 | 0.02em |
| Cutline | Plex Sans 400 | 8.5 | 6.4 | 1.45 | 0 |
| Hero headline | Newsreader 700 | clamp(34, 4.4vw, 62) | | 0.99 | -0.03em |
| Hero subhead | Newsreader 400 italic | clamp(16, 1.42vw, 20) | | 1.42 | 0 |
| Hero prop head | Newsreader 700 | clamp(17, 1.5vw, 20) | | 1.17 | -0.015em |
| Hero prop body | Source Serif 4 400 | clamp(14, 1.05vw, 15) | | 1.52 | 0 |
| CTA button | Plex Sans 700 caps | 16 | | 1.0 | 0.13em |
| Trust line | Plex Sans 400/700 | 12 | | 1.85 | 0.03em |

**Body prose is set at 9.8pt, not the 10.5pt the page budget assumes.** That is a disclosed deviation forced by the sample copy. See `rationale.md`, "What did not fit".

**Source strip is set at 4.7pt, not the 7pt the brief specifies.** Also disclosed. Nineteen entries with full paths do not fit at 7pt on a spread that already carries a 20 row table.

---

## 4. Measure and columns

| Surface | Columns | Column width | Characters per line |
|---|---|---|---|
| Page 19 body | 3 | 2.30in | about 35 |
| Page 20 body | 3 | 2.30in | about 35 |
| NOT FOUND callout | 2, spanning all | 3.55in | about 60 |
| Source strip | 3 | 2.34in | about 55 |
| Cover | 1 | 7.00in | n/a, display only |
| Hero, desktop | 3 for props, 1.62fr + 1fr above | fluid | 45 to 60 |
| Hero, mobile | 1 | fluid | 38 to 48 |

Thirty-five characters is a newspaper measure. It is also the right measure for a reader at a sixth grade level, who does better with short lines than with a wide one.

---

## 5. Spacing scale

`2 · 4 · 6 · 8 · 12 · 16 · 20 · 26 · 34 · 44 · 58` px. Exposed as `--s1` through `--s11`.

Guide page margins: top `0.34in`, bottom `0.30in`, outer `0.44in`, inner `0.50in`. Cover margins: `0.78in` top, `0.75in` sides, `0.62in` bottom. Column gutter `0.19in`. Source strip gutter `0.15in`.

Margins are deliberately tight. A broadsheet does not have generous margins, and the guide cannot afford them.

---

## 6. Rule weights

| Name | Weight | Colour | Use |
|---|---|---|---|
| Hairline | 0.5px to 1px | `--rule-hair` | Decorative only. Column rules in the source strip, checklist row separators, table row separators. |
| Thin | 1px | `--rule` | Functional separators, geography line, cover section rules. |
| Medium | 1.5px to 2px | `--ink` | Subhead rules, compliance rule, brokerage plate border. |
| Heavy | 3px | `--ink` | Headline rule, pull callout top rule, phone block frame. |
| Double | 3px double | `--ink` | Source strip top. The only double rule in the system, and it means "the record starts here". |
| Banner | 7px ink + 2.5px spot | `--ink` + `--spot` | Cover masthead only. Appears once in 39 pages. |
| Callout | 5px top, 2px bottom | `--spot` | NOT FOUND panel only. |

---

## 7. Radii

**Zero. Everywhere.** No element in this system has a rounded corner, including the CTA button. A rounded corner is a software convention, not a printing one, and this direction is arguing that the document is a printed record.

---

## 8. Print rules

```css
@page { size: letter; margin: 0; }
```

Page boxes carry their own margins as padding, so `@page` margin is zero and the trim is exact.

- `print-color-adjust: exact` and `-webkit-print-color-adjust: exact` on every page box, every tinted band, the table header, the NOT FOUND panel, the phone block, and globally inside `@media print`.
- `break-inside: avoid` on the pull callout, the NOT FOUND callout, the figure, the table wrapper, each table, the phone block, the soft close, the source strip, and every `li` in the numbered list, the checklist and the source strip.
- `thead { display: table-header-group }` on every data table so the header repeats if a long table breaks across pages.
- `break-after: page` on each `.page`.
- **No `position: fixed` anywhere in the guide panels.** Zero occurrences in the whole file. `position: absolute` is used only for the photo-well tag and the figure tick label, both inside a `position: relative` parent that never crosses a page break.
- Bullets and list markers are **flex children**, never `li::before { position: absolute }`. Under CSS multi-column an absolute marker lands on the first letter, and this system runs three columns on almost every page.
- The preview scaffolding (`.cap`, the hero panel, the gray stage) is hidden in `@media print` so the file prints as pages, not as a presentation.

---

## 9. Motion

Screen only. The guide has none.

- Only `transform` and `opacity` animate. Never `transition-all`.
- CTA: `transition: background-color .16s cubic-bezier(.2,.8,.3,1), transform .16s cubic-bezier(.2,.8,.3,1)`.
- Hover: background to `--spot-deep`. Active: `translateY(1px)`. Focus-visible: `3px solid var(--ink)` outline at `3px` offset, which is a real focus ring, not a colour change.

---

## 10. The three-path wayfinding system

Distinguished by **value**, then reinforced three more ways so no single failure loses the reader.

| Path | Tab fill | Tab text colour | Grayscale byte | Folio | Running head |
|---|---|---|---|---|---|
| A | `--path-a #14171A` | `--paper` | 23 | `6 · A` to `9 · A` | Path A · Moving here from out of state |
| B | `--path-b #7A2019` | `--paper` | 65 | `10 · B` to `13 · B` | Path B · Moving up inside the valley |
| C | `--path-c #E5E6E1` | `--ink` | 229 | `14 · C` to `17 · C` | Path C · Your first new build |

Tabs bleed off the outer edge on pages 6 to 17 only, stepped top third / middle third / bottom third, with no text within 5mm of the trim. On screen the tab is replaced by a text path label set in Plex Sans 700 caps at 8.5px with `0.22em` tracking above the headline, in the path's own ink, and that label is never print-only.

---

## 11. The NOT FOUND treatment, both scales

**Full callout** (once per page at most): `--spot-wash` panel, 5px `--spot` top rule, 2px `--spot` bottom rule, a reversed `--spot` register stamp reading `NOT FOUND REGISTER · ITEM n`, and a Newsreader 700 italic head. It occupies the full measure and spans all columns.

**Table cell:** Plex Sans 700 caps at 7px, `0.10em` tracking, `--spot`, with a 1.5px `--spot` underline. The words NOT FOUND are always printed. The colour is decoration on top of the words, never a substitute for them.

---

## 12. The dateline system

Every verified fact carries its date where the reader can see it, at three scales:

1. **Page level.** The running head carries `VERIFIED 2026-07-25` in a hairline box at the inner edge.
2. **Object level.** Every table `<caption>` ends with `VERIFIED 2026-07-25` set in `--spot`.
3. **Claim level.** Every source strip entry ends with a `VERIFIED 2026-07-25` stamp in `--spot` 700 caps, so the date is the last thing on every single citation rather than a footnote to the footnotes.

URLs in the source strip print **without the scheme and without `www.`**, full path retained, set in Plex Sans with `overflow-wrap: anywhere`. A printed URL does not need `https://`, and dropping it recovers about eleven characters on nineteen entries.

---

**Em-dashes in this file: zero.**
