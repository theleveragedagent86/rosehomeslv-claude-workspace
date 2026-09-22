# CLAUDE.md — _System / tools

Loose dev tools and scripts, not tied to one business.

- **claude-ads-main/** — downloaded ad-generation tool repo (produced the Rose Homes LV ad plans it contains).
- **scrape_listing_leads.py**, **scrape_listing_leads_pages.py** — scrapers. Their `OUTPUT_DIR` writes into `Rose Homes LV/Marketing/Listing Leads Content/` — update that constant if the target moves.
- **excalidraw_generator.py** — generates `.excalidraw` diagrams.
- **listing-video/** — turns 8 to 10 listing photos into a vertical 1080x1920 reel: photos in the top half, black bottom half for Ryan's green-screen talking head (`--layout full` for photos-only). ffmpeg only, no AI credits. The free stand-in for Dundy AI / Calico AI. Driven by the `listing-video` skill, which does the photo curation. Takes photo paths as arguments, so no hardcoded content path. See its `README.md`.
- **longform-to-shorts/** — cuts vertical 1080x1920 shorts (burned captions, normalized audio) out of an existing long recording, via whisper-cpp + ffmpeg. Three layouts: talking head, screen demo, PIP-hero. Distinct from the `claude-shorts` plugin, which builds teleprompter videos from scratch with HyperFrames. Takes the source video as an argument, so no hardcoded content path. See its `README.md`.

---

## Folder Map — keep this current

```
tools/
├── claude-ads-main/                  ad-generation tool repo
├── scrape_listing_leads.py           -> writes Rose Homes LV/Marketing/Listing Leads Content/
├── scrape_listing_leads_pages.py     -> writes Rose Homes LV/Marketing/Listing Leads Content/
├── excalidraw_generator.py
├── listing-video/                    listing photos -> 9:16 reel, black bottom half for green screen
│   ├── README.md
│   └── listing_video.py              driven by the `listing-video` skill
└── longform-to-shorts/               long recording -> vertical captioned shorts (whisper-cpp + ffmpeg)
    ├── README.md
    ├── make_caption_pngs.py          captions as PNGs (this ffmpeg has no libass)
    ├── render_clip.py                full-camera talking head
    ├── render_screen_clip.py         screen demo + small crisp PIP
    └── render_pip_clip.py            enlarged PIP when the screen is idle
```

**Maintenance rule:** When you add/remove a tool, update this map. If a tool writes to a content folder, keep its hardcoded OUTPUT path in sync when that folder moves. Never leave the map stale.
