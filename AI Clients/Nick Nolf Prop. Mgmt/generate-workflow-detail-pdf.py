from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

output_dir = "/Users/ryanrose/Downloads/Claude/AI Clients/Nick Nolf Prop. Mgmt"
output_path = os.path.join(output_dir, "TNG-Attachment-Organizer-Detail.pdf")

doc = SimpleDocTemplate(
    output_path,
    pagesize=letter,
    rightMargin=0.65*inch,
    leftMargin=0.65*inch,
    topMargin=0.5*inch,
    bottomMargin=0.5*inch,
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle('Title2', parent=styles['Title'], fontSize=18, spaceAfter=2, textColor=colors.HexColor('#1a1a2e'))
subtitle_style = ParagraphStyle('Subtitle2', parent=styles['Normal'], fontSize=11, spaceAfter=4, textColor=colors.HexColor('#555555'), alignment=TA_CENTER)
tagline_style = ParagraphStyle('Tagline', parent=styles['Normal'], fontSize=10, spaceAfter=12, textColor=colors.HexColor('#2d8a4e'), alignment=TA_CENTER, fontName='Helvetica-Bold')
section_style = ParagraphStyle('Section', parent=styles['Heading2'], fontSize=13, spaceBefore=16, spaceAfter=6, textColor=colors.HexColor('#1a1a2e'))
subsection_style = ParagraphStyle('Subsection', parent=styles['Heading3'], fontSize=11, spaceBefore=10, spaceAfter=4, textColor=colors.HexColor('#333333'))
body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor('#333333'), spaceAfter=6)
bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor('#333333'), leftIndent=18, spaceAfter=3, bulletIndent=6)
step_title = ParagraphStyle('StepTitle', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor('#1a1a2e'), fontName='Helvetica-Bold', spaceBefore=8, spaceAfter=2)
step_body = ParagraphStyle('StepBody', parent=styles['Normal'], fontSize=9.5, leading=13, textColor=colors.HexColor('#444444'), leftIndent=12, spaceAfter=6)
example_style = ParagraphStyle('Example', parent=styles['Normal'], fontSize=9, leading=12, textColor=colors.HexColor('#1a1a2e'), fontName='Courier', leftIndent=12, rightIndent=12, spaceBefore=4, spaceAfter=4, backColor=colors.HexColor('#f5f5f5'), borderPadding=8)
callout_style = ParagraphStyle('Callout', parent=styles['Normal'], fontSize=9.5, leading=13, textColor=colors.HexColor('#1a1a2e'), leftIndent=12, rightIndent=12, spaceBefore=6, spaceAfter=6, backColor=colors.HexColor('#eef6ff'), borderPadding=10)
safety_style = ParagraphStyle('Safety', parent=styles['Normal'], fontSize=9.5, leading=13, textColor=colors.HexColor('#cc3333'), leftIndent=12, rightIndent=12, spaceBefore=6, spaceAfter=6, backColor=colors.HexColor('#fff5f5'), borderPadding=10, fontName='Helvetica-Bold')
header_style = ParagraphStyle('Header', parent=styles['Normal'], fontSize=9, leading=12, fontName='Helvetica-Bold', textColor=colors.white)
cell_style = ParagraphStyle('Cell', parent=styles['Normal'], fontSize=9, leading=12)
cell_bold = ParagraphStyle('CellBold', parent=styles['Normal'], fontSize=9, leading=12, fontName='Helvetica-Bold')
desc_style = ParagraphStyle('Desc', parent=styles['Normal'], fontSize=8.5, leading=11, textColor=colors.HexColor('#555555'))
footer_style = ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, textColor=colors.HexColor('#999999'), alignment=TA_CENTER, spaceBefore=20)

def make_table(data, col_widths=None):
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')]),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t

elements = []

# ============================================================
# TITLE
# ============================================================
elements.append(Paragraph("Email Attachment Downloader &amp; File Organizer", title_style))
elements.append(Paragraph("AI-Powered Document Filing for TNG Property Management", subtitle_style))
elements.append(Paragraph("Complimentary Build &mdash; Provided by Ryan Rose, Rose Homes LV", tagline_style))
elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#1a1a2e')))
elements.append(Spacer(1, 8))

