# NRG New-Construction Hub — Full Page Teardown

**Source:** https://www.nevadarealestategroup.com/new-construction/
**Captured:** 2026-07-25 (raw HTML 1,090,434 bytes)
**Stack:** Next.js App Router (RSC, turbopack build), Vercel deploy id `dpl_GZAh5K3bnphFH8yyfeFDmC4uWZ6K`. Page is **fully server-rendered** — every listing card, table, and FAQ answer is in the initial HTML. No client-side hydration is required to read the content.
**Scope:** hub page body only. Site header nav and footer nav deliberately excluded.

---

## 0. TL;DR structural shape

```
breadcrumb
└ hero (420px fixed-height image band, H1 + stat line + 3 CTAs)
└ IDX live MLS feed          ← 36 server-rendered Repliers cards (~2,458 words of card text)
└ direct-answer blockquote + key-takeaways bullet list
└ article meta (author / published / updated / 25 min read)
└ direct-answer-block (2nd, shorter)
└ nav.toc  ← 18 jump links, becomes position:fixed right rail ≥1024px
└ "New Construction by City" pill row (5 city hub links)
└ #builders — 18 builder cards + 5 price-tier filter buttons
└ ONE long <section> containing 15 H2 blocks (why-2026 → lot-premiums → why-NREG)
    incl. 5 <table class="nc-table">
└ #faq — 12 Q&A, always-open (NOT an accordion)
└ #lead-form — 8-field lead form + honeypot
└ fair-housing disclosure
└ navy CTA band (call / email)
└ .mobile-sticky-cta (fixed bottom bar, <1024px only)
└ 7 × JSON-LD blocks
└ "Read Next" blog feed (3 cards)
```

Total on-page body copy (excluding nav/footer): **~9,900 words**, of which ~2,460 is IDX card text and ~7,400 is editorial.

---

## 1. Section-by-section outline (exact page order)

| # | Byte pos | Anchor id | Heading (verbatim) | Type | ~Words | Items |
|---|---|---|---|---|---|---|
| — | 33,443 | — | (breadcrumb: Home › New Construction) | nav strip | 3 | 2 crumbs |
| 1 | 33,590 | — | **H1: New Construction Homes in Las Vegas** | hero image band | 35 | 3 CTAs |
| 2 | 35,713 | — | **H2: Active New-Construction Homes For Sale Right Now** | IDX card grid | 2,458 | **36 listing cards** |
| 3 | 288,744 | — | *(aria-label="Direct answer summary", no heading)* | blockquote + UL | 285 | 1 blockquote + 6 takeaway bullets |
| 4 | 291,480 | — | *(no heading)* — article meta byline | meta strip | 20 | author, pub date, upd date, read time |
| 5 | 292,151 | — | *(class `direct-answer-block`, no heading)* | prose callout | 72 | 1 para |
| 6 | 292,885 | — | **H2: On This Page** (`nav.toc`) | jump-link list | 57 | **18 links** |
| 7 | 293,956 | — | **H2: New Construction by City** | pill link row | 38 | 5 pills |
| 8 | 295,685 | `builders` | **H2: Las Vegas Home Builders** | card grid + filter chips | 759 | **18 builder cards**, 5 filter buttons |
| 9 | 314,174 | `why-2026` | **H2: Why buy new construction in Las Vegas in 2026?** | prose (3 paras, 8 outbound authority links) | 483 | — |
| 10 | 319,196 | `summerlin` | **H2: What new construction is available in Summerlin?** | image + prose | 438 | 1 figure |
| 11 | 324,986 | `henderson` | **H2: What new construction is available in Henderson?** | image + prose (4 sub-blocks) | 459 | 1 figure |
| 12 | 330,749 | `lake-las-vegas` | **H2: What new construction is available in Lake Las Vegas?** | prose (4 sub-blocks) | 471 | — |
| 13 | 334,928 | `sw-vegas` | **H2: What new construction is available in Southwest Las Vegas?** | image + prose (5 sub-blocks) | 425 | 1 figure |
| 14 | 340,634 | `nlv` | **H2: What new construction is available in North Las Vegas?** | image + prose (4 sub-blocks) | 516 | 1 figure |
| 15 | 346,572 | `nw-vegas` | **H2: What new construction is available in Northwest Las Vegas?** | prose (4 sub-blocks) | 457 | — |
| 16 | 350,629 | `boulder-city` | **H2: What new construction is available in Boulder City?** | prose (4 sub-blocks) | 479 | — |
| 17 | 354,609 | `launches-2026` | **H2: Which new-construction communities are launching in 2025-2026?** | **table** | 146 | 10 rows |
| 18 | 356,552 | `builder-comparison` | **H2: How do national and regional Las Vegas builders compare?** | prose + **table** | 194 | 7 rows |
| 19 | 359,800 | `price-by-submarket` | **H2: How much does new construction cost by Las Vegas submarket?** | prose + **table** | 144 | 7 rows |
| 20 | 361,924 | `new-vs-resale` | **H2: Should you buy new construction or resale in Las Vegas?** | **table** | 108 | 8 rows |
| 21 | 363,404 | `step-by-step` | **H2: How do you buy a new-construction home in Las Vegas, step by step?** | numbered prose | 335 | 6 steps (bolded lead-ins, no `<ol>`) |
| 22 | 366,655 | `incentives` | **H2: What builder incentives are available in 2026?** | image + prose + **table** | 319 | 12 rows |
| 23 | 371,810 | `warranties` | **H2: What warranties cover new homes in Nevada?** | prose | 112 | 1 para |
| 24 | 373,103 | `lot-premiums` | **H2: What are lot premiums and how much do they add?** | prose | 93 | 1 para |
| 25 | 373,995 | *(none — not in TOC)* | **H2: Why use Nevada Real Estate Group for new construction?** | prose | 149 | 1 para |
| 26 | 375,659 | `faq` | **H2: Frequently Asked Questions** | Q&A list (always open) | 719 | **12 questions** |
| 27 | 384,627 | `lead-form` | **H3: Get Builder Incentives & Floor Plans** | form | 286 | 8 fields + honeypot |
| 28 | 387,636 | — | *(Fair Housing disclosure aside)* | legal | 95 | — |
| 29 | 388,703 | — | **H2: Expert New Construction Guidance** | navy CTA band | 43 | 2 buttons |
| 30 | 389,000 | — | `.mobile-sticky-cta` | fixed bottom bar | 5 | 3 buttons |
| 31 | 389,600–410,400 | — | 7 × `<script type="application/ld+json">` | schema | — | — |
| 32 | 410,497 | `hub-blog-feed-heading` | **H2: New construction articles** (eyebrow "Read Next") | card grid | 112 | 3 blog cards |

### Notable structural quirks

- **Sections 9–25 are all inside ONE `<section style="padding:80px 0;background:var(--white)">`** with `<div class="container" style="max-width:820px">`. Every H2 is an `id`'d anchor inside a single long-form article container — not separate sections. This is what makes the sticky TOC work as an article outline.
- Every anchored H2 carries `scroll-margin-top:80px` inline (matching `html{scroll-padding-top:80px}`).
- Section 25 ("Why use Nevada Real Estate Group") is the only anchored-style H2 with **no `id`** and **no TOC entry**.
- Each submarket section (11–16) follows an identical 4-part sub-block pattern: *narrative intro → "Named master plans/villages…" → "Price tier reality." → "Who buys / Buyer fit."* Sub-headings are bolded `<strong>` lead-ins inside `<p>`, not real headings — so they never pollute the H2 outline or the TOC.

---

## 2. The sticky "On This Page" component (PRIORITY)

### 2.1 Actual HTML (verbatim, byte 292,885)

