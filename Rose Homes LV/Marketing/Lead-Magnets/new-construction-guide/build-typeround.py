#!/usr/bin/env python3
"""
Design round generator, rounds 4 and 5.

Round 4, the type round.

Ryan's round 3 verdict was specific: direction 6's layout and color, direction 4's
typography, direction 3's layout also liked, direction 2 "nice but a lot of orange",
direction 1 out. Every one of those notes is about type or about a layout he has
already seen. So round 4 changes exactly one variable at a time.

Directions 1 through 5 are direction 6 byte for byte, with only the typeface pairing
swapped. Same layout, same palette, same copy, same spacing. Direction 6 is the other
half of his note: direction 3's layout, repainted in direction 6's palette, set in the
pairing he said he liked.

The swap is not a naive font-family substitution. A heavy grotesque and a serif do not
want the same tracking or the same weight at 54pt, so each variant carries a tracking
delta and a display weight pair. Tracking is applied as calc(base + delta) per selector
so the base file's typographic hierarchy survives instead of being flattened to one value.

Round 5 is the narrowing: one pairing, both surviving layouts.

Round 6 pulls the orange back to an accent at two strengths, in both layouts, and sets
the geometric cover title mixed case to match the navy one.

Re-runnable. `python3 build-typeround.py <round>`, default 6. Building round 5 archives
whatever round is currently live in design/direction-* first.
"""

import glob
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DESIGN = os.path.join(HERE, "design")
BASE6 = os.path.join(DESIGN, "_v3-directed", "direction-6-navy-sunset", "preview.html")
BASE3 = os.path.join(DESIGN, "_v3-directed", "direction-3-sunset-geometric", "preview.html")

FONT_LINK = re.compile(r'<link href="https://fonts\.googleapis\.com/css2\?[^"]*" rel="stylesheet">')

# Display selectors and the letter-spacing the base file gives each one, in em.
# The delta is added, never replacing, so a variant keeps the base hierarchy.
TRACK6 = [
    (".seal .n", -.030), (".cover-title", -.032), (".byname", -.022),
    (".band h1", -.030), (".lead-hit", -.020), (".qt", -.024),
    (".refuse h3", -.030), (".phone-num", -.010), (".pull", -.032),
    (".prop h3", -.018), (".hero h1", -.034),
]
HI6 = ".seal .n,.cover-title,.band h1,.refuse h3,.pull,.hero h1,.folio"
MD6 = ".byname,.lead-hit,.qt,.prop h3,.phone-num"

# Direction 3's display selectors, with the tracking the base file actually gives each.
#
# These were wrong until round 6 was locked, and wrong in a way that produced no error:
# the list carried names from direction 6 (`.band h1`, `.qt`) that direction 3 does not
# use, and bare `.pull` where direction 3 sets `.gp .pull`, which is more specific and
# quietly won. So five display elements, including the largest section headline, kept the
# grotesque's tight tracking under a high contrast serif. Verified by reading computed
# styles out of the rendered page rather than by reading the CSS.
TRACK3 = [
    (".cover-title", -.030), (".op-h", -.030), (".gp .op-line", -.024),
    (".gp .hit", -.022), (".a", -.020), (".refuse h3", -.028),
    (".gp .pull", -.034), (".hero h1", -.030), (".prop h3", -.015),
    (".folio", -.020), (".phone-num", -.020),
]
HI3 = ".cover-title,.op-h,.refuse h3,.gp .pull,.hero h1,.folio"
MD3 = ".gp .op-line,.gp .hit,.a,.prop h3,.phone-num"

SPECTRAL = ("Spectral", "Be Vietnam Pro",
            "family=Spectral:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,600"
            "&family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,600")

