# QA Verification — Independent Cross-Check of Files 00–06 & 08

**QA agent, 2026-07-25.** Every claim below was re-tested against live pages and raw
HTML/CSS/JS pulled fresh this session. Nothing here is taken on an agent's word.

**Method:** `curl` with a desktop Chrome UA against 30+ live URLs; raw HTML parsed with
Python; all 3 stylesheets and 36 JS chunks (17 site-wide + 19 property-page) grepped
directly. Working files in
`/private/tmp/claude-501/-Users-ryanrose-Downloads-Claude/6477daa7-6c35-4157-844e-8990af0dce0e/scratchpad/qa/`.

---

## HEADLINE — read this before anything else

**The flagship page Ryan wants to copy is badly broken, and no agent caught it.**
`/new-construction/` renders 36 listing cards. **21 of them (58%) are in Pahrump** — a town
60 miles outside the Las Vegas valley. Add Mesquite and Boulder City and **23 of 36 (64%)
are outside the LV metro.** Seven more are pre-2020 resales (oldest: 1960). Only about
**8 of 36 cards (22%) are genuinely Las Vegas-metro new construction.**

File `03-geo-subhubs.md:145` states the opposite — that the master hub's feed is "properly
filtered." That is the single most consequential error in the research set, because it
points the client at the wrong competitive angle. The real angle is not "their sub-hubs are
sloppy." It is **"their entire IDX filter is broken, top to bottom, including the hub."**

---

## 1. Verdict table

| # | Claim | Source file | Verdict | Evidence |
|---|---|---|---|---|
| 1 | Hub has an 18-link `nav.toc` | 01 | **CONFIRMED** | 18 `href="#…"` in `<nav class="toc">`; anchors `#builders … #faq` |
| 2 | TOC rail selector is `:is(body:has(.community-card) .toc, body:has(.nc-table) .toc)` | 01 | **CONFIRMED** | Verbatim in `css-0as0ckk54covc.css` inside `@media (min-width:1024px)` |
| 3 | No scroll-spy JS anywhere | 01 | **CONFIRMED** | Only `IntersectionObserver` in any bundle is Next.js `<Link>` prefetch (`onLinkVisibilityChanged`, `rootMargin:"200px"`). Zero `aria-current`, zero `.is-active` |
| 4 | Sub-hubs have no TOC, only `#listings` anchor | 03 | **CONFIRMED** | `henderson/`, `summerlin/new-construction/`: `<nav class="toc">` count = 0 |
| 5 | Community pages have no TOC | 04 | **CONFIRMED** | `/henderson/lake-las-vegas/`: 0 `nav.toc`, 0 `.community-card` |
| 6 | "`/55-plus-communities/` is the only page on the whole site with a real TOC" | 04:95 | **CORRECTED** | Hub, `/builders/`, `/55-plus-communities/` **and every blog post** have `nav.toc`. Four page types, not one |
| 7 | Blog TOC goes fixed right-rail on "hub/community pages" | 05:74 | **CORRECTED** | Blog posts contain neither `.nc-table` nor `.community-card`, so the rail **never** activates on a blog post. Community pages have no TOC at all |
| 8 | 885 blog posts site-wide, sitemap missing ~177 | 05 | **CONFIRMED (177→178)** | `/blog/` index links 885 unique slugs; sitemap has 707 real posts + 1 index URL. Delta = **178** |
| 9 | 708 total blog posts | 00:48, 00:195 | **CORRECTED** | 708 is the *sitemap* figure and includes the `/blog` index URL itself. True post count = **885** |
| 10 | 177 broad / 26 strict NC-adjacent | 00 | **CONFIRMED as arithmetic, rejected as a planning number** | Reproduces exactly on the 708 universe. But "summerlin\|henderson" sweeps in non-NC posts; and the universe is wrong (885, not 708) |
| 11 | 28 NC-adjacent | 03 | **UNVERIFIED** | Falls between my 25 (slug match) and 31 (topic match). Counting rule not stated in file 03 |
| 12 | 173 LV-metro / 186 site-wide NC-adjacent | 05 | **UNVERIFIED** | Plausible but rule not reproducible from the file; my topic-keyword rule yields 31 |
| 13 | 36 `article.search-listing-card` in hub's raw server HTML | 01 | **CONFIRMED** | Exactly 36 `<article class="search-listing-card">` + 36 `id="listing-card-…"` in raw curl output |
| 14 | Community-page IDX is client-hydrated, nothing in server HTML | 04 | **CONFIRMED (nuance)** | `/henderson/lake-las-vegas/`: 0 cards server-side. But it has **no MLS grid at all**, not a hydrated one |
| 15 | Repliers is server-side only, no client fetch | 06 | **CONFIRMED** | Images from `cdn.repliers.io`; listing JSON inline in the RSC payload; no browser-side Repliers call or API key |
| 16 | Tokens `--navy:#2b221a --gold:#d4b27c --brand-rust:#9c5f4e --cream:#f7f4ee --radius:0` | 06 | **CONFIRMED — all five exact** | `:root` block in `css-0as0ckk54covc.css` |
| 17 | Fonts = Cormorant Garamond + Inter | 01 | **CONFIRMED (incomplete)** | Also a second, newer family set: Barlow, Barlow Condensed, Roboto |
| 18 | Henderson sub-hub: 24 listings, 17 built 1942–1996 | 03 | **CORRECTED** | 24 cards confirmed. **15** have a confirmed pre-2000 `yearBuilt` (range **1942–1996**); 2 more have null `yearBuilt`. 17 only if nulls are counted |
| 19 | Summerlin sub-hub shows only 2 listings | 03 | **CONFIRMED — and worse** | 2 cards, built **1984** and **1996**, both addressed "Las Vegas" not Summerlin. **0% are new construction** |
| 20 | A Pahrump listing appears in `/guard-gated-communities/` | 04 | **CONFIRMED — badly undercounted** | **7** Pahrump + 1 Boulder City + 3 Mount Charleston = **11 of 60 (18%)** outside LV metro |
| 21 | Master hub feed is "properly filtered" | 03:145 | **CORRECTED — flatly false** | 21/36 Pahrump, 1 Mesquite, 1 Boulder City, 7 pre-2020 (oldest 1960) |
| 22 | 11 new-construction URLs (2 masters + 8 sub-hubs + 1 outlier) | 00 | **CONFIRMED** | All 11 return 200; sitemap contains exactly those 11 |
| 23 | `/las-vegas/`, `/boulder-city/`, `/henderson/lake-las-vegas/` + `/new-construction/` all 404 | 00 | **CONFIRMED** | All three return **404** |
| 24 | `/builders/` 200, duplicate of hub, canonical → `/new-construction/` | 02 | **CONFIRMED — exactly** | Identical MD5 `6f9f844a09b30b408cc4a3686ac5104b`; canonical → `/new-construction/` |
| 25 | 18 builder pages | 00 | **CORRECTED** | **20** live builder URLs. `pardee` is a distinct builder. `woodside` and `woodside-homes` are two different live pages, each self-canonical |
| 26 | Community pages ~11,650 words / 49 sections / 40 H2 / 18 FAQ | 04 | **PARTLY CORRECTED** | FAQ **18 exact**. H2 **39** (≈40). Sections **46–47** (≈49). Words **9,082–10,279**, so ~12–22% overstated |
| 27 | Blog median 4,591 words | 05 | **CONFIRMED (different basis)** | That is the schema `wordCount` field. My rendered-body count on 2 posts: 5,349 and 4,995. Both defensible; note the basis |
| 28 | 3-free-listing-view wall metered in **localStorage** | 06 | **CORRECTED** | The **3 is confirmed** (`FREE_VIEWS_ORGANIC ?? 3`). Storage is **sessionStorage + a `nreg_vc` cookie**, not localStorage |
| 29 | Lofty has no inline `<form>`; use `#contact` scroll pattern | 08 | **NOT INDEPENDENTLY TESTABLE** | Sourced from Ryan's own skill files, not from NRG. Out of scope for web verification |

