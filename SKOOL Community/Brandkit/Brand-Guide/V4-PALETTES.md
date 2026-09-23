# v4 Palettes, DECIDED

**Status: `Vector` was adopted on 2026-08-19 as brand v2.0.** It is now the shipping palette in `tokens.css` and `tokens.json`. The v1.0 cream, teal and gold system is retired and archived as `tokens-v1.css` / `tokens-v1.json`. The written spec is [BRAND-GUIDE.md](BRAND-GUIDE.md).

Everything below is the **decision record**, kept so the reasoning and the rejections stay auditable. The other four v4 candidates are not adopted and are not coming back.

**The adoption forces a logo regeneration.** Every current Leveraged Agent logo file is built on the retired teal and gold and is now off-palette. That work has not started.

Built 2026-08-19 after Ryan rejected both v1 brand colors outright and asked for a white or light base with an accent that actually pops, derived from the pedigree brokerages' own measured palettes in [PEDIGREE-BRAND-RESEARCH.md](PEDIGREE-BRAND-RESEARCH.md).

## Preview pages

| Page | URL | What it is |
|---|---|---|
| **v4-final.html** | `http://localhost:8091/SKOOL%20Community/Brandkit/Brand-Guide/v4-final.html` | **The decision page.** Ultramarine vs Meridian vs Vector, each with a real full-bleed dark band, working-size tests, and the orange proof. |
| v4-preview.html | `http://localhost:8091/SKOOL%20Community/Brandkit/Brand-Guide/v4-preview.html` | Older 6-up. **Stale:** still carries the deleted Crimson and Sovereign classes, and has no full-bleed dark band. |
| v4-type.html | `http://localhost:8091/SKOOL%20Community/Brandkit/Brand-Guide/v4-type.html` | Six display faces on a fixed Ultramarine palette, Inter body held constant. |
| **v4-fonts.html** | `http://localhost:8091/SKOOL%20Community/Brandkit/Brand-Guide/v4-fonts.html` | **The type decision page.** 12 head / subtext / body pairings on a fixed Vector palette, plus 4 combinations ruled out. Six faces only, all grotesks. Supersedes v4-type.html. |
| **v4-weights.html** | `http://localhost:8091/SKOOL%20Community/Brandkit/Brand-Guide/v4-weights.html` | **The headline weight page.** Barlow 600 / 700 / 800 / 900 on the P08 recipe, everything else held constant. Stacked headline comparison, all four side by side at thumbnail size, then one full card per weight. |

Start `serve.rb` from the workspace root if the URLs do not answer. It runs on port 8091.

## Where this landed

Ryan narrowed the field on 2026-08-19. Three candidates are live, two survive as files but are out of contention, and three are deleted.

| Candidate | Status | Base | Accent | Dark surface |
|---|---|---|---|---|
| **Ultramarine** | **SHORTLIST** | White | Electric blue `#1768E5` | Deep navy `#050E3D` |
| **Meridian** | **SHORTLIST** | White | Navy `#001A72` | **True black `#000000`** |
| **Vector** | **SHORTLIST, new 2026-08-19** | White | Electric blue `#1768E5` | **True black `#000000`** |
| Signal | Also-ran | White | Burnt orange `#BB4C0A` | Warm near-black |
| Ivory | Also-ran | Warm paper `#FDF9F2` | None, the ink is the accent | Warm near-black |

## The two things that decide this

### 1. Meridian's pop is structural, not chromatic

Meridian is Serhant's measured system. Its energy comes from a **full-bleed true-black band butting straight into white**, not from its accent. That navy sits at `15.10:1` against white, which is so dark it barely registers as a color at all.

That matters because **the two things are separable.** You can keep the black-against-white structure and swap in an accent that actually reads. That is exactly what `Vector` is.

**Disclosure:** the original `v4-preview.html` had no full-bleed dark section, only a small stat card. Meridian was therefore judged on a page that never showed its main move. `v4-final.html` fixes this and gives all three candidates an identical black band.

### 2. Orange cannot win, and the reason is mechanical

Ryan's read was that Signal's orange "just doesn't seem to pop" but that a brighter orange "would be too loud." The first half is right. The second half is not the real cost.

Every accent in this set is darkened until **white text sits on it at 4.5:1 or better**, so a single accent value can serve as both a fill and as text. Blue and red clear that bar while still vivid. Orange does not.

