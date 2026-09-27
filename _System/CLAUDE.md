# CLAUDE.md — _System (shared tooling)

Everything Claude *runs* rather than *produces*: plugin dev-copies, skill sources, dev tools, and distribution snapshots. Not tied to any one business.

## The most important thing to understand here

The folders in `plugins/` and `skills/` are **DEV/SOURCE COPIES**. The versions that actually execute live OUTSIDE this workspace:

- **Installed skills:** `~/.claude/skills/<name>/`
- **Installed plugins (marketplace):** `~/.claude/plugins/marketplaces/local-desktop-app-uploads/<name>/`
- Some installed skills are **symlinks** back into this workspace (e.g. `~/.claude/skills/daily-checklist` → `_System/plugins/daily-checklist-plugin/...`). If you move a symlinked target, repoint the symlink.

Many of these running copies reference workspace **content** by hardcoded absolute path (e.g. `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Claude Blogs/`).

## Path-safety procedure — RUN THIS whenever you move/rename a content folder

1. Decide the exact OLD → NEW absolute path.
2. Rewrite every occurrence across **three** locations: the workspace, `~/.claude/skills/`, and `~/.claude/plugins/marketplaces/`. Anchor on the full base path `/Users/ryanrose/Downloads/Claude/...` so prose words are never touched.
3. Check for **symlinks** into the moved path: `find ~/.claude/skills ~/.claude/plugins -type l` and repoint any that break.
4. Verify: grep the three locations for the OLD path — expect zero hits — and confirm every referenced literal path still resolves on disk.

## Re-zipping

Plugins are distributed as `<name>-plugin.zip`. When you change a plugin's dev copy, re-zip it and refresh the snapshot in `_dist/`. Dev copy and zip can drift — the zip is the shippable artifact.

---

## Folder Map — keep this current

```
_System/
├── plugins/    19 plugin dev-copies (blog-writer, tc-plugin, publish-blogs, ig-*, inbound-*, daily-checklist, excalidraw, etc.)  → _System/plugins/CLAUDE.md
│            publish-blogs-plugin/lofty_api.py = shared background Lofty blog API tool (local-news scripts use it too)
├── skills/     skill source copies (blog-writer, listing-marketing, publish-blogs, reverse-prospecting, expired-content, Reddit, skill-builder, Listing Marketing Plan, listing-video, yt-thumbnail, yt-shorts-publish, skool-carousel, skool-manychat, skool-ig-post, coach-teardown, rose-report, skool-reels, skool-shorts-schedule)  → _System/skills/CLAUDE.md
│            skool-carousel + coach-teardown + rose-report + skool-reels + skool-shorts-schedule are SYMLINKED live into ~/.claude/skills/
├── tools/      dev tools (claude-ads-main, scrape_listing_leads*.py, excalidraw_generator.py, listing-video/, longform-to-shorts/)  → _System/tools/CLAUDE.md
├── external-skills/  third-party skill repos cloned for evaluation, NOT installed (instagram-skills by
│            sergebulaev; SlopMonster by ItsssssJack = AI-writing linter + rival-model cleanse, skill name `slopmonster`)
└── _dist/      .zip distribution snapshots (+ inbound-zips/)
```

**Maintenance rule:** When you add, remove, move, or rename a plugin/skill/tool here, update this map and the sub-folder map. When you re-zip, refresh `_dist/`. Remember: editing a dev copy here does NOT change the running skill in `~/.claude/` — sync it if that's the intent. Never leave the map stale.