---

## C1 — TOC footprint (DEFINITIVE)

This was the highest-priority conflict. It is now fully resolved. **There are two different
TOC components that share the `nav.toc` wrapper class**, which is exactly why agents D and E
contradicted each other.

### Which page types have a TOC

| Page type | Tested URL | TOC? | Component | Mode at ≥1024px |
|---|---|---|---|---|
| Master hub | `/new-construction/` | **Yes, 18 links** | BEM | **Fixed right rail** |
| `/builders/` (hub clone) | `/builders/` | Yes, 18 links | BEM | Fixed right rail |
| Lifestyle index | `/55-plus-communities/` | **Yes, 11 links** | BEM | **Fixed right rail** |
| Blog post | 2 tested | **Yes** | `details` | **Inline only — never fixed** |
| Geo sub-hub | `/henderson/`, `/summerlin/` `/new-construction/` | **No** | — | — |
| Community page | `/henderson/lake-las-vegas/`, `/summerlin/` | **No** | — | — |
| Builder page | `/builders/lennar/`, `/builders/kb-home/` | **No** | — | — |
| Other lifestyle | `/guard-gated-communities/`, `/golf-communities/` | **No** | — | — |

### Component A — the "BEM" TOC (hub, `/builders/`, `/55-plus-communities/`)

```html
<nav class="toc" aria-label="Table of contents">
  <h2 class="toc__title">On This Page</h2>
  <ol class="toc__list">
    <li><a href="#builders">Active builders in Las Vegas</a></li>
    ...
  </ol>
</nav>
```

Hub anchors, in order — all 18:
`#builders` `#why-2026` `#summerlin` `#henderson` `#lake-las-vegas` `#sw-vegas` `#nlv`
`#nw-vegas` `#boulder-city` `#launches-2026` `#builder-comparison` `#price-by-submarket`
`#new-vs-resale` `#step-by-step` `#incentives` `#warranties` `#lot-premiums` `#faq`

### Component B — the "details" TOC (blog posts only)

