# Wiki Log — TNG Property Management AI Engagement

---

## [2026-04-05] ingest | Initial In-Person Meeting Transcript and Analysis
- **Source:** `raw/2026-04-05-initial-meeting-transcript-and-analysis.md`
- **Pages created:** 20 (1 overview, 1 source summary, 5 entities, 9 workflows, 4 concepts)
- **Summary:** First ingest. Full meeting transcript between Ryan Rose and Nick Nolf covering TNG Property Management's AI automation needs. Extracted all requested workflows (9), ranked by complexity (Tier 1-4), identified 7 additional suggested workflows, documented all open questions for next meeting, created entity pages for all key people/companies/systems, and established concept pages for naming conventions, Drive structure, specialist architecture, and scheduling strategy.
- **Key finding:** Email management is the central nervous system of the operation. Vendor work order processing (Campbell's + NWHS) is the designated first build. Next meeting April 6, 2026.

## [2026-04-05] build | Vendor Work Order Email Processing Plugin
- **Output:** `vendor-work-order-plugin/` directory + `vendor-work-order-plugin.zip`
- **Files created:** 4 (plugin.json, SKILL.md, vendor-config.json, action-rules.md)
- **Status:** Built with placeholders. Requires Nick's vendor emails, subject line keywords, and action definitions before first run.
- **Wiki updated:** `workflow-vendor-work-order-processing.md` updated to reflect build status
- **Next step:** Fill placeholders at Monday April 6 meeting. Key unknowns: exact actions for estimates vs. approved work orders, vendor email addresses, subject line keywords.

## [2026-04-05] build | Email Attachment Downloader and File Organizer Plugin
- **Output:** `email-attachment-organizer-plugin/` directory + `email-attachment-organizer-plugin.zip`
- **Files created:** 5 (plugin.json, SKILL.md, attachment-config.json, filing-rules.md, schedule-prompt.md)
- **Status:** Built with placeholders. Designated as the NEW first build / free demo for Nick. Requires Gmail address, Drive path/access method, vendor emails, and business hours before first run.
- **Design decisions:** No Gmail labels (Nick's inbox untouched), Unfiled staging folder for unroutable attachments, never creates top-level investor folders, photo compression with HEIC-to-JPG conversion, draft-only notifications.
- **Wiki updated:** `workflow-email-attachment-organizer.md` updated to reflect build status
- **Next step:** Fill placeholders at Monday April 6 meeting. Key unknowns: Drive access method (local sync vs browser), Google Drive base path, vendor/Matt email addresses, business hours for scheduling.
