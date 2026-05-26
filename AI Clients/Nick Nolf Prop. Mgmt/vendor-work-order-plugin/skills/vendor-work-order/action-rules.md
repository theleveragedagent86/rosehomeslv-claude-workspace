# Vendor Work Order Action Rules

This file defines the decision tree for what happens after an email is classified. Read this file at the start of every run alongside `vendor-config.json`.

**IMPORTANT:** All email actions MUST use `gmail_create_draft`. Never send directly. Nick reviews and sends manually (Phase 1, human-in-the-loop).

---

## How Classification Works

1. Read the email subject line
2. Check for estimate keywords from the vendor's `estimate_keywords` array (case-insensitive)
3. Check for approved keywords from the vendor's `approved_keywords` array (case-insensitive)
4. Apply these rules:
   - Estimate keyword matches AND no approved keyword matches = **ESTIMATE**
   - Approved keyword matches AND no estimate keyword matches = **APPROVED**
   - Both match OR neither matches = **NEEDS-REVIEW**
5. When checking for matches, check approved keywords FIRST (they tend to be more specific, e.g., "approved estimate" should classify as APPROVED, not ESTIMATE)

---

## ESTIMATE Actions

When an email is classified as an **ESTIMATE**, execute each action below in order:

### Action 1: [ESTIMATE_ACTION_1]

**Description:** [PLACEHOLDER - e.g., "Forward estimate to investor/owner for approval"]

- **To:** [ESTIMATE_FORWARD_RECIPIENT - e.g., the investor's email address]
- **Subject format:** `Investor Last Name – Address – Tenant Name – Vendor – Estimate – Date`
- **Body template:**
  ```
  [ESTIMATE_FORWARD_BODY_TEMPLATE]

  Example placeholder:
  Hi [Investor First Name],

  We received an estimate from [Vendor Name] for your property at [Address].

  [Paste or summarize the estimate details from the original email]

  Please reply to approve or let us know if you have questions.

  Thank you,
  TNG Property Management
  ```
- **Attachments:** If the original email has attachments (PDF estimates), note them in the draft body

### Action 2: [ESTIMATE_ACTION_2]

**Description:** [PLACEHOLDER - e.g., "File estimate to Google Drive"]

- **Destination:** `[GOOGLE_DRIVE_BASE_PATH]/[Investor Name]/[Property Address]/Work Completed/`
- **File name:** `Investor Last Name – Address – Tenant Name – Vendor – Estimate – Date.pdf`
- **Note:** Google Drive filing is currently DISABLED in vendor-config.json. Skip this action until enabled. Log that it was skipped.

### Action 3: [ESTIMATE_ACTION_3]

**Description:** [PLACEHOLDER - e.g., "Update AppFolio work order with estimate status"]

- **AppFolio status:** [APPFOLIO_ESTIMATE_STATUS]
- **AppFolio note:** [APPFOLIO_ESTIMATE_NOTE_TEMPLATE]
- **Note:** AppFolio integration is currently DISABLED in vendor-config.json. Skip this action until enabled. Log that it was skipped.

---

## APPROVED WORK ORDER Actions

When an email is classified as an **APPROVED WORK ORDER**, execute each action below in order:

### Action 1: [APPROVED_ACTION_1]

**Description:** [PLACEHOLDER - e.g., "Send confirmation to vendor that work is approved"]

- **To:** The vendor's email address (from `vendor-config.json`)
- **Subject format:** `Investor Last Name – Address – Tenant Name – Vendor – Approved WO – Date`
- **Body template:**
  ```
  [APPROVED_CONFIRMATION_BODY_TEMPLATE]

  Example placeholder:
  Hi [Vendor Name] team,

  This is to confirm that the work order for [Address] has been approved.

  [Include any relevant details from the original email]

  Please proceed and let us know when work is scheduled/completed.

  Thank you,
  TNG Property Management
  ```

### Action 2: [APPROVED_ACTION_2]

**Description:** [PLACEHOLDER - e.g., "Notify investor that work has been approved and is proceeding"]

- **To:** [INVESTOR_EMAIL]
- **Subject format:** `Investor Last Name – Address – Tenant Name – Vendor – Work Approved – Date`
- **Body template:**
  ```
  [APPROVED_INVESTOR_NOTIFICATION_TEMPLATE]

  Example placeholder:
  Hi [Investor First Name],

  The work order for your property at [Address] has been approved and the vendor ([Vendor Name]) has been notified to proceed.

  We will follow up once the work is completed.

  Thank you,
  TNG Property Management
  ```

### Action 3: [APPROVED_ACTION_3]

**Description:** [PLACEHOLDER - e.g., "File approved work order to Google Drive"]

- **Destination:** `[GOOGLE_DRIVE_BASE_PATH]/[Investor Name]/[Property Address]/Work Completed/`
- **File name:** `Investor Last Name – Address – Tenant Name – Vendor – Approved WO – Date.pdf`
- **Note:** Google Drive filing is currently DISABLED. Skip until enabled.

### Action 4: [APPROVED_ACTION_4]

**Description:** [PLACEHOLDER - e.g., "Update AppFolio work order status to approved/in-progress"]

- **AppFolio status:** [APPFOLIO_APPROVED_STATUS]
- **AppFolio note:** [APPFOLIO_APPROVED_NOTE_TEMPLATE]
- **Note:** AppFolio integration is currently DISABLED. Skip until enabled.

---

## NEEDS-REVIEW Actions

When an email cannot be confidently classified:

1. **Create a draft email to Nick** summarizing the unclassified email:
   - **To:** The `summary_recipient` from vendor-config.json
   - **Subject:** `Vendor Email Needs Review – [Vendor Name] – [Original Subject] – [Date]`
   - **Body:**
     ```
     A vendor email could not be automatically classified as an estimate or approved work order.

     **From:** [sender]
     **Subject:** [original subject]
     **Received:** [date/time]
     **Snippet:** [first 200 characters of email body]

     **Reason:** [why classification failed - e.g., "No keyword match", "Both estimate and approved keywords matched", "Missing subject line"]

     Please review and take appropriate action.
     ```

2. **Do NOT apply any Gmail labels.** Nick's Gmail stays untouched. The draft itself serves as the flag for review.

---

## Edge Cases

### Revised Estimate
[REVISED_ESTIMATE_HANDLING]
- **Default behavior until defined:** Treat as a new ESTIMATE. Include "(Revised)" in the subject when drafting the forward. Flag in the summary report that this appears to be a revised estimate.

### Partially Approved
[PARTIAL_APPROVAL_HANDLING]
- **Default behavior until defined:** Classify as NEEDS-REVIEW. Include a note that the email may contain a partial approval requiring human judgment.

### Duplicate Email (Already Processed)
- Before creating a draft, check if a draft already exists with a matching subject line
- If a matching draft exists, skip the email entirely. Do not create a duplicate draft.
- The time window search (`newer_than:1d`) also naturally limits reprocessing

### Missing or Blank Subject Line
- Check the email body for reference details (Nick adds context there when subjects are blank)
- If still unclassifiable, mark as NEEDS-REVIEW

### Email Has Attachments
- Note attachment filenames and types in the summary report
- If Drive filing is enabled, download and rename per naming convention
- If Drive filing is disabled, just log: "Attachment present: [filename] (filing skipped, Drive integration disabled)"

### Email From Unknown Sender (Not in Vendor Config)
- Do NOT process. Skip entirely.
- Only process emails from senders listed in vendor-config.json
