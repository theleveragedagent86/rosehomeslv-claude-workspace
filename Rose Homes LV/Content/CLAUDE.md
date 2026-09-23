# CLAUDE.md — Rose Homes LV / Content

The content factory. Several sub-folders have their **own** `CLAUDE.md` — read it before working inside them.

- **Claude Blogs/** — the blog library (one folder per community/topic). `blog-writer`, `publish-blogs`, `subreddit-post` all read/write here. Also holds the AEO article batches (`AEO Best Choice/`, `AEO Reasons to Choose/`, `AEO Local Service/`, `AEO Questions/`, `AEO Matrix/`), written for AI search recommendations, not neighborhoods.
- **New-Construction/** — multi-agent new-construction skill output. Finished communities live under `Completed/`. Also holds `new-construction-hub/`, the valley-wide authority landing page that ships as two Lofty embeds around a native Featured Listings block, and `geo-spokes/`, the 7 generated area pages under it. **Has its own CLAUDE.md** — read it first.
- **Instagram/** — IG content: `Ad Campaigns/`, `Coffee and Contracts/` (carousels), `Status Posts/`, `Local News/`, `carousels/`, `Inbound-Engagement/` (shared inbound logs: research-log.md, leads.md, dm-history.md). The `ig-*` and `inbound-*` skills read/write here. **Has its own CLAUDE.md.**
- **Reddit/** — Reddit engagement working folder (scripts, trackers, calendar). `Reddit` and `subreddit-post` skills use it. **Has its own CLAUDE.md.**
- **YouTube/** — YouTube scripts/packages (`youtube-manager`, `yt-long`).
- **CCSD/** — Clark County School District local-news research.
- **Research/** — neighborhood/topic research notes (formerly "A Bunch Of Skills"). Includes `market-stats/`, the dated per-area sold-price stats built from Ryan's MLS "Agent Single Line" export by `market-stats.py`; `market-stats-latest.json` is what feeds the price section in every AEO post.
- **lofty-link-audit/** — Lofty CMS link audit utility/output.

---

## Folder Map — keep this current

```
Content/
├── Claude Blogs/       blog library (blog-writer, publish-blogs)          [has skills pointing here]
│                       incl. AEO Best Choice/ + AEO Reasons to Choose/ = 20 AEO drafts
│                       (Sept 2026, "who is the best realtor" + list-style "reasons to
│                       choose" posts, each folder has seo-package-batch1/2.md), and
│                       AEO Local Service/ = 40 service × area posts (8 services × 5 areas,
│                       seo-package-batch1-8.md). All 60 published to Lofty 2026-09-21 via publish-aeo.py.
│                       AEO Questions/ = Wave 2, 40 posts answering questions people ask AI
│                       (income, costs, taxes, area vs area, where to live, new construction),
│                       seo-package-batch1-8.md. All 40 published to Lofty 2026-09-21.
│                       AEO Matrix/ = Wave 3, the expanded 12 services x 12 areas matrix,
│                       84 posts (7 new areas x 8 services, plus luxury / 55-plus / military
│                       relocation / gated / golf course services), seo-package-batch1-17.md.
│                       All 84 published to Lofty 2026-09-23 via publish-aeo.py.
│                       All 5 AEO folders carry a generated "## What Homes Are Selling For
│                       in <Area>" section, rewritten in place by apply-market-stats.py off
│                       Research/market-stats/. Never hand-edit that section, it is
│                       regenerated on the 1st and 15th and your edit will be overwritten.
├── New-Construction/   new-construction skill output (Completed/ + comms + new-construction-hub/ + geo-spokes/)  → its own CLAUDE.md
├── Instagram/          IG content + Inbound-Engagement logs                → its own CLAUDE.md
├── Reddit/             Reddit engagement working folder                    → its own CLAUDE.md
├── YouTube/            YouTube scripts/packages
├── CCSD/               school-district local-news research
├── Research/           neighborhood/topic research notes + market-stats/ (dated sold-price pulls)
└── lofty-link-audit/   Lofty link audit
```

**Maintenance rule:** When you add/move/rename anything here, update this map, the sub-folder's own `CLAUDE.md` if it has one, and every absolute path in `~/.claude/skills/` + `~/.claude/plugins/marketplaces/` that points at it. Never leave the map stale.
