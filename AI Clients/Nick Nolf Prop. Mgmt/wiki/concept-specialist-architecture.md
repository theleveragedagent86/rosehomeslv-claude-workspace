---
title: "Concept: Specialist Agent Architecture"
type: concept
created: 2026-04-05
updated: 2026-04-05
sources: [2026-04-05-initial-meeting-transcript-and-analysis.md]
tags: [concept, architecture, agents]
---

# Concept: Specialist Agent Architecture

## Principle
Each task should be a **specialist**, not a jack-of-all-trades. Ryan emphasized this during the meeting.

## Structure
```
AppFolio Specialist
  └── Maintenance follow-up sub-agent
  └── (future sub-agents)

Gmail Specialist
  └── Vendor work order processor
  └── Email classifier / auto-responder
  └── (future sub-agents)

Google Drive Specialist
  └── Attachment organizer
  └── Photo/video handler
  └── Structure enforcer
  └── (future sub-agents)
```

## Rationale
- Keeps each agent focused and reliable
- Reduces scope of errors (one agent failure doesn't cascade)
- Each specialist can be built, tested, and refined independently
- Maps cleanly to the three core systems (Gmail, AppFolio, Drive)

## Implementation
- Each specialist is a separate Claude skill/plugin
- Skill = the prompt/instructions, Plugin = the wrapper that plugs into Claude
- Scheduled tasks trigger each specialist independently

## Related Pages
- [[workflow-email-classifier]] — Gmail specialist
- [[workflow-appfolio-maintenance-followup]] — AppFolio specialist
- [[workflow-email-attachment-organizer]] — Drive specialist
