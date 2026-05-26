from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

output_dir = "/Users/ryanrose/Downloads/Claude/AI Clients/Nick Nolf Prop. Mgmt"
output_path = os.path.join(output_dir, "TNG-Meeting-Script.pdf")

doc = SimpleDocTemplate(
    output_path,
    pagesize=letter,
    rightMargin=0.7*inch,
    leftMargin=0.7*inch,
    topMargin=0.5*inch,
    bottomMargin=0.5*inch,
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle('Title2', parent=styles['Title'], fontSize=18, spaceAfter=2, textColor=colors.HexColor('#1a1a2e'))
subtitle_style = ParagraphStyle('Subtitle2', parent=styles['Normal'], fontSize=11, spaceAfter=12, textColor=colors.HexColor('#555555'), alignment=TA_CENTER)
section_style = ParagraphStyle('Section', parent=styles['Heading2'], fontSize=13, spaceBefore=16, spaceAfter=4, textColor=colors.HexColor('#1a1a2e'))
time_style = ParagraphStyle('Time', parent=styles['Normal'], fontSize=9, textColor=colors.HexColor('#888888'), spaceAfter=6)
talk_style = ParagraphStyle('Talk', parent=styles['Normal'], fontSize=10, leading=15, textColor=colors.HexColor('#1a1a2e'), leftIndent=12, rightIndent=12, spaceBefore=4, spaceAfter=4, fontName='Helvetica-Oblique', backColor=colors.HexColor('#f5f5f5'), borderPadding=8)
body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor('#333333'), spaceAfter=6, spaceBefore=2)
bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor('#333333'), leftIndent=18, spaceAfter=3, bulletIndent=6)
donot_style = ParagraphStyle('DoNot', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor('#cc3333'), leftIndent=18, spaceAfter=3, bulletIndent=6)
footer_style = ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, textColor=colors.HexColor('#999999'), alignment=TA_CENTER, spaceBefore=20)

elements = []

# Title
elements.append(Paragraph("Meeting Script", title_style))
elements.append(Paragraph("Nick Nolf / TNG Property Management &mdash; April 6, 2026", subtitle_style))
elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#1a1a2e')))
elements.append(Spacer(1, 8))

# ============================================================
# SECTION 1: Opening
# ============================================================
elements.append(Paragraph("1. Opening &mdash; Reconnect, Set the Tone", section_style))
elements.append(Paragraph("~5 minutes. Don't lead with the build. Lead with him.", time_style))

elements.append(Paragraph(
    '"Hey Nick, good to see you again. Before we get into anything, I spent some time after our meeting '
    'going through everything we talked about. I want to make sure I\'ve got your priorities right before we start building."',
    talk_style
))

elements.append(Paragraph("Quick recap to show you listened:", body_style))

elements.append(Paragraph(
    '"Your inbox is the nervous system of the operation. Everything flows through that one email. '
    'The filing, the vendor stuff, the follow-ups &mdash; it all starts there. And right now it\'s you and Matt doing all of it by hand."',
    talk_style
))

elements.append(Paragraph("Let him confirm or correct. This builds trust before you show anything.", body_style))

# ============================================================
# SECTION 2: Free Build
# ============================================================
elements.append(Paragraph("2. The Free Build &mdash; Show, Don't Pitch", section_style))
elements.append(Paragraph("~10 minutes. Walk him through what it does in his language, not code.", time_style))

elements.append(Paragraph(
    '"So I went home and actually built something. I want to show it to you &mdash; this one\'s on me, no charge. '
    'I wanted you to see exactly what this looks like before we talk about anything else."',
    talk_style
))

elements.append(Paragraph("Describe the attachment organizer in his terms:", body_style))

elements.append(Paragraph(
    '"Here\'s what it does. Every email that comes in with an attachment &mdash; invoice from Campbell\'s, '
    'estimate from NWHS, photos from Matt, HOA notice, whatever &mdash; Claude grabs it, figures out which '
    'investor and property it belongs to, renames it your way &mdash; last name, dash, address, dash, tenant, '
    'dash, vendor, dash, date &mdash; and drops it into the right folder in your Drive. Work Completed, HOA, Photos, '
    'wherever it goes."',
    talk_style
))

elements.append(Paragraph("Hit his pain points directly:", body_style))

elements.append(Paragraph(
    '"You told me you\'re OCD about your filing. This follows your convention exactly. And if it can\'t figure out '
    'where something goes, it doesn\'t guess &mdash; it puts it in a staging folder and drafts you a message asking '
    'where it should go. Nothing gets misfiled."',
    talk_style
))

elements.append(Paragraph("Then the line that matters:", body_style))

elements.append(Paragraph(
    '"And it doesn\'t touch your Gmail. No labels, no folders, nothing changes in your inbox. '
    'Your system stays exactly how you have it."',
    talk_style
))

elements.append(Paragraph(
    "Pause. Let him react. He'll probably start asking about specific scenarios. Answer from what you know. "
    "This is where the demo sells itself.",
    body_style
))

