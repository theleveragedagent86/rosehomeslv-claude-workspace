---
title: "Concept: Naming Convention"
type: concept
created: 2026-04-05
updated: 2026-04-05
sources: [2026-04-05-initial-meeting-transcript-and-analysis.md]
tags: [concept, naming, convention, critical]
---

# Concept: Naming Convention

## Overview
Nick has a rigid, consistent naming convention used across both email subject lines and Google Drive file names. This convention is central to how his entire operation stays searchable and organized. It is **sacred** — any automation must follow it exactly.

## Email Subject Line Format
```
Investor Last Name – Address – Tenant Name – Topic – Date
```
- Uses space-dash-space (` – `) as delimiter throughout
- Example topic: "HOA Violation"
- When clients send emails with blank subject lines, Nick adds reference details in the email **body** (not subject line, to avoid breaking email threads)

## File Naming Format
```
Owner Last Name – Address – Tenant Name – Vendor – Date
```
- Same space-dash-space delimiter
- Applied to invoices, estimates, HOA notices, lease documents, etc.

## Why It Matters
- Searchability is built into this naming system
- Nick can quickly find any vendor's invoices, quotes, etc. during tax season
- Every workflow that creates, renames, or files documents must follow this convention exactly
- Tens of thousands of documents already follow this pattern

## Workflows That Depend on This
- [[workflow-email-attachment-organizer]] — Must apply this naming when filing attachments
- [[workflow-email-classifier]] — Reads this convention to understand email context
- [[workflow-vendor-work-order-processing]] — Subject lines follow this pattern
- [[workflow-drive-structure-enforcement]] — File names follow this pattern

## Related Pages
- [[concept-drive-structure]] — The folder hierarchy that complements this naming
- [[entity-nick-nolf]] — Creator and enforcer of the convention