ROUND4 = [
    dict(
        slug="direction-1-spectral-and-be-vietnam",
        base="6", display=SPECTRAL[0], text=SPECTRAL[1], url=SPECTRAL[2],
        serif=True, dtrack=".016em", hi=800, md=700,
        thesis="Direction 4's exact pairing dropped into direction 6. The control, and the one "
               "closest to what you already said you liked.",
        why="Spectral is a serif built for long reading on paper and screen both, with a large "
            "x height that keeps 9.5pt body honest. Be Vietnam Pro carries the caps labels at "
            "900 without going brittle. This is the pairing from direction 4, unchanged.",
    ),
    dict(
        slug="direction-2-bodoni-and-archivo",
        base="6", display="Bodoni Moda", text="Archivo",
        url="family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900"
            "&family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900",
        serif=True, dtrack=".022em", hi=700, md=600,
        thesis="Direction 2's typography, which you called nice, with direction 6's color and "
               "layout instead of the orange.",
        why="Bodoni Moda is high contrast, so it is the most formal option here and the most "
            "fragile at small sizes. Weight is held at 700 rather than 800 because Bodoni's "
            "thick strokes get heavy fast. Archivo is a workhorse grotesque with a wide range.",
    ),
    dict(
        slug="direction-3-literata-and-dm-sans",
        base="6", display="Literata", text="DM Sans",
        url="family=Literata:ital,opsz,wght@0,7..72,200..900;1,7..72,200..900"
            "&family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000",
        serif=True, dtrack=".018em", hi=800, md=700, cover=48,
        thesis="Sturdier and squarer than Spectral. Reads solid rather than elegant.",
        why="Literata was drawn for the Google Play book reader, so it is a serif engineered "
            "for sustained reading rather than for a masthead. Slab-ish serifs give the "
            "headlines more physical weight. DM Sans is geometric and neutral underneath it.",
    ),
    dict(
        slug="direction-4-newsreader-and-figtree",
        base="6", display="Newsreader", text="Figtree",
        url="family=Newsreader:ital,opsz,wght@0,6..72,200..800;1,6..72,200..800"
            "&family=Figtree:ital,wght@0,300..900;1,300..900",
        serif=True, dtrack=".014em", hi=700, md=600,
        thesis="The warmest of the five. Magazine feature rather than manual.",
        why="Newsreader has more stroke contrast and open counters than Spectral, which reads "
            "friendlier at headline size and a little softer at body size. Figtree is a rounded "
            "humanist sans, so the caps labels lose some of their institutional edge.",
    ),
    dict(
        slug="direction-5-source-serif-and-public-sans",
        base="6", display="Source Serif 4", text="Public Sans",
        url="family=Source+Serif+4:ital,opsz,wght@0,8..60,200..900;1,8..60,200..900"
            "&family=Public+Sans:ital,wght@0,100..900;1,100..900",
        serif=True, dtrack=".018em", hi=800, md=700,
        thesis="The plainest option. Nothing about the type asks for attention.",
        why="Source Serif 4 and Public Sans are both open source faces designed for documents "
            "people have to trust, and Public Sans is literally the US federal design system "
            "face. If the guide should read as a public record rather than as marketing, this "
            "is the pairing that does it.",
    ),
    dict(
        slug="direction-6-geometric-layout-spectral",
        base="3", display=SPECTRAL[0], text=SPECTRAL[1], url=SPECTRAL[2],
        serif=True, dtrack=".016em", hi=700, md=600,
        thesis="The other half of your note. Direction 3's layout, repainted in direction 6's "
               "navy and sunset, set in the pairing from direction 4.",
        why="You said you liked direction 3's layout and hated the font, so this keeps the "
            "geometry and replaces both the type and the all orange palette. The teal and plum "
            "that direction 3 used as its cool notes are now the lifted navy family.",
    ),
]

BODONI = ("Bodoni Moda", "Archivo",
          "family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900"
          "&family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900")