```html
<nav class="toc" aria-label="Table of contents">
  <h2 class="toc__title">On This Page</h2>
  <ol class="toc__list">
    <li><a href="#builders">Active builders in Las Vegas</a></li>
    <li><a href="#why-2026">Why new construction in 2026</a></li>
    <li><a href="#summerlin">Summerlin new construction</a></li>
    <li><a href="#henderson">Henderson new construction</a></li>
    <li><a href="#lake-las-vegas">Lake Las Vegas new construction</a></li>
    <li><a href="#sw-vegas">Southwest Las Vegas</a></li>
    <li><a href="#nlv">North Las Vegas</a></li>
    <li><a href="#nw-vegas">Northwest Las Vegas</a></li>
    <li><a href="#boulder-city">Boulder City</a></li>
    <li><a href="#launches-2026">2025-2026 launches</a></li>
    <li><a href="#builder-comparison">National vs regional builders</a></li>
    <li><a href="#price-by-submarket">Price by submarket</a></li>
    <li><a href="#new-vs-resale">New vs resale</a></li>
    <li><a href="#step-by-step">Buying step by step</a></li>
    <li><a href="#incentives">Builder incentives</a></li>
    <li><a href="#warranties">Warranties</a></li>
    <li><a href="#lot-premiums">Lot premiums</a></li>
    <li><a href="#faq">FAQ</a></li>
  </ol>
</nav>
```

**Exactly 18 links.** Note the link *labels* are short-form, not the H2 text (e.g. "Summerlin new construction" → H2 "What new construction is available in Summerlin?"). The TOC lives inside `<div class="container" style="max-width:820px">` in the *article-meta* section — i.e. it is placed in normal document flow and then *promoted* to a fixed right rail by CSS.

### 2.2 Actual CSS (from `/_next/static/chunks/0as0ckk54covc.css`)

**Base (mobile / tablet, in-flow):**
```css
.toc{
  background:var(--cream);
  border-left:2px solid var(--gold);
  margin:0 0 40px;
  padding:22px 26px;
}
.toc__title{
  font-family:var(--font-sans);
  letter-spacing:.14em;
  text-transform:uppercase;
  color:var(--gold-hover);
  margin:0 0 12px;
  font-size:11px;
  font-weight:700;
}
.toc__list{
  columns:2;                /* two-column list on tablet/desktop-in-flow */
  column-gap:28px;
  margin:0;
  padding-left:22px;
  list-style:decimal;       /* numbered 1–18 */
}
.toc__list li{break-inside:avoid;margin-bottom:6px}
.toc__list a{color:var(--navy);font-size:14px;line-height:1.6;text-decoration:none}
.toc__list a:hover{
  color:var(--gold-hover);
  text-decoration:underline;
  text-decoration-color:var(--gold);
}

@media (max-width:700px){
  .toc__list{columns:1}     /* collapses to single column on phone */
}
```

**Desktop promotion to fixed right rail — this is the whole trick:**
```css
@media (min-width:1024px){
  :is(body:has(.community-card) .toc, body:has(.nc-table) .toc){
    position:fixed;
    top:calc(var(--nav-h,72px) + 24px);   /* = 96px from viewport top */
    right:24px;
    width:250px;
    max-height:calc(100vh - var(--nav-h,72px) - 60px);
    overflow-y:auto;
    z-index:8;
    background:var(--cream);
    border-left:3px solid var(--gold);
    margin:0;
    padding:18px 20px;
    font-size:13px;
    box-shadow:0 4px 14px #0a0a0a0f;
  }
  :is(body:has(.community-card) .toc .toc__list, body:has(.nc-table) .toc .toc__list){
    columns:1;
    padding-left:18px;
  }
  :is(body:has(.community-card) .toc__list li, body:has(.nc-table) .toc__list li){margin-bottom:4px}
  :is(body:has(.community-card) .toc__list a, body:has(.nc-table) .toc__list a){font-size:13px;line-height:1.45}
}

/* Reserve gutter for the rail so body copy doesn't slide under it */
@media (min-width:1024px) and (max-width:1499px){
  :is(body:has(.community-card) main>section .container:not([style*=max-width]),
      body:has(.nc-table)      main>section .container:not([style*=max-width])){
    max-width:calc(100vw - 320px);
  }
}
```

### 2.3 Key facts to replicate

| Property | Value |
|---|---|
| Positioning | **`position: fixed`, NOT `position: sticky`.** Pinned to the viewport, right rail. |
| Activation | CSS `:has()` feature detection — the rail only turns on if the page body contains a `.nc-table` or `.community-card`. On pages without them, the TOC stays in flow as a 2-column cream box. |
| Desktop breakpoint | `min-width: 1024px` |
| Width | `250px` fixed; offset `right: 24px`; top `96px` (`--nav-h` 72px + 24px) |
| Max height | `calc(100vh - 72px - 60px)`, `overflow-y:auto` (self-scrolls if list overflows) |
| Mobile behaviour | Below 1024px it is **not** a dropdown, not collapsed, not sticky — it is an ordinary in-flow cream card near the top of the article, 2-column list. Below 700px → 1 column. |
| List style | `list-style: decimal` (numbered 1–18), gold left border 2px in-flow / 3px fixed |
| Scroll-spy | **NONE.** No active-link JS, no `IntersectionObserver` for the TOC, no `aria-current`, and no `.toc__list a.is-active` / `--active` CSS rule exists anywhere in the three stylesheets. Confirmed by grepping all 17 JS chunks for `toc` (zero hits) — the only `IntersectionObserver` in the bundle is Next.js `<Link>` prefetch. |
| Smooth-scroll offset | Handled purely in CSS: `html{scroll-padding-top:80px}` plus `scroll-margin-top:80px` inline on every anchored H2. No JS scroll handler. |
| Link hover | color → `--gold-hover` `#B89460`, underline with `text-decoration-color: var(--gold)` |

**Implication for a Lofty rebuild:** the entire component is HTML + CSS. Zero JS to port. The only fragile part is `body:has(...)` — in a Lofty page you would simply drop that guard and apply the fixed rule directly at `min-width:1024px`.

---

## 3. Hero section

Not a full-viewport hero. Fixed **420px tall** image band directly under the breadcrumb.

```html
<div class="breadcrumb"><div class="breadcrumb-inner">
  <a href="/">Home</a><span class="breadcrumb-sep">›</span><span>New Construction</span>
</div></div>

<section style="position:relative;height:420px;overflow:hidden">
  <!-- next/image fill, LCP-preloaded, sizes="100vw", 6 srcset widths 640→1920 -->
  <img alt="New construction homes in Las Vegas" data-nimg="fill"
       style="position:absolute;height:100%;width:100%;left:0;top:0;right:0;bottom:0;object-fit:cover;color:transparent"
       sizes="100vw"
       src="/_next/image/?url=%2Fimages%2Fpage-heroes%2Fnew-construction.jpg&w=1920&q=75"/>

  <!-- scrim -->
  <div style="position:absolute;inset:0;
              background:linear-gradient(to bottom, rgba(10, 10, 10,0.6), rgba(10, 10, 10,0.85))"></div>

  <div style="position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;
              justify-content:center;height:100%;text-align:center;padding:0 24px">
    <h1 style="font-family:var(--font-serif);font-size:clamp(32px, 4.5vw, 48px);
               color:var(--white);font-weight:400;margin-bottom:12px">
      New Construction Homes in Las Vegas
    </h1>
    <p style="color:rgba(255,255,255,0.8);font-size:17px;max-width:640px;margin-bottom:20px">
      73+ active communities · 18 builders · $290K–$10M · ~25 min read
    </p>
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:12px">
      <a href="#builders"        class="btn-gold">Browse Builders ↓</a>
      <a href="tel:+17026371759" class="btn-outline-light">Call (702) 637-1759</a>
      <a href="#lead-form"       class="btn-outline-light">Get Incentive List</a>
    </div>
  </div>
</section>
```

**Stat bar:** it is not a stat *bar* — it is a single `<p>` of middot-separated text. Four tokens: `73+ active communities · 18 builders · $290K–$10M · ~25 min read`. Colour `rgba(255,255,255,0.8)`, 17px, max-width 640px. Cheap to replicate, no grid, no counters.

**Background image handling:** `/images/page-heroes/new-construction.jpg` via Next Image `fill` + `object-fit:cover`, `<link rel="preload" as="image">` with the full 6-width srcset in `<head>` (LCP optimisation). Darkening scrim is a separate absolutely-positioned div with a top→bottom linear gradient `rgba(10,10,10,0.6)` → `rgba(10,10,10,0.85)`.

