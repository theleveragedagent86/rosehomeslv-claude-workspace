# What high-pedigree US real estate brands actually do

Research date: 2026-08-19. Scope: The Leveraged Agent (Skool brand). Not Rose Homes LV.

**How this was gathered.** Every number below was read out of the live production site with a
headless browser, pulling computed `font-family`, `font-weight`, `font-size`, `letter-spacing`
and an area-weighted census of background and text colors. Nothing here is a secondhand claim
from a logo-roundup blog. Where a brand licenses a font that is not publicly available, the
font name is what the site actually requests in its `@font-face` rules.

---

## The evidence

| Brand | Display face | Body face | Base surfaces | Ink | Accent |
|---|---|---|---|---|---|
| **SERHANT.** | Montserrat 800, 68px, -1.5px | Montserrat 400, 14px | `#000000` `#FFFFFF` `#F7F7F7` | `#212121` | navy `#001A72` |
| **The Agency** | Playfair Display 400 (serif) | Lato 400, 16px | `#FFFFFF` `#000000` `#F7F8F6` | `#000000` | red `#ED2127` |
| **Compass** | Compass Serif 700 (custom) | Compass Sans / Open Sans | `#FFFFFF` `#DADADA` | `#171717` | none |
| **Douglas Elliman** | Sainte Colombe (serif) + Euclid Circular A 300 uppercase +2px | Euclid Circular A 300, 18px | `#100B28` near-black | `#FFFFFF` | none |
| **Eklund Gomes** | Canela + Heldane Text (serif) | Equip Extended, uppercase +1.28px | `#000000` `#303030` `#FFFFFF` | `#B9B9B9` | none |
| **The Altman Brothers** | Barlow Semi Condensed | Barlow / Raleway | `#FFFFFF` `#000000` | `#333333` | gold `#D2AD41` |
| **Sotheby's Int'l Realty** | Freight Big + Mercury Display (serif) | Benton Sans | `#FFFFFF` `#E0E0E0` | `#002349` | navy `#002349` |
| **The Corcoran Group** | Chronicle Display 325 (serif) | Avenir / Adelle Sans | `#FFFFFF` `#FEF1E1` | `#212529` | rose `#C0535C` |
| **Real Broker** | PP Telegraf | Inter | `#FFFFFF` `#F5F5F5` | `#050E3D` | pink `#F96B88` |
| **Tom Ferry** (coaching) | Barlow Condensed 700 UPPERCASE, 68px, -0.95px | Barlow, 12px | `#FFFFFF` `#000000` | `#141C29` | blue `#1768E5`, orange `#F26F21` |

---

## Seven things they all do

**1. The base is achromatic. Always.**
Nine of ten build on pure white, pure black, or a near-black. Not one uses a tinted cream or
beige as the primary surface. Corcoran's `#FEF1E1` is the single cream in the set and it is a
minor accent block, not the page.

**2. One accent, and it covers almost no area.**
Where color exists it is a single hue: Agency red, Sotheby's navy, Altman gold, Corcoran rose,
Real pink, Serhant navy. Three brands (Compass, Elliman, Eklund Gomes) ship zero chromatic
accent at all. Nobody runs two decorative colors on top of a tinted base.

**3. Ink is a near-black with a color cast, never pure `#000` in the modern ones.**
`#171717`, `#141C29`, `#100B28`, `#050E3D`, `#002349`, `#212529`. The cast is almost always
blue or navy. This is the detail that separates the expensive-looking sites from the cheap ones.

**4. Two fonts. Never one, never three.**
A display face and a neutral text face, with a hard division of labor. Every brand in the set.

**5. Display type splits into exactly two camps.**

