# CLAUDE.md — _System / tools

Loose dev tools and scripts, not tied to one business.

- **claude-ads-main/** — downloaded ad-generation tool repo (produced the Rose Homes LV ad plans it contains).
- **scrape_listing_leads.py**, **scrape_listing_leads_pages.py** — scrapers. Their `OUTPUT_DIR` writes into `Rose Homes LV/Marketing/Listing Leads Content/` — update that constant if the target moves.
- **excalidraw_generator.py** — generates `.excalidraw` diagrams.

---

## Folder Map — keep this current

```
tools/
├── claude-ads-main/                  ad-generation tool repo
├── scrape_listing_leads.py           -> writes Rose Homes LV/Marketing/Listing Leads Content/
├── scrape_listing_leads_pages.py     -> writes Rose Homes LV/Marketing/Listing Leads Content/
└── excalidraw_generator.py
```

**Maintenance rule:** When you add/remove a tool, update this map. If a tool writes to a content folder, keep its hardcoded OUTPUT path in sync when that folder moves. Never leave the map stale.
