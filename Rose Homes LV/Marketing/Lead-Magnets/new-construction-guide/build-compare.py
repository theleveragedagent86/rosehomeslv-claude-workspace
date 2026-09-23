#!/usr/bin/env python3
"""
Build design/_compare.html: all six design directions side by side in one page.

Each direction is shown as a live, scaled iframe of its own preview.html, so what
Ryan compares is the real rendered artifact rather than a screenshot of it. Iframes
need HTTP because file:// iframes are blocked, so serve the folder first:

    ruby /Users/ryanrose/Downloads/Claude/serve.rb          # from this directory
    open http://localhost:8091/design/_compare.html

Re-runnable. Reads whatever directions currently exist on disk.
"""

import glob
import html
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
DESIGN = os.path.join(HERE, "design")
OUT = os.path.join(DESIGN, "_compare.html")

# Scale factor for the embedded previews. A preview page is 8.5in wide, which at
# 96dpi is 816px; two-up spreads are ~1650px. We render the iframe at full logical
# width and scale it down with a transform so type rendering stays honest.
# A two-page spread is two Letter pages side by side, which lands near 2500px. Anything
# narrower clips the right-hand page instead of scaling it, which is a silent, convincing
# failure: the card looks fine and the content is simply gone.
IFRAME_W = 2500
IFRAME_H = 6600
SCALE = 0.27


def pretty(slug: str) -> str:
    name = re.sub(r"^direction-\d+-", "", slug)
    return name.replace("-", " ").title()


def number(slug: str) -> str:
    m = re.match(r"^direction-(\d+)-", slug)
    return m.group(1) if m else "?"


def first_line_after(path: str, pattern: str) -> str:
    """Pull a labeled one-liner out of a director's rationale.md."""
    if not os.path.isfile(path):
        return ""
    body = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(pattern, body, re.I | re.M)
    return m.group(1).strip() if m else ""


def collect():
    dirs = []
    for d in sorted(glob.glob(os.path.join(DESIGN, "direction-*"))):
        if not os.path.isdir(d):
            continue
        slug = os.path.basename(d)
        preview = os.path.join(d, "preview.html")
        rationale = os.path.join(d, "rationale.md")
        tokens = os.path.join(d, "tokens.md")

        thesis = first_line_after(rationale, r"^\s*>\s*(.+)$") or \
                 first_line_after(rationale, r"\*\*Thesis[:*]*\**\s*(.+)$")

        # Any hex swatches the director declared, for a quick palette strip. Prefer the
        # written tokens.md; fall back to the :root custom properties in the preview when
        # a director died before writing its docs, so the card still shows a real palette
        # rather than a blank strip.
        hexes, src = [], ""
        if os.path.isfile(tokens):
            body = open(tokens, encoding="utf-8", errors="replace").read()
            src = "tokens.md"
        elif os.path.isfile(preview):
            body = open(preview, encoding="utf-8", errors="replace").read()
            m = re.search(r":root\s*\{(.*?)\}", body, re.S)
            body = m.group(1) if m else body
            src = ":root"
        else:
            body = ""
        seen = set()
        for h in re.findall(r"#[0-9a-fA-F]{6}\b", body):
            h = h.lower()
            if h not in seen:
                seen.add(h)
                hexes.append(h)
        hexes = hexes[:10]

        if not thesis:
            thesis = ("companion docs not written yet, the agent hit the session limit "
                      "after rendering the design")

        dirs.append({
            "slug": slug,
            "n": number(slug),
            "name": pretty(slug),
            "has_preview": os.path.isfile(preview),
            "thesis": thesis,
            "hexes": hexes,
            "src": src,
            "docs": [n for n in ("tokens.md", "rationale.md", "claude-design-prompt.md")
                     if os.path.isfile(os.path.join(d, n))],
        })
    return dirs


