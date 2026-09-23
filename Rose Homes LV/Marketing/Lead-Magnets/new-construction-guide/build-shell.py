#!/usr/bin/env python3
"""
Generate build/shell.html: the document the fragments get poured into.

The shell is GENERATED, not hand written, and it is generated from the winning
preview rather than transcribed out of design-system.md. That is deliberate.
design-system.md warns that the render is the contract because the winning file
is a base stylesheet plus an override layer, so the source alone does not tell
you which rule won. Transcribing the CSS by hand would reintroduce exactly the
bug the design lock was written to catch. So both <style> blocks are lifted
verbatim, in order, and only the preview-stage chrome is removed.

What gets removed, and why each one is safe:
  .stage / .cap / .rail   preview scaffolding. design-system.md lists these under
                          "Preview stage only, never in the shipping guide".
  .spread                 a preview device for showing facing pages side by side.
                          The guide is a linear page stack.
  body background         #6E625C is the preview's grey mounting board.
  .page flex + shadow     .page floated in a flex rail and carried a drop shadow.
                          In the guide it is a page, not a card on a board.

Everything else, including the @page rule and the whole @media print block, is
carried through untouched.

Run: python3 build-shell.py
"""

import re
import sys
from pathlib import Path

EMDASH = "\u2014"  # escaped, so a grep over *.py stays clean too

ROOT = Path(__file__).resolve().parent
PREVIEW = ROOT / "design" / "direction-3-geometric-orange-dialed-back" / "preview.html"
OUT = ROOT / "build" / "shell.html"

FRAGMENT_MARKER = "<!-- ===== FRAGMENTS ===== -->"


def style_blocks(html):
    """Return the two <style> block bodies, in document order."""
    blocks = re.findall(r"<style>\n(.*?)\n</style>", html, re.S)
    if len(blocks) != 2:
        sys.exit(f"expected 2 style blocks in the preview, found {len(blocks)}")
    return blocks


def strip_preview_chrome(css):
    """Remove the preview stage rules. Everything else survives verbatim."""
    # whole-rule removals, matched on the selector at the start of a line
    kill_selectors = [
        r"\.stage\{[^}]*\}",
        r"\.cap\{[^}]*\}",
        r"\.cap span\{[^}]*\}",
        r"\.rail\{[^}]*\}",
        r"\.spread\{[^}]*\}",
    ]
    for pat in kill_selectors:
        css = re.sub(pat, "", css)

    # the preview stage comment header above them
    css = css.replace(
        "/* ---------- preview stage chrome, grey caption strips ---------- */", ""
    )

    # body mounting board colour
    css = css.replace("background:#6E625C;", "background:var(--paper);")

    # .page was a flex child on a board. In the guide it is the page.
    css = css.replace(
        "  flex:0 0 auto;\n  width:8.5in; height:11in;",
        "  width:8.5in; height:11in;\n  margin:0 auto;",
    )
    css = css.replace("  box-shadow:0 16px 38px rgba(30,18,14,.40);\n", "")

    # print block: drop the rules that only existed to undo the stage
    for line in [
        "  .stage{ padding:0; line-height:0; }\n",
        "  .rail{ line-height:normal; }\n",
        "  .cap{ display:none; }\n",
        "  .rail{ display:block; margin:0; }\n",
        "  .spread{ display:block; gap:0; }\n",
        "  .page{ box-shadow:none; break-after:page; page-break-after:always; }\n",
    ]:
        css = css.replace(line, "")
    # The page break rule was bundled with the shadow reset on the same line, so
    # removing the stage chrome removed pagination with it. Put it back on its own.
    # Without this the whole 39 page guide prints as one continuous flow.
    css = css.replace(
        "@media print{\n  body{ background:var(--white); }\n",
        "@media print{\n  body{ background:var(--white); }\n"
        "  .page{ break-after:page; page-break-after:always; }\n",
    )
    if "break-after:page" not in css:
        sys.exit("pagination rule lost while stripping preview chrome, refusing to write")

    css = re.sub(r"\n{3,}", "\n\n", css)
    css = re.sub(r"\n[ \t]+\n", "\n", css)
    return css.strip()


