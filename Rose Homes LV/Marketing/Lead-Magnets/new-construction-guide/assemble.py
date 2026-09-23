#!/usr/bin/env python3
"""
Assemble the guide from build/fragments/p01.html .. p39.html.

What this script owns, and why each piece is mechanical rather than authored:

  1. Splices the 39 page fragments into build/shell.html.
  2. Inlines the thirteen diagrams in place of their <!-- SVG-NN --> markers.
     build/svg/index.md requires inlining rather than <img> so that role="img",
     <title> and <desc> reach a screen reader and print color adjustment reaches
     the fills.
  3. Numbers every citation globally, 1..N, in document order. Writers emit
     data-claim="<claim-id>" and a literal asterisk; this replaces the asterisk.
     Three writers hand-numbering in parallel would collide on the first shared
     page, so the number is generated and a writer only has to get the claim-id
     right. An unknown claim-id FAILS THE BUILD, which is what makes that safe.
  4. Fills each page's .srcnote from the ledger: marker range, the source
     organizations on that page, the verified date.
  5. Emits the companion source list, one row per marker, with the full URL.
     design-system.md "Citations, the two tier contract" has the reasoning: the
     guide cites 254 unique URLs, the frozen design gives the strip one line in a
     48px foot, and four extra pages of URLs would fail the 32 to 40 page gate.
  6. Emits the contents block on p2 from the outline, so the TOC cannot drift.

Every page in this guide is a hard break, so pagination is deterministic: one
fragment is one printed page. That is checked, not assumed, by qa-check.py
counting PDF pages. There is no reflow pass to run.

Run: python3 assemble.py
"""

import json
import re
import sys
from collections import OrderedDict
from pathlib import Path
from urllib.parse import urlparse

EMDASH = "\u2014"  # escaped, so a grep over *.py stays clean too

ROOT = Path(__file__).resolve().parent
FRAGS = ROOT / "build" / "fragments"
SHELL = ROOT / "build" / "shell.html"
SVGDIR = ROOT / "build" / "svg"
LEDGER = ROOT / "research" / "fact-ledger.md"
MANIFEST = ROOT / "assets" / "image-manifest.md"
BUILDER_JSON = ROOT / "build" / "data" / "builder-table.json"
OUT_GUIDE = ROOT / "new-construction-buyer-guide.html"
OUT_SOURCES = ROOT / "sources-and-citations.html"

PAGES = 39                # content pages, from guide-outline.md
APPENDIX_PER_PAGE = 42    # measured, not estimated. Two renders gave 88 rows
                          # overflowing by 870px and 24 rows leaving 520px, which
                          # solves to ~43px per row per column and ~23 rows per
                          # column. 42 leaves the first page room for its lede.
VERIFIED = "July 25, 2026"
FRAGMENT_MARKER = "<!-- ===== FRAGMENTS ===== -->"

