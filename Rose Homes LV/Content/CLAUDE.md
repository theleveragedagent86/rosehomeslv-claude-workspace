# CLAUDE.md — Rose Homes LV / Content

The content factory. Several sub-folders have their **own** `CLAUDE.md` — read it before working inside them.

- **Claude Blogs/** — the blog library (one folder per community/topic). `blog-writer`, `publish-blogs`, `subreddit-post` all read/write here.
- **New-Construction/** — multi-agent new-construction skill output. Finished communities live under `Completed/`. **Has its own CLAUDE.md** — read it first.
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
├── New-Construction/   new-construction skill output (Completed/ + comms)  → its own CLAUDE.md
├── Instagram/          IG content + Inbound-Engagement logs                → its own CLAUDE.md
├── Reddit/             Reddit engagement working folder                    → its own CLAUDE.md
├── YouTube/            YouTube scripts/packages
├── CCSD/               school-district local-news research
├── Research/           neighborhood/topic research notes
└── lofty-link-audit/   Lofty link audit
```

**Maintenance rule:** When you add/move/rename anything here, update this map, the sub-folder's own `CLAUDE.md` if it has one, and every absolute path in `~/.claude/skills/` + `~/.claude/plugins/marketplaces/` that points at it. Never leave the map stale.