# Round 5. Ryan kept the Bodoni and Archivo pairing out of round 4 and asked to see it
# in both surviving layouts. The first of these is byte for byte what round 4 direction 2
# already was; it is rebuilt here so the two sit side by side in one comparison instead
# of across two archived rounds.
ROUND5 = [
    dict(
        slug="direction-1-bodoni-navy-layout",
        base="6", display=BODONI[0], text=BODONI[1], url=BODONI[2],
        serif=True, dtrack=".022em", hi=700, md=600,
        thesis="Bodoni and Archivo in the navy layout. Identical to round 4 direction 2, "
               "rebuilt so the two layouts sit next to each other.",
        why="The panel layout: a photographic cover with a lit navy panel under it, the "
            "section opening as a full bleed band dissolving into the paper, and a two column "
            "text page. Bodoni's high contrast reads as formal against the navy, and the "
            "thin strokes hold up because the display sizes here are large.",
    ),
    dict(
        slug="direction-2-bodoni-geometric-layout",
        base="3", display=BODONI[0], text=BODONI[1], url=BODONI[2],
        serif=True, dtrack=".022em", hi=700, md=600,
        thesis="The same pairing in the geometric layout, repainted navy and sunset.",
        why="The geometric layout runs the cover title in caps at a smaller size and uses "
            "harder edged blocks and chips throughout. Caps set in Bodoni is where the face "
            "is at its most classical, and it is also where its thin strokes are most exposed.",
    ),
]

# Round 6. Two asks. The geometric cover was the only place the two round 5 variants
# looked like different typefaces, because it sets the title in caps at 36pt while the
# navy cover sets it mixed case at 52pt; the faces themselves were already identical.
# And the orange: both layouts get it pulled back, at two strengths, so the choice is a
# dial rather than a yes or no.
ROUND6 = [
    dict(
        slug="direction-1-navy-orange-dialed-back",
        base="6", display=BODONI[0], text=BODONI[1], url=BODONI[2],
        serif=True, dtrack=".022em", hi=700, md=600, recolor="dialed-back", one_tint=True,
        thesis="The navy layout with orange demoted from structure to accent.",
        why="Running heads, chips, folios, list markers and the third card tint all move "
            "to navy. Orange keeps the refusal panel, the button, and the accent phrase in "
            "the headline. The photographs keep their warmth.",
    ),
    dict(
        slug="direction-2-navy-orange-minimal",
        base="6", display=BODONI[0], text=BODONI[1], url=BODONI[2],
        serif=True, dtrack=".022em", hi=700, md=600, recolor="minimal", one_tint=True,
        thesis="The same layout with orange pulled back as far as it goes without losing "
               "the refusal panel.",
        why="Everything in the dialed back version, plus the ochre details become gold, the "
            "warm card tints go neutral, the accent phrases go navy, and the warm gradients "
            "over the photographs are cooled. Two warm objects survive: the refusal panel "
            "and the button.",
    ),
    dict(
        slug="direction-3-geometric-orange-dialed-back",
        base="3", display=BODONI[0], text=BODONI[1], url=BODONI[2],
        serif=True, dtrack=".022em", hi=700, md=600,
        recolor="dialed-back", one_tint=True, cover3=46,
        thesis="The geometric layout with the cover title set like the navy one, mixed case "
               "and large, and orange demoted to accent.",
        why="Same treatment as direction 1 applied to the geometric structure: the running "
            "head tag, both folios, the chips, the list markers and the peach cards go navy. "
            "The table zebra goes neutral instead of peach, which is where a lot of the "
            "warmth was hiding.",
    ),
    dict(
        slug="direction-4-geometric-orange-minimal",
        base="3", display=BODONI[0], text=BODONI[1], url=BODONI[2],
        serif=True, dtrack=".022em", hi=700, md=600,
        recolor="minimal", one_tint=True, cover3=46,
        thesis="The geometric layout pulled back as far as direction 2, for a like for like "
               "comparison across both layouts.",
        why="Every clay colored subhead, table header, phone number and eyebrow goes navy, "
            "the remaining warm tints go neutral, and the ochre squares become brand gold. "
            "The NOT FOUND token stays warm because there the color is carrying meaning.",
    ),
]

ROUNDS = {"4": ROUND4, "5": ROUND5, "6": ROUND6}