```html
<nav class="toc" aria-label="Table of contents">
  <details open="">
    <summary>On this page</summary>
    <ol class="toc-list">   <!-- NOTE: toc-list, hyphen — NOT toc__list -->
      <li><a href="#what-is-a-lot-premium-…">What Is a Lot Premium…</a></li>
    </ol>
  </details>
</nav>
```

The hyphen-vs-double-underscore distinction is the crux. Because blog posts use
`ol.toc-list`, **none of the `.toc__list` rules apply to them** — no 2-column layout, no
uppercase eyebrow. And because a blog post's body contains neither `.nc-table` nor
`.community-card`, **the fixed-rail media query never matches on a blog post.**

### The definitive CSS (verbatim from `css-0as0ckk54covc.css`)

Base, applies to every `nav.toc` (two `.toc` rules cascade; the second wins on conflicts):

```css
.toc{background:var(--cream);border-radius:var(--radius-lg);max-width:720px;
     margin:0 0 32px;padding:16px 20px;font-size:14px}
.toc summary{cursor:pointer;color:var(--navy);font-weight:600}
.toc a{color:var(--navy);text-decoration:none}
.toc a:hover{color:var(--gold);text-decoration:underline}

/* later rule — overrides margin/padding/border for all nav.toc */
.toc{background:var(--cream);border-left:2px solid var(--gold);margin:0 0 40px;padding:22px 26px}

.toc__title{font-family:var(--font-sans);letter-spacing:.14em;text-transform:uppercase;
            color:var(--gold-hover);margin:0 0 12px;font-size:11px;font-weight:700}
.toc__list{columns:2;column-gap:28px;margin:0;padding-left:22px;list-style:decimal}
.toc__list li{break-inside:avoid;margin-bottom:6px}
.toc__list a{color:var(--navy);font-size:14px;line-height:1.6;text-decoration:none}
```

Mobile collapse:
```css
@media (max-width:700px){ .toc__list{columns:1} }
```

The promotion to a fixed rail — **this is the whole trick**:
```css
@media (min-width:1024px){
  :is(body:has(.community-card) .toc, body:has(.nc-table) .toc){
    position:fixed; right:24px;
    top:calc(var(--nav-h,72px) + 24px);
    width:250px;
    max-height:calc(100vh - var(--nav-h,72px) - 60px);
    overflow-y:auto;
    z-index:8;
    background:var(--cream);
    border-left:3px solid var(--gold);   /* 3px here vs 2px in flow */
    margin:0; padding:18px 20px; font-size:13px;
    box-shadow:0 4px 14px #0a0a0a0f;
  }
  :is(body:has(.community-card) .toc .toc__list,
      body:has(.nc-table) .toc .toc__list){columns:1;padding-left:18px}
  :is(body:has(.community-card) .toc__list li,
      body:has(.nc-table) .toc__list li){margin-bottom:4px}
  :is(body:has(.community-card) .toc__list a,
      body:has(.nc-table) .toc__list a){font-size:13px;line-height:1.45}
}
```

### How D and E both went wrong

The selector says `body:has(.community-card)`. That reads like "community pages," and that
is what misled Agent E. But `.community-card` is an **editorial card component used on
lifestyle index pages**, and in practice it appears on exactly one page: `/55-plus-communities/`
(420 occurrences). Actual community pages use the `cp-*` prefix and have **zero**
`.community-card` and zero TOC. Agent D was right about community pages and wrong to claim
55-plus was unique; Agent E was right about the CSS and wrong about which pages match it.

### Scroll-spy: definitively NONE

Grepped all 36 JS chunks. The only `IntersectionObserver` in the entire codebase is Next.js's
own link-prefetch observer — its surrounding symbols are `onLinkVisibilityChanged`,
`pingVisibleLinks`, `createPrefetchURL`, `rootMargin:"200px"`. There is no `aria-current`, no
`.is-active`, no `--active` rule in any stylesheet.

**The TOC is 100% CSS plus native anchor jumps. Zero JavaScript. It is trivially portable to
a Lofty HTML embed, and adding scroll-spy is a cheap, real differentiator.**

**Porting note:** `--nav-h` is declared `72px` in the main `:root` but overridden to `64px`
in a second `:root` block. Hardcode your own nav height in the `top:` calc rather than
inheriting this ambiguity.

---

## C2 — Blog counts: Agent E was right

| Source | Count |
|---|---|
| `/blog/` index, unique post slugs | **885** |
| `sitemap.xml`, unique `/blog/` URLs | 708 (= **707 posts** + the `/blog` index URL itself) |
| Live but **missing from sitemap** | **178** |
| In sitemap but not on live index | 0 real posts |

`/blog/page/2/`, `/page/30/`, `/page/60/`, `/page/89/` all return **200 with the identical
885 links** — the pagination route is a catch-all that re-renders the same index. That is a
second, separate hygiene bug (unbounded duplicate URLs).

