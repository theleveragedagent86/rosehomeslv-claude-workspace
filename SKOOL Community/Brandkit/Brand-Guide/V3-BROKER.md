# The Leveraged Agent, palette v3 "Broker"

**Status: DEAD.** Superseded on 2026-08-19 when Ryan adopted v4 `Vector` as brand v2.0 ([tokens.css](tokens.css), spec in [BRAND-GUIDE.md](BRAND-GUIDE.md), record in [V4-PALETTES.md](V4-PALETTES.md)). This file is kept as a decision record only, do not use it. Nothing in the workspace consumes this file yet. Built 2026-08-19 at Ryan's request.

Files: [tokens-v3-broker.css](tokens-v3-broker.css), [tokens-v3-broker.json](tokens-v3-broker.json).
Evidence: [PEDIGREE-BRAND-RESEARCH.md](PEDIGREE-BRAND-RESEARCH.md) and [pedigree-board.html](pedigree-board.html), section 04.

## Why v3 exists

v2 (Voltage, Ember) was designed from contrast math and taste. v3 is designed from **measured convention**. Ten high-pedigree US brokerages were sampled off their live sites, area-weighted, with fonts harvested from their actual `@font-face` rules. Four findings drove this palette:

1. The base surface is achromatic in 9 of 10. **Not one uses a tinted cream as the page surface.** That, not the gold, is why v1 does not pop.
2. There is exactly one accent, covering almost no area. Three of the ten ship zero chromatic accent.
3. Ink is a near-black with a color cast, usually blue or navy, never pure `#000` in the modern brands.
4. Exactly two fonts. Never one, never three.

Ryan's existing colors already satisfy 2, 3 and 4. His gold `#E8A33D` is effectively the Altman Brothers' `#D2AD41`, and `#08343E` is exactly the tinted near-black pattern. **Only the base surface is off-convention.** So v3 is the cheapest of the three candidates: it changes the background to white, deletes sage, and touches nothing else in the brand.

## What changes from v1

| Change | From | To | Why |
|---|---|---|---|
| Primary surface | cream `#F5F2EB` | pure white `#FFFFFF` | 9 of 10 pedigree brands, zero use tinted cream |
| Sunken fill | `#EAE6DA` | `#F7F7F7` | Serhant's measured near-white |
| Sage | `#B5CAC4` | **deleted** | decorative only, 1.54:1, did no work |
| Second accent | none in v1 | still none | rule 2, one accent only |
| Heading weight | Poppins 700 | Poppins **800** | Serhant runs 800, Ferry 700 |
| Labels | sentence case | uppercase, `+0.14em` | rule 6, every pedigree brand tracks labels wide |
| Deep `#08343E` | dark surface | unchanged, now also ink | no change to the color itself |
| Gold `#E8A33D` | accent | unchanged | already the pedigree gold |

Logo files stay valid. They were already built to sit on white or on deep, so nothing needs re-export.

## Tokens

Same semantic schema as v2, so v3 is a drop-in swap for either v2 file: one `<link>` change.

| Token | Hex | Role | Contrast |
|---|---|---|---|
| `--la-bg` | `#FFFFFF` | primary surface, pure white. Do not tint it | |
| `--la-bg-2` | `#F7F7F7` | sunken fill, table rows, inset panels | |
| `--la-bg-inv` | `#08343E` | inverted surface, brand deep teal playing black's role | |
| `--la-line` | `#E3E7E8` | hairline and divider on bg, non-text | 1.25 on bg |
| `--la-structure` | `#0F4C5C` | canonical teal. Chart bars, structural fills, large headings | 9.51 / 8.88 |
| `--la-ink` | `#08343E` | primary text on bg | 13.37 / 12.48 |
| `--la-ink-2` | `#3C646F` | secondary text on bg and bg-2 | 6.47 / 6.04 |
| `--la-ink-inv` | `#FFFFFF` | primary text on bg-inv | 13.37 |
| `--la-ink-2-inv` | `#90ABB2` | secondary text on bg-inv | 5.51 |
| `--la-accent` | `#E8A33D` | THE accent. Fills and buttons, never text on bg | 6.2 on bg-inv |
| `--la-accent-on` | `#08343E` | text placed ON accent | 6.2 |
| `--la-accent-txt` | `#9D6513` | accent used AS text on bg or bg-2 | 4.88 / 4.55 |
| `--la-accent-inv` | `#E8A33D` | accent used AS text on bg-inv, raw gold works there | 6.2 |

Every number above is WCAG 2.1 relative luminance, computed not eyeballed. Secondary text was solved to 6.0 rather than 4.5 so it holds up at small sizes.

Two failures worth naming, because both are easy to trip:
- Gold on white is **2.16:1**. It can never be text on `bg`. Use `--la-accent-txt`.
- White on gold is **1.86:1**. Buttons take `--la-accent-on` (`#08343E`), not white.

### Deliberate omissions

- **No `--la-accent-2` trio.** v2 shipped one. v3 does not, on purpose. One accent covering almost no area is the single most consistent finding in the research, and it is what separates the pedigree brands from typical agent branding.
- **No `--la-accent-txt-inv`.** Gold is 6.2:1 on deep, so the raw accent is already legible there. `--la-accent-inv` carries the same hex for clarity.
- **Sage is gone.** Delete it, do not remap it.

`--la-ink-2-inv` is a v3 addition. Ember's schema had no secondary-on-dark value, and a white-on-deep system needs one.

### Migration from v1

| v1 | v3 Broker |
|---|---|
| `--la-cream` | `--la-bg` (value changes to `#FFFFFF`) |
| `--la-cream-sunk` | `--la-bg-2` (value changes to `#F7F7F7`) |
| `--la-deep` | `--la-bg-inv` and `--la-ink` (same hex, two roles) |
| `--la-teal` | `--la-structure` |
| `--la-teal-muted` | `--la-ink-2` (value changes to `#3C646F`) |
| `--la-gold` | `--la-accent` (unchanged hex) |
| `--la-gold-ink` | `--la-accent-txt` (value changes to `#9D6513`) |
| `--la-sage` | **dropped** |

## Type rules that come with this palette

Colors alone will not get the pedigree read. The three type moves matter as much:

1. **Poppins 800** for headlines, `-0.03em` tracking. v1's 700 reads soft next to Serhant and Ferry.
2. **Inter uppercase, `+0.14em`** for eyebrows, labels, nav, and section markers. Every brand in the sample tracks labels between +1.28px and +2px.
3. **Two fonts only.** Poppins and Inter. This is already structurally the Serhant and Real Broker pattern, and Real Broker literally ships Inter for body, so no font change is needed, only a weight change.

## Open item

The research found that the wordmark alone is the logo in all ten brands, no icon, no house, no key, no roof. The Leveraged Agent has no tagline-free wordmark lockup for placements under the 240px minimum width. That gap is now the highest-value logo work outstanding, independent of which palette ships.
