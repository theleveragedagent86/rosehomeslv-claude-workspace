# Inbound Engagement (@rosehomeslv)

Everything for the inbound Instagram system lives in this one folder. It DMs new followers and reel-likers, and replies to comments on Ryan's own reels, all driven from a single shared tracking file.

## What's in here

| Item | What it is |
|---|---|
| `research-log.md` | **The master tracker.** Every follower, liker, and comment, with all the handles/accounts. `[ ]` = waiting, `[x]` = done. This is the file with "all the accounts and stuff." |
| `cowork-scheduler-prompts.md` | Ready-to-paste prompts for setting up the 4 daily Cowork scheduled tasks. |
| `inbound-research-plugin/` | Researcher. Scans reels/followers/likers and **appends** new items to `research-log.md`. Run first. |
| `inbound-comments-plugin/` | Replies to unchecked comments (5/reel, guardrails, leads to DMs), checks them off. |
| `inbound-dm-followers-plugin/` | DMs unchecked new followers (~15/run), checks them off. |
| `inbound-dm-likes-plugin/` | DMs unchecked reel-likers (~15/run), checks them off. |
| `zips/` | The 4 plugins zipped, ready to upload to Cowork. |
| `_archive/` | The old Playwright-based build (superseded, kept for reference). |

## How it works

1. **Research** appends new followers/likers/comments to `research-log.md` (never adds anyone already listed).
2. **Comments / Follower-DMs / Like-DMs** work only the unchecked `[ ]` items in their section, then mark each `[x]`.
3. A checked `[x]` item is done forever and never worked again. Anyone DMed as a follower is skipped as a liker, and vice versa.

## Run order

Research first (it builds the list), then the others. Cowork command names (type `/inbound` to find them):

- `/inbound-research:inbound-research`
- `/inbound-comments:inbound-comments`
- `/inbound-dm-followers:inbound-dm-followers`
- `/inbound-dm-likes:inbound-dm-likes`

## Controls

- **Caps:** ~15 DMs per run, per plugin. 5 comment replies per reel.
- **Kill switch:** create an empty file named `PAUSE` in this folder. Every plugin stops at the top of its run. Delete it to resume.
- **Eligibility:** skips realtors/brokers and obvious bots. A missing profile picture is fine.

## Current backlog (as of 2026-06-13)

- Followers waiting: **72**
- Likers waiting: **76**
- Comments waiting: **10** (includes 2 buyer leads)
- Already DMed (carried over, never re-messaged): 15
