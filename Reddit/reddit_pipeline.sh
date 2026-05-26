#!/bin/bash
# Reddit Daily Pipeline
# Runs automatically at 9:45 AM on weekdays via LaunchAgent.
#
# Flow:
#   1. Run reddit_discover_api.py  → saves PostDiscovery_[date].md (~2-3 min)
#   2. Cowork scheduler (10:00 AM) reads PostDiscovery, writes DailyDrafts_[date].md
#   3. This script polls for DailyDrafts, then runs reddit_daily.py when it appears

REDDIT_DIR="/Users/ryanrose/Downloads/Claude/Reddit"
LOG_DIR="/tmp"
DATE_TAG=$(date +%Y%m%d)
DATE_MON=$(date +%b%d)   # e.g., Mar15
DATE_YEAR=$(date +%Y)

DISCOVERY_FILE="$REDDIT_DIR/PostDiscovery_${DATE_MON}_${DATE_YEAR}.md"
DRAFTS_FILE="$REDDIT_DIR/DailyDrafts_${DATE_MON}_${DATE_YEAR}.md"
PIPELINE_LOG="$LOG_DIR/reddit_pipeline_${DATE_TAG}.log"

log() {
    echo "[$(date '+%H:%M:%S')] $1" | tee -a "$PIPELINE_LOG"
}

# ── STEP 1: Run discovery ──────────────────────────────────────────────────────

log "=== REDDIT PIPELINE STARTED ==="
log "Discovery file: $DISCOVERY_FILE"
log "Drafts file:    $DRAFTS_FILE"
log ""

if [ -f "$DISCOVERY_FILE" ]; then
    log "[SKIP] PostDiscovery file already exists for today. Skipping discovery."
else
    log "[1/3] Running reddit_discover_api.py..."
    python3 "$REDDIT_DIR/reddit_discover_api.py" >> "$PIPELINE_LOG" 2>&1
    DISCOVER_EXIT=$?

    if [ $DISCOVER_EXIT -eq 0 ]; then
        log "[OK]  Discovery complete. PostDiscovery file saved."
    else
        log "[!]  Discovery script exited with code $DISCOVER_EXIT."
        log "     Cowork will fall back to search query mode."
    fi
fi

# ── STEP 2: Wait for Cowork to write DailyDrafts ──────────────────────────────

log ""
log "[2/3] Waiting for Cowork to generate DailyDrafts..."
log "      Polling every 30s, up to 45 minutes."

MAX_WAIT=2700   # 45 minutes in seconds
WAITED=0
POLL_INTERVAL=30

while [ ! -f "$DRAFTS_FILE" ]; do
    if [ $WAITED -ge $MAX_WAIT ]; then
        log "[!]  Timed out waiting for DailyDrafts after ${MAX_WAIT}s."
        log "     Run manually: python3 $REDDIT_DIR/reddit_daily.py"
        exit 1
    fi
    sleep $POLL_INTERVAL
    WAITED=$((WAITED + POLL_INTERVAL))
    log "      Still waiting... (${WAITED}s elapsed)"
done

log "[OK]  DailyDrafts file found."
log "      Waiting 60s for file to finish writing..."
sleep 60

# ── STEP 3: Run the poster ─────────────────────────────────────────────────────

log ""
log "[3/3] Running reddit_daily.py..."
python3 "$REDDIT_DIR/reddit_daily.py" --non-interactive >> "$PIPELINE_LOG" 2>&1
POSTER_EXIT=$?

log ""
if [ $POSTER_EXIT -eq 0 ]; then
    log "[OK]  Poster finished successfully."
else
    log "[!]  Poster exited with code $POSTER_EXIT. Check log for details."
fi

log ""
log "=== PIPELINE COMPLETE ==="
log "Full log: $PIPELINE_LOG"
