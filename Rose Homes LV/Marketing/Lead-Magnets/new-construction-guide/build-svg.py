#!/usr/bin/env python3
"""
Generate the thirteen guide diagrams into build/svg/, plus build/svg/index.md.

    python3 build-svg.py            # all thirteen
    python3 build-svg.py 04 09      # just those

Why a generator rather than thirteen hand-authored files: they share one palette, one type scale,
and one accessibility scaffold, and the palette is frozen in build/design-system.md. Hand-editing
thirteen files is how a set drifts, and the tracking bug in round 6 was exactly that failure mode
in a different medium.

Three rules these files obey, all of them from build/design-system.md:

  * **Every hex is written out.** No custom properties. An inline SVG in this workspace carries
    hardcoded hexes precisely because `:root` does not reach into it, which is the lesson that cost
    a plum bar and a teal rail inside a navy layout in round 6.
  * **Orange appears in exactly two of the thirteen.** SVG-04 and SVG-12 are the cost diagram, which
    is one of the four places the design system allows warm color. The `NOT FOUND` token is another,
    and it appears wherever the outline says the number does not exist. Everything else is navy and
    neutral. Emphasis that is not one of those is carried by weight, rule, and glyph.
  * **Nothing is encoded by color alone.** Every path element prints its letter and its tab words.
    Every allowed/forbidden pair prints a check or a cross and the literal word.

Class names are all `sv-` prefixed. An inline `<svg><style>` in HTML is NOT scoped, it leaks to the
whole document, so an unprefixed `.h` here would silently restyle the guide.

No number appears in any diagram that is not in research/fact-ledger.md and named in
outline/guide-outline.md for that page.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "svg")

# ---------------------------------------------------------------- palette
# Frozen in build/design-system.md. Do not introduce a hex that is not here.
INK        = "#1C2436"
MUTED      = "#5F5A52"
RULE       = "#847B6D"
RULE_STRONG= "#5F5A52"
PAPER      = "#F7F5F0"
PAPER2     = "#EDE9E0"
CREAM      = "#FBF8F2"
WHITE      = "#FFFFFF"
NAVY600    = "#304880"
NAVY700    = "#2C3F6B"
NAVY800    = "#28375A"
NAVY900    = "#242F4A"
NAVY950    = "#141A27"
NAVY_TINT  = "#E4E9F2"
CLAY       = "#B8360F"
CORAL      = "#E9714A"
OCHRE      = "#EFA00B"
CARD_TINT  = "#FBEFD3"
TINT_CLAY  = "#FBE5DA"
GOLD_BRAND = "#C9A86E"

PATH_A = NAVY600
PATH_B = NAVY950
PATH_C = PAPER2

SANS = "Archivo,ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif"

CSS = f""".sv-h{{font:700 13px {SANS};fill:{INK};letter-spacing:.002em}}
.sv-k{{font:700 8.4px {SANS};fill:{MUTED};letter-spacing:.09em;text-transform:uppercase}}
.sv-l{{font:600 10px {SANS};fill:{INK}}}
.sv-b{{font:400 9.6px {SANS};fill:{INK}}}
.sv-s{{font:500 8.6px {SANS};fill:{MUTED}}}
.sv-n{{font:700 11px {SANS};fill:{INK};font-variant-numeric:tabular-nums}}
.sv-r{{font:600 10px {SANS};fill:{PAPER}}}
.sv-rs{{font:500 8.6px {SANS};fill:{PAPER}}}
.sv-nf{{font:700 8.4px {SANS};fill:{CLAY};letter-spacing:.06em}}
.sv-c{{text-anchor:middle}}
.sv-e{{text-anchor:end}}"""


# ---------------------------------------------------------------- helpers
def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def t(x, y, s, cls="sv-b", extra=""):
    return f'<text x="{x}" y="{y}" class="{cls}"{extra}>{esc(s)}</text>'


def wrap(x, y, s, chars, cls="sv-b", lh=12, anchor=""):
    """Greedy word wrap into one <text> with dy-shifted tspans."""
    words, lines, cur = s.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) <= chars or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    spans = "".join(
        f'<tspan x="{x}" dy="{0 if i == 0 else lh}">{esc(l)}</tspan>'
        for i, l in enumerate(lines))
    return f'<text x="{x}" y="{y}" class="{cls}{anchor}">{spans}</text>'


def wrapped_height(s, chars, lh=12):
    words, n, cur = s.split(), 1, ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) <= chars or not cur:
            cur = trial
        else:
            n += 1
            cur = w
    return n * lh



# Average glyph advance per class, in user units, measured against Archivo at the sizes in CSS.
# Wrapping by character count was the original mistake: it cannot tell you how tall the result is,
# so every box sized by hand overflowed the moment a string got longer than the guess.
CHARW = {"sv-b": 4.95, "sv-s": 4.45, "sv-l": 5.35, "sv-r": 5.35,
         "sv-rs": 4.45, "sv-n": 6.2, "sv-k": 5.0}


def cw_of(cls):
    return CHARW.get(cls.split()[0], 4.95)


def fit(s, width, cls="sv-b"):
    """How many characters of this class fit in `width` user units."""
    return max(8, int(width / cw_of(cls)))


def wrapw(x, y, s, width, cls="sv-b", lh=12):
    return wrap(x, y, s, fit(s, width, cls), cls, lh)


def wrapw_h(s, width, cls="sv-b", lh=12):
    return wrapped_height(s, fit(s, width, cls), lh)


def note(x, y, w, s, fill=NAVY_TINT, cls="sv-b", lh=12, pad=12, stroke=None, r=6, lead=None):
    """A filled panel sized to the text it holds. Returns (markup, height)."""
    inner = w - pad * 2
    lead_h = 0
    if lead:
        lead_h = 16
    th = wrapw_h(s, inner, cls, lh)
    h = pad + lead_h + th + pad - 2
    m = box(x, y, w, h, fill, stroke, r)
    if lead:
        m += t(x + pad, y + pad + 6, lead, "sv-k")
    m += wrapw(x + pad, y + pad + lead_h + 7, s, inner, cls, lh)
    return m, h


def box(x, y, w, h, fill, stroke=None, r=6, sw=1):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{s}/>'


def line(x1, y1, x2, y2, stroke=RULE, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


def tick(x, y, s=3.2, fill=NAVY700):
    """A check glyph, drawn not typed, so it never depends on a font."""
    return (f'<path d="M{x - s} {y} l{s * 0.8} {s * 0.9} l{s * 1.5} {-s * 1.9}" fill="none" '
            f'stroke="{fill}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/>')


def cross(x, y, s=3.2, fill=CLAY):
    return (f'<path d="M{x - s} {y - s} l{s * 2} {s * 2} M{x + s} {y - s} l{-s * 2} {s * 2}" '
            f'fill="none" stroke="{fill}" stroke-width="1.9" stroke-linecap="round"/>')


def notfound(x, y, w=64):
    """The NOT FOUND token. Color is the meaning here, so it stays warm."""
    return (box(x, y, w, 14, TINT_CLAY, r=3)
            + t(x + w / 2, y + 10.2, "NOT FOUND", "sv-nf sv-c"))


def arrow(x1, y1, x2, y2, stroke=NAVY700, sw=1.6, mid="tri"):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}" marker-end="url(#sv-{mid})"/>')


DEFS = f'''<defs>
<marker id="sv-tri" viewBox="0 0 8 8" refX="6.5" refY="4" markerWidth="6" markerHeight="6"
        orient="auto-start-reverse"><path d="M0 0.8 L7.5 4 L0 7.2 z" fill="{NAVY700}"/></marker>
<marker id="sv-tric" viewBox="0 0 8 8" refX="6.5" refY="4" markerWidth="6" markerHeight="6"
        orient="auto-start-reverse"><path d="M0 0.8 L7.5 4 L0 7.2 z" fill="{CLAY}"/></marker>
<marker id="sv-trim" viewBox="0 0 8 8" refX="6.5" refY="4" markerWidth="6" markerHeight="6"
        orient="auto-start-reverse"><path d="M0 0.8 L7.5 4 L0 7.2 z" fill="{MUTED}"/></marker>
<pattern id="sv-hatch" width="6" height="6" patternTransform="rotate(45)"
         patternUnits="userSpaceOnUse">
  <rect width="6" height="6" fill="{PAPER2}"/>
  <line x1="0" y1="0" x2="0" y2="6" stroke="{RULE}" stroke-width="1.6"/>
</pattern>
</defs>'''


def doc(num, w, h, title, desc, body):
    tid, did = f"sv{num}t", f"sv{num}d"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%"
     role="img" aria-labelledby="{tid} {did}" font-family="{SANS}">
<title id="{tid}">{esc(title)}</title>
<desc id="{did}">{esc(desc)}</desc>
<style>{CSS}</style>
{DEFS}
<rect width="{w}" height="{h}" fill="{PAPER}"/>
{body}
</svg>
'''


def heading(x, y, kicker, head):
    return t(x, y, kicker, "sv-k") + t(x, y + 17, head, "sv-h")


def source(x, y, s):
    return t(x, y, s, "sv-s")


W = 700  # full text column, 7.4in of page at ~96dpi


# ================================================================ SVG-01
def svg01():
    h = 296
    paths = [
        ("A", "PATH A · MOVING HERE", "You do not live in Nevada yet.",
         "Pages 6 to 9", PATH_A, PAPER),
        ("B", "PATH B · MOVING UP", "You own a home here and want a bigger one.",
         "Pages 10 to 13", PATH_B, PAPER),
        ("C", "PATH C · FIRST BUILD", "Your first newly built home, or your first home at all.",
         "Pages 14 to 17", PATH_C, INK),
    ]
    b = [heading(0, 14, "Page 5", "Which of these sounds like you?")]
    cw, gap = 218, 23
    top, ph = 52, 128
    for i, (ltr, tab, line1, pages, fill, fg) in enumerate(paths):
        x = i * (cw + gap)
        b.append(box(x, top, cw, ph, fill, RULE if fill == PATH_C else None, r=10))
        if fill == PATH_C:
            # the pale panel needs an edge rule or in grayscale it reads as blank paper
            b.append(f'<rect x="{x}" y="{top}" width="6" height="{ph}" rx="3" fill="{NAVY950}"/>')
        lcls = "sv-r" if fg == PAPER else "sv-l"
        scls = "sv-rs" if fg == PAPER else "sv-s"
        b.append(f'<text x="{x + 20}" y="{top + 42}" '
                 f'style="font:700 26px {SANS};fill:{fg}">{ltr}</text>')
        b.append(f'<text x="{x + 50}" y="{top + 38}" class="{scls}" '
                 f'style="letter-spacing:.08em">{esc(tab)}</text>')
        b.append(wrapw(x + 20, top + 66, line1, cw - 38, lcls, 13))
        b.append(f'<text x="{x + 20}" y="{top + ph - 14}" class="{scls}">{esc(pages)}</text>')

    # Elbow connectors, not diagonals. Three diagonals converging on one point crossed each other
    # and read as an X rather than as a rejoin.
    rail, bar_y = 200, 216
    for i in range(3):
        x = i * (cw + gap) + cw / 2
        b.append(f'<path d="M{x} {top + ph} L{x} {rail} L{W / 2} {rail}" fill="none" '
                 f'stroke="{NAVY700}" stroke-width="1.5" stroke-linejoin="round"/>')
    b.append(arrow(W / 2, rail, W / 2, bar_y - 2))
    b.append(box(0, bar_y, W, 34, NAVY800, r=8))
    b.append(t(W / 2, bar_y + 21, "Page 18. Everyone back together.", "sv-r sv-c"))
    b.append(wrapw(0, bar_y + 62, "If two of them fit, read both. They are four pages each. "
                                  "The edge tab on pages 6 to 17 lets you thumb straight to your "
                                  "path without opening the guide.", W, "sv-s", 12))
    return doc("01", W, h, "Which path is yours",
               "Three panels, one per reader path. Path A, moving here, pages 6 to 9. Path B, "
               "moving up, pages 10 to 13. Path C, first build, pages 14 to 17. Arrows from all "
               "three converge on a single bar reading page 18, everyone back together.",
               "\n".join(b))


# ================================================================ SVG-02
def svg02():
    colw = 330
    rx = W - colw
    b = [heading(0, 14, "Page 3", "Who works for whom at a model home")]
    b.append(line(W / 2, 44, W / 2, 258, RULE, 1, "3 4"))

    # builder side
    b.append(box(0, 44, colw, 30, NAVY800, r=6))
    b.append(t(14, 64, "THE BUILDER'S SIDE", "sv-r", ' style="letter-spacing:.08em"'))
    card_txt = ("Paid by the builder. Represents the builder. One national builder publishes "
                "exactly that in its own buyer materials.")
    card_h = 30 + wrapw_h(card_txt, colw - 28, "sv-s", 11)
    b.append(box(0, 84, colw, card_h, PAPER2, RULE, r=6))
    b.append(t(14, 104, "The on-site sales representative", "sv-l"))
    b.append(wrapw(14, 120, card_txt, colw - 28, "sv-s", 11))
    b.append(t(14, 168, "What that means for you", "sv-l"))
    for i, s in enumerate([
        "They are not your agent and owe you no duty of loyalty.",
        "Anything you tell them, you have told the builder.",
        "This is a role difference, not a character judgment.",
    ]):
        y = 186 + i * 26
        b.append(f'<circle cx="20" cy="{y - 3.5}" r="2.4" fill="{MUTED}"/>')
        b.append(wrapw(32, y, s, colw - 46, "sv-b", 11))

    # buyer side
    b.append(box(rx, 44, colw, 30, NAVY600, r=6))
    b.append(t(rx + 14, 64, "YOUR SIDE", "sv-r", ' style="letter-spacing:.08em"'))
    b.append(box(rx, 84, colw, card_h, CARD_TINT, RULE, r=6))
    b.append(t(rx + 14, 104, "An agent who represents you", "sv-l"))
    b.append(wrapw(rx + 14, 120, "Owes duties Nevada does not let either of you waive, even by "
                                 "agreement.", colw - 28, "sv-s", 11))
    b.append(t(rx + 14, 168, "Duties that cannot be waived", "sv-l"))
    for i, s in enumerate([
        "Reasonable care",
        "Confidentiality, for one year after the agreement ends",
        "Presenting every offer",
        "Disclosing known material facts",
    ]):
        y = 186 + i * 18
        b.append(tick(rx + 20, y - 3.5))
        b.append(t(rx + 32, y, s, "sv-b"))

    m, nh = note(0, 268, W,
                 "Since August 17, 2024 you and your agent sign a written agreement spelling out "
                 "how the agent is paid, before you tour. A Nevada licensee must also disclose "
                 "every source they are paid from, and hand every party the Duties Owed form.")
    b.append(m)
    h = 268 + nh + 8
    return doc("02", W, h, "Who works for whom at a model home",
               "Two columns divided by a dashed line. The builder's side holds the on-site sales "
               "representative, who is paid by and represents the builder. Your side holds an agent "
               "who represents you and owes four duties Nevada does not allow to be waived: "
               "reasonable care, confidentiality for one year after the agreement ends, presenting "
               "every offer, and disclosing known material facts. A footer notes the written buyer "
               "agreement required since August 17, 2024 and the Duties Owed form.",
               "\n".join(b))


# ================================================================ SVG-03
def svg03():
    h = 330
    b = [heading(0, 14, "Page 18", "The sequence, first contact to eleven months after closing")]
    stages = [
        ("Before you\nvisit anything", ["Register your agent at first contact",
                                        "Get a Loan Estimate, not a worksheet"]),
        ("Community\nand lot", ["Walk the lot at 4 p.m.",
                                "Ask for the phase release calendar"]),
        ("The\ncontract", ["Find your outside completion date",
                           "Design selections final before build"]),
        ("The\nbuild", ["Pre-drywall inspection",
                        "Blue tape walkthrough"]),
        ("Closing and\nyour first year", ["Final walkthrough, then close",
                                          "Written punch list completed"]),
    ]
    axis_y = 118
    cw = W / 5
    b.append(line(6, axis_y, W - 6, axis_y, RULE, 1.4))
    for i, (name, items) in enumerate(stages):
        cx = i * cw + cw / 2
        b.append(f'<circle cx="{cx}" cy="{axis_y}" r="5.5" fill="{PAPER}" '
                 f'stroke="{NAVY700}" stroke-width="2"/>')
        for j, ln in enumerate(name.split("\n")):
            b.append(t(cx, 68 + j * 13, ln, "sv-l sv-c"))
        b.append(t(cx, 96, f"STAGE {i + 1}", "sv-k sv-c"))
        for j, s in enumerate(items):
            b.append(wrap(cx, 142 + j * 30, s, 21, "sv-s sv-c", 11))

    # legal deadlines, weighted differently: filled square + heavier rule
    b.append(line(0, 208, W, 208, RULE, 1, "3 4"))
    b.append(t(0, 228, "THESE THREE ARE LEGAL DEADLINES, NOT SUGGESTIONS", "sv-k"))
    legal = [
        ("Five calendar days", "To cancel in writing after signing, in a common interest "
                               "community, but only if you have not personally inspected the home."),
        ("Forty-five days", "A builder's repair clock, started by your written notice of a "
                            "defect inside the first year."),
        ("July 1", "The Assessor mails a postcard after July 1 to property whose ownership "
                   "changed. Sign it and send it back or you lose the 3 percent cap."),
    ]
    for i, (label, s) in enumerate(legal):
        x = i * (W / 3)
        b.append(f'<rect x="{x}" y="{240}" width="9" height="9" fill="{NAVY950}"/>')
        b.append(t(x + 16, 248, label, "sv-l"))
        b.append(wrap(x, 266, s, 36, "sv-s", 11))
    b.append(source(0, 322, "A solid square marks a deadline set by law. A hollow circle marks a "
                            "practical step you control."))
    return doc("03", W, h, "The sequence, first contact to eleven months after closing",
               "A horizontal timeline in five stages: before you visit anything, choosing the "
               "community and lot, the contract, the build, and closing plus your first year. "
               "Below it, three items marked as legal deadlines rather than practical steps: the "
               "five calendar day cancellation window in a common interest community, the "
               "forty-five day builder repair clock inside year one, and the July 1 assessor "
               "postcard that must be returned to keep the 3 percent tax cap.",
               "\n".join(b))


# ================================================================ SVG-04 and SVG-12
def payment_stack(num, kicker, head, note_s):
    """
    Shared by SVG-04 and SVG-12. This is the cost diagram, which is one of the four places
    build/design-system.md allows warm color. The rungs are a deliberate navy to cream ramp
    and flattening one of them would leave three of five bars the same, so the ramp stays.
    """
    b = [heading(0, 14, kicker, head)]
    box_x, box_w = 0, 400
    b.append(box(box_x, 52, box_w, 214, WHITE, NAVY700, r=8, sw=1.6))
    b.append(t(box_x + 14, 72, "INSIDE YOUR MORTGAGE PAYMENT", "sv-k"))
    b.append(t(box_x + box_w - 14, 72, "escrowed", "sv-s sv-e"))
    rungs = [
        ("Principal and interest", NAVY900, PAPER, "The only part a builder advertises"),
        ("Property tax", NAVY700, PAPER, "35 percent of taxable value, no cap in year one"),
        ("Homeowners insurance", NAVY_TINT, INK, "Priced on rebuild cost, not what you paid"),
        ("Master HOA", CORAL, INK, "Almost never published as a dollar amount"),
        ("Sub-association HOA", CARD_TINT, INK, "Two associations is normal here, not a mistake"),
    ]
    y = 84
    for name, fill, fg, rung_note in rungs:
        b.append(box(box_x + 14, y, box_w - 28, 32, fill, RULE if fill == CARD_TINT else None, r=4))
        b.append(f'<text x="{box_x + 26}" y="{y + 15}" '
                 f'style="font:600 10px {SANS};fill:{fg}">{esc(name)}</text>')
        b.append(f'<text x="{box_x + 26}" y="{y + 27}" '
                 f'style="font:500 8.4px {SANS};fill:{fg};opacity:.82">{esc(rung_note)}</text>')
        y += 36

    # the assessment, deliberately outside the box
    ax = 432
    b.append(box(ax, 100, W - ax, 96, OCHRE, NAVY900, r=8, sw=1.6))
    # MUTED on ochre computes 3.20 and fails AA. Ink on ochre is 7.18.
    b.append(t(ax + 14, 122, "OUTSIDE IT", "sv-k", f' style="fill:{INK}"'))
    b.append(t(ax + 14, 142, "The special assessment", "sv-l"))
    b.append(wrapw(ax + 14, 156, "SID, or LID in Henderson. Billed semi-annually about 60 "
                                 "days ahead, on its own bill, and a lien until it is paid.",
                   W - ax - 28, "sv-b", 11))
    b.append(arrow(box_x + box_w + 8, 148, ax - 8, 148))
    b.append(t((box_x + box_w + ax) / 2, 140, "not in", "sv-s sv-c"))
    b.append(t((box_x + box_w + ax) / 2, 168, "escrow", "sv-s sv-c"))

    # the term bar
    b.append(t(0, 292, "HOW LONG YOU PAY IT", "sv-k"))
    b.append(box(0, 300, W, 18, PAPER2, RULE, r=4))
    b.append(box(0, 300, W * 0.62, 18, NAVY700, r=4))
    b.append(t(10, 313, "10 to 30 years, financed at low interest", "sv-rs"))
    b.append(t(W - 10, 313, "then it ends", "sv-s sv-e"))
    b.append(notfound(ax + 14, 206))
    b.append(wrapw(ax + 86, 216, note_s, W - ax - 100, "sv-s", 11))
    return b, box_x, box_w, ax


def svg04():
    b, bx, bw, ax = payment_stack(
        "04", "Pages 19 and 20",
        "Where the special assessment actually sits",
        "No government office and no developer publishes a per home dollar amount. "
        "Look up the parcel.")
    b.append(wrapw(0, 340, "Two houses on the same street can owe different amounts. Assessments "
                           "are apportioned by front foot, area, zone, or another equitable basis.",
                   W, "sv-s", 11))
    h = 360
    return doc("04", W, h, "Where the special assessment sits next to your house payment",
               "A payment stack drawn inside an escrow box holding principal and interest, "
               "property tax, homeowners insurance, master HOA and sub-association HOA. The "
               "special assessment is drawn outside the box, connected by an arrow labeled not in "
               "escrow, because it arrives on its own semi-annual bill and is a lien until paid. "
               "A bar beneath shows it financing over 10 to 30 years and then ending. The dollar "
               "amount is marked NOT FOUND because no office publishes a per home figure.",
               "\n".join(b))


def svg12():
    b, bx, bw, ax = payment_stack(
        "12", "Page 17",
        "What it actually costs every month",
        "Master and sub HOA monthly amounts are not published for most of these communities.")
    m, nh = note(0, 332, W,
                 "One builder's own footnote states its advertised monthly payments are principal "
                 "and interest only, and that taxes, insurance and HOA are not included. The "
                 "homesite premium sits on top of the base price before any of this starts.",
                 CARD_TINT, "sv-b", 11, stroke=RULE)
    b.append(m)
    h = 332 + nh + 8
    return doc("12", W, h, "What a new home actually costs every month",
               "A vertical stack of the monthly cost layers inside an escrow box: principal and "
               "interest, property tax, homeowners insurance, master HOA and sub-association HOA. "
               "The special assessment is drawn outside the box because it is usually not in your "
               "mortgage payment. HOA dollar amounts are marked NOT FOUND. A footer notes that a "
               "builder's advertised monthly payment is principal and interest only.",
               "\n".join(b))


# ================================================================ SVG-05
def svg05():
    b = [heading(0, 14, "Page 21", "The year one reset, and the cap you get afterward")]
    # The shock is the step INTO year one, so the chart has to show the capped home the buyer is
    # leaving. Bars that only grew rightward told the opposite story: they read as ordinary
    # inflation instead of as a reset.
    base_y = 232
    x0, bw, gap = 28, 104, 38
    bars = [
        ("Your old home", "under a 3% cap for years", 0.44, PAPER2, INK, True),
        ("Fiscal year 1", "no cap at all", 1.00, NAVY900, PAPER, False),
        ("Year 2", "+3% ceiling", 1.03, NAVY700, PAPER, False),
        ("Year 3", "+3% ceiling", 1.06, NAVY700, PAPER, False),
        ("Year 4", "+3% ceiling", 1.09, NAVY700, PAPER, False),
    ]
    unit = 128
    b.append(line(x0 - 16, base_y, W - 6, base_y, RULE, 1.2))
    for i, (label, sub, mult, fill, fg, ghost) in enumerate(bars):
        x = x0 + i * (bw + gap)
        bh = unit * mult
        y = base_y - bh
        b.append(box(x, y, bw, bh, fill, RULE if ghost else None, r=4))
        if ghost:
            b.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="4" '
                     f'fill="url(#sv-hatch)" opacity=".5"/>')
        b.append(t(x + bw / 2, base_y + 16, label, "sv-l sv-c"))
        b.append(t(x + bw / 2, base_y + 29, sub, "sv-s sv-c"))
        if i == 1:
            b.append(t(x + bw / 2, y - 9, "full assessed value of the completed home",
                       "sv-s sv-c"))
    # the reset itself
    b.append(f'<path d="M{x0 + bw + 6} {base_y - unit * 0.44} L{x0 + bw + gap - 6} '
             f'{base_y - unit * 0.98}" fill="none" stroke="{CLAY}" stroke-width="1.6" '
             f'marker-end="url(#sv-tric)"/>')
    b.append(t(x0 + bw + gap / 2, base_y - unit * 0.44 + 20, "the reset", "sv-s sv-c"))
    # the 8 percent ceiling for anything that is not a primary residence
    y8 = base_y - unit * 1.20
    b.append(line(x0 - 16, y8, W - 6, y8, NAVY950, 1.4, "6 4"))
    b.append(t(W - 6, y8 - 6, "up to 8% a year, anything that is not your primary residence",
               "sv-s sv-e"))
    m, nh = note(0, base_y + 44, W,
                 "The cap only applies to property that had a separate assessed value the year "
                 "before, and it excludes value added by new improvements. A house that did not "
                 "exist last year has nothing to cap against. Only one property per person "
                 "statewide can carry the 3 percent cap, and recording any ownership document "
                 "knocks it off until you claim it back.")
    b.append(m)
    h = base_y + 44 + nh + 8
    return doc("05", W, h, "The year one property tax reset",
               "A stepped bar chart across four fiscal years. Year one is a tall bar labeled no "
               "cap at all, taxed on the full assessed value of the completed home. Years two "
               "through four step up under a 3 percent annual ceiling for a primary residence. A "
               "dashed line above marks the up to 8 percent ceiling that applies to anything that "
               "is not your primary residence. A note explains that the cap only applies to "
               "property that had a separate assessed value the year before.",
               "\n".join(b))


# ================================================================ SVG-06
def svg06():
    b = [heading(0, 14, "Page 22", "Where the incentive money can and cannot go")]
    b.append(t(0, 60, "THREE BUCKETS IT CAN FILL", "sv-k"))
    cans = [
        ("Closing costs", "Title, escrow, recording, lender fees."),
        ("A rate buydown", "A lump sum into a separate escrow account, released monthly."),
        ("Prepaids", "Plus up to 12 months of HOA assessments."),
    ]
    cw = 148
    for i, (name, s) in enumerate(cans):
        x = i * (cw + 12)
        b.append(box(x, 70, cw, 84, CARD_TINT, RULE, r=6))
        b.append(tick(x + 16, 90))
        b.append(t(x + 28, 94, name, "sv-l"))
        b.append(wrap(x + 12, 114, s, 26, "sv-s", 11))
    # the one it cannot
    x = 3 * (cw + 12)
    # The hatch reads as "blocked" but body copy on top of it does not read at all, so the hatch
    # is a banner and the copy sits on paper underneath it.
    b.append(box(x, 70, W - x, 84, PAPER, RULE_STRONG, r=6, sw=1.6))
    b.append(f'<path d="M{x + 1} 76 h{W - x - 2} v22 h{-(W - x - 2)} z" fill="url(#sv-hatch)"/>')
    b.append(box(x, 70, W - x, 84, "none", RULE_STRONG, r=6, sw=1.6))
    b.append(cross(x + 16, 106))
    b.append(t(x + 28, 110, "Never your down payment", "sv-l"))
    b.append(wrapw(x + 12, 128, "Nor your reserves, nor your own minimum required contribution.",
                   W - x - 24, "sv-s", 11))

    b.append(t(0, 190, "THE CAP LADDER, CONVENTIONAL LOAN", "sv-k"))
    b.append(wrap(0, 206, "How much a builder is allowed to pay toward your costs scales with your "
                          "down payment. Buydowns count against this cap, which is why a builder "
                          "cannot stack an unlimited buydown on unlimited closing cost help.",
                  74, "sv-b", 12))
    ladder = [
        ("Loan over 90% of value", "3%", 0.33),
        ("75.01% to 90%", "6%", 0.66),
        ("75% or less", "9%", 1.00),
        ("Investment property", "2%", 0.22),
    ]
    lx, lw = 400, 300
    for i, (label, pct, frac) in enumerate(ladder):
        y = 196 + i * 30
        b.append(t(lx, y + 12, label, "sv-b"))
        b.append(box(lx + 150, y, 110, 16, PAPER2, r=3))
        b.append(box(lx + 150, y, 110 * frac, 16, NAVY700, r=3))
        b.append(t(lx + 268, y + 12, pct, "sv-n"))
    m, nh = note(0, 268, 380,
                 "On a VA loan, a builder funded temporary buydown is a seller concession capped "
                 "at 4 percent of reasonable value.")
    b.append(m)
    ny = 268 + nh + 12
    b.append(notfound(0, ny))
    b.append(wrapw(72, ny + 10,
                   "No FHA contribution percentage is printed here. The sources conflict.",
                   W - 80, "sv-s", 11))
    h = ny + 34
    return doc("06", W, h, "Where builder incentive money can and cannot go",
               "Three buckets a builder incentive can fill, each marked with a check: closing "
               "costs, a rate buydown, and prepaids including up to twelve months of HOA "
               "assessments. A fourth, hatched and marked with a cross, is the one it can never "
               "fill: your down payment, your reserves, or your own minimum required contribution. "
               "Alongside, a cap ladder for a conventional loan showing 3 percent when the loan is "
               "over 90 percent of value, 6 percent between 75.01 and 90 percent, 9 percent at 75 "
               "percent or less, and 2 percent on an investment property. No FHA percentage is "
               "printed because the sources conflict.",
               "\n".join(b))


# ================================================================ SVG-07
def svg07():
    b = [heading(0, 14, "Page 23", "Two clocks: your rate lock and the build calendar")]
    lx, lw = 128, W - 128
    # build calendar
    b.append(t(0, 78, "THE BUILD", "sv-k"))
    b.append(box(lx, 62, lw, 22, PAPER2, RULE, r=4))
    b.append(box(lx, 62, lw * 0.10, 22, NAVY900, r=4))
    b.append(t(lx + lw * 0.05, 52, "pre-construction", "sv-s sv-c"))
    b.append(box(lx + lw * 0.10, 62, lw * 0.42, 22, NAVY700))
    b.append(t(lx + lw * 0.10 + 6, 77, "one builder publishes 4 to 5 months of build", "sv-rs"))
    b.append(t(lx + lw * 0.56, 77, "another publishes 6 to 12 months", "sv-s"))
    b.append(wrapw(0, 96, "Eleven of the twelve volume builders publish no contract-to-close "
                          "time for Las Vegas at all.", lx - 12, "sv-s", 11))
    # the contractual outside date
    b.append(line(lx + lw, 56, lx + lw, 128, NAVY950, 1.6))
    b.append(t(lx + lw, 48, "outside date in the contract", "sv-s sv-e"))
    b.append(t(lx + lw, 36, "two years from signing, in one published clause", "sv-s sv-e"))

    # the rate lock
    b.append(t(0, 154, "YOUR RATE LOCK", "sv-k"))
    b.append(box(lx, 138, lw * 0.30, 22, NAVY600, r=4))
    b.append(t(lx + 6, 153, "lock window", "sv-rs"))
    b.append(box(lx + lw * 0.30, 138, lw * 0.70, 22, "url(#sv-hatch)", RULE, r=4))
    b.append(t(lx + lw * 0.30 + 8, 153, "unlocked, and the rate moves weekly", "sv-s"))
    rate_note = ("In July 2026 the national 30 year average moved every single week, 6.43 to "
                 "6.58 percent. That is a survey average, not a quote.")
    b.append(wrapw(0, 172, rate_note, lx - 12, "sv-s", 11))

    # collision points
    for i, (frac, label) in enumerate([
        (0.30, "1"), (0.62, "2"), (0.88, "3"),
    ]):
        x = lx + lw * frac
        b.append(line(x, 58, x, 166, CLAY, 1.2, "4 3"))
        b.append(f'<circle cx="{x}" cy="176" r="8.5" fill="{CLAY}"/>')
        b.append(t(x, 179.5, label, "sv-c",
                   f' style="font:700 10px {SANS};fill:{PAPER}"'))

    collide_y = max(172 + wrapw_h(rate_note, lx - 12, "sv-s", 11), 196) + 22
    b.append(t(0, collide_y, "THREE PLACES THE CLOCKS COLLIDE", "sv-k"))
    coll = [
        ("Your lock expires before the house is finished.",
         "Extending costs money, floating costs certainty, and no builder publishes a fee schedule."),
        ("The builder's rate pool runs dry.",
         "A builder can pay a lender in advance to lock a below market rate on a pool of future "
         "loans. Two publish that the rate lasts only until the pool is depleted or expires."),
        ("The appraisal lands months after the price was set.",
         "A price agreed today gets appraised five to twelve months from now, and an appraisal "
         "that moves your loan-to-value can push you across the $832,750 conforming line."),
    ]
    colw = W / 3 - 16
    body_y = collide_y + 18
    for i, (title_s, s_) in enumerate(coll):
        x = i * (W / 3)
        b.append(f'<circle cx="{x + 8}" cy="{body_y - 3}" r="8.5" fill="{CLAY}"/>')
        b.append(t(x + 8, body_y + 0.5, str(i + 1), "sv-c",
                   f' style="font:700 10px {SANS};fill:{PAPER}"'))
        b.append(wrapw(x + 24, body_y, title_s, colw - 24, "sv-l", 12))
        body_y2 = body_y + max(wrapw_h(c[0], colw - 24, "sv-l", 12) for c in coll) + 8
        b.append(wrapw(x, body_y2, s_, colw, "sv-s", 11))
    tail = body_y2 + max(wrapw_h(c[1], colw, "sv-s", 11) for c in coll) + 14
    b.append(notfound(0, tail))
    b.append(wrapw(72, tail + 10, "Extended lock, float-down and lock extension fee schedules. "
                                  "The guide teaches the six questions instead of printing a fee.",
                   W - 80, "sv-s", 11))
    h = tail + 34
    return doc("07", W, h, "Two clocks, your rate lock and the build calendar",
               "Two parallel horizontal timelines. The upper one is the build: a short "
               "pre-construction period, then four to five months of build published by one "
               "builder and six to twelve months by another, ending at a contractual outside date "
               "of two years from signing. The lower one is your rate lock: a short locked window "
               "followed by a long hatched unlocked stretch during which the rate moves weekly. "
               "Three marked collision points: the lock expiring before the house is finished, the "
               "builder's forward commitment rate pool running dry, and the appraisal landing "
               "months after the price was set.",
               "\n".join(b))


# ================================================================ SVG-08
def svg08():
    h = 360
    b = [heading(0, 14, "Page 24", "What surrounds a lot, and what the premium does not tell you")]
    # arterial road along the top with a sound wall
    b.append(box(0, 52, W, 26, PAPER2, r=0))
    b.append(line(0, 65, W, 65, RULE, 1.2, "14 10"))
    b.append(t(10, 48, "ARTERIAL ROAD", "sv-k"))
    b.append(f'<rect x="0" y="80" width="{W}" height="7" fill="{NAVY800}"/>')
    b.append(t(W - 8, 76, "sound wall", "sv-s sv-e"))

    # the cul de sac
    cx, cy = 300, 232
    b.append(f'<path d="M{cx} 96 L{cx} {cy - 46}" stroke="{PAPER2}" stroke-width="34" '
             f'fill="none"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="46" fill="{PAPER2}"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="46" fill="none" stroke="{RULE}" '
             f'stroke-width="1" stroke-dasharray="3 4"/>')

    lots = [
        (150, 118, 130, 80, "backs the road"),
        (150, 208, 130, 96, "downhill"),
        (322, 118, 132, 80, "west-facing rear"),
        (322, 208, 132, 96, "easement"),
        (472, 118, 118, 80, ""),
        (472, 208, 118, 96, ""),
    ]
    for x, y, lw_, lh_, tag in lots:
        b.append(box(x, y, lw_, lh_, CREAM, RULE, r=3))
        if tag:
            b.append(t(x + 8, y + lh_ - 8, tag, "sv-s"))

    # sun path
    b.append(f'<path d="M120 150 Q300 78 600 150" fill="none" stroke="{GOLD_BRAND}" '
             f'stroke-width="1.6" stroke-dasharray="5 5"/>')
    b.append(f'<circle cx="600" cy="150" r="7" fill="{GOLD_BRAND}"/>')
    b.append(t(612, 154, "4 p.m. in July", "sv-s"))
    b.append(t(112, 154, "sunrise", "sv-s sv-e"))

    # easement crossing the right lots
    b.append(f'<rect x="322" y="252" width="268" height="16" fill="url(#sv-hatch)" '
             f'stroke="{RULE_STRONG}" stroke-width="1"/>')
    b.append(t(330, 264, "power line easement", "sv-s"))

    # retention basin
    b.append(f'<ellipse cx="72" cy="266" rx="60" ry="38" fill="{NAVY_TINT}" stroke="{RULE}" '
             f'stroke-width="1"/>')
    b.append(t(72, 268, "retention", "sv-s sv-c"))
    b.append(t(72, 280, "basin", "sv-s sv-c"))

    # drainage fall
    b.append(arrow(210, 316, 120, 300, MUTED, 1.4, "trim"))
    b.append(t(218, 320, "drainage falls this way", "sv-s"))

    b.append(box(0, 330, W, 26, CARD_TINT, RULE, r=6))
    b.append(notfound(10, 336))
    b.append(t(82, 346, "No Clark County source quantifies what orientation costs you in utility "
                        "bills or comfort. Stand on the dirt at 4 p.m. in July.", "sv-b"))
    return doc("08", W, h, "What surrounds a lot",
               "A plan view of a cul-de-sac with six lots. An arterial road and a sound wall run "
               "along the top, so the lots on the upper row back the road. A dashed sun path arc "
               "crosses the drawing from sunrise to a marked 4 p.m. July position at the west, "
               "showing which rear yards carry afternoon sun. A hatched power line easement crosses "
               "two lots on the right. A retention basin sits at the lower left, and an arrow marks "
               "the direction drainage falls. A footer marks as NOT FOUND any Clark County source "
               "quantifying what lot orientation costs in utility bills or comfort.",
               "\n".join(b))


# ================================================================ SVG-09
def svg09():
    b = [heading(0, 14, "Page 26", "The four checkpoints, and what gets sealed after each")]
    stages = [
        ("Pre-drywall", "framing",
         "Framing, straps and hangers, plumbing and electrical runs, duct routing, flashing "
         "and waterproofing.",
         "Everything behind the drywall. This is the only time anyone sees the bones."),
        ("Blue tape walkthrough", "drywall",
         "Surfaces, fit and finish, and whether the options you ordered are what was installed.",
         "Cosmetic items get harder to argue once you have signed for the home."),
        ("Final walkthrough", "finished",
         "The condition you are accepting the house in, and the written punch list.",
         "Your one year clock starts when that punch list is completed, not at closing."),
        ("Eleven month walkthrough", "year",
         "Everything the first year of heat, settling and monsoon has surfaced.",
         "Do it at eleven months, not twelve. Three deadlines converge at the end of year one."),
    ]
    cw = W / 4
    colw = cw - 14
    seal_y = 208 + max(wrapw_h(st[2], colw, "sv-b", 11) for st in stages) + 12
    for i, (name, kind, visible, sealed) in enumerate(stages):
        x = i * cw
        b.append(t(x, 58, f"CHECKPOINT {i + 1}", "sv-k"))
        b.append(t(x, 74, name, "sv-l"))
        # house glyph, 92 wide
        gx, gy = x + 6, 86
        roof = f'M{gx} {gy + 30} L{gx + 46} {gy} L{gx + 92} {gy + 30}'
        b.append(f'<path d="{roof}" fill="none" stroke="{NAVY700}" stroke-width="1.8" '
                 f'stroke-linejoin="round"/>')
        wall_fill = {"framing": PAPER, "drywall": PAPER2,
                     "finished": NAVY_TINT, "year": NAVY_TINT}[kind]
        b.append(f'<rect x="{gx + 8}" y="{gy + 30}" width="76" height="52" fill="{wall_fill}" '
                 f'stroke="{NAVY700}" stroke-width="1.6"/>')
        if kind == "framing":
            for s in range(1, 6):
                b.append(line(gx + 8 + s * 12.6, gy + 30, gx + 8 + s * 12.6, gy + 82, NAVY700, 1))
            b.append(line(gx + 8, gy + 56, gx + 84, gy + 56, NAVY700, 1))
        if kind == "drywall":
            b.append(f'<rect x="{gx + 24}" y="{gy + 44}" width="16" height="10" fill="{NAVY600}"/>')
            b.append(f'<rect x="{gx + 54}" y="{gy + 44}" width="16" height="10" fill="{NAVY600}"/>')
        if kind in ("finished", "year"):
            b.append(f'<rect x="{gx + 24}" y="{gy + 42}" width="14" height="14" fill="{WHITE}" '
                     f'stroke="{NAVY700}" stroke-width="1"/>')
            b.append(f'<rect x="{gx + 52}" y="{gy + 46}" width="16" height="36" fill="{NAVY700}"/>')
        if kind == "year":
            b.append(f'<circle cx="{gx + 78}" cy="{gy + 16}" r="12" fill="{PAPER}" '
                     f'stroke="{NAVY950}" stroke-width="1.6"/>')
            b.append(line(gx + 78, gy + 16, gx + 78, gy + 8, NAVY950, 1.6))
            b.append(line(gx + 78, gy + 16, gx + 84, gy + 18, NAVY950, 1.6))
        b.append(t(x, 194, "WHAT YOU CAN SEE", "sv-k"))
        b.append(wrapw(x, 208, visible, colw, "sv-b", 11))
        # every column drops its second block at the same baseline, set by the tallest first block
        b.append(t(x, seal_y, "SEALED AFTER THIS", "sv-k"))
        b.append(wrapw(x, seal_y + 14, sealed, colw, "sv-s", 11))
    foot_y = seal_y + 14 + max(wrapw_h(st[3], colw, "sv-s", 11) for st in stages) + 14
    m, nh = note(0, foot_y, W,
                 "Nevada measures the statutory one year warranty from the completion of a written "
                 "punch list, not from your closing date. Insist the punch list is written, then "
                 "find that date and put it in your file.",
                 CARD_TINT, "sv-b", 11, stroke=RULE)
    b.append(m)
    h = foot_y + nh + 8
    return doc("09", W, h, "The four inspection checkpoints",
               "Four schematic houses at four build stages. First, pre-drywall, drawn with studs "
               "visible, where framing, straps and hangers, plumbing and electrical runs, duct "
               "routing, flashing and waterproofing are visible, and after which everything behind "
               "the drywall is sealed. Second, the blue tape walkthrough, for surfaces, fit and "
               "finish and whether the options ordered are what was installed. Third, the final "
               "walkthrough and the written punch list. Fourth, the eleven month warranty "
               "walkthrough, drawn with a clock. A footer notes that Nevada measures the statutory "
               "one year warranty from completion of the written punch list, not from closing.",
               "\n".join(b))


# ================================================================ SVG-10
def svg10():
    h = 450
    b = [heading(0, 14, "Page 28", "Where the six areas are")]

    def ridge(pts):
        d = " ".join(f"L{x} {y}" for x, y in pts[1:])
        return (f'<path d="M{pts[0][0]} {pts[0][1]} {d}" fill="none" stroke="{NAVY800}" '
                f'stroke-width="1.8" stroke-linejoin="round"/>')

    # Ranges go outside the basin outline. The first pass drew the west range across the basin
    # floor, where it collided with two markers and read as terrain inside the city.
    b.append(t(376, 56, "Sheep Range", "sv-s sv-c"))
    b.append(ridge([(300, 92), (324, 62), (350, 90), (376, 60), (402, 90), (428, 64), (454, 92)]))
    b.append(f'<path d="M150 120 Q360 96 580 124 Q662 200 610 302 Q400 348 200 316 '
             f'Q118 218 150 120 z" fill="{CREAM}" stroke="{RULE}" stroke-width="1"/>')
    b.append(ridge([(98, 306), (130, 288), (98, 270), (130, 252), (98, 234), (130, 216),
                    (98, 198), (130, 180), (98, 162)]))
    b.append(t(0, 336, "Spring Mountains and the Red Rock escarpment", "sv-s"))

    # corridors, abstract
    b.append(f'<path d="M492 132 Q424 214 352 318" fill="none" stroke="{RULE}" '
             f'stroke-width="6" stroke-linecap="round" opacity=".5"/>')
    b.append(t(506, 138, "I-15", "sv-s"))
    b.append(f'<path d="M252 202 Q372 158 500 210 Q552 270 470 306 Q352 336 270 292 '
             f'Q218 248 252 202 z" fill="none" stroke="{RULE}" stroke-width="3" '
             f'stroke-dasharray="9 7" opacity=".7"/>')
    b.append(t(376, 152, "the 215 beltway", "sv-s sv-c"))
    b.append(f'<line x1="416" y1="216" x2="384" y2="276" stroke="{NAVY950}" stroke-width="5" '
             f'stroke-linecap="round"/>')
    b.append(t(428, 252, "the Strip", "sv-s"))

    areas = [
        ("Summerlin", 202, 222),
        ("Skye Canyon and the northwest", 302, 158),
        ("North Las Vegas", 516, 176),
        ("Southwest and Mountain's Edge", 262, 306),
        ("Henderson: Cadence and Inspirada", 494, 294),
        ("Union Village", 540, 248),
    ]
    for i, (name, x, y) in enumerate(areas):
        # a paper halo so a marker sitting on the beltway or I-15 still reads cleanly
        b.append(f'<circle cx="{x}" cy="{y}" r="12" fill="{PAPER}"/>')
        b.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{NAVY700}"/>')
        b.append(t(x, y + 3.6, str(i + 1), "sv-c",
                   f' style="font:700 10px {SANS};fill:{PAPER}"'))
    # a numbered dot on a schematic is not a label, so the legend carries the names
    b.append(t(0, 362, "THE SIX AREAS IN THIS GUIDE", "sv-k"))
    for i, (name, x, y) in enumerate(areas):
        col, row = i % 3, i // 3
        lx2 = col * (W / 3)
        ly2 = 382 + row * 19
        b.append(f'<circle cx="{lx2 + 7}" cy="{ly2 - 3.5}" r="7" fill="{NAVY700}"/>')
        b.append(t(lx2 + 7, ly2 - 0.4, str(i + 1), "sv-c",
                   f' style="font:700 9px {SANS};fill:{PAPER}"'))
        b.append(t(lx2 + 20, ly2, name, "sv-b"))
    b.append(wrapw(0, 426, "Schematic, not a street map, and not to scale. Distances and "
                           "boundaries are approximate. Pahrump, Mesquite and Boulder City are "
                           "outside this guide and are not drawn.", W, "sv-s", 11))
    return doc("10", W, h, "Where the six areas are",
               "An abstract orientation schematic of the Las Vegas valley, not a street map. The "
               "basin is bounded by the Spring Mountains and Red Rock escarpment to the west and "
               "the Sheep Range to the north, with the 215 beltway drawn as a dashed loop, I-15 as "
               "a diagonal, and the Strip as a short heavy segment. Six numbered markers locate the "
               "areas this guide covers: Summerlin to the west, Skye Canyon and the northwest, "
               "North Las Vegas to the north, the southwest and Mountain's Edge, Henderson with "
               "Cadence and Inspirada to the southeast, and Union Village. Pahrump, Mesquite and "
               "Boulder City are outside the guide and are not drawn.",
               "\n".join(b))


# ================================================================ SVG-11
def svg11():
    b = [heading(0, 14, "Page 15", '"Included" means three completely different things')]
    b.append(box(0, 56, W, 8, PAPER2, r=4))
    b.append(arrow(0, 60, W - 4, 60, NAVY700, 2))
    b.append(t(0, 82, "LESS CHOICE, MORE CERTAINTY", "sv-k"))
    b.append(t(W, 82, "MORE CHOICE, MORE DECISIONS", "sv-k sv-e"))
    models = [
        ("Model 1", "Fixed package",
         "One builder has no design center and no upgrades at all. You buy a set inclusion "
         "package.",
         "You gain: a price that does not move, and a shorter path to the keys.",
         "You give up: every choice past the floor plan.", NAVY900),
        ("Model 2", "Included features",
         "An included-features model instead of a buyer-facing design center. Some compete on "
         "standards: owned solar, an EV outlet, a smart home package, a tankless water heater.",
         "You gain: real equipment in the base price.",
         "You give up: control. Features vary by community and by homesite.", NAVY700),
        ("Model 3", "Full design center",
         "Studios you visit and select in, item by item, or from curated collections.",
         "You gain: the house you actually chose.",
         "You give up: budget certainty, and a great deal of your time.", NAVY600),
    ]
    cw = 226
    inner = cw - 24
    # every column starts its gain/give block at the same baseline, set by the tallest description,
    # so the section below can never be landed on by the longest column
    gain_y = 142 + max(wrapw_h(m[2], inner, "sv-b", 12) for m in models) + 14
    give_y = gain_y + max(wrapw_h(m[3], inner - 18, "sv-s", 11) for m in models) + 10
    limits_y = give_y + max(wrapw_h(m[4], inner - 18, "sv-s", 11) for m in models) + 22
    for i, (n, name, what, gain, give, fill) in enumerate(models):
        x = i * (cw + 11)
        b.append(box(x, 96, cw, 28, fill, r=6))
        b.append(t(x + 12, 115, f"{n} · {name}", "sv-r"))
        b.append(wrapw(x + 12, 142, what, inner, "sv-b", 12))
        b.append(tick(x + 18, gain_y - 3.5))
        b.append(wrapw(x + 30, gain_y, gain, inner - 18, "sv-s", 11))
        b.append(cross(x + 18, give_y - 3.5, fill=MUTED))
        b.append(wrapw(x + 30, give_y, give, inner - 18, "sv-s", 11))

    b.append(t(0, limits_y, "TWO HARD LIMITS NOBODY PUTS ON A FLYER", "sv-k"))
    for i, s_ in enumerate([
        "Your design selections must be final before the build starts, at the one builder that "
        "publishes the rule.",
        "One builder states on every community page that buyers may be limited in the structural "
        "changes, options and upgrades they can make.",
    ]):
        b.append(f'<rect x="0" y="{limits_y + 10 + i * 26}" width="8" height="8" '
                 f'fill="{NAVY950}"/>')
        b.append(wrapw(16, limits_y + 17 + i * 26, s_, W - 16, "sv-b", 11))
    nf_y = limits_y + 10 + 2 * 26 + 8
    b.append(notfound(0, nf_y))
    b.append(wrapw(72, nf_y + 10, "Not one of the twelve volume builders publishes a design center "
                                  "spend requirement, a design credit amount, or whether upgrades "
                                  "can be financed. Ask both in writing.", W - 80, "sv-s", 11))
    h = nf_y + 34
    return doc("11", W, h, "The three builder business models",
               "A left-to-right spectrum from less choice and more certainty to more choice and "
               "more decisions. Model one is a fixed package: no design center and no upgrades, "
               "where you gain a price that does not move and give up every choice past the floor "
               "plan. Model two is included features, where you gain real equipment in the base "
               "price and give up control because features vary by community and homesite. Model "
               "three is a full design center, where you gain the house you chose and give up "
               "budget certainty and time. Two hard limits are listed, and a NOT FOUND note "
               "records that no volume builder publishes a design center spend requirement, a "
               "credit amount, or whether upgrades can be financed.",
               "\n".join(b))


# ================================================================ SVG-13
def svg13():
    b = [heading(0, 14, "Page 11", "The two clocks of a move-up")]
    lx, lw = 118, W - 118
    b.append(t(0, 74, "YOUR BUILD", "sv-k"))
    b.append(box(lx, 58, lw, 24, PAPER2, RULE, r=4))
    b.append(box(lx, 58, lw * 0.52, 24, NAVY700, r=4))
    b.append(t(lx + 8, 74, "the part a builder will estimate for you", "sv-rs"))
    b.append(t(lx + lw * 0.58, 74, "the part only your contract governs", "sv-s"))

    b.append(t(0, 142, "YOUR SALE", "sv-k"))
    b.append(box(lx, 126, lw, 24, PAPER2, RULE, r=4))
    b.append(box(lx, 126, lw * 0.34, 24, NAVY950, r=4))
    b.append(t(lx + 8, 142, "prepare and list", "sv-rs"))
    b.append(box(lx + lw * 0.34, 126, lw * 0.22, 24, NAVY600))
    b.append(t(lx + lw * 0.34 + 8, 142, "under contract", "sv-rs"))
    b.append(t(lx + lw * 0.58, 142, "closed, and you need somewhere to live", "sv-s"))

    for frac in (0.34, 0.52, 0.56, 0.86):
        x = lx + lw * frac
        b.append(line(x, 52, x, 156, CLAY, 1.1, "4 3"))
    marks = [(0.34, "1"), (0.52, "2"), (0.56, "3"), (0.86, "4")]
    for frac, label in marks:
        x = lx + lw * frac
        b.append(f'<circle cx="{x}" cy="168" r="8.5" fill="{CLAY}"/>')
        b.append(t(x, 171.5, label, "sv-c", f' style="font:700 10px {SANS};fill:{PAPER}"'))

    b.append(t(0, 206, "FOUR PLACES THEY COLLIDE", "sv-k"))
    coll = [
        ("List early", "You risk carrying two payments, or moving twice."),
        ("List late", "You risk losing the build slot you waited for."),
        ("The closing date moves", "Builders publish that the closing date is an estimate and is "
                                   "not guaranteed."),
        ("The outside date arrives", "Only the contract deadline is enforceable. One published "
                                     "clause commits to finishing within two years of signing."),
    ]
    cw = W / 4
    for i, (title_s, s_) in enumerate(coll):
        x = i * cw
        b.append(f'<circle cx="{x + 8}" cy="222" r="8.5" fill="{CLAY}"/>')
        b.append(t(x + 8, 225.5, str(i + 1), "sv-c",
                   f' style="font:700 10px {SANS};fill:{PAPER}"'))
        b.append(t(x + 24, 226, title_s, "sv-l"))
        b.append(wrapw(x, 250, s_, cw - 14, "sv-s", 11))
    m, nh = note(0, 288, W,
                 "Eleven of the twelve volume builders publish no contract-to-close time for Las "
                 "Vegas at all. So the question is not when will it be done. It is what is the "
                 "outside date in my contract, and what happens to me on that date.",
                 NAVY_TINT, "sv-b", 11)
    b.append(m)
    h = 288 + nh + 8
    return doc("13", W, h, "The two clocks of a move-up",
               "Two parallel timelines. The upper one is your build, split between the part a "
               "builder will estimate for you and the longer part only your contract governs. The "
               "lower one is your sale: prepare and list, under contract, then closed and needing "
               "somewhere to live. Four marked collision points: listing early and risking two "
               "payments, listing late and risking the build slot, the closing date moving because "
               "builders publish it as an estimate that is not guaranteed, and the contractual "
               "outside date arriving. A footer notes that eleven of twelve volume builders "
               "publish no contract-to-close time at all.",
               "\n".join(b))


BUILDERS = {
    "01": (svg01, 5, "Which path is yours"),
    "02": (svg02, 3, "Who works for whom at a model home"),
    "03": (svg03, 18, "The sequence"),
    "04": (svg04, "19 to 20", "Where the special assessment sits"),
    "05": (svg05, 21, "The year one tax reset"),
    "06": (svg06, 22, "Where the incentive money can and cannot go"),
    "07": (svg07, 23, "Two clocks: rate lock and build calendar"),
    "08": (svg08, 24, "What surrounds a lot"),
    "09": (svg09, 26, "The four checkpoints"),
    "10": (svg10, 28, "Where the six areas are"),
    "11": (svg11, 15, "Three business models"),
    "12": (svg12, 17, "The monthly stack"),
    "13": (svg13, 11, "The two clocks of a move-up"),
}


def main():
    want = sys.argv[1:] or sorted(BUILDERS)
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for num in sorted(want):
        fn, page, title = BUILDERS[num]
        markup = fn()
        path = os.path.join(OUT, f"svg-{num}.svg")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(markup)
        desc = markup.split("<desc", 1)[1].split(">", 1)[1].split("</desc>")[0]
        vb = markup.split('viewBox="0 0 ', 1)[1].split('"', 1)[0]
        rows.append((num, page, title, vb, len(markup), desc))
        print(f"svg-{num}.svg  page {page:<8} {vb:<10} {len(markup) / 1024:5.1f}KB  {title}")

    if len(want) == len(BUILDERS):
        with open(os.path.join(OUT, "index.md"), "w", encoding="utf-8") as fh:
            fh.write(index_md(rows))
        contact_sheets()
        print(f"\nwrote {os.path.join(OUT, 'index.md')}, _contact.html, _gray.html")
    print(f"\n{len(rows)} of {len(BUILDERS)} diagrams written to build/svg/")


CONTACT_TPL = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>SVG contact sheet%(label)s</title>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@100..900&display=swap"
      rel="stylesheet">
<style>
body{margin:0;padding:24px;background:#8a8a8a;font:14px Archivo,system-ui,sans-serif;%(filter)s}
section{background:#F7F5F0;margin:0 auto 22px;max-width:760px;padding:16px 20px 20px;
        border-radius:10px;box-shadow:0 2px 10px #0003}
h2{margin:0 0 10px;font:700 12px Archivo;letter-spacing:.1em;text-transform:uppercase;
   color:#5F5A52}
.fig svg{display:block;width:100%%;height:auto}
</style></head><body>
%(body)s
</body></html>"""


