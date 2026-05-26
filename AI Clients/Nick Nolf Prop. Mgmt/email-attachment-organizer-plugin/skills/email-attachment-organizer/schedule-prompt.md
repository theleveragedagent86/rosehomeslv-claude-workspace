# Email Attachment Organizer — Scheduled Task Prompt

**Paste this prompt into Claude Cowork as a scheduled task.**

Schedule: Every 30 minutes during business hours, Monday through Saturday.

---

## Prompt

```
Run /email-attachment-organizer scan now

This is an automated scheduled run. Do NOT ask questions or wait for input. Execute the full scan silently and report results.

If any attachments cannot be filed (unfiled items), create a summary draft to Nick listing each unfiled item and why it couldn't be routed.

If no emails with attachments are found, just log "No new attachments" and stop. Do not create any drafts or notifications for empty scans.
```

---

## Cowork Schedule Configuration

| Setting | Value |
|---------|-------|
| **Task name** | Email Attachment Organizer |
| **Frequency** | Every 30 minutes |
| **Days** | Monday, Tuesday, Wednesday, Thursday, Friday, Saturday |
| **Start time** | [BUSINESS_HOURS_START — e.g., 8:00 AM] |
| **End time** | [BUSINESS_HOURS_END — e.g., 5:00 PM] |
| **Total runs per day** | ~18 (every 30 min across 9 hours) |
| **Sunday** | OFF |

### Optional: After-Hours Single Run

| Setting | Value |
|---------|-------|
| **Task name** | Email Attachment Organizer (After Hours) |
| **Frequency** | Once |
| **Days** | Monday, Tuesday, Wednesday, Thursday, Friday, Saturday |
| **Time** | [AFTER_HOURS_SCAN_TIME — e.g., 9:00 PM] |

---

## Placeholders to Fill

| Placeholder | What to Fill |
|---|---|
| `[BUSINESS_HOURS_START]` | When does Nick's business day start? |
| `[BUSINESS_HOURS_END]` | When does Nick's business day end? |
| `[AFTER_HOURS_SCAN_TIME]` | What time for the nightly scan? |

---

## Requirements

- Nick's computer must be **on and connected to internet**
- Claude Cowork must be **open and logged in**
- The plugin must be **installed** with all placeholders in `attachment-config.json` filled
- Google Drive access must be configured (local sync or browser)
- Battery backup recommended for 24/7 uptime
