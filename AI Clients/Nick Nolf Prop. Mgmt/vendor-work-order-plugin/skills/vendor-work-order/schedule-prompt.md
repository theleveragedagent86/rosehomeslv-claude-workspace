# Vendor Work Order Scan — Scheduled Task Prompt

**Paste this prompt into Claude Cowork as a scheduled task.**

Schedule: Every 30 minutes during business hours, Monday through Saturday.

---

## Prompt

```
Run /vendor-work-order scan now

This is an automated scheduled run. Do NOT ask questions or wait for input. Execute the full scan silently and report results.

If any emails are classified as NEEDS-REVIEW, create a summary draft to Nick so he sees it in his Gmail drafts.

If no new vendor emails are found, just log "No new vendor emails" and stop. Do not create any drafts or notifications for empty scans.
```

---

## Cowork Schedule Configuration

| Setting | Value |
|---------|-------|
| **Task name** | Vendor Work Order Scan |
| **Frequency** | Every 30 minutes |
| **Days** | Monday, Tuesday, Wednesday, Thursday, Friday, Saturday |
| **Start time** | [BUSINESS_HOURS_START — e.g., 8:00 AM] |
| **End time** | [BUSINESS_HOURS_END — e.g., 5:00 PM] |
| **Total runs per day** | ~18 (every 30 min across 9 hours) |
| **Sunday** | OFF |

### Optional: After-Hours Single Run

If Nick also wants one scan after business hours:

| Setting | Value |
|---------|-------|
| **Task name** | Vendor Work Order Scan (After Hours) |
| **Frequency** | Once |
| **Days** | Monday, Tuesday, Wednesday, Thursday, Friday, Saturday |
| **Time** | [AFTER_HOURS_SCAN_TIME — e.g., 9:00 PM] |

---

## Placeholders to Fill

| Placeholder | What to Fill |
|---|---|
| `[BUSINESS_HOURS_START]` | When does Nick's business day start? (e.g., 8:00 AM) |
| `[BUSINESS_HOURS_END]` | When does Nick's business day end? (e.g., 5:00 PM) |
| `[AFTER_HOURS_SCAN_TIME]` | What time for the nightly scan? (e.g., 9:00 PM) |

---

## Requirements

- Nick's computer must be **on and connected to internet** for scheduled tasks to run
- Claude Cowork must be **open and logged in**
- The vendor-work-order plugin must be **installed** with all placeholders in `vendor-config.json` filled
- Battery backup recommended for 24/7 uptime
