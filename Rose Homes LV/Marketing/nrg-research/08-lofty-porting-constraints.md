# Porting Constraints — NRG page → Rose Homes LV on Lofty

Findings from Ryan's existing `new-construction` skill templates
(`~/.claude/skills/new-construction/landing-page-template.md`,
`landing-page-developer.md`). These constrain how much of the NRG page we can copy
1:1, and they need to be settled **before** anyone writes the hub HTML.

---

## 1. HARD CONSTRAINT — no inline `<form>` element

From `landing-page-template.md:435` and `landing-page-developer.md:181`:

> Lofty doesn't ingest leads from in-embed forms.

Ryan's established pattern:
- The landing page is an **HTML embed** pasted into the Lofty landing-page builder.
- Lofty's own **form block is appended below the embed** at publish time.
- CTAs inside the embed use `href="#contact"`, and page JS rewrites those clicks to
  scroll to the bottom of the document, landing the user on the Lofty form.

### Impact on the NRG clone
NRG's hub has a rich inline lead form — "Get Builder Incentives & Floor Plans" with
area dropdown, budget tier, timeline, phone, email. **We cannot reproduce it inline.**

Options:
| Option | Trade-off |
|---|---|
| **A. Lofty form below embed** (Ryan's current pattern) | Safe, leads ingest correctly. Loses the mid-page form and the qualifying fields. |
| **B. Multiple `#contact` CTA buttons** through the page, all scrolling to the one Lofty form | Keeps NRG's "CTA every 2 sections" rhythm without an inline form. **Recommended.** |
| **C. Inline form posting to Lofty API/webhook** | Matches NRG exactly, but is net-new plumbing and contradicts the existing skill rule. |

**Recommendation: B.** It preserves the conversion *rhythm* of the NRG page — which is
the part that actually matters — while staying inside the known-good Lofty pattern.

---

## 2. OPEN QUESTION — how the Lofty IDX feed actually embeds

Ryan's brief: *"it has listings in there that i can insert the idx feed from my lofty
html page."*

**No existing IDX embed snippet was found anywhere** in `~/.claude/skills/new-construction/`
or in `Rose Homes LV/`. Every current landing page is static HTML with no live listings.

So this is genuinely unsolved and is the **single biggest unknown** in the build. We need
from Ryan one of:
- the IDX embed/iframe snippet Lofty gives him, or
- the URL of a Lofty page of his that already renders an IDX feed, or
- confirmation that the feed only exists on Lofty-native pages (not inside an HTML embed)

**Why it matters:** if Lofty IDX cannot render inside a custom HTML embed, the whole
architecture changes — the hub would have to be a Lofty-native page with limited styling,
or the listing section becomes a styled *link-out* to a filtered Lofty search URL rather
than an inline grid.

**Fallback if inline IDX is impossible:** replicate NRG's listing section as a static
"featured communities" grid plus a prominent button to a pre-filtered Lofty search
(e.g. new-construction filter, price band, area). Visually similar, no live data.

### CONFIRMED (Agent F): there is nothing to copy. We must build the slot ourselves.

NRG consumes the **Repliers API (GLVAR MLS) server-side only**, inside a custom Next.js
app. There is **no widget, no iframe, no client-side fetch** — the API key never reaches
the browser. Evidence Agent F found:
- images served from `cdn.repliers.io/lasvegas/...`
- a `[repliers] build-time MLS fetches skipped` warning left in the shipped bundle
- Repliers field names in the markup (`details.numBedrooms`, `numBathroomsHalf`)
- their misspelled `priceDsc` sort enum

Their listing shell, for sizing our slot:
```
main.nreg-search-page[data-view]
  └ section.search-results-section
      └ ul.listing-grid
          └ li
              └ article.search-listing-card[data-mls]
```
Grid: 1 / 2 / 3 / 4 columns at 500 / 800 / 1700px. Images 4:3, 8px radius.

**Implication:** their approach is not portable to Lofty at all. Their listings are true
SSR output of a paid MLS API inside their own app. On Lofty we only get whatever embed
Lofty itself provides. So the decision tree is:

1. **If Lofty IDX renders inside an HTML embed** → drop it into a `ul.listing-grid`-shaped
   slot in the same page position (right after the hero, before the builder grid).
2. **If it does not** → the listings section becomes a styled block of 6–9 static
   "featured community" cards plus a prominent button to a pre-filtered Lofty search URL.
   Visually equivalent, no live data, zero MLS cost.

**Still blocked on Ryan for the Lofty IDX snippet.** Everything else in the build can
proceed without it, so this does not hold up the hub.

### QA refinement — the IDX dependency is narrower than feared

Per `07-qa-verification.md`, an MLS grid is needed on **only 3 page types**: the hub, the
geo sub-hubs, and the MLS-backed lifestyle pages. **Community, builder and editorial
lifestyle templates carry no MLS grid at all**, server-side or client-side.

**Therefore the 20 P1 builder pages are NOT blocked on the Lofty IDX question** and can be
built and shipped immediately. That materially de-risks the schedule.

---

## 2b. RESOLVED — `position:fixed` works in Lofty. Confirmed from shipped pages.

**Status: no longer a risk.** Evidence from Ryan's own already-published Lofty landing page
`Rose Homes LV/Content/New-Construction/arroyo-at-skyeview/landing-page.html`:

```css
.header  { position: fixed; top:0; left:0; right:0; z-index:1000; }   /* line 127 */
.lightbox{ position: fixed; inset:0; z-index:9999; }                  /* line 528 */
```

Both ship live on Lofty and render correctly, so Lofty's wrapper does **not** apply a
`transform`/`filter`/`contain` that would break fixed positioning. **The sticky TOC rail is
safe to build.**

**`:has()` is still untested (0 usages in any shipped page), but we simply do not need it.**
The competitor used `body:has(.nc-table) .toc` only to conditionally enable the rail across
different page templates. We control our own single page, so we put a plain class on the
container:

```css
/* Do NOT copy the competitor's body:has() selector. Use a direct class. */
@media (min-width: 1024px) {
  .nc-hub .toc { position: fixed; right: 24px; top: 96px; width: 250px; }
}
```
Zero `:has()` dependency, zero risk.

**Two more confirmations from the same shipped file:**
1. **Flat root slugs are the live pattern** — that page publishes to
   `https://rosehomeslv.com/arroyo-at-skyeview`. Confirms Ryan's "no nested pages" and
   settles the slug question: `/new-construction`, `/henderson-new-construction`, etc.
2. **The `#contact` scroll pattern is already implemented** — `scrollToContact()` at
   line 1191 binds every `#contact` anchor. Reuse it verbatim rather than reinventing.

---

## 2c. (superseded) original risk write-up

The entire sticky-TOC design rests on two CSS features inside a Lofty embed:
- `position: fixed` — Lofty may wrap embeds in a container with `transform`, `filter`, or
  `contain`, **any of which silently breaks `position:fixed`** (it would anchor to the
  wrapper instead of the viewport).
- `:has()` — supported in all current browsers, but if Lofty sanitizes or rewrites CSS the
  selector could be stripped.

**This is the #1 technical unknown in the build and it is cheap to settle.** Before
authoring the hub, publish a throwaway Lofty page with a 20-line test embed containing a
fixed-position box and a `:has()` rule, and look at it. Ten minutes of work that de-risks
the flagship deliverable.

**Fallback if `position:fixed` is blocked:** use `position: sticky; top: 96px` on a
right-hand grid column instead. Sticky is far less likely to be broken by a wrapper, though
it does require the TOC to live inside a two-column grid rather than float free.

---

## 3. URL structure on Lofty

From root `CLAUDE.md`:
- Blog posts live at **`/blog/<slug>`** — singular. The plural `/blogs/` **404s**.
- Landing pages get their own slug at root level.

### Proposed mapping of NRG's 4-tier pyramid onto Lofty

| NRG tier | NRG URL | Rose Homes LV equivalent | Lofty type |
|---|---|---|---|
| 1 — hub | `/new-construction/` | `/new-construction` | Landing page |
| 2 — geo sub-hub | `/henderson/new-construction/` | `/henderson-new-construction` | Landing page |
| 3 — builder | `/builders/dr-horton/` | `/dr-horton-las-vegas` | Landing page |
| 4 — support | `/blog/{slug}-2026/` | `/blog/<slug>` | Blog post |

**Note:** Lofty likely does not support nested paths like `/henderson/new-construction`.
Flatten to hyphenated root slugs. Confirm with Ryan before committing slugs, since
slugs are painful to change after indexing.

---

## 4. Content rules that override NRG's copy

Per workspace `CLAUDE.md`, applied to everything we write:

- **No em-dashes.** NRG's copy uses them heavily. All ported/inspired copy must use
  commas, periods, or "and".
- **Factual only.** NRG quotes specific incentives ("$20–50K", "Builder Incentives May
  2026" table with per-builder closing-cost credits). **Do not copy these numbers.** They
  are NRG's research, they go stale monthly, and a wrong incentive figure is a real
  liability. Either verify each with the builder directly or mark **NOT FOUND**.
- **6th-grade reading level, professional but warm.** NRG's voice is more analyst-report
  than Ryan's. Rewrite, don't transplant.
- **Soft CTAs.** NRG uses "Call (702) 637-1759" hard CTAs in the hero. Ryan's voice
  invites rather than pushes.
- **Ryan's contact block:** Ryan Rose | Real Broker, LLC | 702-747-5921 |
  ryan@rosehomeslv.com | rosehomeslv.com

---

## 5. Scope reality check

NRG has **2,129 unique pages** and a Next.js + Sanity + Repliers pipeline behind them.
We are not cloning that. The defensible subset:

| Build | Pages | Effort |
|---|---|---|
| **P0** — master hub + sticky TOC + IDX slot | 1 | High (this is the flagship) |
| **P1** — 5 geo sub-hubs | 5 | Medium (template reuse) |
| **P1** — 18 builder pages | 18 | Medium (template reuse, research-heavy) |
| **P2** — NC blog cluster, one post per hub FAQ | 15–20 | Medium |
| **P3** — `/compare/` pages anchored on Summerlin | 10–12 | Low (cheap, high long-tail) |
| **Skip** — 1,200 programmatic neighborhood pages | — | Not feasible without their data pipeline |

**The single highest-leverage insight from this research:** NRG's hub FAQ *is* their blog
editorial calendar. Every FAQ question on `/new-construction/` has a matching blog post
that links back to the hub. Build the hub FAQ first, then each answer becomes a post.
