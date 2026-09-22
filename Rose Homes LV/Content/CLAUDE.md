# CLAUDE.md — Rose Homes LV / Content

The content factory. Several sub-folders have their **own** `CLAUDE.md` — read it before working inside them.

- **Claude Blogs/** — the blog library (one folder per community/topic). `blog-writer`, `publish-blogs`, `subreddit-post` all read/write here. Also holds the AEO article batches (`AEO Best Choice/`, `AEO Reasons to Choose/`, `AEO Local Service/`, `AEO Questions/`), written for AI search recommendations, not neighborhoods.
- **New-Construction/** — multi-agent new-construction skill output. Finished communities live under `Completed/`. Also holds `new-construction-hub/`, the valley-wide authority landing page that ships as two Lofty embeds around a native Featured Listings block, and `geo-spokes/`, the 7 generated area pages under it. **Has its own CLAUDE.md** — read it first.
- **Instagram/** — IG content: `Ad Campaigns/`, `Coffee and Contracts/` (carousels), `Status Posts/`, `Local News/`, `carousels/`, `Inbound-Engagement/` (shared inbound logs: research-log.md, leads.md, dm-history.md). The `ig-*` and `inbound-*` skills read/write here. **Has its own CLAUDE.md.**
- **Reddit/** — Reddit engagement working folder (scripts, trackers, calendar). `Reddit` and `subreddit-post` skills use it. **Has its own CLAUDE.md.**
- **YouTube/** — YouTube scripts/packages (`youtube-manager`, `yt-long`).
- **CCSD/** — Clark County School District local-news research.
- **Research/** — neighborhood/topic research notes (formerly "A Bunch Of Skills").
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
│                       seo-package-batch1-8.md. Drafted 2026-09-21, not yet published.
├── New-Construction/   new-construction skill output (Completed/ + comms + new-construction-hub/ + geo-spokes/)  → its own CLAUDE.md
├── Instagram/          IG content + Inbound-Engagement logs                → its own CLAUDE.md
├── Reddit/             Reddit engagement working folder                    → its own CLAUDE.md
├── YouTube/            YouTube scripts/packages
├── CCSD/               school-district local-news research
├── Research/           neighborhood/topic research notes
└── lofty-link-audit/   Lofty link audit
```

**Maintenance rule:** When you add/move/rename anything here, update this map, the sub-folder's own `CLAUDE.md` if it has one, and every absolute path in `~/.claude/skills/` + `~/.claude/plugins/marketplaces/` that points at it. Never leave the map stale.
