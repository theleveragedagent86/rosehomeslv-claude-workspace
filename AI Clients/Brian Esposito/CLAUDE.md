# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Directory Is

Client deliverable workspace for **Brian Esposito** (Branch Manager, Nations Lending, Las Vegas, NMLS #1535781). This is not a traditional codebase — it produces two artifacts for the client:

1. **`lender-engagement.zip`** — a Claude Cowork plugin containing two skills (`lender-comments` and `lender-research`) that automate Brian's Instagram engagement strategy
2. **Two Word docs** generated from Python: strategy plan + step-by-step setup guide

Full project context lives at `/Users/ryanrose/.claude/plans/joyful-tumbling-wreath.md` (plan) and `/Users/ryanrose/.claude/plans/joyful-tumbling-wreath-agent-a14986442c537b88b.md` (Brian's research profile). Read both before making meaningful changes.

## Build Commands

```bash
# Rebuild both Word docs (requires python-docx)
python3 build_plan_doc.py
python3 build_setup_guide_doc.py

# Rebuild the plugin zip (always run from the project root)
cd plugin-build && zip -r ../lender-engagement.zip lender-engagement/ -x "*.DS_Store" && cd ..
```

There is no test suite, linter, or CI. Verification is manual (open the `.docx`, inspect the zip with `unzip -l`).

## Architecture: the dual-source-of-truth gotcha

Skill files exist in **two parallel locations** and must be kept in sync:

- `plugin-build/lender-engagement/skills/` — **canonical source** that gets zipped into the Cowork plugin. Uses relative `./skills/...` paths per the [plugin manifest spec](/Users/ryanrose/.claude/plugins/marketplaces/claude-plugins-official/plugins/plugin-dev/skills/plugin-structure/references/manifest-reference.md). Supporting files live in `references/` subdirectories.
- `skills/` — older staged copy from before the plugin structure. Uses absolute `~/.claude/skills/...` paths. Kept for legacy reference.

**When editing skill content:** edit the `plugin-build/` version first, then `cp` the changed files to `skills/` to keep them consistent, then rebuild the zip. When searching for content across the project, expect duplicate hits in both trees.

## Plugin structure (what goes inside the zip)

```
lender-engagement/
├── .claude-plugin/plugin.json        # Mandatory. Includes inline Playwright MCP config.
├── skills/
│   ├── lender-comments/              # Auto-discovered as /lender-comments
│   │   ├── SKILL.md                  # YAML frontmatter, then instructions
│   │   ├── target-accounts.md        # LO target list (live data, not a template)
│   │   └── references/               # Supporting docs, loaded on demand
│   └── lender-research/              # Auto-discovered as /lender-research
│       ├── SKILL.md
│       └── references/
└── README.md
```

`plugin.json` registers the Playwright MCP server inline (`playwright-instagram` with a persistent `--user-data-dir`). When Brian installs the plugin in Cowork, the MCP auto-registers.

## Template: ig-engage

Both skills are modeled on Ryan's personal `ig-engage` skill at `/Users/ryanrose/.claude/skills/ig-engage/`. Read those files before making structural changes to Brian's skills — the session-start checklist, Playwright tool detection, pacing rules, and rate-limit protocol are all adapted from there. Don't reinvent patterns that already exist in `ig-engage`.

## Non-negotiable rules baked into the skill content

These appear in multiple files. If you change one, grep and update all of them:

- **No em-dashes, ever.** Brian flagged this; use commas, periods, or "and". Applies to skill output AND to user-facing docs written by/for Brian.
- **Maximum 2 sentences per comment.** Hard cap. Every example in `comment-guidelines.md` must be ≤2 sentences.
- **Never mention Nations Lending** in any Instagram comment (compliance + strategy).
- **Never quote interest rates or APRs** (compliance risk).
- **Skip political, LGBTQ+, religious, controversial posts entirely** — no likes, no comments.
- **Target `@espohomeloans` business account only** — not Brian's personal `@brian_j_esposito`.
- **MMI production sweet spot: $2M–$10M.** The `lender-research` skill prioritizes this band when Brian provides an MMI export.
- **Academy Lending is gone** — do not include it in competitor lists.

When a rule changes, expect to edit ~5–10 files across both skill trees and both Python doc builders. Grep across the whole directory rather than trusting a single edit.

## Current state (as of 2026-04-22)

- `target-accounts.md` has 14 verified competitor LOs (web-researched; no MMI export yet)
- Both Word docs and the plugin zip are up to date with the "max 2 sentences" rule
- In-person setup with Brian was rescheduled; the setup guide (`Brian_Setup_Guide.docx`) is written for him to follow solo

## Voice anchors for Brian's comments

Two verbatim phrases Brian confirmed as his voice — use them as-is in examples and templates:

- VA posts: *"The hardest part is usually breaking the myth of VA lending."*
- Coaching posts: *"Coaching a new LO through their first year is the whole job."*

His broader brand voice: warm professional peer × mentor, story-driven, emoji-friendly (the `:)` matches Nations Lending's "Home loans made human :)" tagline), former PGA TOUR / TPC Head Pro (golf credibility when relevant), nickname "Espo."