| Orange | White on it | Near-black on it | Verdict |
|---|---|---|---|
| `#F26F21` (Tom Ferry's actual orange) | **2.97** fails | 6.18 passes | Needs dark text, so two accent values |
| `#FF8A3D` (brighter) | **2.35** fails | 7.82 passes | Worse |
| `#E8621A` | **3.39** fails | 5.41 passes | Still fails |
| `#BB4C0A` (the corrected one in Signal) | 5.06 passes | 3.63 fails | Works, but has gone brown |
| `#1768E5` (blue, for comparison) | 5.06 passes | n/a | Clears the same bar fully saturated |

So brighter orange is not too loud. It forces a **second accent value**, which is the exact failure mode that killed Rosewood at `2.81:1` and the v1 gold at `2.16:1`. That is the disqualifier.

### On the blue bias

It is not a bias worth correcting. Serhant, Sotheby's, Real Broker and Tom Ferry all land on navy or blue, and it is the only hue that reads authoritative without raising its voice. Blue's genuine risk is **looking generic**, and that risk is handled by structure, the true-black surface, not by switching hue. That is the argument for Vector over plain Ultramarine.

## Rejection record

Do not re-propose any of these. Token files are deleted; hexes preserved here only so the reasoning survives.

### Rosewood, rejected 2026-08-19
Real Broker pink `#F96B88`. Failed on mechanics: `2.81:1` with white, so it needed two accent values. Corcoran's rose `#C0535C` is the same family with the same problem.
`bg #FFFFFF` / `bg-2 #FDF6F7` / `bg-inv #2A1116` / `structure #A32741` / `ink #2A1116` / `accent #F96B88`.

### Crimson, rejected 2026-08-19
The Agency red, corrected from their measured `#ED2127` (which misses AA at `4.33`) to `#DE0F16`. Ryan: "the red will probably be bad because it shouts more." Mechanically fine, tonally wrong for a teaching brand.
`bg #FFFFFF` / `bg-2 #F7F6F6` / `bg-inv #131011` / `line #EAE6E6` / `structure #A3121A` / `ink #171314` / `ink-2 #6B6265` / `ink-2-inv #9A8F91` / `accent #DE0F16` / `accent-inv #FF6B6B`.

### Sovereign, rejected 2026-08-19
Violet `#834CE2`. Rejected on **differentiation, not aesthetics**: Mike Sherrard already owns purple in this niche. It was also the only hue in the set with no grounding in the research; nearest real precedent was BHHS cabernet `#552448`.
`bg #FFFFFF` / `bg-2 #F8F6FB` / `bg-inv #150E33` / `line #E8E4F0` / `structure #4E1F9E` / `ink #150E33` / `ink-2 #605771` / `ink-2-inv #948AAE` / `accent #834CE2` / `accent-inv #B08CF5`.

## Token specs

Every pairing below is WCAG 2.1 computed, never eyeballed. All five files share one schema: 13 color tokens plus 6 type tokens, so swapping palettes is a one-line `<link>` change.

### Ultramarine, `tokens-v4-ultramarine.css`

**SHORTLIST.** One accent only, no --la-accent-2. #1768E5 clears AA in both directions, 5.06:1 as text on white and 5.06:1 for white on it, so accent and accent-txt are the same value. This is the whole reason to prefer it over the old gold.

| Token | Hex | Role |
|---|---|---|
| `--la-bg` | `#FFFFFF` | primary surface, pure white |
| `--la-bg-2` | `#F7F8FA` | sunken fill, table rows, inset panels |
| `--la-bg-inv` | `#050E3D` | inverted surface, navy near-black |
| `--la-line` | `#E4E7EF` | hairline and divider on bg, non-text |
| `--la-structure` | `#0B3FA8` | deep blue, chart bars, structural fills, large headings |
| `--la-ink` | `#050E3D` | primary text on bg |
| `--la-ink-2` | `#55627F` | secondary text on bg and bg-2 |
| `--la-ink-inv` | `#FFFFFF` | primary text on bg-inv |
| `--la-ink-2-inv` | `#6A7CAF` | secondary text on bg-inv |
| `--la-accent` | `#1768E5` | THE accent, fills, buttons, links |
| `--la-accent-on` | `#FFFFFF` | text placed ON accent |
| `--la-accent-txt` | `#1768E5` | accent used AS text on bg or bg-2 |
| `--la-accent-inv` | `#5B9BFF` | accent used AS text on bg-inv |

**Evidence:** ink #050E3D is Real Broker's measured ink. accent #1768E5 is Tom Ferry's measured CTA blue. Serhant's only accent is navy #001A72.

**Contrast:** `ink_on_bg` 18.48, `ink-2_on_bg` 6.11, `ink-inv_on_bg-inv` 18.48, `ink-2-inv_on_bg-inv` 4.5, `accent-on_on_accent` 5.06, `accent-txt_on_bg` 5.06, `accent-txt_on_bg-2` 4.76, `accent-inv_on_bg-inv` 6.67

### Meridian, `tokens-v4-meridian.css`

**SHORTLIST.** This is the only palette in the set where pure #000000 is correct, because it is a surface and not text. The pop here is structural, not chromatic: full-bleed black sections against white, with navy #001A72 as the single accent. Serhant, Compass and Eklund Gomes all build this way. Every value except the two greys is measured, nothing is invented.

| Token | Hex | Role |
|---|---|---|
| `--la-bg` | `#FFFFFF` | primary surface, pure white |
| `--la-bg-2` | `#F7F7F7` | sunken fill, table rows. Serhant's measured grey |
| `--la-bg-inv` | `#000000` | inverted surface, true black. A surface, never text |
| `--la-line` | `#E3E3E3` | hairline and divider on bg, non-text |
| `--la-structure` | `#001A72` | navy. Chart bars, structural fills, large headings |
| `--la-ink` | `#212121` | primary text on bg. Serhant's measured ink |
| `--la-ink-2` | `#5C5C5C` | secondary text on bg and bg-2 |
| `--la-ink-inv` | `#FFFFFF` | primary text on bg-inv |
| `--la-ink-2-inv` | `#B9B9B9` | secondary text on bg-inv. Eklund Gomes' measured grey |
| `--la-accent` | `#001A72` | THE accent. Fills, buttons, links. Serhant's exact navy |
| `--la-accent-on` | `#FFFFFF` | text placed ON accent |
| `--la-accent-txt` | `#001A72` | accent used AS text on bg or bg-2. Same value, huge margin both ways |
| `--la-accent-inv` | `#7290FF` | accent used AS text on bg-inv. Raw navy is 1.39 on black |

**Evidence:** bg-inv #000000, bg-2 #F7F7F7, ink #212121 and accent #001A72 are all Serhant's measured values. ink-2-inv #B9B9B9 is Eklund Gomes' measured grey.

**Contrast:** `ink_on_bg` 16.1, `ink-2_on_bg` 6.69, `ink-inv_on_bg-inv` 21.0, `ink-2-inv_on_bg-inv` 10.7, `accent-on_on_accent` 15.1, `accent-txt_on_bg` 15.1, `accent-txt_on_bg-2` 14.09, `accent-inv_on_bg-inv` 7.15

### Vector, `tokens-v4-vector.css`

**SHORTLIST, new 2026-08-19.** Built after Ryan narrowed to Ultramarine vs Meridian. It is the hybrid: Meridian's white-plus-true-black surface system, which is where its pop actually comes from, with Ultramarine's #1768E5 as the single accent instead of a deep navy. Meridian's navy accent is 15.1:1 and therefore invisible as a pop; this keeps the black-against-white structure and puts a real accent back on top of it.

| Token | Hex | Role |
|---|---|---|
| `--la-bg` | `#FFFFFF` | primary surface, pure white |
| `--la-bg-2` | `#F7F8FA` | sunken fill, table rows, inset panels. Faint cool cast |
| `--la-bg-inv` | `#000000` | inverted surface, true black. A surface, never text |
| `--la-line` | `#E4E7EF` | hairline and divider on bg, non-text |
| `--la-structure` | `#0B3FA8` | deep blue. Chart bars, structural fills, large headings |
| `--la-ink` | `#050E3D` | primary text on bg |
| `--la-ink-2` | `#55627F` | secondary text on bg and bg-2 |
| `--la-ink-inv` | `#FFFFFF` | primary text on bg-inv |
| `--la-ink-2-inv` | `#9AA3BC` | secondary text on bg-inv |
| `--la-accent` | `#1768E5` | THE accent. Fills, buttons, links |
| `--la-accent-on` | `#FFFFFF` | text placed ON accent |
| `--la-accent-txt` | `#1768E5` | accent used AS text on bg |
| `--la-accent-inv` | `#5B9BFF` | accent used AS text on bg-inv |

**Evidence:** bg-inv #000000 is Serhant's measured surface. accent #1768E5 is Tom Ferry's measured CTA blue. ink #050E3D is Real Broker's measured near-black. ink-2-inv is derived.

**Contrast:** `ink_on_bg` 18.48, `ink-2_on_bg` 6.11, `ink-inv_on_bg-inv` 21.0, `ink-2-inv_on_bg-inv` 8.34, `accent-on_on_accent` 5.06, `accent-txt_on_bg` 5.06, `accent-txt_on_bg-2` 4.76, `accent-inv_on_bg-inv` 7.58

### Signal, `tokens-v4-signal.css`

**Also-ran.** Tom Ferry runs orange #F26F21 as his second accent. Raw, it is 2.97:1 on white and cannot be text or carry white text. #BB4C0A is that same hue pushed until it clears AA in both directions, so one value does the button and the link.

| Token | Hex | Role |
|---|---|---|
| `--la-bg` | `#FFFFFF` | primary surface, pure white. Do not tint it |
| `--la-bg-2` | `#FBF7F4` | sunken fill, table rows, inset panels. Faintly warm |
| `--la-bg-inv` | `#1A1310` | inverted surface, warm near-black |
| `--la-line` | `#EEE7E1` | hairline and divider on bg, non-text |
| `--la-structure` | `#7E3405` | deep burnt orange. Chart bars, structural fills, large headings |
| `--la-ink` | `#1A1310` | primary text on bg |
| `--la-ink-2` | `#665C55` | secondary text on bg and bg-2 |
| `--la-ink-inv` | `#FFFFFF` | primary text on bg-inv |
| `--la-ink-2-inv` | `#A0928A` | secondary text on bg-inv |
| `--la-accent` | `#BB4C0A` | THE accent. Fills, buttons, links |
| `--la-accent-on` | `#FFFFFF` | text placed ON accent |
| `--la-accent-txt` | `#BB4C0A` | accent used AS text on bg or bg-2. Same value, it clears both |
| `--la-accent-inv` | `#F2874A` | accent used AS text on bg-inv |

**Evidence:** accent from Tom Ferry's orange #F26F21, corrected. Warm near-black ink follows finding 3.

**Contrast:** `ink_on_bg` 18.35, `ink-2_on_bg` 6.51, `ink-inv_on_bg-inv` 18.35, `ink-2-inv_on_bg-inv` 6.09, `accent-on_on_accent` 5.06, `accent-txt_on_bg` 5.06, `accent-txt_on_bg-2` 4.75, `accent-inv_on_bg-inv` 7.29

### Ivory, `tokens-v4-ivory.css`

**Also-ran.** The 'lighter color' reading of the brief rather than the pure-white one. Corcoran runs a warm cream #FEF1E1 as its secondary surface. Here there is no accent hue: buttons and links are the ink itself. Compass and Eklund Gomes ship with no accent at all and look expensive doing it. Included as the control, so you can see what zero color costs you in energy.

| Token | Hex | Role |
|---|---|---|
| `--la-bg` | `#FDF9F2` | primary surface, warm paper. This palette is the one that is NOT pure white |
| `--la-bg-2` | `#F6EEDF` | sunken fill, deeper cream. The palette's signature |
| `--la-bg-inv` | `#17130E` | inverted surface, warm near-black |
| `--la-line` | `#EDE3D4` | hairline and divider on bg, non-text |
| `--la-structure` | `#443B31` | warm dark brown. Chart bars, structural fills |
| `--la-ink` | `#17130E` | primary text on bg |
| `--la-ink-2` | `#675E54` | secondary text on bg and bg-2 |
| `--la-ink-inv` | `#FFFFFF` | primary text on bg-inv |
| `--la-ink-2-inv` | `#A79C8E` | secondary text on bg-inv |
| `--la-accent` | `#17130E` | THE accent, and it is the ink. Fills, buttons, links |
| `--la-accent-on` | `#FFFFFF` | text placed ON accent |
| `--la-accent-txt` | `#17130E` | accent used AS text on bg or bg-2 |
| `--la-accent-inv` | `#FFFFFF` | accent used AS text on bg-inv |

**Evidence:** bg-2 is Corcoran's cream #FEF1E1 family. The no-accent construction is Compass and Eklund Gomes.

**Contrast:** `ink_on_bg` 17.61, `ink-2_on_bg` 6.05, `ink-inv_on_bg-inv` 18.49, `ink-2-inv_on_bg-inv` 6.86, `accent-on_on_accent` 18.49, `accent-txt_on_bg` 17.61, `accent-txt_on_bg-2` 16.03, `accent-inv_on_bg-inv` 18.49

## Type, `v4-fonts.html` (current) and `v4-type.html` (superseded)

Type is a separable decision from color. `v4-fonts.html` is where the type decision actually gets made: 12 head + body **pairings**, color held constant on Vector so only type varies. Every card forces the same 41px headline, the same 13px paragraph with an inline link, and the same two 320px thumbnails, because display faces all look good big and the real decision happens at caption size and at thumbnail size.

**Ryan rejected Space Grotesk, Fraunces and Bodoni Moda outright on 2026-08-19.** Do not re-propose them. That removed every serif from the set, so this is now a decision between grotesks and hierarchy has to be bought with weight, size and width rather than with a contrast of face.

Surviving faces, and nothing outside this list: **Poppins, Inter, Archivo, Inter Tight, Barlow, Raleway.**

**Raleway has two separate roles and only one of them works.** As a display face it is P12, and at 800 it thickens and loses the elegance that made it appealing. As *subtext*, meaning the eyebrow, the subhead and the small label but never a paragraph, it is P02, P05, P08 and P09, and there it works: it stays at 15px and up on a single short line, which is the only place its low x-height and tight apertures are not a liability.

| # | Head / subtext / body | Character | Note |
|---|---|---|---|
| P01 | Poppins 800 / Inter | The v1 default | Safe and legible, and the most common combination in the coaching space, which is why it does not differentiate |
| P02 | Poppins 800 / **Raleway 600** / Inter | v1 head, Raleway accent | Keeps the existing Poppins headline, adds Raleway on the one short line under it |
| P03 | Poppins 800 / Barlow | Geometric + compact | Barlow is narrower than Inter, more words per line |
| P04 | Archivo 800 / Inter | Editorial | Closest of anything here to the measured pedigree set. Front-runner |
| P05 | Archivo 800 / **Raleway 600** / Inter | Editorial + accent | Softens an otherwise very tight, very grotesk page without touching body copy |
| P06 | Archivo 800 / Barlow | All-grotesk | Most brokerage-looking. Risk: close relatives, so hierarchy leans on size and weight |
| P07 | Barlow 800 / Inter | Barlow head, control | Narrower and slightly rounded. Friendlier than Archivo, less trendy than Poppins. The control for P08 |
| P08 | Barlow 800 / **Raleway 600** / Inter | **CHOSEN** | Picked 2026-08-19 ("p08 seems to be best"), and the 800 headline weight confirmed against the 600-900 ladder the same day |
| P09 | Barlow 800 / **Raleway 600** / Barlow | One family + accent | Cheap and consistent, but the headline needs a big weight and size gap to stay separate |
| P10 | Barlow 800 / Archivo | Barlow head, heavier body | Archivo has more presence than Inter at body size |
| P11 | Inter Tight 800 / Inter | One family | Cheapest to maintain, least distinctive |
| P12 | Raleway 800 / Inter | Raleway as display | Thickens at 800 and loses its elegance. Judge it in the thumbnails |

**Tracking is deliberately not constant across pairings.** Values in use: Poppins `-0.03em`, Archivo `-0.032em`, Barlow `-0.028em`, Inter Tight `-0.032em`, Raleway `-0.028em`.

**Ruled out on the record, do not re-propose:**

| Skip | Why |
|---|---|
| Raleway as running body | The distinction that matters. Refined at 15px on a short line, mushy at 13px across a paragraph, and 13px across a paragraph is what a Skool post is |
| Raleway head + Raleway subtext | Two low x-height lines stacked. The subhead stops reading as a separate level and the block flattens |
| Poppins + Poppins | Geometric, wide, low x-height. Tiring in a paragraph |
| Inter Tight + Inter at similar sizes | Indistinguishable, the page reads flat. Now that every serif is gone this applies to Archivo + Barlow and Barlow + Barlow too |

### Headline weight, `v4-weights.html`

P08 fixes the faces but not the headline weight. `v4-weights.html` locks everything from P08 (Raleway 600 subtext, Inter 400/500 body, Vector palette) and moves **only** the Barlow headline weight across 600, 700, 800 and 900. Ryan asked for the full 600 to 900 range on 2026-08-19.

**Tracking is not held constant, on purpose.** Heavier weights need more negative tracking, because the letterforms widen and the space between them looks proportionally larger. A single locked value would make 900 look loose and 600 look cramped, and the comparison would be measuring tracking instead of weight. The page ships the values you would actually use.

| Weight | Name | Tracking | Verdict |
|---|---|---|---|
| 600 | SemiBold | `-0.020em` | Not a headline weight. Reads like an enlarged subhead, and the strokes thin out on the black thumbnail. Useful as a card title or section label at 18 to 22px |
| 700 | Bold | `-0.024em` | Fine and unremarkable. Only three weight steps clear of Inter 400 body, so it buys the least hierarchy |
| 800 | ExtraBold | `-0.028em` | **The recommendation.** Dense enough to hold a thumbnail, open enough that the counters in a, e and o stay clear. Five steps clear of Inter 400, which is where the hierarchy comes from now that no serif is in play |
| 900 | Black | `-0.032em` | Loudest at thumbnail size. Cost is up close: counters tighten and long headlines get heavy at 41px. Barlow is narrow enough to survive this better than Poppins would |

**DECIDED 2026-08-19: 800 everywhere.** Ryan reviewed the full 600 to 900 ladder and took the recommendation, "the original recommended one is fine". No page/thumbnail split, the same Barlow 800 carries both. The split (800 on page, 900 in thumbnails) was offered and not taken, so do not re-propose it. **The type spec is therefore closed: Barlow 800 headline at `-0.028em`, Raleway 600 subtext, Inter 400/500 body.**

Verified by computed-style probe: all four weights resolve to real loaded Barlow files (600, 700, 800, 900), not browser-synthesised bold. Barlow 900 had to be added to the Google Fonts URL, `v4-fonts.html` only loads up to 800.

### Superseded: `v4-type.html`

Body is Inter in all six, only the display face changes. **Stale:** three of its six faces (Space Grotesk, Fraunces, Bodoni Moda) are now rejected, and it sits on Ultramarine rather than Vector. Kept for the record only.

| # | Display face | Weight | Tracking | Reads as |
|---|---|---|---|---|
| T1 | Poppins | 800 | -0.03em | The v1 default. Geometric, friendly, very common in the coaching space |
| T2 | Archivo | 800 | -0.03em | Tighter and more editorial. Closest to the pedigree set |
| T3 | Bodoni Moda | 700 | -0.01em | High-contrast serif. Luxury, in the Sotheby's and Elliman direction |
| T4 | Space Grotesk | 700 | -0.03em | Technical, slightly odd letterforms. Reads "systems" |
| T5 | Fraunces | 800 | -0.03em | Warm soft serif. Human and less corporate |
| T6 | Inter Tight | 800 | -0.03em | One-family system. Cheapest to maintain, least distinctive |

## Migrating from v1

| v1 token | v4 equivalent | Note |
|---|---|---|
| `--la-teal` | `--la-structure` | The role survives, the hue does not |
| `--la-gold` | `--la-accent` | v1 gold failed as text at `2.16` on white and `1.86` on the teal |
| `--la-ink` | `--la-ink` | Same role, new color-cast near-black |
| `--la-paper` | `--la-bg` | White in four of five, warm paper in Ivory |

## Cost of adopting any v4

1. Regenerate every logo. All current lockups are built on teal and gold.
2. Refresh the ~44 per-project asset copies under `hyperframes-student-kit/video-projects/*/assets/`. These do not auto-update.
3. Rebuild the Classroom-Covers set.
4. Update `BRAND-GUIDE.md` and retire `tokens.css` to `tokens-v1.css`.

## Open

- No palette adopted. **v1 remains canonical.**
- No tagline-free wordmark lockup exists under 240px.
- Type (T1 to T6) is unmade and independent of the color decision.
