---
title: "Workflow: Inbound Email Reader, Classifier, and Auto-Responder"
type: workflow
created: 2026-04-05
updated: 2026-04-05
sources: [2026-04-05-initial-meeting-transcript-and-analysis.md]
tags: [workflow, email, priority, complex]
complexity: tier-3-complex
status: primary-need
---

# Workflow: Inbound Email Reader, Classifier, and Auto-Responder

## Status
**PRIMARY NEED** — Nick called this his "biggest thing" multiple times. The vendor work order processing is the first build because it's a contained slice of this larger system.

## What It Does
Monitor the single PM Gmail inbox on a scheduled loop. Read new emails, classify them by type, select the appropriate Gmail template (from ~25 existing templates), draft a response, and place it in drafts for approval.

## Scheduling Logic
- **During business hours:** Check every 30 minutes (~16 tasks for an 8-hour day)
- **After hours/weekends:** One check per night
- **Business hours responses:** Send quickly (within minutes goal)
- **After hours responses:** Schedule-send via Gmail's future send for 8 AM next business day
- Rationale: Don't train tenants/owners to expect 24/7 instant responses

## Template System
- ~25 existing Gmail templates for common scenarios:
  - HOA violation meeting action
  - HOA response
  - 30-day move-out notice
  - Various other PM communications
- Claude selects the right template based on email classification
- Cross-references AppFolio for tenant info, lease dates, etc.
- Cross-references Google Drive lease PDFs to verify information

## Human-in-the-Loop Strategy
1. **Phase 1 (now):** Claude drafts into Gmail drafts for Nick's approval
2. Include at bottom of each email: "If this doesn't fully answer your question, please reply back"
3. **Phase 2 (future):** Close the loop — autonomous responses based on master knowledge base

## Investor Carve-Outs
- 10-15 of ~500 investors have unique preferences
- Example: one owner wants all maintenance paid with his credit card across 8 properties
- Some owners insist on using their own vendors
- These patterns are visible in email history and need to be learned

## Complexity Assessment
**Tier 3: Complex** — Requires classifying emails across potentially hundreds of categories, matching to correct template, pulling data from AppFolio/Drive, handling 10-15 investor carve-outs, applying scheduling logic. The variety of inbound email formats from people who don't follow naming conventions makes classification the hardest part.

## Open Questions
- What does Nick consider "business hours"? Never defined in meeting.
- During business hours, does he want draft approval or is sending OK eventually?
- Can he provide a mapping of which template applies to which email type?
- How should Claude handle emails that don't fit any existing template?
- How many emails per day does the inbox typically receive?

## Related Pages
- [[workflow-vendor-work-order-processing]] — First build, a contained subset of this
- [[workflow-email-attachment-organizer]] — Triggered alongside this
- [[workflow-master-email-knowledge-base]] — Long-term enhancement
- [[concept-naming-convention]] — Email naming patterns
- [[concept-specialist-architecture]] — Each task is a specialist