# Domain to organization, for the printed source strip. A reader glancing at the
# foot of a page should see WHO said it, which is the whole point of showing
# sources. Anything not listed falls back to its bare domain, which is honest but
# uglier, so add rows here rather than leaving fallbacks in the shipped guide.
ORGS = {
    "leg.state.nv.us": "Nevada Revised Statutes",
    "law.justia.com": "Nevada Revised Statutes",
    "law.cornell.edu": "Cornell Legal Information Institute",
    "red.nv.gov": "Nevada Real Estate Division",
    "doi.nv.gov": "Nevada Division of Insurance",
    "business.nv.gov": "Nevada Department of Business and Industry",
    "app.nvcontractorsboard.com": "Nevada State Contractors Board",
    "homeispossiblenv.org": "Nevada Housing Division",
    "nvrural.org": "Nevada Rural Housing",
    "nvbar.org": "State Bar of Nevada",
    "clarkcountynv.gov": "Clark County",
    "ebfiles.clarkcountynv.gov": "Clark County",
    "treasurer.co.clark.nv.us": "Clark County Treasurer",
    "cityofhenderson.com": "City of Henderson",
    "ccsd.net": "Clark County School District",
    "search.ccsd.net": "Clark County School District",
    "fhfa.gov": "Federal Housing Finance Agency",
    "entp.hud.gov": "HUD",
    "hud.gov": "HUD",
    "va.gov": "Department of Veterans Affairs",
    "benefits.va.gov": "Department of Veterans Affairs",
    "consumerfinance.gov": "Consumer Financial Protection Bureau",
    "selling-guide.fanniemae.com": "Fannie Mae",
    "freddiemac.com": "Freddie Mac",
    "fred.stlouisfed.org": "Federal Reserve Bank of St. Louis",
    "nar.realtor": "National Association of Realtors",
    "bbb.org": "Better Business Bureau",
    "lifestoryresearch.com": "Lifestory Research",
    "zondahome.com": "Zonda",
    "reviewjournal.com": "Las Vegas Review-Journal",
    "vegasinc.lasvegassun.com": "Las Vegas Sun",
    "businesspress.vegas": "Las Vegas Business Press",
    "nevadabusiness.com": "Nevada Business Magazine",
    "fox5vegas.com": "FOX5 Las Vegas",
    "globenewswire.com": "GlobeNewswire",
    "builderonline.com": "Builder Magazine",
    "custombuilderonline.com": "Custom Builder",
    "nevadabuilders.org": "Southern Nevada Home Builders Association",
    "amgnv.com": "Association Management Group",
    "communities.howardhughes.com": "Howard Hughes",
    "summerlin.com": "Summerlin",
    "skyecanyon.com": "Skye Canyon",
    "cadencenv.com": "Cadence",
    "mymountainsedge.com": "Mountain's Edge",
    "valleyvistanlv.org": "Valley Vista",
}

BUILDER_DOMAINS = {
    "lennar.com": "Lennar",
    "resourcecenter.lennar.com": "Lennar",
    "kbhome.com": "KB Home",
    "drhorton.com": "D.R. Horton",
    "richmondamerican.com": "Richmond American",
    "pulte.com": "Pulte",
    "beazer.com": "Beazer",
    "lgihomes.com": "LGI Homes",
    "centurycommunities.com": "Century Communities",
    "tripointehomes.com": "Tri Pointe Homes",
    "taylormorrison.com": "Taylor Morrison",
    "tollbrothers.com": "Toll Brothers",
    "cdn.tollbrothers.com": "Toll Brothers",
    "tollbrothersmortgage.com": "Toll Brothers Mortgage",
    "blueheron.com": "Blue Heron",
    "woodsidehomes.com": "Woodside Homes",
    "signaturehomes.com": "Signature Homes",
    "touchstoneliving.com": "Touchstone Living",
    "storybooknewhomes.com": "Storybook Homes",
    "christopherhomes.com": "Christopher Homes",
    "harmonyhomes.com": "Harmony Homes",
    "edwardhomesnv.com": "Edward Homes",
    "landonmillerhomes.com": "Landon Miller Homes",
    "meritagehomes.com": "Meritage Homes",
    "investors.meritagehomes.com": "Meritage Homes",
    "trusthomebuildersnv.com": "Trust Home Builders",
    "pinnaclelv.com": "Pinnacle Homes",
}
ORGS.update(BUILDER_DOMAINS)


def die(msg):
    sys.exit(f"assemble.py: {msg}")


def domain(url):
    d = urlparse(url).netloc.lower()
    return d[4:] if d.startswith("www.") else d


def org_of(url):
    d = domain(url)
    return ORGS.get(d, d)


