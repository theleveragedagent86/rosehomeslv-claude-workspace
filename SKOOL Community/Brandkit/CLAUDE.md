# CLAUDE.md — The Leveraged Agent / Brandkit

**Canonical brand assets for "The Leveraged Agent"** (the Skool community brand). This is the single source of truth — copy FROM here into new projects. This is the Leveraged Agent counterpart to `hyperframes-student-kit/Rose Homes Brandkit/` (which is the *realtor* brand, a different business — do not mix them).

## The assets

| File | Size | What it actually is |
|---|---|---|
| `leveraged-agent-logo.png` | 1424 × 752 | **Horizontal wordmark.** "The Leveraged Agent" + tagline "AI workflows for working agents", dark teal type on cream with a gold subtitle and a circuit-trace motif on the right. Use for headers, outros, wide lockups. |
| `leveraged-agent-logo-small.png` | 1024 × 1024 | **Square "LA" monogram/icon** on a cream circuit-trace field. Use for avatars, profile pics, favicons, badges. |
| `leveraged-agent-youtube-banner.png` | 2560 × 1440 | YouTube channel banner. |

### Naming warning (read this)

`leveraged-agent-logo-small.png` is **not a small version of the logo** — it is the *square monogram*, at full 1024×1024. The name is misleading but is kept **on purpose**: ~44 copies of these two files are already bundled in `hyperframes-student-kit/video-projects/*/assets/`, and composition HTML references them by these exact filenames. Renaming here would break drop-in compatibility. Rename only if you also update every project that references them.

## Palette — SAMPLED, not an official spec

These hex values were **sampled from the raster artwork**, not taken from a brand guide. Treat them as approximations until Ryan sets canonical values.

| Role | Wordmark | Square monogram |
|---|---|---|
| Cream background | `#F5F2EB` | `#F5F1E6` |
| Dark teal (type / letterforms) | `#04404C` | `#104854` |
| Gold accent | `#C48424` | `#E8A030` |
| Sage/blue circuit lines | `#C0CCCC` | `#C0CCCC` |

**Known issue: the two assets are NOT color-matched.** The wordmark's teal and gold are visibly different from the monogram's (they appear to have been generated separately). A true brand guide needs one canonical teal, one canonical gold, and one canonical cream. **NOT FOUND:** official brand hex values, typeface names, clear-space/min-size rules, and dark-background logo variants. Ask Ryan before treating any of the above as authoritative.

Also note: the square monogram has a small AI-generation sparkle artifact in its bottom-right corner.

## Using these

- **New HyperFrames video project:** copy into the project's own `assets/` — projects bundle assets and reference them relatively, so they must be local:
  ```bash
  cp "/Users/ryanrose/Downloads/Claude/SKOOL Community/Brandkit/leveraged-agent-logo.png" assets/
  ```
  Do **not** symlink or reference this folder from a composition; it breaks portable renders.
- **Never** put Rose Homes LV realtor branding on Leveraged Agent material, or vice versa. Different businesses.

---

## Folder Map — keep this current

```
Brandkit/
├── CLAUDE.md                            this file
├── leveraged-agent-logo.png             1424x752 horizontal wordmark
├── leveraged-agent-logo-small.png       1024x1024 square "LA" monogram (NOT a small logo)
└── leveraged-agent-youtube-banner.png   2560x1440 channel banner
```

**Maintenance rule:** When you add, remove, or replace a brand asset here, update this map AND the parent `SKOOL Community/CLAUDE.md` map in the same change. If you replace a logo, remember the ~44 per-project copies under `hyperframes-student-kit/video-projects/*/assets/` do NOT auto-update — refresh them deliberately. Never leave the map stale.
