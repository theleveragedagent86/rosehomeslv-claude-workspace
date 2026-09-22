# Reddit Weekly Posts — see the subreddit-post skill

This file used to hold a full copy of the weekly Reddit posting workflow. That content has been merged into the canonical skill and corrected (the old copy used the wrong `/blogs/` blog-link pattern, listed the rotation with "Answer The Public" in the wrong slot, and pointed at memory files that do not exist).

**The authoritative version now lives at:**

`/Users/ryanrose/.claude/skills/subreddit-post/SKILL.md`

Run it with `/subreddit-post`. Do not maintain a second copy here; edit the skill instead so the two never drift apart.

## Quick reference

- **What it does:** generates the weekly batch of 21 r/VegasRealtor posts (7 content calendar + 14 blog repurpose), runs QA, and writes `Week_MonDD-MonDD_Posts.md`.
- **Tracker (rotation state):** `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Reddit/repurposed-blogs.md`
- **Blog links:** always `/blog/<slug>` (singular). `/blogs/` 404s.
- **Posting:** Ryan posts from the batch file, by hand or via `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Reddit/reddit_weekly_poster.py`.
- **Rotation:** 44 directories (DESERT SHORES, QUAIL RIDGE, SKYE CANYON folded in 2026-06-24). Full order is in the skill.