**CTA button CSS:**
```css
.btn-gold{
  background:var(--gold);color:var(--navy);border-radius:var(--radius-md); /* = 0 */
  letter-spacing:.04em;text-transform:uppercase;
  transition:background var(--transition), transform var(--transition);
  align-items:center;gap:8px;min-height:44px;padding:13px 28px;
  font-size:14px;font-weight:700;display:inline-flex;
}
.btn-gold:hover{background:var(--gold-hover);transform:translateY(-2px)}

.btn-outline-light{
  border:2px solid #fff9;color:var(--white);border-radius:var(--radius-md);
  backdrop-filter:blur(4px);letter-spacing:.02em;
  padding:14px 28px;font-size:15px;font-weight:600;display:inline-flex;
  justify-content:center;align-items:center;
}
.btn-outline-light:hover{border-color:var(--white);background:#ffffff26}
```

---

## 4. IDX / MLS listing section — the block to swap for Lofty

### 4.1 Provider & render mode

- **Provider: Repliers IDX** on top of the **GLVAR** MLS. Images served from `https://cdn.repliers.io/lasvegas/IMG-<mlsid>_<n>.jpg?class=large`, then proxied through Next's `/_next/image/` optimiser.
- **Server-rendered, not a client fetch.** All 36 `<article>` cards are in the initial HTML. No XHR/JSON hydration payload for listings, no third-party IDX iframe, no widget script. Copy states "Refreshes every 30 minutes" — i.e. ISR/cron revalidation on the server.
- Cards deep-link to first-party SEO detail pages: `/property/<slug>-<mlsid>/`.

### 4.2 Wrapper markup (exact)

```html
<section class="nc-live-section">
  <div class="container">
    <div class="nc-live-header">
      <span class="nc-live-eyebrow">Live MLS Feed · Updated Every 30 Min</span>
      <h2>Active New-Construction Homes For Sale Right Now</h2>
      <p class="nc-live-lede">187 active LV-metro new-construction listings — single-family homes
        built 2024 or later, plus spec/model/builder-inventory homes from earlier years. Refreshes
        every 30 minutes from the GLVAR MLS via Repliers IDX.</p>
      <p class="nc-live-meta">Scanned 289 listings across three new-construction signals
        (yearBuilt ≥ 2025, "new construction", "brand new") and post-filtered against the listing
        description to drop renovated older homes mentioning "brand new appliances" etc.
        Sorted by most recent update.</p>
    </div>

    <ul class="listing-grid" role="list">
      <li><article id="listing-card-2720672" data-mls="2720672" class="search-listing-card"> … </article></li>
      … 36 total …
    </ul>

    <p class="nc-live-attrib">Listing data sourced from GLVAR via Repliers IDX. Builder
      identification, spec versus model versus quick-move-in status, and current incentive packages
      vary — confirm with the listing detail page, the builder sales office, or your NREG agent
      before scheduling a tour. Information deemed reliable but not guaranteed.</p>
  </div>
</section>
```

Note the copy says **187 active listings** and **289 scanned**, but only **36 cards render** on the hub page (first page of results, no pagination control, no "view all" button in this block).

### 4.3 Section CSS (inlined in `<head>` as `data-href="rr-new-construction"`, precedence `high`)

```css
.nc-live-section { padding:56px 0 16px; background:var(--cream); border-bottom:1px solid var(--border-light); }
.nc-live-header  { max-width:880px; margin:0 auto 32px; }
.nc-live-eyebrow { display:inline-block; font-size:12px; letter-spacing:0.18em; text-transform:uppercase;
                   color:var(--gold-text,#B89968); font-weight:700; margin-bottom:12px; }
.nc-live-header h2 { font-family:var(--font-serif); font-size:clamp(28px,3.5vw,42px); color:var(--navy);
                   font-weight:400; margin:0 0 14px 0; line-height:1.1; }
.nc-live-lede    { font-size:16px; line-height:1.55; color:var(--text-secondary); margin:0 0 12px 0; max-width:70ch; }
.nc-live-meta    { font-size:12px; color:var(--text-faint,#8B8B8B); margin:0; max-width:78ch; }
.nc-live-attrib  { font-size:12px; color:var(--text-faint,#8B8B8B); margin-top:24px; line-height:1.55; max-width:78ch; }
.nc-live-empty   { padding:32px; text-align:center; background:var(--white);
                   border:1px solid var(--border-light); border-radius:12px; }
.nc-live-cta     { display:inline-block; padding:12px 24px; background:var(--gold,#D4B27C);
                   color:var(--navy); border-radius:999px; font-weight:700; font-size:14px; text-decoration:none; }
```

### 4.4 Grid + card dimensions (for the Lofty swap)

```css
.listing-grid{display:grid;grid-template-columns:minmax(0,1fr);gap:12px;margin:0;padding:0;list-style:none}
@media (min-width:500px) {.listing-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (min-width:800px) {.listing-grid{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (min-width:1700px){.listing-grid{grid-template-columns:repeat(4,minmax(0,1fr))}}

.search-listing-card{
  background:var(--white);border:1px solid #00000012;border-radius:8px;
  display:flex;flex-direction:column;position:relative;overflow:hidden;contain:layout;
  transition:transform .15s, box-shadow .15s, border-color .15s;
}
.search-listing-card:hover{border-color:#0000001a;transform:translateY(-2px);box-shadow:0 10px 28px #0000001a}

.search-card-image{aspect-ratio:4/3;width:100%;position:relative;background:#0000000a}
```

**Container:** the grid sits inside `.container` = `max-width:1200px; padding:0 24px`. Note the ≥1024px `:has()` rule shrinks `.container` to `calc(100vw - 320px)` up to 1499px to make room for the TOC rail — but this section's container is *not* exempt, so the IDX grid narrows on 1024–1499px screens too. Card border-radius **8px** (an exception — the site's `--radius-md/lg` are all `0`).

### 4.5 Card anatomy — every field rendered

Image well (`.search-card-image`, 4:3):
- `next/image` fill, `sizes="(max-width: 600px) 100vw, (max-width: 900px) 50vw, (max-width: 1440px) 33vw, 25vw"`
- prev/next photo arrows: `button.card-photo-arrow.card-photo-arrow-prev|next` (32px circle, `opacity:0` until card hover/focus-within)
- dot pager: `div.card-photo-dots` > `button.card-photo-dot` × 5 (first `.is-active`)
- badge stack: `div.search-card-badges` (absolute top:10px left:10px, column, gap 6px)
- photo count: `<span class="search-card-photocount">📷 99</span>`
- save heart: `button.card-save-heart` (SVG heart outline)

Body (`.search-card-body`):
- `.search-card-price-row` → `.search-card-price` (`$3,500,000`) + `.search-card-proptype` (dot + "House")
- `.search-card-monthly` — `Est. $19,762/mo`, `title="Estimated PITI — 20% down, 6.00% APR, 30-year fixed, taxes and insurance included"`
- `.search-card-statblock` — 4 `.stat-cell`s with Lucide icons: **Beds** (bed-double), **Baths** (bath), **Sq. Ft. + Acres** stacked (ruler), **Built in YYYY** (house)
- `.search-card-address-row` → `.search-card-address` (street) / `.search-card-city` (City, NV, ZIP) / `.search-card-subdivision` (subdivision or builder entity, e.g. "Custom Builds LLC") + `button.card-email-btn` "Email Agent"
- `button.card-tour-btn` "Tour this home" (full-width)

Footer (`.search-card-footer`):
- `.search-card-mls` — `MLS #2720672 · Listed 10 months ago`
- `.search-card-brokerage` — `Listing courtesy of Las Vegas Sotheby's Int'l`

Whole-card link: `<a class="search-card-stretched-link" aria-label="…, $3,500,000" href="/property/…/">` with an `.sr-only` span.

### 4.6 Badge inventory (actual counts across the 36 cards)

| Badge class | Label | Background | Count on page |
|---|---|---|---|
| `badge-new` | `NEW` | `#16a34a` | 18 |
| `badge-newconstruction` | `NEW CONSTRUCTION` | `#2563eb` | 17 |
| `badge-reduced` | `PRICE REDUCED $<amount>` (e.g. `$1.4k`, `$160k`, `$189k`) | `#16a34a` | 12 |
| `badge-openhouse` | `OPEN HOUSE` | *(defined elsewhere)* | 3 |
| `badge-pending` | `PENDING` | `#b45309` | 3 |
| `badge-active` | `ACTIVE` | `var(--navy)` | 0 (defined, unused here) |