CSS = """
*,*::before,*::after{box-sizing:border-box}
html{color-scheme:light dark}
body{margin:0;font:15px/1.6 ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
     background:#101114;color:#e9e9ec}
header{padding:32px 28px 20px;border-bottom:1px solid #2a2c33;position:sticky;top:0;
       background:#101114ee;backdrop-filter:blur(8px);z-index:10}
h1{margin:0 0 6px;font-size:21px;letter-spacing:-.01em}
.sub{color:#9a9ca6;font-size:13.5px;max-width:74ch}
.grid{display:grid;gap:22px;padding:24px 28px 60px;
      grid-template-columns:repeat(auto-fill,minmax(700px,1fr))}
.card{border:1px solid #2a2c33;border-radius:10px;overflow:hidden;background:#17181c;
      display:flex;flex-direction:column}
.card h2{margin:0;padding:14px 16px 4px;font-size:16px;letter-spacing:-.01em}
.card h2 .n{display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;
     border-radius:5px;background:#2f3138;color:#c9cbd3;font-size:12px;margin-right:9px}
.thesis{padding:0 16px 12px;color:#9a9ca6;font-size:13px;font-style:italic;min-height:2.6em}
.sw{display:flex;gap:4px;padding:0 16px 12px}
.sw i{width:20px;height:20px;border-radius:4px;border:1px solid #ffffff22;display:block}
.frame{position:relative;height:%(fh)dpx;border-top:1px solid #2a2c33;background:#6b6b6b;
       overflow:hidden}
.frame iframe{position:absolute;top:0;left:0;width:%(iw)dpx;height:%(ih)dpx;border:0;
       transform:scale(%(sc)s);transform-origin:top left}
.missing{display:grid;place-items:center;height:100%%;color:#6d6f78;font-size:13px;
       background:repeating-linear-gradient(45deg,#1b1c21,#1b1c21 10px,#191a1f 10px,#191a1f 20px)}
.foot{display:flex;gap:14px;padding:11px 16px;border-top:1px solid #2a2c33;font-size:12.5px}
.foot a{color:#8ab4f8;text-decoration:none}
.foot a:hover{text-decoration:underline}
.pend{color:#8a7a4a}
@media (prefers-color-scheme:light){
  body{background:#f6f6f7;color:#16171a}
  header{background:#f6f6f7ee;border-color:#dcdde1}
  .sub,.thesis{color:#63656d}
  .card{background:#fff;border-color:#dcdde1}
  .card h2 .n{background:#eceef2;color:#3a3c44}
  .frame,.foot{border-color:#dcdde1}
}
""" % {"fh": int(IFRAME_H * SCALE), "iw": IFRAME_W, "ih": IFRAME_H, "sc": SCALE}


def build():
    dirs = collect()
    cards = []
    for d in dirs:
        sw = "".join(f'<i style="background:{h}"></i>' for h in d["hexes"])
        if d["has_preview"]:
            frame = (f'<div class="frame"><iframe loading="lazy" title="{html.escape(d["name"])} preview" '
                     f'src="{d["slug"]}/preview.html"></iframe></div>')
        else:
            frame = '<div class="frame"><div class="missing">preview.html not written yet</div></div>'
        cards.append(f"""
  <section class="card">
    <h2><span class="n">{d['n']}</span>{html.escape(d['name'])}</h2>
    <p class="thesis">{html.escape(d['thesis'] or '')}</p>
    <div class="sw">{sw}</div>
    {frame}
    <div class="foot">
      <a href="{d['slug']}/preview.html" target="_blank">open full size</a>
      {' '.join('<a href="%s/%s" target="_blank">%s</a>' % (d['slug'], n, n[:-3].replace('-', ' '))
                for n in d['docs'])
       or '<span class="pend">docs pending</span>'}
    </div>
  </section>""")

    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>New Construction Guide, six design directions</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <h1>Round 6, less orange, two layouts, two strengths</h1>
  <p class="sub">Bodoni Moda and Archivo throughout. One and two are the navy layout, three and four
  the geometric one, and within each pair the second has the orange pulled back further. Orange keeps
  the refusal panel and the button at every strength, because those are the two places it is doing a
  job. The geometric cover title is now mixed case and large, the way the navy one sets it, and
  every tinted card takes the pale fill of the Sub association bar in the cost diagram. Previews
  are live and scaled to {int(SCALE * 100)} percent of a {IFRAME_W}px frame, wide enough to hold a
  full two page spread without clipping the right hand page. Open one full size to judge it at
  reading distance, which is the only fair way. Earlier rounds are archived under
  <code>_v3-directed/</code>, <code>_v4-type/</code> and <code>_v5-layout/</code>.</p>
</header>
<div class="grid">{''.join(cards)}
</div>
</body>
</html>"""

    os.makedirs(DESIGN, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(doc)

    ready = sum(1 for d in dirs if d["has_preview"])
    print(f"wrote {OUT}")
    print(f"  {len(dirs)} directions, {ready} with a rendered preview")
    for d in dirs:
        mark = "ok  " if d["has_preview"] else "MISS"
        print(f"  [{mark}] {d['n']}. {d['name']}  {' '.join(d['hexes'][:5])}")
    print("\nserve it:  ruby /Users/ryanrose/Downloads/Claude/serve.rb")
    print("then open: http://localhost:8091/design/_compare.html")


if __name__ == "__main__":
    build()
