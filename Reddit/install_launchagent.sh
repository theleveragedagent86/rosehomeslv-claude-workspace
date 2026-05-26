#!/bin/bash
# One-time install script for the Reddit Pipeline LaunchAgent.
# Run this once from Terminal:
#   bash /Users/ryanrose/Downloads/Claude/Reddit/install_launchagent.sh

PLIST_NAME="com.rosehomeslv.reddit-pipeline"
PLIST_SRC="/Users/ryanrose/Downloads/Claude/Reddit/${PLIST_NAME}.plist"
PLIST_DEST="$HOME/Library/LaunchAgents/${PLIST_NAME}.plist"
PIPELINE_SCRIPT="/Users/ryanrose/Downloads/Claude/Reddit/reddit_pipeline.sh"

echo ""
echo "=== Reddit Pipeline LaunchAgent Installer ==="
echo ""

# Check the source plist exists
if [ ! -f "$PLIST_SRC" ]; then
    echo "[ERROR] Plist not found at: $PLIST_SRC"
    echo "        Make sure the Reddit folder is at /Users/ryanrose/Downloads/Claude/Reddit/"
    exit 1
fi

# Make the pipeline script executable
chmod +x "$PIPELINE_SCRIPT"
echo "[OK] Made reddit_pipeline.sh executable"

# Unload existing agent if already installed
if launchctl list | grep -q "$PLIST_NAME" 2>/dev/null; then
    echo "[..] Unloading existing agent..."
    launchctl unload "$PLIST_DEST" 2>/dev/null
fi

# Copy plist to LaunchAgents
cp "$PLIST_SRC" "$PLIST_DEST"
echo "[OK] Copied plist to ~/Library/LaunchAgents/"

# Load the agent
launchctl load "$PLIST_DEST"
LOAD_EXIT=$?

echo ""
if [ $LOAD_EXIT -eq 0 ]; then
    echo "[OK] LaunchAgent installed and loaded successfully."
    echo ""
    echo "What happens now:"
    echo "  9:45 AM Mon-Fri  →  reddit_discover_api.py runs (finds real posts)"
    echo "  10:00 AM         →  Cowork scheduler reads PostDiscovery, writes DailyDrafts"
    echo "  ~10:05 AM        →  reddit_daily.py runs automatically (posts everything)"
    echo ""
    echo "Logs: /tmp/reddit_pipeline_[date].log"
    echo ""
    echo "To uninstall later:"
    echo "  launchctl unload ~/Library/LaunchAgents/${PLIST_NAME}.plist"
    echo "  rm ~/Library/LaunchAgents/${PLIST_NAME}.plist"
else
    echo "[!] launchctl load returned exit code $LOAD_EXIT"
    echo "    Try running: launchctl load $PLIST_DEST"
fi