```css
.search-card-badge{
  font-family:var(--font-mulish),sans-serif;letter-spacing:.06em;color:var(--white);
  text-transform:uppercase;white-space:nowrap;border-radius:999px;padding:5px 12px;
  font-size:11px;font-weight:700;line-height:1.2;display:inline-block;box-shadow:0 1px 3px #0000002e;
}
.search-card-badges{position:absolute;top:10px;left:10px;display:flex;flex-direction:column;
  align-items:flex-start;gap:6px;max-width:calc(100% - 20px);z-index:2}
@media(mobile){.search-card-badges{gap:4px;max-width:calc(100% - 8px);top:4px;left:4px}}
```

**Lofty swap note:** replace the whole `<ul class="listing-grid">…</ul>` with the Lofty IDX embed and keep `.nc-live-section` / `.nc-live-header` / `.nc-live-attrib` around it. The eyebrow + lede + methodology paragraph + attribution paragraph are the credibility-building parts and are pure static HTML.

---

## 5. Every table on the page (5 total, all `<table class="nc-table">`)

Shared CSS:
```css
.nc-table{border-collapse:collapse;width:100%;font-size:.9rem}
.nc-table thead{background:var(--navy);color:var(--white)}
.nc-table th,.nc-table td{border:1px solid var(--border-light);text-align:left;padding:10px 14px}
.nc-table th{font-size:.85rem;font-weight:600}
.nc-table td{color:var(--text-secondary)}
.nc-table tbody tr:nth-child(2n){background:var(--cream)}
.nc-table tbody tr:hover{background:#c9a96e14}
@media(mobile){.nc-table{font-size:.8rem}.nc-table th,.nc-table td{padding:6px 8px}}
```
Every table has a real `<caption>` (SEO/a11y win worth copying).

### Table 1 — `#launches-2026`
> **Caption:** Notable Las Vegas new-construction community launches 2025-2026 — builder, location, starting price, and status.

| Community | Builder | Location | Price From | Status |
|---|---|---|---|---|
| Ascension at Summerlin | Pulte / Toll Brothers | Summerlin | $1.2M | Selling (approaching sellout) |
| Meriden | KB Home | Henderson | Mid $300s | Opened April 2026 |
| Primrose Park | Richmond American | Summerlin (Cliffs) | $1.1M | Opened Dec 2025 |
| The Loughton | Toll Brothers | Summerlin | Low $500s | Opened Fall 2025 |
| Esplanade at Red Rock | Taylor Morrison | Summerlin | TBD | Opening Early 2026 |
| Malibu at Vista Cielo | Harmony Homes | North Las Vegas | Low $200s | Opened March 2026 |
| Topaz at Skye Canyon | LGI Homes | NW Las Vegas | Mid $300s | Opened Q4 2025 |
| Kyle Canyon Master Plan | Richmond American / Tri Pointe | NW Las Vegas | TBD | First approvals Jan 2025 |
| Wellston Ridge | StoryBook Homes | SW Las Vegas | Upper $400s | Opened April 2026 |
| Black Mountain Ranch | Lennar | Henderson | $345K | Actively selling (7 collections) |

### Table 2 — `#builder-comparison`
> **Caption:** National vs regional Las Vegas builders — price tiers, community counts, design center, and warranty structure (May 2026).

| Builder | Type | Price Range | Active Communities | Design Center | Warranty |
|---|---|---|---|---|---|
| Toll Brothers | National Luxury | $400K–$2.2M+ | 18 | Full Design Studio | 1/2/10 + extended |
| Lennar | National Volume | $277K–$1.28M | 50+ | Everything's Included | 1/2/10 |
| KB Home | National Volume | $317K–$883K | 28 | Built to Order studio | 1/2/10 + ENERGY STAR |
| D.R. Horton | National Entry | $308K–$822K | 17 | Standard selections | 1/2/10 |
| Blue Heron | Local Custom | $1.5M–$10M+ | 8 | Atelier full custom | Custom warranty |
| Harmony Homes | Local Entry | $200K–$471K | 4 | Standard selections | 1/2/10 |
| Touchstone Living | Local Entry | $305K–$471K | 5 | Standard selections | 1/2/10 |

### Table 3 — `#price-by-submarket`
> **Caption:** Las Vegas new construction pricing by submarket — entry / mid / luxury tiers (May 2026).

| Submarket | Entry (Townhome/SF) | Mid-Range (SF) | Luxury/Custom | Top Builder |
|---|---|---|---|---|
| Summerlin | $500K–$650K | $650K–$1.2M | $1.2M–$2.4M+ | Toll Brothers, Pulte |
| Henderson (Cadence/Inspirada) | $350K–$500K | $500K–$900K | $900K–$1.28M | Lennar, D.R. Horton |
| Lake Las Vegas | $400K–$600K | $600K–$1M | $1M–$15M+ | Blue Heron, Toll Brothers |
| Southwest Las Vegas | $350K–$500K | $500K–$750K | $750K–$1M+ | KB Home, Pulte |
| North Las Vegas | $200K–$400K | $400K–$600K | $600K–$800K | D.R. Horton, Harmony |
| NW (Sunstone/Skye Canyon) | $400K–$550K | $550K–$800K | $800K–$1.1M | Lennar, Woodside, Shea |
| Boulder City | N/A | N/A | $875K–$1.02M | Beazer |

### Table 4 — `#new-vs-resale`
> **Caption:** New construction vs resale — trade-offs across price, customization, warranty, energy, landscape, HOA, financing, and timeline.

| Factor | New Construction | Resale |
|---|---|---|
| Price premium | 10-15% per sq ft above comparable resale | Lower cost per sq ft |
| Customization | Full design center + structural options | Renovate after close |
| Warranty | 1/2/10 year (NRS 116B minimum) | None (unless transferable) |
| Energy efficiency | 30-50% more efficient than pre-2010 | Varies by age |
| Landscape | New — 3-5 years to mature | Established |
| HOA track record | Unknown (new community) | Years of financials to review |
| Financing | Builder incentives (rate buydowns, credits) | Standard market rates |
| Timeline | 6-14 months (build-to-order) | 30-45 day close |

### Table 5 — `#incentives`
> **Caption:** Current builder incentives in Las Vegas — May 2026. Incentives change monthly; contact builder or Nevada Real Estate Group for current numbers.

| Builder | Closing Cost Credit | Rate Buydown | Design Center Credit | Conditions |
|---|---|---|---|---|
| Lennar | $10K-$25K | 2/1 buydown | Included via "Everything's Included" | Preferred lender required for max |
| D.R. Horton | Up to $20K | 1% permanent | Standard package included | DHI Mortgage usage tied to top tier |
| KB Home | $15K-$30K | 2/1 or permanent | $5K-$15K studio credit | Contact builder for current |
| Pulte / Del Webb | $15K-$45K | 3/2/1 or permanent | $10K-$25K | Pulte Mortgage preferred |
| Toll Brothers | $10K-$30K | 1-2% permanent | $25K-$75K design credit | Highest design center allowance |
| Taylor Morrison | $15K-$35K | 2/1 buydown | $15K-$40K | Resort-lifestyle communities |
| Richmond American | $10K-$25K | 2/1 buydown | Studio credits | HomeAmerican Mortgage preferred |
| Tri Pointe Homes | $10K-$20K | 2/1 buydown | Contact builder | Inspirada / Cadence |
| Beazer Homes | $10K-$20K | Mortgage Choice flexible | Standard package | Lender flexibility unique to Beazer |
| Century Communities | $8K-$18K | 2/1 buydown | Contact builder | Inspire program |
| LGI Homes | Closing costs covered | Builder-paid points | Included finishes | No-haggle pricing model |
| Harmony / Touchstone / StoryBook | $10K-$15K | 2/1 buydown | Standard package | Local builder flexibility |

### Bonus — the 18 builder cards (`#builders`) rendered as data

