# Email Attachment Filing Rules

This file defines how to determine where attachments go and what to name them. Read this file at the start of every run alongside `attachment-config.json`.

**IMPORTANT:** Do NOT create, modify, or apply Gmail labels. Nick's Gmail stays exactly as-is. Do NOT delete or modify emails after downloading attachments.

---

## Step 1: Identify the Property and Investor

Every attachment must be filed under the correct investor and property. Use these methods in order until you get a match:

### Method A: Parse the Subject Line (Primary)

Nick's email subject lines follow this format:
```
Investor Last Name – Address – Tenant Name – Topic – Date
```

Split the subject by ` – ` (space, en-dash, space). If the subject follows this convention:
- **Part 1** = Investor Last Name
- **Part 2** = Property Address
- **Part 3** = Tenant Name
- **Part 4** = Topic (may indicate document type: "HOA Violation", "Invoice", etc.)
- **Part 5** = Date

### Method B: Check Known Senders

If the subject doesn't follow the convention, check `known_senders` in attachment-config.json. Known senders have a default document type and subfolder. But you still need the investor/property. Check the email body for:
- A property address (look for Las Vegas street patterns: numbers + street name + Ave/Dr/St/Blvd/Ln/Way)
- An investor or owner name
- A tenant name
- A unit number

### Method C: Scan Email Body

If neither the subject line nor the sender mapping provides the investor/property:
- Search the email body for address patterns
- Search for names that match investor or tenant patterns
- Check the email thread (use `gmail_read_thread`) for context from prior messages

### Method D: Flag as Unfiled

If the property and investor CANNOT be determined:
- **Do NOT guess.** Do NOT file the attachment to a random folder.
- Download the attachment to a staging area: `[GOOGLE_DRIVE_BASE_PATH]/Unfiled/[Date]/`
- Include it in the summary report as "Unfiled - needs manual routing"
- Create a draft to Nick asking where this attachment should go

---

## Step 2: Determine Document Type and Subfolder

Once you know the investor and property, determine which subfolder the attachment goes in.

### Classification Priority

1. **Check known_senders first** — if the sender has a `default_type` in config, use it unless the email content clearly indicates otherwise
2. **Check the email subject/body for document_type keywords** from attachment-config.json
3. **Check the file extension** — `.heic`/`.jpg`/`.png` from a phone are likely photos, `.pdf` could be anything
4. **Check the filename itself** — vendors often name files descriptively ("Invoice_12345.pdf", "Estimate_Smith.pdf")

### Subfolder Mapping

| Document Type | Subfolder | Common Sources |
|---------------|-----------|----------------|
| Invoice / Bill | Work Completed | Vendors, contractors |
| Estimate / Quote | Work Completed | Vendors, contractors |
| HOA Notice / Violation | HOA | HOA management companies |
| Lease / Addendum | Tenants | Tenants, attorneys, Nick's own drafts |
| Owner Documents (tax, insurance, deed) | Owners | Title companies, insurance, county |
| Photos (move-in, move-out, inspection) | Photos | Matt, inspectors |
| Repair/Completion Proof | Work Completed | Vendors, contractors |

### When Document Type is Ambiguous

If the document type cannot be confidently determined:
- File to **Work Completed** as the default (most common)
- Flag in the summary report: "Filed to Work Completed (type uncertain)"
- Nick can move it manually if needed — better to file somewhere than nowhere

---

## Step 3: Rename the Attachment

**CRITICAL: Follow the naming convention EXACTLY.** The delimiter is ` – ` (space, en-dash, space). Never use hyphens (-), colons (:), slashes, or other separators.

### Naming Format
```
Investor Last Name – Address – Tenant Name – Vendor/Source – Document Type – Date.ext
```

### Examples
```
Smith – 1234 Desert Rose Dr – Johnson – Campbell's Appliance – Invoice – 04-05-2026.pdf
Williams – 5678 Sahara Ave – Garcia – NWHS – Estimate – 04-05-2026.pdf
Davis – 9012 Flamingo Rd – Lee – HOA – Violation Notice – 04-05-2026.pdf
Thompson – 3456 Boulder Hwy – Rivera – Matt – Move-In Photos – 04-05-2026.jpg
```