**The 178 missing posts are genuinely orphaned, and the pattern is legible:** 114 of 178 have
no year suffix (`10-things-you-need-to-buy-a-home-today`,
`10-tips-to-buying-a-new-construction-home`), versus 484 of 708 sitemap entries that *do*
carry `-2025`/`-2026`. The sitemap generator appears to emit only newer CMS-managed posts and
drops the legacy imported set.

**Verdict: real hygiene bug, Agent E did not overcount.** Correct file 00.

---

## C3 — NC-adjacent blog count: one defensible number

The disagreement is caused by two free variables nobody pinned down: **which universe**
(708 sitemap vs 885 live) and **which keyword rule**. Measured both:

| Rule | On 708 (sitemap) | On 885 (live) |
|---|---|---|
| **Strict** — slug contains `new-construction` | 20 | **25** |
| **Topical** — `new-construction, builder, incentive, lot-premium, design-center, pre-drywall, buydown` | 26 | **31** |
| **Broad** — topical + geo names (`summerlin, henderson, inspirada, cadence, skye`) | **177** | 222 |

The orchestrator's 177 reproduces exactly, so the arithmetic was sound — but the broad rule
is not fit for planning, because `summerlin` and `henderson` match large volumes of resale,
lifestyle and agent-bio content that has nothing to do with new construction.

> **Use this number: 31 NC-topical posts out of 885 (3.5%), counted on the live index with
> the geo-agnostic topical rule.** If you want the tightest defensible figure, **25** by pure
> slug match. Do not use 177 or 222.

Agent C's 28 and Agent E's 173/186 could not be reproduced because neither file states its
rule. Both are flagged UNVERIFIED, not wrong.

---

## C4 — IDX rendering: server vs client, per page type

All three agents were right about different page types. Counts are of
`<article class="search-listing-card">` in **raw curl output** (no JS executed):

| Page type | URL tested | Cards in raw server HTML | Verdict |
|---|---|---|---|
| Master hub | `/new-construction/` | **36** | Fully SSR |
| Geo sub-hub | `/henderson/new-construction/` | **24** | Fully SSR |
| Geo sub-hub | `/summerlin/new-construction/` | **2** | Fully SSR |
| Lifestyle | `/guard-gated-communities/` | **60** | Fully SSR |
| Lifestyle | `/55-plus-communities/` | **0** | **No MLS grid at all** — uses editorial `.community-card` |
| Lifestyle | `/golf-communities/` | **0** | No MLS grid |
| Community | `/henderson/lake-las-vegas/` | **0** | **No MLS grid** |
| Community | `/summerlin/` | **0** | No MLS grid |
| Builder | `/builders/lennar/`, `/builders/kb-home/` | **0** | No MLS grid |

**Everything MLS-backed is server-rendered.** Full listing JSON (`mlsNumber`, `listPrice`,
`details.yearBuilt`, `details.sqft`, photo arrays) is inlined in the Next.js RSC payload. No
browser-side Repliers call exists; the API key never reaches the client. Agent F confirmed.

**One correction of nuance:** Agent D described community-page IDX as "client-hydrated,
nothing in server HTML." The "nothing in server HTML" half is right, but there is nothing
client-side either — **community, lifestyle-editorial and builder pages simply have no MLS
grid.** That is a meaningful difference for planning: those templates are pure content, so on
Lofty they need no IDX slot at all.

**Where a Lofty feed goes:** hub, geo sub-hubs, and MLS-backed lifestyle pages. Their SSR
approach is not portable (it is a paid server-side API inside their own Next.js app), so file
08's decision tree stands unchanged — but it now applies to **3 page types, not all of them.**

---

## C5 — Design tokens: Agent F correct on all five

From the `:root` block of `css-0as0ckk54covc.css`. Every value Agent F reported is exact:

```
--navy:#2b221a      --gold:#d4b27c       --cream:#f7f4ee
--brand-rust:#9c5f4e                     --radius:0
```

Supporting palette: `--navy-deep:#1a1410` · `--gold-hover:#b89460` · `--gold-light:#e8d4b0`
· `--gold-text:#7a5b2a` · `--cream-warm:#ede7da` · `--stone:#7a7368` · `--line:#e8e2d6`
· `--urgency:#e63946` · `--positive/--success:#3d6b4a`

**No disagreement between A and F on tokens.** The palette is a warm dark-brown/gold scheme,
not the navy-blue the name `--navy` implies — `#2b221a` is a dark brown. Worth flagging to
Ryan, since "navy" in the spec would mislead a designer.

Radius is **0 across the board** (`--radius`, `--radius-md`, `--radius-lg` all `0`;
`--radius-sm:2px`). Sharp corners are a deliberate brand choice. Note file 01's observation
that IDX cards use an 8px radius is a genuine inconsistency **on their side**.

**Fonts — file 01 is right but incomplete.** Two generations coexist:
- Legacy: `--font-serif: "Cormorant Garamond", Georgia, serif` · `--font-sans: "Inter", …`
- Newer: `--font-cond: Barlow Condensed` · `--font-body: Barlow` · `--font-ui: Roboto`

Fluid type scale is `clamp()`-based, `--text-xs` through `--text-2xl`; container `1240px`.

