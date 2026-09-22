---
name: inbound-research
description: Use to research inbound Instagram activity for @rosehomeslv. Harvests new comments on Ryan's reels, new followers, and recent reel-likers, and appends them to the shared research log for the comment and DM plugins to work. Run this before the comment or DM plugins.
model: opus
---

## What This Plugin Does

This is the **researcher**. It opens `@rosehomeslv` in your real Chrome (via Cowork) and appends new inbound activity to one shared file that the other three plugins read from and check off:

`/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Inbound-Engagement/research-log.md`

It only **adds** to that file. It never replies and never DMs. It also never adds anyone or anything already in the file (checked or unchecked), which is how nobody gets worked twice.

## Start of Run (do in order)

1. **Pause check:** if `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Inbound-Engagement/PAUSE` exists, STOP and report "Paused." Do nothing else.
2. **Read the research log** at the path above. Build a set of handles already listed under Followers and Likers, and a set of comment fingerprints already under Comments. These are your "already known" sets for dedupe (match handles canonically: lowercase, ignore a leading `@`).
3. **Browser check:** you need browser control of Chrome (Cowork / Claude in Chrome). If you do not have it, STOP and tell Ryan.
4. Go to `https://www.instagram.com` and confirm you are logged in as `@rosehomeslv`. If not, STOP and ask Ryan to log in.
5. Read `./references/eligibility-and-browser.md` for the eligibility filter and the harvest mechanics.

## Harvest (append new items only)

### A. New comments on Ryan's reels
- Open `https://www.instagram.com/rosehomeslv/reels/`, open the most recent ~6 reels.
- Read each reel's comments. For each comment build a fingerprint = `reel-id + commenter-handle + a short hash of the text`.
- Skip the comment if that fingerprint is already in the Comments section, if it is Ryan's own comment, or if it is charged (political, LGBTQ+, religious, hostile) per the ig-engage guardrails.
- For each new, safe comment, append under `## Comments`:
  `- [ ] @handle on reel <reel-id> : "<comment text>" — added <today>`

### B. New followers
- Open `https://www.instagram.com/rosehomeslv/followers/` (newest first). Walk the top ~75.
- Skip anyone already under Followers (checked or unchecked). Apply the **eligibility filter** (skip realtors/brokers and obvious bots; keep regular people and non-competing businesses).
- For each new eligible follower, append under `## Followers`:
  `- [ ] @handle (<display name or "no name">) — added <today>`

### C. Recent reel-likers
- For Ryan's most recent ~6 reels, open each reel's "liked by" list.
- Skip anyone already under Likers (checked or unchecked) or already under Followers as done. Apply the eligibility filter.
- For each new eligible liker, append under `## Likers`:
  `- [ ] @handle (reel <reel-id>) — added <today>`

Append items to the **end of the matching section**, preserving everything already there. Do not reorder or uncheck anything.

## Safety

- Pace gently: a few seconds between reels and list scrolls. This is reading only, but do not hammer.
- **Stop on any block or challenge.** If Instagram shows "Action Blocked", "Try Again Later", a verify-identity / login challenge, or logs you out: STOP immediately, write a `PAUSE` file in the shared folder with the reason and time, and tell Ryan. Do not continue.

## Report

Print a short summary:
```
Research complete
- New comments added: [n]
- New followers added: [n] (skipped realtors/bots: [n])
- New likers added: [n]
- Total still waiting in log: [comments n, followers n, likers n]
```
