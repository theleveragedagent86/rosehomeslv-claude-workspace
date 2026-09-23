# The Leveraged Agent, palette v2 candidates

**Status: DEAD.** Superseded on 2026-08-19 when Ryan adopted v4 `Vector` as brand v2.0 ([tokens.css](tokens.css), spec in [BRAND-GUIDE.md](BRAND-GUIDE.md), record in [V4-PALETTES.md](V4-PALETTES.md)). This file is kept as a decision record only, do not use it. Nothing in the workspace consumes these files yet. Built 2026-08-19 at Ryan's request.

Preview both side by side: serve the workspace and open [v2-preview.html](v2-preview.html) at
`http://localhost:8091/SKOOL%20Community/Brandkit/Brand-Guide/v2-preview.html`.
Do not open it as `file://`, the fonts and token stylesheet will not load.

## Why v2 exists

v1 is light-first and low chroma. On cream `#F5F2EB` any accent has to stay dark to be legible, which caps how loud it can get: gold is 1.93:1 on cream and sage is 1.54:1, so neither can be text and neither can pop. Both v2 candidates fix that, by different routes.

- **Voltage** moves the primary surface to near-black. On a dark ground a fully saturated accent is still legible text, so the accent can be as loud as you want.
- **Ember** stays light-first but swaps the ochre gold for a true orange, the complement of the heritage teal. Maximum hue tension available inside a cream system.

## Token model, read this before using either

v2 uses **semantic** names, not color-literal ones. v1 called things `--la-cream` and `--la-gold`, which stops meaning anything the moment the palette changes (`--la-cream: #04171C` is nonsense). v2 names describe the role, so the two candidates are drop-in swappable with each other and with any future palette.

Both files define the identical 14 role tokens plus 4 type tokens. Swapping palettes is one `<link>` change.

| Role token | What it is |
|---|---|
| `--la-bg` | primary surface |
| `--la-bg-2` | second surface: cards, elevated panels, or sunken rows |
| `--la-bg-inv` | inverted surface, the opposite pole |
| `--la-line` | hairline and divider on `bg`, non-text |
| `--la-structure` | decorative brand color: chart bars, rules, circuit traces |
| `--la-ink` | primary text on `bg` |
| `--la-ink-2` | secondary text on `bg` |
| `--la-ink-inv` | primary text on `bg-inv` |
| `--la-accent` | primary accent, fills and buttons |
| `--la-accent-on` | text placed ON `accent` |
| `--la-accent-txt` / `-txt-inv` | the accent used AS text, darkened or lightened to pass |
| `--la-accent-2` | secondary accent |
| `--la-accent-2-on` | text placed ON `accent-2` |
| `--la-accent-2-txt` / `-txt-inv` | secondary accent used AS text |

The `-on` and `-txt` split is the part that matters. An accent bright enough to fill a button is almost never legible as text on the same surface, so each accent ships with a companion value for the other job. That is exactly the failure v1 has with gold.

### Migration from v1

| v1 | Voltage | Ember |
|---|---|---|
| `--la-cream` | `--la-bg-inv` | `--la-bg` |
| `--la-cream-sunk` | (none, use `--la-bg-2`) | `--la-bg-2` |
| `--la-deep` | `--la-bg` | `--la-bg-inv` |
| `--la-teal` | `--la-structure` | `--la-structure` |
| `--la-teal-muted` | `--la-ink-2` | `--la-ink-2` |
| `--la-gold` | `--la-accent-2` | `--la-accent` |
| `--la-gold-ink` | `--la-accent-2-txt-inv` | `--la-accent-txt` |
| `--la-sage` | (dropped) | (dropped) |

Sage is dropped in both. It was decorative-only at 1.54:1 and did no work.

## A. Voltage

Dark-first, high chroma, tech-forward. Keeps the teal DNA in the surface itself, so the brand still reads teal without teal having to carry text.

