# Direction 6 · Ledger · Design Tokens

**Thesis:** new construction is a series of line items, and this guide prices every one.

Every value below is the value actually used in `preview.html`. Nothing here is aspirational.

---

## 1. Color

| Token | Hex | Role |
|---|---|---|
| `--paper` | `#FAFAF7` | Page stock. Cool bone, not a warm cream. |
| `--white` | `#FFFFFF` | Knockout boxes: checkbox wells, the phone register, landing page card fills. |
| `--ledger` | `#E8EEE9` | The figures rail ground. Columnar pad green at 7 percent ink. |
| `--ledger-deep` | `#D3DFD6` | Brought forward and carried forward total bands. |
| `--unknown` | `#F1EBDD` | Ground for any unpriced value. **Never used without a 45 degree hatch and the literal words.** |
| `--ink` | `#131A16` | Primary text, headlines, hard rules, reversed band grounds. |
| `--ink-2` | `#39443E` | Deck, secondary prose, table `where` column, rail labels. |
| `--muted` | `#54605A` | Audit trail, running heads, folios, column heads, captions. |
| `--rule` | `#BFC9C3` | Hairlines, row separators, cover sheet ruling. Non-text. |
| `--rule-strong` | `#8A968F` | Column rules, table head rule, checkbox borders. Non-text. |
| `--debit` | `#A83A14` | Money that leaves your pocket. Figures, footnote markers, NOT FOUND label, hatch. |
| `--debit-deep` | `#7A2410` | Reversed NOT FOUND tag ground. |
| `--credit` | `#093026` | Action and settled state. CTA ground, hero headline, retired district rule, brokerage slot. |
| `--credit-2` | `#0C4438` | CTA hover only. |

Scaffolding gray `#6b6b6b` around the page boxes is preview furniture and is not part of the palette.

### Why this palette

Financial statements are printed on tinted columnar stock with black narrative and a single warm accent for amounts that matter. The green is the accounting pad; the rust is red ink without the alarm; the deep green-black is the settled column. It sits nowhere near Rose Homes LV navy `#1C2333` or champagne `#C9A86E`, and nowhere near a builder's marketing blue.

---

## 2. WCAG contrast, computed

Ratios computed in Python from sRGB relative luminance, `(L1+0.05)/(L2+0.05)`, rounded to two decimals. AA threshold is 4.5:1 for body and 3:1 for large text (24px+, or 18.66px+ at 700).

| Foreground | Background | FG hex | BG hex | Ratio | Used at | AA |
|---|---|---|---|---|---|---|
| ink | paper | `#131A16` | `#FAFAF7` | 16.92 | 14px / 400 body prose | PASS |
| ink | white | `#131A16` | `#FFFFFF` | 17.69 | 16.5px / 400 hero subhead | PASS |
| ink-2 | paper | `#39443E` | `#FAFAF7` | 9.70 | 15px / 400 deck, 10.2px / 400 table | PASS |
| ink-2 | white | `#39443E` | `#FFFFFF` | 10.14 | 13.5px / 400 hero prop body | PASS |
| muted | paper | `#54605A` | `#FAFAF7` | 6.28 | 8.9px / 400 audit trail | PASS |
| muted | paper | `#54605A` | `#FAFAF7` | 6.28 | 9.5px / 500 running head, folio | PASS |
| muted | ledger | `#54605A` | `#E8EEE9` | 5.58 | 7.5px / 600 rail column heads | PASS |
| ink | ledger | `#131A16` | `#E8EEE9` | 15.03 | 10px / 700 rail amounts | PASS |
| ink-2 | ledger | `#39443E` | `#E8EEE9` | 8.62 | 9.5px / 400 rail item labels | PASS |
| ink | ledger-deep | `#131A16` | `#D3DFD6` | 12.89 | 10.5px / 700 total figures | PASS |
| muted | ledger-deep | `#54605A` | `#D3DFD6` | **4.78** | 7.2px / 700 total band caption | PASS |
| debit | paper | `#A83A14` | `#FAFAF7` | 6.12 | 11px / 700 marker, 12px / 700 phone | PASS |
| debit | ledger | `#A83A14` | `#E8EEE9` | 5.44 | 10px / 700 cost figures in the rail | PASS |
| debit | unknown | `#A83A14` | `#F1EBDD` | 5.39 | 8 to 8.5px / 700 NOT FOUND label | PASS |
| ink | unknown | `#131A16` | `#F1EBDD` | 14.88 | 13px / 400 disclosure body | PASS |
| debit-deep | paper | `#7A2410` | `#FAFAF7` | 9.62 | 14px / 600 inline emphasis | PASS |
| white | debit-deep | `#FFFFFF` | `#7A2410` | 10.06 | 8.5px / 700 reversed NOT FOUND tag | PASS |
| credit | paper | `#093026` | `#FAFAF7` | 13.73 | 14.5px / 500 soft close ask | PASS |
| credit | white | `#093026` | `#FFFFFF` | 14.36 | 52px / 600 hero headline | PASS |
| paper | credit | `#FAFAF7` | `#093026` | 13.73 | 17px / 600 CTA button label | PASS |
| paper | ink | `#FAFAF7` | `#131A16` | 16.92 | 8 to 8.5px / 700 reversed band labels | PASS |
| credit-2 | paper | `#0C4438` | `#FAFAF7` | 10.57 | CTA hover ground | PASS |
| rule-strong | paper | `#8A968F` | `#FAFAF7` | 2.94 | non-text rules only | n/a |
| rule | paper | `#BFC9C3` | `#FAFAF7` | 1.63 | non-text hairlines only | n/a |

