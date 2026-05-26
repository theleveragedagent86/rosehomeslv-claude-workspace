#!/usr/bin/env python3
"""
New Construction Home Options PDF - BRANDED VERSION
Nick Middleton & Family
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image as RLImage, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus.flowables import HRFlowable
from reportlab.graphics.shapes import Drawing, Rect, String, Line
from reportlab.graphics import renderPDF
from PIL import Image as PILImage
import os

# ── Paths ──
BASE_DIR = "/Users/ryanrose/Downloads/Claude/Instagram"
OUTPUT_PDF = os.path.join(BASE_DIR, "Middleton_New_Construction_Options_BRANDED.pdf")
BIRCH_IMG = os.path.join(BASE_DIR, "birch_floorplan.png")

# ── Colors - Rich branded palette ──
NAVY = HexColor("#0b1d3a")
DEEP_BLUE = HexColor("#132d5e")
ROYAL = HexColor("#1a3f7a")
GOLD = HexColor("#c9a227")
WARM_GOLD = HexColor("#d4af37")
LIGHT_GOLD = HexColor("#f5e6b8")
CREAM = HexColor("#faf8f0")
LIGHT_BG = HexColor("#f0f2f5")
MED_GRAY = HexColor("#d0d0d0")
TEXT_DARK = HexColor("#1a1a1a")
TEXT_MED = HexColor("#444444")
TEXT_LIGHT = HexColor("#666666")
WHITE = white
ACCENT_GREEN = HexColor("#1b6b20")
ACCENT_RED = HexColor("#b71c1c")

# ── Styles ──
styles = getSampleStyleSheet()

cover_title = ParagraphStyle(
    'CoverTitle', parent=styles['Title'],
    fontSize=38, leading=46, textColor=WHITE,
    alignment=TA_CENTER, spaceAfter=6,
    fontName='Helvetica-Bold'
)
cover_subtitle = ParagraphStyle(
    'CoverSubtitle', parent=styles['Normal'],
    fontSize=20, leading=26, textColor=WARM_GOLD,
    alignment=TA_CENTER, spaceAfter=6,
    fontName='Helvetica'
)
cover_date = ParagraphStyle(
    'CoverDate', parent=styles['Normal'],
    fontSize=13, leading=18, textColor=HexColor("#b0b8c8"),
    alignment=TA_CENTER, spaceAfter=4,
    fontName='Helvetica'
)
section_header = ParagraphStyle(
    'SectionHeader', parent=styles['Heading1'],
    fontSize=24, leading=30, textColor=NAVY,
    spaceAfter=2, spaceBefore=0,
    fontName='Helvetica-Bold'
)
community_name = ParagraphStyle(
    'CommunityName', parent=styles['Heading2'],
    fontSize=14, leading=18, textColor=ROYAL,
    spaceAfter=2, spaceBefore=0,
    fontName='Helvetica-Bold'
)
body_text = ParagraphStyle(
    'BodyText', parent=styles['Normal'],
    fontSize=10, leading=14, textColor=TEXT_DARK,
    spaceAfter=4, fontName='Helvetica'
)
body_bold = ParagraphStyle(
    'BodyBold', parent=styles['Normal'],
    fontSize=10, leading=14, textColor=TEXT_DARK,
    spaceAfter=4, fontName='Helvetica-Bold'
)
small_text = ParagraphStyle(
    'SmallText', parent=styles['Normal'],
    fontSize=9, leading=12, textColor=TEXT_LIGHT,
    spaceAfter=2, fontName='Helvetica'
)
incentive_style = ParagraphStyle(
    'Incentive', parent=styles['Normal'],
    fontSize=10, leading=14, textColor=ACCENT_GREEN,
    spaceAfter=3, fontName='Helvetica-Bold',
    leftIndent=10
)
bullet_style = ParagraphStyle(
    'Bullet', parent=styles['Normal'],
    fontSize=10, leading=14, textColor=TEXT_DARK,
    spaceAfter=2, fontName='Helvetica',
    leftIndent=20, bulletIndent=10
)
note_style = ParagraphStyle(
    'Note', parent=styles['Normal'],
    fontSize=9, leading=13, textColor=ACCENT_RED,
    spaceAfter=4, fontName='Helvetica-Oblique',
    leftIndent=10
)
page_title = ParagraphStyle(
    'PageTitle', parent=styles['Heading1'],
    fontSize=18, leading=24, textColor=NAVY,
    spaceAfter=12, spaceBefore=0,
    fontName='Helvetica-Bold'
)

# ── Helper functions ──

def gold_line():
    return HRFlowable(width="100%", thickness=3, color=GOLD, spaceBefore=6, spaceAfter=10)

def thin_line():
    return HRFlowable(width="100%", thickness=0.5, color=MED_GRAY, spaceBefore=4, spaceAfter=6)

def accent_line():
    return HRFlowable(width="100%", thickness=2, color=ROYAL, spaceBefore=4, spaceAfter=8)

def detail_row(label, value):
    return Paragraph(f'<font color="{ROYAL.hexval()}"><b>{label}:</b></font>  {value}', body_text)

def bullet(text):
    return Paragraph(f"\u2022  {text}", bullet_style)

def incentive_bullet(text):
    return Paragraph(f"\u2713  {text}", incentive_style)

def make_table(headers, rows, col_widths=None):
    """Create a styled data table with branded colors."""
    data = [headers] + rows
    if col_widths is None:
        col_widths = [None] * len(headers)

    header_style = ParagraphStyle('TH', parent=styles['Normal'],
        fontSize=9, leading=12, textColor=WHITE, fontName='Helvetica-Bold', alignment=TA_CENTER)
    cell_style = ParagraphStyle('TC', parent=styles['Normal'],
        fontSize=9, leading=12, textColor=TEXT_DARK, fontName='Helvetica', alignment=TA_CENTER)
    cell_left = ParagraphStyle('TCL', parent=styles['Normal'],
        fontSize=9, leading=12, textColor=TEXT_DARK, fontName='Helvetica', alignment=TA_LEFT)

    formatted = []
    for i, row in enumerate(data):
        frow = []
        for j, cell in enumerate(row):
            if i == 0:
                frow.append(Paragraph(str(cell), header_style))
            else:
                st = cell_left if j == 0 else cell_style
                frow.append(Paragraph(str(cell), st))
        formatted.append(frow)

    t = Table(formatted, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), WHITE),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, CREAM]),
        ('GRID', (0, 0), (-1, -1), 0.75, GOLD),
        ('TOPPADDING', (0, 1), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 7),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t

def branded_section_header(title, subtitle=None):
    """Returns a list of flowables for a branded section header with gold accent."""
    items = []
    # Gold accent bar
    items.append(HRFlowable(width="100%", thickness=4, color=GOLD, spaceBefore=0, spaceAfter=4))
    items.append(Paragraph(title, section_header))
    if subtitle:
        items.append(Paragraph(subtitle, community_name))
    items.append(HRFlowable(width="30%", thickness=2, color=GOLD, spaceBefore=4, spaceAfter=10))
    return items


# ══════════════════════════════════════════
# PAGE HEADER/FOOTER via custom doc template
# ══════════════════════════════════════════

from reportlab.platypus.doctemplate import BaseDocTemplate, PageTemplate, Frame
from reportlab.lib.units import inch

def draw_page_decorations(canvas, doc):
    """Draw branded header bar and footer on every page except the cover."""
    page_num = canvas.getPageNumber()
    width, height = letter

    if page_num == 1:
        # COVER PAGE - Full navy background
        canvas.setFillColor(NAVY)
        canvas.rect(0, 0, width, height, fill=1, stroke=0)

        # Gold accent stripe near top
        canvas.setFillColor(GOLD)
        canvas.rect(0, height - 85, width, 4, fill=1, stroke=0)

        # Gold accent stripe near bottom
        canvas.setFillColor(GOLD)
        canvas.rect(0, 100, width, 4, fill=1, stroke=0)

        # Bottom text
        canvas.setFillColor(HexColor("#6a7a94"))
        canvas.setFont("Helvetica", 9)
        canvas.drawCentredString(width/2, 60, "Prepared with care by Ryan Rose  |  Your Las Vegas Real Estate Resource")
    else:
        # ALL OTHER PAGES - branded header bar
        canvas.setFillColor(NAVY)
        canvas.rect(0, height - 38, width, 38, fill=1, stroke=0)

        # Gold line under header
        canvas.setFillColor(GOLD)
        canvas.rect(0, height - 41, width, 3, fill=1, stroke=0)

        # Header text
        canvas.setFillColor(WHITE)
        canvas.setFont("Helvetica-Bold", 9)
        canvas.drawString(54, height - 25, "New Construction Options")

        canvas.setFillColor(WARM_GOLD)
        canvas.setFont("Helvetica", 9)
        canvas.drawRightString(width - 54, height - 25, "Middleton Family")

        # Footer
        canvas.setStrokeColor(MED_GRAY)
        canvas.setLineWidth(0.5)
        canvas.line(54, 40, width - 54, 40)

        canvas.setFillColor(TEXT_LIGHT)
        canvas.setFont("Helvetica", 8)
        canvas.drawString(54, 28, "Ryan Rose  |  Las Vegas Real Estate")
        canvas.drawRightString(width - 54, 28, f"Page {page_num - 1}")


# Build with custom template
doc = BaseDocTemplate(
    OUTPUT_PDF,
    pagesize=letter,
)

# Frame for cover page (centered, more padding)
cover_frame = Frame(
    1.0*inch, 0.8*inch,
    letter[0] - 2.0*inch, letter[1] - 1.6*inch,
    id='cover'
)

# Frame for content pages (account for header bar)
content_frame = Frame(
    0.75*inch, 0.7*inch,
    letter[0] - 1.5*inch, letter[1] - 1.5*inch,
    id='content'
)

cover_template = PageTemplate(id='cover', frames=[cover_frame], onPage=draw_page_decorations)
content_template = PageTemplate(id='content', frames=[content_frame], onPage=draw_page_decorations)
doc.addPageTemplates([cover_template, content_template])

from reportlab.platypus import NextPageTemplate

story = []

# ════════════════════════════════════════
# PAGE 1: COVER (on navy background)
# ════════════════════════════════════════
story.append(Spacer(1, 2.0*inch))

story.append(Paragraph("New Construction", cover_title))
story.append(Paragraph("Home Options", cover_title))
story.append(Spacer(1, 16))

# Gold divider
story.append(HRFlowable(width="35%", thickness=2, color=WARM_GOLD, spaceBefore=0, spaceAfter=16))

story.append(Paragraph("Prepared for", cover_date))
story.append(Spacer(1, 6))
story.append(Paragraph("Nick Middleton &amp; Family", cover_subtitle))
story.append(Spacer(1, 24))
story.append(Paragraph("March 10, 2026", cover_date))

story.append(Spacer(1, 1.5*inch))

profile_style = ParagraphStyle('Profile', parent=styles['Normal'],
    fontSize=11, leading=16, textColor=HexColor("#8a96ac"), alignment=TA_CENTER, fontName='Helvetica')
story.append(Paragraph("Southwest Las Vegas  |  4+ Bedrooms  |  New Construction", profile_style))

# Switch to content template for all subsequent pages
story.append(NextPageTemplate('content'))
story.append(PageBreak())

# ════════════════════════════════════════
# PAGE 2: COMPARISON TABLE
# ════════════════════════════════════════
for f in branded_section_header("At-a-Glance Comparison"):
    story.append(f)

headers = ["Community", "Builder", "Plan(s)", "Sq Ft", "Bed/Bath", "Base Price", "HOA", "Est. Move-In"]
rows = [
    ["Lexington Chase", "Richmond\nAmerican", "The Birch", "2,310", "4 / 2.5-3", "~$600K", "$94/mo", "July"],
    ["Ironwood", "Century", "2114", "TBD*", "4 / 2.5+", "$535,990+", "TBD", "June"],
    ["Delamar", "Pulte Homes", "Calico\nEgan\nDelano", "2,990 -\n3,158", "4 / 3", "$574,990 -\n$586,990", "$150/mo", "May\n(move-in\nready)"],
    ["Southwind", "Century", "2308\n2605", "2,308 -\n2,605", "4 / 2.5", "$525,990 -\n$543,990", "TBD", "May - July"],
]

col_w = [1.0*inch, 0.85*inch, 0.75*inch, 0.7*inch, 0.65*inch, 0.85*inch, 0.6*inch, 0.7*inch]
story.append(make_table(headers, rows, col_w))

story.append(Spacer(1, 10))
story.append(Paragraph("<i>* Exact sq ft for Ironwood Plan 2114 pending confirmation from builder. Pricing may vary with selected options and upgrades.</i>", small_text))

story.append(Spacer(1, 14))

# Incentives in a highlighted box-like area
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Current Builder Incentives</b></font>', body_bold))
story.append(accent_line())
story.append(incentive_bullet("Richmond American: 3% toward closing/rate buy-down + 2% at design center"))
story.append(incentive_bullet("Ironwood (Century): $10K off price + 6% toward closing costs"))
story.append(incentive_bullet("Delamar (Pulte): 6% closing costs + 4.99% conv. 30-yr fixed (close by end of May)"))
story.append(incentive_bullet("Southwind (Century): 6% toward closing costs (end of May quick move-in)"))

story.append(PageBreak())

# ════════════════════════════════════════
# PAGES 3-4: RICHMOND AMERICAN - LEXINGTON CHASE
# ════════════════════════════════════════
for f in branded_section_header("Richmond American Homes", "Lexington Chase  |  The Birch"):
    story.append(f)

story.append(detail_row("Location", "Southwest Las Vegas, approximately 5 minutes south of Durango Station"))
story.append(detail_row("Community Size", "77 homes"))
story.append(detail_row("HOA", "$94/month  |  No LID/SID"))
story.append(Spacer(1, 6))

story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Plan Details</b></font>', body_bold))
story.append(thin_line())
plan_headers = ["Plan", "Sq Ft", "Bed/Bath", "Stories", "Garage", "Projected Price"]
plan_rows = [["The Birch", "2,310", "4 / 2.5-3", "2-Story", "2-Car", "~$600,000"]]
story.append(make_table(plan_headers, plan_rows, [1.1*inch, 0.8*inch, 0.9*inch, 0.8*inch, 0.8*inch, 1.2*inch]))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Key Features</b></font>', body_bold))
story.append(thin_line())
story.append(bullet("Gourmet kitchen with open great room layout"))
story.append(bullet("Owner's suite with walk-in closet on second floor"))
story.append(bullet("Optional covered patios, balcony, and center-meet doors"))
story.append(bullet("Loft area on second floor"))
story.append(bullet("Study/optional 5th bedroom on main floor"))
story.append(bullet("HERS Index rating of 50 (highly energy efficient; standard new home = 100)"))
story.append(bullet("Customizable interiors available: cabinet colors, flooring selections"))
story.append(bullet("Estimated move-in: July"))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Builder Incentives</b></font>', body_bold))
story.append(thin_line())
story.append(incentive_bullet("3% of base price toward rate buy-down and/or closing costs (with builder's preferred lender)"))
story.append(incentive_bullet("2% of base price at design center for upgrades"))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Estimated Monthly Payment</b></font>', body_bold))
story.append(thin_line())
story.append(Paragraph("Target monthly payment of approximately $3,000 at a ~$600K purchase price.", body_text))

story.append(PageBreak())

# Birch Floorplan page
story.append(Paragraph("The Birch  |  Floor Plan", page_title))
story.append(gold_line())

if os.path.exists(BIRCH_IMG):
    img = PILImage.open(BIRCH_IMG)
    iw, ih = img.size
    max_w = 6.5 * inch
    max_h = 7.5 * inch
    ratio = min(max_w / iw, max_h / ih)
    story.append(RLImage(BIRCH_IMG, width=iw*ratio, height=ih*ratio))
else:
    story.append(Paragraph("<i>Floor plan image not available</i>", small_text))

story.append(Spacer(1, 6))
story.append(Paragraph("Approx. 2,310 sq ft  |  3-5 Bed  |  2.5-3 Bath  |  2-Car Garage", small_text))

story.append(PageBreak())

# ════════════════════════════════════════
# PAGES 5-6: CENTURY - IRONWOOD
# ════════════════════════════════════════
for f in branded_section_header("Century", "Ironwood  |  Plan 2114"):
    story.append(f)

story.append(detail_row("Location", "Southwest Las Vegas, off Durango Drive"))
story.append(detail_row("Community Size", "105 home sites"))
story.append(detail_row("HOA", "To be confirmed"))
story.append(Spacer(1, 6))

story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Plan Details</b></font>', body_bold))
story.append(thin_line())
plan_headers2 = ["Plan", "Base Price", "Stories", "Garage", "Configuration"]
plan_rows2 = [["2114", "$535,990", "2-Story", "2-Car", "Highly configurable\n(3-6 bed options)"]]
story.append(make_table(plan_headers2, plan_rows2, [0.8*inch, 1.1*inch, 0.8*inch, 0.8*inch, 2.2*inch]))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Configuration Options for 4-Bedroom Layout</b></font>', body_bold))
story.append(thin_line())
story.append(bullet("Bed 4 / Bath in lieu of Den / Powder: +$7,350"))
story.append(bullet("Bed 5 in lieu of Loft: +$5,150"))
story.append(bullet("Bed 6 in lieu of Loft: +$3,750"))
story.append(bullet("Super Loft option: +$400"))
story.append(bullet("Super Great Room (deletes Den/Bed 4, reconfigures kitchen): +$2,550"))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Elevation Styles</b></font>', body_bold))
story.append(thin_line())

elev_h = ["Style", "Description", "Additional Cost"]
elev_r = [
    ["Traditional", "6-Panel Square entry; short panel garage door", "Included"],
    ["Modern", "2-Panel Square entry; long panel garage door", "+$450"],
    ["Craftsman", "Cheyenne entry doors; carriage garage door", "+$1,150"],
]
story.append(make_table(elev_h, elev_r, [1.2*inch, 2.8*inch, 1.2*inch]))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Smart Home Standard (Included)</b></font>', body_bold))
story.append(thin_line())
story.append(bullet("Schlage Z-wave front door deadbolt"))
story.append(bullet("Ecobee Wi-Fi thermostat"))
story.append(bullet("Qolsys IQ security panel"))
story.append(bullet("Amazon eero WiFi mesh system"))
story.append(bullet("3-year prepaid Alarm.com subscription"))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Builder Incentives (June Homes)</b></font>', body_bold))
story.append(thin_line())
story.append(incentive_bullet("$10,000 off the purchase price"))
story.append(incentive_bullet("6% of base price toward closing costs and rate buy-down (with Inspire Home Loans)"))
story.append(incentive_bullet("Special financing rates available through April closings (May likely to be added)"))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Available Lots of Note</b></font>', body_bold))
story.append(thin_line())
story.append(bullet("Lot 34* and Lot 13: Oversized home sites, permitted only (more customization flexibility)"))
story.append(Paragraph("<i>* May be Lot 36 rather than Lot 34; awaiting clarification from the builder.</i>", small_text))
story.append(bullet("All other lots are spec'd, but interior non-structural options can still be changed"))

story.append(Spacer(1, 14))

# Ironwood Upgrades - flows onto same/next page
story.append(Paragraph("Ironwood  |  Popular Upgrade Options", page_title))
story.append(gold_line())

story.append(Paragraph("The following is a selection of available upgrades. Full option catalog available upon request.", small_text))
story.append(Spacer(1, 8))

story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Covered Patio Options</b></font>', body_bold))
story.append(thin_line())
patio_h = ["Option", "Price"]
patio_r = [
    ["Alumawood Patio Cover - Lattice", "$5,450"],
    ["Alumawood Patio Cover - Solid", "$4,150"],
    ["Full Patio Cover", "$9,750"],
    ["Patio Pavers Only", "$950"],
]
story.append(make_table(patio_h, patio_r, [3.5*inch, 1.5*inch]))

story.append(Spacer(1, 8))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Fireplace Options</b></font>', body_bold))
story.append(thin_line())
fp_h = ["Option", "Price"]
fp_r = [
    ['55" Linear Electric Fireplace (includes flat-screen pre-wire)', "$3,850"],
    ['78" Linear Electric Fireplace (includes flat-screen pre-wire)', "$4,600"],
]
story.append(make_table(fp_h, fp_r, [3.5*inch, 1.5*inch]))

story.append(Spacer(1, 8))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Appliance Packages (LG)</b></font>', body_bold))
story.append(thin_line())
app_h = ["Package", "Price"]
app_r = [
    ["Base Level Package (Gas) - Standard", "Included"],
    ["Silver Package (Gas)", "+$330"],
    ["Gold Package (Single Oven/OTR Microwave, Gas)", "+$3,400"],
    ["Washer/Dryer Base Level Package", "+$1,430"],
    ['Refrigerator (27 cu. ft. Side-by-Side)', "+$1,340"],
]
story.append(make_table(app_h, app_r, [3.5*inch, 1.5*inch]))

story.append(Spacer(1, 8))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Electrical Upgrades</b></font>', body_bold))
story.append(thin_line())
el_h = ["Package", "Includes", "Price"]
el_r = [
    ["Upgrade 1", "Ceiling fan pre-wire (all rooms), cable in bedrooms & loft", "$1,310"],
    ["Upgrade 2", "Everything in Upgrade 1 + EV charger pre-wire, puck lights,\nflat screen pre-wire, low volt panel", "$2,680"],
]
story.append(make_table(el_h, el_r, [1.0*inch, 3.3*inch, 0.9*inch]))

story.append(Spacer(1, 8))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Water Filtration</b></font>', body_bold))
story.append(thin_line())
wtr_h = ["Option", "Price"]
wtr_r = [
    ["Drinking Water System", "$250"],
    ["Reverse Osmosis System", "$650"],
    ["Water Softener", "$1,700"],
    ["Water Softener - Upgrade", "$2,400"],
]
story.append(make_table(wtr_h, wtr_r, [3.5*inch, 1.5*inch]))

story.append(Spacer(1, 8))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Design Packages</b></font>', body_bold))
story.append(thin_line())
pkg_h = ["Package Level", "Price"]
pkg_r = [
    ["Prelude (Base)", "Included"],
    ["Crescendo I", "$9,860"],
    ["Mezzo I", "$9,600"],
    ["Dolce II", "$17,800"],
    ["Aria II", "$18,440"],
    ["Tempo II", "$19,000"],
    ["Aria III / Mezzo III", "$20,970"],
]
story.append(make_table(pkg_h, pkg_r, [3.5*inch, 1.5*inch]))
story.append(Spacer(1, 4))
story.append(Paragraph("<i>Primary bath wall tile upgrades available with select packages ($2,300 - $3,200 additional)</i>", small_text))

story.append(PageBreak())

# ════════════════════════════════════════
# PULTE HOMES - DELAMAR
# ════════════════════════════════════════
for f in branded_section_header("Pulte Homes", "Delamar  |  Highlands Ranch, Southern Highlands"):
    story.append(f)

story.append(detail_row("Location", "Southern Highlands area, Southwest Las Vegas (89141)"))
story.append(detail_row("Available Homes", "15 units currently available"))
story.append(detail_row("HOA", "$150/month"))
story.append(detail_row("Freeway Access", "I-15 and 215 Beltway"))
story.append(Spacer(1, 6))

story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Available Plans</b></font>', body_bold))
story.append(thin_line())
pulte_h = ["Plan", "Sq Ft", "Bed/Bath", "Stories", "Garage", "Starting Price"]
pulte_r = [
    ["Calico", "3,097", "4 / 3", "2-Story", "2-Car", "$574,990"],
    ["Egan", "3,158", "4 / 3", "2-Story", "2-Car", "$578,990"],
    ["Delano", "2,990", "4 / 3", "2-Story", "2-Car", "$586,990"],
]
story.append(make_table(pulte_h, pulte_r, [0.9*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch, 1.1*inch]))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Plan Highlights</b></font>', body_bold))
story.append(thin_line())
story.append(bullet("<b>Calico:</b> First-floor bedroom, large kitchen, flexible layout"))
story.append(bullet("<b>Egan:</b> Family room + gathering room, private owner's retreat, upstairs game room"))
story.append(bullet("<b>Delano:</b> Optional first-floor guest suite, open living spaces, spacious laundry"))
story.append(bullet("All plans include Pulte's Life Tested Home designs with smart home technology"))
story.append(bullet("Rooftop deck options available on select plans"))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Builder Incentives (Move-In Ready Homes, Close by End of May)</b></font>', body_bold))
story.append(thin_line())
story.append(incentive_bullet("6% of purchase price toward closing costs"))
story.append(incentive_bullet("4.99% conventional 30-year fixed interest rate"))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Important Note on Finishes</b></font>', body_bold))
story.append(thin_line())
story.append(Paragraph(
    "Pulte's professional design team curates the interior finish selections for their homes. "
    "An in-person visit to the model home and/or design center is strongly recommended to "
    "evaluate the chosen finishes and available options before making a decision.",
    body_text
))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Nearby Amenities</b></font>', body_bold))
story.append(thin_line())
story.append(bullet("Southern Highlands shopping, dining, and golf club"))
story.append(bullet("Quick freeway access for commuting"))

story.append(PageBreak())

# ════════════════════════════════════════
# CENTURY - SOUTHWIND
# ════════════════════════════════════════
for f in branded_section_header("Century", "Southwind  |  Southwest Las Vegas"):
    story.append(f)

story.append(detail_row("Location", "Southwest Las Vegas (89178), near Mountain's Edge"))
story.append(detail_row("Access", "I-15 / Blue Diamond Road and I-215 / Durango Drive"))
story.append(detail_row("HOA", "$0/month"))
story.append(Spacer(1, 4))
story.append(Paragraph('<font color="' + ACCENT_GREEN.hexval() + '"><b>Lowest HOA of all options presented</b></font>', body_text))
story.append(Spacer(1, 6))

story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Plans of Interest</b></font>', body_bold))
story.append(thin_line())
sw_h = ["Plan", "Sq Ft", "Bed/Bath", "Stories", "Garage", "Base Price"]
sw_r = [
    ["Residence 2308", "2,308", "3-4 / 2.5", "2-Story", "2-Car", "$525,990"],
    ["Residence 2605", "2,605", "3-5 / 2.5-3", "2-Story", "2-Car", "$543,990"],
]
story.append(make_table(sw_h, sw_r, [1.2*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch, 1.0*inch]))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>4-Bedroom Configuration Notes</b></font>', body_bold))
story.append(thin_line())
story.append(bullet("<b>Plan 2308:</b> The 4th bedroom replaces the loft on the second floor"))
story.append(bullet("<b>Plan 2605:</b> The 4th bedroom is located downstairs on the first floor"))
story.append(bullet("With model-home level finishes, final price is expected to be just under $600K"))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Timeline Options</b></font>', body_bold))
story.append(thin_line())
story.append(bullet("<b>Fully customized selections:</b> June or July move-in/close"))
story.append(bullet("<b>Quick move-in (close by end of May):</b> Limited customization but faster timeline"))

story.append(Spacer(1, 10))
story.append(Paragraph('<font color="' + NAVY.hexval() + '"><b>Builder Incentives</b></font>', body_bold))
story.append(thin_line())
story.append(incentive_bullet("Quick move-in (end of May close): 6% toward closing costs"))
story.append(Paragraph("    <i>Note: This 6% applies to rate buy-down and standard closing costs only, not interior upgrades or customizations.</i>", small_text))
story.append(Spacer(1, 4))
story.append(incentive_bullet("Website promotional rate: 3.75% first-year rate (4.608% APR) with Inspire Home Loans"))

story.append(Spacer(1, 10))
story.append(Paragraph(
    "NOTE: Written confirmation of all incentive details from the builder is pending and expected by March 11, 2026. "
    "The information above is based on verbal communication and may be updated once confirmed in writing.",
    note_style
))

story.append(PageBreak())

# ════════════════════════════════════════
# ADDITIONAL OPTIONS
# ════════════════════════════════════════
story.append(Spacer(1, 1.2*inch))
for f in branded_section_header("Additional Options"):
    story.append(f)
story.append(Spacer(1, 16))

coming_soon = ParagraphStyle('ComingSoon', parent=styles['Normal'],
    fontSize=14, leading=20, textColor=ROYAL, alignment=TA_CENTER, fontName='Helvetica')

story.append(Paragraph("Two additional new construction communities are currently being evaluated.", coming_soon))
story.append(Spacer(1, 16))
story.append(Paragraph("Details will be shared as they are confirmed.", coming_soon))
story.append(Spacer(1, 30))
story.append(HRFlowable(width="40%", thickness=1, color=GOLD, spaceBefore=0, spaceAfter=0))

story.append(PageBreak())

# ════════════════════════════════════════
# NEXT STEPS
# ════════════════════════════════════════
story.append(Spacer(1, 0.6*inch))
for f in branded_section_header("Next Steps"):
    story.append(f)
story.append(Spacer(1, 12))

step_style = ParagraphStyle('Step', parent=styles['Normal'],
    fontSize=12, leading=18, textColor=TEXT_DARK, fontName='Helvetica',
    spaceAfter=14, leftIndent=30)

steps = [
    "<b>1.</b>  Review the options in this document and let me know which communities stand out to you. Once I know your top picks, I'll get tours lined up for Sunday, March 15th so we can see everything in one day.",
    "<b>2.</b>  Discuss financing and get pre-approved so we can move quickly when you find the right fit.",
    "<b>3.</b>  <b>Important note on incentives:</b> The rate buy-downs and closing cost incentives listed for each builder are offered through their on-site preferred lenders. If you choose to use your own financing instead, those specific incentives would no longer apply.",
    "<b>4.</b>  Reach out with any questions. I'm here to help at every step of the process.",
]
for s in steps:
    story.append(Paragraph(s, step_style))

story.append(Spacer(1, 40))
story.append(HRFlowable(width="50%", thickness=3, color=GOLD, spaceBefore=0, spaceAfter=16))

contact_style = ParagraphStyle('Contact', parent=styles['Normal'],
    fontSize=15, leading=20, textColor=NAVY, alignment=TA_CENTER, fontName='Helvetica-Bold')
contact_sub = ParagraphStyle('ContactSub', parent=styles['Normal'],
    fontSize=11, leading=16, textColor=ROYAL, alignment=TA_CENTER, fontName='Helvetica')

story.append(Paragraph("Ryan Rose", contact_style))
story.append(Spacer(1, 4))
story.append(Paragraph("Your Las Vegas Real Estate Resource", contact_sub))

# ── Build ──
doc.build(story)
print(f"PDF created: {OUTPUT_PDF}")
print(f"File size: {os.path.getsize(OUTPUT_PDF):,} bytes")