| Token | Hex | Role |
|---|---|---|
| `--la-bg` | `#04171C` | primary surface, near-black with a teal cast |
| `--la-bg-2` | `#0A2A33` | elevated surface, cards and panels |
| `--la-bg-inv` | `#F2EFE6` | bone, for light sections and print |
| `--la-line` | `#1B3239` | hairline, non-text |
| `--la-structure` | `#14586A` | decorative teal, chart bars and rules. **Never text**, 2.30:1 |
| `--la-ink` | `#F2EFE6` | primary text, 15.96:1 |
| `--la-ink-2` | `#7D98A1` | secondary text, 6.01:1 on bg, 4.94:1 on bg-2 |
| `--la-ink-inv` | `#04171C` | text on bone, 15.96:1 |
| `--la-accent` | `#2DE2C5` | aqua, 11.18:1 on bg, 9.19:1 on bg-2 |
| `--la-accent-on` | `#04171C` | text on aqua, 11.18:1 |
| `--la-accent-txt-inv` | `#0F7B65` | aqua as text on bone, 4.52:1 |
| `--la-accent-2` | `#FFB627` | amber, 10.46:1 on bg, 8.60:1 on bg-2 |
| `--la-accent-2-on` | `#04171C` | text on amber, 10.46:1 |
| `--la-accent-2-txt-inv` | `#916308` | amber as text on bone, 4.58:1 |

Aqua is the heritage teal pushed up-chroma, so it is an evolution of the mark rather than a replacement, and amber is the heritage gold at full saturation. Both anchors survive.

**Cost:** the logo files have to be regenerated. The current dark variants sit on `#08343E`, not `#04171C`, and the gold in them is `#E8A33D`, not `#FFB627`.

## B. Ember

Light-first, warm, human. Keeps cream as the primary surface so existing print and slide work needs less rework, and buys pop from hue tension instead of value.

| Token | Hex | Role |
|---|---|---|
| `--la-bg` | `#FBF7F0` | paper |
| `--la-bg-2` | `#F1EDE7` | sunken fill, table rows, inset panels |
| `--la-bg-inv` | `#0A2028` | near-black teal |
| `--la-line` | `#E6E1D8` | hairline, non-text |
| `--la-structure` | `#0B3D4A` | heritage teal, headings and chart bars, 11.04:1 |
| `--la-ink` | `#0A2028` | primary text, 15.73:1 |
| `--la-ink-2` | `#3B6472` | secondary text, 6.05:1 on bg, 5.54:1 on bg-2 |
| `--la-ink-inv` | `#FBF7F0` | text on the dark surface, 15.73:1 |
| `--la-accent` | `#FF5F2E` | ember. **Fills and buttons only**, 2.84:1 on paper |
| `--la-accent-on` | `#0A2028` | text on ember, 5.54:1 |
| `--la-accent-txt` | `#C43708` | ember as text, 5.05:1 on bg, 4.62:1 on bg-2 |
| `--la-accent-2` | `#F0A500` | amber, for numerals on the dark surface, 8.07:1 |
| `--la-accent-2-on` | `#0A2028` | text on amber, 8.07:1 |
| `--la-accent-2-txt` | `#8F6103` | amber as text on paper, 5.07:1 on bg, 4.64:1 on bg-2 |

**The one rule that will bite you:** buttons filled with `#FF5F2E` take **dark** label text, not white. White on ember is 3.03:1 and fails. This is counterintuitive and it is the single most likely mistake in this palette.

**Cost:** the logo files have to be regenerated. Ember replaces gold entirely.

## How these were derived

Every value was computed, not eyeballed. Anchors (`#2DE2C5`, `#FFB627`, `#FF5F2E`) were chosen for hue and chroma, then each companion token was solved by holding the anchor's hue and saturation and sweeping HSL lightness until it hit the WCAG 2.1 target against its declared surface. Twelve pairings per palette were then asserted at AA, and both pass with zero failures. The contrast numbers in the tables and in the `.json` files are outputs of that check.

Type is unchanged from v1: Poppins for headings, Inter for body. Heading tracking tightens from `-0.02em` to `-0.03em` and body line-height opens from `1.5` to `1.55`, both because the higher-contrast surfaces need slightly more air.

## Files

| File | What it is |
|---|---|
| `tokens-v2-voltage.css` / `.json` | Voltage alone, `:root` scoped |
| `tokens-v2-ember.css` / `.json` | Ember alone, `:root` scoped |
| `tokens-v2.css` | both, scoped to `[data-la-palette="voltage"|"ember"]` for A/B on one page |
| `v2-preview.html` | full component preview of both, uses `tokens-v2.css` |
| `palette-options.html` | the earlier three-way teaser board, including option C |

## Still open

- Neither palette has logo files. Adopting either means re-running `darkify.mjs` with new anchors and, for Ember, rebuilding the mark's gold entirely.
- Option C from `palette-options.html`, keeping cream and teal and only pushing gold to `#FFAE0F` plus a `#00C2A8` second accent, was not built as tokens. It is the cheap path if regenerating logos is off the table.
- No decision on which, if either, ships. v1 stays canonical until Ryan says otherwise.