**Lowest text ratio actually used: 4.78:1.** Zero FAILs. No pair was adjusted after the fact; `--muted` on `--ledger-deep` was the binding constraint and set the darkness of `--muted`.

### Grayscale values (sRGB luminance to gray)

| Token | Gray | Token | Gray |
|---|---|---|---|
| paper | 98.0% | ink | 9.6% |
| ledger | 92.7% | ink-2 | 25.7% |
| unknown | 92.3% | muted | 36.5% |
| ledger-deep | 86.2% | debit | 37.2% |
| rule | 77.8% | debit-deep | 25.9% |
| rule-strong | 57.7% | credit | 16.5% |

Two collisions are known and designed around: `ledger` and `unknown` are 0.4 points apart, and `debit` and `muted` are 0.7 points apart. **No meaning may rest on either pair.** Every unknown carries a hatch, a hairline border, and the literal string `NOT FOUND`.

---

## 3. Type

Three families, because a ledger has three voices: narrative, label, amount.

| Role | Family | Weights | Why |
|---|---|---|---|
| Display | **Newsreader** | 400, 500, 600 + italic 400 | Transitional serif with real optical sizing. Financial press, not luxury real estate. Carries the headline, deck, asides, disclosures, soft close. |
| Text | **IBM Plex Sans** | 400, 500, 600, 700 | Wide apertures, plain at 6th grade reading level, ships genuine tabular lining figures. |
| Figure | **IBM Plex Mono** | 400, 500, 600, 700 | Every amount, every reference numeral, every URL, every date column. Monospace is the ledger's native hand. |

```
https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300..700;1,6..72,300..600&display=swap
```

Global: `font-variant-numeric: tabular-nums lining-nums` on `body`. Every numeral in the guide is the same width as every other numeral. That is non-negotiable in this direction.

### Scale, print pages (px at 96dpi, pt = px x 0.75)

| Element | Size / line-height | Tracking | Family, weight |
|---|---|---|---|
| Cover title | 78 / 0.95 | -0.032em | Newsreader 600 |
| Cover subtitle | 17.5 / 1.40 | 0 | Newsreader 400 |
| Cover eyebrow | 10 / 1.0 | 0.26em caps | Mono 600 |
| Geography strip | 11.5 / 1.0 | 0.16em caps | Mono 600 |
| Credibility line | 13 / 1.50, figure 15 | 0 | Plex Sans 400 / Mono 700 |
| Byline name | 23 / 1.0 | -0.02em | Newsreader 600 |
| Brokerage slot | 13.5 / 1.0 | 0.10em caps | Plex Sans 600 |
| Compliance line 1 | 11.5 / 1.50 | 0 | Plex Sans 500 |
| Compliance line 2 | 10.5 / 1.60 | 0.02em | Mono 400 |
| Licence slot | 11 / 1.0 | 0 | Mono 700, `min-width:13ch` |
| Page headline h1 | 25.5 / 1.06 | -0.020em | Newsreader 500 |
| Deck | 15 / 1.38 | 0 | Newsreader italic 400 |
| Subhead h2 | 18 / 1.20 | -0.012em | Newsreader 600 |
| Body prose | **14 / 1.47** (10.5pt) | 0 | Plex Sans 400 |
| Numbered / check list | 13.2 / 1.44 | 0 | Plex Sans 400, markers Mono 700 |
| Aside body | 14 / 1.40 | 0 | Newsreader 400 |
| Aside tag | 8.5 / 1.0 | 0.20em caps | Mono 600 |
| Disclosure heading | 19 / 1.14 | -0.015em | Newsreader 600 |
| Disclosure body | 13 / 1.48 | 0 | Plex Sans 400 |
| Table caption | 8 / 1.0 | 0.18em caps | Mono 700 |
| Table `th` | 7.5 / 1.0 | 0.13em caps | Mono 700 |
| Table `td` | 10.2 / 1.18 | 0 | Plex Sans 400 |
| Table district cell | 10.5 / 1.18 | -0.02em | Mono 700 |
| Table date cell | 9.5 / 1.18 | -0.03em | Mono 400 |
| Source marker, inline | 7 superscript | 0 | Mono 600 |
| Rail head band | 8.5 / 1.0 | 0.19em caps | Mono 700 reversed |
| Rail column head | 7.5 / 1.0 | 0.16em caps | Mono 600 |
| Rail item label | 9.5 / 1.30 | 0 | Plex Sans 400 |
| Rail amount | 10 / 1.0 | -0.01em | Mono 700 |
| Rail line number | 7.5 / 1.0 | 0 | Mono 600 |
| NOT FOUND chip | 8 to 8.5 / 1.0 | 0.06em caps | Mono 700 |
| Total band caption | 7.2 / 1.0 | 0.15em caps | Mono 700 |
| Total band figure | 10.5 / 1.0 | 0 | Mono 700 |
| Phone register title | 8 / 1.0 | 0.17em caps | Mono 700 |
| Phone number | 12 / 1.0 | -0.02em | Mono 700 |
| Running head | 9.5 / 1.0 | 0.17em caps | Mono 500 |
| Folio numeral | 12 / 1.0 | 0.14em | Mono 700 |
| Audit trail heading | 8 / 1.0 | 0.20em caps | Mono 700 |
| Audit trail entry | **8.9 / 1.26** | 0 | Plex Sans 400 |
| Audit trail URL | 7.35 / 1.26 | 0 | Mono 400, `overflow-wrap:anywhere` |
| Soft close | 14.5 / 1.42 | 0 | Newsreader 400, ask line 500 |
| Marginal ref numeral | 9 / 1.50 | 0.02em | Mono 600 |

