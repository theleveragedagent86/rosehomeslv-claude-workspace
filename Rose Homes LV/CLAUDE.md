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
- **Dashboard/** — the localhost Command Center (`index.html` + data JSON), served by
  [serve.rb](../serve.rb) on 8091 and rebuilt 6am daily. Wears the **Slate** dark skin (chosen
  2026-08-24 from four variants) over the Vector token structure, used as tool styling, not realtor
  branding, plus a two-token status extension. Reads `Clients/Transactions/*/transaction.json`
  through an adapter and never writes to them. Google Calendar is an iframe embed that renders off
  Ryan's own browser session, so it is display-only and unreadable by the build.

## Skills that write here (run from `~/.claude/`, reference these paths absolutely)

blog-writer, publish-blogs, listing-marketing, listing-description, reverse-prospecting, expired-workflow, cma, seller-cma, new-construction, tc-plugin (transaction-coordination), daily-checklist, weekly-update, ig-*, inbound-*, Reddit, subreddit-post, youtube-manager, local-news. If you move a folder here, their absolute paths must be updated — see [_System/CLAUDE.md](../_System/CLAUDE.md).

---

## Folder Map — keep this current

```
Rose Homes LV/
├── Clients/         Buyers/ · Listings/ · Transactions/ (private) · Lisa-Jones-TC-Process-Breakdown.md
├── Prospecting/     Expireds/ · Active Cannonballs/ · Digital Cannonballs/ · Brenkus-Team-Competitive-Analysis.md · Expired-Content-Library.md
├── Content/         Claude Blogs/ · New-Construction/ · Instagram/ · Reddit/ · YouTube/ · CCSD/ · Research/ · lofty-link-audit/
├── Marketing/       Listing Marketing Plan/ · Listing Leads Content/ · Lead-Magnets/ · Newsletter/ (NEWSLETTER-TEMPLATE.md, The Rose Report weekly, fed by /local-news) · Relocation Guide/ · Smart Plans/ · nrg-research/ · email-templates.md · seller-report-template.html
├── CMA Reports/     _template/ (master) + one folder per property
├── Brand/           Personal Brand Strategy/ · Marketing/ · ryan-rose-*.html · *.excalidraw · overpriced_homes_graphic.*
├── Dashboard/       index.html (localhost Command Center, port 8091, Slate dark skin) +
│                    completion-log.json (checkbox state) + config.example.json +
│                    runs/ (one .md + .json per live run) +
│                    runs/baked/ (one .md per baked button, filename MUST equal the
│                                command id in serve.rb COMMANDS or the button reports
│                                "never built": daily-checklist, tc-status, deadlines,
│                                money. transactions/pipeline/contacts.md are extras
│                                with no button.) +
│                    data/ (transactions.json, commissions.json, built by Rebuild data)
└── Diverse Dispute/ Vendor dispute file: Diverse Marketing LLC $12k deposit refund. README.md · diverse-evidence-log.md · correspondence-log.md · contract/ · screenshots/<YYYY-MM-DD>/
```

**Diverse Dispute note:** time-sensitive. Portal screenshots are due on the 10th of every
month through 2026-12-10, and the refund demand goes out **2026-12-19**. Read
`Diverse Dispute/README.md` before touching anything in there, and do not draft anything
adversarial to Diverse before that date.

**Maintenance rule:** When you add, remove, move, or rename anything under Rose Homes LV, update this map, the affected sub-folder's `CLAUDE.md` (if any), and — critically — every absolute path reference in `~/.claude/skills/` and `~/.claude/plugins/marketplaces/` that points at the moved item. Never leave the map or a skill path stale.
