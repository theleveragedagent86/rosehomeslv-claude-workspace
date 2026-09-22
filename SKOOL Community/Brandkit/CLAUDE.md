# CLAUDE.md — The Leveraged Agent / Brandkit

**Canonical brand assets for "The Leveraged Agent"** (the Skool community brand). This is the single source of truth — copy FROM here into new projects. This is the Leveraged Agent counterpart to `hyperframes-student-kit/Rose Homes Brandkit/` (which is the *realtor* brand, a different business — do not mix them).

## The assets

| File | Size | What it actually is |
|---|---|---|
| `leveraged-agent-logo.png` | 1424 × 752 | **Horizontal lockup on white.** "LA" monogram + stacked "Leveraged / Agent" in Barlow 800, navy `#050E3D` on white with the `#1768E5` rule under the monogram. No tagline. Use for headers, outros, wide lockups. |
| `leveraged-agent-logo-small.png` | 1024 × 1024 | **Square "LA" monogram/icon** on white. Use for avatars, profile pics, favicons, badges. |
| `leveraged-agent-logo-dark.png` | 1424 × 752 | **The same lockup on true black.** White type, same blue rule. Use on any dark background. |
| `leveraged-agent-logo-small-dark.png` | 1024 × 1024 | **Square monogram on true black.** |
| `leveraged-agent-youtube-banner.png` | 2560 × 1440 | YouTube channel banner. Black field, deep-blue slab bled off the left edge, everything readable inside the centred 1546 × 423 TV-safe box. |

**All five were regenerated on 2026-09-01** from the v2.0 "Vector" design system, replacing the v1 cream / teal / gold artwork in place. They are rendered, not drawn: change `Design-System/logo.js` or `Logos/logos.html` and rerun the build, never retouch a PNG.

### Naming warning (read this)

`leveraged-agent-logo-small.png` is **not a small version of the logo** — it is the *square monogram*, at full 1024×1024. The name is misleading but is kept **on purpose**: ~29 copies of these two files are already bundled in `hyperframes-student-kit/video-projects/*/assets/`, and composition HTML references them by these exact filenames. Renaming here would break drop-in compatibility. Rename only if you also update every project that references them.

## Palette, canonical, v2.0 "Vector"

**ADOPTED 2026-08-19.** Ryan said "lets go vector". `Vector` is the shipping brand. It lives in `Brand-Guide/tokens.css` and `Brand-Guide/tokens.json`, and the written spec is [Brand-Guide/BRAND-GUIDE.md](Brand-Guide/BRAND-GUIDE.md). **The v1.0 cream / teal / gold system is retired**, archived unchanged as `Brand-Guide/tokens-v1.css` and `tokens-v1.json`. Do not use v1 colors, or the v2 / v3 / other v4 candidates, in new work.

**White base, true-black dark surface, one blue accent, thirteen tokens.**

| Token | Hex | Role |
|---|---|---|
| `bg` | `#FFFFFF` | Primary surface |
| `bg-2` | `#F7F8FA` | Sunken fills, cards on white |
| `bg-inv` | `#000000` | Dark surface, full-bleed bands |
| `line` | `#E4E7EF` | Hairlines and dividers. **Not a text color** |
| `structure` | `#0B3FA8` | Deep blue for rules, bars, structural fills. **Not a text color** |
| `ink` | `#050E3D` | **Primary ink** on light. 18.48:1 |
| `ink-2` | `#55627F` | Secondary text on light. 6.11:1 |
| `ink-inv` | `#FFFFFF` | Primary ink on black. 21:1 |
| `ink-2-inv` | `#9AA3BC` | Secondary text on black. 8.34:1 |
| `accent` | `#1768E5` | **Accent fill.** Buttons, badges |
| `accent-on` | `#FFFFFF` | Text on `accent`. 5.06:1 |
| `accent-txt` | `#1768E5` | The same blue as text on white. 5.06:1 |
| `accent-inv` | `#5B9BFF` | Accent on black. 7.58:1 |

**The one color rule:** one accent, one value. `#1768E5` works as a fill and as text on white without a second darker variant, which is exactly what the v1 gold could not do and what killed Rosewood and every orange candidate. Never introduce a second accent value. Black is a surface, never a text color. Most of the visual pop is **structural**, a full-bleed black band butted against white, not chromatic.

**No warm colors anywhere.** No cream, no gold, no sage, no orange.