# ============================================================
# SECTION 3: Transition
# ============================================================
elements.append(Paragraph("3. Transition to Pricing &mdash; Frame the Partnership", section_style))
elements.append(Paragraph("~5 minutes. Natural bridge from the free build to the business conversation.", time_style))

elements.append(Paragraph(
    '"So that one\'s yours. Free. I wanted you to see the quality of what I build before we talk about money. '
    'Now let me tell you how I work going forward, because I think the right move here is me being your AI '
    'operations guy &mdash; not someone you call when something breaks."',
    talk_style
))

elements.append(Paragraph(
    '"You\'ve got about nine workflows you described to me. The email classifier, the AppFolio follow-ups, '
    'the photo compression, the cross-reference audits, Drive structure enforcement &mdash; all of it. Some are '
    'simple, some are heavy. Here\'s how I\'d structure it."',
    talk_style
))

# ============================================================
# SECTION 4: Pricing
# ============================================================
elements.append(Paragraph("4. The Pricing Conversation &mdash; Simple, Direct", section_style))
elements.append(Paragraph("~10 minutes. Conversational, not a slide deck. Hand him the pricing PDF here.", time_style))

elements.append(Paragraph(
    '"Two parts. There\'s a one-time build fee for each workflow &mdash; that covers me building it, testing it, '
    'getting it live on your system. Then there\'s a monthly retainer that covers me keeping everything running, '
    'tuning it when things change, and being available when you need me."',
    talk_style
))

elements.append(Paragraph("Walk the tiers conversationally:", body_style))

elements.append(Paragraph(
    '"For something straightforward like the one I just gave you, or the vendor work order processor, or Drive '
    'folder enforcement &mdash; that\'s fifteen hundred. Mid-range stuff like the AppFolio follow-up manager or '
    'photo compression &mdash; two to three thousand. The big one, the full email classifier with your 25 templates '
    'and the investor carve-outs &mdash; that\'s three to five. And the long-term knowledge base where Claude learns '
    'all 100,000 of your emails &mdash; that\'s its own conversation, probably five-plus."',
    talk_style
))

elements.append(Paragraph("For the retainer:", body_style))

elements.append(Paragraph(
    '"The monthly retainer starts at one-fifty once we get the first paid workflow live. As we add more, it grows &mdash; '
    'roughly 75 to 100 more per workflow because there\'s more for me to monitor and maintain. By the time we\'ve got '
    'four or five things running, you\'re at four-fifty, maybe five hundred a month. But at that point you\'re saving '
    'fifteen hundred to two thousand a month in labor, so the math is pretty clear."',
    talk_style
))

# ============================================================
# SECTION 5: Close
# ============================================================
elements.append(Paragraph("5. Close the Pricing &mdash; Tie It to His Money", section_style))
elements.append(Paragraph("~2 minutes. Anchor the value.", time_style))

elements.append(Paragraph(
    '"You and Matt are spending four to five hours a day on stuff Claude can handle. At thirty bucks an hour '
    'that\'s around three thousand a month. Even if we only automate sixty percent of it, that\'s eighteen hundred '
    'in savings. The retainer never gets close to that number."',
    talk_style
))

# ============================================================
# SECTION 6: Next Steps
# ============================================================
elements.append(Paragraph("6. Pivot to Next Steps &mdash; Start Building Together", section_style))
elements.append(Paragraph("Rest of meeting. Pull out the placeholder checklist. This becomes collaborative.", time_style))

elements.append(Paragraph(
    '"So here\'s what I need from you today to get the free one live. I need your Gmail address, Matt\'s email, '
    'Campbell\'s email, NWHS email, your Drive folder path, and about ten minutes looking at your folder structure '
    'together so I can see the example. Then we fill in the blanks and run it while we\'re sitting here."',
    talk_style
))

elements.append(Paragraph(
    "Hand him the placeholder checklist PDF. Fill it in together. The rest of the meeting is collaborative building, not selling.",
    body_style
))

# ============================================================
# SECTION 7: Do Not
# ============================================================
elements.append(Spacer(1, 8))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc')))
elements.append(Spacer(1, 4))
elements.append(Paragraph("Things to NOT Do", section_style))

donts = [
    "Don't show him code or file structure. He doesn't care about SKILL.md. He cares about files appearing in Drive with the right names.",
    "Don't apologize for pricing. State it and let the silence sit.",
    "Don't offer discounts. If he pushes back, offer a simpler version of a workflow, not a lower price.",
    "Don't oversell the timeline. If he asks \"can we have everything by end of May?\" be honest &mdash; the email classifier and maybe two others. Not all nine.",
]

for d in donts:
    elements.append(Paragraph(d, donot_style, bulletText='\u2022'))

# Footer
elements.append(Spacer(1, 16))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc')))
elements.append(Paragraph("Prepared for Ryan Rose &mdash; Rose Homes LV &nbsp;|&nbsp; Meeting with Nick Nolf, TNG Property Management", footer_style))

doc.build(elements)
print(f"PDF created: {output_path}")
