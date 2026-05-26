---
title: "Workflow: AppFolio Maintenance Follow-Up Manager"
type: workflow
created: 2026-04-05
updated: 2026-04-05
sources: [2026-04-05-initial-meeting-transcript-and-analysis.md]
tags: [workflow, appfolio, maintenance]
complexity: tier-2-moderate
status: planned
---

# Workflow: AppFolio Maintenance Follow-Up Manager

## What It Does
Log into AppFolio on a scheduled basis, navigate to work orders, pull the "no action for 7 days" report, and send follow-up messages to tenants and/or vendors through AppFolio's built-in messaging.

## Current State
- Matt currently spends 1-2 hours per day on maintenance follow-up
- 22 active work orders at time of initial meeting
- AppFolio has a built-in "no action for 7 days" report

## Proposed Schedule
- Run every morning
- Check the "no action for 7 days" report
- Send contextually appropriate follow-up messages through AppFolio (not email)

## Implementation Approach
- Named: "AppFolio Maintenance Manager"
- Would use Claude Cowork (browser automation) to interact with AppFolio
- Depends on whether AppFolio has an API (more reliable) or requires browser-only interaction

## Complexity Assessment
**Tier 2: Moderate** — Requires browser-based login, navigating to specific reports, reading work order status, composing contextual follow-ups, and sending through AppFolio's messaging. Browser automation through AppFolio's interface adds complexity.

## Open Questions
- What specific follow-up messages should be sent? Templated or contextual?
- Follow up with tenant, vendor, or both? Does it depend on who hasn't responded?
- Does AppFolio have an API?
- Is automated login allowed under AppFolio TOS?

## Related Pages
- [[entity-appfolio]] — The system being automated
- [[entity-matt]] — Currently does this work manually
- [[concept-specialist-architecture]] — This is one specialist agent
