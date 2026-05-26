#!/usr/bin/env python3
"""
New Construction Home Options PDF for Nick Middleton & Family
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image as RLImage, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus.flowables import HRFlowable
from reportlab.graphics.shapes import Drawing, Circle, String, Line, Rect
from PIL import Image as PILImage
import os

# ── Paths ──
BASE_DIR = "/Users/ryanrose/Downloads/Claude/Instagram"
OUTPUT_PDF = "/Users/ryanrose/Downloads/Claude/Buyers/Nick Middleton/Middleton_New_Construction_Options.FINAL.pdf"
BIRCH_IMG = os.path.join(BASE_DIR, "birch_floorplan.png")
MAP_IMG = os.path.join(BASE_DIR, "vegas_community_map.png")

# ── Colors ──
DARK = HexColor("#1a1a2e")
ACCENT = HexColor("#16213e")
HIGHLIGHT = HexColor("#0f3460")
GOLD = HexColor("#c9a227")
LIGHT_BG = HexColor("#f5f5f5")
MED_GRAY = HexColor("#e0e0e0")
TEXT_DARK = HexColor("#2c2c2c")
TEXT_MED = HexColor("#555555")
WHITE = white

# ── Styles ──
styles = getSampleStyleSheet()

# Cover styles
cover_title = ParagraphStyle(
    'CoverTitle', parent=styles['Title'],
    fontSize=32, leading=40, textColor=DARK,
    alignment=TA_CENTER, spaceAfter=8,
    fontName='Helvetica-Bold'
)
cover_subtitle = ParagraphStyle(
    'CoverSubtitle', parent=styles['Normal'],
    fontSize=18, leading=24, textColor=HIGHLIGHT,
    alignment=TA_CENTER, spaceAfter=6,
    fontName='Helvetica'
)
cover_date = ParagraphStyle(
    'CoverDate', parent=styles['Normal'],
    fontSize=12, leading=16, textColor=TEXT_MED,
    alignment=TA_CENTER, spaceAfter=4,
    fontName='Helvetica'
)

# Section styles
section_header = ParagraphStyle(
    'SectionHeader', parent=styles['Heading1'],
    fontSize=22, leading=28, textColor=DARK,
    spaceAfter=4, spaceBefore=0,
    fontName='Helvetica-Bold'
)
community_name = ParagraphStyle(
    'CommunityName', parent=styles['Heading2'],
    fontSize=14, leading=18, textColor=HIGHLIGHT,
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
    fontSize=9, leading=12, textColor=TEXT_MED,
    spaceAfter=2, fontName='Helvetica'
)
incentive_style = ParagraphStyle(
    'Incentive', parent=styles['Normal'],
    fontSize=10, leading=14, textColor=HexColor("#1b5e20"),
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
    fontSize=9, leading=13, textColor=HexColor("#b71c1c"),
    spaceAfter=4, fontName='Helvetica-Oblique',
    leftIndent=10
)
page_title = ParagraphStyle(
    'PageTitle', parent=styles['Heading1'],
    fontSize=18, leading=24, textColor=DARK,
    spaceAfter=12, spaceBefore=0,
    fontName='Helvetica-Bold'
)

# ── Helper functions ──

def gold_line():
    return HRFlowable(width="100%", thickness=2, color=GOLD, spaceBefore=6, spaceAfter=10)

def thin_line():
    return HRFlowable(width="100%", thickness=0.5, color=MED_GRAY, spaceBefore=4, spaceAfter=6)

def section_divider():
    return HRFlowable(width="100%", thickness=1.5, color=HIGHLIGHT, spaceBefore=8, spaceAfter=10)

def detail_row(label, value):
    return Paragraph(f"<b>{label}:</b>  {value}", body_text)

def bullet(text):
    return Paragraph(f"\u2022  {text}", bullet_style)

def incentive_bullet(text):
    return Paragraph(f"\u2713  {text}", incentive_style)

def make_table(headers, rows, col_widths=None):
    """Create a styled data table."""
    data = [headers] + rows
    if col_widths is None:
        col_widths = [None] * len(headers)

    # Convert header strings to bold paragraphs
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
        ('BACKGROUND', (0, 0), (-1, 0), HIGHLIGHT),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), WHITE),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('GRID', (0, 0), (-1, -1), 0.5, MED_GRAY),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t


# ── Build the document ──

doc = SimpleDocTemplate(
    OUTPUT_PDF,
    pagesize=letter,
    topMargin=0.6*inch,
    bottomMargin=0.6*inch,
    leftMargin=0.75*inch,
    rightMargin=0.75*inch,
)

story = []

# ════════════════════════════════════════
# PAGE 1: COVER
# ════════════════════════════════════════
story.append(Spacer(1, 1.8*inch))

# Decorative top line
story.append(HRFlowable(width="60%", thickness=3, color=GOLD, spaceBefore=0, spaceAfter=20))

story.append(Paragraph("New Construction", cover_title))
story.append(Paragraph("Home Options", cover_title))
story.append(Spacer(1, 12))
story.append(HRFlowable(width="40%", thickness=1, color=HIGHLIGHT, spaceBefore=0, spaceAfter=16))
story.append(Paragraph("Prepared for", cover_date))
story.append(Spacer(1, 4))
story.append(Paragraph("Nick Middleton &amp; Family", cover_subtitle))
story.append(Spacer(1, 20))
story.append(Paragraph("March 10, 2026", cover_date))
story.append(Spacer(1, 8))
story.append(HRFlowable(width="60%", thickness=3, color=GOLD, spaceBefore=16, spaceAfter=0))

story.append(Spacer(1, 1.2*inch))

# Buyer profile summary
profile_style = ParagraphStyle('Profile', parent=styles['Normal'],
    fontSize=10, leading=15, textColor=TEXT_MED, alignment=TA_CENTER, fontName='Helvetica')
story.append(Paragraph("Las Vegas Valley  |  4+ Bedrooms  |  New Construction", profile_style))
story.append(Spacer(1, 6))
story.append(Paragraph("Curated options based on your preferences and budget", profile_style))

story.append(PageBreak())

# ════════════════════════════════════════
# PAGE 2: COMPARISON TABLE
# ════════════════════════════════════════
story.append(Paragraph("At-a-Glance Comparison", section_header))
story.append(gold_line())

headers = ["Community", "Builder", "Plan(s)", "Sq Ft", "Bed/Bath", "Price Range", "HOA", "Move-In"]
rows = [
    ["Delamar", "Pulte", "Calico, Egan,\nDelano", "2,990 -\n3,158", "4 / 3", "$575K -\n$587K", "$150/mo", "May"],
    ["Cordora", "Pulte", "Mesquite,\nJuniper", "2,255 -\n2,325", "4 / 2.5", "$586K -\n$593K", "TBD", "Aug -\nSept"],
    ["Paldona", "Pulte", "Adler, Halton,\nHalton Peak", "1,866 -\n2,708", "3-4 / 2.5-3", "$534K -\n$559K", "TBD", "TBD"],
    ["Southwind", "Century", "2054, 2308,\n2605", "2,054 -\n2,605", "4 / 2.5-3.5", "$530K -\n$582K", "TBD", "Apr -\nJune"],
    ["Ironwood", "Century", "2114", "TBD*", "4 / 2.5+", "$536K+", "TBD", "June"],
]

col_w = [0.9*inch, 0.75*inch, 0.85*inch, 0.7*inch, 0.65*inch, 0.8*inch, 0.7*inch, 0.65*inch]
story.append(make_table(headers, rows, col_w))

story.append(Spacer(1, 8))
story.append(Paragraph("<i>* Ironwood sq ft pending confirmation. Pricing may vary with selected options and upgrades.</i>", small_text))

story.append(Spacer(1, 12))

# Incentives summary
story.append(Paragraph("Current Builder Incentives", community_name))
story.append(thin_line())
story.append(incentive_bullet("Delamar (Pulte): 6% closing costs + 4.99% conv. 30-yr fixed (close by end of May)"))
story.append(incentive_bullet("Cordora (Pulte): 3% toward closing costs"))
story.append(incentive_bullet("Paldona (Pulte): Incentives pending confirmation"))
story.append(incentive_bullet("Southwind (Century): 3.75% ARM (FHA/VA), 3.875% ARM (Conv.), 6% for dirt builds"))
story.append(incentive_bullet("Ironwood (Century): $10K off price + 6% toward closing costs"))
story.append(PageBreak())

# ════════════════════════════════════════
# PULTE HOMES - DELAMAR
# ════════════════════════════════════════
story.append(Paragraph("Pulte Homes", section_header))
story.append(Paragraph("Delamar  |  Highlands Ranch, Southern Highlands", community_name))
story.append(gold_line())

story.append(detail_row("Location", "Southern Highlands area, Southwest Las Vegas (89141)"))
story.append(detail_row("Available Homes", "15 units currently available"))
story.append(detail_row("HOA", "$150/month"))
story.append(detail_row("Freeway Access", "I-15 and 215 Beltway"))
story.append(Spacer(1, 6))

story.append(Paragraph("Available Plans", body_bold))
story.append(thin_line())
pulte_h = ["Plan", "Sq Ft", "Bed/Bath", "Stories", "Garage", "Starting Price"]
pulte_r = [
    ["Calico", "3,097", "4 / 3", "2-Story", "2-Car", "$574,990"],
    ["Egan", "3,158", "4 / 3", "2-Story", "2-Car", "$578,990"],
    ["Delano", "2,990", "4 / 3", "2-Story", "2-Car", "$586,990"],
]
story.append(make_table(pulte_h, pulte_r, [0.9*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch, 1.1*inch]))

story.append(Spacer(1, 10))
story.append(Paragraph("Plan Highlights", body_bold))
story.append(thin_line())
story.append(bullet("<b>Calico:</b> First-floor bedroom, large kitchen, flexible layout"))
story.append(bullet("<b>Egan:</b> Family room + gathering room, private owner's retreat, upstairs game room"))
story.append(bullet("<b>Delano:</b> Optional first-floor guest suite, open living spaces, spacious laundry"))
story.append(bullet("All plans include Pulte's Life Tested Home designs with smart home technology"))
story.append(bullet("Rooftop deck options available on select plans"))

story.append(Spacer(1, 10))
story.append(Paragraph("Builder Incentives (Move-In Ready Homes, Close by End of May)", body_bold))
story.append(thin_line())
story.append(incentive_bullet("6% of purchase price toward closing costs"))
story.append(incentive_bullet("4.99% conventional 30-year fixed interest rate"))

story.append(Spacer(1, 10))
story.append(Paragraph("Important Note on Finishes", body_bold))
story.append(thin_line())
story.append(Paragraph(
    "Pulte's professional design team curates the interior finish selections for their homes. "
    "An in-person visit to the model home and/or design center is strongly recommended to "
    "evaluate the chosen finishes and available options before making a decision.",
    body_text
))

story.append(Spacer(1, 10))
story.append(Paragraph("Nearby Amenities", body_bold))
story.append(thin_line())
story.append(bullet("Southern Highlands shopping, dining, and golf club"))
story.append(bullet("Quick freeway access for commuting"))

story.append(PageBreak())

# ════════════════════════════════════════
# PULTE HOMES - CORDORA
# ════════════════════════════════════════
story.append(Paragraph("Pulte Homes", section_header))
story.append(Paragraph("Cordora  |  Southwest Las Vegas", community_name))
story.append(gold_line())

story.append(detail_row("Location", "8784 Indigo Spring Street, Las Vegas, NV 89139"))
story.append(detail_row("Status", "Just started selling; models open March 21, 2026"))
story.append(detail_row("HOA", "TBD (community association fees required)"))
story.append(detail_row("Community", "Private onsite park"))
story.append(Spacer(1, 6))

story.append(Paragraph("Available Plans", body_bold))
story.append(thin_line())
cord_h = ["Plan", "Sq Ft", "Bed/Bath", "Stories", "Garage", "Starting Price"]
cord_r = [
    ["Mesquite", "2,255", "4 / 2.5", "2-Story", "2-Car", "$585,990"],
    ["Juniper", "2,325", "4 / 2.5", "2-Story", "2-Car", "$592,990"],
]
story.append(make_table(cord_h, cord_r, [0.9*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch, 1.1*inch]))

story.append(Spacer(1, 10))
story.append(Paragraph("Plan Highlights", body_bold))
story.append(thin_line())
story.append(bullet("<b>Mesquite:</b> Kitchen overlooking gathering room, flex room/loft options, owner's suite with spa shower"))
story.append(bullet("<b>Juniper:</b> Designed for families with thoughtful storage, 2-story open layout"))
story.append(bullet("All plans include Pulte's Life Tested Home designs with smart home technology"))

story.append(Spacer(1, 10))
story.append(Paragraph("Builder Incentives", body_bold))
story.append(thin_line())
story.append(incentive_bullet("3% toward closing costs"))

story.append(Spacer(1, 10))
story.append(Paragraph("Timeline", body_bold))
story.append(thin_line())
story.append(bullet("Estimated completions: August / September 2026"))

story.append(Spacer(1, 10))
story.append(Paragraph("Quinn Canyon (Sister Community)", body_bold))
story.append(thin_line())
story.append(Paragraph(
    "Quinn Canyon is located immediately next door and offers the same floor plans with "
    "more current availability. Models are open now and can be viewed during the Sunday "
    "3/15 tour. Cordora models open 3/21.",
    body_text
))

story.append(PageBreak())

# ════════════════════════════════════════
# PULTE HOMES - PALDONA
# ════════════════════════════════════════
story.append(Paragraph("Pulte Homes", section_header))
story.append(Paragraph("Paldona  |  Southwest Las Vegas", community_name))
story.append(gold_line())

story.append(detail_row("Location", "8744 Indigo Springs Rd, Las Vegas, NV 89139"))
story.append(detail_row("Status", "Now selling"))
story.append(detail_row("HOA", "TBD (community association fees required)"))
story.append(Spacer(1, 6))

story.append(Paragraph("Available Plans", body_bold))
story.append(thin_line())
pald_h = ["Plan", "Sq Ft", "Bed/Bath", "Stories", "Garage", "Starting Price"]
pald_r = [
    ["Adler", "1,866", "3 / 2.5", "2-Story", "2-Car", "$533,990"],
    ["Halton", "2,034", "3 / 3", "2-Story", "2-Car", "$539,990"],
    ["Halton Peak", "2,708", "3-4 / 3", "3-Story", "2-Car", "$558,990"],
]
story.append(make_table(pald_h, pald_r, [1.0*inch, 0.7*inch, 0.8*inch, 0.8*inch, 0.8*inch, 1.1*inch]))

story.append(Spacer(1, 10))
story.append(Paragraph("Plan Highlights", body_bold))
story.append(thin_line())
story.append(bullet("<b>Adler:</b> 2-story with open kitchen and gathering room, upstairs loft near bedrooms"))
story.append(bullet("<b>Halton:</b> Flexible 2-story design with open kitchen, loft workspace, and smart home features"))
story.append(bullet("<b>Halton Peak:</b> 3-story with optional 4th bedroom, game room, walk-in laundry near bedrooms"))
story.append(bullet("All plans include Pulte's Life Tested Home designs with smart home technology"))

story.append(Spacer(1, 10))
story.append(Paragraph("Builder Incentives", body_bold))
story.append(thin_line())
story.append(incentive_bullet("Incentives pending confirmation"))

story.append(Spacer(1, 10))
story.append(Paragraph("Note", body_bold))
story.append(thin_line())
story.append(Paragraph(
    "Paldona is located adjacent to Cordora on Indigo Springs. "
    "An in-person visit to the model home and/or design center is strongly recommended to "
    "evaluate the chosen finishes and available options before making a decision.",
    body_text
))

story.append(PageBreak())

# ════════════════════════════════════════
# CENTURY COMMUNITIES - SOUTHWIND
# ════════════════════════════════════════
story.append(Paragraph("Century", section_header))
story.append(Paragraph("Southwind  |  Southwest Las Vegas", community_name))
story.append(gold_line())

story.append(detail_row("Location", "Southwest Las Vegas (89178), near Mountain's Edge"))
story.append(detail_row("Access", "I-15 / Blue Diamond Road and I-215 / Durango Drive"))
story.append(detail_row("HOA", "TBD"))
story.append(Spacer(1, 6))

story.append(Paragraph("Available Plans", body_bold))
story.append(thin_line())
sw_h = ["Plan", "Sq Ft", "Bed/Bath", "Stories", "Garage", "Base Price"]
sw_r = [
    ["Residence 2054", "2,054", "3-4 / 2.5", "2-Story", "2-Car", "$510,990"],
    ["Residence 2308", "2,308", "3-4 / 2.5", "2-Story", "2-Car", "$525,990"],
    ["Residence 2605", "2,605", "3-5 / 2.5-3.5", "2-Story", "2-Car", "$543,990"],
]
story.append(make_table(sw_h, sw_r, [1.2*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch, 1.0*inch]))

story.append(Spacer(1, 10))
story.append(Paragraph("Current Inventory (4+ Bedrooms)", body_bold))
story.append(thin_line())
inv_h = ["Plan", "Sq Ft", "Bed/Bath", "Lot", "Price", "Move-In", "Interior Package"]
inv_r = [
    ["Res 2054", "2,054", "4 / 2.5", "#224", "$530,430\n(was $540,430)", "June", "Mezzo I, 42\"\nFlagstone cabs"],
    ["Res 2308", "2,308", "4 / 2.5", "#262", "$564,990", "April", "Tempo II, 42\"\nWhite cabs"],
    ["Res 2605", "2,605", "5 / 3.5", "#263", "$575,490", "April", "Prelude Java\n42\" cabs"],
    ["Res 2605", "2,605", "4 / 3.5", "#225", "$581,490\n(was $591,490)", "June", "Tempo II, 42\"\nFlagstone cabs"],
]
story.append(make_table(inv_h, inv_r, [0.7*inch, 0.6*inch, 0.6*inch, 0.45*inch, 0.95*inch, 0.55*inch, 1.35*inch]))
story.append(Spacer(1, 4))
story.append(Paragraph("<i>All inventory homes include upgraded electrical packages and 8 ft front entry doors. Addresses on Ruby Dome Ave.</i>", small_text))

story.append(Spacer(1, 10))
story.append(Paragraph("Configuration Notes", body_bold))
story.append(thin_line())
story.append(bullet("<b>Plan 2054:</b> Base is 3 bed; Lot #224 is configured as 4 bed/2.5 bath"))
story.append(bullet("<b>Plan 2308:</b> The 4th bedroom replaces the loft on the second floor"))
story.append(bullet("<b>Plan 2605:</b> The 4th bedroom is located downstairs on the first floor"))

story.append(Spacer(1, 10))
story.append(Paragraph("Timeline Options", body_bold))
story.append(thin_line())
story.append(bullet("<b>Current inventory:</b> April and June move-ins available (see table above)"))
story.append(bullet("<b>Dirt build (custom):</b> Late summer move-in with full customization"))

story.append(Spacer(1, 10))
story.append(Paragraph("Builder Incentives (Confirmed)", body_bold))
story.append(thin_line())
story.append(incentive_bullet("3.75% 5/1 ARM on FHA/VA (with Inspire Home Loans)"))
story.append(incentive_bullet("3.875% 7/6 ARM on Conventional (with Inspire Home Loans)"))
story.append(incentive_bullet("Dirt build: 6% of base price toward closing costs / rate buy-down"))

story.append(PageBreak())

# ════════════════════════════════════════
# CENTURY COMMUNITIES - IRONWOOD
# ════════════════════════════════════════
story.append(Paragraph("Century", section_header))
story.append(Paragraph("Ironwood  |  Plan 2114", community_name))
story.append(gold_line())

story.append(detail_row("Location", "Southwest Las Vegas, off Durango Drive"))
story.append(detail_row("Community Size", "105 home sites"))
story.append(detail_row("HOA", "To be confirmed"))
story.append(Spacer(1, 6))

story.append(Paragraph("Plan Details", body_bold))
story.append(thin_line())
plan_headers2 = ["Plan", "Base Price", "Stories", "Garage", "Configuration"]
plan_rows2 = [["2114", "$535,990", "2-Story", "2-Car", "Highly configurable\n(3-6 bed options)"]]
story.append(make_table(plan_headers2, plan_rows2, [0.8*inch, 1.1*inch, 0.8*inch, 0.8*inch, 2.2*inch]))

story.append(Spacer(1, 10))
story.append(Paragraph("Configuration Options for 4-Bedroom Layout", body_bold))
story.append(thin_line())
story.append(bullet("Bed 4 / Bath in lieu of Den / Powder: +$7,350"))
story.append(bullet("Bed 5 in lieu of Loft: +$5,150"))
story.append(bullet("Bed 6 in lieu of Loft: +$3,750"))
story.append(bullet("Super Loft option: +$400"))
story.append(bullet("Super Great Room (deletes Den/Bed 4, reconfigures kitchen): +$2,550"))

story.append(Spacer(1, 10))
story.append(Paragraph("Elevation Styles", body_bold))
story.append(thin_line())

elev_h = ["Style", "Description", "Additional Cost"]
elev_r = [
    ["Traditional", "6-Panel Square entry; short panel garage door", "Included"],
    ["Modern", "2-Panel Square entry; long panel garage door", "+$450"],
    ["Craftsman", "Cheyenne entry doors; carriage garage door", "+$1,150"],
]
story.append(make_table(elev_h, elev_r, [1.2*inch, 2.8*inch, 1.2*inch]))

story.append(Spacer(1, 10))
story.append(Paragraph("Smart Home Standard (Included)", body_bold))
story.append(thin_line())
story.append(bullet("Schlage Z-wave front door deadbolt"))
story.append(bullet("Ecobee Wi-Fi thermostat"))
story.append(bullet("Qolsys IQ security panel"))
story.append(bullet("Amazon eero WiFi mesh system"))
story.append(bullet("3-year prepaid Alarm.com subscription"))

story.append(Spacer(1, 10))
story.append(Paragraph("Builder Incentives (June Homes)", body_bold))
story.append(thin_line())
story.append(incentive_bullet("$10,000 off the purchase price"))
story.append(incentive_bullet("6% of base price toward closing costs and rate buy-down (with Inspire Home Loans)"))
story.append(incentive_bullet("Special financing rates available through April closings (May likely to be added)"))

story.append(Spacer(1, 10))
story.append(Paragraph("Available Lots of Note", body_bold))
story.append(thin_line())
story.append(bullet("Lot 34* and Lot 13: Oversized home sites, permitted only (more customization flexibility)"))
story.append(Paragraph("<i>* May be Lot 36 rather than Lot 34; awaiting clarification from the builder.</i>", small_text))
story.append(bullet("All other lots are spec'd, but interior non-structural options can still be changed"))

story.append(Spacer(1, 14))

# Ironwood - Popular Upgrades (continuing on same page to reduce white space)
story.append(Paragraph("Ironwood  |  Popular Upgrade Options", page_title))
story.append(gold_line())

story.append(Paragraph("The following is a selection of available upgrades. Full option catalog available upon request.", small_text))
story.append(Spacer(1, 8))

# Patio
story.append(Paragraph("Covered Patio Options", body_bold))
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
story.append(Paragraph("Fireplace Options", body_bold))
story.append(thin_line())
fp_h = ["Option", "Price"]
fp_r = [
    ['55" Linear Electric Fireplace (includes flat-screen pre-wire)', "$3,850"],
    ['78" Linear Electric Fireplace (includes flat-screen pre-wire)', "$4,600"],
]
story.append(make_table(fp_h, fp_r, [3.5*inch, 1.5*inch]))

story.append(Spacer(1, 8))
story.append(Paragraph("Appliance Packages (LG)", body_bold))
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
story.append(Paragraph("Electrical Upgrades", body_bold))
story.append(thin_line())
el_h = ["Package", "Includes", "Price"]
el_r = [
    ["Upgrade 1", "Ceiling fan pre-wire (all rooms), cable in bedrooms & loft", "$1,310"],
    ["Upgrade 2", "Everything in Upgrade 1 + EV charger pre-wire, puck lights,\nflat screen pre-wire, low volt panel", "$2,680"],
]
story.append(make_table(el_h, el_r, [1.0*inch, 3.3*inch, 0.9*inch]))

story.append(Spacer(1, 8))
story.append(Paragraph("Water Filtration", body_bold))
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
story.append(Paragraph("Design Packages", body_bold))
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


# ── Build ──
doc.build(story)
print(f"PDF created: {OUTPUT_PDF}")
print(f"File size: {os.path.getsize(OUTPUT_PDF):,} bytes")