---

## C6 — The filter bugs: BOTH CONFIRMED, both worse than reported

This is the client's competitive angle and it holds up. Evidence is the `details.yearBuilt`
field parsed from each page's own inlined listing JSON.

### 6a. `/henderson/new-construction/` — 24 listings, 15 confirmed not new

| MLS | Address | yearBuilt |
|---|---|---|
| 2799528 | **242 Kansas Avenue** | **1942** |
| 2790136 | 479 S Water Street | 1953 |
| 2776385 | 249 Shoshone Lane | 1964 |
| 2785455 | 236 E Country Club Drive | 1973 |
| 2773894 | 620 Hidden Valley Drive | 1976 |
| 2771618 | 1121 Pawnee Lane | 1983 |
| 2794167 | 2366 Belvedere Drive | 1984 |
| 2771091 | 943 Tami Circle | 1984 |
| 2783170 | 3147 Viewcrest Avenue | 1985 |
| 2799554 | 845 Shoreview Drive | 1987 |
| 2802700 | 400 Breeze Way | 1992 |
| 2793593 | 2583 Hummingbird Hill Avenue | 1993 |
| 2802026 | 2848 Via Terra Street | 1994 |
| 2799404 | 640 N Racetrack Road | 1995 |
| 2795505 | **822 Grape Vine Avenue** | **1996** |

Full range across the page: **1942 to 2026.** Two further listings (0000 Jena Street,
430 Paradise Hills Road) have a **null `yearBuilt`** — counting those gets you to Agent C's
17. The honest statement is **"15 confirmed pre-2000, plus 2 with no year on record, out of
24."** Use 15 with the client; it is unimpeachable.

### 6b. `/summerlin/new-construction/` — 2 listings, both resales, neither in Summerlin

| MLS | Address | yearBuilt |
|---|---|---|
| 2794360 | 121 Logansberry Lane — **Las Vegas** | **1984** |
| 2792864 | 8640 Blissville Avenue — **Las Vegas** | **1996** |

A page titled for Summerlin new construction, returning two 1980s/90s resales, neither
addressed in Summerlin. **Zero percent accuracy.** This is the strongest single demo asset in
the whole teardown.

### 6c. `/guard-gated-communities/` — Agent D undercounted 7×

60 cards. City distribution: **Las Vegas 40 · Henderson 9 · Pahrump 7 · Mount Charleston 3 ·
Boulder City 1.** So **11 of 60 (18%)** sit outside the Las Vegas guard-gated market.
Pahrump examples: 2120 Iroquois Avenue, 1890 W Dyer Road, 4161 S Bailey Avenue,
9376 Winston Court, 9350 S Winston Court, 2100 Iroquois Avenue, 1560 Windy Lane.

### 6d. NEW — the master hub is the worst offender

Not previously reported by anyone. 36 cards on `/new-construction/`:

**Las Vegas 8 · Pahrump 21 · Henderson 4 · Boulder City 1 · North Las Vegas 1 · Mesquite 1**

- **21 of 36 (58%) are Pahrump.** Sample: 3451 S Soplo Ave, 2880 S Red Rock, 1700 Escuela
  Ave, 5621 Humbolt Pl, 3001 Spy Glass Ave, 653 & 667 S Dyani Dr, 601 Nikki Way.
- 7 of 36 are pre-2020 builds: 1704 James Street (**1960**), 4545 W Desert Inn Rd (1972),
  5854 Alfred Dr (1975), 3660 W Robindale Rd (1978), 2366 Belvedere Dr (1984),
  400 Breeze Way (1992), 6340 Dallaswood Ln (1994).
- Year range **1960–2026**.

The page's own methodology copy claims listings are "single-family homes built 2024 or later"
and post-filtered to drop renovated older homes. **The rendered output contradicts the
page's own stated methodology.** File 03's "the master hub's feed is properly filtered" is
false and must be struck.

---

## C7 — new-construction URL set: CONFIRMED (11)

All 11 return **200**, and the sitemap contains exactly these 11 and no others:

`/new-construction/` · `/henderson/new-construction/` · `/summerlin/new-construction/` ·
`/north-las-vegas/new-construction/` · `/centennial-hills/new-construction/` ·
`/enterprise/new-construction/` · `/reno-new-construction/` · `/sparks/new-construction/` ·
`/dayton/new-construction/` · `/fernley/new-construction/` · `/pahrump/new-construction-homes/`

Breakdown of 2 masters + 8 sub-hubs + 1 outlier is internally consistent.

Claimed 404s — **all three verified 404**:
`/las-vegas/new-construction/` · `/boulder-city/new-construction/` ·
`/henderson/lake-las-vegas/new-construction/`

Worth noting for our build: **there is no `/las-vegas/new-construction/`.** The city term is
owned by the root `/new-construction/`. That is a deliberate and correct choice to avoid
self-competition, and we should copy it.

---

## C8 — `/builders/` index: CONFIRMED exactly

