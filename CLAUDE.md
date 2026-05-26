# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this workspace is

This is Ryan Rose's real estate operations workspace, not a traditional source-code project. It mixes three things in one tree:

1. **Claude Code plugins and skills** that automate Ryan's business workflows (blog writing, Reddit engagement, transaction coordination, daily checklist, listing marketing, CMA reports, etc.).
2. **Content libraries** consumed by those plugins or used directly (Claude Blogs, Listings, Listing Marketing Plan, Expireds, Smart Plans, Reddit, Instagram, Transactions).
3. **Domain sub-projects** with their own `CLAUDE.md` that act as scoped agent contexts.

Per-domain `CLAUDE.md` files exist in `New-Construction/`, `Reddit/`, and `Instagram/`. Read those before doing work inside those folders — they are authoritative for their domain. This top-level file covers cross-cutting conventions only.

## Plugin and skill conventions

Plugins live as `<name>-plugin/skills/<skill-name>/` directories with a paired `<name>-plugin.zip` snapshot at the root. The unzipped folder is the working copy; the `.zip` is the distribution artifact you re-zip when shipping. Examples: [blog-writer-plugin/](blog-writer-plugin/), [reddit-plugin/](reddit-plugin/), [tc-plugin/](tc-plugin/), [publish-blogs-plugin/](publish-blogs-plugin/), [daily-checklist-plugin/](daily-checklist-plugin/), [reverse-prospecting-plugin/](reverse-prospecting-plugin/), [listing-description-plugin/](listing-description-plugin/).

Skills can also live in the **user-global skills folder** at `~/.claude/skills/<skill-name>/`. The current `.claude/settings.local.json` adds three of those (`Reddit`, `ig-ads`, `listing-marketing`) as `additionalDirectories` so they show up in this workspace. When a slash command reaches into `~/.claude/skills/`, that's why. Don't duplicate a skill into both places — pick one home and let the other reference it.

Some skills have richer multi-agent architectures. The most elaborate example is the new-construction skill at `~/.claude/skills/new-construction/`, orchestrated by [New-Construction/CLAUDE.md](New-Construction/CLAUDE.md) — 9 sub-agents across 5 waves writing per-community marketing assets into [New-Construction/](New-Construction/). Read that file before touching anything under `New-Construction/`.

## Local preview server

[serve.rb](serve.rb) is a one-liner WEBrick server on port 8091 that serves the current working directory. Use it to preview standalone HTML artifacts (landing pages, buyer guides, listings, infographics) in a browser before publishing.

```bash
ruby serve.rb
# then open http://localhost:8091/<path-to-html>
```

## Permissions

`.claude/settings.local.json` accumulates `Bash(...)` and `WebFetch(...)` allowlist entries as Ryan approves them. Before adding more, check whether a broader pattern already covers the request. Never widen `Read` beyond `/Users/ryanrose/**` — that's already broad enough.

## Content rules that apply everywhere in this workspace

These are referenced by name in multiple sub-projects' instructions; treat them as defaults unless a sub-project's `CLAUDE.md` overrides them:

- **No em-dashes.** Use commas, periods, or "and". Real estate prospects flag em-dashes as AI-generated.
- **Factual only.** Never fabricate prices, square footage, school ratings, HOA amounts, builder incentives, or program details. Mark gaps as "NOT FOUND" so a human can fill them in.
- **Las Vegas / Clark County focus.** Henderson, Summerlin, Spring Valley, Centennial Hills, North Las Vegas, Skye Canyon, Green Valley. Reject other locations unless a sub-project explicitly broadens the scope.
- **Professional but warm tone, 6th-grade reading level.** Short sentences. Talk like you're explaining to a friend. No jargon, no "premier", no "exclusive opportunity".
- **Soft CTAs.** Invite, don't push. "Want me to send the buyer guide?" beats "Call now!"
- **Ryan's contact info:** Ryan Rose | Real Broker, LLC | 702-747-5921 | ryan@rosehomeslv.com | rosehomeslv.com.
- **Lofty smart plan emails** end with `#signature#` (Lofty auto-inserts the signature). Never hardcode the sign-off.
- **Lofty merge field for first name:** `#lead_first_name#`.
- **Blog URL pattern on rosehomeslv.com:** `/blog/<slug>` (singular). The plural `/blogs/` 404s — see [memory/project_lofty_blog_url_pattern.md](../../.claude/projects/-Users-ryanrose-Downloads-Claude/memory/project_lofty_blog_url_pattern.md) if relevant.

## When working with this workspace

- If a `<sub-folder>/CLAUDE.md` exists, read it before doing work inside that folder. It's the source of truth for that domain.
- Plugin source code and the matching `.zip` can drift. When you change a plugin folder, re-zip it and update the snapshot before reporting the work as done.
- Standalone HTML files at the workspace root (e.g. [seller-report-template.html](seller-report-template.html), [ryan-rose-cannonball.html](ryan-rose-cannonball.html), [overpriced_homes_graphic.png](overpriced_homes_graphic.png)) are one-off artifacts, not part of any plugin. Edit them in place.
