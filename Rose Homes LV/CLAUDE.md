# CLAUDE.md — Rose Homes LV (real estate business)

Everything under this folder is the **Rose Homes LV** real estate business (Ryan Rose, Real Broker LLC, Las Vegas / Clark County). This is the core, highest-volume business in the workspace.

**Brand & voice:** Professional but warm, 6th-grade reading level, soft CTAs, no em-dashes, factual only, Las Vegas focus. Contact: Ryan Rose | Real Broker, LLC | 702-747-5921 | ryan@rosehomeslv.com | rosehomeslv.com. (Full content rules are in the [root CLAUDE.md](../CLAUDE.md).)

**Do not mix** this business with `AI Clients/`, `SKOOL Community/`, or `Content Channels/` — different brands entirely.

## Sub-folders

- **Clients/** — active people: `Buyers/`, `Listings/` (sellers), `Transactions/` (per-deal working folders, git-ignored / private).
- **Prospecting/** — outreach & lead-gen: `Expireds/`, `Active Cannonballs/`, `Digital Cannonballs/`, competitor intel.
- **Content/** — the content factory: `Claude Blogs/`, `New-Construction/`, `Instagram/`, `Reddit/`, `YouTube/`, `CCSD/` and local-news, `Research/` (neighborhood research notes), `lofty-link-audit/`. Several of these carry their own `CLAUDE.md`.
- **Marketing/** — listing & lead marketing: `Listing Marketing Plan/`, `Listing Leads Content/`, `Lead-Magnets/`, `Relocation Guide/`, `Smart Plans/` (Lofty nurture), templates.
- **CMA Reports/** — `/seller-cma` output. `_template/` is the master (never edit for a client); each report is a self-contained `<Street Address>/` folder.
- **Brand/** — personal-brand strategy, sales/cover letters, one-off HTML artifacts, strategy diagrams.

## Skills that write here (run from `~/.claude/`, reference these paths absolutely)

blog-writer, publish-blogs, listing-marketing, listing-description, reverse-prospecting, expired-workflow, cma, seller-cma, new-construction, tc-plugin (transaction-coordination), daily-checklist, weekly-update, ig-*, inbound-*, Reddit, subreddit-post, youtube-manager, local-news. If you move a folder here, their absolute paths must be updated — see [_System/CLAUDE.md](../_System/CLAUDE.md).

---

## Folder Map — keep this current

```
Rose Homes LV/
├── Clients/         Buyers/ · Listings/ · Transactions/ (private) · Lisa-Jones-TC-Process-Breakdown.md
├── Prospecting/     Expireds/ · Active Cannonballs/ · Digital Cannonballs/ · Brenkus-Team-Competitive-Analysis.md · Expired-Content-Library.md
├── Content/         Claude Blogs/ · New-Construction/ · Instagram/ · Reddit/ · YouTube/ · CCSD/ · Research/ · lofty-link-audit/
├── Marketing/       Listing Marketing Plan/ · Listing Leads Content/ · Lead-Magnets/ · Relocation Guide/ · Smart Plans/ · email-templates.md · seller-report-template.html
├── CMA Reports/     _template/ (master) + one folder per property
└── Brand/           Personal Brand Strategy/ · Marketing/ · ryan-rose-*.html · *.excalidraw · overpriced_homes_graphic.*
```

**Maintenance rule:** When you add, remove, move, or rename anything under Rose Homes LV, update this map, the affected sub-folder's `CLAUDE.md` (if any), and — critically — every absolute path reference in `~/.claude/skills/` and `~/.claude/plugins/marketplaces/` that points at the moved item. Never leave the map or a skill path stale.
