# Cowork Scheduler Prompts (@rosehomeslv inbound engagement)

Four separate scheduled tasks, one per plugin. Suggested staggered times so the account is not doing everything in one burst. Research runs first (it builds the list the others work from).

| Time (suggested) | Task | Cowork slash command |
|------------------|------|---------------|
| 8:00 AM | Research | `/inbound-research:inbound-research` |
| 9:30 AM | Comments | `/inbound-comments:inbound-comments` |
| 12:00 PM | Follower DMs | `/inbound-dm-followers:inbound-dm-followers` |
| 3:00 PM | Like DMs | `/inbound-dm-likes:inbound-dm-likes` |

> Cowork namespaces plugin commands as `/plugin-name:skill-name`. Easiest path: type `/inbound` and all four show up in the autocomplete menu. The natural-language scheduled prompts below also trigger the right skill on their own, so they work as written.

Shared tracking lives in this folder: `research-log.md` (the master list), `dm-history.md` (every DM sent), `leads.md` (people to follow up with), and `PAUSE` (create this file to stop everything).

---

## 1. Research (8:00 AM daily)

```
Run the /inbound-research skill now, in Chrome, for @rosehomeslv. Append today's new comments, new followers, and recent reel-likers to the shared research log at /Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Inbound-Engagement/research-log.md, skipping anyone or anything already listed. If a PAUSE file exists in that folder, stop and tell me. Stop immediately if Instagram shows any block, challenge, or login prompt. Give me a short summary when done.
```

## 2. Comments (9:30 AM daily)

```
Run the /inbound-comments skill now, in Chrome, for @rosehomeslv. Reply to the unchecked comments in the research log, up to 5 per reel, following Ryan's rules: skip anything political or charged, no em-dashes, verify any teamwork claim against the Transactions records before affirming it, and send leads to my DMs. Check each comment off when done. If a PAUSE file exists, stop. Stop immediately on any Instagram block or challenge and tell me. Short summary when done.
```

## 3. Follower DMs (12:00 PM daily)

```
Run the /inbound-dm-followers skill now, in Chrome, for @rosehomeslv. DM up to 15 of the unchecked new followers in the research log a rotated welcome message, oldest first, skipping realtors/brokers and bots, pacing 60 to 120 seconds between DMs. Check each one off the instant it sends so nobody is ever messaged twice. If a PAUSE file exists, stop. Stop immediately on any Instagram block or challenge and tell me. Short summary when done.
```

## 4. Like DMs (3:00 PM daily)

```
Run the /inbound-dm-likes skill now, in Chrome, for @rosehomeslv. DM up to 15 of the unchecked reel-likers in the research log a rotated thank-you message, oldest first, skipping realtors/brokers, bots, and anyone already messaged, pacing 60 to 120 seconds between DMs. Check each one off the instant it sends. If a PAUSE file exists, stop. Stop immediately on any Instagram block or challenge and tell me. Short summary when done.
```

---

## Notes
- Run **research before** comments/DMs each day (it builds the list).
- Each DM plugin sends at most 15 per run. Anyone over the cap or not reached stays `[ ]` and is picked up next run, oldest first, so the list drains in order.
- To pause everything for a day: create an empty file named `PAUSE` in this folder. Delete it to resume.
- Anyone already messaged (including the 15 from before) is checked off in `research-log.md` and will never be DMed again.
