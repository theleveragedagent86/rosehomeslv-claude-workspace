# 09 — New Construction Hub: Design System Spec

**Deliverable:** the complete, buildable design system for the Rose Homes LV
`/new-construction` authority hub (~8,000 to 11,000 words, ~18 sections, sticky TOC rail,
20 builder cards, 5 data tables, FAQ, live-listings slot), shipped as a raw-HTML embed
inside Lofty CMS.

**Read order for the builder:** §0 (what carries over unchanged) → §1 tokens → §2 type →
§3 TOC rail → §4 components → §5 rhythm → §6 responsive → §7 a11y → §8 guardrails.

**Sources this spec is built on**
- `~/.claude/skills/new-construction/landing-page-template.md` (Ryan's established system)
- `~/.claude/skills/new-construction/builder-brand-colors.md` (canonical builder hexes)
- `Rose Homes LV/Brand/Personal Brand Strategy/checklist-carousel/slides/*.html` (house palette)
- `Rose Homes LV/Brand/ryan-rose-sales-letter.html`, `ryan-rose-cover-letter.html`,
  `ryan-rose-relaunch-roadmap.html` (secondary palette + Playfair precedent)
- `01-hub-page-teardown.md`, `06-conversion-and-tech.md`, `08-lofty-porting-constraints.md`

---

## 0. What carries over from Ryan's template UNCHANGED (do not re-litigate)

These are settled. Copy them verbatim. Do not redesign, do not "improve".

| Thing | Status | Where it lives |
|---|---|---|
| Cream/editorial base (`--dark #faf8f3`, `--dark-surface #f2efe7`, `--dark-card #ffffff`, `--cream #f4f1e7`, `--text-dark #2a2520`) | **KEEP verbatim** | template §Design Tokens |
| Alpha-dark scale `--w60 / --w40 / --w20 / --w08 / --w04` | **KEEP verbatim** (usage rules tightened in §7) | template §Design Tokens |
| JS wrapper-stripper for Lofty full-bleed escape | **KEEP verbatim, byte for byte** | template §Lofty CMS Full-Bleed Escape |
| The ban on `width:100vw; left:50%; margin-left:-50vw` | **KEEP.** It shipped a real bug on Sierra at Skyeview. Never reach for it. | template §Lofty CMS Full-Bleed Escape |
| Sections lay out at body width with internal padding + centered `.container` | **KEEP** | template §Lofty CMS Full-Bleed Escape |
| `position: fixed` sticky header, 60px tall, cream blur, `filter: invert(1)` on the Real Broker logo | **KEEP** | template §1 Sticky Header |
| Section label pattern: 11px, 600, 3px tracking, uppercase, trailing rule line | **KEEP the pattern**, retune the values (§4.5) | Delamar reference `.section-label` |
| `--radius: 10px` / `--radius-sm: 6px`, pill CTAs | **KEEP.** This is the single loudest anti-clone signal against NRG's square-corner system. | template §Design Tokens |
| Inter as the body face | **KEEP** | template §Typography |
| Bebas Neue in the brand | **KEEP, but demoted.** See §2.3. | template §Typography |
| No inline `<form>`. CTAs use `href="#contact"` and JS scrolls to the Lofty form below the embed. | **KEEP** | template §Lead Capture, doc 08 §1 |
| Scroll-reveal via IntersectionObserver | **KEEP** | template |

### Departures from the template, each justified in place

1. **A house accent replaces the per-builder accent.** §1.1
2. **"White text on accent" is dropped for the primary CTA.** It fails WCAG with a gold accent (2.26:1). §1.4
3. **Playfair Display is added for the 18 long H2s; Bebas Neue is demoted to H1 + numerals + CTA bands.** §2.3
4. **`overflow-x: hidden` becomes `overflow-x: clip` on `html, body`.** Required for `position: sticky` to work. §3.4
5. **Long-form body text gets a dedicated `--text-body` token. `--w40` is banned for body copy** (measured 3.50:1, fails AA). §7.1
6. **The article zone does NOT alternate section backgrounds.** §5.1
7. **Scroll-spy JS is added** (NRG has none). §3.6

---

## 1. Resolved Rose Homes LV house palette

### 1.1 The problem, stated plainly

Ryan's template sets `--accent` **per builder**. This hub has 20 builders and no single
owner, so there is no builder to inherit from. The template's own fallback is
"default navy `#1a365d`", which is a generic placeholder, not a brand color.

**Rose Homes LV does have a real, documented house palette.** It is not in the
landing-page template because that template was written for builder-branded community
pages. It is in the Brand folder, and it is consistent across every piece Ryan has
made under his own name rather than a builder's.

### 1.2 Where each hex came from (cited)

| Hex | Role | Source file | Evidence |
|---|---|---|---|
| **`#C9A86E`** | House accent (brass/gold) | `Brand/Personal Brand Strategy/checklist-carousel/slides/*.html` + `checklist-pdf/checklist.html` | **150 occurrences**, by far the dominant color. Used for kicker, eyebrow, numerals, rules, pills, italic emphasis, borders, the `Rose Homes LV` wordmark accent, and the CTA box. |
| **`#b7955a`** | Accent hover (darker brass) | same carousel set | present as the one darker gold variant |
| **`#1C2333`** | House deep tone (cool navy ink) | same carousel set | **26 occurrences**, the slide background and the on-gold text color |
| **`#242d47`** | Navy elevated | same carousel set | the radial-gradient lift on the slide background |
| **`#8A8FA8`** | Muted slate | same carousel set | 17 occurrences, the index/handle text |
| **`#D8DCE8`** | Body text on navy | same carousel set | 16 occurrences, the body copy color on dark slides |
| **`#F7F5F0`** | Warm cream | `checklist-pdf/checklist.html` | the print/PDF page base |
| `#b8a88a`, `#c8b98a`, `#d4cabb`, `#e8e0d5` | Secondary sand family | `Brand/ryan-rose-sales-letter.html`, `ryan-rose-cover-letter.html`, `ryan-rose-relaunch-roadmap.html` | `#b8a88a` appears 6 to 10 times per file as the accent rule / border color |
| `#1a1a1a`, `#222222` | Near-black ink | same three letters | body ink |
| `#fafaf7`, `#fdfcfa` | Cream base | same three letters | page base, which is why `--dark: #faf8f3` in the template is already brand-consistent |

**Verdict: the brand is NOT undefined.** Rose Homes LV has a settled two-color house
signature: **warm brass `#C9A86E` over cool navy `#1C2333`**, on a cream base. The older
letters use a desaturated sand (`#b8a88a`) which is the same hue family, one step muted.
The carousel/checklist set is the newer and more systematized expression, and it is
literally new-construction branded content ("New Construction Buyer's Defense Checklist"),
so it is the correct precedent for this page.

### 1.3 The clone risk, and how we beat it

NRG's accent is `--gold: #d4b27c` on `--cream: #f7f4ee`. Ours is `#C9A86E` on `#faf8f3`.
Those are close enough that gold-on-cream alone will not differentiate us. **Four
structural moves carry the differentiation instead. All four are already Ryan's system:**

| Axis | NRG | Rose Homes LV | Visible? |
|---|---|---|---|
| Deep tone | `#2B221A` warm brown (their own teardown notes "it is NOT navy") | `#1C2333` cool navy | Yes, strongly. Brown vs blue-black reads instantly. |
| Geometry | `--radius: 0` everywhere, hard rectangles | `--radius: 10px`, pill CTAs | Yes. This is the loudest single signal. |
| Primary CTA | gold fill, navy text, square | navy fill, cream text, gold hairline, pill | Yes, and it also fixes an accessibility failure (§1.4) |
| Display face | Cormorant Garamond (old-style Garamond, low contrast, angled stress) | Playfair Display (Didone-adjacent, high contrast, vertical stress, ball terminals) + Bebas Neue | Yes. Very different silhouettes. |

Additional differentiators the competitor does not have at all: a scoped sticky article
rail (§3), TOC scroll-spy with a reading-progress indicator (§3.6), navy-tinted shadows
instead of neutral black, per-builder brand-color stripes on the builder cards (§4.1),
and properly scroll-locked tables with a sticky first column (§4.2).

### 1.4 Why the primary CTA is navy, not gold

Ryan's template rule is "Buttons keep white text on accent backgrounds." That rule was
written against builder accents like Pulte blue `#1b75a1`, where white text measures
**5.11:1** and passes AA.

With the Rose gold, white on `#C9A86E` measures **2.26:1**. That fails AA (4.5:1) and
even fails the 3:1 large-text floor. **We cannot ship a gold-fill button with white text.**

Resolution, which is also the anti-clone move:

- **Primary CTA:** `--navy` fill, `--dark` cream text (**14.79:1**), 1px `--accent` hairline.
- **Secondary CTA:** transparent fill, `--accent-ink` text (**5.28:1** on cream), 1.5px `--accent` border.
- **Gold as a fill** is reserved for dark surfaces only, where `#C9A86E` on `#1C2333`
  measures **6.96:1** and passes comfortably. That is the correct home for the gold:
  it is a dark-surface color, and `--accent-ink` is its cream-surface counterpart.

### 1.5 The `:root` block, ready to paste

```css
:root{
  /* ============================================================
     BASE — cream/editorial. Carried over verbatim from
     ~/.claude/skills/new-construction/landing-page-template.md
     ============================================================ */
  --dark:          #faf8f3;   /* body background, soft off-white cream */
  --dark-surface:  #f2efe7;   /* alternate section background */
  --dark-card:     #ffffff;   /* cards float on cream as pure white */
  --cream:         #f4f1e7;   /* input / spec-item backgrounds */
  --white:         #ffffff;
  --text-dark:     #2a2520;   /* headline ink, warm charcoal — 14.30:1 on --dark */

  /* ============================================================
     LONG-FORM ADDITIONS — new in this spec, see §7.1
     ============================================================ */
  --text-body:     #4a443d;   /* the 10,000 words. 9.05:1 on --dark, 8.36:1 on --dark-surface */
  --text-meta:     #68645f;   /* captions, bylines, table notes. 5.53:1 on --dark */

  /* ============================================================
     ROSE HOMES LV HOUSE ACCENT — brass
     #C9A86E sourced from Brand/Personal Brand Strategy/checklist-carousel
     ============================================================ */
  --accent:        #c9a86e;   /* fills on DARK surfaces only. 6.96:1 on --navy */
  --accent-hover:  #b5924f;   /* hover on dark surfaces */
  --accent-ink:    #846127;   /* the ONLY gold allowed on cream for text. 5.28:1 */
  --accent-muted:  rgba(201,168,110,0.12);  /* callout / takeaway backgrounds */
  --accent-tint:   rgba(201,168,110,0.06);  /* zebra rows, faint wash */
  --accent-line:   rgba(201,168,110,0.34);  /* hairlines, dividers */

  /* ============================================================
     ROSE HOMES LV HOUSE DEEP TONE — cool navy
     #1C2333 / #242d47 sourced from the same carousel set
     ============================================================ */
  --navy:          #1c2333;   /* CTA bands, table heads, primary buttons. 14.79:1 with cream text */
  --navy-deep:     #141a28;   /* deepest band, footer-adjacent. 16.37:1 with cream text */
  --navy-light:    #2a3350;   /* hover on navy. 11.72:1 with cream text */
  --navy-on:       #d8dce8;   /* muted body text ON navy. 11.46:1 */
  --navy-on-faint: rgba(216,220,232,0.62);

  /* ============================================================
     ALPHA-DARK SCALE — carried over verbatim. Usage rules in §7.1.
     ============================================================ */
  --w60: rgba(42,37,32,0.70);  /* 5.53:1 — OK for meta text */
  --w40: rgba(42,37,32,0.55);  /* 3.50:1 — DECORATIVE + >=24px ONLY. Never body copy. */
  --w20: rgba(42,37,32,0.30);  /* rules, dividers */
  --w08: rgba(42,37,32,0.10);  /* borders */
  --w04: rgba(42,37,32,0.04);  /* faint surfaces */

  /* ============================================================
     GEOMETRY
     ============================================================ */
  --radius:       10px;   /* kept from template — the anti-NRG signal */
  --radius-sm:     6px;
  --radius-pill: 999px;

  --container:  1180px;   /* was 1120px; +60px buys the rail without squeezing the measure */
  --measure:      68ch;   /* prose column cap, ~673px at 18px Inter */
  --rail:        250px;   /* TOC rail width */
  --rail-gap:     48px;
  --nav-h:        60px;   /* Ryan's fixed header height */
  --anchor-off:   84px;   /* --nav-h + 24 */

  /* ============================================================
     SHADOWS — navy-tinted, layered, never flat.
     Tinting with --navy is the trick 06-conversion-and-tech.md §2.d
     flags as worth stealing from NRG's property-detail sub-theme.
     ============================================================ */
  --shadow-sm:   0 1px 2px rgba(28,35,51,.05);
  --shadow-card: 0 1px 2px rgba(28,35,51,.05), 0 6px 18px -10px rgba(28,35,51,.16);
  --shadow-lift: 0 2px 4px rgba(28,35,51,.06), 0 14px 32px -14px rgba(28,35,51,.26);
  --shadow-rail: 0 1px 2px rgba(28,35,51,.04), 0 10px 30px -18px rgba(28,35,51,.22);
  --shadow-band: 0 24px 60px -32px rgba(28,35,51,.50);
  --shadow-focus: 0 0 0 3px rgba(28,35,51,.18);

  /* ============================================================
     MOTION — only transform + opacity are ever animated. §8.
     ============================================================ */
  --t:      220ms cubic-bezier(.2,.6,.2,1);
  --t-slow: 420ms cubic-bezier(.2,.6,.2,1);
}
```

### 1.6 Builder brand colors: `builder-brand-colors.md` wins, and the template is stale

**Finding that must be surfaced.** `builder-brand-colors.md` and the
`## Builder Accent Colors` table in `landing-page-template.md` **disagree on 11 of 12
builders**, and several of the template's values are simply wrong:

| Builder | `builder-brand-colors.md` (canonical) | `landing-page-template.md` (stale) |
|---|---|---|
| Pulte | `#033764` Astronaut Blue (Verified) | `#1b75a1` |
| Lennar | `#005DAA` Lennar Blue (Verified) | `#0057a0` |
| KB Home | `#FFC527` Lightning Yellow (Verified) | `#c8102e` (red) |
| Toll Brothers | `#3E7C84` Ming Teal (Verified) | `#8b6f4e` (brown) |
| Taylor Morrison | `#0060AE` Endeavour Blue (Verified) | `#003d6b` |
| D.R. Horton | `#003087` Horton Blue | `#00703c` (green) |
| Richmond American | `#B91D2C` Richmond Red | `#6b1d2a` |
| Tri Pointe | `#1F2D3D` Tri Pointe Navy | `#f37021` (orange) |
| Beazer | `#A7122A` Beazer Red PMS 187 (Verified) | `#003b5c` (blue) |
| Century Communities | `#4A104A` Crown Purple (Verified) | `#1a3a5c` |
| Woodside | `#1B365D` Woodside Navy | `#2d5a27` (green) |

**Use `builder-brand-colors.md`. Ignore the template table.** A separate cleanup task
should correct `landing-page-template.md`.

**Gap: Shea Homes is not in `builder-brand-colors.md`.** The stale template lists
`#9e7e38`. Mark it **NOT VERIFIED** in the build and flag it, per the workspace
factual-only rule.

**The 20 builder cards** (`--b` set inline per card):

```
Lennar               #005DAA      Beazer Homes        #A7122A
KB Home              #FFC527      LGI Homes           #1F4D3D
D.R. Horton          #003087      Century Communities #4A104A
Pulte / Del Webb     #033764      Meritage Homes      #005495
Toll Brothers        #3E7C84      Woodside Homes      #1B365D
Richmond American    #B91D2C      Blue Heron          #0E0E0E
Tri Pointe Homes     #1F2D3D      Christopher Homes   #1F1F1F
Taylor Morrison      #0060AE      Harmony Homes       #3F3F3F
Shea Homes           NOT VERIFIED StoryBook Homes     #5B3A2E
Signature Homes      #1A1A1A      Touchstone Living   #C73E2B
```

**Hard a11y rule:** the builder brand color is **decorative only**. It may be a stripe,
a tint, or a rule. It may **never** carry text, and it may **never** be the sole
carrier of information. KB Home's `#FFC527` measures 1.58:1 on white, so any
text-on-brand-color treatment is dead on arrival. §4.1 is designed around this.

---

## 2. Typographic system for long-form reading

### 2.1 The three faces

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Playfair+Display:ital,wght@0,600;1,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

```css
:root{
  --font-display: 'Bebas Neue', 'Arial Narrow', sans-serif;   /* H1, numerals, CTA bands */
  --font-head:    'Playfair Display', Georgia, 'Times New Roman', serif;  /* the 18 H2s */
  --font-body:    'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
}
```

Six font files total. Three families per page is exactly what NRG runs
(`06-conversion-and-tech.md` §2.d: "Three families per page, not two"), so this is not
bloat, it is parity with the benchmark at a smaller payload.

**Playfair Display is not a new brand element.** It is already Ryan's display face
everywhere he writes under his own name rather than a builder's: the checklist carousel
(47 declarations), `ryan-rose-sales-letter.html`, `ryan-rose-cover-letter.html`,
`ryan-rose-relaunch-roadmap.html`. Bringing it into the hub is brand *continuity*, not
brand invention. Montserrat (also in the carousel) is deliberately dropped, because Inter
already covers that role and a fourth family is not worth the request.

### 2.2 The scale

Base is **18px**, not 16px. On a 25-minute read, 16px Inter at a 68ch measure is
measurably more tiring, and the competitor tops out at 18px on its own `--text-base`.

| Role | Family | Size | Line-height | Weight | Tracking | Case |
|---|---|---|---|---|---|---|
| **H1** (once, hero) | Bebas Neue | `clamp(52px, 9vw, 96px)` | `0.92` | 400 | `0.02em` | uppercase |
| **H2** (18 sections) | Playfair Display | `clamp(28px, 3.4vw, 40px)` | `1.18` | 600 | `-0.015em` | sentence |
| **H3** (sub-heads, FAQ Qs) | Inter | `clamp(19px, 1.5vw, 22px)` | `1.35` | 700 | `-0.01em` | sentence |
| **H4** (card titles) | Inter | `17px` | `1.35` | 700 | `-0.005em` | sentence |
| **Body** | Inter | `18px` | `1.75` | 400 | `0` | sentence |
| **Lede** (1st para of a section) | Inter | `20px` | `1.68` | 400 | `-0.003em` | sentence |
| **Small / meta** | Inter | `14px` | `1.6` | 400 | `0` | sentence |
| **Caption / figcaption** | Inter | `12.5px` | `1.55` | 400 italic | `0.01em` | sentence |
| **Eyebrow / section label** | Inter | `11px` | `1` | 700 | `0.22em` | uppercase |
| **Table head** | Inter | `12px` | `1.35` | 600 | `0.08em` | uppercase |
| **Table cell** | Inter | `15px` | `1.5` | 400 | `0` | sentence |
| **Stat numeral** | Bebas Neue | `clamp(34px, 4vw, 52px)` | `0.9` | 400 | `0.01em` | uppercase |
| **CTA band headline** | Bebas Neue | `clamp(32px, 4.4vw, 56px)` | `0.95` | 400 | `0.03em` | uppercase |
| **Pull-quote** | Playfair Display | `clamp(21px, 2.2vw, 26px)` | `1.5` | 600 italic | `-0.01em` | sentence |

**Measure:** `--measure: 68ch` on the prose column. At 18px Inter that is roughly 673px
and roughly 68 to 72 characters, inside the 45 to 75 comfort band. NRG's article
container is a fixed `820px`, which at 18px is closer to **88 characters** and is
measurably too wide. Using `ch` rather than `px` means the measure stays correct if the
base size is ever retuned.

**Paragraph spacing:** `margin: 0 0 22px` (about `1.22em` at 18px). Not `16px` like NRG,
which is too tight against a 1.75 line-height and makes paragraphs blur together.

**H2 spacing inside the article:** `margin: 72px 0 20px`. NRG uses `48px 0 20px`. On a
10,000-word page the extra 24px of air above each H2 is what makes 18 sections feel like
18 chapters instead of one scroll.

### 2.3 Bebas Neue at long-form H2 size: the verdict

**Bebas Neue is the wrong face for the 18 section headings. Keep it, demote it.**

Concrete reasons, not taste:

1. **It has no lowercase.** Bebas Neue ships caps only. Every H2 renders as full caps
   whatever you type. Our H2s are natural-language questions running 6 to 11 words
   ("What new construction is available in Southwest Las Vegas?"). All-caps strings past
   about four words destroy word-shape recognition and measurably slow reading. On a page
   whose entire strategy is "keep people reading for 25 minutes", that is a direct hit to
   the primary objective.
2. **It has exactly one weight (400).** With 18 H2s and a required H3 tier beneath them,
   a single-weight face gives no way to build hierarchy inside the display layer. You end
   up faking it with size alone, which flattens the outline.
3. **Its cap-only geometry mis-scales.** A 40px Bebas H2 has the optical mass of roughly
   28px sentence-case text but consumes the full 40px of cap height. Long questions wrap
   to two or three lines of solid condensed caps, producing the "picket fence" effect and
   reading as a visual wall exactly where we are trying to create a break.
4. **Question marks look shouty in caps.** Fourteen of our H2s end in `?`. All-caps
   questions read as demands.

**Where Bebas Neue stays, because it is genuinely strong there and it is Ryan's signature:**

- **The H1.** One instance, short, huge. This is Bebas's best case and it is the first
  thing a visitor sees, so the brand signature lands immediately.
- **Stat numerals.** The stat bar, builder-card price ranges, the "20 builders / 5 tables"
  counters. Condensed caps numerals are excellent here.
- **CTA band headlines.** Short (4 to 7 words), high-impact, on navy. Bebas excels.
- **Section numerals** (`01` through `18`) in the eyebrow.

Net effect: Bebas Neue still appears roughly 25 to 30 times across the page and owns every
loud moment. It simply stops being asked to do a job it was never drawn for.

### 2.4 Base typography CSS

```css
html{
  font-size: 16px;
  scroll-behavior: smooth;
  scroll-padding-top: var(--anchor-off);
}
@media (prefers-reduced-motion: reduce){ html{ scroll-behavior: auto; } }

body{
  margin: 0 !important; padding: 0 !important;
  background: var(--dark);
  color: var(--text-body);
  font-family: var(--font-body);
  font-size: 18px; line-height: 1.75; font-weight: 400;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
  font-variant-numeric: proportional-nums;
}

h1,h2,h3,h4{ color: var(--text-dark); margin: 0; text-wrap: balance; }

h1{
  font-family: var(--font-display);
  font-size: clamp(52px, 9vw, 96px);
  line-height: .92; font-weight: 400;
  letter-spacing: .02em; text-transform: uppercase;
}

.rh-prose h2{
  font-family: var(--font-head);
  font-size: clamp(28px, 3.4vw, 40px);
  line-height: 1.18; font-weight: 600; letter-spacing: -.015em;
  margin: 72px 0 20px;
  scroll-margin-top: var(--anchor-off);
}
.rh-prose > h2:first-child{ margin-top: 0; }

.rh-prose h3{
  font-family: var(--font-body);
  font-size: clamp(19px, 1.5vw, 22px);
  line-height: 1.35; font-weight: 700; letter-spacing: -.01em;
  margin: 40px 0 12px;
  scroll-margin-top: var(--anchor-off);
}

.rh-prose p{ margin: 0 0 22px; max-width: var(--measure); }
.rh-prose > p:last-child{ margin-bottom: 0; }

.rh-lede{
  font-size: 20px; line-height: 1.68; letter-spacing: -.003em;
  color: var(--text-dark);
  max-width: var(--measure);
  margin: 0 0 26px;
}

.rh-prose ul, .rh-prose ol{
  max-width: var(--measure);
  margin: 0 0 22px; padding-left: 22px;
}
.rh-prose li{ margin-bottom: 10px; padding-left: 4px; }
.rh-prose li::marker{ color: var(--accent-ink); }

.rh-prose strong{ font-weight: 600; color: var(--text-dark); }

/* In-copy links: navy text (14.79:1) with a gold underline.
   Deliberately NOT gold text like NRG — high contrast body, gold only as the signal. */
.rh-prose a{
  color: var(--navy);
  text-decoration: underline;
  text-decoration-color: var(--accent);
  text-decoration-thickness: 1.5px;
  text-underline-offset: 3px;
  transition: color var(--t), text-decoration-color var(--t);
}
.rh-prose a:hover{ color: var(--accent-ink); text-decoration-color: var(--accent-ink); }
.rh-prose a:active{ color: var(--navy-light); }

.rh-small  { font-size: 14px;   line-height: 1.6;  color: var(--text-meta); }
.rh-caption{ font-size: 12.5px; line-height: 1.55; color: var(--text-meta);
             font-style: italic; letter-spacing: .01em; }
```

---

## 3. The sticky TOC rail

### 3.1 Decision: `position: sticky` inside a grid column, NOT `position: fixed`

NRG uses `position: fixed` plus a `body:has(.nc-table)` feature guard plus a
`max-width: calc(100vw - 320px)` gutter-reservation hack. **We are not copying that.**

First, a correction to `08-lofty-porting-constraints.md` §2b, which lists `position: fixed`
inside a Lofty embed as "the #1 technical unknown." **It is not unknown.**
`landing-page-template.md:100` states outright that the header "escapes via
`position: fixed`", and it ships that way on both Delamar and Sierra at Skyeview. Fixed
positioning demonstrably works inside a Lofty HTML embed. Ryan's wrapper-stripper also
force-sets `overflow: visible` on every ancestor, which is exactly the condition
`position: sticky` needs, so both options are technically viable.

**We choose sticky on architecture, and get the risk reduction for free:**

| | `position: fixed` (NRG) | `position: sticky` in a grid column (ours) |
|---|---|---|
| Gutter | Needs the `calc(100vw - 320px)` container hack, or copy slides under the rail | Grid reserves the column. Zero hacks. |
| Scoping | Floats over the entire page. Needs `:has()` or JS to hide it over the hero and FAQ. | Lives inside the article zone only. Appears and disappears naturally at the zone boundaries. |
| `:has()` dependency | Required | **Eliminated.** Removes doc 08 risk #2 entirely. |
| Failure mode | A 250px box glued mid-viewport overlapping body copy. Ugly and obvious. | Falls back to an ordinary in-flow card at the top of the article. Reads fine. |
| Scroll containment | Fine | Requires `overflow-x: clip` not `hidden` on `html, body` (§3.4) |

Sticky also gives something fixed cannot: the rail **stops** at the end of the article
instead of following you into the FAQ and the CTA band, which is the correct behavior for
an article outline and is a visible quality difference against the competitor.

### 3.2 HTML

```html
<!-- ARTICLE ZONE. Everything the TOC indexes lives inside .rh-article-shell. -->
<section class="rh-section rh-section--base" id="guide">
  <div class="rh-container">
    <div class="rh-article-shell">

      <!-- LEFT: the ~9,000-word prose column -->
      <div class="rh-prose">
        <h2 id="builders">Which builders are active in Las Vegas right now?</h2>
        <p>…</p>
        <!-- …18 anchored H2 blocks… -->
      </div>

      <!-- RIGHT: the rail -->
      <aside class="rh-rail">
        <nav class="rh-toc" aria-labelledby="rh-toc-title">
          <p class="rh-toc__title" id="rh-toc-title">On This Page</p>
          <div class="rh-toc__progress" aria-hidden="true">
            <span class="rh-toc__progress-fill"></span>
          </div>
          <ol class="rh-toc__list">
            <li><a href="#builders">Active builders</a></li>
            <li><a href="#why-new">Why new construction now</a></li>
            <li><a href="#summerlin">Summerlin</a></li>
            <li><a href="#henderson">Henderson</a></li>
            <li><a href="#lake-las-vegas">Lake Las Vegas</a></li>
            <li><a href="#sw-vegas">Southwest Las Vegas</a></li>
            <li><a href="#nlv">North Las Vegas</a></li>
            <li><a href="#nw-vegas">Northwest Las Vegas</a></li>
            <li><a href="#boulder-city">Boulder City</a></li>
            <li><a href="#launches">2026 launches</a></li>
            <li><a href="#builder-comparison">National vs regional</a></li>
            <li><a href="#price-by-area">Price by submarket</a></li>
            <li><a href="#new-vs-resale">New vs resale</a></li>
            <li><a href="#step-by-step">Buying step by step</a></li>
            <li><a href="#incentives">Builder incentives</a></li>
            <li><a href="#warranties">Warranties</a></li>
            <li><a href="#lot-premiums">Lot premiums</a></li>
            <li><a href="#faq">FAQ</a></li>
          </ol>
          <a class="rh-btn rh-btn--primary rh-btn--sm rh-toc__cta" href="#contact">
            Get the builder list
          </a>
        </nav>
      </aside>

    </div>
  </div>
</section>
```

TOC labels are the **short keyword form**, not the H2 text. That is NRG's pattern and it
is correct: it keeps the rail scannable and gives the H2s room to be full natural-language
questions for SEO.

### 3.3 CSS (production, paste as-is)

```css
/* ---------- shell ---------- */
.rh-container{ max-width: var(--container); margin: 0 auto; padding: 0 28px; width: 100%; }

.rh-article-shell{ display: block; }

@media (min-width: 1024px){
  .rh-article-shell{
    display: grid;
    grid-template-columns: minmax(0,1fr) var(--rail);
    gap: var(--rail-gap);
    align-items: start;
  }
}

.rh-prose{ min-width: 0; }
.rh-prose > *{ max-width: var(--measure); }
/* opt-out: tables, takeaway boxes, figures use the full column */
.rh-prose > .rh-wide{ max-width: none; }

/* ---------- rail: in-flow card (mobile / tablet default) ---------- */
.rh-rail{ margin: 0 0 44px; }

.rh-toc{
  background: var(--dark-surface);
  border: 1px solid var(--w08);
  border-left: 3px solid var(--accent);
  border-radius: var(--radius);
  padding: 22px 26px;
  box-shadow: var(--shadow-sm);
}

.rh-toc__title{
  margin: 0 0 14px;
  font-family: var(--font-body);
  font-size: 11px; font-weight: 700;
  letter-spacing: .22em; text-transform: uppercase;
  color: var(--accent-ink);
}

.rh-toc__progress{ display: none; }

.rh-toc__list{
  columns: 2; column-gap: 30px;
  margin: 0; padding-left: 20px;
  list-style: decimal;
}
.rh-toc__list li{ break-inside: avoid; margin-bottom: 8px; }
.rh-toc__list li::marker{ color: var(--w20); font-size: 12px; }

.rh-toc__list a{
  display: block;
  color: var(--navy);
  font-size: 14px; line-height: 1.5; font-weight: 400;
  text-decoration: none;
  border-radius: var(--radius-sm);
  transition: color var(--t), transform var(--t);
}
.rh-toc__list a:hover{ color: var(--accent-ink); transform: translateX(2px); }
.rh-toc__list a:active{ color: var(--navy-light); }
.rh-toc__list a:focus-visible{
  outline: 2px solid var(--navy);
  outline-offset: 3px;
}

.rh-toc__cta{ display: none; }

@media (max-width: 700px){
  .rh-toc__list{ columns: 1; }
}

/* ---------- rail: promoted to a sticky column at >=1024px ---------- */
@media (min-width: 1024px){
  .rh-rail{
    position: -webkit-sticky;
    position: sticky;
    top: var(--anchor-off);
    margin: 0;
    max-height: calc(100vh - var(--anchor-off) - 32px);
    overflow-y: auto;
    overscroll-behavior: contain;
    scrollbar-width: thin;
    scrollbar-color: var(--w20) transparent;
    z-index: 5;
  }
  .rh-rail::-webkit-scrollbar{ width: 6px; }
  .rh-rail::-webkit-scrollbar-thumb{ background: var(--w20); border-radius: 999px; }
  .rh-rail::-webkit-scrollbar-track{ background: transparent; }

  .rh-toc{
    padding: 20px 20px 20px 22px;
    box-shadow: var(--shadow-rail);
  }

  /* reading-progress hairline, desktop only */
  .rh-toc__progress{
    display: block;
    position: relative;
    height: 2px; width: 100%;
    background: var(--w08);
    border-radius: 999px;
    margin: 0 0 16px;
    overflow: hidden;
  }
  .rh-toc__progress-fill{
    position: absolute; inset: 0;
    background: var(--accent);
    transform-origin: left center;
    transform: scaleX(0);            /* JS writes scaleX only. Never width. */
    transition: transform var(--t-slow);
  }

  .rh-toc__list{
    columns: 1;
    padding-left: 0;
    list-style: none;
    counter-reset: toc;
  }
  .rh-toc__list li{
    counter-increment: toc;
    margin-bottom: 1px;
  }
  .rh-toc__list a{
    position: relative;
    padding: 6px 8px 6px 30px;
    font-size: 13px; line-height: 1.45;
    color: var(--text-meta);
  }
  .rh-toc__list a::before{
    content: counter(toc, decimal-leading-zero);
    position: absolute; left: 8px; top: 7px;
    font-size: 10px; font-weight: 600; letter-spacing: .04em;
    color: var(--w20);
    font-variant-numeric: tabular-nums;
    transition: color var(--t);
  }
  /* the active bar. transform-only, so it is cheap and reduced-motion safe. */
  .rh-toc__list a::after{
    content: '';
    position: absolute; left: 0; top: 4px; bottom: 4px;
    width: 2px; border-radius: 999px;
    background: var(--accent);
    transform: scaleY(0);
    transform-origin: center;
    transition: transform var(--t);
  }
  .rh-toc__list a:hover{ color: var(--text-dark); transform: none; }
  .rh-toc__list a:hover::before{ color: var(--accent-ink); }

  /* ACTIVE STATE — three redundant signals, never color alone (§7.3) */
  .rh-toc__list a[aria-current="true"]{
    color: var(--text-dark);
    font-weight: 600;
    background: var(--accent-muted);
  }
  .rh-toc__list a[aria-current="true"]::before{ color: var(--accent-ink); }
  .rh-toc__list a[aria-current="true"]::after{ transform: scaleY(1); }

  .rh-toc__cta{
    display: inline-flex;
    width: 100%;
    justify-content: center;
    margin-top: 18px;
  }
}

/* No sticky support (very old Safari): stays an in-flow card. Nothing breaks. */
@supports not (position: sticky){
  @media (min-width: 1024px){
    .rh-rail{ position: static; max-height: none; overflow: visible; }
  }
}
```

### 3.4 The one thing that will break sticky, and the fix

`landing-page-template.md` ships this reset:

```css
html, body { width: 100%; max-width: 100%; overflow-x: hidden; background: #faf8f3; }
```

**`overflow-x: hidden` on `html` or `body` computes `overflow-y` to `auto`.** That turns
the root into a scroll container that is not the viewport, and `position: sticky` silently
stops working in Chrome and Safari. This is the single most common cause of "my sticky
element does nothing."

**Required change** (this is why NRG's own body rule is `overflow-x: clip`, per
`06-conversion-and-tech.md` §2.d):

```css
html, body{
  width: 100%; max-width: 100%;
  overflow-x: hidden;          /* fallback for Safari < 16 */
  background: #faf8f3;
}
@supports (overflow-x: clip){
  html, body{ overflow-x: clip; }   /* clip does NOT create a scroll container */
}
body{ margin: 0 !important; padding: 0 !important; }
```

**Also required:** the wrapper-stripper already sets `overflow: visible !important` on
every ancestor. **Do not weaken that line.** It is now load-bearing for the rail, not just
for full-bleed.

**Also:** no ancestor of `.rh-rail` may have `transform`, `filter`, `perspective`,
`backdrop-filter`, `will-change`, or `contain: paint`. Any of those create a containing
block and break sticky. In practice that means: do not put a scroll-reveal transform on
`.rh-article-shell` or `.rh-section`. Put reveals on `.rh-prose > *` instead.

### 3.5 Anchor offset

```css
html{ scroll-padding-top: var(--anchor-off); }   /* 84px = 60px header + 24px air */
.rh-prose h2, .rh-prose h3, [id]{ scroll-margin-top: var(--anchor-off); }
```

Pure CSS, no JS scroll handler, same as the competitor.

### 3.6 Scroll-spy: yes, add it. Here is why and here is the code.

NRG ships **zero** scroll-spy (confirmed in `01-hub-page-teardown.md` §2.3: no active-link
JS, no `aria-current`, no `.is-active` rule anywhere in three stylesheets). That is a gap,
not a design decision, and it is a cheap win.

**Justification:**
- On an 18-section, 25-minute page, a static TOC answers "what is here" but never "where
  am I". Positional feedback is a documented retention device on long reads, and retention
  is the stated objective for this page.
- Cost is roughly 40 lines of vanilla `IntersectionObserver`. No dependency, no layout
  thrash, no scroll listener.
- The page already ships JS (the wrapper-stripper, the reveal observer), so this adds no
  new category of risk.
- It degrades perfectly. If the script fails, the TOC is still a working jump-link list.
- It also drives the reading-progress hairline, which is a second retention cue for free.

**Rules:** the JS only ever writes `aria-current` and a `transform`. It never writes
`width`, `height`, `top`, or any layout property.

```html
<script>
(function(){
  'use strict';
  var toc = document.querySelector('.rh-toc');
  if (!toc || !('IntersectionObserver' in window)) return;

  var links = Array.prototype.slice.call(toc.querySelectorAll('.rh-toc__list a'));
  var rail  = document.querySelector('.rh-rail');
  var fill  = toc.querySelector('.rh-toc__progress-fill');
  var prose = document.querySelector('.rh-prose');
  if (!links.length || !prose) return;

  var map = {};                      // id -> link
  var targets = [];
  links.forEach(function(a){
    var id = (a.getAttribute('href') || '').slice(1);
    var el = id && document.getElementById(id);
    if (el){ map[id] = a; targets.push(el); }
  });
  if (!targets.length) return;

  var visible = new Set();
  var currentId = null;

  function setActive(id){
    if (id === currentId) return;
    currentId = id;
    links.forEach(function(a){ a.removeAttribute('aria-current'); });
    var a = map[id];
    if (!a) return;
    a.setAttribute('aria-current', 'true');

    // keep the active item inside the rail's own scrollport.
    // set scrollTop directly — scrollIntoView() would also scroll the page.
    if (rail && rail.scrollHeight > rail.clientHeight){
      var top = a.offsetTop, bottom = top + a.offsetHeight;
      if (top < rail.scrollTop) rail.scrollTop = top - 8;
      else if (bottom > rail.scrollTop + rail.clientHeight) {
        rail.scrollTop = bottom - rail.clientHeight + 8;
      }
    }
  }

  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if (e.isIntersecting) visible.add(e.target.id);
      else visible.delete(e.target.id);
    });
    // pick the first visible heading in document order; otherwise keep the last one
    for (var i = 0; i < targets.length; i++){
      if (visible.has(targets[i].id)){ setActive(targets[i].id); return; }
    }
  }, {
    // activation band = the top ~35% of the viewport, below the fixed header
    rootMargin: '-' + (60 + 28) + 'px 0px -65% 0px',
    threshold: 0
  });
  targets.forEach(function(t){ io.observe(t); });

  // reading progress across the article zone. transform only.
  if (fill){
    var ticking = false;
    function progress(){
      ticking = false;
      var r = prose.getBoundingClientRect();
      var total = r.height - window.innerHeight;
      var p = total <= 0 ? 1 : (-r.top) / total;
      fill.style.transform = 'scaleX(' + Math.min(1, Math.max(0, p)) + ')';
    }
    window.addEventListener('scroll', function(){
      if (!ticking){ ticking = true; requestAnimationFrame(progress); }
    }, { passive: true });
    window.addEventListener('resize', progress, { passive: true });
    progress();
  }
})();
</script>
```

---

## 4. Component specs

### 4.1 Builder card (20-up grid, per-builder accent stripe)

Design intent: NRG uses 20 logo SVGs. We do not have those files and sourcing 20 licensed
logos is a project of its own. Instead each card carries the builder's **real verified
brand color** as a top stripe plus a tinted monogram chip. This is more distinctive than a
row of grayscale logos, needs zero assets, and satisfies the "per-builder accent stripe"
requirement using `builder-brand-colors.md` directly.

```html
<ul class="rh-builder-grid" role="list">
  <li>
    <a class="rh-builder-card" href="/lennar-las-vegas" style="--b:#005DAA;">
      <span class="rh-builder-card__stripe" aria-hidden="true"></span>
      <span class="rh-builder-card__mono" aria-hidden="true">LEN</span>
      <h3 class="rh-builder-card__name">Lennar</h3>
      <p class="rh-builder-card__parent">Lennar Corporation (NYSE: LEN)</p>
      <ul class="rh-builder-card__stats" role="list">
        <li>$277K to $1.3M</li><li>50 communities</li><li>20+ years</li>
      </ul>
      <p class="rh-builder-card__note">Everything's Included pricing. Strongest presence
        in Henderson, Lake Las Vegas, and the southwest valley.</p>
      <ul class="rh-builder-card__areas" role="list">
        <li>Henderson</li><li>Lake Las Vegas</li><li>Southwest</li><li>North LV</li>
      </ul>
      <span class="rh-builder-card__go">View builder page</span>
    </a>
  </li>
  <!-- x20 -->
</ul>
```

```css
.rh-builder-grid{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(272px, 1fr));
  gap: 16px;
  list-style: none; margin: 0; padding: 0;
}

.rh-builder-card{
  --b: var(--navy);                      /* fallback if a card omits --b */
  position: relative;
  display: block;
  overflow: hidden;
  padding: 24px 22px 20px;
  background: var(--dark-card);
  border: 1px solid var(--w08);
  border-radius: var(--radius);
  box-shadow: var(--shadow-card);
  text-decoration: none;
  color: inherit;
  /* explicit properties only. never transition-all. */
  transition: transform var(--t), box-shadow var(--t), border-color var(--t);
}

.rh-builder-card__stripe{
  position: absolute; inset: 0 0 auto 0;
  height: 4px;
  background: var(--b);
}

.rh-builder-card__mono{
  display: inline-flex; align-items: center; justify-content: center;
  min-width: 46px; height: 30px; padding: 0 10px;
  margin-bottom: 14px;
  border-radius: var(--radius-sm);
  /* brand color as a tint only. text stays navy so every builder is readable. */
  background: color-mix(in srgb, var(--b) 14%, transparent);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--b) 30%, transparent);
  color: var(--navy);
  font-family: var(--font-body);
  font-size: 11px; font-weight: 700; letter-spacing: .12em;
}
@supports not (background: color-mix(in srgb, red 10%, transparent)){
  .rh-builder-card__mono{ background: var(--w04); box-shadow: inset 0 0 0 1px var(--w08); }
}

.rh-builder-card__name{
  font-family: var(--font-head);
  font-size: 21px; line-height: 1.2; font-weight: 600; letter-spacing: -.01em;
  color: var(--text-dark); margin: 0 0 3px;
}
.rh-builder-card__parent{
  font-size: 12px; line-height: 1.4; color: var(--text-meta); margin: 0 0 14px;
}

.rh-builder-card__stats{
  display: flex; flex-wrap: wrap; gap: 6px;
  list-style: none; margin: 0 0 14px; padding: 0;
}
.rh-builder-card__stats li{
  padding: 4px 11px;
  background: var(--dark-surface);
  border-radius: var(--radius-pill);
  font-family: var(--font-body);
  font-size: 12px; font-weight: 500; color: var(--text-body);
  font-variant-numeric: tabular-nums;
}

.rh-builder-card__note{
  font-size: 14px; line-height: 1.6; color: var(--text-body); margin: 0 0 14px;
}

.rh-builder-card__areas{
  display: flex; flex-wrap: wrap; gap: 5px;
  list-style: none; margin: 0 0 16px; padding: 0;
}
.rh-builder-card__areas li{
  padding: 3px 9px;
  border: 1px solid var(--w08);
  border-radius: var(--radius-pill);
  font-size: 11px; font-weight: 500; color: var(--text-meta);
}

.rh-builder-card__go{
  display: inline-flex; align-items: center; gap: 6px;
  font-size: 13px; font-weight: 600;
  color: var(--accent-ink);
}
.rh-builder-card__go::after{
  content: '\2192';
  transition: transform var(--t);
}

/* states — every interactive element gets all three (§8) */
.rh-builder-card:hover{
  transform: translateY(-3px);
  box-shadow: var(--shadow-lift);
  border-color: var(--accent-line);
}
.rh-builder-card:hover .rh-builder-card__go::after{ transform: translateX(4px); }
.rh-builder-card:focus-visible{
  outline: 2px solid var(--navy);
  outline-offset: 3px;
  box-shadow: var(--shadow-lift);
}
.rh-builder-card:active{ transform: translateY(-1px); box-shadow: var(--shadow-card); }

@media (prefers-reduced-motion: reduce){
  .rh-builder-card,
  .rh-builder-card__go::after{ transition: none; }
  .rh-builder-card:hover{ transform: none; }
}
```

**Grid behavior:** `auto-fill minmax(272px, 1fr)` yields 1 column below 600px, 2 at
600 to 900px, 3 at 900 to 1280px, 4 above 1280px. The builder grid lives **outside** the
article shell (full container width), so the rail never squeezes it.

### 4.2 Data table (5 tables, readable and mobile-scrollable)

```html
<figure class="rh-table-fig rh-wide">
  <div class="rh-table-wrap" tabindex="0" role="region"
       aria-label="Las Vegas new construction pricing by submarket">
    <table class="rh-table">
      <caption>Las Vegas new construction pricing by submarket, entry, mid, and luxury tiers.</caption>
      <thead>
        <tr><th scope="col">Submarket</th><th scope="col">Entry</th>
            <th scope="col">Mid-range</th><th scope="col">Luxury</th>
            <th scope="col">Most active builders</th></tr>
      </thead>
      <tbody>
        <tr><th scope="row">Summerlin</th><td>…</td><td>…</td><td>…</td><td>…</td></tr>
      </tbody>
    </table>
  </div>
  <figcaption class="rh-caption">Verify current pricing with the builder sales office.
    Ranges move monthly.</figcaption>
</figure>
```

```css
.rh-table-fig{ margin: 40px 0 40px; }

.rh-table-wrap{
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  border: 1px solid var(--w08);
  border-radius: var(--radius);
  box-shadow: var(--shadow-card);
  /* scroll-edge shadows: the right shadow fades out when you reach the end */
  background:
    linear-gradient(to right, var(--dark-card) 30%, rgba(255,255,255,0)) left center / 28px 100% no-repeat,
    linear-gradient(to left,  var(--dark-card) 30%, rgba(255,255,255,0)) right center / 28px 100% no-repeat,
    radial-gradient(farthest-side at 0 50%, rgba(28,35,51,.14), rgba(28,35,51,0)) left center / 14px 100% no-repeat,
    radial-gradient(farthest-side at 100% 50%, rgba(28,35,51,.14), rgba(28,35,51,0)) right center / 14px 100% no-repeat,
    var(--dark-card);
  background-attachment: local, local, scroll, scroll, local;
}
.rh-table-wrap:focus-visible{ outline: 2px solid var(--navy); outline-offset: 2px; }

.rh-table{
  width: 100%;
  min-width: 660px;              /* forces a real scroll instead of squeezing to 8px type */
  border-collapse: collapse;
  font-family: var(--font-body);
  font-size: 15px; line-height: 1.5;
  font-variant-numeric: tabular-nums;
}

.rh-table caption{
  caption-side: top;
  padding: 14px 18px 12px;
  text-align: left;
  font-size: 12.5px; line-height: 1.55; font-style: italic;
  color: var(--text-meta);
  border-bottom: 1px solid var(--w08);
}

.rh-table thead th{
  position: sticky; top: 0; z-index: 2;
  background: var(--navy);
  color: var(--dark);
  font-size: 12px; font-weight: 600;
  letter-spacing: .08em; text-transform: uppercase;
  text-align: left;
  padding: 13px 16px;
  white-space: nowrap;
}
.rh-table thead th:first-child{ border-top-left-radius: 0; }

.rh-table td,
.rh-table tbody th{
  padding: 13px 16px;
  border-bottom: 1px solid var(--w08);
  color: var(--text-body);
  vertical-align: top;
}
.rh-table tbody th{
  text-align: left; font-weight: 600; color: var(--text-dark);
  white-space: nowrap;
}
.rh-table tbody tr:last-child td,
.rh-table tbody tr:last-child th{ border-bottom: 0; }

/* zebra uses the gold tint, not gray — ties the tables to the palette */
.rh-table tbody tr:nth-child(even){ background: var(--accent-tint); }
.rh-table tbody tr:hover{ background: var(--accent-muted); }

/* row-header column freezes on narrow screens so you never lose your place */
@media (max-width: 900px){
  .rh-table tbody th{
    position: sticky; left: 0; z-index: 1;
    background: var(--dark-card);
    box-shadow: 1px 0 0 var(--w08);
  }
  .rh-table tbody tr:nth-child(even) th{ background: #f8f4ec; }
  .rh-table thead th:first-child{ position: sticky; left: 0; z-index: 3; background: var(--navy); }
}

/* swipe affordance, touch only */
.rh-table-hint{ display: none; }
@media (hover: none) and (max-width: 900px){
  .rh-table-hint{
    display: block;
    margin: 8px 0 0;
    font-size: 12px; color: var(--text-meta);
  }
}
```

Note `caption` is kept and **visible**. `01-hub-page-teardown.md` §5 flags it as an
"SEO/a11y win worth copying" and it doubles as the section's data-source line.

### 4.3 FAQ block (always open, not an accordion)

Matching the competitor's choice deliberately. All answers in the initial DOM, mirrored
1:1 into `FAQPage` JSON-LD. No `<details>`, no toggle JS, nothing hidden from a crawler
or a screen reader.

```html
<div class="rh-faq">
  <div class="rh-faq__item">
    <h3 class="rh-faq__q">Do I need my own agent to buy new construction in Las Vegas?</h3>
    <p class="rh-faq__a">…50 to 70 words…</p>
  </div>
  <!-- x12 -->
</div>
```

```css
.rh-faq{ max-width: 780px; margin: 0 auto; }

.rh-faq__item{
  padding: 26px 0 26px 22px;
  border-bottom: 1px solid var(--w08);
  border-left: 2px solid transparent;
  transition: border-color var(--t);
}
.rh-faq__item:first-child{ padding-top: 0; }
.rh-faq__item:last-child{ border-bottom: 0; }
.rh-faq__item:hover{ border-left-color: var(--accent); }

.rh-faq__q{
  font-family: var(--font-body);
  font-size: 19px; line-height: 1.4; font-weight: 700; letter-spacing: -.01em;
  color: var(--text-dark);
  margin: 0 0 10px;
  scroll-margin-top: var(--anchor-off);
}
.rh-faq__a{
  font-size: 16.5px; line-height: 1.75;
  color: var(--text-body);
  margin: 0; max-width: 66ch;
}
.rh-faq__a a{ color: var(--navy); text-decoration: underline;
  text-decoration-color: var(--accent); text-underline-offset: 3px; }
```

FAQ answers step down to 16.5px from the 18px body. Twelve short blocks read better a
touch tighter, and it visually separates the FAQ from the article.

### 4.4 Section label / eyebrow

Ryan's flex-plus-rule pattern is kept, retuned for a long page: numbered, so it doubles as
a progress cue.

```html
<p class="rh-eyebrow"><span class="rh-eyebrow__num">07</span>Submarket guide</p>
```

```css
.rh-eyebrow{
  display: flex; align-items: center; gap: 12px;
  margin: 0 0 16px;
  font-family: var(--font-body);
  font-size: 11px; font-weight: 700;
  letter-spacing: .22em; text-transform: uppercase;
  color: var(--accent-ink);
}
.rh-eyebrow::after{
  content: ''; flex: 1; max-width: 56px; height: 1px;
  background: var(--accent);
}
.rh-eyebrow__num{
  font-family: var(--font-display);
  font-size: 15px; letter-spacing: .06em; line-height: 1;
  color: var(--w20);
  font-variant-numeric: tabular-nums;
}
/* on navy bands */
.rh-band .rh-eyebrow{ color: var(--accent); }
.rh-band .rh-eyebrow::after{ background: var(--accent-line); }
.rh-band .rh-eyebrow__num{ color: var(--navy-on-faint); }
```

### 4.5 Key-takeaway box and pull-quote

Two distinct devices. Do not merge them.

```html
<aside class="rh-takeaway rh-wide" aria-label="Key takeaways">
  <p class="rh-takeaway__title">The short version</p>
  <ul>
    <li>…</li>
  </ul>
</aside>

<blockquote class="rh-quote">
  <p>Builder pricing does not change whether or not you bring your own agent.</p>
  <cite>Ryan Rose, Real Broker LLC</cite>
</blockquote>
```

```css
.rh-takeaway{
  margin: 36px 0;
  padding: 26px 28px 22px;
  background: var(--accent-muted);
  border-left: 3px solid var(--accent);
  border-radius: 0 var(--radius) var(--radius) 0;
}
.rh-takeaway__title{
  margin: 0 0 14px;
  font-family: var(--font-body);
  font-size: 11px; font-weight: 700;
  letter-spacing: .22em; text-transform: uppercase;
  color: var(--accent-ink);
}
.rh-takeaway ul{ list-style: none; margin: 0; padding: 0; max-width: none; }
.rh-takeaway li{
  position: relative;
  padding-left: 22px; margin-bottom: 11px;
  font-size: 16.5px; line-height: 1.65; color: var(--text-body);
}
.rh-takeaway li:last-child{ margin-bottom: 0; }
.rh-takeaway li::before{
  content: '\203A';                       /* the > glyph, matching NRG's marker idea */
  position: absolute; left: 4px; top: -1px;
  color: var(--accent-ink); font-weight: 700; font-size: 17px;
}

.rh-quote{
  margin: 44px 0;
  padding: 4px 0 4px 26px;
  border-left: 3px solid var(--accent);
  max-width: 60ch;
}
.rh-quote p{
  font-family: var(--font-head);
  font-size: clamp(21px, 2.2vw, 26px);
  line-height: 1.5; font-weight: 600; font-style: italic; letter-spacing: -.01em;
  color: var(--text-dark);
  margin: 0 0 12px; max-width: none;
}
.rh-quote cite{
  font-family: var(--font-body);
  font-size: 12px; font-style: normal; font-weight: 600;
  letter-spacing: .14em; text-transform: uppercase;
  color: var(--text-meta);
}
```

### 4.6 Buttons and the CTA band

```css
/* ---------- buttons ---------- */
.rh-btn{
  display: inline-flex; align-items: center; justify-content: center; gap: 9px;
  min-height: 48px;                      /* >44px touch target */
  padding: 14px 30px;
  border: 1px solid transparent;
  border-radius: var(--radius-pill);     /* pill — the anti-NRG geometry signal */
  font-family: var(--font-body);
  font-size: 14px; font-weight: 600;
  letter-spacing: .04em; text-transform: uppercase;
  text-decoration: none; cursor: pointer;
  transition: transform var(--t), box-shadow var(--t),
              background-color var(--t), border-color var(--t), color var(--t);
}
.rh-btn--sm{ min-height: 40px; padding: 10px 20px; font-size: 12.5px; }

/* PRIMARY — navy fill, cream text (14.79:1), gold hairline.
   NOT gold fill with white text: that measures 2.26:1 and fails AA. See §1.4. */
.rh-btn--primary{
  background: var(--navy);
  color: var(--dark);
  border-color: var(--accent);
  box-shadow: var(--shadow-card);
}
.rh-btn--primary:hover{
  background: var(--navy-light);
  border-color: var(--accent-hover);
  transform: translateY(-2px);
  box-shadow: var(--shadow-lift);
}
.rh-btn--primary:active{ transform: translateY(0); box-shadow: var(--shadow-sm); }
.rh-btn--primary:focus-visible{
  outline: 2px solid var(--navy); outline-offset: 3px;
}

/* SECONDARY — gold ink on cream (5.28:1) */
.rh-btn--secondary{
  background: transparent;
  color: var(--accent-ink);
  border: 1.5px solid var(--accent);
}
.rh-btn--secondary:hover{
  background: var(--accent-muted);
  border-color: var(--accent-hover);
  transform: translateY(-2px);
}
.rh-btn--secondary:active{ transform: translateY(0); background: var(--accent-tint); }
.rh-btn--secondary:focus-visible{ outline: 2px solid var(--navy); outline-offset: 3px; }

/* ON-NAVY — gold fill is correct here. Gold on navy = 6.96:1. */
.rh-band .rh-btn--primary{
  background: var(--accent);
  color: var(--navy);
  border-color: var(--accent);
}
.rh-band .rh-btn--primary:hover{ background: var(--accent-hover); }
.rh-band .rh-btn--primary:focus-visible{ outline: 2px solid var(--accent); outline-offset: 3px; }
.rh-band .rh-btn--secondary{ color: var(--dark); border-color: var(--accent-line); }
.rh-band .rh-btn--secondary:hover{ background: rgba(201,168,110,.14); border-color: var(--accent); }

@media (prefers-reduced-motion: reduce){
  .rh-btn{ transition: background-color var(--t), border-color var(--t), color var(--t); }
  .rh-btn:hover{ transform: none; }
}

/* ---------- CTA band ---------- */
.rh-band{
  background: var(--navy);
  color: var(--navy-on);
  padding: 68px 28px;
  position: relative; overflow: hidden;
  box-shadow: var(--shadow-band);
}
/* layered radial depth + SVG grain, per the anti-generic rules */
.rh-band::before{
  content: ''; position: absolute; inset: 0; pointer-events: none;
  background:
    radial-gradient(120% 90% at 12% 0%,  rgba(42,51,80,.85) 0%, rgba(28,35,51,0) 58%),
    radial-gradient(90% 70% at 100% 100%, rgba(201,168,110,.13) 0%, rgba(28,35,51,0) 62%);
}
.rh-band::after{
  content: ''; position: absolute; inset: 0; pointer-events: none; opacity: .05;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='140' height='140' filter='url(%23n)'/%3E%3C/svg%3E");
}
.rh-band > *{ position: relative; z-index: 1; }

.rh-band__title{
  font-family: var(--font-display);
  font-size: clamp(32px, 4.4vw, 56px);
  line-height: .95; font-weight: 400;
  letter-spacing: .03em; text-transform: uppercase;
  color: var(--dark);
  margin: 0 0 14px; max-width: 18ch;
}
.rh-band__sub{
  font-size: 17px; line-height: 1.7; color: var(--navy-on);
  margin: 0 0 26px; max-width: 56ch;
}
.rh-band__actions{ display: flex; flex-wrap: wrap; gap: 12px; }
```

**Important:** `.rh-band` may **not** be an ancestor of `.rh-rail`. It is a full-bleed
interruptor between article blocks, never a wrapper, because `overflow: hidden` on it
would kill the rail's sticky.

### 4.7 Stat bar

```html
<div class="rh-stats">
  <div class="rh-stat"><span class="rh-stat__n">20</span><span class="rh-stat__l">Active builders</span></div>
  <div class="rh-stat"><span class="rh-stat__n">70+</span><span class="rh-stat__l">Communities</span></div>
  <div class="rh-stat"><span class="rh-stat__n">$290K</span><span class="rh-stat__l">Entry pricing</span></div>
  <div class="rh-stat"><span class="rh-stat__n">22</span><span class="rh-stat__l">Minute read</span></div>
</div>
```

```css
.rh-stats{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1px;
  background: var(--w08);
  border: 1px solid var(--w08);
  border-radius: var(--radius);
  overflow: hidden;
}
.rh-stat{ background: var(--dark-card); padding: 22px 20px; text-align: left; }
.rh-stat__n{
  display: block;
  font-family: var(--font-display);
  font-size: clamp(34px, 4vw, 52px);
  line-height: .9; letter-spacing: .01em;
  color: var(--text-dark);
  font-variant-numeric: tabular-nums;
}
.rh-stat__l{
  display: block; margin-top: 8px;
  font-size: 11px; font-weight: 600;
  letter-spacing: .16em; text-transform: uppercase;
  color: var(--text-meta);
}
/* on navy */
.rh-band .rh-stats{ background: rgba(216,220,232,.16); border-color: rgba(216,220,232,.16); }
.rh-band .rh-stat{ background: var(--navy); }
.rh-band .rh-stat__n{ color: var(--accent); }
.rh-band .rh-stat__l{ color: var(--navy-on-faint); }
```

### 4.8 Live-listings slot (Lofty IDX)

Per `08-lofty-porting-constraints.md` §2, the Lofty IDX snippet is still an open item with
Ryan. Build the slot so **either** outcome drops in without a redesign.

Target geometry, matched to the competitor so the visual weight is equivalent:
4:3 image well, 8px radius, 12px gap, 1 / 2 / 3 / 4 columns at 500 / 800 / 1700px.

```html
<section class="rh-section rh-section--surface" id="live">
  <div class="rh-container">
    <header class="rh-idx__header">
      <p class="rh-eyebrow"><span class="rh-eyebrow__num">02</span>Live MLS feed</p>
      <h2 class="rh-idx__title">New construction for sale in Las Vegas right now</h2>
      <p class="rh-lede">…</p>
      <p class="rh-small">…methodology sentence…</p>
    </header>

    <!-- Lofty IDX embed goes here, untouched. -->
    <div class="rh-idx-slot" data-idx-slot>
      <!-- pre-IDX placeholder: 6 skeleton cards, identical geometry, remove on wire-up -->
      <div class="rh-idx-skel" aria-hidden="true"></div>
      <div class="rh-idx-skel" aria-hidden="true"></div>
      <div class="rh-idx-skel" aria-hidden="true"></div>
      <div class="rh-idx-skel" aria-hidden="true"></div>
      <div class="rh-idx-skel" aria-hidden="true"></div>
      <div class="rh-idx-skel" aria-hidden="true"></div>
    </div>

    <p class="rh-small rh-idx__attrib">Listing data from the GLVAR MLS. Builder,
      spec versus model status, and current incentives vary. Confirm with the builder
      sales office before you tour. Information deemed reliable but not guaranteed.</p>
  </div>
</section>
```

```css
.rh-idx__header{ max-width: 76ch; margin: 0 0 30px; }
.rh-idx__title{
  font-family: var(--font-head);
  font-size: clamp(28px, 3.4vw, 40px);
  line-height: 1.18; font-weight: 600; letter-spacing: -.015em;
  margin: 0 0 14px;
}

.rh-idx-slot{
  display: grid;
  grid-template-columns: minmax(0,1fr);
  gap: 12px;
  min-height: 420px;                 /* reserves space, kills the CLS jump on embed load */
}
@media (min-width: 500px) { .rh-idx-slot{ grid-template-columns: repeat(2, minmax(0,1fr)); } }
@media (min-width: 800px) { .rh-idx-slot{ grid-template-columns: repeat(3, minmax(0,1fr)); } }
@media (min-width: 1700px){ .rh-idx-slot{ grid-template-columns: repeat(4, minmax(0,1fr)); } }

/* Defensive, LOW-specificity styling of whatever Lofty injects.
   Do not fight the embed's internals. Nudge only the outer box. */
.rh-idx-slot > *{ min-width: 0; border-radius: 8px; }
.rh-idx-slot iframe{ width: 100%; border: 0; display: block; }

/* skeleton, remove when the real embed is wired */
.rh-idx-skel{
  aspect-ratio: 4/3;
  background:
    linear-gradient(var(--dark-surface), var(--dark-surface)) top / 100% 66% no-repeat,
    var(--dark-card);
  border: 1px solid var(--w08);
  border-radius: 8px;
  box-shadow: var(--shadow-card);
}

.rh-idx__attrib{ margin-top: 22px; max-width: 78ch; }
```

**Fallback path** (if Lofty IDX will not render inside an HTML embed): swap
`.rh-idx-slot` contents for 6 static "featured community" cards reusing
`.rh-builder-card` styling, plus a full-width `.rh-btn--primary` linking to a
pre-filtered Lofty search URL. The grid, spacing, header, and attribution all stay,
so nothing above or below has to change.

### 4.9 Section shells

```css
.rh-section{ padding: 84px 28px; }
.rh-section--base   { background: var(--dark); }
.rh-section--surface{ background: var(--dark-surface); }
.rh-section--tight  { padding: 52px 28px; }

/* hairline seam so adjacent same-color sections still read as separate */
.rh-section + .rh-section--base,
.rh-section + .rh-section--surface{ border-top: 1px solid var(--w08); }
```

---

## 5. Page rhythm and engagement

### 5.1 Three zones, and why the article zone does NOT alternate backgrounds

Ryan's template says sections alternate `--dark` / `--dark-surface`. **That rule holds
everywhere on this page except the article zone**, and here is why: alternating full-bleed
backgrounds behind a sticky rail means the rail card sits on a shifting background as you
scroll, which reads as a rendering bug. It also fights the "one long article" structure
that makes the TOC coherent (the competitor puts all 15 of its editorial H2s inside a
**single** `<section>` for exactly this reason).

| Zone | Sections | Background | Rail? | Rhythm comes from |
|---|---|---|---|---|
| **A. Entry** | hero, trust strip, live listings, direct answer, builder grid | Alternates `--dark` / `--dark-surface` per section | No | Full-bleed background flips |
| **B. Article** | the 18 anchored H2 blocks | **One continuous `--dark`** | Yes | Inline devices (below) + full-bleed interruptors |
| **C. Exit** | FAQ, CTA band, related reading, disclosure | Alternates again | No | Full-bleed background flips |

### 5.2 The device rotation for Zone B

**Hard rule: no more than roughly 350 words of unbroken prose.** At 18px/1.75 that is
about one and a half laptop screens, which is the practical attention floor on a page
this long. Every H2 block must contain at least one non-paragraph element.

Rotate these so no two consecutive sections use the same device:

| Device | Component | Frequency |
|---|---|---|
| Numbered eyebrow + Playfair H2 | §4.4 + §2.4 | Every section (18x) |
| Lede paragraph at 20px | `.rh-lede` | Every section |
| Key-takeaway box | §4.5 | About every 3rd section (6x) |
| Data table | §4.2 | 5x, per the content plan |
| Pull-quote | §4.5 | 4x, on the sections with a strong single claim |
| Figure with `figcaption` | image + `.rh-caption` | 5x, on the submarket sections |
| Inline stat trio | §4.7 | 3x |
| Full-bleed navy interruptor | §4.6 `.rh-band` | 3x, after roughly sections 6, 11, and 16 |
| Bolded lead-in sub-blocks inside `<p>` | plain `<strong>` | Every submarket section |

The bolded lead-in pattern is worth copying verbatim from the competitor
(`01-hub-page-teardown.md` §1, "Notable structural quirks"): sub-topics are `<strong>`
lead-ins inside paragraphs, not real headings. They give the eye a landing point every
80 to 120 words without adding 60 more entries to the heading outline or polluting the TOC.

### 5.3 CTA placement

Doc 08 §1 settles this: no inline form, all CTAs are `href="#contact"` scrolling to the
Lofty form below the embed. Placement, which preserves the competitor's "CTA roughly every
two sections" cadence without a form:

1. Hero: primary + secondary
2. End of the live-listings section: one secondary
3. End of the builder grid: one primary
4. Zone B navy interruptor #1 (after roughly section 6)
5. Zone B navy interruptor #2 (after roughly section 11)
6. Zone B navy interruptor #3 (after roughly section 16)
7. TOC rail CTA, desktop only, persistently visible (`.rh-toc__cta`)
8. End of FAQ: one primary
9. Closing CTA band above the Lofty form
10. Mobile sticky CTA bar, below 1024px (§6)

That is ten conversion surfaces with zero inline `<form>` elements.

### 5.4 Imagery cadence

Five images maximum in Zone B, all on submarket sections, all `loading="lazy"` except any
above the fold. Treatment per the anti-generic rules:

```css
.rh-figure{ margin: 36px 0; }
.rh-figure__frame{
  position: relative; overflow: hidden;
  border-radius: var(--radius);
  aspect-ratio: 16/9;
  box-shadow: var(--shadow-card);
}
.rh-figure__frame img{ width: 100%; height: 100%; object-fit: cover; display: block; }
.rh-figure__frame::after{
  content: ''; position: absolute; inset: 0; pointer-events: none;
  background:
    linear-gradient(to top, rgba(28,35,51,.42) 0%, rgba(28,35,51,0) 46%),
    linear-gradient(to bottom right, rgba(201,168,110,.10), rgba(28,35,51,.06));
  mix-blend-mode: multiply;
}
.rh-figure figcaption{ margin-top: 10px; }
```

The navy-plus-brass overlay is what stops stock builder photography from looking like
stock builder photography, and it ties every image to the palette.

### 5.5 Scroll reveal

Keep Ryan's IntersectionObserver reveal, but apply it to `.rh-prose > *` and card children,
**never** to `.rh-article-shell` or `.rh-section`, because a `transform` on a rail ancestor
kills sticky (§3.4).

```css
.rh-reveal{ opacity: 0; transform: translateY(16px);
            transition: opacity .55s ease, transform .55s ease; }
.rh-reveal.is-in{ opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce){
  .rh-reveal{ opacity: 1; transform: none; transition: none; }
}
```

---

## 6. Responsive breakpoints

Six steps. Deliberately fewer than the competitor's fifteen, which
`06-conversion-and-tech.md` §2.d itself flags as a maintainability warning.

| Breakpoint | What changes |
|---|---|
| **>= 1700px** | IDX slot goes to 4 columns. Nothing else. |
| **>= 1280px** | Builder grid settles at 4 columns. `--container` 1180px caps out and side gutters grow. |
| **>= 1024px** | **The big one.** Article shell becomes `1fr / 250px` grid. Rail becomes sticky, single-column, numbered, with progress bar, active states, and the rail CTA. Mobile sticky CTA bar hides. IDX 3-col. Section padding 84px. |
| **< 1024px** | Rail returns to document flow as a 2-column cream card above the prose. Mobile sticky CTA bar appears (mirrors the competitor's 1024px trade-off). |
| **<= 900px** | Tables get a sticky first column and the swipe hint. Builder grid 2-col. Section padding 64px. Hero H1 clamps down. |
| **<= 768px** | Section padding 52px 20px. Container padding 20px. H2 bottoms out near 28px. Stat bar 2-up. Body stays 18px (do **not** shrink long-form body on mobile). `.rh-band` padding 52px 20px. |
| **<= 560px** | TOC list 1 column (fires at 700px, restated). Builder grid 1-col. IDX 1-col. Buttons go full-width. `.rh-quote` padding-left 18px. |
| **<= 400px** | H1 clamp floor 44px. Table `min-width` stays 660px, so it scrolls, which is correct. Stat bar 1-up. |

**Explicit non-change:** body copy stays 18px at every width. Shrinking long-form body text
on mobile is the most common mistake on pages like this and it is where most of the read
happens.

```css
/* mobile sticky CTA bar — position:fixed is proven in Ryan's Lofty embeds
   (the template header uses it and ships). Below 1024px only. */
.rh-mobile-cta{
  display: none;
  position: fixed; left: 0; right: 0; bottom: 0; z-index: 100;
  grid-template-columns: 1fr 1fr 1.6fr;
  background: var(--navy);
  border-top: 1px solid var(--accent-line);
  box-shadow: 0 -6px 24px -8px rgba(28,35,51,.5);
  padding-bottom: env(safe-area-inset-bottom);
}
@media (max-width: 1023px){
  .rh-mobile-cta{ display: grid; }
  body{ padding-bottom: 64px !important; }
}
.rh-mobile-cta a{
  min-height: 58px;
  display: flex; align-items: center; justify-content: center; gap: 7px;
  color: var(--dark);
  font-family: var(--font-body);
  font-size: 12.5px; font-weight: 700;
  letter-spacing: .06em; text-transform: uppercase;
  text-decoration: none;
  border-right: 1px solid rgba(216,220,232,.14);
  transition: background-color var(--t);
}
.rh-mobile-cta a:last-child{
  border-right: 0; background: var(--accent); color: var(--navy);
}
.rh-mobile-cta a:hover { background: var(--navy-light); }
.rh-mobile-cta a:last-child:hover{ background: var(--accent-hover); }
.rh-mobile-cta a:active{ background: var(--navy-deep); }
.rh-mobile-cta a:focus-visible{ outline: 2px solid var(--accent); outline-offset: -3px; }
```

---

## 7. Accessibility

### 7.1 Measured contrast ratios

All computed against the actual token values using the WCAG 2.x relative-luminance formula.

**On `--dark` (`#faf8f3`):**

| Foreground | Ratio | Verdict |
|---|---|---|
| `--text-dark` `#2a2520` | **14.30:1** | AAA. Headings. |
| `--text-body` `#4a443d` | **9.05:1** | AAA. **The 10,000 words go here.** |
| `--text-meta` / `--w60` composite `#68645f` | **5.53:1** | AA. Captions, bylines, table notes. |
| `--accent-ink` `#846127` | **5.28:1** | AA. Eyebrows, gold links, list markers. |
| `--navy` `#1c2333` | **14.79:1** | AAA. In-copy links, focus rings. |
| **`--w40` composite `#888380`** | **3.50:1** | **FAILS AA.** See below. |
| `--accent` `#c9a86e` | **2.13:1** | Fails. **Decorative only.** Never text on cream. |

**On `--dark-surface` (`#f2efe7`):** `--text-body` 8.36:1, `--w60` 5.11:1,
`--accent-ink` 4.88:1. All pass AA.

**On `--dark-card` (`#ffffff`):** `--text-body` 9.61:1, `--accent-ink` 5.61:1.

**On `--navy` (`#1c2333`):**

| Foreground | Ratio | Verdict |
|---|---|---|
| `--dark` `#faf8f3` | **14.79:1** | AAA. Band headlines, primary button text. |
| `--navy-on` `#d8dce8` | **11.46:1** | AAA. Band body copy. |
| `--accent` `#c9a86e` | **6.96:1** | AA. **This is where gold belongs.** |
| `#ffffff` | 15.70:1 | AAA. |

**On `--navy-deep` (`#141a28`):** `--dark` 16.37:1, `--accent` 7.70:1.

**The `--w40` finding, stated plainly.** Ryan's template says "Body text: Inter,
`var(--w40)` for muted." On a short community page that is survivable. On a 10,000-word
authority hub it is not: `--w40` measures **3.50:1**, which fails AA (4.5:1) and also
fails the 3:1 large-text floor for anything under 24px. **`--w40` is therefore restricted
to non-text decoration and to text at 24px+ only.** All muted body copy uses
`--text-meta` (5.53:1). This is the single most important accessibility change in the spec.

**The white-on-gold finding.** `#ffffff` on `--accent` is **2.26:1**. The template's
"buttons keep white text on accent backgrounds" rule cannot apply here. See §1.4.

### 7.2 Focus-visible

One ring, two tones, always 3:1 or better against its own background.

```css
:where(a, button, [tabindex], summary, input, select, textarea):focus{ outline: none; }

:where(a, button, [tabindex], summary, input, select, textarea):focus-visible{
  outline: 2px solid var(--navy);          /* 14.79:1 on every cream surface */
  outline-offset: 3px;
  border-radius: var(--radius-sm);
}
.rh-band :focus-visible,
.rh-mobile-cta :focus-visible,
.rh-table thead :focus-visible{
  outline-color: var(--accent);            /* 6.96:1 on navy */
}

/* skip link */
.rh-skip{
  position: absolute; left: -9999px; top: 0; z-index: 200;
  padding: 12px 20px; background: var(--navy); color: var(--dark);
  font-size: 14px; font-weight: 600; text-decoration: none;
  border-radius: 0 0 var(--radius) 0;
}
.rh-skip:focus{ left: 0; }
```

### 7.3 Other requirements

- **Never color alone.** The active TOC item carries a color change **plus** weight 600
  **plus** a background tint **plus** a 2px gold bar **plus** `aria-current="true"`.
  Builder brand color is decorative and always accompanied by the builder name in text.
- **Heading order is strict.** One `<h1>`. Eighteen `<h2>`. `<h3>` only inside an `<h2>`
  block. Never skip a level to get a size, use a class.
- **Tables:** real `<caption>`, `<thead>`, `scope="col"` / `scope="row"`. The scroll
  container is `tabindex="0"` with `role="region"` and an `aria-label` so keyboard users
  can scroll it.
- **The FAQ is not an accordion**, so every answer is in the accessibility tree and in the
  crawlable DOM by default.
- **Touch targets** minimum 44x44px. `.rh-btn` is 48px, `.rh-mobile-cta a` is 58px.
- **`prefers-reduced-motion`** disables `scroll-behavior: smooth`, all reveal transitions,
  all `translateY` hovers, and the progress-bar transition. The scroll-spy `aria-current`
  updates still fire, because that is state, not motion.
- **Alt text** on every builder photo and submarket figure. Decorative overlays use
  `aria-hidden="true"`.
- **`lang="en"`** on `<html>`, and `<time datetime>` on the published and updated dates.

```css
@media (prefers-reduced-motion: reduce){
  *, *::before, *::after{
    animation-duration: .01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .01ms !important;
    scroll-behavior: auto !important;
  }
  .rh-toc__progress-fill{ transition: none; }
}
```

---

## 8. Anti-generic guardrails (compliance checklist)

| Rule | How this spec satisfies it |
|---|---|
| **No default Tailwind palette** | Zero Tailwind. Every color is either from Ryan's cream base, the Rose Homes LV brand files, or a verified builder brand hex. No `indigo-500`, no `blue-600`, nothing derived from a framework default. |
| **No flat `shadow-md`** | Every shadow is two-layer and tinted with `rgba(28,35,51,…)`, never pure black. See `--shadow-card`, `--shadow-lift`, `--shadow-rail`, `--shadow-band`. |
| **Different fonts for headings and body** | Playfair Display (serif) for H2 and pull-quotes, Bebas Neue (condensed display) for H1, numerals, and band headlines, Inter (sans) for body and H3. Three distinct roles. |
| **Tight tracking on large headings** | H1 `.02em` on caps (caps need positive tracking), H2 `-.015em`, H3 `-.01em`, pull-quote `-.01em`. |
| **Generous line-height on body** | Body `1.75`, lede `1.68`, FAQ answers `1.75`, table cells `1.5`. |
| **Layered gradients + grain** | `.rh-band::before` layers two radial gradients. `.rh-band::after` adds an inline SVG `feTurbulence` noise layer at 5% opacity. `.rh-figure__frame::after` layers a scrim plus a brass/navy `mix-blend-mode: multiply` treatment. |
| **Only animate transform and opacity** | Every animated property in this spec is `transform`, `opacity`, or a color. The progress bar is `scaleX`, never `width`. The TOC active bar is `scaleY`, never `height`. |
| **Never `transition-all`** | Every `transition` in this document names its properties explicitly. Search the file: `transition-all` and bare `transition: all` appear zero times. |
| **Hover + focus-visible + active on every interactive element** | Builder card, TOC link, all three button variants, in-copy links, mobile CTA buttons, table scroll region. All three states specified. |
| **Gradient overlay + color treatment on images** | §5.4 `.rh-figure__frame::after`. |
| **Intentional spacing tokens** | Vertical rhythm is a fixed set: 8 / 12 / 16 / 22 / 26 / 36 / 44 / 52 / 72 / 84. No arbitrary values. |
| **Depth layering system** | Base `--dark` → surface `--dark-surface` → card `--dark-card` + `--shadow-card` → floating rail `--shadow-rail` → interruptor band `--shadow-band`. Four distinct z-planes, each with its own shadow weight. |

---

## 9. Build order

1. Paste the token block (§1.5) and the type base (§2.4). Verify the wrapper-stripper
   still runs and the page is full-bleed.
2. **Change `overflow-x: hidden` to the `clip` pattern (§3.4) before anything else.**
   Sticky will not work until this lands.
3. Build the article shell grid and the rail (§3.3) with placeholder H2s. Confirm sticky
   works inside the live Lofty embed before writing 10,000 words into it. If it does not,
   the only thing to check is whether an ancestor has `transform` / `filter` / `contain`.
4. Wire the scroll-spy (§3.6).
5. Components in this order: eyebrow, buttons, section shells, tables, takeaway, quote,
   FAQ, stat bar, CTA band, builder card, IDX slot.
6. Pour in content. Enforce the 350-word rule as you go, not afterward.
7. Run the §7.1 contrast table against the shipped page. Verify no `--w40` on body copy
   and no white-on-gold anywhere.
8. Test at all six breakpoints, plus reduced-motion, plus keyboard-only.