- Returns **200**.
- **Byte-identical to the hub** — both MD5 `6f9f844a09b30b408cc4a3686ac5104b`, 1,091,657 bytes.
  Not merely "a near-duplicate": it is the same response body.
- `<link rel="canonical" href="https://www.nevadarealestategroup.com/new-construction/"/>` —
  the canonical points away from itself to the hub.
- Absent from the sitemap, consistent with deliberate exclusion.

Agent B fully confirmed.

### Correction found while verifying: there are 20 builder pages, not 18

The sitemap holds **20 unique** `/builders/*` URLs, and all 20 return 200:
`beazer · blue-heron · century-communities · christopher · dr-horton · harmony · kb-home ·
lennar · lgi · pardee · pulte-del-webb · richmond-american · shea · storybook ·
taylor-morrison · toll-brothers · touchstone · tri-pointe · woodside · woodside-homes`

- **`pardee` is a distinct builder** (Pardee Homes), not a duplicate. File 00 dismissed it as
  a Reno-list artifact; it is a real 20th page.
- **`woodside` vs `woodside-homes` are two different pages** — different MD5, different
  `<title>` ("Woodside Homes Las Vegas | New Construction Builder" vs "Woodside Homes Las
  Vegas New Construction Homes 2026"), and **each canonicalizes to itself.** This is a live
  keyword-cannibalization bug, more serious than file 00's "duplicate sitemap entry" framing.

---

## C9 — Magnitude spot-checks

Counted independently: rendered text inside `<main>`, `<script>`/`<style>`/`<svg>` stripped,
FAQ count from `"@type":"Question"` in JSON-LD.

| Page | Words | H2 | H3 | `<section>` | FAQ |
|---|---|---|---|---|---|
| `/henderson/lake-las-vegas/` | **10,279** | 39 | 110 | 47 | **18** |
| `/summerlin/` | **9,082** | 39 | 110 | 46 | **18** |
| `/new-construction/` (hub) | 8,854 | 24 | 16 | 13 | 12 |
| `/55-plus-communities/` | 4,555 | 14 | 29 | 16 | 10 |
| `/henderson/new-construction/` | 2,556 | 10 | 0 | 14 | 8 |
| `/builders/lennar/` | 1,607 | 8 | 15 | 10 | 6 |
| blog — lot-premium-negotiation | 5,349 | 17 | 14 | 1 | 9 |
| blog — henderson-builders-guide | 4,995 | 17 | 12 | 1 | 7 |

**Community pages (file 04):** FAQ count of 18 is **exact**. H2 40 ≈ 39 and sections 49 ≈ 47
are within tolerance. **Word count is the one to fix: 11,650 claimed vs 9,082–10,279
measured, so ~12–22% high.** Restate as "roughly 9,000–10,500 words." Still a very large page
and the strategic point is unchanged.

**Blog (file 05):** median 4,591 is the **schema `wordCount` field**, whereas my 5,349/4,995
are rendered body text. Both are legitimate; the file should just name its basis. The
structural claims (13–18 H2s, 6–9 FAQs) match my two samples exactly (17 H2; 9 and 7 FAQs).

**Note the template hierarchy this reveals:** community pages (~10k words, 39 H2) are far
longer than the hub (8.8k, 24 H2), which dwarfs the sub-hubs (2.5k, 10 H2) and builder pages
(1.6k, 8 H2). Sub-hub and builder pages are thin, and that is a real opening for us.

---

## C10 — Registration wall: the "3" is right, the storage is not

Recovered from the property-page chunk `pjs/03rz0adw2vm~e.js`:

```js
GATE_CONFIG = {
  FREE_VIEWS_ORGANIC: Number(process.env.NEXT_PUBLIC_FREE_VIEWS_ORGANIC) ?? 3,
  FREE_VIEWS_PAID:    Math.max(1, process.env.NEXT_PUBLIC_FREE_VIEWS_PAID ?? 3),
  OTP_TRIGGER:        process.env.NEXT_PUBLIC_OTP_TRIGGER ?? "registration",
  PAID_ATTRIBUTION_WINDOW_DAYS: 30
}
STORAGE = {
  VIEWED_LISTINGS:   "nreg_viewed_listings",
  VIEW_COUNT_COOKIE: "nreg_vc",
  ...
}
```

**Confirmed: 3 free listing views**, separately configurable for organic vs paid traffic.

**Corrected: it is not localStorage.** The only localStorage keys in the entire bundle set are
`nreg_favorites`, `debug`, and `supabase.gotrue-js.locks.debug`. Metering is dual:

| Mechanism | Key | Storage |
|---|---|---|
| Unique-listing set | `nreg_viewed_listings` | sessionStorage |
| Anonymous view counter | `nreg_anon_views` | sessionStorage |
| Durable view counter | `nreg_vc` | **cookie** (survives storage clear) |
| Full gate bypass | `nreg_ml=1` | cookie |
| Logged-in-agent exemption | `nreg_gate_agent` | sessionStorage, backed by `fetch("/api/agent/session")` |
| Attribution | `nreg_attr`, `nreg_first_utm`, `nreg_click_ids`, `nreg_src`, `nreg_paid` | mixed |

Flow: `meterListingView(mlsNumber)` returns `{trafficSource, threshold, uniqueViews, walled}`.
If `walled`, it checks for an agent session, then opens a focus-trapped modal and fires GTM
`gate_wall_shown` with `traffic_source` and `threshold`. Registration POSTs to
`/api/leads/buyer/` with `source: "NREG - Registration"` and
`questions: "Registered via listing gate (…, N homes viewed)"`. Partially-typed fields persist
in sessionStorage so a reload does not lose them. A secondary prompt fires at **≥5** browse
events.

**Two things the fleet missed here:**
1. **Auth is Supabase** (`supabase.gotrue-js`, `supabaseUrl`, `supabaseKey` — 65 hits). That is
   a fourth stack component absent from file 00's "Next.js + Sanity + Repliers."
2. **A bot user-agent regex (`_LIMITED_BOT_UA_RE`) exempts crawlers from the wall.** That is
   why every `curl` in this research returned complete unwalled HTML, and it is how they keep
   a hard paywall without cloaking penalties.

**Likely source of Agent F's confusion:** the hub carries editorial copy reading *"Register
with a buyer's agent on your first visit."* That is advice about builder registration in new
construction, not the site's own wall.

---

## 2. Corrections to apply to other files

### `00-master-sitemap-architecture.md`
1. **§2 and §6 — blog count.** "708 posts" → **885 posts; 707 in the sitemap, 178 orphaned.**
   Add to §7 as hygiene issue #7.
2. **§4 and §2 — builder count.** "18 builder pages" → **20.** `pardee` is a real distinct
   page. Rewrite the woodside note: `woodside` and `woodside-homes` are **two live pages, each
   self-canonical** — active cannibalization, not a sitemap dupe.
3. **§6 — NC-adjacent count.** "177 posts" → **31 NC-topical of 885 (or 25 by strict slug).**
   State the rule. Keep 177 only if explicitly labelled "broad, includes geo terms."
4. **§7 — add hygiene issue.** `/blog/page/{n}/` returns 200 with identical content for any
   `n` (tested to 89): unbounded duplicate URLs.
5. **§1 — stack.** Add **Supabase Auth** alongside Next.js + Sanity + Repliers.
6. **§8 — "Sticky TOC component" P0.** Note it is CSS-only and that NRG ships it on **only 3
   page types**; putting it on every page is a differentiator, not parity.

### `01-hub-page-teardown.md`
Substantially accurate — the strongest file in the set. Two additions:
1. **Add the IDX contamination finding.** The teardown documents the 36-card grid without
   noting that 21 are Pahrump and 7 are pre-2020. Anyone using this file as a build spec would
   copy a broken filter.
2. **§ tokens — flag that `--navy:#2b221a` is a dark brown, not navy,** so a designer reading
   the token name does not pick a blue.

### `03-geo-subhubs.md`
1. **Line 145 — STRIKE the claim that the master hub's feed is "properly filtered."** Replace
   with C6d: 21/36 Pahrump, 7 pre-2020, range 1960–2026, contradicting the page's own stated
   methodology. This is the most important single correction in this document.
2. **Line 141 — the 1942–1996 bucket.** "17" → **"15 confirmed pre-2000, plus 2 with null
   `yearBuilt`."**
3. **Add to the Summerlin row:** both listings are addressed **Las Vegas**, not Summerlin.
4. **State the counting rule behind "28 NC-adjacent"** or replace with 31/25 from C3.

### `04-community-lifestyle-pages.md`
1. **Line 95 — STRIKE "The only page on the whole site that has a real TOC is
   `/55-plus-communities/`."** Replace with the C1 table: hub, `/builders/`,
   `/55-plus-communities/` (BEM, fixed rail) and all blog posts (`details`, inline only).
2. **Guard-gated Pahrump finding — "a Pahrump listing" → 7 Pahrump + 1 Boulder City +
   3 Mount Charleston = 11 of 60 (18%).** List the addresses from C6c.
3. **Word count** "~11,650" → **"roughly 9,000–10,500."** Keep 18 FAQs (exact) and ~39 H2s.
4. **"client-hydrated" IDX** → community/builder/editorial-lifestyle pages have **no MLS grid
   at all**, server-side or client-side.

### `05-blog-cluster.md`
1. **Line 74 — STRIKE "the hub and community pages get a floating right-rail TOC."** Community
   pages have no TOC. The rail activates only where `.nc-table` or `.community-card` is
   present: the hub, `/builders/`, and `/55-plus-communities/`.
2. **Internal inconsistency, lines 49 vs 73–74.** Line 49 correctly identifies the blog TOC as
   `nav.toc > ol.toc-list`, but lines 73–74 then describe it with the **hub's** `.toc__title`
   / `.toc__list` styling (uppercase eyebrow, two-column decimal). Blog posts use
   `<details><summary>` + `ol.toc-list` and get **none** of those rules. Rewrite 73–74 to
   describe Component B only.
3. **Line 13 — "missing 177 posts"** → **178.** 885 live, 707 real posts in sitemap.
4. **Line 17 — label the median as schema `wordCount`,** not rendered body words, and note
   rendered bodies run ~8–15% higher.
5. **Lines 14/16 — 173/186 NC-adjacent** need their counting rule stated, or replace with C3.

### `06-conversion-and-tech.md`
1. **Registration wall** — keep "3 free views" (confirmed, `FREE_VIEWS_ORGANIC ?? 3`), replace
   "localStorage" with **sessionStorage (`nreg_anon_views`, `nreg_viewed_listings`) plus the
   `nreg_vc` cookie**; add the `nreg_ml=1` bypass, the Supabase/agent-session exemption, the
   separate paid-traffic threshold, and the bot-UA exemption.
2. **Add Supabase Auth to the stack section.**
3. **Design tokens confirmed verbatim — no change needed.**

### `08-lofty-porting-constraints.md`
Accurate; its core conclusion (Repliers is server-side-only and not portable) is confirmed.
One refinement: **an IDX slot is needed on only 3 page types** — hub, geo sub-hubs, and
MLS-backed lifestyle pages. Community, builder and editorial-lifestyle templates carry no MLS
grid, so they can ship on Lofty with no IDX dependency at all. That materially de-risks the
build: **P1 builder pages are not blocked on the Lofty IDX question.**

---

## 3. Gaps / what we still don't know

**Blocking the build**
1. **The Lofty IDX embed snippet — still the single biggest unknown.** File 08 flags it and
   nothing in this QA pass resolves it; it can only come from Ryan. Newly narrowed, though:
   it is needed for 3 page types, not all, so builder pages can start now.
2. **Whether Lofty landing pages support `body:has()`-scoped CSS and `position:fixed` inside
   an HTML embed.** The TOC is the component Ryan specifically wants and it depends on both.
   Untested — nobody has put this CSS into a real Lofty embed. **Test this first with a
   throwaway page**; if `position:fixed` is clipped by a Lofty wrapper, the rail needs
   `position:sticky` inside a grid column instead, which changes the page skeleton.

**Unverified claims left standing**
3. **Agent E's 173-post corpus statistics** (81% linking to `/new-construction/`, exactly 4
   figures in 162 of 173, median 26 internal links, 27 YouTube embeds). I verified structure
   on 2 posts only. The per-post numbers matched, so the corpus work is probably sound, but
   the aggregates are unaudited. Treat as directional.
