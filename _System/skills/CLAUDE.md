# CLAUDE.md — _System / skills

Standalone skill source copies (dev). The running skills live in `~/.claude/skills/<name>/`. Editing a copy here does not change the live skill unless you sync it. See [../CLAUDE.md](../CLAUDE.md) for path-safety.

---

## Folder Map — keep this current

```
skills/
├── blog-writer/           expired-content/     listing-marketing/
├── publish-blogs/         reverse-prospecting/ skill-builder/
├── Reddit/                Listing Marketing Plan/
├── listing-video/         listing photos -> 9:16 reel w/ black green-screen half; curates the shots, then
│                          calls ../tools/listing-video/listing_video.py to render
├── yt-thumbnail/          YouTube thumbnails: strategy brief -> Higgsfield plate + face
│   ├── SKILL.md           -> HTML/CSS brand layer -> Playwright render + 120px squint proof
│   ├── render.mjs         Playwright renderer; resolves playwright from hyperframes-student-kit
│   ├── brands/            rose-homes.json + leveraged-agent.json (NEVER mix the two)
│   ├── templates/         face-right.html, big-number.html, vs-split.html
│   ├── references/        strategy-brief.md, design-rules.md, refresh-loop.md
│   └── assets/            ryan-cutout.png (RGBA, chest-up, smiling — the only stock expression)
├── skool-carousel/        Leveraged Agent (Skool) IG carousels for an AGENT audience:
│   ├── SKILL.md           cover hook x3 -> slides 2-8 (20-word cap) -> CTA slide -> caption
│   │                      -> Claude Design brief -> AUTOMATION PACK. Grounded in
│   │                      Mentor-Mining/ryan-built-inventory.md (proof rule) + Brandkit
│   │                      palette. NOT Rose Homes LV, that is ig-carousel.
│   └── references/
│       ├── design-loop-prompt.md  measured Vector brand DNA (hex/type/grid/radius/shadow/
│       │                  SAFE AREA) + 3-lens critic loop (brief-fit, brand, craft), pasted
│       │                  after the DESIGN BRIEF into Claude Design. Mirrors tokens.json,
│       │                  keep in sync.
│       ├── check-slides.mjs  added 2026-09-11. Playwright: renders each *.dc.html slide to
│       │                  png/ at 1080x1350 and MEASURES every element against the 4:5 safe
│       │                  band (y 135..1215, the centred 1:1 profile-grid crop). Exits 1 and
│       │                  names the offender. Run it whenever slides are actually rendered;
│       │                  a visual read is not evidence. Uses the Playwright in
│       │                  SKOOL Community/hyperframes-student-kit/node_modules/.
│       └── manychat-flow.md  the keyword-CTA automation architecture: comment trigger ->
│                          rotated public reply -> DM sequence (1000-char IG cap) -> 3-button
│                          branch -> tags -> 24h follow-up. Also the ManyChat build order for
│                          driving the browser. Ryan does signup/payment/IG OAuth himself.
├── coach-teardown/        Leveraged Agent COMPETITOR RESEARCH. Ryan gives a realtor-coach IG
│   ├── SKILL.md           handle, this harvests every post/comment/liker via IG's own web API
│   │                      from a logged-in Chrome, reverse-engineers the funnel mechanic, and
│   │                      cuts ranked DM lists A-E + TOP-300. Their coaching clients ARE Ryan's
│   │                      Skool avatar. Output: SKOOL Community/Instagram/Competitor-Research/.
│   └── references/        harvest.md = the exact browser code (window.__job pattern to dodge the
│                          45s CDP timeout, x-csrftoken for likers, the has_more_headload_comments
│                          pagination fix, 6-worker pool, Blob-to-disk so raw rows never hit
│                          context). analysis.md = RE regex, topic classifier, CTA-lift table,
│                          TOP-300 scoring. newsletter.md = the EMAIL half, where coaches actually
│                          sell, incl. mining their paid-room curriculum. output-templates.md =
│                          the README / 10-section teardown / catalogue / CSV schemas.
│                          Reference implementation: the Peyson-Robertson teardown.
├── yt-shorts-publish/     Rose Homes LV YouTube SHORTS: parse titles/descriptions/tags from a folder
│   ├── SKILL.md           Ryan names, normalize (contact block, #Shorts, no em-dashes), build
│   │                      schedule.md from times Ryan gives, then fill + schedule each draft in
│   │                      YouTube Studio via claude-in-chrome. Phase-B twin of /codename-history.
│   └── references/        metadata-format.md (fields, description template, schedule.md layout),
│                          publish-automation.md (Studio click steps, focus checks, verify)
├── rose-report/           The Rose Report weekly Thursday newsletter (Rose Homes LV, beehiiv). Routine:
│   ├── SKILL.md           update LAST week's web post with live reel links -> build this week's issue
│   │                      from /local-news research + "Missed last week?" catch-up line -> beehiiv
│   │                      snippet -> draft. Never sends/tests/schedules without Ryan's yes.
│   ├── scripts/           swap_reels.py (Pxx marker -> live reel link, both HTML files),
│   │                      beehiiv.py (list/get/create/update; key from Keychain; create+update Max-only)
│   └── references/        beehiiv.md (plan limits, what beehiiv strips, snippet rules, browser paste flow)
```

**`rose-report` is live as a symlink**, `~/.claude/skills/rose-report` → this folder. Issues live in
`Rose Homes LV/Marketing/Newsletter/issues/<send-date>/`; if that moves, update the Paths table in its SKILL.md.

**`skool-carousel` and `coach-teardown` are live as symlinks**, `~/.claude/skills/<name>` → this folder.
It reads grounding files by absolute path from `SKOOL Community/`, so if that folder moves,
update the table in its SKILL.md.

**`yt-thumbnail` is live as a symlink**, `~/.claude/skills/yt-thumbnail` → this folder, so
edits here take effect immediately with no sync step. It also depends on two things
outside itself: Playwright in `SKOOL Community/hyperframes-student-kit/node_modules`, and
the Higgsfield MCP Element `cf5b602a-f8b4-41da-9568-b13356f3d77b` (`ryan-rose`) for
generating alternate facial expressions.

**Maintenance rule:** When you add/remove a skill source, update this map. Keep it in sync with the live `~/.claude/skills/` copy when the change should go live. Never leave the map stale.