# ============================================================
# OVERVIEW
# ============================================================
elements.append(Paragraph("What This Automation Does", section_style))

elements.append(Paragraph(
    "This workflow runs automatically every 30 minutes during business hours. It scans your TNG Gmail inbox "
    "for any email that has an attachment, downloads those attachments, figures out which investor and property "
    "they belong to, renames them following your exact naming convention, and files them into the correct folder "
    "in your Google Drive. Invoices, estimates, HOA notices, lease documents, move-in photos from Matt &mdash; all "
    "handled automatically.",
    body_style
))

elements.append(Paragraph(
    "It does not touch your Gmail in any way. No labels are created, no folders are added, no emails are moved "
    "or deleted. Your inbox stays exactly the way you have it. The automation only reads and downloads.",
    body_style
))

# ============================================================
# THE PROBLEM IT SOLVES
# ============================================================
elements.append(Paragraph("The Problem It Solves", section_style))

problems = [
    "Every email attachment currently requires manual downloading, renaming, and filing to the correct Drive folder",
    "Your naming convention (Investor Last Name \u2013 Address \u2013 Tenant Name \u2013 Vendor \u2013 Date) must be applied by hand to every single file",
    "Photos from Matt's phone arrive at full size (5-15 MB each) and need to be compressed before filing",
    "HEIC photos from iPhones need to be converted to JPG for universal viewing",
    "With hundreds of investors and thousands of documents, even one misfiled document can take hours to find",
    "This work happens every day, multiple times per day, and never stops",
]
for p in problems:
    elements.append(Paragraph(p, bullet_style, bulletText='\u2022'))

# ============================================================
# HOW IT WORKS - 10 STEPS
# ============================================================
elements.append(Paragraph("How It Works &mdash; Step by Step", section_style))

elements.append(Paragraph(
    "Every 30 minutes during business hours (plus one after-hours scan at night), the automation runs "
    "through this exact sequence:",
    body_style
))

# Step 1
elements.append(Paragraph("Step 1: Verify the Gmail Account", step_title))
elements.append(Paragraph(
    "Before doing anything, the system confirms it is connected to your TNG Gmail account. If for any reason "
    "it detects a different account, it stops immediately and alerts you. It will never process someone else's email.",
    step_body
))

# Step 2
elements.append(Paragraph("Step 2: Search for Emails with Attachments", step_title))
elements.append(Paragraph(
    "The system searches your Gmail for all emails received in the last 24 hours that have attachments. "
    "It looks at up to 25 emails per scan. It does not read emails without attachments &mdash; those are ignored entirely.",
    step_body
))

# Step 3
elements.append(Paragraph("Step 3: Read Each Email", step_title))
elements.append(Paragraph(
    "For each email with attachments, the system reads the subject line, sender, date, email body, and "
    "the list of attached files (names, types, and sizes). If the email is part of a longer thread, it can "
    "read the full conversation for additional context.",
    step_body
))

# Step 4
elements.append(Paragraph("Step 4: Identify the Investor and Property", step_title))
elements.append(Paragraph(
    "This is the most important step. The system determines which investor and property each attachment "
    "belongs to, using multiple methods in order:",
    step_body
))

methods = [
    "<b>Subject line parsing:</b> If your naming convention is in the subject (Investor \u2013 Address \u2013 Tenant \u2013 Topic \u2013 Date), it extracts each component directly.",
    "<b>Known sender matching:</b> Emails from Campbell's Appliance, NWHS, or Matt are recognized automatically and routed based on pre-configured defaults.",
    "<b>Email body scanning:</b> If the subject is unclear, the system scans the email body for Las Vegas addresses, investor names, and tenant names.",
    "<b>Thread context:</b> If a single email is unclear, the system checks prior messages in the same thread for property references.",
]
for m in methods:
    elements.append(Paragraph(m, bullet_style, bulletText='\u2022'))