4. **Agent B's 20-builder-page template claims** (shared template, builder chip grid on every
   page). I confirmed status codes, canonicals and word counts for 3 builder pages but did not
   audit the template internals across all 20.
5. **The `/compare/` (38) and `/guides/` (10) page counts** in file 00 were not independently
   re-verified this pass.
6. **Whether the registration wall actually fires.** I recovered the code path, not live
   behavior — the bot-UA exemption means `curl` can never trigger it. Confirming the modal
   requires a real browser session, and the wall's real-world conversion impact is unknowable
   from outside.

**Strategic gaps the fleet did not cover**
7. **No traffic or ranking data anywhere in the research.** 2,129 pages is impressive
   engineering, but nothing establishes that the hub actually ranks or converts. We are
   reverse-engineering a competitor on the assumption it works. A single Ahrefs/Semrush pull
   on `nevadarealestategroup.com/new-construction/` would either validate the whole programme
   or reveal we are copying an expensive page that ranks for nothing. **Recommend doing this
   before committing to P1/P2/P3.**
8. **No mobile teardown.** Everything was analysed at desktop width. The TOC is explicitly
   desktop-only (≥1024px) and mobile gets a sticky CTA bar instead. For a Las Vegas real
   estate audience — majority mobile — the mobile experience is arguably the more important
   half, and it is undocumented.
9. **Nobody checked whether NRG's content is itself accurate.** File 08 correctly forbids
   copying their incentive figures. Given that their IDX filter is this broken, their prose
   claims deserve the same skepticism. Do not treat their copy as a research shortcut.
10. **`--nav-h` is declared twice with different values (72px, then 64px).** Whatever we port
    must hardcode our own nav height rather than inherit this.

---

## 4. Bottom line for the client

The component Ryan wants is **real, simple, and free**: a pure-CSS fixed right-rail TOC, no
JavaScript, ~30 lines. It is fully specified in C1 above and can be lifted today. NRG ships it
on only 3 of their ~2,129 pages, and it has no scroll-spy — putting it on every hub page,
with scroll-spy, beats them outright for trivial effort.

The competitive angle is stronger than the fleet reported, but it is **not** the one file 03
framed. It is not "their sub-hubs are sloppy while the hub is clean." **Their new-construction
IDX filter is broken everywhere, and the flagship hub is the worst offender** — 58% Pahrump,
homes back to 1960, on a page whose own copy promises LV-metro homes built 2024 or later. A
side-by-side of their `/summerlin/new-construction/` (two homes, 1984 and 1996, neither in
Summerlin) against a correctly-filtered Lofty feed is the entire pitch.
