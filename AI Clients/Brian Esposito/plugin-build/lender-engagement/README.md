# Lender Engagement Plugin

Instagram engagement automation for mortgage branch recruiting via value-provided marketing.

## Built For

Brian J. Esposito, Branch Manager, Nations Lending, Las Vegas NV (NMLS #1535781)

## What This Plugin Does

Two skills that automate Brian's daily Instagram engagement strategy to build name recognition with competitor mortgage loan officers in Las Vegas, Henderson, and Clark County.

### /lender-comments (daily engagement engine)
- Visits target competitor LO Instagram profiles
- Likes posts and top comments
- Writes 1-2 sentence value-add comments in Brian's voice (hard cap at 2)
- Paces itself naturally to avoid rate limits
- Saves a session log after each run
- **Trigger:** "run lender-comments," "engage on lender posts," "daily IG routine"

### /lender-research (target list builder)
- Discovers competitor LOs with active Instagram accounts
- Integrates with MMI production data ($2M-$10M sweet spot)
- Verifies accounts are active, public, and not at Nations Lending
- Updates the shared target-accounts.md list
- **Trigger:** "run lender-research," "find new LOs," "refresh target list"

## Installation

1. Install this plugin in Claude Code or Cowork
2. The Playwright MCP server is configured automatically via plugin.json
3. First time: log into Instagram as @espohomeloans in the Playwright browser
4. Populate target-accounts.md by running `/lender-research`

## Requirements

- Claude Code or Cowork
- Node.js 18+ (for Playwright MCP)
- Instagram account (@espohomeloans) logged in

## Plugin Structure

```
lender-engagement/
├── .claude-plugin/
│   └── plugin.json                    (manifest + MCP config)
├── skills/
│   ├── lender-comments/
│   │   ├── SKILL.md                   (main skill)
│   │   ├── target-accounts.md         (LO target list)
│   │   └── references/
│   │       ├── comment-guidelines.md  (voice + examples)
│   │       ├── browser-playbook.md    (IG automation playbook)
│   │       ├── playwright-setup.md    (MCP install guide)
│   │       └── daily-schedule-prompt.md (Cowork scheduler prompt)
│   └── lender-research/
│       ├── SKILL.md                   (main skill)
│       └── references/
│           └── research-methodology.md (sources + verification)
└── README.md
```

## Author

Ryan Rose, Rose Homes LV (ryan@rosehomeslv.com)