elements.append(Paragraph(
    "<b>If the investor and property cannot be confidently determined, the system does NOT guess.</b> "
    "It files the attachment to a staging folder called \"Unfiled\" and creates a draft email to you asking "
    "where it should go. A misfiled document in the wrong investor's folder is far worse than an unfiled "
    "document you can route in 5 seconds.",
    safety_style
))

# Step 5
elements.append(Paragraph("Step 5: Classify the Document Type", step_title))
elements.append(Paragraph(
    "The system determines what kind of document the attachment is, which decides which subfolder it goes into. "
    "Classification is based on the sender, subject line keywords, the attachment filename, and the file type.",
    step_body
))

doc_data = [
    [Paragraph('Document Type', header_style), Paragraph('Goes To Subfolder', header_style), Paragraph('Common Sources', header_style)],
    ['Invoice / Bill', 'Work Completed', 'Vendors, contractors'],
    ['Estimate / Quote', 'Work Completed', 'Vendors, contractors'],
    ['HOA Notice / Violation', 'HOA', 'HOA management companies'],
    ['Lease / Addendum', 'Tenants', 'Tenants, attorneys'],
    ['Owner Documents', 'Owners', 'Title, insurance, county'],
    ['Photos', 'Photos', 'Matt, inspectors'],
    ['Repair Completion Proof', 'Work Completed', 'Vendors, contractors'],
]
elements.append(make_table(doc_data, [1.8*inch, 1.8*inch, 3.1*inch]))
elements.append(Spacer(1, 4))

elements.append(Paragraph(
    "If the document type is ambiguous, it files to Work Completed (the most common subfolder) and flags "
    "it in the report as \"type uncertain\" so you can move it if needed.",
    step_body
))

# Step 6
elements.append(Paragraph("Step 6: Rename the Attachment", step_title))
elements.append(Paragraph(
    "Every attachment is renamed to match your exact naming convention before filing. The delimiter is always "
    "space-en dash-space ( \u2013 ), matching your existing system perfectly.",
    step_body
))

elements.append(Paragraph("Naming format:", step_body))
elements.append(Paragraph(
    "Investor Last Name \u2013 Address \u2013 Tenant Name \u2013 Vendor \u2013 Document Type \u2013 Date.ext",
    example_style
))

elements.append(Paragraph("Examples of renamed files:", step_body))
examples = [
    "Smith \u2013 1234 Desert Rose Dr \u2013 Johnson \u2013 Campbell's Appliance \u2013 Invoice \u2013 04-06-2026.pdf",
    "Williams \u2013 5678 Sahara Ave \u2013 Garcia \u2013 NWHS \u2013 Estimate \u2013 04-06-2026.pdf",
    "Davis \u2013 9012 Flamingo Rd \u2013 Lee \u2013 HOA \u2013 Violation Notice \u2013 04-06-2026.pdf",
    "Thompson \u2013 3456 Boulder Hwy \u2013 Rivera \u2013 Matt \u2013 Move-In Photos \u2013 04-06-2026.jpg",
]
for ex in examples:
    elements.append(Paragraph(ex, example_style))

# Step 7
elements.append(Paragraph("Step 7: Compress Photos (When Needed)", step_title))
elements.append(Paragraph(
    "Photos from modern phones are often 5-15 MB each. The system checks every photo attachment against a "
    "configurable size limit (default: 5 MB). If a photo exceeds the limit, it is compressed to 80% quality &mdash; "
    "still perfectly viewable on a phone and usable as legal evidence, but significantly smaller for Drive storage.",
    step_body
))

compress_data = [
    [Paragraph('Feature', header_style), Paragraph('Details', header_style)],
    ['Formats handled', 'JPG, JPEG, PNG, HEIC'],
    ['HEIC conversion', Paragraph('Automatically converts Apple HEIC to JPG for universal compatibility', desc_style)],
    ['Max file size', 'Configurable (default 5 MB)'],
    ['Compression quality', 'Configurable (default 80%)'],
    ['PDFs', 'Never compressed (left at original quality)'],
]
elements.append(make_table(compress_data, [1.8*inch, 4.9*inch]))

