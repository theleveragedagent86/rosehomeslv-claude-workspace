# CLAUDE.md, Mentor-Mining

Structured teardowns of the creators Ryan treats as unofficial mentors, turned into content Ryan can actually make. One subfolder per mentor. First run was Nick Saraev, 2026-08-03.

## What this is for

Ryan runs **The Leveraged Agent**, teaching realtors to run their business with AI. Mentors like Saraev make content for a different audience (aspiring AI-automation solopreneurs). The job here is not to summarize them. It is to extract the transferable system and the transferable packaging, and to be honest about what does not transfer.

## The pipeline

| Phase | Output | What it does |
|---|---|---|
| A | `<mentor>/00-corpus.csv` | Every video with views, likes, comments, duration, upload date, views/day. `yt-dlp --flat-playlist` for ids, then per-video `--print` for full metadata. |
| B | `<mentor>/01-deep-reads/` | One file per selected video, identical 9-section schema, fanned out across parallel subagents. |
| C | `<mentor>/02-patterns.md` | The repeatable formula. Hook mechanisms and title formulas ranked by median views/day, age-controlled. |
| D | `<mentor>/03-translation-matrix.md` | THE asset. One row per system: mentor system, realtor equivalent, whether Ryan already built it, module fit, effort, angle. |
| E | `content-queue.md` | Top rows turned into shootable angles. Lives at this level, not per-mentor, so mentors can feed one queue. |

## Rules that make the output trustworthy

1. **`ryan-built-inventory.md` is the gate.** A matrix row may only be marked `YES` if it names a specific skill or plugin from that file. A false YES is the worst possible error here, because Ryan's whole credibility with agents is "I run this in a real Vegas brokerage," not "I watched a video about it."
2. **`_System/plugins/` is NOT proof something runs.** Those are dev/source copies. Running versions live in `~/.claude/skills/` and `~/.claude/plugins/marketplaces/local-desktop-app-uploads/`. Verify on disk before marking anything live. `listing-description` was caught this way: written, never installed.
3. **Views/day is confounded by publish date.** Spearman age vs views/day on the Saraev corpus was **-0.737**. Never compare medians across eras without controlling for cohort year. Every table in `02-patterns.md` carries an age column for this reason.
4. **Do not select the deep-read set by raw velocity.** It over-selects recent tool-reaction videos that rot in weeks and translate to nothing. Stratify: transferable systems, packaging craft, teaching format, and thesis-critical.
5. **NO is a legitimate verdict.** A catalog of honest NOs beats a padded matrix. Stretches go in the "what does not transfer" section, never in the matrix.
6. **Compliance is not optional.** Ryan is licensed. Flag DNC/TCPA, MLS data-use, fair housing and Meta Special Ad Category, Nevada license advertising, RESPA Section 8, and FTC review-gating inline on any row that touches them.
7. **No em-dashes.** Workspace-wide rule.

## Re-running or adding a mentor

The manual pipeline above is the source of truth. It has been run once end to end. Codifying it into a skill via `skill-builder` is the intended next step, and the artifacts here are the spec for that skill. Nate Herk is the intended first test of whether it generalizes.

Transcripts need `yt-dlp` (installed 2026-08-03 via Homebrew). YouTube's `timedtext` endpoint returns 200 with zero bytes to a plain fetch, so browser scraping is not a viable substitute at scale.

---

## Folder Map, keep this current

```
Mentor-Mining/
├── CLAUDE.md                   this file
├── ryan-built-inventory.md     ground truth for the "Ryan built it?" column, gates every YES
├── content-queue.md            top 10 shootable angles, all gated on systems Ryan actually runs
└── saraev/                     Nick Saraev (488K subs, 303 long-form videos, run 2026-08-03)
    ├── 00-corpus.csv           all 303 videos ranked by views/day
    ├── 01-deep-reads/          38 files, `<tier>-<video_id>.md`, tiers T1-SYSTEM / T2-PACKAGING / T3-TEACHING / T4-THESIS
    ├── 02-patterns.md          the queryable Saraev formula, age-controlled
    └── 03-translation-matrix.md  58 rows, the honest gaps, and the "don't sell AI to local businesses" assessment
```

**Maintenance rule:** When you add a mentor, add a subfolder here and a line in this map, and update the parent [../CLAUDE.md](../CLAUDE.md). Never leave the map stale.
