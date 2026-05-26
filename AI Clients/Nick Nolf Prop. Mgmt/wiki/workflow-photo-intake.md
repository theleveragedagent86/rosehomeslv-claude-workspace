---
title: "Workflow: Photo Intake, Organization, and Compression"
type: workflow
created: 2026-04-05
updated: 2026-04-05
sources: [2026-04-05-initial-meeting-transcript-and-analysis.md]
tags: [workflow, photos, drive, compression]
complexity: tier-1-straightforward
status: planned
---

# Workflow: Photo Intake, Organization, and Compression

## What It Does
Receive move-in photos from Matt's emails, place them in the correct property's Google Drive folder under "Photos," and reduce file sizes automatically.

## Trigger
Matt emails photos to the PM email address from his phone.

## Steps
1. Detect email from Matt with photo attachments
2. Identify which property the photos belong to (from email content)
3. Download photos
4. Compress/reduce file sizes (modern phone photos are too large)
5. Place in correct property folder under "Photos" in Google Drive

## Photo Types
- **MLS photos** — for listing the rental property
- **Inventory photos** — for condition documentation at move-in

## Complexity Assessment
**Tier 1: Straightforward** — Clear trigger (email from Matt with attachments), clear destination (property folder under Photos), single compression operation. Only complexity is correctly identifying which property from the email content.

## Open Questions
- When Matt emails photos, does the subject/body consistently identify which property? If not, how does Nick currently know?
- What compression level/format is acceptable?
- Should MLS photos and inventory photos be separated into subfolders?

## Related Pages
- [[entity-matt]] — Takes and sends the photos
- [[concept-drive-structure]] — Where photos are filed
- [[workflow-video-compression]] — Similar but heavier
