---
name: excalidraw
description: Use when someone asks to create an excalidraw graphic, generate a hand-drawn whiteboard infographic, build educational content graphics, visualize a transcript or framework, or make an "excalidraw-style" diagram. Produces a native .excalidraw JSON file that drops into excalidraw.com with Virgil font, hachure fills, and pastel palette baked in.
argument-hint: "transcript, content brief, or diagram description"
---

## What This Skill Does

Generates **native `.excalidraw` JSON files** from a transcript or content brief. The file drops into excalidraw.com (or any Excalidraw instance) and renders pixel-perfect because the output IS Excalidraw — not an approximation.

Output is always:
- Hand-drawn Virgil font (`fontFamily: 1`)
- Hachure (sketchy) fill style
- Excalidraw pastel palette (sky blue, mint, lavender, pink, yellow, peach, coral)
- White background, sentence-cased labels
- No em dashes anywhere
- Fully editable after import (drag boxes, swap colors, fix typos)

**Supporting files in this skill directory:**
- [generator.py](generator.py) — Python module with element factories and templates
- [diagram-types.md](diagram-types.md) — How to pick the right layout from content shape
- [cowork-loader.md](cowork-loader.md) — Optional: load directly into excalidraw.com via Chrome MCP

---

## Workflow

### Step 1: Parse the input

The user gives you a transcript, framework, or short description. Extract:

1. **Title** — the core idea, 2 to 7 words
2. **Diagram type** — pick from these five (see [diagram-types.md](diagram-types.md) for selection rules):
   - `comparison` — left vs right contrast (e.g. "trap" vs "framework", "before" vs "after")
   - `weekly_grid` — 7 day cards (Mon to Sun)
   - `pillars` — 2 to 4 vertical pillars with icon, label, sublabel
   - `layered_stack` — bottom-to-top stacked layers (Layer 1, Layer 2, etc.)
   - `flowchart` — decision branches with diamonds and arrows
3. **Structured content** — fill the slots for the chosen diagram type
4. **Footer** — one optional one-line takeaway

If you cannot tell which diagram type fits, ask the user. Do not guess.

### Step 2: Write a build script

Create `/tmp/build_excalidraw.py` that imports the generator and constructs the elements. Pattern:

```python
import sys
sys.path.insert(0, '/Users/ryanrose/Downloads/Claude/excalidraw-plugin/skills/excalidraw')
from generator import (
    PALETTE, GRAY,
    rect, text, arrow, diamond, ellipse,
    labeled_box, day_card, pillar_box, standalone_text,
    save, _reset,
)

_reset()
els = []

# ... build elements here using the helpers ...

save(els, '/Users/ryanrose/Downloads/Claude/<slug>.excalidraw')
```

Use a kebab-case slug for the filename (e.g. `feed-growth.excalidraw`, `weekly-rhythm.excalidraw`).

### Step 3: Run the script

```bash
python3 /tmp/build_excalidraw.py
```

Verify the file saved to `/Users/ryanrose/Downloads/Claude/<slug>.excalidraw` and the elements count looks right (typically 20 to 50 elements).

### Step 4: Validate

Run a quick sanity check:

```bash
python3 -c "
import json
with open('/Users/ryanrose/Downloads/Claude/<slug>.excalidraw') as f:
    doc = json.load(f)
els = doc['elements']
ids = {e['id'] for e in els}
em = sum(1 for e in els if e.get('text') and ('—' in e['text'] or '–' in e['text']))
bad = 0
for e in els:
    for ref in ['containerId']:
        if e.get(ref) and e[ref] not in ids: bad += 1
    for b in (e.get('boundElements') or []):
        if b['id'] not in ids: bad += 1
print(f'{len(els)} elements, dupes={len(els)-len(ids)}, bad_refs={bad}, em_dashes={em}')
"
```

All counts should be 0 except for the element count.

### Step 5: Hand off

Tell the user:
1. The file path (with markdown link)
2. To drag the file into [excalidraw.com](https://excalidraw.com)
3. Offer to load it directly if Chrome MCP is available (see [cowork-loader.md](cowork-loader.md))

---

## Generator API (cheat sheet)

```python
# Palette
PALETTE["sky_blue"]   # "#a5d8ff"
PALETTE["mint"]       # "#b2f2bb"
PALETTE["lavender"]   # "#d0bfff"
PALETTE["pink"]       # "#ffc9c9"
PALETTE["yellow"]     # "#ffec99"
PALETTE["peach"]      # "#ffd8a8"
PALETTE["coral"]      # "#ffa8a8"
PALETTE["purple"]     # "#eebefa"
GRAY                  # "#868e96" — for subtitles/footers

# Composite helpers (the ones you usually want)
labeled_box(x, y, w, h, bg, label, size=24)    # → ([elements], rect_id)
pillar_box(x, y, w, h, bg, icon, label, sub)   # → [elements]
day_card(x, y, w, h, bg, day, icon, type, desc) # → [elements]
standalone_text(cx, y, content, size=20, color=STROKE)  # → text element
connect(elements, src_id, dst_id, src_face, dst_face)   # → arrow

# Raw primitives
rect(x, y, w, h, bg, **kw)
text(x, y, content, size, align, **kw)
arrow(x, y, points, **kw)
diamond(x, y, w, h, bg, **kw)
ellipse(x, y, w, h, bg, **kw)
```

**Coordinate system:** top-left origin, y grows downward. Excalidraw auto-zooms to fit on import, so absolute coordinates are fine. Typical canvas: 1200 to 1400 wide.

**Title position convention:** centered at `CX, 25` with `size=36`.

---

## Brand Rules (always)

- **No em dashes.** The generator strips them automatically, but keep the input clean.
- **Sentence case** on labels and headers. Not Title Case, not ALL CAPS (except for short emphatic labels like "MON" or "LISTINGS").
- **Pastel only.** Never use saturated colors. The palette above is the entire menu.
- **Hachure fill** on every shape. Set automatically by the helpers.
- **Footer is optional.** One short takeaway. If the content does not have a clear takeaway, skip it.

---

## Examples

Two reference graphics ship with this skill — see [generator.py](generator.py) `demo_feed_growth()` and `demo_weekly_rhythm()` at the bottom of the file. Run either with:

```bash
python3 /Users/ryanrose/Downloads/Claude/excalidraw-plugin/skills/excalidraw/generator.py demo1
python3 /Users/ryanrose/Downloads/Claude/excalidraw-plugin/skills/excalidraw/generator.py demo2
```

These produce `feed-growth.excalidraw` and `weekly-rhythm.excalidraw` in the script's directory. Read them as canonical examples of how to assemble a comparison and a weekly grid respectively.
