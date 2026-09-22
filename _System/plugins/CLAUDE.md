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
- `local-news-plugin/publish-local-news.py` + `fix-local-news-blogs.py` and
  `publish-blogs-plugin/publish-aeo.py` now run through lofty_api by default (background).
  `--ui` = old tab-4 editor method. The local-news `_dist` zip bundles a copy of
  lofty_api.py; in the workspace those two load it from `../publish-blogs-plugin/`.

**Maintenance rule:** When you add/remove a plugin, update this map. When you edit a plugin, re-zip to `../_dist/` and sync the running copy in `~/.claude/` if the change should go live. Never leave the map stale.
