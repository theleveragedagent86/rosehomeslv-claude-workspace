---
title: "Workflow: Vendor Work Order Email Processing"
type: workflow
created: 2026-04-05
updated: 2026-04-05
sources: [2026-04-05-initial-meeting-transcript-and-analysis.md]
tags: [workflow, email, vendor, first-build, priority]
complexity: tier-1-straightforward
status: designated-first-build
---

# Workflow: Vendor Work Order Email Processing

## Status
**BUILT** — Plugin created on April 5, 2026. Placeholders need to be filled at Monday meeting before first run.

**Plugin location:** `vendor-work-order-plugin/` (also zipped as `vendor-work-order-plugin.zip`)

## What It Does
Monitor incoming emails from two specific vendors and distinguish between **estimates** and **approved work orders** based on subject line keywords. Different actions follow depending on which type it is. All email responses are created as drafts only (Phase 1, human-in-the-loop).

## Plugin Structure
```
vendor-work-order-plugin/
├── .claude-plugin/plugin.json           # Plugin metadata
└── skills/vendor-work-order/
    ├── SKILL.md                         # Main workflow (Gmail MCP tools)
    ├── vendor-config.json               # Vendor data + placeholders
    └── action-rules.md                  # Decision tree for actions
```

## Vendors in Scope
1. [[entity-campbells-appliance]] — Campbell's Appliance
2. [[entity-nwhs]] — NWHS (Northwest Handyman Service)

## Classification Logic
- Email subject lines clearly indicate "estimate" vs. "approved"
- Approved keywords checked FIRST (more specific, avoids "approved estimate" false match)
- Three classifications: ESTIMATE, APPROVED, NEEDS-REVIEW
- NEEDS-REVIEW is the safe fallback for ambiguous emails

## Workflow Steps
1. Verify correct Gmail account connected
2. Search for vendor emails (from: + newer_than:1d + not already processed)
3. Read and classify each email against keyword arrays
4. Extract naming convention components from subject/body
5. Execute actions per classification (all drafts only, never send)
6. Report results in summary table

## Placeholders to Fill (Monday Meeting)
- Nick's Gmail address
- Vendor email addresses (Campbell's + NWHS)
- Subject line keywords for estimate and approved (per vendor)
- Date format Nick uses
- Gmail label names (processed, estimate, approved, unclassified)
- Exact actions for estimates vs. approved work orders (the decision tree)
- Google Drive base path (when ready)
- AppFolio URL (when ready)

See `vendor-config.json` and `action-rules.md` for full placeholder list.

## Complexity Assessment
**Tier 1: Straightforward** — Two vendors, two email types per vendor, subject lines are clear. Classification is binary pattern matching. The actions that follow need definition but the detection itself is simple.

## Related Pages
- [[workflow-email-classifier]] — This is a subset of the broader email system
- [[entity-campbells-appliance]] — Vendor
- [[entity-nwhs]] — Vendor
- [[concept-naming-convention]] — Email naming patterns