GUIDE_ADDITIONS = """
/* ==========================================================================
   ADDED FOR THE SHIPPING GUIDE. Not in the preview, because the preview only
   had to show three pages and a hero. Nothing here restyles a preview
   component; these are the pieces a 39 page document needs and a 3 page
   sample did not.
   ========================================================================== */

/* Screen-only page separation. The preview got this from its grey rail, which
   is gone. Print overrides it back to nothing. */
.page{ box-shadow:0 2px 14px rgba(28,36,54,.13); margin-bottom:18px; }
@media print{ .page{ box-shadow:none; margin-bottom:0; } }

/* The source strip runs to two lines on the dense pages. The preview only ever
   showed a one line example, and a 48px foot holds two lines of 6.9pt/1.35
   with room left over. Measured, not assumed. */
.foot .srcnote{ max-width:6.6in; }
.foot-l .srcnote{ padding-right:8pt; }

/* Skip link, screen only. A 39 page print document still gets keyboard users. */
.skip{
  position:absolute; left:-9999px; top:0;
  background:var(--ink); color:var(--paper);
  font:800 12px/1 var(--text); padding:12px 16px; border-radius:0 0 var(--r-sm) 0;
  z-index:10; text-decoration:none;
}
.skip:focus{ left:0; }
@media print{ .skip{ display:none; } }

/* Links. The preview never had one, so nothing styled them and all 21 anchors in
   the guide rendered default browser blue, which is outside the palette and
   prints as grey mud. Clay rather than navy so a link does not read as a heading,
   and the underline is offset so it does not collide with descenders. */
.gp a, .close a, .card a{
  color:var(--clay); text-decoration:underline;
  text-decoration-thickness:.6pt; text-underline-offset:2px;
}
.gp a:hover{ text-decoration-thickness:1.2pt; }
.gp a:focus-visible{ outline:2.5px solid var(--navy-800); outline-offset:2px; }
.card-dusk a, .close a{ color:var(--gold); }
@media print{
  /* In print a link cannot be clicked, so it has to carry its own address.
     Only for external links, and only where the href is a real URL. */
  .gp a[href^="http"]::after{
    content:" (" attr(data-print) ")";
    font-weight:600; color:var(--muted); text-decoration:none;
  }
  .gp a[href^="http"]:not([data-print])::after{ content:""; }
}

/* Inline diagram sizing. build/svg/index.md requires the SVGs to be inlined
   rather than referenced as an image file, so role="img", title and desc
   reach a screen reader and print-color-adjust reaches the fills. An inlined
   svg has no intrinsic box, so it needs one here.

   SIZING RULE, measured not guessed. Every diagram is authored at viewBox width
   700 and its smallest label is 8 design units. Rendered at width W the label
   prints at 6 * (W/710) points. So:
        full measure, 710px  ->  6.0pt   legible
        85 percent,   604px  ->  5.1pt   floor
        half column,  343px  ->  2.9pt   illegible

   A 700 wide diagram therefore CANNOT sit in a .cols column. Four of them did,
   and printed labels at 2.9 to 3.2pt. `.fig` spans the full measure by default
   and `.fig.col` is the opt in for the two diagrams authored narrow. */
.fig svg{ width:100%; max-width:100%; height:auto; }
.fig.wide{ grid-column:1 / -1; }
.fig.narrow svg{ max-width:236px; }

/* Contents block on p2. Typography, per the outline, not a component. */
.toc{ list-style:none; margin:0; padding:0; }
.toc li{
  display:flex; align-items:baseline; gap:6pt;
  font:400 9pt/1.5 var(--text); margin-bottom:3.4pt;
  break-inside:avoid; page-break-inside:avoid;
}
.toc .lbl{ flex:0 0 auto; font-weight:700; }
.toc .dots{ flex:1 1 auto; border-bottom:.75pt dotted var(--rule); transform:translateY(-2px); }
.toc .pg{ flex:0 0 auto; font-weight:800; font-variant-numeric:tabular-nums; }
.toc .grp{
  font:800 7.2pt/1 var(--text); letter-spacing:.16em; text-transform:uppercase;
  color:var(--navy-700); margin:9pt 0 5pt;
}
.toc li:first-child .grp{ margin-top:0; }

/* Path edge tab. audience-path-map.md requires a reader to find their path by
   the edge of the closed stack, and requires it to survive a black and white
   printer, so the three tabs are separated by value and the pale one inverts.
   Hexes are written out because a :root custom property does not reach here
   any more reliably than it reached inside the inline SVGs. */
.tab{
  position:absolute; right:0; width:.30in;
  display:flex; align-items:center; justify-content:center;
  writing-mode:vertical-rl;
  font:800 7pt/1 var(--text); letter-spacing:.19em; text-transform:uppercase;
}
.tab-a{ background:#304880; color:#F7F5F0; top:1.30in; height:2.15in; }
.tab-b{ background:#141A27; color:#F7F5F0; top:3.55in; height:2.15in; }
.tab-c{
  background:#EDE9E0; color:#1C2436; top:5.80in; height:2.15in;
  box-shadow:inset 0 0 0 2pt #141A27;
}

/* `.tok` is an inline-flex chip with 4pt of right padding, so a sentence that
   ends right after one prints a visible gap before its period. It hit all three
   writers, who each worked around it by reordering the sentence. Fixed once here
   instead. */
.tok{ margin-right:-2.4pt; }
.tok + .tok{ margin-left:2.4pt; }

/* ==========================================================================
   SOURCE APPENDIX, pages 40 to 44.

   This is the decision recorded in this folder's CLAUDE.md: "Attribution is now
   one short inline line under the paragraph it supports, with full URLs in a
   numbered back appendix." The design sample's own running foot already pointed
   at "the source appendix, page 41", and the folder header already described a
   44 page guide. 39 content pages plus 5 appendix pages is where 44 comes from.

   Set at 7pt over 1.34 in two columns. 34 of 39 pages cite something, and a
   guide that hides its sources is a brochure.
   ========================================================================== */
.srclist{
  columns:2; column-gap:20pt; column-rule:.75pt solid var(--rule);
  list-style:none; margin:0; padding:0;
}
.srclist li{
  break-inside:avoid; page-break-inside:avoid;
  margin:0 0 5.4pt; padding-left:8pt; border-left:1.6pt solid var(--navy-tint);
  font:400 7pt/1.34 var(--text); color:var(--ink);
}
/* The marker run reads "12 to 14, 19", so it cannot be an absolutely positioned
   numeral in a fixed gutter the way a single number could. It leads the row. */
.srclist .sn{
  font-weight:800; font-variant-numeric:tabular-nums; color:var(--navy-700);
  margin-right:4pt;
}
.srclist .sv{ font-weight:700; }
.srclist .su{ color:var(--muted); word-break:break-all; }
.srclist .sd{ color:var(--muted); white-space:nowrap; }
.srclist .snf{ color:var(--clay); font-weight:800; }
.appx-lede{ font:500 8.6pt/1.45 var(--text); color:var(--ink); margin:0 0 10pt; max-width:6.4in; }
.appx-lede b{ font-weight:800; }

/* Tear-out rule on p38. page-budget.md designs that page to be physically
   removed, so it prints a cut line. */
.tearout{
  position:absolute; left:0; right:0; top:0;
  border-top:1.2pt dashed var(--rule-strong);
}
.tearout span{
  position:absolute; left:var(--pad); top:5pt;
  font:800 6.4pt/1 var(--text); letter-spacing:.16em; text-transform:uppercase;
  color:var(--muted); background:var(--paper); padding:0 5pt;
}
"""

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Before You Walk Into the Model Home | Las Vegas New Construction Buyer Guide</title>
<meta name="description" content="A plain guide to buying a newly built home in Las Vegas, Henderson, and Clark County. Every number sourced and dated. Ryan Rose, Real Broker, LLC.">
<meta name="author" content="Ryan Rose, Real Broker, LLC">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&display=swap" rel="stylesheet">
"""


def main():
    html = PREVIEW.read_text()
    base, override = style_blocks(html)

    doc = [
        HEAD,
        "<style>",
        "/* ---------- BASE, lifted verbatim from the winning preview ---------- */",
        strip_preview_chrome(base),
        "</style>",
        "<style>",
        "/* ---------- TYPE AND PALETTE OVERRIDE, lifted verbatim ---------- */",
        override.strip(),
        "</style>",
        "<style>",
        GUIDE_ADDITIONS.strip(),
        "</style>",
        "</head>",
        "<body>",
        '<a class="skip" href="#p2">Skip to the contents</a>',
        "",
        FRAGMENT_MARKER,
        "",
        "</body>",
        "</html>",
        "",
    ]
    out = "\n".join(doc)

    if EMDASH in out:
        sys.exit("em-dash in generated shell, refusing to write")
    if "position:fixed" in out.replace(" ", ""):
        sys.exit("position:fixed in generated shell, refusing to write")

    OUT.write_text(out)
    print(f"wrote {OUT.relative_to(ROOT)}  {len(out.splitlines())} lines")
    print(f"  base css {len(strip_preview_chrome(base).splitlines())} lines, "
          f"override {len(override.strip().splitlines())}, "
          f"guide additions {len(GUIDE_ADDITIONS.strip().splitlines())}")


if __name__ == "__main__":
    main()