# Step 8
elements.append(Paragraph("Step 8: File to Google Drive", step_title))
elements.append(Paragraph(
    "The renamed (and possibly compressed) attachment is filed to the correct location in your Google Drive. "
    "The destination path follows your folder structure exactly:",
    step_body
))

elements.append(Paragraph(
    "[Drive Root] / Investor Name / Property Address / Subfolder / Renamed File",
    example_style
))

elements.append(Paragraph("Filing rules:", step_body))

filing_rules = [
    "If the property subfolder exists, the file is placed directly",
    "If the subfolder is missing but the investor folder exists, the subfolder is created automatically",
    "If the investor folder itself is missing, the file goes to Unfiled &mdash; the system never creates top-level investor folders on its own",
    "If a file with the same name already exists at the destination, a version number is appended (v2, v3, etc.) and flagged as a possible duplicate",
]
for r in filing_rules:
    elements.append(Paragraph(r, bullet_style, bulletText='\u2022'))

# Step 9
elements.append(Paragraph("Step 9: Handle Unfiled Items", step_title))
elements.append(Paragraph(
    "Any attachment that could not be confidently routed to an investor and property is placed in a staging "
    "area in your Drive:",
    step_body
))

elements.append(Paragraph(
    "[Drive Root] / Unfiled / [Today's Date] / [Original Filename]",
    example_style
))

elements.append(Paragraph(
    "A draft email is created in your Gmail with the details of each unfiled item &mdash; the sender, subject, "
    "attachment name, and the reason it could not be routed. You review the draft, decide where it goes, and "
    "move it manually. Nothing is lost, nothing is guessed.",
    step_body
))

# Step 10
elements.append(Paragraph("Step 10: Generate a Summary Report", step_title))
elements.append(Paragraph(
    "After every scan, the system produces a report showing exactly what it did. The report includes:",
    step_body
))

report_items = [
    "A table of every attachment filed: sender, subject, original filename, renamed filename, destination folder, and file size",
    "A separate table for any unfiled items with the reason they could not be routed",
    "A photo compression summary showing original vs. compressed sizes and savings percentage",
    "Totals: attachments filed, photos compressed, items needing review",
]
for r in report_items:
    elements.append(Paragraph(r, bullet_style, bulletText='\u2022'))

# ============================================================
# WHAT IT DOES NOT DO
# ============================================================
elements.append(Paragraph("What This Automation Does NOT Do", section_style))

donts = [
    "Does not create, modify, or apply Gmail labels &mdash; your inbox stays untouched",
    "Does not delete or move emails &mdash; the email remains in Gmail exactly where it is",
    "Does not send any emails &mdash; it only creates drafts for your review (unfiled notifications only)",
    "Does not create top-level investor folders &mdash; only subfolders within existing investor directories",
    "Does not guess where a file goes &mdash; if uncertain, it stages the file and asks you",
    "Does not open, read, or execute attachment contents &mdash; it only downloads, renames, and files them",
]
for d in donts:
    elements.append(Paragraph(d, bullet_style, bulletText='\u2022'))

# ============================================================
# SCHEDULE
# ============================================================
elements.append(Paragraph("How Often It Runs", section_style))

sched_data = [
    [Paragraph('Setting', header_style), Paragraph('Value', header_style)],
    ['Frequency', 'Every 30 minutes'],
    ['Days', 'Monday through Saturday'],
    ['Business hours', 'Configurable (e.g., 8:00 AM to 5:00 PM)'],
    ['Runs per day', '~18 during business hours'],
    ['After-hours scan', '1 additional scan (e.g., 9:00 PM)'],
    ['Sunday', 'Off'],
]
elements.append(make_table(sched_data, [2.0*inch, 4.7*inch]))

elements.append(Spacer(1, 6))
elements.append(Paragraph(
    "The computer must remain on and connected to the internet for scheduled scans to run. "
    "A battery backup is recommended for uninterrupted operation.",
    body_style
))

# ============================================================
# DOCUMENT TYPES
# ============================================================
elements.append(Paragraph("Document Types Recognized", section_style))

elements.append(Paragraph(
    "The system recognizes these document types out of the box. Additional types can be added at any time "
    "by updating the configuration file &mdash; no rebuild required.",
    body_style
))

