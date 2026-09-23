# The Leveraged Agent Brand Guide v2.0 "Vector"

**Adopted 2026-08-19.** This replaces v1.0 (cream, teal, gold), which is archived as [tokens-v1.css](tokens-v1.css) and [tokens-v1.json](tokens-v1.json). v1.0 was recovered by pixel-sampling the existing logo artwork; v2.0 is a deliberate rebrand, and the two share nothing but the clear-space and min-size rules.

**Why the change.** Ryan rejected the teal and the gold outright and asked for a white or light base with an accent that actually pops, built from the pedigree brokerages' own measured palettes. The full candidate field, the rejection record with every hex, and the reasoning are in [V4-PALETTES.md](V4-PALETTES.md). Vector won: Serhant's white-plus-true-black surface structure carrying Tom Ferry's electric blue as the single accent.

**What is evidence and what is a decision.** The three anchor hexes are measured from real brokerage brand systems (see [PEDIGREE-BRAND-RESEARCH.md](PEDIGREE-BRAND-RESEARCH.md)). `structure`, `ink-2`, `ink-2-inv` and `accent-inv` are derived, chosen to hit specific WCAG targets. The clear-space and min-size numbers carry over unchanged from v1.0.

**Consequence, stated plainly: every current logo file is now off-palette.** All five are built on the v1.0 teal and gold. They still work as artwork but they no longer match the brand. Regeneration is open work, see section 5.

Machine-readable: [tokens.css](tokens.css), [tokens.json](tokens.json).

---

## 1. Palette

Thirteen tokens. Nothing outside this list is a brand color. Every ratio below is WCAG 2.1 computed, not eyeballed.

### Surfaces

| Token | Hex | Role |
|---|---|---|
| `bg` | `#FFFFFF` | Primary surface. Pure white, not off-white |
| `bg-2` | `#F7F8FA` | Sunken fill, table rows, inset panels. Faint cool cast |
| `bg-inv` | `#000000` | Inverted surface. **True black, and it is a surface, never text** |
| `line` | `#E4E7EF` | Hairline and divider on `bg`. Non-text, 1.24 |
| `structure` | `#0B3FA8` | Deep blue for chart bars, structural fills, very large headings. 9.17 on `bg` |

### Ink

| Token | Hex | On | Ratio | Verdict |
|---|---|---|---|---|
| `ink` | `#050E3D` | `bg` | **18.48** | AAA. The default text color |
| `ink` | `#050E3D` | `bg-2` | 17.35 | AAA |
| `ink-2` | `#55627F` | `bg` | 6.11 | AA. Captions and secondary copy |
| `ink-2` | `#55627F` | `bg-2` | 5.75 | AA |
| `ink-inv` | `#FFFFFF` | `bg-inv` | **21.00** | AAA. The default text color on black |
| `ink-2-inv` | `#9AA3BC` | `bg-inv` | 8.34 | AAA |

### Accent, and there is only one

| Token | Hex | On | Ratio | Verdict |
|---|---|---|---|---|
| `accent` | `#1768E5` | fills, buttons | | The accent |
| `accent-on` | `#FFFFFF` | `accent` | 5.06 | AA. White is the only text that goes on the blue |
| `accent-txt` | `#1768E5` | `bg` | 5.06 | AA. **The accent is a legal text color on white**, unlike v1's gold |
| `accent-txt` | `#1768E5` | `bg-2` | 4.76 | AA, and this is the palette's tightest pair |
| `accent-inv` | `#5B9BFF` | `bg-inv` | 7.58 | AAA. The blue lightens on black so it stays readable |

### Color rules

1. **One accent, one value on light.** `#1768E5` works as a fill and as text on white. That single fact is why Vector exists: v1's gold needed a second darker value (`gold-ink`) the moment it had to be readable, and so did every rejected candidate. Do not introduce a second accent.
2. **Black is a surface, never text.** Text on white is `ink` `#050E3D`, not black. True black is reserved for full-bleed inverted bands.
3. **The pop is structural first, chromatic second.** Most of the impact comes from a full-bleed black band butted against white, not from the blue. If a layout feels flat, add the band before you add more blue.
4. **`line` and `structure` are not text colors.** `line` fails everything at 1.24. `structure` passes at 9.17 but is reserved for fills and display-size headings so it does not compete with `ink`.
5. **No warm colors anywhere.** No cream, no gold, no teal. Those are v1.0 and they are retired.

---

## 2. Logos

