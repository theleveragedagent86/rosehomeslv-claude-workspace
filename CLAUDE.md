# CLAUDE.md — Ryan Rose Workspace (root)

This is the top-level guide for Claude Code (claude.ai/code) working anywhere in this workspace.

## How this workspace is organized

This tree holds **four separate businesses plus shared tooling**, one per top-level folder. They have different brands, audiences, and voices. **Keep them separate — never mix content, branding, or client data across them.**

| Folder | What it is | Business |
|---|---|---|
| **[Rose Homes LV/](Rose%20Homes%20LV/)** | The real estate business — all realtor content, clients, listings, transactions, marketing. | Rose Homes LV / Real Broker |
| **[AI Clients/](AI%20Clients/)** | AI consulting & automation client work (Brian Esposito, Crystal, Nick Nolf, Zbuyer). | AI automation agency |
| **[SKOOL Community/](SKOOL%20Community/)** | "The Leveraged Agent" Skool community — course modules, VSL, student content. | Skool / coaching |
| **[Content Channels/](Content%20Channels/)** | Faceless / personal content channels (Codename History) and research (Karpathy Autoresearch). | Media / personal |
| **[Personal/](Personal/)** | Personal knowledge bases (My Wiki Obsidian vault, LLM-Wiki). | Personal |
| **[_System/](_System/)** | Shared tooling: all plugin dev-copies, skill sources, dev tools, and `.zip` snapshots. | Infrastructure |

Loose at the root: `CLAUDE.md` (this file), `serve.rb` (preview server), `hyperframes/` (self-contained video-generation tool/repo).

**Each top-level folder has its own `CLAUDE.md`.** Claude Code auto-loads the `CLAUDE.md` of the folder you're working in, so read it before doing work there — it is authoritative for that business.

## The CLAUDE.md documentation system (read this)

Every significant folder carries a `CLAUDE.md` describing its structure. At the bottom of each is a **"Folder Map"** and a **maintenance rule**:

> **Maintenance rule:** When you add, remove, move, or rename anything in a folder, update the "Folder Map" in THAT folder's `CLAUDE.md` **and** the parent folder's `CLAUDE.md` in the same change. If you move something across top-level folders, update the `CLAUDE.md` in BOTH the source and destination. Never leave a Folder Map stale.

Follow this every time you change the file tree, without being asked.

## How plugins & skills actually run (important)

The plugin folders in `_System/plugins/` and skill folders in `_System/skills/` are **dev/source copies**. The **running** versions live outside this workspace:

- Installed skills: `~/.claude/skills/<name>/`
- Installed plugins: `~/.claude/plugins/marketplaces/local-desktop-app-uploads/<name>/`

Many of those running skills reference workspace content by **hardcoded absolute path** (e.g. `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Clients/Listings/`). **Consequence:** if you move or rename a content folder, you must update every absolute reference to it in the workspace **and** in `~/.claude/skills/` and `~/.claude/plugins/marketplaces/`, or the skill breaks. See [_System/CLAUDE.md](_System/CLAUDE.md) for the full path-safety procedure.

## Local preview server

[serve.rb](serve.rb) is a WEBrick server on port 8091 that serves the current working directory. Use it to preview standalone HTML (landing pages, buyer guides, CMAs, infographics) before publishing.

```bash
ruby serve.rb
# then open http://localhost:8091/<path-to-html>
```

## Permissions

`.claude/settings.local.json` accumulates `Bash(...)` / `WebFetch(...)` allowlist entries as Ryan approves them. Check whether a broader pattern already covers a request before adding more. Never widen `Read` beyond `/Users/ryanrose/**`.

## Content rules — default across the WHOLE workspace

Apply everywhere unless a folder's own `CLAUDE.md` overrides them. (These are strongest for Rose Homes LV; other businesses may set their own voice in their `CLAUDE.md`.)

- **No em-dashes.** Use commas, periods, or "and". Prospects flag em-dashes as AI-generated.
- **Factual only.** Never fabricate prices, square footage, school ratings, HOA amounts, builder incentives, or program details. Mark gaps as "NOT FOUND".
- **Las Vegas / Clark County focus** for realtor work: Henderson, Summerlin, Spring Valley, Centennial Hills, North Las Vegas, Skye Canyon, Green Valley.
- **Professional but warm, 6th-grade reading level.** Short sentences. No jargon, no "premier", no "exclusive opportunity".
- **Soft CTAs.** Invite, don't push.
- **Ryan's contact info:** Ryan Rose | Real Broker, LLC | 702-747-5921 | ryan@rosehomeslv.com | rosehomeslv.com.
- **Lofty smart plan emails** end with `#signature#` (Lofty auto-inserts the signature). First-name merge field: `#lead_first_name#`.
- **Blog URL pattern on rosehomeslv.com:** `/blog/<slug>` (singular). The plural `/blogs/` 404s.

---

## Folder Map — keep this current

```
Claude/
├── CLAUDE.md                 # this file (root guide)
├── serve.rb                  # localhost:8091 preview server
├── hyperframes/              # self-contained video-generation tool (own git repo)
├── Rose Homes LV/            # real estate business  → Rose Homes LV/CLAUDE.md
├── AI Clients/               # AI consulting clients  → AI Clients/CLAUDE.md
├── SKOOL Community/          # The Leveraged Agent Skool  → SKOOL Community/CLAUDE.md
├── Content Channels/         # Codename History, Karpathy  → Content Channels/CLAUDE.md
├── Personal/                 # wikis  → Personal/CLAUDE.md
└── _System/                  # plugins, skills, tools, zips  → _System/CLAUDE.md
```

**Maintenance rule:** When you add, remove, move, or rename a top-level folder, update this map and create/adjust that folder's own `CLAUDE.md`. If a change moves content between businesses, update both sides. Never leave this stale.
