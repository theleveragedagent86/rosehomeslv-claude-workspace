---
title: "Concept: Scheduling Strategy"
type: concept
created: 2026-04-05
updated: 2026-04-05
sources: [2026-04-05-initial-meeting-transcript-and-analysis.md]
tags: [concept, scheduling, infrastructure]
---

# Concept: Scheduling Strategy

## Overview
Claude cannot run continuously — tasks must be scheduled at intervals.

## Proposed Schedule
- **Business hours:** Every 30 minutes (~16 tasks for an 8-hour day)
- **After hours:** One check per night
- **Total:** ~17 scheduled task executions per day
- **Days:** Monday through Saturday

## After-Hours Email Behavior
- Responses drafted after hours should be **schedule-sent** via Gmail's future send for 8 AM the next business day
- Rationale: Don't train tenants/owners to expect 24/7 instant responses

## Infrastructure Requirements
- Computer must remain on for scheduled tasks to run
- Battery backup recommended for 24/7 operation
- Ryan mentioned dispatch mode on Claude mobile app (trigger tasks from phone, but computer must be on)
- Consider mirroring Google Drive locally so Claude doesn't have to log in online each time

## Token/Cost Implications
- Token usage decreases significantly once tasks are built and finalized (less "thinking" required)
- Ryan recommended starting with $100/month plan to monitor usage
- Can scale down to $20/month if usage allows
- 16+ scheduled tasks per day needs cost monitoring

## Open Questions
- What exactly are Nick's "business hours"? Never defined in meeting.
- How will costs scale with 17 daily task runs?

## Related Pages
- [[concept-specialist-architecture]] — Each specialist runs on its own schedule
- [[workflow-email-classifier]] — Most schedule-dependent workflow