> **All five are v1.0 artwork and are now off-palette.** They are built on the retired teal `#0F4C5C`, gold `#E8A33D`, cream `#F5F2EB` and sage `#B5CAC4`. Nothing here has been regenerated for Vector yet. The file inventory, naming warning, clear-space and min-size rules below all still apply and carry forward to the replacements. The color descriptions do not.

Five files. All live at `Brandkit/` root.

| File | Size | Use it for |
|---|---|---|
| `leveraged-agent-logo.png` | 1424 × 752 | Horizontal wordmark on cream. Headers, outros, wide lockups |
| `leveraged-agent-logo-dark.png` | 1424 × 752 | **New.** Same wordmark on `deep`. Use on any dark surface |
| `leveraged-agent-logo-small.png` | 1024 × 1024 | Square "LA" monogram on cream. Avatars, profile pics, favicons, badges |
| `leveraged-agent-logo-small-dark.png` | 1024 × 1024 | **New.** Same monogram on `deep` |
| `leveraged-agent-youtube-banner.png` | 2560 × 1440 | YouTube channel banner |

The naming warning still stands: **`leveraged-agent-logo-small.png` is not a small logo.** It is the square monogram at full 1024 × 1024. The name is kept on purpose because roughly 44 copies are bundled under `hyperframes-student-kit/video-projects/*/assets/` and composition HTML calls them by these exact filenames. The two new dark files follow the same naming so they drop in the same way.

### How the dark variants were made

Generated on 2026-08-19 from the originals by remapping every pixel: the cream-to-teal luminance axis was inverted onto `cream` over `deep` using a smoothstep so antialiasing survives, and gold pixels were held at their own hue and blended 72% toward canonical `#E8A33D`. Result: the dark variants are color-corrected to the canonical palette, which the light originals still are not. Script is at `Brand-Guide/darkify.mjs` if they ever need regenerating.

Side effect worth knowing: the remap also cleaned up the AI-generation sparkle artifact that sits in the light monogram's bottom-right corner. The dark monogram does not have it.

### Clear space

**Minimum clear space = 8% of the placed logo height, on all four sides.** Nothing else may enter that band, including page edges.

Grounded in the artwork: the wordmark's cap height measures 97px at native 1424 × 752, and the file already carries about one cap height of internal padding at its top and left. The 8% rule is additional space beyond the file's own edges, which puts total breathing room at roughly 1.5 cap heights.

At a 400px placement (400 × 211), that is 17px on every side.

### Minimum size

| Mark | Screen | Print |
|---|---|---|
| Wordmark | **240px wide** | 1.25in / 32mm wide |
| Monogram | **32px** | 0.35in / 9mm |

The wordmark floor is set by its tagline, not its name. "AI workflows for working agents" has a 53px cap height at native size, which is 3.7% of the file width, so it drops below a 9px legibility floor under 240px wide. Below 240px, **use the monogram instead**.

The monogram floor is set by the "LA" itself, which occupies 35% of the canvas. At 32px placed, the letters land near 11px. A 16px favicon is the one allowed exception, because at favicon size the mark is recognized as a shape rather than read as letters.

### Do not

- Do not recolor either mark. Use the light file on light, the dark file on dark.
- Do not place the light (cream-background) file on a dark surface. That is what the dark variants are for.
- Do not stretch, rotate, add a drop shadow, or add an outline.
- Do not put the wordmark on a photo. Put it on a flat `cream` or `deep` field.
- Do not use the monogram where the wordmark fits. The monogram is for square and small slots only.
- **Never put Rose Homes LV realtor branding on Leveraged Agent material, or the reverse.** Different businesses.

---

## 3. Typography

**Settled 2026-08-19.** Chosen as pairing P08 in [v4-fonts.html](v4-fonts.html), which tested 12 head / subtext / body pairings with color held constant so only type varied. The headline weight was then confirmed separately against the 600 to 900 ladder in [v4-weights.html](v4-weights.html). Poppins is retired along with the v1.0 palette.

Three faces, three roles, no overlap.

| Role | Face | Weight | Tracking | Where |
|---|---|---|---|---|
| **Display** | Barlow | **800** ExtraBold | `-0.028em` | Headlines and thumbnail titles |
| **Subtext** | Raleway | **600** SemiBold | `0.01em` | Eyebrow, subhead, small label |
| **Body** | Inter | 400 / 500 | `0` | All running text, captions, buttons |
| **Micro-label** | Raleway | 600 | `0.15em` | Uppercase labels, e.g. `MODULE 03 · 14 MIN` |