Filter chips above the grid: `All (18)` `Entry (5)` `Mid (10)` `Luxury (1)` `Custom (2)` — pill buttons, `border-radius:20px`, active = navy fill. (No filter JS is server-rendered; the buttons are static in the initial HTML.)

| Builder | Parent / ticker | Price range | Communities | Tenure | Areas | Link |
|---|---|---|---|---|---|---|
| D.R. Horton | D.R. Horton, Inc. (NYSE: DHI) | $308K–$822K | 17 | 20+ yrs | NLV, Henderson, SW | /builders/dr-horton/ |
| Lennar | Lennar Corporation (NYSE: LEN) | $277K–$1.3M | 50 | 20+ yrs | Henderson, Lake LV, SW, NLV | /builders/lennar/ |
| KB Home | KB Home (NYSE: KBH) | $317K–$883K | 28 | 30+ yrs | Henderson, Summerlin, SW, NLV | /builders/kb-home/ |
| Pulte / Del Webb | PulteGroup, Inc. (NYSE: PHM) | $307K–$2.4M | 22 | 30+ yrs | Summerlin, Henderson, NLV, SW | /builders/pulte-del-webb/ |
| Toll Brothers | Toll Brothers, Inc. (NYSE: TOL) | $400K–$2.2M | 18 | 15+ yrs | Summerlin, Henderson, NW | /builders/toll-brothers/ |
| Taylor Morrison | Taylor Morrison Home Corp. (NYSE: TMHC) | $400K–$1.3M | 11 | 15+ yrs | Henderson, Summerlin, SW | /builders/taylor-morrison/ |
| Richmond American | M.D.C. Holdings / Sekisui House | $450K–$1.2M | 13 | 30+ yrs | Summerlin, Henderson, NW, SW | /builders/richmond-american/ |
| Tri Pointe Homes | Tri Pointe Homes (NYSE: TPH) | $466K–$1.1M | 15 | 30+ yrs (as Pardee) | Summerlin, Henderson, SW, NW | /builders/tri-pointe/ |
| Woodside Homes | — | $490K–$675K | 7 | 10+ yrs | Summerlin, Henderson, NW | /builders/woodside/ |
| Beazer Homes | Beazer Homes USA (NYSE: BZH) | $350K–$1M | 16 | 20+ yrs | Henderson, SW, NLV, Boulder City | /builders/beazer/ |
| Century Communities | Century Communities (NYSE: CCS) | $400K–$669K | 8 | 10+ yrs | NLV, Henderson | /builders/century-communities/ |
| LGI Homes | LGI Homes (NASDAQ: LGIH) | $290K–$450K | 4 | 10+ yrs | NLV, SW | /builders/lgi/ |
| Shea Homes | — | $399K–$705K | 1 | 20+ yrs | NW | /builders/shea/ |
| Blue Heron | — | $1.5M–$10M | 8 | 20+ yrs | Henderson, Summerlin, NW | /builders/blue-heron/ |
| Christopher Homes | — | $2M–$8M | 1 | 35+ yrs | Henderson | /builders/christopher/ |
| Harmony Homes | — | $200K–$471K | 4 | 15+ yrs | NLV | /builders/harmony/ |
| StoryBook Homes | — | $350K–$565K | 5 | 20+ yrs | Henderson, SW | /builders/storybook/ |
| Touchstone Living | — | $305K–$471K | 5 | 10+ yrs | NLV, SW | /builders/touchstone/ |

Builder card markup + CSS:
```html
<a class="nc-builder-card" style="text-decoration:none;color:inherit;display:block" href="/builders/dr-horton/">
  <div class="nc-builder-logo"><img src="/images/builder-logos/dr-horton.svg" alt="D.R. Horton logo" width="160" height="48"/></div>
  <h4 class="nc-builder-name">D.R. Horton</h4>
  <p class="nc-builder-parent">D.R. Horton, Inc. (NYSE: DHI)</p>
  <div class="nc-builder-stats"><span>$308K–$822K</span><span>17 communities</span><span>20+ years</span></div>
  <p class="nc-builder-strengths">America's largest homebuilder by volume. Express Homes sub-brand …</p>
  <div class="nc-builder-areas"><span class="nc-area-tag">North Las Vegas</span>…</div>
  <div class="nc-builder-links"><span class="nc-builder-link">View Builder Page →</span></div>
</a>
```
```css
.comm-hub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px}
.nc-builder-card{background:var(--white);border:1px solid var(--border-light);border-radius:var(--radius-lg);padding:24px;cursor:pointer;
  transition:border-color var(--transition),box-shadow var(--transition),transform var(--transition)}
.nc-builder-card:hover{border-color:var(--gold);box-shadow:var(--shadow-md);transform:translateY(-2px)}
.nc-builder-logo{height:40px;margin-bottom:12px}
.nc-builder-logo img{object-fit:contain;width:auto;height:100%}
.nc-builder-name{font-family:var(--font-serif);color:var(--navy);font-size:18px;margin-bottom:4px}
.nc-builder-parent{color:var(--text-faint);font-size:11px;margin-bottom:10px}
.nc-builder-stats span{background:var(--cream);border-radius:20px;padding:3px 10px;font-size:12px;color:var(--text-secondary)}
.nc-area-tag{background:#0a0a0a0f;border-radius:20px;padding:2px 10px;font-size:11px;font-weight:500;color:var(--navy)}
.nc-builder-link{color:var(--gold);font-size:13px;font-weight:600}
```
All 18 builder logos are local SVGs at `/images/builder-logos/<slug>.svg`, `<link rel="preload" as="image">`'d in `<head>`.

---

## 6. Lead-gen forms

### 6.1 Primary hub form — `#lead-form` (section bg `--cream`, container `max-width:700px`)

```html
<form class="nc-lead-form">
  <input type="hidden" name="source" value="new-construction-hub"/>
  <!-- honeypot, off-screen at left:-10000px -->
  <label for="website">Leave this field blank</label>
  <input type="text" id="website" name="website" tabindex="-1" autocomplete="off" value=""/>

  <h3>Get Builder Incentives &amp; Floor Plans</h3>
  <p>We'll send you the latest 2026 builder incentives, floor plans, and price sheets for
     communities matching your criteria. Free, no obligation.</p>

  <div class="nc-form-grid">
    <input required placeholder="First name" name="firstName"/>
    <input required placeholder="Last name"  name="lastName"/>
    <input type="email" required placeholder="Email" name="email"/>
    <input type="tel"   required placeholder="Phone" name="phone"/>
    <select name="area" required>…</select>
    <select name="budget" required>…</select>
    <select name="timeline" required class="nc-form-full">…</select>
    <textarea name="notes" rows="3" class="nc-form-full"
      placeholder="Anything specific? Builder preference, must-haves, etc."></textarea>
    <p class="sms-consent-note">…</p>
    <button type="submit" class="nc-form-full btn-gold">Send My Builder Match</button>
    <p class="nc-form-fine nc-form-full">By submitting you agree to be contacted by
      Nevada Real Estate Group. We never share your info.</p>
  </div>
</form>
```

**Fields (8 visible + 1 hidden + 1 honeypot):**

| Field | Name | Type | Required | Options |
|---|---|---|---|---|
| — | `source` | hidden | — | `new-construction-hub` |
| Leave this field blank | `website` | text (honeypot) | no | — |
| First name | `firstName` | text | yes | — |
| Last name | `lastName` | text | yes | — |
| Email | `email` | email | yes | — |
| Phone | `phone` | tel | yes | — |
| Preferred area | `area` | select | yes | Summerlin · Henderson · Southwest Las Vegas · North Las Vegas · Lake Las Vegas · Boulder City · Northwest / Skye Canyon · Open to all areas |
| Budget | `budget` | select | yes | Under $400K · $400K–$600K · $600K–$800K · $800K–$1.2M · $1.2M–$2M · $2M+ |
| Timeline | `timeline` | select (full width) | yes | Within 30 days · 1–3 months · 3–6 months · 6–12 months · Just researching |
| Notes | `notes` | textarea rows=3 (full width) | no | — |

Submit label: **"Send My Builder Match"**.

