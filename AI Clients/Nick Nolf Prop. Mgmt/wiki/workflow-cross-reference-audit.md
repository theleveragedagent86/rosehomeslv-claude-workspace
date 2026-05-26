---
title: "Workflow: Cross-Reference Audit (Google Drive vs. AppFolio)"
type: workflow
created: 2026-04-05
updated: 2026-04-05
sources: [2026-04-05-initial-meeting-transcript-and-analysis.md]
tags: [workflow, audit, drive, appfolio]
complexity: tier-3-complex
status: planned
---

# Workflow: Cross-Reference Audit (Google Drive vs. AppFolio)

## What It Does
Pull lease end dates and tenant information from PDF lease agreements in Google Drive, cross-reference against AppFolio data, flag mismatches, and send Nick a daily report at 4 PM.

## Why It Matters
Catches human errors in file management. Nick's documentation discipline is high, but with 500+ investors and thousands of documents, mismatches between Drive and AppFolio are inevitable.

## Complexity Assessment
**Tier 3: Complex** — Requires reading PDF lease agreements (potentially multiple addendums per property, must identify the most recent/correct one), extracting dates and tenant info, logging into AppFolio to pull the same data, comparing, identifying mismatches, and compiling a daily report. PDF format variability is the biggest challenge.

## Open Questions
- Which AppFolio field is the "source of truth" — AppFolio or Drive? Nick said AppFolio is most accurate.
- Does he want Drive updated to match AppFolio, or just flagged for manual review?
- How should multiple addendums per property be handled? Which takes precedence?

## Related Pages
- [[entity-appfolio]] — One side of the comparison
- [[concept-drive-structure]] — The other side
- [[workflow-email-classifier]] — May trigger when mismatches are found