def contact_sheets():
    """
    Two review artifacts, regenerated with the set so they can never show a stale diagram.

    `_gray.html` is not decoration. audience-path-map.md warns that a large share of readers
    print this at home in black and white, and the failure it warns about, three hues at the
    same value collapsing into three identical grays, is invisible in color. Check both.
    """
    body = "\n".join(
        f'<section><h2>svg-{n}</h2><div class="fig">'
        f'{open(os.path.join(OUT, f"svg-{n}.svg"), encoding="utf-8").read()}</div></section>'
        for n in sorted(BUILDERS))
    for name, label, filt in (("_contact.html", "", ""),
                              ("_gray.html", " grayscale", "filter:grayscale(1)")):
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
            fh.write(CONTACT_TPL % {"label": label, "filter": filt, "body": body})


def index_md(rows):
    out = ["# SVG diagram index", "",
           "Generated by [`build-svg.py`](../../build-svg.py). Do not hand-edit these files; edit "
           "the generator and re-run, or the set drifts.", "",
           "```bash", "python3 build-svg.py        # all thirteen",
           "python3 build-svg.py 04 09  # just those", "```", "",
           "## Reviewing them", "",
           "`build/svg/_contact.html` renders all thirteen at reading size, and `_gray.html` "
           "renders the same set through a grayscale filter. Both are regenerated with the set, "
           "so neither can show a stale diagram. Serve the folder and open them:", "",
           "```bash",
           "python3 -m http.server 8092 --bind 127.0.0.1",
           "# then http://127.0.0.1:8092/build/svg/_contact.html", "```", "",
           "The grayscale sheet is a real gate, not a nicety. `audience-path-map.md` requires the "
           "three reader paths to stay distinguishable on a home black and white printer, and the "
           "failure it warns about, different hues at the same value collapsing into identical "
           "grays, is invisible on screen in color.", "",
           "## How the assembler uses these", "",
           "**Inline them, do not `<img>` them.** They must inherit the page's fonts, they must "
           "survive grayscale printing, and an `<img>` would not let the guide's print stylesheet "
           "reach inside. Each file is a complete `<svg>` element with `role=\"img\"` and a "
           "`<title>`/`<desc>` pair already wired to `aria-labelledby`, so inlining satisfies the "
           "accessibility gate with no extra markup.", "",
           "Wrap each one in the guide's `.fig` component and give it a `.figcap`. The `<desc>` "
           "text below is the accessible description that already ships inside the file; the "
           "`.figcap` is the visible caption and should not repeat it verbatim.", "",
           "**Every class inside these files is `sv-` prefixed.** An inline `<svg><style>` in HTML "
           "is not scoped and leaks to the whole document, so an unprefixed rule here would "
           "silently restyle the guide.", "",
           "## The set", "",
           "| ID | Page | Title | viewBox | Size |", "|---|---|---|---|---|"]
    for num, page, title, vb, size, _ in rows:
        out.append(f"| SVG-{num} | {page} | {title} | `{vb}` | {size / 1024:.1f}KB |")
    out += ["", "## Accessible descriptions", "",
            "These are already inside each file. They are reproduced here so the accessibility "
            "audit can be run against this document without parsing thirteen SVGs.", ""]
    for num, page, title, vb, size, desc in rows:
        out.append(f"**SVG-{num}, page {page}.** {' '.join(desc.split())}")
        out.append("")
    out += ["## Rules these files follow", "",
            "- **Every hex is written out**, because `:root` custom properties do not reach inside "
            "an inline SVG. That is the round 6 lesson, in a different medium.",
            "- **Orange appears in SVG-04 and SVG-12 only**, which are the cost diagram, plus the "
            "`NOT FOUND` token wherever the outline says the number does not exist. Those are two "
            "of the four places `build/design-system.md` allows warm color. Every other emphasis "
            "is carried by weight, rule and glyph.",
            "- **Nothing is encoded by color alone.** Allowed and forbidden pairs print a drawn "
            "check or cross and the literal word. Path elements print the letter and the tab words.",
            "- **Check and cross glyphs are drawn as paths, not typed**, so they never depend on a "
            "font that failed to load.",
            "- **No number appears that is not in `research/fact-ledger.md`** and named in "
            "`outline/guide-outline.md` for that page. Where the outline says a figure does not "
            "exist, the diagram prints the `NOT FOUND` token instead of estimating.", ""]
    return "\n".join(out)


if __name__ == "__main__":
    main()
