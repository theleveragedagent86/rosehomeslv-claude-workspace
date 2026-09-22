# Inbound Engagement Plugin

Automated **inbound** Instagram engagement for `@rosehomeslv`. Replies to comments on Ryan's reels and DMs new followers and reel-likers, using a real logged-in browser (Playwright MCP). Runs on a daily local schedule.

This is the inbound counterpart to the `ig-engage` skill (which is outbound). Read `CLAUDE.md` before anything else. It is the safety contract.

## What it does

| Skill | Job |
|-------|-----|
| `/inbound-engage` | Daily orchestrator. Runs the other three in order, in one browser session. **This is the entry point.** |
| `/inbound-scout` | Harvests new comments on Ryan's reels, new real followers, and likers of flagged reels. |
| `/comment-replies` | Replies to up to 5 comments per reel. |
| `/auto-dmer` | DMs new followers and reel-likers, with rotated message variants and a real-follower filter. |

## One-time setup

1. **Install the plugin** in Claude Code / Cowork (or drop this folder where your other plugins live). The `playwright-instagram` MCP server auto-registers from `.claude-plugin/plugin.json`.
2. **Log in once.** The MCP uses a persistent browser profile at `~/.cache/playwright-instagram-profile` (the same one `ig-engage` uses). Open that browser, go to instagram.com, and log into `@rosehomeslv`. The session persists, so you only do this once (re-do it if Instagram logs you out).
3. **Confirm browser tools are available.** The skills look for `browser_navigate`, `browser_snapshot`, etc. If they are missing, the MCP is not connected.

## Running it

**Always start in preview mode.** Preview harvests the real lists and drafts every reply and DM to `output/PREVIEW-<date>.md` without posting:

```
/inbound-engage preview
```

Review the draft. Check that the harvested followers/likers/comments are right, the message variants sound like Ryan, and the real-follower filter is catching bots. When happy:

```
/inbound-engage live
```

Live mode posts, paces itself, and respects the daily caps and warm-up ramp in `skills/auto-dmer/references/safety-and-caps.md`.

## Daily schedule (local, 8:00 PM, Opus 4.8)

The run lives on Ryan's Mac. It does NOT need the laptop on 24/7, only awake at 8:00 PM and Ryan logged into macOS.

The runner (`scripts/run-inbound-engage.sh`) runs each phase as its own Opus 4.8 session, in order: scout, then comment-replies, then auto-dmer. Fresh context between phases (stronger than `/compact`); state passes on disk. It is configured **live** (`scripts/com.rosehomeslv.inbound-engage.plist`, daily 20:00) and uses `--dangerously-skip-permissions` so it never stalls unattended.

**The files are staged and ready, but NOT armed.** Installing a standing, permission-bypassing automation that DMs strangers is a switch only you should throw, so you run the arm commands yourself.

### Before you arm it (one-time)

- **Log @rosehomeslv into the browser profile** at `/Users/ryanrose/.cache/playwright-instagram-profile`. The unattended run cannot pause for a login, so this must be done first. Run the helper, log in, and close the window:
  ```
  zsh "/Users/ryanrose/Downloads/Claude/inbound-engagement-plugin/scripts/login-once.sh"
  ```
- **Do one manual run first** to confirm the browser, login, and MCP work end to end (recommended even though the schedule is live):
  ```
  /Users/ryanrose/Downloads/Claude/inbound-engagement-plugin/scripts/run-inbound-engage.sh preview
  ```
  Then read `output/PREVIEW-<date>.md`.

### Arm it (you run these)

```
chmod +x "/Users/ryanrose/Downloads/Claude/inbound-engagement-plugin/scripts/run-inbound-engage.sh"
cp "/Users/ryanrose/Downloads/Claude/inbound-engagement-plugin/scripts/com.rosehomeslv.inbound-engage.plist" ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.rosehomeslv.inbound-engage.plist
launchctl list | grep rosehomeslv      # confirm it loaded
```

Optional, so the Mac wakes for the run even if asleep (needs your password):
```
sudo pmset repeat wake MTWRFSU 19:58:00
```

It will first fire at the next 20:00. Since the plist arg is `live`, that run posts and DMs.

### Switch to preview later

Change the second arg in the plist `ProgramArguments` from `live` to `preview`, then reload:
```
launchctl unload ~/Library/LaunchAgents/com.rosehomeslv.inbound-engage.plist
launchctl load ~/Library/LaunchAgents/com.rosehomeslv.inbound-engage.plist
```

## Kill-switch

- **Pause one run:** `touch state/PAUSE` (delete the file to resume).
- **Stop the schedule entirely:** `launchctl unload ~/Library/LaunchAgents/com.rosehomeslv.inbound-engage.plist`
- **If Instagram throws a block or challenge:** the run stops itself, saves state, and waits 24h. Do not force it back on.

## Where things are

- Logs: `output/<date>.md` (and `output/PREVIEW-<date>.md` for preview runs).
- Runtime state (never committed): `state/`.
- Flag a reel for liker-DMs: add its URL to `state/target-reels.md`. Empty file = liker-DM stays idle.
- Message templates and variants: `skills/auto-dmer/references/dm-templates.md`.

## What is intentionally not here

Sharer-DM was cut. Instagram does not reveal who shares a reel via DM, so there is no one to target. See `CLAUDE.md`.
