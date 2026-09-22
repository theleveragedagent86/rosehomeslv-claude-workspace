# Inbound Engage — Daily Schedule Reference

How the daily run is wired. The real schedule is a macOS LaunchAgent that runs `scripts/run-inbound-engage.sh` daily at 20:00. This file documents what it does and gives a Cowork-paste alternative.

## Schedule settings

- **Frequency:** Daily
- **Time:** 20:00 (8:00 PM). Different from when `ig-engage` runs.
- **Model:** Opus 4.8 (`claude-opus-4-8`).
- **Mode:** `live` (posts and DMs). Use `preview` to draft only.

## How the runner works (split sessions = compaction)

`scripts/run-inbound-engage.sh` invokes each phase as its **own** `claude` session, in order, so context is fresh between phases (stronger than a mid-run `/compact`):

```
claude -p "... follow skills/inbound-scout/SKILL.md ..."     --model claude-opus-4-8 --mcp-config scripts/mcp-playwright.json --dangerously-skip-permissions
# (only if a work-list was produced)
claude -p "... follow skills/comment-replies/SKILL.md ..."   --model claude-opus-4-8 --mcp-config scripts/mcp-playwright.json --dangerously-skip-permissions
claude -p "... follow skills/auto-dmer/SKILL.md ..."         --model claude-opus-4-8 --mcp-config scripts/mcp-playwright.json --dangerously-skip-permissions
```

State and the day's work-list pass between phases on disk. Each phase opens its own browser on the shared persistent profile, one at a time, so they never collide.

## Cowork-paste alternative (single session)

If running from the Cowork scheduler instead of the LaunchAgent, this runs all three phases in one session (no split):

```
Run the daily inbound Instagram routine for @rosehomeslv on Opus 4.8.

Read inbound-engagement-plugin/CLAUDE.md (the safety contract) first, then run /inbound-engage in LIVE mode. In one browser session it will: scout new comments on my reels, new real followers, and likers of any flagged reels; reply to up to 5 comments per reel (own reels only, ig-engage guardrails, no em-dashes); then DM new followers and reel-likers using rotated variants, the real-follower filter, the warm-up ramp, and the caps in auto-dmer/references/safety-and-caps.md.

Log every DM to state/dmed-users.json (timestamped) and output/dm-history.md so the same person is never messaged twice. Stop the whole run immediately if Instagram shows "Action Blocked", "Try Again Later", a verify page, or logs out. Flag any DM replies as live leads for me.
```

## Pause / stop

- Skip one day: `touch inbound-engagement-plugin/state/PAUSE` (delete to resume).
- Stop the schedule: `launchctl unload ~/Library/LaunchAgents/com.rosehomeslv.inbound-engage.plist`.
