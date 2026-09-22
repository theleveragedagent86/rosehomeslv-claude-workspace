# Diagram Type Selection

Pick the layout from the **shape of the content**, not its topic. If you cannot tell, ask the user.

---

## comparison — left vs right

**Pick this when the content has two opposing sides.** Trigger phrases:
- "X vs Y"
- "the trap/mistake" + "the framework/fix"
- "before" + "after"
- "old way" + "new way"
- "broken" + "fixed"

**Slots:**
- title
- left header (often the "wrong" side, in pink or peach)
- left items (2 to 4 boxes or labels)
- right header (often the "right" side, in mint or sky blue)
- right items (2 to 4 boxes or labels)
- footer (one-line takeaway)

**Layout:** ~1300 wide. Left column at x=80, right column at x=720, "VS" lavender circle at x=560 y=225. Header rows at y=100. Item rows starting y=180.

**Reference:** `demo_feed_growth()` in generator.py.

---

## weekly_grid — 7 day cards

**Pick this when the content is organized by day of the week.** Trigger phrases:
- "Monday/Tuesday/Wednesday..."
- "weekly content rhythm"
- "7 days, 7 X"
- "what to post each day"

**Slots:**
- title
- subtitle (optional, short tagline)
- 7 days, each with:
  - day name ("MON", "TUE"...)
  - icon (emoji)
  - post type / label
  - one-line description
  - card color (cycle through the palette)
- footer

**Layout:** 4 cards on top row (Mon to Thu), 3 cards on bottom row (Fri to Sun) centered below the top row. Card size 245 x 195. "↻ Repeat weekly" indicator below the bottom row.

**Reference:** `demo_weekly_rhythm()` in generator.py.

---

## pillars — 2 to 4 vertical pillars

**Pick this when the content names a small set of categories or principles.** Trigger phrases:
- "the 3 pillars of X"
- "the 4 categories"
- "core types"
- "the framework has X parts"

**Slots:**
- title
- 2 to 4 pillars, each with:
  - icon (emoji at top)
  - label (one-word category name, often UPPERCASE)
  - sublabel (one-line description)
  - color (cycle through palette)
- footer

**Layout:** Each pillar 140 wide x 200 tall. Gap 10. Center the row on the canvas. Icon at y+20, label at y+70, sublabel at y+100.

**Build using `pillar_box()` helper.**

---

## layered_stack — bottom-to-top stack

**Pick this when content describes building on top of something.** Trigger phrases:
- "Layer 1, Layer 2..."
- "foundation" + "built on top"
- "the stack"
- "starts with X, then Y on top"

**Slots:**
- title
- layers (bottom to top), each with:
  - layer number / name
  - description
  - color (typically gradient through palette)
- optional side notes per layer

**Layout:** Single column, ~600 wide. Each layer 80 tall, 20px gap. Bottom layer at the highest y, top layer at the lowest y. Side notes to the right at x = layer_right + 30.

**Build using `labeled_box()` helper, stacked vertically.**

---

## flowchart — branching decisions

**Pick this when content describes a process with conditionals.** Trigger phrases:
- "if X then Y"
- "step 1, step 2, then..."
- "5-minute setup"
- "decision tree"

**Slots:**
- title
- nodes (rectangles for steps, diamonds for decisions)
- connections (arrows with optional labels)
- start and end markers

**Layout:** Top-down or left-to-right. Diamonds for decisions, rectangles for actions, ellipses for start/end. Use `connect()` helper to wire elements.

**Build using `rect()`, `diamond()`, `ellipse()`, and `connect()` primitives.**

---

## Color assignment heuristic

When picking colors for the slots, alternate to avoid monotony:

- **Comparison:** left side in pink/peach (the "trap"), right side in mint/sky_blue (the "fix"). VS circle in lavender.
- **Weekly grid:** rotate through `[sky_blue, peach, yellow, mint, lavender, coral, pink]` for Mon to Sun.
- **Pillars:** start with sky_blue, then peach, then yellow (matches the demo).
- **Layered stack:** start at the bottom with peach, then yellow, mint, lavender (warmer at the base, cooler at the top).
- **Flowchart:** rectangles in mint or sky_blue, diamonds in lavender, end states in peach (success) or pink (failure).

---

## When to ask vs guess

Ask the user if:
- The content could fit two diagram types equally well
- The content has more than 8 distinct items (won't fit cleanly in any of these layouts)
- The user's input is vague ("make a graphic about X")

Guess if:
- The content has obvious shape signals (days of week, "vs", numbered layers, etc.)
- The user explicitly said the diagram type
