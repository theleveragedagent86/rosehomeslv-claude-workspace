# CLAUDE.md — Rose Homes LV / Marketing / Lead-Magnets

Gated, downloadable assets used to capture leads from paid and organic traffic. Each one is a self-contained folder holding the guide itself, a landing page, and the SEO/publishing metadata that gets it live.

**The shape every lead magnet here follows:**

| File | Role |
|---|---|
| `<name>-guide.html` | the guide, print-first, self-contained, inline `<style>`, Google Fonts only |
| `<name>-guide.pdf` | Chrome-headless render of the above, the thing the lead actually receives |
| `landing-page.html` | the gated page traffic lands on; the lead form is injected by Lofty, not hardcoded here |
| `seo-package.md` | title, meta, OG/Twitter, JSON-LD, plus the exact Lofty publish values |
| `smart-plan.md` | the Lofty nurture sequence that fires on capture (emails end with `#signature#`) |

## What lives here

- **moving-to-las-vegas/** — the relocation lead magnet. Landing page, `relocation-guide.html` + `.pdf`, SEO package, smart plan, and a companion blog post. Read its `landing-page.html` for the Lofty full-bleed escape CSS.
  **The guide was rebuilt on the new construction guide's frozen design system on 2026-07-31.** It is now 11 print-first `.page` fragments in `fragments/p01..p11.html`, assembled by `build.py`, which lifts both `<style>` blocks verbatim out of `../new-construction-guide/build/shell.html`. Do not hand-copy that CSS: the shell is a base plus an override layer and transcribing it reintroduces the bug the design lock exists to catch. Chapter copy uses only the class inventory in [../new-construction-guide/build/design-system.md](../new-construction-guide/build/design-system.md).
  - `python3 build.py` then `python3 ../new-construction-guide/generate-pdf.py --html relocation-guide.html --pdf relocation-guide.pdf --no-footer`. **Pass `--no-footer`**, or Chrome stamps its own page number on top of the design's folio.
  - **`card-dusk` is unusable here.** It still renders a dark navy fill, and `.a` headings on it fail contrast. Use `card-clay`, `card-agave`, or `card-coral`.
  - **Check page fit mechanically after any copy change.** `.page` is a fixed box with `overflow:hidden`, so overset text vanishes with no error. Measure every descendant's bottom against `.foot`'s top in the rendered page, not by eye.
  - `assets/img/` is twelve photos borrowed from the new construction guide and recompressed to 2200px wide at quality 62, which took the PDF from 13.5MB to 6.7MB with no visible loss at print size. The full resolution originals stay in `../new-construction-guide/assets/img/`.
  - `_archive/` holds the pre-rebuild single-file guide. The landing page and blog post were **not** restyled and still carry the old cream and blue palette.
- **new-construction-guide/** — the **area-wide** Las Vegas / Henderson / Clark County new construction buyer guide. Builder-agnostic, three branching reader paths, named builder comparison table, and a dated market snapshot appendix that is regenerated quarterly. Built and refreshed by the `/new-construction-guide` skill. **Has its own CLAUDE.md** — read it first.

## Do not confuse these two new-construction assets

| | `Marketing/Lead-Magnets/new-construction-guide/` | `Content/New-Construction/<community>/` |
|---|---|---|
| Scope | the whole valley, builder-agnostic | one named community, one builder |
| Funnel | cold paid traffic who has no community in mind | warm traffic already looking at that community |
| Skill | `/new-construction-guide` | `/new-construction` |
| Design | its own researched conversion palette, deliberately not Rose Homes navy/gold | Bebas Neue + Inter, per-builder accent color |

Sending a community build into the lead-magnet folder, or the reverse, breaks the publishing scripts on both sides.

## Rules that apply to everything here

- **No em-dashes.** Checked mechanically; it is a hard failure, not a style note.
- **Factual only.** Never invent a price, fee, incentive, warranty term, or school rating. Mark gaps `NOT FOUND`.
- **Nevada advertising:** every asset a lead sees must identify the brokerage. `Real Broker, LLC` appears on the guide cover, the about page, the back matter, and the landing page.
- **Clark County only** for the new-construction guide: excludes Pahrump, Mesquite, and Boulder City.
- Landing pages carry **no hardcoded GA or Pixel tags**. Lofty injects those at publish (GA `G-50N1D59DW6`, Pixel `621835647008401`).

---

## Folder Map — keep this current

```
Lead-Magnets/
├── moving-to-las-vegas/        relocation lead magnet
│   ├── build.py                fragments + the new-construction shell CSS -> the guide
│   ├── fragments/              p01.html .. p11.html, one file per printed page
│   ├── assets/img/             12 photos, recompressed from the new construction set
│   ├── relocation-guide.html   generated. do not hand-edit
│   ├── relocation-guide.pdf    generated with --no-footer
│   ├── landing-page.html       Lofty landing page (still the old palette)
│   ├── moving-to-las-vegas-blog.html · seo-package.md · smart-plan.md
│   └── _archive/               the pre-2026-07-31 single-file guide
└── new-construction-guide/     area-wide new construction guide  → its own CLAUDE.md
```

**Maintenance rule:** When you add, remove, move, or rename a lead magnet here, update this map and the Folder Map in [Marketing/CLAUDE.md](../CLAUDE.md). If you move a folder, also update every absolute path that points at it in `~/.claude/skills/` and `~/.claude/plugins/marketplaces/` — the `/new-construction-guide` skill hardcodes this path in its `paths.md`. Never leave the map or a skill path stale.