# Direction 3's palette mapped onto direction 6's. Its two cool notes, the agave teal
# and the plum dusk, become the lifted navy family, which is what pulls the orange back
# from being the whole page to being the accent.
#
# This is a document wide substitution, not a :root override, because direction 3's
# inline SVG diagrams and inline style attributes carry hardcoded hexes that no custom
# property reaches. Overriding :root alone left the cost diagram with a plum bar and a
# teal rail sitting in a navy layout.
D3_RECOLOR = [
    ("#2B1D23", "#1C2436"),   # ink to navy black
    ("#6B584E", "#5F5A52"),   # warm gray muted
    ("#FBF6ED", "#F7F5F0"),   # paper
    ("#FDF8F1", "#FBF8F2"),   # cream
    ("#F8EFE2", "#EDE9E0"),   # sand to second surface
    ("#166A62", "#2C3F6B"),   # agave teal to navy-700
    ("#0F4F49", "#242F4A"),   # deep agave to navy-900
    ("#4A2B52", "#28375A"),   # plum dusk to navy-800
    ("#DCEBE7", "#E4E9F2"),   # agave tint to navy tint
    ("#EDE6EE", "#E4E9F2"),   # plum tint to navy tint
    ("#9E3A1F", "#B8360F"),   # clay to text weight sunset
    ("#977C61", "#847B6D"),   # rule
    ("#7C6349", "#5F5A52"),   # strong rule
    ("#F3E6D6", "#FBE5DA"),   # clay tint to sunset tint
    ("rgba(43,29,35", "rgba(28,36,54"),
    ("rgba(74,43,82", "rgba(40,55,90"),
    ("rgba(251,246,237", "rgba(247,245,240"),
    ("rgba(158,58,31", "rgba(184,54,15"),
]


# --------------------------------------------------------------------------------------
# Orange reduction, rounds 6 and later.
#
# Both layouts inherited the sunset family as a structural color, not an accent: running
# heads, chips, folios, list markers, card tints and photo overlays were all warm, so the
# page reads orange before it reads anything else. These blocks hand the structural roles
# back to the navy family and leave orange only where it carries meaning.
#
# Two things stay warm at every level, deliberately. The refusal panel is the loudest
# object on the spread by design, and the primary button is the one thing on the landing
# page that has to be found without looking. Spending the boldness in one place is the
# whole point; spreading it everywhere is what made it feel like too much.
DIALED_BACK_6 = """
.chip-sunset{ background:var(--navy-950); color:var(--paper); }
.eyebrow{ background:var(--navy-800); }
.hero-eyebrow{ background:var(--navy-800); }
.seal{ background:var(--navy-800); color:var(--gold); }
.nlist .n{ background:var(--navy-700); }
.folio-sunset{ background:var(--navy-800); color:var(--paper); }
.card-sunset-tint{ background:var(--navy-tint); }
.q-sunset{ color:var(--navy-700); }
.q-sunset::before{ background:var(--navy-600); }
.prop-3{ background:var(--navy-tint); }
.prop-3 .ic{ background:var(--navy-700); }
"""

MINIMAL_6 = DIALED_BACK_6 + """
.card-ochre-tint{ background:var(--paper-2); }
.q-ink::before{ background:var(--gold-brand); }
.brokerage .dot{ background:var(--gold); color:var(--navy-950); }
.trust .lock .dot{ background:var(--gold); color:var(--navy-950); }
.edition b{ color:var(--gold); }
.close p b{ color:var(--gold); }
.prop-2{ background:var(--paper-2); }
.prop-2 .ic{ background:var(--navy-600); }
.gp .deck b, .gp .lead-hit, .pull span, .band .sec-line{ color:var(--navy-700); }
.hero h1 em{ color:var(--navy-600); }
.cover-title em{ color:var(--gold); }
/* the photo overlays carried most of the warmth. Cooled, not removed: the rock is red
   and no overlay is going to change that. */
.cover-photo .lift{ background:
  radial-gradient(90% 70% at 78% 16%, rgba(55,84,152,.26) 0%, rgba(55,84,152,0) 62%),
  linear-gradient(180deg, rgba(20,26,39,.46) 0%, rgba(20,26,39,0) 34%); }
.band .warm{ background:
  radial-gradient(80% 60% at 82% 22%, rgba(55,84,152,.30) 0%, rgba(55,84,152,0) 64%);
  mix-blend-mode:multiply; }
.hero{ background:
  radial-gradient(96% 62% at 100% 0%, rgba(55,84,152,.16) 0%, rgba(55,84,152,0) 58%),
  radial-gradient(80% 66% at 0% 100%, rgba(44,63,107,.13) 0%, rgba(44,63,107,0) 62%),
  var(--paper); }
"""