### Scale, landing hero

| Element | Desktop | 900px and below | 420px and below |
|---|---|---|---|
| Hero h1 | 52 / 1.02 / -0.028em | 34 / -0.022em | 30 |
| Hero subhead | 16.5 / 1.60 | 15.5 | 15 |
| CTA label | 17 / 600 | 16.5, full width | 16.5 |
| Prop heading | 20 / 1.18 / -0.016em | 20 | 18 |
| Prop body | 13.5 / 1.50 | 13.5 | 13.5 |
| Statement total figure | 17 Mono 700 | 17 | 17 |
| Trust line 1 | 14 / 500 | 13 | 13 |
| Trust lines 2 and 3 | 12.5 Mono | 11.5 | 11.5 |

---

## 4. Spacing, rules, radii

**Spacing scale, 4px base:** `4 · 8 · 12 · 16 · 22 · 30 · 40 · 54 · 72`. Nothing in the system uses a value outside this scale except optical corrections on rule offsets.

**Rule weights, four only:**

| Token | Weight | Meaning |
|---|---|---|
| `--hair` | 0.5px | Row separator inside a ledger block, audit trail column rule |
| `--line` | 1px | Column boundary, table head underline, box border |
| `--bar` | 2px | Section rule, deck underline, h2 topper, trust line, table head topper |
| `--heavy` | 3px | Audit trail topper, disclosure topper, and 3px **double** for totals |

The 3px double rule is reserved. It appears only on a brought forward or carried forward total. That is the single strongest typographic mark in the guide and it is spent on the running cost.

**Radii: 0 everywhere.** No rounded corners on any element, including the CTA. A ledger has no rounded corners.

---

## 5. Print rules

```css
@page { size: letter; margin: 0; }
* { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
```

- Page box is the full trim: `8.5in x 11in`, padding `44px 48px 40px` (0.46in top, 0.5in sides, 0.42in bottom).
- **The ledger grid, 720px live width:** ref rail `34` · gap `12` · text column `448` · gap `16` · figures rail `210`. Identical on verso and recto. Reference on the left, description in the middle, amount on the right, on every page, without mirroring. This is a general ledger row, not a book spread.
- `break-inside: avoid` on `.aside`, `.disclose`, `.railbox`, `.svgwrap`, `.tw`, `.bf`, `.cf`, `.softclose`, every `tbody tr`, every `li`.
- `thead { display: table-header-group }` so the district header repeats if the table ever breaks.
- **No `position: fixed` anywhere in the guide.** The bottom anchored total uses `position: absolute` inside its own page box, which does not repeat.
- Bullets and checkboxes use `display:flex` with the marker as a real flex child. No `::before { position:absolute }` anywhere.
- Measured ink: **cover 7.79%, page 19 8.36%, page 20 7.90%.** Only 4.7 to 5.6 percent of pixels fall below 50 percent reflectance.
- The licence slot is a monospace inline-block with `min-width: 13ch` at the end of its line inside a bottom anchored band. A real Nevada number (9 to 13 characters) drops in with zero reflow.
