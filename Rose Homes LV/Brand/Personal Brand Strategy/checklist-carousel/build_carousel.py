#!/usr/bin/env python3
"""
Rose Homes LV — New Construction Buyer's Defense Checklist
Instagram carousel generator. Emits 8 standalone 1080x1350 slide HTML files
(dark navy brand template) plus a stacked preview.html.

Brand: Deep Navy #1C2333, Champagne Gold #C9A86E, White, Slate #8A8FA8.
Fonts: Playfair Display (display), Montserrat (labels), Inter (body).
"""

import os

BASE = "/Users/ryanrose/Downloads/Claude/Rose Homes LV/Brand/Personal Brand Strategy/checklist-carousel"
SLIDES_DIR = os.path.join(BASE, "slides")
os.makedirs(SLIDES_DIR, exist_ok=True)

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?'
         'family=Playfair+Display:ital,wght@0,600;0,700;1,600;1,700&'
         'family=Montserrat:wght@500;600;700&'
         'family=Inter:wght@400;500;600&display=swap" rel="stylesheet">')

CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
html,body{ width:1080px; height:1350px; }
body{ font-family:'Inter',Arial,sans-serif; background:#1C2333; color:#fff; }
.slide{
  position:relative; width:1080px; height:1350px;
  padding:88px 86px 78px; display:flex; flex-direction:column;
  background:radial-gradient(125% 80% at 14% 6%, #242d47 0%, #1C2333 56%);
  overflow:hidden;
}
.bracket{ position:absolute; width:56px; height:56px; }
.bracket.tl{ top:44px; left:46px; border-top:3px solid #C9A86E; border-left:3px solid #C9A86E; }
.bracket.br{ bottom:44px; right:46px; border-bottom:3px solid #C9A86E; border-right:3px solid #C9A86E; }

.topbar{ display:flex; justify-content:space-between; align-items:center; z-index:2; }
.kicker{ font-family:'Montserrat',sans-serif; font-weight:600; text-transform:uppercase;
  letter-spacing:.26em; font-size:23px; color:#C9A86E; }
.idx{ font-family:'Montserrat',sans-serif; font-weight:600; letter-spacing:.2em;
  font-size:22px; color:#8A8FA8; }

.mid{ flex:1; display:flex; flex-direction:column; justify-content:center; z-index:2; }
.mid.top{ justify-content:flex-start; padding-top:34px; }

.num{ font-family:'Playfair Display',Georgia,serif; font-weight:700; font-size:158px; line-height:.82; color:#C9A86E; }
.numrule{ width:90px; height:3px; background:#C9A86E; margin:20px 0 40px; }

.pill{ display:inline-block; font-family:'Montserrat',sans-serif; font-weight:700; font-size:21px;
  letter-spacing:.13em; text-transform:uppercase; color:#1C2333; background:#C9A86E;
  padding:10px 20px; border-radius:4px; margin-bottom:28px; align-self:flex-start; }

.title{ font-family:'Playfair Display',Georgia,serif; font-weight:700; font-size:68px;
  line-height:1.08; letter-spacing:-1px; color:#fff; }
.title em{ font-style:italic; color:#C9A86E; }

.body{ font-family:'Inter',sans-serif; font-weight:400; font-size:34px; line-height:1.56;
  color:#D8DCE8; margin-top:34px; max-width:906px; }
.body b{ color:#fff; font-weight:600; }
.body .g{ color:#C9A86E; font-weight:600; }

.foot{ display:flex; justify-content:space-between; align-items:center; z-index:2; }
.mark{ font-family:'Playfair Display',serif; font-weight:700; font-size:30px; color:#fff; letter-spacing:-.5px; }
.mark span{ color:#C9A86E; }
.handle{ font-family:'Montserrat',sans-serif; font-weight:600; font-size:22px; letter-spacing:.05em; color:#8A8FA8; }
.swipe{ font-family:'Montserrat',sans-serif; font-weight:700; font-size:24px; letter-spacing:.16em;
  text-transform:uppercase; color:#C9A86E; }

/* cover */
.eyebrow{ font-family:'Montserrat',sans-serif; font-weight:600; text-transform:uppercase;
  letter-spacing:.28em; font-size:25px; color:#C9A86E; margin-bottom:26px; }
.cover-title{ font-family:'Playfair Display',serif; font-weight:700; font-size:94px; line-height:1.04;
  letter-spacing:-2px; color:#fff; }
.cover-title em{ font-style:italic; color:#C9A86E; }
.cover-sub{ font-family:'Inter',sans-serif; font-weight:400; font-size:35px; line-height:1.5;
  color:#D8DCE8; margin-top:38px; max-width:850px; }

/* cta */
.ctabox{ border:2px solid #C9A86E; border-radius:10px; padding:32px 36px; margin-top:40px;
  background:rgba(201,168,110,.08); }
.ctabox .lead{ font-family:'Montserrat',sans-serif; font-weight:700; font-size:35px; line-height:1.34; color:#fff; }
.ctabox .lead b{ color:#C9A86E; }
.contact{ margin-top:38px; }
.contact .n{ font-family:'Playfair Display',serif; font-weight:700; font-size:40px; color:#fff; }
.contact .n span{ color:#C9A86E; }
.contact .d{ font-family:'Inter',sans-serif; font-weight:500; font-size:29px; color:#C9A86E; margin-top:12px; letter-spacing:.02em; }
"""

MARK = '<div class="mark">Rose Homes<span> LV</span></div>'
HANDLE = '<div class="handle">@rosehomeslv</div>'

def page(inner):
    return ("<!doctype html><html><head><meta charset='utf-8'>" + FONTS +
            "<style>" + CSS + "</style></head><body>" + inner + "</body></html>")

def slide(idx, kicker, mid_html, foot_left, foot_right, mid_top=False):
    midcls = "mid top" if mid_top else "mid"
    return page(
        "<div class='slide'>"
        "<div class='bracket tl'></div><div class='bracket br'></div>"
        "<div class='topbar'><div class='kicker'>" + kicker + "</div>"
        "<div class='idx'>" + f"{idx:02d}" + " / 08</div></div>"
        "<div class='" + midcls + "'>" + mid_html + "</div>"
        "<div class='foot'>" + foot_left + foot_right + "</div>"
        "</div>"
    )

slides = []

# 1 — COVER
slides.append(slide(
    1, "Las Vegas Buyer's Guide",
    "<div class='eyebrow'>New Construction</div>"
    "<div class='cover-title'>The Buyer's<br><em>Defense</em> Checklist</div>"
    "<div class='cover-sub'>The questions builders hope you don't ask. And the costs they don't put on the sign.</div>",
    MARK, "<div class='swipe'>Swipe &rarr;</div>"
))

# 2 — SETUP / STATEMENT
slides.append(slide(
    2, "Read this first",
    "<div class='title'>That friendly face at the model home works for the <em>builder</em>.</div>"
    "<div class='body'><b>Not for you.</b> Here are 5 things to check before you sign a new build in Las Vegas. Save this for your next tour.</div>",
    MARK, HANDLE
))

# 3 — 01 REPRESENTATION
slides.append(slide(
    3, "Representation",
    "<div class='num'>01</div><div class='numrule'></div>"
    "<div class='title'>Bring your own agent on <em>day one</em>.</div>"
    "<div class='body'>Most builders pay your agent, so it costs you nothing. But walk in alone and you can lose the right to bring one later. Register with representation on visit one.</div>",
    MARK, HANDLE
))

# 4 — 02 CONTRACT
slides.append(slide(
    4, "The contract",
    "<div class='num'>02</div><div class='numrule'></div>"
    "<div class='title'>Read the contract the <em>builder</em> wrote.</div>"
    "<div class='body'>Their lawyers wrote it to protect them. Find the delay clause, the cancellation terms, and whether tariff increases can be passed to you. Get every promise in writing.</div>",
    MARK, HANDLE
))

# 5 — 03 SID/LID (hero)
slides.append(slide(
    5, "Hidden costs",
    "<div class='num'>03</div><div class='numrule'></div>"
    "<span class='pill'>The big Vegas one</span>"
    "<div class='title'>Ask about <em>SID and LID</em> bonds.</div>"
    "<div class='body'>These assessments are billed on top of your property taxes. Often <span class='g'>$500 to $3,000+ a year</span>, for 10 to 20 years. They transfer to you and can lead to foreclosure if unpaid. Get the number before you fall in love.</div>",
    MARK, HANDLE
))

# 6 — 04 LENDER
slides.append(slide(
    6, "Financing",
    "<div class='num'>04</div><div class='numrule'></div>"
    "<div class='title'>Don't take the builder's lender at <em>face value</em>.</div>"
    "<div class='body'>The incentives are usually tied to their preferred lender. Get their full Loan Estimate, then compare one outside quote on rate and fees. Know what a buydown becomes after it ends.</div>",
    MARK, HANDLE
))

# 7 — 05 INSPECTION
slides.append(slide(
    7, "Inspections",
    "<div class='num'>05</div><div class='numrule'></div>"
    "<div class='title'>Inspect the <em>brand-new</em> home.</div>"
    "<div class='body'>About 9 out of 10 new homes have a significant issue at inspection. Get a pre-drywall inspection before the walls close, and an independent final inspection before closing. New is not flawless.</div>",
    MARK, HANDLE
))

# 8 — CTA
slides.append(slide(
    8, "Your move",
    "<div class='title'>Get the full <em>checklist</em>.</div>"
    "<div class='body'>Eight sections. Every question to ask before you sign a new build in Las Vegas. Free, and no builder will hand it to you.</div>"
    "<div class='ctabox'><div class='lead'>Comment <b>CHECKLIST</b> or DM me and I'll send the printable PDF.</div></div>"
    "<div class='contact'><div class='n'>Ryan <span>Rose</span></div>"
    "<div class='d'>Rose Homes LV · 702-747-5921 · rosehomeslv.com</div></div>",
    MARK, HANDLE
))

# write slides
for i, html in enumerate(slides, 1):
    with open(os.path.join(SLIDES_DIR, f"slide-{i:02d}.html"), "w") as f:
        f.write(html)

# stacked preview for humans
prev = ("<!doctype html><html><head><meta charset='utf-8'>" + FONTS +
        "<style>" + CSS +
        " body{background:#5a5f70;} .wrap{display:flex;flex-wrap:wrap;gap:26px;justify-content:center;padding:30px;}"
        " .thumb{width:1080px;transform:scale(.42);transform-origin:top center;margin:-390px -310px;}"
        "</style></head><body><div class='wrap'>")
for i in range(1, 9):
    prev += f"<div class='thumb'>{slides[i-1].split('<body>')[1].split('</body>')[0]}</div>"
prev += "</div></body></html>"
with open(os.path.join(BASE, "preview.html"), "w") as f:
    f.write(prev)

print(f"Wrote {len(slides)} slides to {SLIDES_DIR}")
print(f"Wrote preview to {os.path.join(BASE, 'preview.html')}")