types_data = [
    [Paragraph('Type', header_style), Paragraph('Keywords That Trigger It', header_style), Paragraph('Subfolder', header_style)],
    ['Invoice', 'invoice, inv, payment due, bill', 'Work Completed'],
    ['Estimate', 'estimate, quote, bid, proposal', 'Work Completed'],
    ['HOA Notice', 'hoa, violation, homeowner, association, architectural', 'HOA'],
    ['Lease', 'lease, rental agreement, addendum, amendment', 'Tenants'],
    ['Owner Document', 'owner, investor, property tax, insurance, deed', 'Owners'],
    ['Photos', 'photo, photos, picture, image, move-in, move-out, inspection', 'Photos'],
    ['Work Completed', 'completed, finished, done, before and after, repair', 'Work Completed'],
]
elements.append(make_table(types_data, [1.3*inch, 3.2*inch, 1.3*inch]))

# ============================================================
# KNOWN SENDERS
# ============================================================
elements.append(Paragraph("Pre-Configured Known Senders", section_style))

elements.append(Paragraph(
    "These senders are recognized automatically. When the system sees an email from a known sender, "
    "it already knows the default document type and subfolder, which speeds up classification and improves accuracy. "
    "New senders can be added at any time.",
    body_style
))

sender_data = [
    [Paragraph('Sender', header_style), Paragraph('Default Type', header_style), Paragraph('Default Subfolder', header_style)],
    ["Campbell's Appliance", 'Invoice', 'Work Completed'],
    ['NWHS (Northwest Handyman Service)', 'Invoice', 'Work Completed'],
    ['Matt (Move-In Photos)', 'Photos', 'Photos'],
]
elements.append(make_table(sender_data, [2.5*inch, 1.7*inch, 2.5*inch]))

# ============================================================
# SAFETY
# ============================================================
elements.append(Paragraph("Safety and Error Handling", section_style))

elements.append(Paragraph(
    "This automation is designed to be conservative. It prioritizes never misfiling over always filing. "
    "Here is how it handles edge cases:",
    body_style
))

safety_data = [
    [Paragraph('Scenario', header_style), Paragraph('What Happens', header_style)],
    [Paragraph('Email has no parseable context (blank subject, unknown sender, generic body)', cell_style), Paragraph('Attachment goes to Unfiled staging folder. Draft notification sent to you.', desc_style)],
    [Paragraph('Cannot determine investor or property', cell_style), Paragraph('Attachment goes to Unfiled. System never guesses names.', desc_style)],
    [Paragraph('File with same name already exists in Drive', cell_style), Paragraph('Version number appended (v2). Flagged as possible duplicate in report.', desc_style)],
    [Paragraph('Very large attachment (>25 MB)', cell_style), Paragraph('Noted in report. Filing attempted normally. Flagged if it fails.', desc_style)],
    [Paragraph('Unusual file type (.exe, .bat, .sh)', cell_style), Paragraph('Never opened or executed. Filed if safe type, flagged if executable.', desc_style)],
    [Paragraph('Photo compression fails', cell_style), Paragraph('Filed at original size. Noted in report. Filing is never blocked by compression failure.', desc_style)],
    [Paragraph('Gmail account mismatch', cell_style), Paragraph('Full stop. System halts immediately and alerts user.', desc_style)],
    [Paragraph('Investor folder does not exist in Drive', cell_style), Paragraph('Attachment goes to Unfiled. Top-level folders are never auto-created.', desc_style)],
    [Paragraph('Multiple attachments on one email', cell_style), Paragraph('Each attachment named and classified individually. Same-type files get sequence numbers (1 of 5, 2 of 5, etc.)', desc_style)],
]
elements.append(make_table(safety_data, [2.8*inch, 3.9*inch]))

# ============================================================
# FOOTER
# ============================================================
elements.append(Spacer(1, 16))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc')))
elements.append(Paragraph("Prepared by Ryan Rose &mdash; Rose Homes LV &nbsp;|&nbsp; For: Nick Nolf, TNG Property Management", footer_style))

doc.build(elements)
print(f"PDF created: {output_path}")
