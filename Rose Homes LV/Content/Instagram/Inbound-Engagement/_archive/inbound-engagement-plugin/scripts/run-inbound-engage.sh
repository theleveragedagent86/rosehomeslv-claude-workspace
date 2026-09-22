#!/bin/zsh
# Daily inbound Instagram engagement runner for @rosehomeslv.
#
# Runs each phase as its OWN claude session (fresh context between phases, which is
# stronger than a mid-run /compact), in order: scout -> comment-replies -> auto-dmer.
# State and the day's work-list pass between phases on disk, so the split is safe.
#
# Model: Opus 4.8. Permission mode: blanket bypass (unattended, authorized by Ryan).
#
# Requirements at run time:
#   - Mac awake and Ryan logged into macOS (screen may be locked).
#   - @rosehomeslv logged into /Users/ryanrose/.cache/playwright-instagram-profile.
#
# Usage: run-inbound-engage.sh [live|preview]   (default: live)

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

MODE="${1:-live}"
PLUGIN_DIR="/Users/ryanrose/Downloads/Claude/inbound-engagement-plugin"
CLAUDE="/opt/homebrew/bin/claude"
MODEL="claude-opus-4-8"
MCP="$PLUGIN_DIR/scripts/mcp-playwright.json"
DAY="$(date +%Y-%m-%d)"
STAMP="$(date '+%Y-%m-%d-%H%M')"
LOG="$PLUGIN_DIR/output/run-$STAMP.log"
WORKLIST="$PLUGIN_DIR/output/worklist-$DAY.json"

cd "$PLUGIN_DIR" || exit 1

# Pause guard.
if [ -f "$PLUGIN_DIR/state/PAUSE" ]; then
  echo "[$STAMP] PAUSE file present, skipping run." >> "$LOG"
  exit 0
fi

run_phase() {
  local skill="$1"
  echo "[$(date '+%H:%M:%S')] phase: $skill (mode=$MODE, model=$MODEL)" >> "$LOG"
  "$CLAUDE" -p "The plugin root is $PLUGIN_DIR. Read and follow $PLUGIN_DIR/skills/$skill/SKILL.md now, in $MODE mode. Treat any ../.. relative paths in that file as relative to $PLUGIN_DIR/skills/$skill/. Obey the safety contract in $PLUGIN_DIR/CLAUDE.md at all times, and stop immediately if Instagram shows any block or challenge." \
    --model "$MODEL" \
    --mcp-config "$MCP" \
    --strict-mcp-config \
    --dangerously-skip-permissions >> "$LOG" 2>&1
}

# Phase 1: scout (fresh session).
run_phase "inbound-scout"

# Gate: only continue if scout produced today's work-list. This keeps the reply/DM
# phases from re-opening the browser to re-harvest when scout was blocked or empty.
if [ ! -f "$WORKLIST" ]; then
  echo "[$(date '+%H:%M:%S')] no work-list for $DAY, stopping after scout." >> "$LOG"
  exit 0
fi

# Phase 2: comment-replies (fresh session).
run_phase "comment-replies"

# Phase 3: auto-dmer (fresh session).
run_phase "auto-dmer"

echo "[$(date '+%H:%M:%S')] run complete." >> "$LOG"
