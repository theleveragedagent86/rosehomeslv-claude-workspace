from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import os

output_dir = "/Users/ryanrose/Downloads/Claude/AI Clients/Nick Nolf Prop. Mgmt"
output_path = os.path.join(output_dir, "TNG-Workflow-Pricing.pdf")

doc = SimpleDocTemplate(
    output_path,
    pagesize=letter,
    rightMargin=0.6*inch,
    leftMargin=0.6*inch,
    topMargin=0.5*inch,
    bottomMargin=0.5*inch,
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle('Title2', parent=styles['Title'], fontSize=18, spaceAfter=2, textColor=colors.HexColor('#1a1a2e'))
subtitle_style = ParagraphStyle('Subtitle2', parent=styles['Normal'], fontSize=11, spaceAfter=12, textColor=colors.HexColor('#555555'), alignment=TA_CENTER)
section_style = ParagraphStyle('Section', parent=styles['Heading2'], fontSize=14, spaceBefore=18, spaceAfter=8, textColor=colors.HexColor('#1a1a2e'))
tier_label = ParagraphStyle('TierLabel', parent=styles['Normal'], fontSize=10, textColor=colors.HexColor('#1a1a2e'), fontName='Helvetica-Bold')
cell_style = ParagraphStyle('Cell', parent=styles['Normal'], fontSize=9, leading=12)
cell_bold = ParagraphStyle('CellBold', parent=styles['Normal'], fontSize=9, leading=12, fontName='Helvetica-Bold')
header_style = ParagraphStyle('Header', parent=styles['Normal'], fontSize=9, leading=12, fontName='Helvetica-Bold', textColor=colors.white)
desc_style = ParagraphStyle('Desc', parent=styles['Normal'], fontSize=8.5, leading=11, textColor=colors.HexColor('#555555'))
price_style = ParagraphStyle('Price', parent=styles['Normal'], fontSize=10, leading=12, fontName='Helvetica-Bold', alignment=TA_CENTER, textColor=colors.HexColor('#1a1a2e'))
price_small = ParagraphStyle('PriceSmall', parent=styles['Normal'], fontSize=8, leading=10, alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
free_style = ParagraphStyle('Free', parent=styles['Normal'], fontSize=10, leading=12, fontName='Helvetica-Bold', alignment=TA_CENTER, textColor=colors.HexColor('#2d8a4e'))
note_style = ParagraphStyle('Note', parent=styles['Normal'], fontSize=9, textColor=colors.HexColor('#666666'), spaceAfter=6, spaceBefore=6)
footer_style = ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, textColor=colors.HexColor('#999999'), alignment=TA_CENTER, spaceBefore=20)
savings_style = ParagraphStyle('Savings', parent=styles['Normal'], fontSize=10, textColor=colors.HexColor('#1a1a2e'), spaceBefore=4, spaceAfter=2)
savings_bold = ParagraphStyle('SavingsBold', parent=styles['Normal'], fontSize=11, textColor=colors.HexColor('#1a1a2e'), fontName='Helvetica-Bold', spaceBefore=2, spaceAfter=2)
intro_style = ParagraphStyle('Intro', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor('#333333'), spaceAfter=12, spaceBefore=6)

elements = []

# Title
elements.append(Paragraph("TNG Property Management", title_style))
elements.append(Paragraph("AI Workflow Automation &mdash; Services &amp; Investment", subtitle_style))
elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#1a1a2e')))
elements.append(Spacer(1, 6))

elements.append(Paragraph(
    "Below are the nine automation workflows identified for TNG Property Management, "
    "organized by complexity. Each workflow has a one-time build fee that covers design, development, "
    "testing, and deployment on your system.",
    intro_style
))

# ============================================================
# TIER 1
# ============================================================
elements.append(Paragraph("Tier 1: Straightforward", section_style))

tier1_color = colors.HexColor('#2d8a4e')

data = [
    [
        Paragraph('#', header_style),
        Paragraph('Workflow', header_style),
        Paragraph('What It Does', header_style),
        Paragraph('Investment', header_style),
    ],
    [
        '1',
        Paragraph('<b>Email Attachment Downloader &amp; File Organizer</b>', cell_bold),
        Paragraph('Scans Gmail for emails with attachments. Downloads, renames per your naming convention, classifies by document type (invoice, estimate, HOA, lease, photos), and files to the correct Google Drive folder automatically. Includes photo compression.', desc_style),
        Paragraph('<b>FREE</b>', free_style),
    ],
    [
        '2',
        Paragraph('<b>Vendor Work Order Email Processing</b>', cell_bold),
        Paragraph('Monitors Gmail for emails from Campbell\'s Appliance and NWHS. Classifies each as an estimate or approved work order based on subject line keywords. Takes the appropriate action for each type. Drafts only, you review and send.', desc_style),
        Paragraph('$1,500', price_style),
    ],
    [
        '3',
        Paragraph('<b>Google Drive Structure Enforcement</b>', cell_bold),
        Paragraph('Given your perfect example folder hierarchy, replicates that exact structure for every new property, tenant, or investor. Deterministic, no guessing. Ensures consistency across your entire Drive.', desc_style),
        Paragraph('$1,500', price_style),
    ],
    [
        '4',
        Paragraph('<b>Photo Intake, Organization &amp; Compression</b>', cell_bold),
        Paragraph('Receives move-in photos from Matt\'s emails, identifies the correct property, compresses oversized phone photos, converts HEIC to JPG, and files to the correct property folder under Photos in Drive.', desc_style),
        Paragraph('$1,500', price_style),
    ],
]

t = Table(data, colWidths=[0.3*inch, 1.6*inch, 3.5*inch, 1.3*inch], repeatRows=1)
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('ALIGN', (0, 0), (0, -1), 'CENTER'),
    ('ALIGN', (3, 0), (3, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')]),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    # Green left border for free row
    ('LINEBEFORESTYLE', (0, 1), (0, 1)),
]))
elements.append(t)

