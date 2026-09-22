# CLAUDE.md — Content Channels

Faceless / personal content projects that are **not** part of Rose Homes LV, AI Clients, or the Skool community. Their own brands and voices.

- **Codename History/** — the faceless history YouTube channel (OverSimplified-style WW1/WW2 content). Driven by the `/codename-script`, `/codename-history`, and `/codename-viral` skills (installed in `~/.claude/skills/`), which reference this folder by absolute path (`transcripts/`, `scripts-work/`, `scripts-pitches/`, `episodes/`, `character-library/`, `codename-history-project-brief.md`). Its rendered `episodes/` are git-ignored (archive to SSD). Has its own `.claude` context.
- **Karpathy Autoresearch/** — a self-contained research/experiment project (its own git repo).

## Working here

- These are separate content brands. Do not apply Rose Homes LV realtor rules unless a specific asset calls for them.
- `Karpathy Autoresearch/` is a nested git repo — commit inside it, not from the workspace root.

---

## Folder Map — keep this current

```
Content Channels/
├── Codename History/        faceless history YT channel (transcripts, scripts, episodes, character-library)
└── Karpathy Autoresearch/   research project (own git repo)
```

**Maintenance rule:** When you add, remove, move, or rename a project here, update this map. If you move `Codename History/`, also update the absolute paths in the `~/.claude/skills/codename-*` skills. Never leave the map stale.