**Typefaces, settled 2026-08-19:** **Barlow 800** headlines at `-0.028em`, including inside thumbnails. **Raleway 600** subtext only, meaning eyebrow, subhead and small label, never a running paragraph. **Inter 400/500** body at line-height 1.6. Micro-labels are Raleway 600 uppercase at `0.15em`. The 800-to-400 gap between headline and body carries the entire hierarchy, because there is no serif in the system. Barlow and Raleway are **not installed on this Mac**. As of 2026-09-01 that no longer matters for anything in this folder: the woff2 files are self-hosted in [Design-System/fonts/](Design-System/fonts/) and `Design-System/tokens.css` imports them, so a headless render over `file://` gets the real faces with no network. Poppins is retired. Pages outside this folder that still want the CDN:

```
https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&family=Raleway:wght@400;500;600;700&display=swap
```

**The logo regeneration happened on 2026-09-01.** Ryan imported a Claude Design project ("Leveraged Agent, classroom tiles") that carries the whole v2.0 system as running code: tokens, a component library, an `<la-logo>` web component, and the type-only classroom cover. It was extracted into [Design-System/](Design-System/) and every brand image was rebuilt from it. **Still off-palette and NOT yet refreshed:** the ~29 bundled logo copies under `hyperframes-student-kit/video-projects/*/assets/` (deliberately left alone, see below) and the Instagram carousel system. `Brand-Guide/brand-guide.html` is still stale: it links `tokens.css` so it picks up the new variables, but it hardcodes v1 hexes throughout and describes eight tokens that no longer exist. `YouTube-Thumbnails/template.html` is untouched, it was already white plus near-black, and Ryan locked it for CTR on 2026-07-16 — note it therefore still uses system-font 900, not Barlow 800.

**Why the bundled per-project copies were left on v1:** those compositions are themselves still v1, their outros sit on `rgba(15,76,92)` teal gradients. Dropping a Vector lockup into a teal gradient clashes harder than leaving the matching v1 art in place, and the videos they belong to are already rendered. Refresh them when a composition is migrated, not before.

**Clear space and min size, carried forward from v1.0 unchanged:** clear space = 8% of the placed logo height on all four sides. Wordmark minimum 240px wide on screen (1.25in / 32mm print). Below that, use the square monogram, minimum 48px. These rules apply to whatever replaces the current artwork.

The v1 sparkle artifact in the old monogram's bottom-right corner is gone; the mark is drawn type now, not a generated image.

### How the decision was reached

The full record is in [Brand-Guide/V4-PALETTES.md](Brand-Guide/V4-PALETTES.md), and the research it was built on is [Brand-Guide/PEDIGREE-BRAND-RESEARCH.md](Brand-Guide/PEDIGREE-BRAND-RESEARCH.md), which measures what 10 top US brokerages actually do off their live sites: achromatic base, exactly one accent, tinted near-black ink.

