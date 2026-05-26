from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

output_dir = "/Users/ryanrose/Downloads/Claude/AI Clients/Nick Nolf Prop. Mgmt"
output_path = os.path.join(output_dir, "TNG-Placeholder-Checklist.pdf")

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
section_style = ParagraphStyle('Section', parent=styles['Heading2'], fontSize=13, spaceBefore=16, spaceAfter=6, textColor=colors.HexColor('#1a1a2e'))
subsection_style = ParagraphStyle('Subsection', parent=styles['Heading3'], fontSize=11, spaceBefore=10, spaceAfter=4, textColor=colors.HexColor('#333333'))
note_style = ParagraphStyle('Note', parent=styles['Normal'], fontSize=9, textColor=colors.HexColor('#666666'), spaceAfter=8, leftIndent=6)
cell_style = ParagraphStyle('Cell', parent=styles['Normal'], fontSize=9, leading=12)
header_cell = ParagraphStyle('HeaderCell', parent=styles['Normal'], fontSize=9, leading=12, textColor=colors.white)
ask_style = ParagraphStyle('Ask', parent=styles['Normal'], fontSize=9, leading=12, textColor=colors.HexColor('#444444'), fontName='Helvetica-Oblique')
blank = ParagraphStyle('Blank', parent=styles['Normal'], fontSize=9, leading=12)
footer_style = ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, textColor=colors.HexColor('#999999'), alignment=TA_CENTER, spaceBefore=20)

elements = []

# Title
elements.append(Paragraph("TNG Property Management", title_style))
elements.append(Paragraph("Placeholder Checklist &mdash; Fill In With Nick at Meeting", subtitle_style))
elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#1a1a2e')))
elements.append(Spacer(1, 8))

def make_table(data, col_widths=None):
    if col_widths is None:
        col_widths = None
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

# --- SECTION 1: General ---
elements.append(Paragraph("General (Both Plugins)", section_style))

data = [
    ['#', 'Item', 'What to Ask Nick', 'Value'],
    ['1', 'Gmail Address', Paragraph("What's the TNG Gmail address Claude will monitor?", ask_style), ''],
    ['2', 'Date Format', Paragraph("How do you write dates in file names? Like 04-06-2026 or 04/06/2026?", ask_style), ''],
    ['3', 'Business Hours Start', Paragraph("What time does your business day start?", ask_style), ''],
    ['4', 'Business Hours End', Paragraph("What time does your business day end?", ask_style), ''],
    ['5', 'After-Hours Scan Time', Paragraph("What time for the one nightly scan? e.g., 9 PM", ask_style), ''],
]
elements.append(make_table(data, [0.3*inch, 1.4*inch, 3.2*inch, 2.0*inch]))

# --- SECTION 2: Vendor/Sender Emails ---
elements.append(Paragraph("Vendor / Sender Emails", section_style))

data = [
    ['#', 'Item', 'What to Ask Nick', 'Value'],
    ['6', "Campbell's Email", Paragraph("What email address do Campbell's invoices and estimates come from?", ask_style), ''],
    ['7', "Campbell's Domain", Paragraph("(e.g., @campbellsappliance.com)", ask_style), ''],
    ['8', 'NWHS Email', Paragraph("What email address does NWHS send from?", ask_style), ''],
    ['9', 'NWHS Domain', Paragraph("(e.g., @nwhs.com)", ask_style), ''],
    ['10', "Matt's Email", Paragraph("What email does Matt send move-in photos from?", ask_style), ''],
    ['11', 'Other Senders?', Paragraph("Any other vendors who regularly email attachments?", ask_style), ''],
]
elements.append(make_table(data, [0.3*inch, 1.4*inch, 3.2*inch, 2.0*inch]))

# --- SECTION 3: Email Keywords ---
elements.append(Paragraph("Email Keywords (Vendor Work Order Plugin)", section_style))