**Consent copy (verbatim, `.sms-consent-note`):**
> By submitting this form, you agree that Nevada Real Estate Group, Chris Nevada, and LPT Realty (the brokerage of record), and their agents, may contact you at the phone number and email you provide about your real estate inquiry — including by automated or auto-dialed telephone calls, prerecorded or artificial-voice messages, and text messages (SMS/MMS) — even if your number is on a state or federal Do-Not-Call list, and that your phone number is your account sign-in. Message and data rates may apply; reply STOP to opt out of texts. Consent is not a condition of any purchase or service, and you may ask us to stop contacting you at any time. See our [Terms of Use](/terms-of-use/) and [Privacy Policy](/privacy-policy/).

Fine print under the button:
> By submitting you agree to be contacted by Nevada Real Estate Group. We never share your info.

Form CSS:
```css
.nc-form-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.nc-form-full{grid-column:1/-1}
.nc-form-grid input,.nc-form-grid select,.nc-form-grid textarea{
  border:1px solid var(--border-light);border-radius:var(--radius-md);
  font-size:15px;font-family:var(--font-sans);color:var(--navy);padding:12px 16px}
.nc-form-grid input:focus,…{outline:2px solid var(--gold);border-color:var(--gold)}
.nc-form-fine{color:var(--text-faint);font-size:11px;margin-top:4px}
@media(mobile){.nc-form-grid{grid-template-columns:1fr}}
/* success state */
.nc-form-success{border:1px solid var(--gold);text-align:center;background:#c9a96e1a;padding:32px}
```

### 6.2 Site-wide modal form — `<dialog class="ccm">` (rendered at end of body, sits outside `<main>`)

`action="/api/leads/buyer/" method="POST"` — the real lead endpoint.

- Eyebrow: **Talk to a Local Vegas Area Specialist**
- Headline: **No pressure. No spam.<br>Just answers from Nevada's #1 team.**
- Sub: *Tell us a little about what you're looking for. We'll respond in under 1 hour.*
- Fields: honeypot `website`, hidden `source`, `firstName` (ph "Jane"), `lastName` (ph "Doe"), `email` (ph "you@email.com"), `phone`, `timeline` select — options: `0–3 months — ready to buy` / `3–6 months — actively looking` / `6–12 months — researching` / `12+ months — just exploring` / `I'm selling, not buying`
- Submit: **Send →** · alt: "or call (702) 637-1759"
- Trust line: `★★★★★ 9,061+ Reviews · #1 Team in Nevada · 9,600+ Homes Sold · No spam · Reply in 1 hr`
- Same `sms-consent-note` copy as above
- Footer: `⚖ Equal Housing Opportunity · Typical response time: under 30 minutes during business hours (Mon–Sun 8a–8p PT)`

### 6.3 Mobile sticky CTA bar (3rd conversion surface)

```html
<div class="mobile-sticky-cta" aria-label="Quick contact options">
  <a href="tel:+17026371759" class="msc__btn msc__btn--call">📞 Call</a>
  <a href="sms:+17026371759" class="msc__btn msc__btn--text">💬 Text</a>
  <a href="#lead-form"       class="msc__btn msc__btn--cta">Get Incentive List →</a>
</div>
```
```css
.mobile-sticky-cta{position:fixed;bottom:0;left:0;right:0;display:none;
  grid-template-columns:1fr 1fr 2fr;background:var(--navy);border-top:1px solid var(--line-dark);
  z-index:100;padding-bottom:env(safe-area-inset-bottom);box-shadow:0 -4px 16px #0a0a0a33}
@media (max-width:1023px){.mobile-sticky-cta{display:grid}
  body:has(.mobile-sticky-cta) main{padding-bottom:70px}}
.mobile-sticky-cta .msc__btn{height:60px;color:var(--cream);font-size:13px;font-weight:700;
  text-transform:uppercase;letter-spacing:.04em;border-right:1px solid var(--line-dark);
  display:flex;justify-content:center;align-items:center;gap:8px}
.mobile-sticky-cta .msc__btn--cta{background:var(--gold);color:var(--navy)}
```
Same 1024px breakpoint as the TOC rail — **on desktop you get the TOC rail, on mobile you get the sticky CTA bar.** Neat trade-off.

---

## 7. FAQ block — `#faq`

**It is NOT an accordion.** All 12 answers are always visible. No `<details>`, no `<summary>`, no toggle JS, no `.faq-answer` class on this page (the site's stylesheet *does* ship `.faq-item.open`, `.faq-item-blog[open] .faq-summary:after{content:"+"}` accordion styles, but the hub page doesn't use them).

Markup pattern (repeated 12×, all inline-styled):
```html
<section id="faq" style="padding:80px 0;background:var(--white)">
 <div class="container">
  <div class="section-header" style="text-align:center;margin-bottom:48px">
    <span class="section-label">Common Questions</span>
    <h2 style="font-family:var(--font-serif);font-size:var(--text-xl);font-weight:400;color:var(--navy)">
      Frequently Asked Questions</h2>
  </div>
  <div class="faq-list" style="max-width:780px;margin:0 auto">
    <div class="faq-item" style="border-bottom:1px solid var(--border)">
      <div style="padding:22px 0">
        <h3 style="font-size:var(--text-base);font-weight:500;color:var(--navy);line-height:1.4;margin-bottom:10px">
          What builder incentives are currently available in Las Vegas?</h3>
        <p style="font-size:var(--text-sm);color:var(--text-secondary);line-height:1.75">…answer…</p>
      </div>
    </div>
    … ×12 …
  </div>
 </div>
</section>
```

**All 12 questions verbatim (H3s, in order):**
1. What builder incentives are currently available in Las Vegas?
2. How long does it take to build a new home in Las Vegas?
3. Can I customize a new construction home in Las Vegas?
4. What are lot premiums and are they negotiable?
5. Is new construction or resale a better value in Las Vegas?
6. What warranty coverage comes with a new home in Nevada?
7. Do I need a buyer's agent for new construction?
8. What is the average lot premium for a Summerlin home in 2026?
9. Can I use my own lender or do I have to use the builder's preferred lender?
10. How much should I budget for design center upgrades?
11. What 2025-2026 communities just opened in Las Vegas?
12. Are new construction homes in Boulder City a good investment?

Answer lengths: 49–73 words each (mean ~60). Each answer ends with either a concrete number range or a soft CTA to contact NREG.

**FAQPage schema: YES** — all 12 Q&A pairs are mirrored 1:1 in a `FAQPage` JSON-LD block (the JSON-LD answer text is identical to the visible `<p>` text). See §8.

---

## 8. Schema.org / JSON-LD — 7 blocks

All 7 sit together after the navy CTA band (byte ~389,600–410,400).