*Camp A, luxury listings* (Agency, Compass, Elliman, Eklund Gomes, Sotheby's, Corcoran):
high-contrast display **serif** at **light weight**, 325 to 400, large, near-zero tracking.
Chronicle, Canela, Heldane, Freight Big, Mercury, Playfair, Sainte Colombe. This sells houses
to consumers.

*Camp B, personality and performance* (Serhant, Tom Ferry, Altman): **heavy sans**, geometric
or condensed, 700 to 800, **negative tracking** from -0.95px to -1.5px, frequently uppercase.
This sells the operator.

**6. Labels are wide-tracked uppercase.**
Camp A pairs its light serif headline with tiny all-caps sans labels at +1.28px to +2px
tracking. That tension, huge soft serif over small hard caps, is most of the "luxury" effect.

**7. The wordmark is the logo.**
Serhant, Eklund | Gomes, Compass, Corcoran, Elliman: the name set in the display face, all
caps, wide tracking, no icon, no house, no key, no roof. SERHANT.'s period is the entire mark.

---

## The finding that matters for The Leveraged Agent

**Serhant is the only brand in the set that reads luxury pedigree and sells to agents.** He
does it by running Camp B mechanics (Montserrat 800 at -1.5px, loud, personality-forward) under
Camp A discipline (black and white only, one navy accent, wordmark-only logo, no ornament).
That is precisely the position you asked for: mass appeal without looking cheap.

Tom Ferry is the pure coaching play and he abandons the pedigree cues entirely: saturated blue
CTAs, an orange secondary, condensed uppercase. It converts, and it looks like an info product.

**Your competitive set is coaching, not luxury listings.** But the pedigree cues are what stop
a coaching brand from looking like an info product. Borrow the discipline, not the serif.

---

## Scoring your three palettes against the convention

| | Achromatic base | One accent | Near-black tinted ink | Verdict |
|---|---|---|---|---|
| **v1** (cream `#F7F1E3`) | fails, tinted cream is the page | fails, gold + sage | passes, `#08343E` | weakest, off-convention on two of three |
| **Voltage** (`#04171C`) | passes, this is the Elliman/Compass move exactly | borderline, aqua + amber | passes | strongest if amber is demoted to data-only |
| **Ember** (`#FBF7F0`) | borderline, paper not white, Corcoran is the only precedent | passes, ember is the single accent | passes, `#0A2028` | on-convention but orange reads startup, not pedigree |

**Type: you are already correct and should not change it.** Poppins (geometric display) plus
Inter (neutral grotesk) is structurally the Serhant/Real Broker pattern. Real Broker literally
uses Inter for body. Your `--la-track-head: -0.03em` is tighter than Serhant's -0.022em and
Ferry's -0.014em, which is fine and reads deliberate. The change worth making is weight: push
Poppins headlines to 700/800. Serhant runs 800.

---

## The cheapest fix, and the one I would actually recommend

**Your gold is already the pedigree gold.** The Altman Brothers run `#D2AD41`. Your canonical
gold is `#E8A33D` and your classroom-cover gold is `#D9A441`. That is the same color. The gold
was never the problem.

**The cream is the problem.** No high-pedigree brand in the United States uses a tinted cream as
its primary surface, and the cream is what forces every accent to stay dark and low-chroma,
which is the exact reason nothing pops.

So the minimum-change, maximum-credibility move is a fourth option:

- Base: pure `#FFFFFF` and `#000000`, plus one near-white `#F7F7F7` for sunken blocks
- Ink: keep `#08343E`, the teal-cast near-black, which is dead on convention
- Accent: keep the gold, **one** accent only, used at small area
- Drop sage entirely
- Poppins 700/800 for display, Inter for body, wide-tracked uppercase Inter for labels

That is Altman's formula with your ink, it keeps your existing logo files valid on white, and it
costs nothing to adopt. Voltage remains the option if you want the brand to read tech-forward
rather than broker-forward, and it is genuinely well built, but it requires regenerating logos.

---

## Substitutions used in the visual board

`pedigree-board.html` renders type specimens with Google Fonts. Licensed faces that are not
publicly available are substituted and labeled as such on the board itself:

| Real face | Substitute on board |
|---|---|
| Canela, Heldane, Chronicle, Freight Big, Mercury, Sainte Colombe, Compass Serif | Cormorant Garamond |
| Euclid Circular A, PP Telegraf, Compass Sans | Poppins |
| Equip Extended, Benton Sans, Adelle Sans, Avenir | Inter |

Montserrat, Playfair Display, Lato, Barlow, Barlow Condensed, Barlow Semi Condensed and Raleway
are real on the board because they are the real faces those brands use.

---

## Not verified

- No brand in this set publishes a public brand guide with named hex values, so every color here
  is measured from the rendered site, not quoted from a brandbook. Treat them as accurate to
  what ships, not as official token names.
- Josh Flagg, Aaron Kirman, Jade Mills and Tracy Tutor were on the target list and were not
  inspected. NOT FOUND, not researched.
- reverseselling.com (Brandon Mulrenin) was on the target list. Navigation was blocked and it was
  replaced with corcoran.com to hold the sample at ten. Tom Ferry is therefore the only pure
  coaching brand in the set, which is the weakest part of this evidence.
- Visual companion: `pedigree-board.html`. Serve it over localhost (`ruby serve.rb`, port 8091),
  do not open it as file://.
