# CLAUDE.md — _System / plugins

Dev/source copies of every Claude Code plugin. **These do not run directly** — the executing copies live in `~/.claude/plugins/marketplaces/local-desktop-app-uploads/<name>/` (and some skills in `~/.claude/skills/`, occasionally symlinked back here). See [../CLAUDE.md](../CLAUDE.md) for the path-safety and re-zip procedure.

Each plugin is `<name>-plugin/` containing `.claude-plugin/plugin.json` and `skills/<skill>/`.

---

## Folder Map — keep this current

```
plugins/
├── blog-writer-plugin/          digital-cannonball-plugin/    listing-description-plugin/
├── local-news-plugin/           publish-blogs-plugin/         reddit-plugin/
├── reverse-prospecting-plugin/  tc-plugin/                    daily-checklist-plugin/   (symlinked from ~/.claude/skills/daily-checklist)
├── excalidraw-plugin/           ig-ads-plugin/                ig-carousel-plugin/
├── ig-engage-plugin/            ig-research-plugin/           inbound-comments-plugin/
├── inbound-dm-followers-plugin/ inbound-dm-likes-plugin/      inbound-research-plugin/
```

**Lofty background tooling (added 2026-09-21):**
- `publish-blogs-plugin/lofty_api.py` = calls Lofty's blog API through any open cms.lofty.com
  Chrome tab (no focus, no tab number). `dump` all posts, `patch` fields by post id, plus
  `find_by_slug` / `create` used by the local-news scripts. Skips frozen tabs.
- `publish-blogs-plugin/build_live_schema.py` = builds full JSON-LD @graph (Article/NewsArticle +
  Person + RealEstateAgent + Place + FAQPage) for live posts missing schema, from a dump.
- `publish-blogs-plugin/backfill_schema.py` = adds FAQPage, wraps bare Article schema in the
  Person/RealEstateAgent @graph, and fills missing featured images, from a dump.
- `local-news-plugin/publish-local-news.py` + `fix-local-news-blogs.py` and
  `publish-blogs-plugin/publish-aeo.py` + `fix-live-posts.py` now run through lofty_api by
  default (background). fix-live-posts `schema` mode overwrites live FAQ: backfill after.
  `--ui` = old tab-4 editor method. The local-news `_dist` zip bundles a copy of
  lofty_api.py; in the workspace those two load it from `../publish-blogs-plugin/`.

**AEO price refresh chain (added 2026-09-23), all in `publish-blogs-plugin/`:**
- `market-stats.py <csv>` = turns Ryan's MLS "Agent Single Line" sold export into dated
  per-area stats (median, middle half, $/sq ft, DOM, property-type split) in
  `Rose Homes LV/Content/Research/market-stats/`. Areas are zip-code groupings.
- `apply-market-stats.py` = rewrites the generated "## What Homes Are Selling For in <Area>"
  section in all 184 AEO posts from `market-stats-latest.json`. Idempotent, replaces rather
  than appends, and skips the 6 Nevada-law posts where price is irrelevant.
- `refresh-market-stats.py` = the driver: newest export -> stats -> posts -> Lofty ->
  schema backfill. Refuses an export older than 21 days. `--dry-run` stops before publishing.
  Run on the 1st and 15th by the `aeo-market-stats-refresh` scheduled task.

**Maintenance rule:** When you add/remove a plugin, update this map. When you edit a plugin, re-zip to `../_dist/` and sync the running copy in `~/.claude/` if the change should go live. Never leave the map stale.
