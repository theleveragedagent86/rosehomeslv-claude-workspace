#!/usr/bin/env python3
"""Generate a professional fillable PDF Transaction Intake Form for Rose Homes LV."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_LEFT

OUTPUT = "/Users/ryanrose/Downloads/Claude/tc-plugin/skills/transaction-coordination/assets/Transaction-Intake-Form.pdf"

W, H = letter  # 612 x 792
MARGIN_L = 40
MARGIN_R = W - 40
CONTENT_W = MARGIN_R - MARGIN_L

# Colors
DARK_GRAY = HexColor("#3a3a3a")
SECTION_BG = HexColor("#e8e8e8")
FIELD_BORDER = HexColor("#999999")
ACCENT = HexColor("#b71c1c")  # Deep red accent for Rose branding
LABEL_COLOR = HexColor("#444444")


def draw_header(c, y):
    """Draw the branded header."""
    # Top accent bar
    c.setFillColor(ACCENT)
    c.rect(0, y, W, 3, fill=1, stroke=0)
    y -= 30

    # Company name
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(DARK_GRAY)
    c.drawString(MARGIN_L, y, "Rose Homes LV")
    y -= 22

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(DARK_GRAY)
    c.drawString(MARGIN_L, y, "Transaction Intake Form")
    y -= 16

    # Subtitle
    c.setFont("Helvetica", 9)
    c.setFillColor(LABEL_COLOR)
    c.drawString(MARGIN_L, y, "Rose Homes LV  —  Transaction Coordination")
    y -= 6

    # Divider line
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.5)
    c.line(MARGIN_L, y, MARGIN_R, y)
    y -= 8
    return y


def draw_section_header(c, y, title, number):
    """Draw a section header bar."""
    h = 16
    y -= h
    c.setFillColor(SECTION_BG)
    c.roundRect(MARGIN_L, y, CONTENT_W, h, 2, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(DARK_GRAY)
    c.drawString(MARGIN_L + 6, y + 4, f"{number}. {title}")
    y -= 6
    return y


def add_text_field(c, name, x, y, w, h=16, tooltip=""):
    """Add a fillable text field."""
    c.acroForm.textfield(
        name=name,
        tooltip=tooltip or name,
        x=x, y=y, width=w, height=h,
        borderWidth=0.5,
        borderColor=FIELD_BORDER,
        fillColor=white,
        textColor=black,
        fontSize=9,
        fontName="Helvetica",
        fieldFlags="",
    )


def add_checkbox(c, name, x, y, size=12, tooltip=""):
    """Add a fillable checkbox."""
    c.acroForm.checkbox(
        name=name,
        tooltip=tooltip or name,
        x=x, y=y,
        size=size,
        borderWidth=0.5,
        borderColor=FIELD_BORDER,
        fillColor=white,
        buttonStyle="check",
        checked=False,
    )


def add_multiline_field(c, name, x, y, w, h=48, tooltip=""):
    """Add a multi-line text area."""
    c.acroForm.textfield(
        name=name,
        tooltip=tooltip or name,
        x=x, y=y, width=w, height=h,
        borderWidth=0.5,
        borderColor=FIELD_BORDER,
        fillColor=white,
        textColor=black,
        fontSize=9,
        fontName="Helvetica",
        fieldFlags="multiline",
    )


def label(c, text, x, y, bold=False):
    """Draw a label."""
    c.setFont("Helvetica-Bold" if bold else "Helvetica", 8)
    c.setFillColor(LABEL_COLOR)
    c.drawString(x, y, text)


def labeled_field(c, lbl, field_name, x, y, w, field_h=16):
    """Draw a label above a text field. Returns y below the field."""
    label(c, lbl, x, y + field_h + 2)
    add_text_field(c, field_name, x, y, w, field_h)
    return y - 4


def labeled_row(c, fields, y, field_h=16):
    """Draw a row of labeled fields. fields = [(label, name, width), ...]
    Returns y below the row."""
    x = MARGIN_L
    gap = 8
    for lbl_text, name, w in fields:
        labeled_field(c, lbl_text, name, x, y, w, field_h)
        x += w + gap
    return y - field_h - 6


def build_pdf():
    c = canvas.Canvas(OUTPUT, pagesize=letter)
    c.setTitle("Transaction Intake Form — Rose Homes LV")
    c.setAuthor("Rose Homes LV")

    # ── PAGE 1 ──
    y = H - 20
    y = draw_header(c, y)

    # ── Section 1: Transaction Type ──
    y = draw_section_header(c, y, "TRANSACTION TYPE", "1")
    y -= 2
    cb_labels = ["Buyer — Resale", "Buyer — New Construction", "Seller"]
    cb_names = ["tx_buyer_resale", "tx_buyer_newcon", "tx_seller"]
    x = MARGIN_L + 6
    for i, (cb_lbl, cb_name) in enumerate(zip(cb_labels, cb_names)):
        add_checkbox(c, cb_name, x, y - 12, 12, cb_lbl)
        label(c, cb_lbl, x + 16, y - 10)
        x += 170
    y -= 26

    # ── Section 2: Property Information ──
    y = draw_section_header(c, y, "PROPERTY INFORMATION", "2")

    # Property Address — full line
    y = labeled_row(c, [("Property Address", "property_address", CONTENT_W)], y)

    # City, State, Zip
    y = labeled_row(c, [
        ("City", "city", 250),
        ("State", "state", 80),
        ("Zip", "zip", 100),
    ], y)

    # APN | Purchase Price
    y = labeled_row(c, [
        ("APN", "apn", 180),
        ("Purchase Price", "purchase_price", 150),
    ], y)

    # Loan Amount | Loan Type
    y = labeled_row(c, [
        ("Loan Amount", "loan_amount", 150),
        ("Loan Type (e.g., Conv 30 Yr, FHA, VA, Cash)", "loan_type", 280),
    ], y)

    # ── Section 3: Key Dates ──
    y = draw_section_header(c, y, "KEY DATES", "3")
    y = labeled_row(c, [
        ("Contract / Acceptance Date", "acceptance_date", 200),
        ("COE Date", "coe_date", 200),
    ], y)

    # ── Section 4: Contract Deadlines ──
    y = draw_section_header(c, y, "CONTRACT DEADLINES (days from acceptance unless noted)", "4")

    # Row 1: EM days + EMD amount
    y = labeled_row(c, [
        ("Earnest Money (business days)", "em_days", 180),
        ("EMD Amount ($)", "emd_amount", 150),
    ], y)

    # Row 2: Seller Disclosure | Due Diligence / Inspection
    y = labeled_row(c, [
        ("Seller Disclosure (cal days)", "seller_disclosure_days", 180),
        ("Due Diligence / Inspection (cal days)", "inspection_days", 210),
    ], y)

    # Row 3: Appraisal | Loan Contingency
    y = labeled_row(c, [
        ("Appraisal Contingency (cal days)", "appraisal_days", 190),
        ("Loan Contingency (cal days)", "loan_contingency_days", 190),
    ], y)

    # Row 4: HOA Review
    y = labeled_row(c, [
        ("HOA Review (cal days after receipt of CIC resale pkg)", "hoa_review_days", 300),
    ], y)

    # ── Section 5: Buyer Information ──
    y = draw_section_header(c, y, "BUYER INFORMATION", "5")
    y = labeled_row(c, [("Buyer Name(s)", "buyer_names", CONTENT_W)], y)
    y = labeled_row(c, [
        ("Buyer Email 1", "buyer_email_1", 255),
        ("Buyer Email 2", "buyer_email_2", 255),
    ], y)
    y = labeled_row(c, [
        ("Buyer Phone 1", "buyer_phone_1", 255),
        ("Buyer Phone 2", "buyer_phone_2", 255),
    ], y)

    # ── Section 6: Seller Information ──
    y = draw_section_header(c, y, "SELLER INFORMATION", "6")
    y = labeled_row(c, [("Seller Name(s)", "seller_names", CONTENT_W)], y)

    # ── Section 7: Escrow Information ──
    y = draw_section_header(c, y, "ESCROW INFORMATION", "7")
    y = labeled_row(c, [
        ("Escrow Company", "escrow_company", 255),
        ("Escrow Officer Name", "escrow_officer_name", 255),
    ], y)
    y = labeled_row(c, [
        ("Escrow Officer Email", "escrow_officer_email", 255),
        ("Escrow Team Email", "escrow_team_email", 255),
    ], y)
    y = labeled_row(c, [("Escrow Office Address", "escrow_office_address", CONTENT_W)], y)

    # ── PAGE 2 ──
    c.showPage()
    y = H - 30

    # Mini header on page 2
    c.setFillColor(ACCENT)
    c.rect(0, H - 3, W, 3, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(DARK_GRAY)
    c.drawString(MARGIN_L, y, "Transaction Intake Form — Rose Homes LV")
    c.setFont("Helvetica", 8)
    c.setFillColor(LABEL_COLOR)
    c.drawString(MARGIN_R - 40, y, "Page 2")
    y -= 6
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1)
    c.line(MARGIN_L, y, MARGIN_R, y)
    y -= 10

    # ── Section 8: Lender Information ──
    y = draw_section_header(c, y, "LENDER INFORMATION", "8")
    y = labeled_row(c, [
        ("Lender Name", "lender_name", 255),
        ("Lender Company", "lender_company", 255),
    ], y)
    y = labeled_row(c, [
        ("Lender Email", "lender_email", 255),
        ("Lender Phone", "lender_phone", 255),
    ], y)

    # ── Section 9: Listing Agent ──
    y = draw_section_header(c, y, "LISTING AGENT (Buyer — Resale transactions)", "9")
    y = labeled_row(c, [
        ("Listing Agent Name", "listing_agent_name", 255),
        ("Listing Agent Company", "listing_agent_company", 255),
    ], y)
    y = labeled_row(c, [
        ("Listing Agent Email", "listing_agent_email", 255),
        ("Listing Agent Phone", "listing_agent_phone", 255),
    ], y)
    y = labeled_row(c, [
        ("Listing Agent TC Name", "listing_agent_tc_name", 255),
        ("Listing Agent TC Email", "listing_agent_tc_email", 255),
    ], y)

    # ── Section 10: Builder Info ──
    y = draw_section_header(c, y, "BUILDER INFO (Buyer — New Construction transactions)", "10")
    y = labeled_row(c, [
        ("Builder Name", "builder_name", 170),
        ("Builder Rep Name", "builder_rep_name", 170),
        ("Builder Rep Email", "builder_rep_email", 170),
    ], y)

    # ── Section 11: Buyer Agent ──
    y = draw_section_header(c, y, "BUYER AGENT (Seller transactions)", "11")
    y = labeled_row(c, [
        ("Buyer Agent Name", "buyer_agent_name", 255),
        ("Buyer Agent Email", "buyer_agent_email", 255),
    ], y)

    # ── Section 12: Additional Terms ──
    y = draw_section_header(c, y, "ADDITIONAL TERMS", "12")

    # Leaseback row with checkboxes + fields
    y -= 2
    label(c, "Leaseback?", MARGIN_L + 6, y)
    add_checkbox(c, "leaseback_yes", MARGIN_L + 60, y - 3, 12, "Leaseback Yes")
    label(c, "Yes", MARGIN_L + 76, y)
    add_checkbox(c, "leaseback_no", MARGIN_L + 100, y - 3, 12, "Leaseback No")
    label(c, "No", MARGIN_L + 116, y)

    label(c, "Leaseback Days", MARGIN_L + 160, y)
    add_text_field(c, "leaseback_days", MARGIN_L + 235, y - 4, 60, 16)

    label(c, "Leaseback Security Deposit ($)", MARGIN_L + 310, y)
    add_text_field(c, "leaseback_deposit", MARGIN_L + 450, y - 4, 82, 16)

    y -= 28

    # Personal Property Included
    label(c, "Personal Property Included", MARGIN_L, y + 2)
    y -= 50
    add_multiline_field(c, "personal_property", MARGIN_L, y, CONTENT_W, 48)
    y -= 8

    # Special Terms / Notes
    label(c, "Special Terms / Notes", MARGIN_L, y + 2)
    y -= 50
    add_multiline_field(c, "special_terms", MARGIN_L, y, CONTENT_W, 48)
    y -= 14

    # Footer
    c.setStrokeColor(HexColor("#cccccc"))
    c.setLineWidth(0.5)
    c.line(MARGIN_L, y, MARGIN_R, y)
    y -= 12
    c.setFont("Helvetica", 7)
    c.setFillColor(LABEL_COLOR)
    c.drawString(MARGIN_L, y, "Rose Homes LV  |  Transaction Coordination  |  Confidential")
    c.drawRightString(MARGIN_R, y, "Generated form — all fields are fillable")

    c.save()
    print(f"PDF saved to: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