# Direction 3 never had a navy family of its own, so the recolored hexes get names here
# before the structural swaps can reference them.
NAVY_VARS_3 = """
:root{
  --navy-600:#304880; --navy-700:#2C3F6B; --navy-800:#28375A; --navy-950:#141A27;
  --navy-tint:#E4E9F2; --paper-2:#EDE9E0; --gold:#D8BB84; --gold-brand:#C9A86E;
}
"""

DIALED_BACK_3 = NAVY_VARS_3 + """
.rh-a{ background:var(--navy-800); color:var(--paper); }
.chip-sunset{ background:var(--navy-950); color:var(--paper); }
.chip-coral{ background:var(--navy-tint); color:var(--ink); }
.nlist .n{ background:var(--navy-700); }
.folio{ background:var(--navy-800); }
.foot-r .folio{ background:var(--navy-950); }
.card-clay{ background:var(--navy-tint); }
table.sid tbody tr:nth-child(even){ background:var(--paper-2); }
.gp .q-clay{ color:var(--navy-700); }
.gp .q-clay::before{ background:var(--navy-600); }
.prop-1{ background:var(--navy-tint); }
.prop-1 .ic{ background:var(--navy-700); }
.hero-eyebrow{ background:var(--navy-800); }
"""

MINIMAL_3 = DIALED_BACK_3 + """
.gp .hit{ color:var(--navy-700); }
.gp .op-eyebrow, .gp .op-line, .gp .op-deck b{ color:var(--navy-700); }
.gp .pull span{ color:var(--navy-700); }
table.sid tbody th{ color:var(--navy-700); }
.phone-num{ color:var(--navy-700); }
.map-card h4{ color:var(--navy-700); }
.edition b{ color:var(--navy-700); }
.cover-eyebrow{ color:var(--navy-700); }
.card-coral{ background:var(--paper-2); }
.prop-3{ background:var(--paper-2); }
.mark .sq, .brokerage .sq, .trust .lock .sq{ background:var(--gold-brand); }
.cred{ background:var(--gold); }
.card-dusk sup.src{ color:var(--gold); }
.close p b{ color:var(--gold); }
"""

# The tinted cards all take the fill of the "Sub association" bar in the cost diagram,
# #FBEFD3, which is the ochre tint. Applied to every tinted card rather than only the blue
# ones: leaving two card tints behind that no longer encode anything different is exactly
# what the palette rules forbid, and it reads as an accident rather than a decision.
# Note the geometric layout's own diagram draws that bar in #FBE5DA, a pinker tint. The
# ochre one is used in both layouts so the two stay comparable.
CARD_TINT = "#FBEFD3"

ONE_TINT_6 = f"""
.card-navy-tint, .card-sunset-tint, .card-ochre-tint,
.prop-1, .prop-2, .prop-3{{ background:{CARD_TINT}; }}
.pill-done{{ background:{CARD_TINT}; }}
"""

ONE_TINT_3 = f"""
.card-agave, .card-clay, .card-coral,
.prop-1, .prop-2, .prop-3{{ background:{CARD_TINT}; }}
.chip-coral{{ background:{CARD_TINT}; color:var(--ink); }}
"""

ONE_TINT = {"6": ONE_TINT_6, "3": ONE_TINT_3}

RECOLOR = {
    ("6", "dialed-back"): DIALED_BACK_6, ("6", "minimal"): MINIMAL_6,
    ("3", "dialed-back"): DIALED_BACK_3, ("3", "minimal"): MINIMAL_3,
}