```
https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700&family=Raleway:wght@400;500;600;700&display=swap
```

### The rules that make this work

1. **Raleway is subtext only.** Eyebrow, subhead, small label, 15px and up, one short line. **Never a paragraph.** Its low x-height and tight apertures read as refined on a single short line and go mushy across a 13px running paragraph, which is exactly what a Skool post is. This is a hard rule, not a preference.
2. **Barlow 800 in thumbnails too.** The page/thumbnail weight split, 800 on page and 900 in thumbnails, was considered and declined. One weight, both places.
3. **The 800 to 400 gap is the whole hierarchy.** There is no serif in this system, so the separation between a headline and body copy is bought entirely with weight, size and width. A headline that drops to 700 is only three weight steps clear of body and the hierarchy visibly softens.
4. **Tracking is per weight, not global.** If you ever use another Barlow weight: 600 `-0.020em`, 700 `-0.024em`, 800 `-0.028em`, 900 `-0.032em`. Heavier weights widen, so a single locked value makes heavy look loose and light look cramped.
5. **Do not pair Barlow with Archivo, Inter Tight, or a second Barlow as the display face.** With no serif left in the system, two grotesks at similar sizes read as one slightly inconsistent font rather than as two levels.

**Exception:** this does **not** apply to the YouTube thumbnail template in `Brandkit/YouTube-Thumbnails/`, which Ryan approved on 2026-07-16 locked to its own stack (`-apple-system, "Helvetica Neue", Arial`, weight 900). Leave that template alone.

---

## 4. What the rebrand invalidates

v1.0 was a palette recovered from existing artwork, so everything already matched it. v2.0 is a deliberate break, so a lot of shipped material is now off-brand. Nothing below is broken, and nothing has been changed. This is the visible drift list.

| Thing | Uses | Status under v2.0 |
|---|---|---|
| All 5 logo files at `Brandkit/` root | teal, gold, cream, sage | **Off-palette.** Regeneration required, see section 5 |
| ~44 bundled logo copies under `hyperframes-student-kit/video-projects/*/assets/` | same files | **Off-palette, and they do not auto-update.** Replacing the root logos does not touch these. Refresh deliberately |
| `Classroom-Covers/icons/` | gold `#D9A441`, navy `#0B2E33`, cream `#F5F2EA` | **Off-palette.** The earlier plan to nudge these toward v1's gold and navy is now moot, they need rebuilding on Vector |
| `Classroom-Covers/open-houses.png` | v1 palette | **Off-palette.** Re-render when the icons are rebuilt |
| Instagram carousel system | cream `#F5F2EB` + Poppins | **Off-palette and off-type.** Both the surface and the display face changed |
| `YouTube-Thumbnails/template.html` | white `#ffffff`, near-black `#0a0a0a` | **Unaffected, and closer to Vector than it was to v1.** Ryan locked this for CTR on 2026-07-16. Still leave it alone |
| `brand-guide.html` | hardcodes v1 hexes throughout | **Stale.** It links `tokens.css` but its content still describes the cream, teal and gold system. Needs a rebuild |
| `v4-fonts.html`, `v4-weights.html`, `v4-final.html` | Vector | **Current.** These are already on the adopted palette |

**Order of operations if you rebuild.** Logos first, because everything else places them. Then the ~44 bundled copies. Then classroom covers and the carousel system, which are the highest-volume output.

---

## 5. Still open

- **Logo regeneration is the blocking item.** Every current logo is v1.0 teal and gold. Until they are rebuilt on Vector, any layout that uses the real palette and the real logo together will clash. The clear-space and min-size rules in section 2 carry forward unchanged, so the replacements have a spec to hit.
- **No tagline-free wordmark lockup exists.** The standard asset for placements under 240px wide, where the monogram is too abstract. Worth generating as part of the regeneration rather than as a separate job.
- **No vector source.** Every asset is a raster PNG, so none of it scales cleanly past its native size or prints crisply at large format. If the logos are being remade anyway, this is the moment to fix it.
- **`brand-guide.html` needs rebuilding** on the Vector palette and the Barlow / Raleway / Inter stack. It currently hardcodes v1 hexes.
- **Barlow and Raleway are not installed locally.** Anything rendered on this Mac through a headless browser will fall back unless the Google Fonts link is present in the page. Inter is installed.

```bash
brew install --cask font-barlow font-raleway
```
