#!/usr/bin/env python3
"""
Geo spoke page generator.

    python3 build.py summerlin          # build one area
    python3 build.py --all              # build every area that has a content.json

Reads  geo-spokes/<area>/content.json
Writes geo-spokes/<area>/part-1-above-listings.html
       geo-spokes/<area>/part-2-below-listings.html
       geo-spokes/<area>/_preview-stitched.html   (local preview only, never paste)
       geo-spokes/<area>/0-seo-fields.txt

The CSS and the rail/spy script are NOT copied into this file. They are read from the live
hub's part-1 at build time, so a fix to the hub system flows into every spoke on the next
build. The builder registry (name, brand color, tier, slug) is read from the hub's builder
grid for the same reason.

The build FAILS (exit 1) on: em-dashes, unknown builder keys, duplicate ids, an inline
<form>, a meta title over 48 chars (Lofty appends " | Ryan Rose"), a description over 160.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent            # geo-spokes/
HUB = ROOT.parent / "new-construction-hub" / "part-1-above-listings.html"
SITE = "https://www.rosehomeslv.com"
HUB_SLUG = "las-vegas-new-construction"

AREAS = [  # order used for the "other areas" pills
    ("summerlin", "Summerlin"),
    ("henderson", "Henderson"),
    ("north-las-vegas", "North Las Vegas"),
    ("southwest-las-vegas", "Southwest Las Vegas"),
    ("skye-canyon", "Skye Canyon"),
    ("centennial-hills", "Centennial Hills"),
    ("lake-las-vegas", "Lake Las Vegas"),
]
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700;800'
         '&family=Inter:wght@400;500;600;700&family=Raleway:wght@400;500;600;700&display=swap" '
         'rel="stylesheet">')

errors = []


def fail(msg):
    errors.append(msg)


# ------------------------------------------------------------------ hub system
def load_hub():
    src = HUB.read_text()
    style = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
    scripts = re.findall(r"<script>(.*?)</script>", src, re.S)
    escape_js = scripts[0].replace("#faf8f3", "#FFFFFF")   # Vector: no warm surfaces
    page_js = scripts[1]
    # the hub's code comments use em-dashes; keep shipped files clean of them entirely
    style, escape_js, page_js = (s.replace(" \u2014 ", ", ").replace("\u2014", ",")
                                 for s in (style, escape_js, page_js))
    builders = {}
    for m in re.finditer(
            r'<li class="rh-builder" data-tier="(\w+)" style="--b:(#[0-9A-Fa-f]{6})">\s*'
            r'<h3>(.*?)</h3>.*?href="/([a-z0-9-]+)"', src, re.S):
        tier, color, name, slug = m.groups()
        key = slug.replace("-las-vegas", "")
        builders[key] = {"tier": tier, "color": color, "name": name, "slug": slug}
    if len(builders) != 20:
        fail(f"hub builder registry parsed {len(builders)} builders, expected 20")
    return style, escape_js, page_js, builders


# ------------------------------------------------------------------ blocks
def esc(s):
    return html.escape(s, quote=True)


def render_blocks(blocks, builders, ind="          "):
    out = []
    for b in blocks:
        (kind, val), = b.items()
        if kind == "p":
            out.append(f"{ind}<p>{val}</p>")
        elif kind == "lede":
            out.append(f'{ind}<p class="rh-lede">{val}</p>')
        elif kind == "h3":
            out.append(f"{ind}<h3>{val}</h3>")
        elif kind in ("ul", "ol"):
            items = "\n".join(f"{ind}  <li>{li}</li>" for li in val)
            out.append(f"{ind}<{kind}>\n{items}\n{ind}</{kind}>")
        elif kind == "facts":
            rows = "\n".join(f"{ind}  <strong>{k}:</strong> {v}<br>" for k, v in val)
            rows = rows[: rows.rfind("<br>")]
            out.append(f'{ind}<p class="rh-areafacts">\n{rows}\n{ind}</p>')
        elif kind == "table":
            head = "".join(f"<th>{h}</th>" for h in val["head"])
            body = "\n".join(
                f"{ind}          <tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
                for r in val["rows"])
            note = (f'\n{ind}  <p class="rh-tablenote">{val["note"]}</p>' if val.get("note") else "")
            out.append(
                f'{ind}<div class="rh-wide">\n{ind}  <div class="rh-tablewrap">\n'
                f'{ind}    <table class="rh-table">\n{ind}      <thead><tr>{head}</tr></thead>\n'
                f'{ind}      <tbody>\n{body}\n{ind}      </tbody>\n{ind}    </table>\n'
                f'{ind}  </div>{note}\n{ind}</div>')
        elif kind == "builders":
            cards = []
            for item in val["cards"]:
                k = item["key"]
                if k not in builders:
                    fail(f"unknown builder key '{k}'")
                    continue
                r = builders[k]
                cards.append(
                    f'{ind}    <li class="rh-builder" data-tier="{r["tier"]}" style="--b:{r["color"]}">\n'
                    f'{ind}      <h3>{r["name"]}</h3><span class="rh-builder__tier">{r["tier"].title()}</span>\n'
                    f'{ind}      <p class="rh-builder__note">{item["note"]}</p>\n'
                    f'{ind}      <a class="rh-builder__link" href="/{r["slug"]}">View builder page &rarr;</a>\n'
                    f'{ind}    </li>')
            note = (f'\n{ind}  <p class="rh-tablenote" style="margin-top:16px;">{val["note"]}</p>'
                    if val.get("note") else "")
            out.append(f'{ind}<div class="rh-wide">\n{ind}  <ul class="rh-builders">\n'
                       + "\n".join(cards) + f"\n{ind}  </ul>{note}\n{ind}</div>")
        elif kind == "pills":
            pills = "\n".join(f'{ind}  <a class="rh-pill" href="{h}">{t}</a>' for t, h in val)
            out.append(f'{ind}<div class="rh-pills">\n{pills}\n{ind}</div>')
        elif kind == "note":
            out.append(f'{ind}<p class="rh-tablenote">{val}</p>')
        elif kind == "html":
            out.append(val)
        else:
            fail(f"unknown block type '{kind}'")
    return "\n".join(out)


def render_sections(sections, builders):
    out = []
    for s in sections:
        out.append(f'\n          <h2 id="{s["id"]}">{s["h2"]}</h2>')
        out.append(render_blocks(s["blocks"], builders))
    return "\n".join(out)


def rail(toc, title_id):
    items = "\n".join(f'              <li><a href="#{i}">{t}</a></li>' for i, t in toc)
    return f'''        <!-- ---------- STICKY TOC RAIL ---------- -->
        <aside class="rh-rail">
          <nav class="rh-toc" aria-labelledby="{title_id}">
            <p class="rh-toc__title" id="{title_id}">On This Page</p>
            <div class="rh-toc__progress" aria-hidden="true"><span class="rh-toc__progress-fill"></span></div>
            <div class="rh-toc__scroll">
            <ol class="rh-toc__list">
{items}
            </ol>
            </div><!-- /.rh-toc__scroll -->
            <a class="rh-btn rh-btn--primary rh-btn--sm rh-toc__cta" href="#contact">{esc_text("Talk to Ryan")}</a>
          </nav>
        </aside>'''


def esc_text(s):
    return s


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def header_comment(c, part):
    where = "ABOVE" if part == 1 else "BELOW"
    return f'''<!-- ================================================================
     ROSE HOMES LV, {c["area"].upper()} NEW CONSTRUCTION, PART {part} of 2 ({where} the featured listings)
     Page: {SITE}/{c["slug"]}
     Paste into the Lofty HTML / custom code module {where}
     the Featured Listings block you build in Lofty's editor.

     GENERATED FILE. Do not hand-edit. Edit geo-spokes/{c["folder"]}/content.json
     and run: python3 geo-spokes/_build/build.py {c["folder"]}
     CSS and script come from new-construction-hub/part-1-above-listings.html.

     Design tokens: SKOOL Brandkit "Vector" v2.0.
     ================================================================ -->'''


# ------------------------------------------------------------------ page
def build(folder, style, escape_js, page_js, builders):
    c = json.loads((ROOT / folder / "content.json").read_text())
    c["folder"] = folder
    area, slug = c["area"], c["slug"]
    url = f"{SITE}/{slug}"

    p1_sections = c["part1_sections"]
    p2_sections = c["part2_sections"]
    other = [(n, f"/{a}-new-construction") for a, n in AREAS if a != folder]

    toc = ([(s["id"], s["toc"]) for s in p1_sections]
           + [("listings", "Homes for sale now")]
           + [(s["id"], s["toc"]) for s in p2_sections]
           + [("faq", "Questions and answers"), ("other-areas", "Other areas"), ("sources", "Sources")])

    stats = "\n".join(
        f'''          <div>
            <span class="rh-stat__num">{n}</span>
            <span class="rh-stat__label">{l}</span>
          </div>''' for n, l in c["hero"]["stats"])
    takeaways = "\n".join(f"          <li>{t}</li>" for t in c["takeaways"])
    img = c["hero"]["image"]

    # ---------------- PART 1
    p1_body = f'''<div class="nc-hub">

  <!-- ============ BREADCRUMB ============ -->
  <div class="rh-crumb">
    <div class="rh-container">
      <a href="{SITE}/">Home</a> &rsaquo; <a href="/{HUB_SLUG}">New Construction</a> &rsaquo; {area}
    </div>
  </div>

  <!-- ============ HERO (white, photo dissolves in from the right, see hub CLAUDE.md) ============ -->
  <header class="rh-hero">

    <figure class="rh-hero__media">
      <img src="{img["src"]}"
           alt="{esc(img["alt"])}"
           width="{img["width"]}" height="{img["height"]}" loading="eager" fetchpriority="high" decoding="async">
    </figure>

    <div class="rh-container rh-hero__inner">
      <div class="rh-hero__panelInner">
        <p class="rh-hero__kicker">{c["hero"]["kicker"]}</p>
        <h1>{c["hero"]["h1"]}</h1>
        <p class="rh-hero__sub">
          {c["hero"]["sub"]}
        </p>

        <div class="rh-hero__stats">
{stats}
        </div>

        <div class="rh-hero__cta">
          <a class="rh-btn rh-btn--primary" href="#listings">See homes for sale</a>
          <a class="rh-btn rh-btn--ghost" href="#{p1_sections[0]["id"]}">{c["hero"].get("secondary_cta", "Browse communities")}</a>
          <a class="rh-btn rh-btn--ghost" href="#contact">Talk to Ryan</a>
        </div>
      </div>
    </div>
  </header>

  <!-- ============ ARTICLE ZONE, PART 1 ============ -->
  <section class="rh-section rh-section--base" id="guide">
    <div class="rh-container">
      <div class="rh-article-shell">

        <!-- ---------- PROSE COLUMN ---------- -->
        <div class="rh-prose">

      <blockquote class="rh-answer" id="answer" aria-label="Direct answer summary">
        <p>
          {c["answer"]}
        </p>
      </blockquote>

      <div class="rh-takeaways">
        <h3>What to know first</h3>
        <ol>
{takeaways}
        </ol>
      </div>

      <p class="rh-byline">
        By <strong>Ryan Rose</strong>, Real Broker, LLC, Nevada license S.018852
        &middot; Updated <time datetime="{c["updated_iso"]}">{c["updated_text"]}</time>
        &middot; About a {c["read_minutes"]} minute read
      </p>
{render_sections(p1_sections, builders)}

        </div><!-- /.rh-prose -->

{rail(toc, "rh-toc-title")}
      </div><!-- /.rh-article-shell -->
    </div>
  </section>

  <!-- ============ LIVE LISTINGS SLOT ============ -->
  <section class="rh-section rh-section--alt" id="listings">
    <div class="rh-container">
      <p class="rh-eyebrow">Homes for sale</p>
      <h2 style="font-family:var(--font-head);font-size:clamp(26px,3vw,38px);line-height:1.14;font-weight:800;letter-spacing:-.028em;margin:0 0 18px;">
        {c["listings"]["h2"]}
      </h2>
      <p class="rh-lede" style="max-width:68ch;">
        {c["listings"]["lede"]}
      </p>

      <!-- =================================================================
           END OF EMBED 1.

           Lofty's native Featured Listings block goes immediately BELOW this
           embed, then PART 2 goes below that.

           Filter for THIS page:
           {c["listings"]["lofty_filter"]}
           ================================================================= -->
    </div>
  </section>

</div><!-- /.nc-hub -->'''

    faq_html = "\n".join(
        f'''            <div class="rh-faq__item">
              <h3>{q}</h3>
              <p>{a}</p>
            </div>''' for q, a in c["faq"])
    sources_html = "\n".join(
        f'          <p class="rh-source">Source: <a href="{u}" rel="nofollow">{t}</a></p>'
        for t, u in c["sources"])
    pills_other = "\n".join(f'            <a class="rh-pill" href="{h}">{t}</a>' for t, h in other)

    # ---------------- PART 2
    p2_body = f'''<div class="nc-hub">

  <!-- ============ ARTICLE ZONE, PART 2 (rail resumes below the listings) ============ -->
  <section class="rh-section rh-section--base" id="guide-2">
    <div class="rh-container">
      <div class="rh-article-shell">

        <!-- ---------- PROSE COLUMN ---------- -->
        <div class="rh-prose">
{render_sections(p2_sections, builders)}

          <h2 id="faq">Questions about new construction in {area}</h2>
          <div class="rh-faq rh-wide">
{faq_html}
          </div>

          <h2 id="other-areas">Where else is new construction going up?</h2>
          <p>
            {area} is one of seven parts of the valley with steady new home building. The full guide
            compares all of them side by side, with prices, builders, and the buying process.
          </p>
          <div class="rh-pills">
            <a class="rh-pill" href="/{HUB_SLUG}">All Las Vegas new construction</a>
{pills_other}
          </div>

          <h2 id="sources">Sources and how this page is maintained</h2>
          <p>
            Every price and neighborhood on this page comes from a builder, the master plan
            developer, or a public agency, and the sources are listed below. Where a number could not
            be confirmed it was left out rather than guessed.
          </p>
          <p>
            Starting prices change with every release, and neighborhoods sell out. Treat the numbers
            here as a starting point, not a quote. This page was last reviewed in {c["reviewed_text"]}.
          </p>
{sources_html}
        </div><!-- /.rh-prose -->

{rail(toc, "rh-toc-title-2")}
      </div><!-- /.rh-article-shell -->
    </div>
  </section>

  <!-- ============ CTA BAND ============ -->
  <section class="rh-section rh-section--base" id="contact">
    <div class="rh-container">
      <div class="rh-band">
        <h2>{c["cta"]["h2"]}</h2>
        <p>
          {c["cta"]["p"]}
        </p>
        <a class="rh-btn rh-btn--primary" href="tel:7027475921">Call or text 702-747-5921</a>
        <div class="rh-band__contact">
          <strong style="color:var(--ink-inv);">Ryan Rose</strong><br>
          Real Broker, LLC<br>
          <a href="tel:7027475921">702-747-5921</a><br>
          <a href="mailto:ryan@rosehomeslv.com">ryan@rosehomeslv.com</a><br>
          <a href="https://www.rosehomeslv.com">rosehomeslv.com</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ============ MOBILE STICKY BAR ============ -->
  <div class="rh-mobilebar">
    <a class="rh-btn rh-btn--ghost" href="#listings">Homes</a>
    <a class="rh-btn rh-btn--ghost" href="#{p1_sections[0]["id"]}">{c["hero"].get("mobile_label", "Communities")}</a>
    <a class="rh-btn rh-btn--primary" href="#contact">Talk to Ryan</a>
  </div>

</div><!-- /.nc-hub -->'''

    # ---------------- JSON-LD
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": "New Construction", "item": f"{SITE}/{HUB_SLUG}"},
                {"@type": "ListItem", "position": 3, "name": area, "item": url}]},
            {"@type": "Article", "headline": strip_tags(c["hero"]["h1"]),
             "description": c["seo"]["description"],
             "author": {"@type": "Person", "name": "Ryan Rose", "jobTitle": "Real Estate Agent",
                        "worksFor": {"@type": "RealEstateAgent", "name": "Real Broker, LLC"}},
             "publisher": {"@type": "Organization", "name": "Rose Homes LV", "url": SITE},
             "dateModified": c["updated_iso"], "mainEntityOfPage": url,
             "image": img["src"],
             "about": {"@type": "Place", "name": c["place_name"],
                       "address": {"@type": "PostalAddress", "addressLocality": c["locality"],
                                   "addressRegion": "NV", "addressCountry": "US"}},
             "isPartOf": {"@type": "WebPage", "url": f"{SITE}/{HUB_SLUG}"},
             "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["#answer"]}},
            {"@type": "RealEstateAgent", "name": "Ryan Rose", "telephone": "+1-702-747-5921",
             "email": "ryan@rosehomeslv.com", "url": SITE,
             "areaServed": {"@type": "Place", "name": c["place_name"]},
             "parentOrganization": {"@type": "Organization", "name": "Real Broker, LLC"}},
            {"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": strip_tags(q),
                 "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in c["faq"]]},
        ]}
    ld_html = ('<script type="application/ld+json">\n'
               + json.dumps(ld, indent=2, ensure_ascii=False) + "\n</script>")

    script = f"<script>{page_js}</script>"
    part1 = "\n".join([header_comment(c, 1), "", f"<script>{escape_js}</script>", "", FONTS, "",
                       f"<style>{style}</style>", "", p1_body, "", script, ld_html, ""])
    part2 = "\n".join([header_comment(c, 2), "", FONTS, "", f"<style>{style}</style>", "", p2_body,
                       "", script, ""])

    # ---------------- validation
    whole = part1 + part2
    visible = re.sub(r"<!--.*?-->|<style>.*?</style>|<script>.*?</script>", "", whole, flags=re.S)
    for bad, label in (("—", "em-dash"), ("–", "en-dash"), ("&mdash;", "em-dash entity")):
        n = visible.count(bad)
        if n:
            fail(f"{folder}: {n} {label}(s)")
    if re.search(r"<form\b", whole, re.I):
        fail(f"{folder}: inline <form> is not allowed in Lofty embeds")
    for part_name, part in (("part1", part1), ("part2", part2)):
        ids = re.findall(r'\sid="([^"]+)"', part)
        dup = {i for i in ids if ids.count(i) > 1}
        if dup:
            fail(f"{folder} {part_name}: duplicate ids {sorted(dup)}")
    all_ids = set(re.findall(r'\sid="([^"]+)"', whole))
    for tid, _ in toc:
        if tid not in all_ids:
            fail(f"{folder}: rail links to missing #{tid}")
    for href in set(re.findall(r'href="#([^"]+)"', whole)):
        if href not in all_ids:
            fail(f"{folder}: anchor #{href} has no target")
    live = set()
    for sm in sorted(ROOT.glob("_build/live-sitemap-*.json")):
        d = json.loads(sm.read_text())
        live |= {s for k, v in d.items() if isinstance(v, list) for s in v}
    for s in set(re.findall(r'href="(?:https://www\.rosehomeslv\.com)?/blog/([^"#?]+)', whole)):
        if s not in live:
            fail(f"{folder}: /blog/{s} is not in the live sitemap file")
    if re.search(r'href="[^"]*/blogs/', whole):
        fail(f"{folder}: /blogs/ (plural) link, use /blog/")
    seo = c["seo"]
    if len(seo["title"]) > 48:
        fail(f"{folder}: meta title {len(seo['title'])} chars, max 48 before Lofty's suffix")
    if len(seo["description"]) > 160:
        fail(f"{folder}: meta description {len(seo['description'])} chars, max 160")
    if len(seo["keywords"]) > 100:
        fail(f"{folder}: keywords {len(seo['keywords'])} chars, max 100")
    if "NOT FOUND" in visible:
        fail(f"{folder}: 'NOT FOUND' left in page copy, cut the claim instead")

    # ---------------- write
    out = ROOT / folder
    (out / "part-1-above-listings.html").write_text(part1)
    (out / "part-2-below-listings.html").write_text(part2)
    p2_nohead = part2.replace(FONTS, "")
    p2_nohead = re.sub(r"<style>.*?</style>", "", p2_nohead, count=1, flags=re.S)
    standin = '''<div style="background:#000;color:#fff;padding:90px 28px;text-align:center;font-family:'Raleway',sans-serif;">
  <p style="font-size:11px;letter-spacing:.15em;text-transform:uppercase;color:#5B9BFF;margin:0 0 14px;font-weight:600;">Preview stand-in</p>
  <p style="font-size:20px;margin:0 0 8px;font-family:'Barlow',sans-serif;font-weight:800;letter-spacing:-.028em;">Lofty Featured Listings block renders here</p>
  <p style="font-size:14px;opacity:.7;margin:0;">Built in Lofty's editor, between embed 1 and embed 2</p>
  <div style="height:520px;"></div>
</div>'''
    (out / "_preview-stitched.html").write_text(
        '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>{area} new construction preview</title></head><body>\n'
        + part1 + "\n" + standin + "\n" + p2_nohead + "\n</body></html>\n")
    (out / "0-seo-fields.txt").write_text(seo_sheet(c, url))
    return c, len(part1), len(part2)


def seo_sheet(c, url):
    s = c["seo"]
    t = s["title"]
    return f'''LOFTY PAGE SETTINGS - {c["area"].upper()} NEW CONSTRUCTION
{"=" * (len(c["area"]) + 40)}
Generated by geo-spokes/_build/build.py from content.json. Edit there, not here.

URL SLUG
========
{c["slug"]}

Full URL:
{url}

Parent page (link from here, and it already links back):
{SITE}/{HUB_SLUG}


META TITLE   ({len(t)} chars, shows as {len(t) + 12} live)
{"=" * (len(str(len(t))) + 36)}
{t}

*** LOFTY APPENDS " | Ryan Rose" (12 chars) TO WHATEVER YOU TYPE. ***
Keep this field at 48 or fewer. Do not add the brand yourself.


META DESCRIPTION   ({len(s["description"])} chars, limit 160)
=====================================
{s["description"]}


META KEYWORDS   ({len(s["keywords"])} chars, limit 100)
==================================
{s["keywords"]}


CANONICAL URL
=============
{url}


OPEN GRAPH / TWITTER
====================
og:title           {s.get("og_title", t)}
og:description     {s.get("og_description", s["description"])}
og:type            article
og:url             {url}
og:image           {c["hero"]["image"]["src"]}
og:image:alt       {c["hero"]["image"]["alt"]}
twitter:card       summary_large_image

Lofty defaults og:image to a generic Chime placeholder. Paste the og:image above
into the page's share image field or every share of this page uses the placeholder.


H1 ON THE PAGE   (already in part 1, do not add another in Lofty)
===============
{strip_tags(c["hero"]["h1"])}


WHAT GETS PASTED, IN THIS ORDER
===============================
1. part-1-above-listings.html      Lofty HTML module
2. Lofty Featured Listings block    built in Lofty's editor, filter below
3. part-2-below-listings.html      Lofty HTML module

_preview-stitched.html is a local preview only. Never paste it.

FEATURED LISTINGS BLOCK FILTER
{c["listings"]["lofty_filter"]}

Schema (BreadcrumbList, Article, RealEstateAgent, FAQPage) is already inside part 1.
Do NOT put it in Lofty's Page Script field (5,000 char cap).
Do NOT paste GA or Meta Pixel tags, Lofty injects them.


LAUNCH CHECKLIST
================
[ ] Create as a CMS SITE PAGE, not a landing page, so it enters sitemap.xml
[ ] Slug exactly: {c["slug"]}  (the hub already links to it)
[ ] Build the Featured Listings block with the filter above
[ ] Paste part 1 above it, part 2 below it
[ ] Enter title, description, keywords, canonical, og:image by hand
[ ] Publish, open the live page, confirm one H1 and both rails
[ ] Search Console: URL Inspection, Request indexing
'''


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    style, escape_js, page_js, builders = load_hub()
    folders = ([a for a, _ in AREAS if (ROOT / a / "content.json").exists()]
               if args == ["--all"] else args)
    for f in folders:
        try:
            c, n1, n2 = build(f, style, escape_js, page_js, builders)
            print(f"built {f}: part1 {n1:,} bytes, part2 {n2:,} bytes")
        except (KeyError, ValueError) as e:
            fail(f"{f}: content.json problem: {e!r}")
    if errors:
        print("\nBUILD ERRORS:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("OK, no validation errors")


if __name__ == "__main__":
    main()
