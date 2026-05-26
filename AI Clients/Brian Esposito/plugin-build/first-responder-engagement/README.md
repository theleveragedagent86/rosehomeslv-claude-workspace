# First Responder Engagement Plugin

Instagram community presence engagement with Las Vegas first responders for genuine relationship building.

## Built For

Brian J. Esposito, Branch Manager, Nations Lending, Las Vegas NV (NMLS #1535781)

## What This Plugin Does

Two skills that help Brian build authentic community presence with Vegas-area first responders (military/veterans, police, fire/EMS, healthcare). The goal is community-building, NOT lead generation. Brian's voice in these comments is a 28-year Vegas neighbor and Par for the Cure founder, never a mortgage lender.

### /responder-comments (daily community presence)
- Visits target Vegas-area first responder Instagram profiles
- Likes posts and select aligned comments
- Writes 1-2 sentence community-presence comments in Brian's voice
- Acknowledges service genuinely without pitching anything
- Saves a session log after each run
- **Trigger:** "run responder-comments," "engage on first responder posts," "community presence routine"

### /responder-research (target list builder)
- Discovers Vegas-area first responder Instagram accounts via hashtag mining and bio searches
- Verifies accounts are active, public, and not primarily political
- Maintains category balance across all four responder types
- Updates the shared target-accounts.md list
- **Trigger:** "run responder-research," "find new first responders," "refresh responder list"

## Critical Rule

**Comments NEVER mention mortgages, lending, Nations Lending, VA loans, hero programs, or any business.** Not subtle, not implicit, not "as a community member who works in housing." Never. The implicit business benefit (top-of-mind for VA loans / hero programs / referrals someday) is downstream and indirect. Reaching for it directly would destroy the strategy.

## Combined Use With lender-engagement Plugin

This plugin runs on the same @espohomeloans account as the `lender-engagement` plugin. To stay under Instagram's natural-engagement thresholds:

- Combined daily comments: target ~30 max
- Schedule the two skills at different times of day
- If lender-comments has already run heavy today, run responder-comments lighter (5-10 posts)
- The two plugins share the same Playwright MCP server (`playwright-instagram`), so login is shared

## Installation

1. Install this plugin in Claude Code or Cowork
2. The Playwright MCP server is configured automatically (or reused if lender-engagement is already installed)
3. First time only: log into Instagram as @espohomeloans in the Playwright browser
4. Populate target-accounts.md by running `/responder-research`

## Requirements

- Claude Code or Cowork
- Node.js 18+ (for Playwright MCP)
- Instagram account (@espohomeloans) logged in

## Plugin Structure

```
first-responder-engagement/
├── .claude-plugin/
│   └── plugin.json                    (manifest + MCP config)
├── skills/
│   ├── responder-comments/
│   │   ├── SKILL.md                   (main skill)
│   │   ├── target-accounts.md         (responder target list)
│   │   └── references/
│   │       ├── comment-guidelines.md  (voice + examples by post type)
│   │       ├── browser-playbook.md    (IG automation playbook)
│   │       ├── playwright-setup.md    (MCP install guide)
│   │       └── daily-schedule-prompt.md (Cowork scheduler prompt)
│   └── responder-research/
│       ├── SKILL.md                   (main skill)
│       └── references/
│           └── research-methodology.md (sources + verification)
└── README.md
```

## Author

Ryan Rose, Rose Homes LV (ryan@rosehomeslv.com)