def load_ledger():
    """claim-id -> dict. The ledger is the only source of truth for a number."""
    claims = OrderedDict()
    for line in LEDGER.read_text().split("\n"):
        if not line.startswith("| "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6:
            continue
        cid = cells[0]
        if not re.fullmatch(r"[a-z]{3,5}-[a-z0-9-]+", cid):
            continue
        claims[cid] = {
            "id": cid,
            "statement": cells[1],
            "value": cells[2],
            "url": cells[3],
            "verified": cells[4],
            "confidence": cells[5],
        }
    if not claims:
        die("parsed zero claims out of the fact ledger")
    return claims


ALT_ROW = re.compile(r"^\|\s*`([a-z0-9\-]+\.jpg)`\s*\|\s*(.+?)\s*\|\s*$", re.M)


def load_alt():
    """
    filename -> alt text, from the manifest's canonical table.

    Single-sourced because nine of the fifteen images appear on more than one page
    and three writers each authored their own wording for the same file. Without
    this the guide ships one photograph described three different ways.
    """
    alts = dict(ALT_ROW.findall(MANIFEST.read_text()))
    if len(alts) < 10:
        die(
            "image-manifest.md has no canonical alt text table, or it did not parse. "
            "Expected rows of the form: | `open-core.jpg` | description |"
        )
    return alts


IMG_RE = re.compile(r'(<img\s[^>]*?src="assets/img/([a-z0-9\-]+\.jpg)"[^>]*?>)')
ALT_ATTR = re.compile(r'\salt="[^"]*"')


def apply_alt(html, alts, unknown):
    """Overwrite every alt on a guide photograph with the manifest's wording."""
    def sub(m):
        tag, fname = m.group(1), m.group(2)
        if fname not in alts:
            unknown.add(fname)
            return tag
        stripped = ALT_ATTR.sub("", tag)
        return stripped[:-1].rstrip() + f' alt="{alts[fname]}">'

    return IMG_RE.sub(sub, html)


# Builder table footnotes, p32 to p35. These are a separate numbering run from the
# ledger citations, they are written as [12] rather than a superscript, and they
# come from builder-table.json rather than the fact ledger. Kept separate because
# the table reports on named companies and its numbering has to match
# builder-table.md, which is the file a reader would be handed in a dispute.
BRACKET_RE = re.compile(r"\[(\d{1,3})\]")


def load_builder_footnotes():
    data = json.loads(BUILDER_JSON.read_text())
    fns = {int(f["n"]): f for f in data.get("footnotes", [])}
    if not fns:
        die("builder-table.json carries no footnotes[]")
    return fns


def collect_brackets(pages, fns):
    """page -> sorted footnote numbers cited there. Fails on an unknown number."""
    per_page = {}
    unknown = []
    for pageno, html in pages:
        if pageno < 32 or pageno > 35:
            continue
        nums = sorted({int(n) for n in BRACKET_RE.findall(html)})
        for n in nums:
            if n not in fns:
                unknown.append((pageno, n))
        if nums:
            per_page[pageno] = nums
    if unknown:
        lines = "\n".join(f"    p{p:02d}  [{n}]" for p, n in unknown)
        die(
            "builder table cites a footnote number that is not in "
            f"builder-table.json:\n{lines}"
        )
    return per_page


def read_fragments():
    frags = []
    missing = []
    for n in range(1, PAGES + 1):
        f = FRAGS / f"p{n:02d}.html"
        if not f.exists():
            missing.append(f.name)
            continue
        frags.append((n, f.read_text().strip()))
    return frags, missing


def inline_svgs(html, used):
    """Replace <!-- SVG-NN --> with the diagram markup, verbatim."""
    def sub(m):
        sid = m.group(1)
        path = SVGDIR / f"svg-{sid}.svg"
        if not path.exists():
            die(f"fragment references SVG-{sid} but {path.name} does not exist")
        used.add(sid)
        return path.read_text().strip()

    return re.sub(r"<!--\s*SVG-(\d{2})\s*-->", sub, html)


SUP_RE = re.compile(
    r'<sup class="src" data-claim="([a-z0-9-]+)"\s*>\s*\*?\s*</sup>'
)


def number_citations(pages, claims):
    """
    Global sequential numbering in document order, and the per-page marker map.
    Returns (pages, order) where order is the numbered citation list.
    """
    order = []          # [(number, claim-id, page)]
    seen = {}           # claim-id -> number, so a repeat cites the same footnote
    per_page = {}       # page -> [numbers]
    unknown = []

    out = []
    for pageno, html in pages:
        nums = []

        def sub(m):
            cid = m.group(1)
            if cid not in claims:
                unknown.append((pageno, cid))
                return m.group(0)
            if cid in seen:
                n = seen[cid]
            else:
                n = len(order) + 1
                seen[cid] = n
                order.append((n, cid, pageno))
            nums.append(n)
            return f'<sup class="src">{n}</sup>'

        html = SUP_RE.sub(sub, html)
        per_page[pageno] = nums
        out.append((pageno, html))

    if unknown:
        lines = "\n".join(f"    p{p:02d}  {c}" for p, c in sorted(set(unknown)))
        die(
            "citation refers to a claim-id that is not in the fact ledger.\n"
            "  Nothing ships with an unverifiable number, so this is a hard stop.\n"
            f"{lines}"
        )
    return out, order, per_page


def srcnote_text(nums, order_by_num, claims):
    """One line: marker range, the organizations, the verified date."""
    if not nums:
        return ""
    lo, hi = min(nums), max(nums)
    rng = f"Source {lo}" if lo == hi else f"Sources {lo} to {hi}"

    orgs = []
    for n in sorted(set(nums)):
        o = org_of(claims[order_by_num[n]]["url"])
        if o not in orgs:
            orgs.append(o)
    # Three organizations is the most that fits on one line at 6.9pt across 6.6in.
    if len(orgs) > 3:
        shown = ", ".join(orgs[:3])
        tail = f", and {len(orgs) - 3} more"
    else:
        shown = ", ".join(orgs)
        tail = ""
    return (
        f"{rng}: {shown}{tail}. Verified {VERIFIED}. "
        f"Every URL is in the companion source list."
    )


SRCNOTE_RE = re.compile(
    r'(<span class="srcnote"[^>]*\bdata-srcnote\b[^>]*>)(.*?)(</span>)', re.S
)


def builder_srcnote_text(nums):
    """
    The p32 to p35 strip. Writer 3 measured the alternative: about 45 unique
    footnotes across p33 and p34 is roughly 1.4 Letter pages of URLs at 7pt, on
    two pages already sitting at their 400 word ceiling. So the dates print in the
    table and the addresses route to the companion, which is the same two tier
    scheme the rest of the guide already uses. Every cell still resolves to a web
    address and a date, or to NOT FOUND.
    """
    if not nums:
        return ""
    lo, hi = min(nums), max(nums)
    rng = f"Builder footnote {lo}" if lo == hi else f"Builder footnotes {lo} to {hi}"
    return (
        f"{rng} on this page each resolve to a web address and the date I checked "
        f"it, in the companion source list. Verified {VERIFIED}."
    )


def fill_srcnotes(pages, per_page, order, claims, builder_per_page=None):
    order_by_num = {n: cid for n, cid, _ in order}
    builder_per_page = builder_per_page or {}
    out = []
    unfilled = []
    for pageno, html in pages:
        text = srcnote_text(per_page.get(pageno, []), order_by_num, claims)
        btext = builder_srcnote_text(builder_per_page.get(pageno, []))
        if btext:
            text = f"{text} {btext}".strip() if text else btext
        found = [False]

        def sub(m):
            found[0] = True
            return m.group(1).replace(" data-srcnote", "") + text + m.group(3)

        html = SRCNOTE_RE.sub(sub, html)
        if not found[0] and (per_page.get(pageno) or builder_per_page.get(pageno)):
            unfilled.append(pageno)
        out.append((pageno, html))
    if unfilled:
        die(
            "these pages carry citations but have no "
            '<span class="srcnote" data-srcnote></span> for the strip: '
            + ", ".join(f"p{p:02d}" for p in unfilled)
        )
    return out


SOURCES_HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Source List | Before You Walk Into the Model Home</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900&family=Archivo:ital,wdth,wght@0,62..125,100..900&display=swap" rel="stylesheet">
<style>
:root{ --paper:#F7F5F0; --ink:#1C2436; --muted:#5F5A52; --rule:#847B6D;
  --navy-700:#2C3F6B; --navy-800:#28375A; --paper-2:#EDE9E0; --clay:#B8360F;
  --tint-clay:#FBE5DA;
  --display:"Bodoni Moda",Georgia,serif; --text:"Archivo","Helvetica Neue",Arial,sans-serif; }
*{ box-sizing:border-box; }
html{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }
body{ margin:0; background:var(--paper); color:var(--ink); font-family:var(--text); }
.wrap{ max-width:8.5in; margin:0 auto; padding:.55in; }
h1{ font-family:var(--display); font-weight:700; font-size:30pt; line-height:1.04;
  letter-spacing:-.008em; margin:0 0 10pt; }
.lede{ font:400 11pt/1.55 var(--text); max-width:34em; margin:0 0 8pt; }
.meta{ font:600 8.4pt/1.5 var(--text); color:var(--muted); margin:0 0 22pt;
  padding-bottom:12pt; border-bottom:2.4pt solid var(--ink); }
h2{ font-family:var(--display); font-weight:700; font-size:15pt; letter-spacing:-.008em;
  margin:26pt 0 8pt; padding-top:10pt; border-top:.75pt solid var(--rule); }
table{ width:100%; border-collapse:collapse; table-layout:fixed; }
caption{ caption-side:top; text-align:left; font:700 7.4pt/1.3 var(--text);
  color:var(--muted); padding:0 0 5pt; }
th[scope=col]{ background:var(--navy-800); color:var(--paper);
  font:800 6.8pt/1 var(--text); letter-spacing:.05em; text-transform:uppercase;
  text-align:left; padding:7pt 6pt; }
td{ font:400 8.4pt/1.45 var(--text); padding:5pt 6pt; vertical-align:top;
  word-break:break-word; }
tbody tr:nth-child(even){ background:var(--paper-2); }
td.num{ font-weight:800; font-variant-numeric:tabular-nums; width:2.6em; color:var(--navy-700); }
td.pg{ font-weight:700; font-variant-numeric:tabular-nums; width:3.2em; }
td.cid{ font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:7.4pt;
  color:var(--muted); width:11em; }
td.url{ width:17em; }
td.url a{ color:var(--clay); }
.foot{ margin-top:28pt; padding-top:12pt; border-top:2.4pt solid var(--ink);
  font:500 8.4pt/1.6 var(--text); color:var(--muted); }
.foot b{ color:var(--ink); }
@page{ size:letter; margin:.5in; }
@media print{ body{ background:#FFFFFF; } .wrap{ padding:0; } tr{ break-inside:avoid; } }
</style>
</head>
<body>
<div class="wrap">
"""


def builder_section(builder_per_page, fns):
    """The p32 to p35 footnote run, its own numbering, grouped by page."""
    if not builder_per_page:
        return []
    parts = [
        "<h2>Builder comparison table, pages 32 to 35</h2>",
        '<p class="lede">These are a separate numbering run, written in the guide as '
        "a bracketed number like [12], and they match the numbering in my working "
        "file <b>builder-table.md</b> so the two never disagree. A cell marked "
        "<b>NOT FOUND</b> means I looked and could not verify it from a primary "
        "source. It is not an estimate.</p>",
    ]
    for pageno in sorted(builder_per_page):
        nums = builder_per_page[pageno]
        parts.append(f"<h2>Page {pageno}, builder footnotes</h2>")
        parts.append(
            f"<table><caption>Builder table footnotes cited on page {pageno}.</caption>"
            '<thead><tr><th scope="col">No.</th><th scope="col">Source</th>'
            '<th scope="col">Verified</th></tr></thead><tbody>'
        )
        for n in nums:
            f = fns[n]
            url = f.get("url", "")
            cell = (
                f'<a href="{url}">{org_of(url)}</a><br>'
                f'<span style="font-size:7pt">{url}</span>'
                if url.startswith("http")
                else (url or "NOT FOUND")
            )
            parts.append(
                f'<tr><td class="num">[{n}]</td><td class="url">{cell}</td>'
                f'<td class="pg">{f.get("verified", "")}</td></tr>'
            )
        parts.append("</tbody></table>")
    return parts


APPENDIX_ALT = (
    "The Mojave desert at sunrise, low warm light raking across sand and creosote, "
    "a quiet mountain range on the horizon."
)


def marker_run(nums):
    """
    "12, 13, 14, 19" prints as "12 to 14, 19". A statute page can back nine
    consecutive markers and the run notation saves a line per row.
    """
    ints = sorted({n for n in nums if isinstance(n, int)})
    others = [str(n) for n in nums if not isinstance(n, int)]
    out, i = [], 0
    while i < len(ints):
        j = i
        while j + 1 < len(ints) and ints[j + 1] == ints[j] + 1:
            j += 1
        out.append(str(ints[i]) if j == i else f"{ints[i]} to {ints[j]}")
        i = j + 1
    return ", ".join(out + others)


def appendix_entry(markers, org, url, verified):
    """One row per unique source address."""
    run = marker_run(markers)
    if not url or not url.startswith("http"):
        return (
            f'<li><span class="sn">{run}</span>'
            f'<span class="sv">{org or "source"}</span> '
            f'<span class="snf">NOT FOUND</span></li>'
        )
    return (
        f'<li><span class="sn">{run}</span>'
        f'<span class="sv">{org}</span><br>'
        f'<span class="su">{url}</span> '
        f'<span class="sd">verified {verified}</span></li>'
    )


def build_appendix(order, claims, builder_per_page, fns, first_page, per_page_cap):
    """
    Generate the source appendix as real .page fragments, so the guide is
    self-contained and a reader holding the PDF can check any number without
    leaving it. Returns [(pageno, html), ...].
    """
    # ONE ROW PER UNIQUE SOURCE, not per marker.
    #
    # 364 markers cite only 164 distinct addresses, because a single statute page
    # or program page backs many separate claims. Printing a row per marker
    # repeated the same URL up to nine times and ran to 13 pages. Grouping by
    # address is both shorter and more useful: the reader sees every number a
    # given source backs, and the specific value still sits in the body of the
    # guide next to its marker.
    by_url = OrderedDict()
    for n, cid, guide_page in order:
        c = claims[cid]
        by_url.setdefault(c["url"], {"markers": [], "verified": c["verified"]})
        by_url[c["url"]]["markers"].append(n)

    entries = []
    for url, rec in by_url.items():
        entries.append(appendix_entry(
            markers=rec["markers"], org=org_of(url), url=url, verified=rec["verified"]
        ))

    # The builder table's own numbering run, grouped the same way and kept last so
    # it reads as the separate run that it is.
    b_by_url = OrderedDict()
    for pageno in sorted(builder_per_page):
        for bn in builder_per_page[pageno]:
            f = fns[bn]
            u = f.get("url", "")
            b_by_url.setdefault(u, {"markers": [], "verified": f.get("verified", "")})
            b_by_url[u]["markers"].append(f"[{bn}]")

    builder_entries = [
        appendix_entry(markers=rec["markers"], org=org_of(u), url=u,
                       verified=rec["verified"])
        for u, rec in b_by_url.items()
    ]

    all_entries = entries + builder_entries
    chunks = [
        all_entries[i:i + per_page_cap]
        for i in range(0, len(all_entries), per_page_cap)
    ]

    pages = []
    total = len(chunks)
    for i, chunk in enumerate(chunks):
        pageno = first_page + i
        foot = "foot-r" if pageno % 2 == 0 else "foot-l"
        folio = f'<span class="folio">{pageno}</span>'
        note = (
            '<span class="srcnote">Every value on this page was verified '
            f"{VERIFIED}. Programs, limits and builder terms move, so check the "
            "date before you rely on a number.</span>"
        )
        footinner = f"{note}{folio}" if foot == "foot-l" else f"{folio}{note}"

        lede = ""
        if i == 0:
            lede = (
                '<p class="appx-lede">Every numbered marker in this guide resolves '
                "here, with the address I found it at and the date I checked it. "
                "<b>If a number matters to your decision, look it up and then check "
                "it yourself.</b> A source with no date on it is not a source.</p>"
            )
        pages.append((pageno, f"""<div class="page gp" id="p{pageno}">
  <div class="body">
    <div class="band">
      <img src="assets/img/open-back.jpg" alt="{APPENDIX_ALT}">
      <div class="tone"></div>
      <div class="head">
        <span class="rh-a">Sources, {i + 1} of {total}</span>
        <span class="rh-b">Where every number came from</span>
      </div>
    </div>
    <div class="pad" style="padding-top:14pt">
      {lede}
      <ol class="srclist">
{chr(10).join("        " + e for e in chunk)}
      </ol>
    </div>
  </div>
  <div class="foot {foot}">{footinner}</div>
</div>"""))
    return pages


def write_sources(order, claims, per_page, builder_per_page=None, fns=None):
    """
    The companion source list. Generated, never authored, so it cannot drift from
    the ledger. Grouped by guide page, because a reader arrives here holding a
    page number and a marker number.
    """
    by_page = {}
    for n, cid, pageno in order:
        by_page.setdefault(pageno, []).append((n, cid))

    parts = [SOURCES_HEAD]
    parts.append("<h1>Every source in this guide</h1>")
    parts.append(
        '<p class="lede">This is the companion source list for '
        "<b>Before You Walk Into the Model Home</b>. Every numbered marker in the "
        "guide appears here with the claim it supports, the value, the full web "
        "address, and the date I checked it.</p>"
    )
    parts.append(
        '<p class="lede">If a number in the guide matters to your decision, look it '
        "up here and then check it against the source yourself. Programs, limits, "
        "and builder terms change. A dated source tells you when to stop trusting "
        "it.</p>"
    )
    parts.append(
        f'<p class="meta">{len(order)} sources across {len(by_page)} pages. '
        f"Every value verified {VERIFIED}.<br>"
        "Ryan Rose &middot; Real Broker, LLC &middot; Nevada license S.0185572 "
        "&middot; 702-747-5921 &middot; ryan@rosehomeslv.com</p>"
    )

    for pageno in sorted(by_page):
        rows = by_page[pageno]
        parts.append(f"<h2>Page {pageno}</h2>")
        parts.append(
            f'<table><caption>Sources cited on page {pageno} of the guide.</caption>'
            "<thead><tr>"
            '<th scope="col">No.</th>'
            '<th scope="col">What it supports</th>'
            '<th scope="col">Value</th>'
            '<th scope="col">Source</th>'
            '<th scope="col">Claim id</th>'
            "</tr></thead><tbody>"
        )
        for n, cid in rows:
            c = claims[cid]
            url = c["url"]
            link = (
                f'<a href="{url}">{org_of(url)}</a><br>'
                f'<span style="font-size:7pt">{url}</span><br>'
                f'<span style="font-size:7pt">verified {c["verified"]}</span>'
                if url.startswith("http")
                else url
            )
            parts.append(
                f'<tr><td class="num">{n}</td>'
                f"<td>{c['statement']}</td>"
                f"<td>{c['value']}</td>"
                f'<td class="url">{link}</td>'
                f'<td class="cid">{cid}</td></tr>'
            )
        parts.append("</tbody></table>")

    parts.extend(builder_section(builder_per_page or {}, fns or {}))

    parts.append(
        '<p class="foot">Nothing in this list is my opinion. Each row is a statement '
        "I found in a primary source, with the address and the date. Where a source "
        "reports on a named company, that is a third-party finding, not a judgment "
        "of mine, and you should verify its current status before relying on it."
        "<br><br>"
        "<b>Ryan Rose</b> &middot; Real Broker, LLC &middot; Nevada license "
        "S.0185572<br>702-747-5921 &middot; ryan@rosehomeslv.com &middot; "
        "rosehomeslv.com</p>"
    )
    parts.append("</div>\n</body>\n</html>\n")

    html = "\n".join(parts)
    if EMDASH in html:
        die("em-dash in the generated source list, refusing to write")
    OUT_SOURCES.write_text(html)
    return html


def main():
    claims = load_ledger()
    frags, missing = read_fragments()

    if not frags:
        die(f"no fragments found in {FRAGS.relative_to(ROOT)}. Nothing to assemble.")
    if missing:
        print(f"WARNING: {len(missing)} fragments missing: {', '.join(missing)}")
        print("         assembling a partial guide. Page count will not be 39.")

    alts = load_alt()
    fns = load_builder_footnotes()

    used_svgs = set()
    unknown_imgs = set()
    frags = [(n, inline_svgs(h, used_svgs)) for n, h in frags]
    frags = [(n, apply_alt(h, alts, unknown_imgs)) for n, h in frags]
    if unknown_imgs:
        die(
            "fragment references a photograph with no canonical alt text in "
            "assets/image-manifest.md: " + ", ".join(sorted(unknown_imgs))
        )

    builder_per_page = collect_brackets(frags, fns)
    frags, order, per_page = number_citations(frags, claims)
    frags = fill_srcnotes(frags, per_page, order, claims, builder_per_page)

    appendix = build_appendix(
        order, claims, builder_per_page, fns,
        first_page=PAGES + 1, per_page_cap=APPENDIX_PER_PAGE,
    )
    frags = frags + appendix

    shell = SHELL.read_text()
    if FRAGMENT_MARKER not in shell:
        die("shell.html has no fragment marker. Re-run build-shell.py.")

    body = "\n\n".join(
        f"<!-- ================= p{n:02d} ================= -->\n{h}"
        for n, h in frags
    )
    guide = shell.replace(FRAGMENT_MARKER, body)

    # mechanical gates, the ones that are cheap to check here rather than in QA
    if EMDASH in guide:
        bad = [
            f"p{n:02d}" for n, h in frags if EMDASH in h
        ]
        die(f"em-dash in the assembled guide. Offending fragments: {', '.join(bad)}")
    if re.search(r"position\s*:\s*fixed", guide):
        die("position:fixed in the assembled guide, which repeats on every printed page")
    for ent in ("&mdash;", "&#8212;", "&#x2014;"):
        if ent in guide:
            die(f"HTML entity {ent} in the assembled guide")

    OUT_GUIDE.write_text(guide)
    sources = write_sources(order, claims, per_page, builder_per_page, fns)

    all_svgs = {p.stem.split("-")[1] for p in SVGDIR.glob("svg-*.svg")}
    unused = sorted(all_svgs - used_svgs)

    print(f"wrote {OUT_GUIDE.name}")
    print(f"      {len(frags)} of {PAGES} pages, {len(guide.splitlines())} lines")
    print(f"      {len(order)} citations, {len(set(c for _, c, _ in order))} unique claim-ids")
    print(f"      {len(used_svgs)} of {len(all_svgs)} diagrams inlined"
          + (f", unused: {', '.join(unused)}" if unused else ""))
    nb = sum(len(v) for v in builder_per_page.values())
    print(f"      {nb} builder footnote references across "
          f"{len(builder_per_page)} pages")
    print(f"      alt text normalised from the manifest on "
          f"{len(IMG_RE.findall(guide))} photographs")
    print(f"wrote {OUT_SOURCES.name}")
    print(f"      {len(sources.splitlines())} lines")

    if missing:
        print(f"\nINCOMPLETE: still waiting on {', '.join(missing)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
