# CLAUDE.md — Content Channels

Faceless / personal content projects that are **not** part of Rose Homes LV, AI Clients, or the Skool community. Their own brands and voices.

- **Codename History/** — the faceless history YouTube channel (OverSimplified-style WW1/WW2 content). Driven by the `/codename-script`, `/codename-history`, and `/codename-viral` skills (installed in `~/.claude/skills/`), which reference this folder by absolute path (`transcripts/`, `scripts-work/`, `scripts-pitches/`, `episodes/`, `character-library/`, `codename-history-project-brief.md`). Its rendered `episodes/` are git-ignored (archive to SSD). Has its own `.claude` context.
- **Karpathy Autoresearch/** — a self-contained research/experiment project (its own git repo).

**Shorts publishing state lives in git, not just YouTube.** `Codename History/episodes/shorts-queue.md` holds the channel-wide cadence rule and the long-video table, and `Codename History/episodes/_schedule/` holds the dated schedule builds (`shorts-schedule-<date>.md` = the day grid plus per-Short title/description/tags, `draft-ids.md` = YouTube video IDs and Studio edit links). `_schedule/` is checked in even though the rest of `episodes/` is git-ignored, because it is text and it is the only record of what is scheduled where. Current rule, set 27 Aug 2026: 3 Shorts a day at 12:00 AM / 12:00 PM / 6:00 PM, never two from the same story on one day.

## Working here

- These are separate content brands. Do not apply Rose Homes LV realtor rules unless a specific asset calls for them.
- `Karpathy Autoresearch/` is a nested git repo — commit inside it, not from the workspace root.

---

## Folder Map — keep this current

```
Content Channels/
├── Codename History/        faceless history YT channel (transcripts, scripts, episodes, character-library)
│   └── episodes/_schedule/  checked-in Shorts schedule builds + YouTube draft IDs
└── Karpathy Autoresearch/   research project (own git repo)
```

**Maintenance rule:** When you add, remove, move, or rename a project here, update this map. If you move `Codename History/`, also update the absolute paths in the `~/.claude/skills/codename-*` skills. Never leave the map stale.