### Naming Rules

1. **Investor Last Name:** From subject line parse or email body. If unknown, use `UNKNOWN INVESTOR`
2. **Address:** Short form (number + street name). Drop "Las Vegas, NV 89XXX" from the address
3. **Tenant Name:** From subject line or email body. If unknown, omit this segment entirely
4. **Vendor/Source:** The sender's display name or company name. Use `display_name` from known_senders if available
5. **Document Type:** From the classification step (Invoice, Estimate, HOA Notice, Lease, etc.)
6. **Date:** Use the date format from `attachment-config.json`. If unknown, use the email received date
7. **Extension:** Keep the original file extension (`.pdf`, `.jpg`, `.png`, etc.)

### Multiple Attachments Per Email

If an email has multiple attachments:
- Name each one individually
- If they're all the same type (e.g., 5 invoice pages), append a sequence number: `... – Invoice – 04-05-2026 (1 of 5).pdf`
- If they're different types (e.g., invoice + photo), classify and name each separately

---

## Step 4: Build the Destination Path

```
[GOOGLE_DRIVE_BASE_PATH]/[Investor Name]/[Property Address]/[Subfolder]/[Renamed File]
```

### Example Full Paths
```
[DRIVE]/Smith/1234 Desert Rose Dr/Work Completed/Smith – 1234 Desert Rose Dr – Johnson – Campbell's Appliance – Invoice – 04-05-2026.pdf

[DRIVE]/Davis/9012 Flamingo Rd/HOA/Davis – 9012 Flamingo Rd – Lee – HOA – Violation Notice – 04-05-2026.pdf

[DRIVE]/Thompson/3456 Boulder Hwy/Photos/Thompson – 3456 Boulder Hwy – Rivera – Matt – Move-In Photos – 04-05-2026.jpg
```

### If the Folder Doesn't Exist

- If the investor folder exists but the property subfolder doesn't, create it following the structure in `attachment-config.json`
- If the investor folder doesn't exist at all, **do NOT create it.** Flag as unfiled and ask Nick. A missing investor folder likely means a data entry gap, not a new investor.
- **Never create top-level investor folders without explicit instruction.**

---

## Step 5: Handle Photos (Compression)

When the attachment is a photo (`.jpg`, `.jpeg`, `.png`, `.heic`):

1. Check the file size against `compression.max_file_size_mb` in config
2. If the file is larger than the max, compress it to `compression.photo_quality` (default: 80%)
3. Convert `.heic` files to `.jpg` (HEIC is Apple's format and not universally viewable)
4. Log the original size and compressed size in the summary report

**Note:** Photo compression requires image processing capability. If running in an environment without image tools, flag the photos as "needs compression" in the summary and file them at original size.

---

## Edge Cases

### Email Has No Parseable Context
- Subject is blank, body is generic, sender is unknown
- File attachments to `[GOOGLE_DRIVE_BASE_PATH]/Unfiled/[Date]/`
- Draft a notification to Nick with the email details

### Duplicate Attachment (Same File Already in Drive)
- Before filing, check if a file with the same name already exists at the destination path
- If it does, append a version number: `... – Invoice – 04-05-2026 (v2).pdf`
- Flag in the summary: "Possible duplicate filed as v2"

### Very Large Attachments (>25MB)
- Note in the summary report
- Attempt to file normally
- If filing fails due to size, flag for manual handling

### Non-Standard File Types
- If the attachment is not a common type (`.pdf`, `.jpg`, `.png`, `.doc`, `.xlsx`), still file it but flag in the summary: "Unusual file type: [extension]"
- Do NOT open or execute `.exe`, `.bat`, `.sh`, or other executable files

### Email Thread Has Attachments Across Multiple Messages
- When reading a thread, process only attachments from the NEWEST unprocessed message
- Do not re-download attachments from earlier messages in the same thread