def override_css(v):
    track = TRACK3 if v["base"] == "3" else TRACK6
    hi, md = (HI6, MD6) if v["base"] == "6" else (HI3, MD3)
    display_all = ",".join(s for s, _ in track)
    lines = [
        "/* TYPE OVERRIDE. Only typography changes below, plus the direction 3",
        "   palette port on direction 6 of this round. Layout and spacing are untouched. */",
        ":root{",
        f'  --display:"{v["display"]}", Georgia, "Times New Roman", serif;'
        if v["serif"] else f'  --display:"{v["display"]}", "Helvetica Neue", Arial, sans-serif;',
        f'  --text:"{v["text"]}", "Helvetica Neue", Arial, sans-serif;',
        f'  --dtrack:{v["dtrack"]};',
    ]
    lines.append("}")
    lines.append("body,.page,.hero{ font-optical-sizing:auto; }")
    lines.append(
        f"{display_all}{{ font-variation-settings:normal; font-optical-sizing:auto; }}")
    for sel, base in track:
        lines.append(f"{sel}{{ letter-spacing:calc({base:.3f}em + var(--dtrack)); }}")
    lines.append(f'{hi}{{ font-weight:{v["hi"]}; }}')
    lines.append(f'{md}{{ font-weight:{v["md"]}; }}')
    if v["base"] == "6":
        # The cover panel is a fixed 5.72in box with overflow:hidden on the page, so a
        # face wider than the grotesque the layout was drawn for pushes the compliance
        # line off the paper and clips it silently. Every serif here runs the title to
        # three lines at 54pt in a 6.5in measure, which also breaks the accent phrase
        # "Model Home" across a line. Measured: a 7.3in measure at 52pt puts it back to
        # two lines with the accent intact, at a rendered height within 5px of the
        # original. Literata is wider still and needs 48pt, which is a real property of
        # the face and is shown rather than hidden.
        lines.append(".cover-title{ max-width:7.3in; font-size:%dpt; }"
                     % v.get("cover", 52))
        # Same problem one size down. The refusal headline is the loudest object on the
        # spread, and a wide face drops "number." onto a line of its own. Measured: the
        # 6.2in measure is the constraint, not the size, and 6.8in still clears the
        # panel's own padding. Narrower faces are unaffected because they already fit.
        lines.append(".refuse h3{ max-width:6.8in; }")
    if v.get("cover3"):
        # The geometric cover sets its title in caps at 36pt. Mixed case at that size
        # reads small, so it goes up with the caps removed.
        lines.append(".cover-title{ text-transform:none; font-size:%dpt; }" % v["cover3"])
    if v.get("recolor"):
        lines.append(RECOLOR[(v["base"], v["recolor"])].strip())
    if v.get("one_tint"):
        lines.append(ONE_TINT[v["base"]].strip())
    return "\n".join(lines)