data = [
    ['#', 'Item', 'What to Ask Nick', 'Value'],
    ['12', "Campbell's Estimate", Paragraph("When Campbell's sends an estimate, what word is in the subject? 'Estimate'? 'Quote'?", ask_style), ''],
    ['13', "Campbell's Approved", Paragraph("When it's approved, what does the subject say? 'Approved'?", ask_style), ''],
    ['14', 'NWHS Estimate', Paragraph("Same for NWHS \u2014 what word means estimate?", ask_style), ''],
    ['15', 'NWHS Approved', Paragraph("What word means approved for NWHS?", ask_style), ''],
]
elements.append(make_table(data, [0.3*inch, 1.4*inch, 3.2*inch, 2.0*inch]))

# --- SECTION 4: Google Drive ---
elements.append(Paragraph("Google Drive", section_style))

data = [
    ['#', 'Item', 'What to Ask Nick', 'Value'],
    ['16', 'Drive Base Path', Paragraph("Where's the root folder where all investor folders live?", ask_style), ''],
    ['17', 'Access Method', Paragraph("Is Drive synced locally or browser-only?", ask_style), 'Local / Browser'],
    ['18', 'Local Path', Paragraph("If synced: what's the folder path? (e.g., G:\\My Drive\\TNG)", ask_style), ''],
]
elements.append(make_table(data, [0.3*inch, 1.4*inch, 3.2*inch, 2.0*inch]))

# --- SECTION 5: Vendor Work Order Actions ---
elements.append(Paragraph("Vendor Work Order Actions", section_style))
elements.append(Paragraph('Ask Nick: "Walk me through what you do today when you get an estimate from a vendor. Step by step. Then walk me through what happens when one is approved."', note_style))

elements.append(Paragraph("When an ESTIMATE arrives:", subsection_style))
data = [
    ['Step', 'Action', 'Notes'],
    ['1', '', ''],
    ['2', '', ''],
    ['3', '', ''],
]
elements.append(make_table(data, [0.5*inch, 3.7*inch, 2.7*inch]))

elements.append(Paragraph("When an APPROVED work order arrives:", subsection_style))
data = [
    ['Step', 'Action', 'Notes'],
    ['1', '', ''],
    ['2', '', ''],
    ['3', '', ''],
    ['4', '', ''],
]
elements.append(make_table(data, [0.5*inch, 3.7*inch, 2.7*inch]))

# --- SECTION 6: Folder Structure ---
elements.append(Paragraph("Folder Structure Verification", section_style))
elements.append(Paragraph('Ask Nick: "Can you show me one perfect example folder in Drive so I can see exactly how it\'s set up?"', note_style))

data = [
    ['Item', "Nick's Actual Convention", 'Notes'],
    ['Example investor folder name', '', ''],
    ['Example property folder name', '', ''],
    [Paragraph('Subfolders (confirm: HOA / Owners / Tenants / Photos / Work Completed)', cell_style), '', 'Any others?'],
    ['Example invoice file name', '', ''],
    ['Example estimate file name', '', ''],
    ['Example HOA notice file name', '', ''],
    [Paragraph('Delimiter confirmed: space-en dash-space ( \u2013 ) ?', cell_style), '', ''],
]
elements.append(make_table(data, [2.3*inch, 2.5*inch, 2.1*inch]))

# --- SECTION 7: Optional/Future ---
elements.append(Paragraph("Optional / Future", section_style))

data = [
    ['#', 'Item', 'What to Ask', 'Value'],
    ['19', 'AppFolio URL', Paragraph("What's your AppFolio web address?", ask_style), ''],
    ['20', 'AppFolio Login', Paragraph("Did you create the Claude login in AppFolio?", ask_style), 'Yes / No'],
    ['21', "Ryan's Email", Paragraph("For CC on summary reports", ask_style), ''],
    ['22', 'Photo Max Size', Paragraph("How small for compressed photos? 5MB good?", ask_style), ''],
]
elements.append(make_table(data, [0.3*inch, 1.3*inch, 3.2*inch, 2.1*inch]))

# Footer
elements.append(Spacer(1, 16))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc')))
elements.append(Paragraph("Prepared by Ryan Rose &mdash; Rose Homes LV &nbsp;|&nbsp; For: Nick Nolf, TNG Property Management", footer_style))

doc.build(elements)
print(f"PDF created: {output_path}")
