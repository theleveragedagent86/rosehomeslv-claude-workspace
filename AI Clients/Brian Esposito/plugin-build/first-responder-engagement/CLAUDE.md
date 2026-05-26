# CLAUDE.md

This file provides guidance to Claude Code when working inside the `first-responder-engagement` plugin.

## What This Plugin Does

Two skills (`/responder-comments` and `/responder-research`) that build Brian Esposito's community presence with Las Vegas first responders on Instagram. Operates @espohomeloans. Companion to (not replacement for) the `lender-engagement` plugin.

**The implicit business benefit (top-of-mind for VA loans, hero programs, family referrals later) is real but indirect. It is destroyed the moment a comment reaches for it.**

## The Single Most Important Rule

**Comments NEVER mention mortgages, lending, Nations Lending, VA loans, hero programs, or any business.** Not subtle, not implicit, not "as a community member who works in housing." Never. If a comment cannot be written without referencing the business, skip the post.

This is the central rule that distinguishes this plugin from the lender plugin. Every other rule flows from it.

## How This Plugin Differs From lender-engagement

The two plugins share the @espohomeloans account, the Playwright MCP server (`playwright-instagram`), and the same browser session. They differ on voice and behavior:

| Behavior | lender-engagement | first-responder-engagement |
|----------|-------------------|---------------------------|
| Voice | Industry peer + mentor | Vegas neighbor (no service-provider energy) |
| Comment leads with | Insight or question | Specific acknowledgment |
| Replies per post | 1-2 | 0-1 (default: zero) |
| Comment likes per post | 5-10 | 3-5 (only aligned ones) |
| Skip rate | Moderate | Aggressive (default skip) |
| Mortgage references | Implicit, never explicit | NEVER, in any form |
| Voice anchor | Mortgage expertise | Gratitude + 28-year Vegas neighbor |

## Combined-Volume Cap

Both plugins run on the same Instagram account. To stay under Instagram's natural-engagement thresholds, daily combined volume should target ~30 posts max:

- Schedule the two skills at different times (e.g., lender at 9 AM, responder at 2 PM)
- If `lender-comments` already ran heavy (15+ posts) today, run `responder-comments` lighter (5-10)
- A rate limit on either plugin = stop both for 24+ hours

## Aggressive-Skip Defaults

First responder content trips guardrails far more than mortgage industry content. The plugin is built to skip first, engage second. Hard skips include:

- All political content (police reform, military policy, immigration, election content) — any direction
- Active line-of-duty death posts (unless Brian personally knew the person)
- Active critical incident posts (active shooter, mass casualty) until fully resolved
- Polarizing religious content
- Vaccine / mask / COVID controversy
- LGBTQ+ topics, race-as-debate framing
- Venting about the public, the department, the job
- Posts under 2 hours old with no engagement
- Anything where commenting could look opportunistic from a mortgage business account

The compounding effect of "when in doubt, skip" is by design. There are plenty of safe posts to engage with.

## Plugin Structure

```
first-responder-engagement/
├── .claude-plugin/plugin.json     # Inline Playwright MCP (shared with lender plugin)
├── CLAUDE.md                      # This file
├── README.md
└── skills/
    ├── responder-comments/
    │   ├── SKILL.md
    │   ├── target-accounts.md     # 4 categories: Military/Veterans, Police, Fire/EMS, Healthcare
    │   └── references/
    │       ├── comment-guidelines.md      # Voice + 6 post-type sections with examples
    │       ├── browser-playbook.md        # IG automation patterns + skip edge cases
    │       ├── playwright-setup.md        # Shared MCP setup notes
    │       └── daily-schedule-prompt.md   # Cowork scheduler prompt
    └── responder-research/
        ├── SKILL.md
        └── references/research-methodology.md  # Discovery without MMI: bio search + hashtag mining
```

## No MMI Equivalent for This Audience

Unlike the lender plugin (which uses Brian's MMI production export to seed the target list), there is no centralized data source for first responders. Discovery is entirely from Instagram bio searches, hashtag mining (#lvmpd, #vegasfire, #nellisafb, #vegasnurse, etc.), and following department/institutional accounts to find individuals who post personally.

This makes verification more important. A bio that says "Vegas firefighter" might be a fitness influencer using the title for clout. Always check post content, recency, and tone before adding to the target list.

## Target Categories (aim for rough balance)

- **Military / Veterans** — Nellis AFB, Creech AFB, NV National Guard, local VFW/American Legion members
- **Police / Law Enforcement** — LVMPD, Henderson PD, North LV PD, NV Highway Patrol, individual officers (NOT department PR-only accounts)
- **Fire / EMS** — Clark County Fire, Henderson Fire, LV Fire & Rescue, individual firefighters/paramedics/EMTs
- **Healthcare** — Sunrise, UMC, Valley, Henderson Hospital nurses/doctors/frontline workers

Total target: 20-30 active accounts, 5-8 per category.

## Voice Anchors (use these phrases as-is when fit)

- For routine on-duty content: "The daily reps that nobody sees are what makes the big calls go right. Respect."
- For department fundraisers: Brian has Par for the Cure credibility — "Pulling off events like this is its own full-time job."
- For 28-year Vegas pride: "Twenty-eight years in this valley and the community side still surprises me."
- For Memorial Day genuine remembrance: "Remembering the names today. Thank you for keeping the watch."

## Cross-Reference

For broader workspace conventions (em-dash rule, max 2 sentences, dual-source-of-truth gotcha between `plugin-build/` and `skills/`), see the workspace-level CLAUDE.md at `/Users/ryanrose/Downloads/Claude/AI Clients/Brian Esposito/CLAUDE.md`.

For the strategy plan presented to Brian, see `Brian_First_Responder_Engagement_Plan.docx` in the workspace root.
