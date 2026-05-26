---
title: "Workflow: Email Attachment Downloader and File Organizer"
type: workflow
created: 2026-04-05
updated: 2026-04-05
sources: [2026-04-05-initial-meeting-transcript-and-analysis.md]
tags: [workflow, email, drive, attachments, first-build]
complexity: tier-2-moderate
status: built-with-placeholders
---

# Workflow: Email Attachment Downloader and File Organizer

## Status
**BUILT** — Plugin created on April 5, 2026. Designated as the first build / free enticing demo for Nick. Placeholders need to be filled at Monday meeting before first run.

**Plugin location:** `email-attachment-organizer-plugin/` (also zipped as `email-attachment-organizer-plugin.zip`)

## What It Does
Scan Gmail for emails with attachments, download them, rename them following Nick's exact naming convention, classify by document type (invoice, estimate, HOA notice, lease, photos, etc.), and file into the correct Google Drive folder. Includes photo compression for oversized phone photos.

## Plugin Structure
```
email-attachment-organizer-plugin/
├── .claude-plugin/plugin.json
└── skills/email-attachment-organizer/
    ├── SKILL.md                  # Main 10-step workflow
    ├── attachment-config.json    # Sender data, doc types, Drive paths, placeholders
    ├── filing-rules.md           # How to identify property, classify, rename, and file
    └── schedule-prompt.md        # Cowork scheduled task prompt (every 30 min)
```

## Workflow Steps
1. Verify correct Gmail account
2. Search for emails with attachments (`has:attachment newer_than:1d`)
3. Read each email and extract context (subject, sender, body, attachments)
4. Identify investor and property (subject parse > known sender > body scan > unfiled)
5. Classify document type (invoice, estimate, HOA, lease, photos, etc.)
6. Rename per naming convention: `Investor – Address – Tenant – Source – Type – Date.ext`
7. Compress photos if oversized
8. File to correct Drive folder: `[Base]/Investor/Property/Subfolder/`
9. Handle unfiled items (stage to Unfiled folder, draft notification to Nick)
10. Report results in summary table

## Key Design Decisions
- **No Gmail labels** — Nick's inbox stays untouched
- **Unfiled staging** — if property can't be determined, files go to `Unfiled/[Date]/` rather than guessing
- **Never creates investor folders** — only subfolders within existing investor directories
- **Draft-only notifications** — unfiled items generate a draft to Nick, nothing sent automatically
- **Photo compression** — HEIC to JPG conversion, configurable quality/size limits

## Placeholders to Fill (Monday Meeting)
- Nick's Gmail address
- Google Drive base path and access method (local sync vs. browser)
- Vendor email addresses (Campbell's, NWHS, Matt)
- Date format Nick uses
- Business hours start/end for scheduling
- Any additional known senders beyond the three configured

See `attachment-config.json` for full placeholder list.

## Naming Convention
See [[concept-naming-convention]] for full details.
- Format: `Investor Last Name – Address – Tenant Name – Vendor – Date`
- Delimiter: ` – ` (space, en-dash, space) used consistently throughout

## Drive Folder Structure
- Investor name > Property Address > Subfolders:
  - HOA
  - Owners
  - Tenants
  - Photos
  - Work Completed

## Complexity Assessment
**Tier 2: Moderate** — Requires reading the email, understanding which investor/property/tenant it relates to, correctly applying the naming convention, and filing to the right subfolder. The naming convention is rigid and well-defined (helps), but variety of incoming email formats from external parties introduces variability.

## Related Pages
- [[concept-naming-convention]] — The naming system
- [[concept-drive-structure]] — Folder hierarchy
- [[workflow-email-classifier]] — Emails trigger this workflow
- [[workflow-photo-intake]] — Photo-specific subset of this workflow