# ============================================================
# TIER 2
# ============================================================
elements.append(Paragraph("Tier 2: Moderate", section_style))

data = [
    [
        Paragraph('#', header_style),
        Paragraph('Workflow', header_style),
        Paragraph('What It Does', header_style),
        Paragraph('Investment', header_style),
    ],
    [
        '5',
        Paragraph('<b>AppFolio Maintenance Follow-Up Manager</b>', cell_bold),
        Paragraph('Logs into AppFolio daily, pulls the "no action for 7 days" report on work orders, and sends follow-up messages to tenants and vendors through AppFolio\'s built-in messaging. Replaces 1-2 hours/day of manual follow-up.', desc_style),
        Paragraph('$2,500', price_style),
    ],
    [
        '6',
        Paragraph('<b>Video Compression &amp; Organization</b>', cell_bold),
        Paragraph('Compresses move-in walkthrough videos to phone-viewable, legal-evidence quality. Files into the correct property folders in Google Drive. Addresses the current ~500 GB of uncompressed video storage.', desc_style),
        Paragraph('$2,000', price_style),
    ],
]

t = Table(data, colWidths=[0.3*inch, 1.6*inch, 3.5*inch, 1.3*inch], repeatRows=1)
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('ALIGN', (0, 0), (0, -1), 'CENTER'),
    ('ALIGN', (3, 0), (3, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')]),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
]))
elements.append(t)

# ============================================================
# TIER 3
# ============================================================
elements.append(Paragraph("Tier 3: Complex", section_style))

data = [
    [
        Paragraph('#', header_style),
        Paragraph('Workflow', header_style),
        Paragraph('What It Does', header_style),
        Paragraph('Investment', header_style),
    ],
    [
        '7',
        Paragraph('<b>Inbound Email Classifier &amp; Auto-Responder</b>', cell_bold),
        Paragraph('Monitors your Gmail inbox every 30 minutes. Reads each new email, classifies it by type, selects the correct template from your 25 Gmail templates, cross-references AppFolio and Drive for tenant/lease data, drafts the response, and schedules after-hours emails for 8 AM. Handles investor carve-outs.', desc_style),
        Paragraph('$4,000', price_style),
    ],
    [
        '8',
        Paragraph('<b>Cross-Reference Audit (Drive vs. AppFolio)</b>', cell_bold),
        Paragraph('Reads PDF lease agreements from Google Drive, extracts lease end dates and tenant info, cross-references against AppFolio data, flags mismatches, and emails you a daily report at 4 PM summarizing any discrepancies found.', desc_style),
        Paragraph('$3,000', price_style),
    ],
]

t = Table(data, colWidths=[0.3*inch, 1.6*inch, 3.5*inch, 1.3*inch], repeatRows=1)
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('ALIGN', (0, 0), (0, -1), 'CENTER'),
    ('ALIGN', (3, 0), (3, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')]),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
]))
elements.append(t)

# ============================================================
# TIER 4
# ============================================================
elements.append(Paragraph("Tier 4: Advanced", section_style))

data = [
    [
        Paragraph('#', header_style),
        Paragraph('Workflow', header_style),
        Paragraph('What It Does', header_style),
        Paragraph('Investment', header_style),
    ],
    [
        '9',
        Paragraph('<b>Master Email Knowledge Base &amp; Pattern Learning</b>', cell_bold),
        Paragraph('Processes your 100,000+ email archive to identify behavioral patterns across 500+ investors. Learns the 10-15 investor carve-outs, categorizes every type of property management scenario, and builds a comprehensive reference. This is the long-term foundation that enables fully autonomous email responses.', desc_style),
        Paragraph('$5,000+', price_style),
    ],
]

t = Table(data, colWidths=[0.3*inch, 1.6*inch, 3.5*inch, 1.3*inch], repeatRows=1)
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('ALIGN', (0, 0), (0, -1), 'CENTER'),
    ('ALIGN', (3, 0), (3, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')]),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
]))
elements.append(t)

# ============================================================
# SUMMARY BOX
# ============================================================
elements.append(Spacer(1, 16))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc')))
elements.append(Spacer(1, 8))

elements.append(Paragraph("Investment Summary", section_style))

summary_data = [
    [
        Paragraph('Package', header_style),
        Paragraph('Includes', header_style),
        Paragraph('Total', header_style),
    ],
    [
        Paragraph('<b>Starter</b>', cell_bold),
        Paragraph('Attachment Organizer (free) + 1 additional workflow', desc_style),
        Paragraph('$1,500 - $2,500', price_style),
    ],
    [
        Paragraph('<b>Growth</b>', cell_bold),
        Paragraph('Attachment Organizer (free) + 3 additional workflows', desc_style),
        Paragraph('$5,000 - $8,000', price_style),
    ],
    [
        Paragraph('<b>Complete</b>', cell_bold),
        Paragraph('All 9 workflows', desc_style),
        Paragraph('$16,000 - $21,000', price_style),
    ],
]

t = Table(summary_data, colWidths=[1.2*inch, 3.5*inch, 2.0*inch], repeatRows=1)
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('ALIGN', (2, 0), (2, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')]),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
]))
elements.append(t)

# Footer
elements.append(Spacer(1, 20))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc')))
elements.append(Paragraph("Prepared by Ryan Rose &mdash; Rose Homes LV &nbsp;|&nbsp; For: Nick Nolf, TNG Property Management", footer_style))

doc.build(elements)
print(f"PDF created: {output_path}")