On 2026-08-19 Ryan rejected both v1 brand colors outright, the teal and the gold, and asked for a white or light base with an accent that actually pops. That produced the v4 set. **Rejected and gone, do not re-propose:** `Rosewood` (Real Broker pink `#F96B88`, failed at 2.81:1 and needed two accent values), `Crimson` (The Agency red `#DE0F16`, "shouts more"), `Sovereign` (violet `#834CE2`, rejected on **differentiation**, Mike Sherrard already owns purple in this niche), plus the earlier `Signal` (burnt orange) and `Ivory` (warm paper) also-rans, and the losing finalists `Ultramarine` (same blue but navy dark surface) and `Meridian` (Serhant's system, navy accent at 15.10:1 that barely reads as a color). **Orange cannot win here and the reason is mechanical:** dark enough to carry white text means it reads brown, bright enough to be loud means it needs a second value. Superseded palette proposals `V2-PALETTES.md` (Voltage, Ember) and `V3-BROKER.md` also remain as files and are dead.

Type was decided separately. **Ryan rejected Space Grotesk, Fraunces and Bodoni Moda on 2026-08-19, do not re-propose them.** That removed every serif. From the six surviving grotesks he picked **P08** off [Brand-Guide/v4-fonts.html](Brand-Guide/v4-fonts.html) ("p08 seems to be best"), then confirmed **800** off the 600/700/800/900 ladder in [Brand-Guide/v4-weights.html](Brand-Guide/v4-weights.html) ("the original recommended one is fine"). The page/thumbnail weight split, 800 on page and 900 in thumbnails, was offered and declined. Do not re-propose it. Tracking varies per weight on those pages on purpose (600 `-0.020em` through 900 `-0.032em`), since a locked value would make 900 look loose and 600 look cramped. Four pairings are ruled out on the record in `V4-PALETTES.md`: Raleway as running body, Raleway head + Raleway subtext, Poppins body, and Inter Tight + Inter at similar sizes. `v4-type.html` and `v4-preview.html` are superseded and stale.

## Using these

- **New HyperFrames video project:** copy into the project's own `assets/` — projects bundle assets and reference them relatively, so they must be local:
  ```bash
  cp "/Users/ryanrose/Downloads/Claude/SKOOL Community/Brandkit/leveraged-agent-logo.png" assets/
  ```
  Do **not** symlink or reference this folder from a composition; it breaks portable renders.
- **Never** put Rose Homes LV realtor branding on Leveraged Agent material, or vice versa. Different businesses.

## Design-System/ — the v2.0 system as running code

Extracted 2026-09-01 from Ryan's Claude Design project *"Leveraged Agent, classroom tiles"*. **This is the build source for every brand image in this folder.** Nothing here is decorative documentation; the renders come out of it.

| File | What it is |
|---|---|
| `tokens.css` | The 13-token Vector palette plus the type, spacing, shape and motion scales, as `--la-*` custom properties. Imports `fonts/fonts.css`. Same values as `Brand-Guide/tokens.css`, in the shape the components consume. |
| `la-components.css` | The component primitives: `.la-btn`, `.la-card`, `.la-badge`, `.la-band-section`, `.la-stat`, fields, tabs, dialog, toast, tooltip. Class-based, no build step. |
| `logo.js` | The `<la-logo>` custom element. `variant="lockup|wordmark|monogram|accent|favicon"`, plus `inverse` and `no-tagline`. It renders **inline SVG into a shadow root on purpose**: an `<img src="logo.svg">` is an isolated document that cannot reach the page's webfonts and silently falls back to Arial. It also re-measures after the fonts land and tightens the viewBox to the real ink, so a placement only ever sets a width. |
| `fonts/` | Self-hosted Barlow 400-900, Raleway and Inter woff2 + `fonts.css`. This is why headless renders work over `file://` with no network. |
| `classroom-cover.css` | The 1600 × 847 type-only cover: `.cov`, `.cov__meta`, `.cov__title` (+`--md`/`--sm` steps), `.cov__rule`, `.cov__sub`, `.cov__mark`. |
| `build-assets.mjs` | **The one build command.** Renders logos, the banner, the covers and the SVG masters. |

```bash
cd "/Users/ryanrose/Downloads/Claude/SKOOL Community/Brandkit"
node Design-System/build-assets.mjs                 # everything
node Design-System/build-assets.mjs covers          # one group: logos | banner | covers | svg
```

It imports Playwright by absolute path from `hyperframes-student-kit/node_modules`, so it runs from anywhere and does not need a server. Two things it does deliberately, do not "simplify" them away: it pins each frame to whole pixels before shooting, because `la-logo` sizes itself from an aspect ratio and a fractional box makes the screenshot clip round up (that is where stray 1025px-tall "1024px" exports come from); and the SVG masters get the woff2 embedded as a data URI, because an `<img src="logo.svg">` cannot otherwise load Barlow.

## Logos/ — the v2.0 logo set

`logos.html` is the source sheet, every export is one `[data-export]` frame in it. Edit that file, rerun `build-assets.mjs logos svg`.

- **PNG, transparent:** `logo-lockup`, `logo-wordmark`, each also `-inverse` (for black grounds) and `-tagline` / `-tagline-inverse`.
- **PNG, own field:** `logo-monogram` (white), `-inverse` (black), `-accent` (`#1768E5`), `favicon-512`, `favicon-32`.
- **SVG masters:** the same set, each with Barlow 800 and Raleway 600 embedded as a base64 data URI so they render correctly as a bare `<img>` or handed to anyone.

**The tagline is `"Automating 80% of the job that sucks"`**, which came with the design project and **replaces v1's "AI workflows for working agents"**. It lives as a constant in `logo.js` (and `TAGLINE` in `build-assets.mjs` for the banner). It ships only on the `-tagline` variants and the YouTube banner; the four canonical root files carry no tagline. The old tagline still appears in `Open-House-Reconnection-Prompt/` and in `Brand-Guide/`, which have not been updated.

## YouTube-Banner/ — channel banner source

`banner.html` renders `../leveraged-agent-youtube-banner.png` at 2560 × 1440. YouTube crops hard, so **only the centred 1546 × 423 box is guaranteed to survive**; the deep-blue slab off the left edge is decoration that is meant to be cropped away on phones. `TAGLINE_GOES_HERE` is substituted at build time.

## YouTube-Thumbnails/ — the canonical thumbnail template

**This is the standing template for every Leveraged Agent YouTube thumbnail. Ryan approved this exact layout on 2026-07-16 — reuse it as-is; the only thing that should change between thumbnails is the headline text.**

| File | What it is |
|---|---|
| `example.png` | Ryan's approved reference render ("your leads are ghosting you"). Visual ground truth — if a new render doesn't look like this, something's wrong. |
| `template.html` | The reusable layout. One placeholder: the literal string `TEXT_GOES_HERE` inside `<div class="text">`. Everything else (fonts, sizes, photo crop) is locked in. |
| `headshot.png` | Ryan's headshot, background already flattened to white (source: `main headshot.white bg.png`). This is the subject photo the template composites in — do not swap for the older gray-textured-background or transparent-cutout headshots used in earlier iterations of this workspace; this white-bg version is what's calibrated against `example.png`. |

### Recipe (design spec, in case the template needs to be rebuilt)

- Canvas: 1280×720 (standard YouTube thumbnail).
- Background: solid `#ffffff`.
- Headline: `-apple-system, "Helvetica Neue", Arial, sans-serif`, weight **900**, `font-size:94px`, `line-height:1.15`, `letter-spacing:-0.02em`, lowercase, color `#0a0a0a`. Positioned `left:44px; top:190px; width:630px` (let it wrap naturally — do not manually break lines).
- Photo: right-aligned frame `580px × 720px` (`top:0; right:0`), `overflow:hidden`. Inside it, `headshot.png` sized `height:1168px; width:auto`, positioned `top:-13px; left:50%; transform:translateX(-50%)`. This crop gives ~110px of headroom above the hair and lets the shoulders fill the full 580px frame width by the bottom edge — tight enough to be "mainly the head," wide enough that the shoulders don't get clipped mid-curve.

### How to render a new thumbnail

Requires the local preview server running from the workspace root (`ruby serve.rb` from `/Users/ryanrose/Downloads/Claude`, serves port 8091) and Playwright, which is installed under `hyperframes-student-kit/node_modules`. A reusable render script already lives there:

```bash
cd "/Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit"
node render-thumbnail.mjs "your headline text here" output-file-name
# → saves to Brandkit/YouTube-Thumbnails/output-file-name.png
```

The script swaps `TEXT_GOES_HERE` in `template.html`, renders at true 1280×720, and cleans up its temp file. No manual HTML editing needed for a routine new thumbnail — just the headline text.

### Style rules for headline text

Match Ryan's approved examples (`example.png` and the "still not followed up." / "ai does this for you." / "photos become leads." set): short, punchy, all-lowercase, 3-6 words, states a specific claim or hook grounded in the actual video content, ends without a question mark unless it reads better with one. Two lines is typical at this font size; if a phrase wraps to 3+ lines, shorten it rather than shrinking the font.

## Classroom-Covers/ — Skool module cover graphics

**Rebuilt 2026-09-01 on v2.0 Vector: type only, no icon, no gradient.** Canvas is 1600 × 847 (~1.89:1, the card image crop ratio). A full-bleed black field, a `#5B9BFF` meta label, an uppercase Barlow 800 title, a `#1768E5` rule, a Raleway 600 subtitle, and the wordmark bottom-right. Only the top banner is generated here; the white title/description/progress-bar strip below it is auto-populated by Skool from the module's own fields.

The v1 look (dark-teal radial gradient, gold underline, gold/navy/cream isometric icon) is **dead**, along with the whole `icons/` system, because Vector forbids warm colors. The one rendered v1 cover and its icon are in [v1-archive/](v1-archive/).

| File | What it is |
|---|---|
| `template.html` | The single-cover layout. Tokens: `META_GOES_HERE`, `TITLE_GOES_HERE`, `SUBTITLE_GOES_HERE`. |
| `tiles.html` | All seven covers on one contact sheet, scaled to fit. Serve or open it to review the set at once. |
| `fit-title.js` | Steps the title size down by character count (>17 chars → `--md`, >34 → `--sm`) so a title never reaches a third line, then re-runs after the fonts land because the first pass measures Arial. |
| `configs/` | One `<NN>-<slug>.json` per module: `{ "meta", "title", "subtitle" }`. The build only picks up files matching `NN-*.json`. |
| `01-start-here.png` … `09-resources.png` | The rendered covers. `08-sellers` added 2026-09-17 (seller-side workflows, starting with the weekly seller update). `09-resources` added 2026-09-17, blank meta (no module number), same as `08-sellers`. |

The meta label carries the module number and **no runtime**, because a module holds several videos.

### How to render

```bash
cd "/Users/ryanrose/Downloads/Claude/SKOOL Community/Brandkit"
node Design-System/build-assets.mjs covers
```

To add a module, drop a new `<NN>-<slug>.json` into `configs/` and rerun. `hyperframes-student-kit/render-classroom-cover.mjs` is **retired** and is now a stub that points here.

### Known gotcha (already handled, don't reintroduce)

`TITLE_GOES_HERE` is a literal substring of `SUBTITLE_GOES_HERE`. A token-replace that does the title first partially matches and corrupts the subtitle (it once produced "SUBOPEN HOUSES"). `build-assets.mjs` replaces `SUBTITLE_GOES_HERE` first. Keep that order.

### Heads-up: these seven do not match the live classroom

The design ships Modules 01-07 (Start here / Follow-up / Listing launch package / Open houses / Sphere / Photos become leads / Offer packet). The Skool classroom today has Module 0, 1, 2 and Open Houses, and the [Claude Code Course for Realtors](../Claude%20Code%20Course%20for%20Realtors/) decision from 2026-08-24 is **one tile, Level 0-10**, not a module ladder. Nothing has been uploaded to Skool. Reconcile the naming before these go live.

---

## Folder Map — keep this current

```
Brandkit/
├── CLAUDE.md                            this file
├── leveraged-agent-logo.png             1424x752 lockup on white. v2.0 Vector, rebuilt 2026-09-01
├── leveraged-agent-logo-dark.png        1424x752 lockup on true black. v2.0 Vector
├── leveraged-agent-logo-small.png       1024x1024 square "LA" monogram (NOT a small logo). v2.0
├── leveraged-agent-logo-small-dark.png  1024x1024 monogram on true black. v2.0
├── leveraged-agent-youtube-banner.png   2560x1440 channel banner. v2.0, TV-safe box respected
├── Design-System/                       THE BUILD SOURCE, extracted 2026-09-01 from Ryan's Claude
│   │                                    Design project. Every brand image here is rendered from it
│   ├── build-assets.mjs                 the one build command: logos | banner | covers | svg
│   ├── tokens.css                       v2.0 Vector tokens in --la-* form, imports fonts/fonts.css
│   ├── la-components.css                .la-btn/.la-card/.la-badge/.la-band-section/fields/tabs/overlays
│   ├── classroom-cover.css              the 1600x847 type-only cover
│   ├── logo.js                          <la-logo> custom element, inline SVG in a shadow root
│   └── fonts/                           self-hosted Barlow/Raleway/Inter woff2 + fonts.css
├── Logos/                               v2.0 logo set, PNG + SVG masters (fonts embedded)
│   ├── logos.html                       THE SOURCE SHEET, one [data-export] frame per export
│   ├── logo-lockup[-inverse|-tagline|-tagline-inverse].png/.svg
│   ├── logo-wordmark[-inverse|-tagline|-tagline-inverse].png/.svg
│   ├── logo-monogram[-inverse|-accent].png/.svg
│   └── favicon-512.png · favicon-32.png · favicon.svg
├── YouTube-Banner/
│   └── banner.html                      source for leveraged-agent-youtube-banner.png
├── v1-archive/                          RETIRED v1 cream/teal/gold artwork, reference only
│   ├── README.md                        what is in here and why nothing should be pulled from it
│   ├── classroom-cover-open-houses.png/.json   the one rendered v1 cover + its config
│   └── icon-open-houses-house.svg       the v1 isometric icon system, dead under v2.0
├── Brand-Guide/                         canonical palette, contrast matrix, logo rules, v2.0 2026-08-19
│   ├── BRAND-GUIDE.md                   the written spec (source of truth), v2.0 "Vector"
│   ├── brand-guide.html                 visual guide (serve it, do not open as file://). STALE: hardcodes
│   │                                    v1 hexes and describes 8 tokens that no longer exist
│   ├── tokens.css                       CANONICAL v2.0 "Vector". --la-* CSS custom properties
│   ├── tokens.json                      CANONICAL v2.0 "Vector", machine-readable, with contrast table
│   ├── tokens-v1.css                    ARCHIVE: the retired v1.0 cream / teal / gold, verbatim
│   ├── tokens-v1.json                   ARCHIVE: the retired v1.0, verbatim. Kept for auditability
│   ├── darkify.mjs                      regenerates the two dark logo variants from the light ones
│   ├── palette-options.html             PROPOSAL ONLY: 3 higher-chroma "pop" palettes vs current
│   ├── V2-PALETTES.md                   PROPOSAL ONLY: spec for the two v2 candidates + v1 migration table
│   ├── tokens-v2-voltage.css/.json      v2 candidate A "Voltage", dark-first, aqua + amber
│   ├── tokens-v2-ember.css/.json        v2 candidate B "Ember", light-first, orange + teal
│   ├── tokens-v2.css                    both v2 candidates, switch via [data-la-palette="voltage"|"ember"]
│   ├── v2-preview.html                  full component preview of both v2 candidates
│   ├── V3-BROKER.md                     PROPOSAL ONLY: spec for v3 "Broker" + v1 migration table
│   ├── tokens-v3-broker.css/.json       v3 candidate "Broker", white base, deep-teal ink, gold sole accent
│   ├── v3-preview.html                  side-by-side component preview: v1 vs v3 Broker, same markup
│   ├── V4-PALETTES.md                   THE DECISION RECORD: spec for the v4 candidates (no teal,
│   │                                    no gold) + accent-legibility comparison + the rejection record
│   │                                    for Rosewood, Crimson and Sovereign + type table + v1 migration
│   ├── tokens-v4-ultramarine.css/.json  v4 LOST: "Ultramarine", white base, navy ink #050E3D,
│   │                                    electric blue accent #1768E5, deep-navy dark surface
│   ├── tokens-v4-meridian.css/.json     v4 LOST: "Meridian", white + TRUE-black co-equal surfaces,
│   │                                    navy accent #001A72 (Serhant's measured system; #000 is a
│   │                                    surface, never text)
│   ├── tokens-v4-vector.css/.json       ADOPTED 2026-08-19 as v2.0, promoted to tokens.css/.json.
│   │                                    "Vector", built 2026-08-19: Meridian's white + true-black
│   │                                    structure with Ultramarine's #1768E5 accent. Candidate record
│   ├── tokens-v4-signal.css/.json       v4 also-ran: "Signal", warm near-black, burnt-orange #BB4C0A.
│   │                                    Ryan: the orange "just doesn't seem to pop". Kept for the record
│   ├── tokens-v4-ivory.css/.json        v4 also-ran: "Ivory", warm-paper #FDF9F2 base, NO accent hue
│   ├── v4-final.html                    THE DECISION PAGE: Ultramarine vs Meridian vs Vector, each with
│   │                                    a real full-bleed dark band + working-size tests + orange proof
│   ├── v4-preview.html                  older 6-up preview. STALE: still contains the deleted Crimson
│   │                                    and Sovereign classes, and has NO full-bleed dark band
│   ├── v4-fonts.html                    THE TYPE DECISION PAGE: 12 head+body pairings on a FIXED Vector
│   │                                    palette so only type varies + 4 combinations ruled out. Six faces
│   │                                    only: Poppins/Inter/Archivo/Inter Tight/Barlow/Raleway, all
│   │                                    grotesks. Raleway is subtext-only. Tracking varies per face
│   ├── v4-weights.html                  THE HEADLINE WEIGHT PAGE: P08 locked (Raleway 600 subtext, Inter
│   │                                    body, Vector), ONLY Barlow headline weight varies 600/700/800/900.
│   │                                    Stacked headline compare + all 4 side-by-side at thumbnail size +
│   │                                    one full card each. 800 recommended. Tracking varies per weight
│   ├── v4-type.html                     SUPERSEDED and STALE: 3 of its 6 faces (Space Grotesk/Fraunces/
│   │                                    Bodoni Moda) are rejected, and it sits on Ultramarine not Vector
│   ├── PEDIGREE-BRAND-RESEARCH.md       RESEARCH: measured brand conventions of 10 high-pedigree US
│   │                                    brokerages (Serhant, Agency, Compass, Elliman, Eklund Gomes,
│   │                                    Altman, Sotheby's, Corcoran, Real, Tom Ferry) + how v1/v2 score
│   └── pedigree-board.html              visual companion to the research: real swatches + type specimens
├── YouTube-Thumbnails/                  canonical thumbnail template, see section above
│   ├── example.png                      Ryan-approved reference render
│   ├── template.html                    reusable layout (swap TEXT_GOES_HERE only)
│   └── headshot.png                     white-bg source headshot used by the template
├── YouTube-Bumpers/                     3s intro sting + TWO transparent like/subscribe OVERLAYS,
│   │                                    YouTube ONLY. hyperframes project, HTML in / video out,
│   │                                    re-renderable. Vector v2.0 inverted, typographic wordmark
│   │                                    (no logo file, they are all still v1 art). READ README.md
│   │                                    FIRST. Bumper goes at 0:35 AFTER the hook, never at 0:00.
│   │                                    Overlays are ProRes 4444 with REAL alpha and composite over
│   │                                    recorded footage, they are not cards you cut to; render
│   │                                    with --format mov or you get an opaque black frame.
│   │                                    The full-frame end card was DELETED 2026-08-24: the outro
│   │                                    is now an overlay on Ryan's own footage and YouTube's
│   │                                    clickable cards sit on that footage, so he frames himself
│   │                                    in the RIGHT half (the overlay owns the left column).
│   │                                    The ending overlay is the wordmark PANEL top-left plus the
│   │                                    Like + Subscribe chips bottom-left. Ryan APPROVED that
│   │                                    panel by name on 2026-08-24, do not strip it; a radial
│   │                                    scrim and bare keylined type were both tried and rejected.
│   │                                    What he DID reject is motion during the hold, so
│   │                                    everything animates in then holds dead still. A WebM alpha
│   │                                    variant was tried and REJECTED, it decodes back opaque;
│   │                                    verify alpha by decoding pixels, never by ffprobe alone
│   │                                    (command is in README.md)
│   ├── README.md                        placement, alpha verification, Studio setup, why not Skool
│   ├── compositions/bumper.html         3s sting source
│   ├── compositions/like-subscribe.html 6s mid-roll overlay source, chips only, bottom-left
│   ├── compositions/like-subscribe-end.html  20s ending overlay source, adds the wordmark panel
│   │                                    top-left; no exit and no drift, the video cuts on it
│   └── renders/                         bumper.mp4, like-subscribe.mov, like-subscribe-end.mov;
│                                        1920x1080 30fps silent, all git-ignored (*.mp4 and *.mov)
└── Classroom-Covers/                    Skool module covers, v2.0 type-only. See section above
    ├── template.html                    single-cover layout (META/TITLE/SUBTITLE tokens)
    ├── tiles.html                       all 7 on one contact sheet
    ├── fit-title.js                     steps title size by length so nothing hits a 3rd line
    ├── configs/                         one <NN>-<slug>.json per module: meta/title/subtitle
    └── 01-start-here.png … 09-resources.png   the 9 rendered covers, 1600x847 (08 + 09 added 2026-09-17; 08/09 have no module number)
```

**Maintenance rule:** When you add, remove, or replace a brand asset here, update this map AND the parent `SKOOL Community/CLAUDE.md` map in the same change. **Brand images are build outputs, not artwork** — change `Design-System/` or a source HTML and rerun `node Design-System/build-assets.mjs`, never retouch a PNG by hand, or the next build silently reverts you. The ~29 per-project logo copies under `hyperframes-student-kit/video-projects/*/assets/` do NOT auto-update and are deliberately still v1; refresh one only when its composition is migrated. Never leave the map stale. `hyperframes-student-kit/render-thumbnail.mjs` still pairs with `YouTube-Thumbnails/` and has to live where Playwright is installed; `render-classroom-cover.mjs` is retired. `build-assets.mjs` hardcodes the absolute path to `hyperframes-student-kit/node_modules/playwright`, so if this folder or that one moves, fix it there too.
