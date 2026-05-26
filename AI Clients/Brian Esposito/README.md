# Brian Esposito -- IG Engagement Skill Package

**Client:** Brian J. Esposito, Branch Manager, Nations Lending (Las Vegas)
**Prepared by:** Ryan Rose, Rose Homes LV
**Date:** April 2026

---

## Package Contents

```
Brian Esposito/
├── skills/
│   ├── claude.json                         <-- Cowork plugin config (MCP + skill registry)
│   ├── CLAUDE.md                           <-- Project-level instructions for Claude
│   ├── lender-comments/
│   │   ├── SKILL.md                        <-- Main engagement skill
│   │   ├── CLAUDE.md                       <-- Browser automation playbook
│   │   ├── comment-guidelines.md           <-- Voice, tone, example comments
│   │   ├── target-accounts.md              <-- Competitor LO target list (empty, pending MMI data)
│   │   ├── daily-schedule-prompt.md        <-- Copy/paste prompt for Cowork daily scheduler
│   │   └── Playwright_MCP_Setup.md         <-- Step-by-step MCP install guide
│   └── lender-research/
│       ├── SKILL.md                        <-- Target list discovery skill
│       └── CLAUDE.md                       <-- Research methodology and sources
├── Brian_Esposito_IG_Engagement_Plan.docx  <-- Client-facing strategy doc
├── build_plan_doc.py                       <-- Script that generated the Word doc
└── README.md                               <-- This file
```

---

## Setup Checklist (for Ryan)

- [ ] Review all skill files for accuracy
- [ ] Get Brian's MMI production export ($2M-$10M) to seed target-accounts.md
- [ ] Run /lender-research to populate the initial target list
- [ ] Confirm Brian has added a recruiting link to his @espohomeloans Instagram bio
- [ ] Schedule in-person setup session (Thursday 4/17 afternoon)
- [ ] During setup: install Claude Code, Cowork, Playwright MCP, log into Instagram
- [ ] Run a live dry-run test on one target account
- [ ] Set up Cowork daily scheduler with daily-schedule-prompt.md

## Installation (for Brian's machine)

1. Copy the `skills/` folder contents to Brian's `~/.claude/skills/`
2. Copy `claude.json` MCP config into Brian's `~/.claude.json` (merge if he already has one)
3. Follow Playwright_MCP_Setup.md to install the browser automation tool
4. Log into @espohomeloans in the Playwright browser
5. Test: type "/lender-comments" in Claude Code and verify it loads

## Pending Items

- Brian sending MMI export (PDF/Excel) to seed target list
- Confirm Nations Lending compliance approval (if needed)
- Any specific LOs Brian wants prioritized or excluded