def build_one(v):
    src = BASE3 if v["base"] == "3" else BASE6
    doc = open(src, encoding="utf-8").read()

    if v["base"] == "3":
        for old, new in D3_RECOLOR:
            doc = re.sub(re.escape(old), new, doc, flags=re.I)

    new_link = (f'<link href="https://fonts.googleapis.com/css2?{v["url"]}'
                f'&display=swap" rel="stylesheet">')
    doc, n = FONT_LINK.subn(new_link, doc)
    if n != 1:
        raise SystemExit(f"{v['slug']}: expected exactly 1 font link, found {n}")

    label = f'{v["display"]} and {v["text"]}'
    doc = re.sub(r"<title>[^<]*</title>",
                 f"<title>{label}, Before You Walk Into the Model Home</title>", doc)
    doc = doc.replace("Direction 6, Navy and Sunset", label)
    doc = doc.replace("Direction 3, Sunset Geometric", label)

    doc = doc.replace("</head>", f"<style>\n{override_css(v)}\n</style>\n</head>", 1)

    out = os.path.join(DESIGN, v["slug"])
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(out)
    with open(os.path.join(out, "preview.html"), "w", encoding="utf-8") as fh:
        fh.write(doc)

    base_note = ("direction 3 of round 3, layout only, repainted"
                 if v["base"] == "3" else "direction 6 of round 3, unchanged")
    with open(os.path.join(out, "tokens.md"), "w", encoding="utf-8") as fh:
        fh.write(f"""# Tokens, {label}

Layout and palette are inherited from {base_note}. The only tokens this variant
sets are the two typefaces and the tracking delta that makes them sit correctly at
display size.

| Token | Value |
|---|---|
| `--display` | {v["display"]} |
| `--text` | {v["text"]} |
| `--dtrack` | {v["dtrack"]}, added to every display tracking value |
| display weight, large | {v["hi"]} |
| display weight, medium | {v["md"]} |

## Palette, identical across every variant in this round

| Token | Hex | Role |
|---|---|---|
| `--paper` | #F7F5F0 | the ground everywhere |
| `--paper-2` | #EDE9E0 | second surface, table zebra |
| `--ink` | #1C2436 | navy black, all body text |
| `--muted` | #5F5A52 | warm gray, attributions |
| `--navy-500` | #375498 | the spotlight peak |
| `--navy-700` | #2C3F6B | base of the lit panel |
| `--navy-950` | #141A27 | deep edge |
| `--sunset` | #D24018 | saturated fill, never text on paper |
| `--sunset-d` | #B8360F | text weight sunset, 5.39 on paper |
| `--ochre` | #EFA00B | fill only, carries ink at 7.16 |
| `--gold` | #D8BB84 | lifted gold, text only on navy-900 and darker |

Contrast pairs were computed in round 3 against `--navy-500`, the lightest point of the
spotlight, which is the worst case. Changing the typeface does not change any of them.
""")

    with open(os.path.join(out, "rationale.md"), "w", encoding="utf-8") as fh:
        fh.write(f"""# {label}

> {v["thesis"]}

## Why this pairing

{v["why"]}

## What changed from round 3

{"Layout from direction 3, palette from direction 6, type from direction 4."
 if v["base"] == "3" else
 "Nothing except the two typefaces and the tracking and weight adjustments they need."}
Same copy, same page architecture, same page budget, same contrast pairs. If one of
these reads better than another, the difference is typography and nothing else.

## Tracking

The base file tracks display type tight, between -.018em and -.034em, which suits the
heavy grotesque it was drawn for. A serif at 54pt does not want that. Every display
selector here is `calc(base + {v["dtrack"]})`, so the relative hierarchy the base
established survives while the absolute tracking loosens to what this face wants.
""")
    return out


def archive_current(label, incoming):
    """Move whatever design/direction-* is live into design/<label>/ before a new round
    overwrites it. Re-running the same round must not archive that round on top of the
    one it replaced, so a live set that already is the incoming round is left alone."""
    live = [d for d in glob.glob(os.path.join(DESIGN, "direction-*")) if os.path.isdir(d)]
    if not live:
        return
    if {os.path.basename(d) for d in live} <= {v["slug"] for v in incoming}:
        return
    dest = os.path.join(DESIGN, label)
    os.makedirs(dest, exist_ok=True)
    for d in live:
        target = os.path.join(dest, os.path.basename(d))
        if os.path.isdir(target):
            shutil.rmtree(target)
        shutil.move(d, target)
    print(f"archived {len(live)} directions to design/{label}/")


def main():
    for f in (BASE6, BASE3):
        if not os.path.isfile(f):
            raise SystemExit(f"missing base: {f}")
    rnd = sys.argv[1] if len(sys.argv) > 1 else "6"
    if rnd not in ROUNDS:
        raise SystemExit(f"unknown round {rnd}, have {sorted(ROUNDS)}")
    prior = {"5": "_v4-type", "6": "_v5-layout"}.get(rnd)
    if prior:
        archive_current(prior, ROUNDS[rnd])
    print(f"round {rnd}")
    for v in ROUNDS[rnd]:
        out = build_one(v)
        kb = os.path.getsize(os.path.join(out, "preview.html")) / 1024
        print(f"  {v['slug']:44s} {v['display']} + {v['text']}  ({kb:.0f}KB)")
    print("\nnext: python3 build-compare.py   then screenshot each and check page fit")


if __name__ == "__main__":
    main()