| # | `@type` | Contents |
|---|---|---|
| 1 | **BreadcrumbList** | 2 ListItems: Home → New Construction |
| 2 | **CollectionPage** | name "New Construction Homes in Las Vegas", description, url, image (`/og/new-construction.jpg`), `datePublished 2026-01-15T08:00:00-08:00`, `dateModified 2026-05-13T18:00:00-07:00`, author Person "Chris Nevada", publisher Organization + ImageObject logo |
| 3 | **FAQPage** | `mainEntity`: 12 × Question / acceptedAnswer Answer — verbatim match to visible FAQ |
| 4 | **RealEstateAgent** | `@id` `…/#realestateagent`, name, url, logo, image, `telephone +17026371759`, `email info@NevadaGroup.com`, `priceRange "$$"`, PostalAddress (8945 W Russell Rd Suite 170, Las Vegas NV 89148), GeoCoordinates (36.0879, -115.2952), hasMap, OpeningHoursSpecification (Mon–Sun 08:00–20:00), areaServed 5 × City (Las Vegas, Henderson, Summerlin, North Las Vegas, Boulder City), hasCredential (Real Estate License S.181401, red.nv.gov), founder Person Chris Nevada, **AggregateRating 4.9 / 9061 reviews**, sameAs (site, FB, IG, YouTube) |
| 5 | **ItemList** | `numberOfItems` = 18, 18 × ListItem → Organization (builder name, url `/builders/<slug>/`, image = logo SVG, sameAs = builder's own site, areaServed City) |
| 6 | **Article** | headline "New Construction Homes in Las Vegas: 18 Builders, 73+ Communities, $290K–$10M (2026)", description, datePublished/dateModified (same as CollectionPage), 2 images, author Person Chris Nevada with `worksFor` RealEstateAgent + `knowsAbout` [Las Vegas Real Estate, New Construction Homes, Builder Incentives, Master-Planned Communities, Buyer Representation] + hasCredential, publisher Organization (logo 105×60), mainEntityOfPage WebPage, **`speakable` SpeakableSpecification `cssSelector: [".direct-answer-block", ".faq-answer"]`** |
| 7 | **HowTo** | name "How to buy a new-construction home in Las Vegas", `totalTime "P90D"`, 2 × HowToSupply (pre-approval, buyer's-agent representation), **6 × HowToStep** each with `name`, `text`, and `url` pointing at `…/new-construction#step-by-step`. Steps mirror the `#step-by-step` section 1:1 |

Also present but non-schema: `<link rel="alternate" type="text/plain" href="/llms.txt">` and `/llms-full.txt` (AI-crawler feeds), plus `<link rel="manifest" href="/manifest.webmanifest">`.

**Doubling up CollectionPage + Article on the same URL is deliberate** — CollectionPage for the IDX/builder-listing half, Article for the 7,400-word editorial half.

---

## 9. Meta / SEO

| Element | Value |
|---|---|
| `<title>` | `New Construction Homes Las Vegas \| 18 Builders` (48 chars) |
| `meta description` | `Browse 73+ new construction communities in Summerlin, Henderson, SW Vegas & more. 18 active builders, $290K–$10M. Builder incentives + floor plans.` (147 chars) |
| `canonical` | `https://www.nevadarealestategroup.com/new-construction/` (trailing slash) |
| `hreflang` | `en-US` and `x-default` both → the canonical URL |
| `robots` | `index, follow` |
| `googlebot` | `index, follow, max-image-preview:large, max-snippet:-1` |
| `og:title` | `New Construction Homes Las Vegas — 18 Builders` |
| `og:description` | `Find your new home in Summerlin, Henderson, Southwest Vegas, North Las Vegas, Lake Las Vegas, Boulder City. Builder incentives, floor plans, price comparisons.` |
| `og:url` | `https://www.nevadarealestategroup.com/new-construction/` |
| `og:site_name` | `Nevada Real Estate Group` |
| `og:locale` | `en_US` |
| `og:type` | `website` |
| `og:image` | `https://www.nevadarealestategroup.com/og/new-construction.jpg` (1200×630, alt "Las Vegas new construction homes") |
| `twitter:card` | `summary_large_image` |
| `twitter:title` | `New Construction Homes Las Vegas \| 18 Builders` |
| `twitter:description` | `Browse 73+ new construction communities. 18 active builders. $290K–$10M.` |
| `twitter:image` | same OG image |
| PWA meta | `mobile-web-app-capable yes`, `apple-mobile-web-app-title NREG`, `apple-mobile-web-app-status-bar-style default` |
| **H1 (one only)** | `New Construction Homes in Las Vegas` |
| H2 count in body | 22 (excl. nav/footer) |
| H3 count in body | 16 (12 FAQ + form + 3 blog cards) |
| H4 count | 18 (builder card names) |
| GTM | `GTM-W9BG6VB9` |

**SEO pattern worth stealing:** every submarket H2 is phrased as a natural-language question ("What new construction is available in Summerlin?"), and the 4 comparison H2s are also questions ("How do national and regional Las Vegas builders compare?"). The TOC labels are the *short* keyword form. The `#why-2026` section stacks **eight** "According to the [authority]…" outbound citations (Clark County Building & Fire, US Census NRC, FRED 30-yr mortgage, BLS Las Vegas MSA, John Burns RE Consulting, Zonda, HUD, RCLCO) — heavy E-E-A-T signalling.

---

## 10. Design tokens

The whole theme is one `:root` block (also inlined in `<head>` in abbreviated form for anti-FOUC).

### Colors
| Token | Hex | Use |
|---|---|---|
| `--navy` | `#2B221A` | primary dark (it is a warm dark brown, not navy) |
| `--navy-deep` | `#1A1410` | deepest |
| `--navy-light` | `#3A3025` | hover on dark |
| `--gold` | `#D4B27C` | primary accent / CTA fill |
| `--gold-hover` | `#B89460` | accent hover, TOC title colour |
| `--gold-light` | `#E8D4B0` | hero italic highlights |
| `--gold-text` | `#7A5B2A` | accessible gold for small text/eyebrows |
| `--white` | `#FFFFFF` | |
| `--cream` | `#F7F4EE` | alternating section bg, TOC bg |
| `--cream-warm` | `#EDE7DA` | |
| `--text-primary` / `--ink` | `#0A0A0A` | |
| `--text-secondary` / `--ink-muted` / `--text-faint` | `#4A4A4A` | body copy |
| `--border` / `--border-light` / `--line` | `#E8E2D6` | |
| `--line-dark` | `#2A2A2A` | |
| `--stone` | `#7A7368` | |
| `--brand-rust` / hover | `#9C5F4E` / `#7A4A3D` | |
| `--positive` / `--success` | `#3D6B4A` | |
| `--urgency` / `--urgency-soft` | `#E63946` / `#FCE5E8` | |
| `--success-soft` | `#E4EDE7` | |
| `--surface-dark` | `#0A0A0A` | |
| `--charcoal` | `#211913` | |
| `--border-dim` | `#D4B27C2E` | |
| Badge colours (IDX) | new/reduced `#16A34A`, pending `#B45309`, new-construction `#2563EB` | |

### Typography
| Token | Stack |
|---|---|
| `--font-serif` | `'Cormorant Garamond', Georgia, serif` — **all H1/H2/H3 headings** |
| `--font-sans` | `'Inter', 'Helvetica Neue', Arial, sans-serif` — eyebrows, TOC title, form inputs |
| `--font-body` | `var(--font-barlow), system-ui, sans-serif` — `<body>` default, line-height 1.6 |
| `--font-cond` | `var(--font-barlow-cond), 'Arial Narrow', sans-serif` |
| `--font-ui` | `var(--font-roboto), system-ui, sans-serif` |
| also loaded | Libre Caslon Display, Mulish (badge font), Fraunces, JetBrains Mono |

Fluid type scale (all `clamp()`):
```
--text-xs   clamp(.75rem,  .7rem  + .25vw,  .875rem)    12→14px
--text-sm   clamp(.875rem, .8rem  + .35vw,  1rem)       14→16px
--text-base clamp(1rem,    .95rem + .25vw,  1.125rem)   16→18px
--text-lg   clamp(1.125rem,1rem   + .75vw,  1.5rem)     18→24px
--text-xl   clamp(1.5rem,  1.2rem + 1.25vw, 2.25rem)    24→36px   ← every section H2
--text-2xl  clamp(2rem,    1.2rem + 2.5vw,  3.5rem)     32→56px
```
Body line-height 1.6; long-form paragraphs `line-height:1.8`; FAQ answers `1.75`; measure capped at `max-width:70ch` / `78ch` on lede and meta text.

### Radius — the anti-generic move
```
--radius:0  --radius-sm:2px  --radius-md:0  --radius-lg:0  --radius-xl:0
```
**Square corners everywhere by default.** Exceptions that hard-code a radius: IDX listing cards `8px`, badges/chips/pills `999px` (fully round), builder stat pills `20px`, `.nc-live-empty` `12px`. Buttons (`.btn-gold`, `.btn-outline-light`) use `--radius-md` = **0**, i.e. hard rectangles.

### Shadows
```
--shadow-sm    0 1px 3px  rgba(10,10,10,.04)
--shadow-md    0 4px 16px rgba(10,10,10,.08)
--shadow-lg    0 12px 40px rgba(10,10,10,.12)
--shadow-card  0 2px 8px  rgba(10,10,10,.04)
--shadow-hover 0 8px 24px rgba(10,10,10,.08)
--shadow-deep  0 20px 60px rgba(10,10,10,.12)
TOC rail:      0 4px 14px rgba(10,10,10,.06)
IDX card hover:0 10px 28px rgba(0,0,0,.10)
mobile CTA bar:0 -4px 16px rgba(10,10,10,.20)
```
All neutral-tinted, low opacity. No coloured shadows except the `is-hovered` map-sync state (`0 10px 30px #c9a96e4d`).

### Layout & spacing
| Token / rule | Value |
|---|---|
| `--container` | `1240px` (variable) — but the actual class is `.container{width:100%;max-width:1200px;margin:0 auto;padding:0 24px}` |
| Long-form article container | inline `max-width:820px` (and `880px` for the direct-answer + IDX header blocks) |
| FAQ list | `max-width:780px` |
| Lead form | `max-width:700px` |
| Blog feed | `max-width:1080px` |
| `--nav-h` | `72px` |
| `--transition` | `.2s ease` |
| Section vertical rhythm | `80px 0` (major), `64px 0` (blog feed), `56px 0 16px` (IDX), `40px 0` / `36px 0 0` / `32px 0` (connective tissue) |
| H2 spacing inside article | `margin:48px 0 20px` + `scroll-margin-top:80px` |
| Paragraph gap | `margin-bottom:16px` |
| Grid gaps | IDX `12px`, builder cards `10px`, form `12px`, blog `24px`, hero CTAs `12px` |
| `html` | `font-size:16px; overflow-x:clip; scroll-padding-top:80px` |

### Breakpoints in use
`500px` (IDX 2-col) · `700px` (TOC 1-col) · `720px` (hero mobile) · `768px` (misc) · `800px` (IDX 3-col) · **`1023/1024px` (TOC rail on ↔ mobile CTA bar on)** · `1499px` (container gutter reservation ends) · `1700px` (IDX 4-col).

---

## 11. Direct-answer / AI-optimisation blocks (worth copying wholesale)

Three separate "answer engine" surfaces stacked before the TOC:

**(a) `blockquote.direct-answer`** — inline-styled, `background:rgba(212,178,124,0.08)`, `border-left:3px solid var(--gold)`, 17px/1.65:
> New construction in the Las Vegas valley delivered approximately 12,500 single-family units in 2025 — the highest annual volume since 2007. Twelve major national builders are active (Lennar, KB Home, Pulte/Del Webb, Toll Brothers, D.R. Horton, Richmond American, Taylor Morrison, Tri Pointe, Century Communities, Beazer, Shea, LGI) plus regional luxury builders (Blue Heron, Christopher Homes, Woodside, Harmony, Storybook, Touchstone). The most active master plans for new construction in 2026 are Inspirada, Cadence, Skye Canyon, Tule Springs, Stonebridge, Redpoint, and Kestrel. Builders are offering rate buydowns of $20-50K and closing cost credits of $10-25K through 2026.

**(b) `ul.key-takeaways`** — 6 bullets, `background:var(--cream)`, `border-left:3px solid var(--gold)`, custom `›` glyph markers in `--gold-text`:
- 12,500+ single-family new-builds delivered in 2025 — highest since 2007.
- 18 active builders in the valley; 12 national + 6 regional luxury.
- Most active 2026 master plans: Inspirada, Cadence, Skye Canyon, Tule Springs.
- Builder concessions in 2026 average $30-60K (rate buydowns + closing credits + upgrades).
- SID/LID assessments typically add $300-$3,200/year per home — verify before signing.
- VA loans close in 30-45 days on new construction — same as conventional.

**(c) `section.direct-answer-block`** — the `speakable` target in the Article schema:
> Las Vegas has **18 active new-construction home builders** across **73+ communities**, with prices ranging from **$290,000 to over $10 million** as of May 2026. Top-volume builders include Lennar, D.R. Horton, KB Home, and Pulte/Del Webb; luxury and custom builders include Toll Brothers, Blue Heron, and Christopher Homes. The most active submarkets are Summerlin, Henderson, Southwest Las Vegas, and North Las Vegas. Buyers can use a Nevada-licensed buyer's agent at no additional cost — builder pricing does not change whether or not you bring representation.

**Article meta strip** between (b) and (c):
```html
<div class="article-meta">
  <span class="meta-author">By <a href="/about/">Chris Nevada</a>, Owner · NV S.181401</span>
  <span class="meta-divider">·</span>
  <span class="meta-date">Published <time dateTime="2026-01-15T08:00:00-08:00">January 15, 2026</time></span>
  <span class="meta-divider">·</span>
  <span class="meta-date">Updated <time dateTime="2026-05-13T18:00:00-07:00">May 13, 2026</time></span>
  <span class="meta-divider">·</span>
  <span class="meta-readtime">25 min read</span>
</div>
```

---

## 12. Internal linking

**"New Construction by City" pill row** (section 7) — 5 spoke pages:
`/henderson/new-construction/` · `/summerlin/new-construction/` · `/north-las-vegas/new-construction/` · `/centennial-hills/new-construction/` · `/enterprise/new-construction/`
Pill style: `padding:9px 18px; border:1px solid var(--border); border-radius:999px; background:var(--white); font-size:14px`.

**18 builder hub pages:** `/builders/<slug>/`.

**In-copy blog links** (contextual, `color:var(--navy);text-decoration:underline`):
`/blog/las-vegas-home-prices-2026-up/` · `/blog/vegas-new-build-700k-vs-summerlin-2026/` · `/blog/nevada-hoa-fines-your-nrs-116/` · Henderson top-5 guide · Lake Las Vegas community guide · Mountain's Edge community guide · Skye Canyon guide · Trilogy Sunstone 55+ guide · Las Vegas construction boom analysis · Las Vegas home costs breakdown · Las Vegas homebuilder sales analysis · Las Vegas property tax guide.

**"Read Next" feed** — 3 cards, `grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px`, each card `background:var(--cream); border-left:3px solid var(--gold)`, 16:9 image (`padding-bottom:56.25%`):
1. New Construction Incentives in Las Vegas: May 2026 Builder Roundup
2. Best Real Estate Agent for New Construction in Las Vegas: Your 2026 Guide to Builder Negotiations and Expert Representation
3. Inspirada's Final 75 Homes: Last Window to Buy New in South Henderson (2026)

---

## 13. Rebuild checklist for Rose Homes LV (Lofty)

1. **Anchor architecture first.** One long container (`max-width:820px`), 15–18 `id`'d H2s phrased as questions, `scroll-margin-top:80px` on each.
2. **TOC rail is pure CSS** — copy §2.2 verbatim, drop the `body:has()` guard, keep the 1024px breakpoint and 250px/right:24px geometry. No JS needed. Optionally add scroll-spy (NRG has none — an easy differentiator).
3. **Reserve the gutter** with the `max-width:calc(100vw - 320px)` rule at 1024–1499px or the rail will overlap copy.
4. **Swap `<ul class="listing-grid">` for the Lofty IDX embed**, keeping `.nc-live-section` header (eyebrow / H2 / lede / methodology paragraph) and `.nc-live-attrib` disclaimer as static HTML around it. Container = `.container` at 1200px, cards ~4:3, 8px radius, gap 12px.
5. **Ship all 5 tables with `<caption>`s** — they are the highest-density "quotable answer" surface for AI search.
6. **Three schema blocks minimum:** FAQPage (mirroring visible answers verbatim), Article (with `speakable` cssSelector), HowTo (6 buying steps). Add BreadcrumbList + RealEstateAgent + ItemList if building builder pages.
7. **Mirror the 1024px trade-off:** TOC rail on desktop, 3-button sticky CTA bar (Call / Text / Get list) on mobile.
8. Content targets: ~7,400 editorial words, 12 FAQs at 50–70 words each, 6-bullet key-takeaways, one direct-answer paragraph, 8+ authoritative outbound citations.
9. **Workspace rule reminder:** NRG's copy is full of em-dashes. Rose Homes LV content must use commas/periods/"and" instead.

---

*Raw HTML: `/private/tmp/.../scratchpad/nc-hub.html`. Stylesheets pulled from `/_next/static/chunks/0_nc1eonl2f1h.css`, `0as0ckk54covc.css`, `0uyhgk7_6scb-.css`; all 17 JS chunks grepped for TOC/scroll-spy logic (none found).*
