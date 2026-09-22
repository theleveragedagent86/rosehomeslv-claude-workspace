#!/usr/bin/env python3
"""
Build full "our process" JSON-LD for live Lofty posts that have none
====================================================================
Input is a dump from `lofty_api.py dump`. Output is a patches file for
`lofty_api.py patch`. Only posts with an empty Schema tab are touched.

    python3 build_live_schema.py dump.json patches.json [--all-missing] [--report]

Per post the @graph holds (same shape publish-aeo.py build_graph ships):
  - Article (NewsArticle for Local News) with @id <url>#article, headline,
    description, image (the post's own featured image), dates, keywords,
    articleSection, mainEntityOfPage /blog/<slug>, about = Place node(s)
  - Person #ryanrose and RealEstateAgent #org, fixed @ids on every post
  - FAQPage built from the post's own question headings and their answers

When the local Claude Blogs / Local News file for the slug has researched
JSON-LD, its description, keywords, about and FAQ win over generated ones.
Local image paths are never used: they were placeholders that 404.
"""
import html
import importlib.util
import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTENT = Path("/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content")
SITE = "https://www.rosehomeslv.com"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


aeo = _load("publish_aeo", HERE / "publish-aeo.py")

# (display name, regex, addressLocality). Longest / most specific first.
AREAS = [
    ("Sun City Summerlin", r"sun city summerlin", "Las Vegas"),
    ("Sun City Anthem", r"sun city anthem", "Henderson"),
    ("Green Valley Ranch", r"green valley ranch", "Henderson"),
    ("Green Valley", r"green valley", "Henderson"),
    ("Madeira Canyon", r"madeira canyon", "Henderson"),
    ("MacDonald Highlands", r"macdonald highlands", "Henderson"),
    ("MacDonald Ranch", r"macdonald ranch", "Henderson"),
    ("Calico Ridge", r"calico ridge", "Henderson"),
    ("Anthem", r"anthem", "Henderson"),
    ("Inspirada", r"inspirada", "Henderson"),
    ("Cadence", r"cadence", "Henderson"),
    ("Whitney Ranch", r"whitney ranch", "Henderson"),
    ("Seven Hills", r"seven hills", "Henderson"),
    ("Horizon's Edge", r"horizon.?s edge", "Henderson"),
    ("The Lakes", r"the lakes(?! of)", "Las Vegas"),
    ("Lake Las Vegas", r"lake las vegas", "Henderson"),
    ("North Las Vegas", r"north las vegas|nlv", "North Las Vegas"),
    ("Aliante", r"aliante", "North Las Vegas"),
    ("Mesquite", r"mesquite", "Mesquite"),
    ("Mountain's Edge", r"mountain.?s edge", "Las Vegas"),
    ("Southwest Las Vegas", r"southwest las vegas|southwest", "Las Vegas"),
    ("Centennial Hills", r"centennial hills", "Las Vegas"),
    ("Spring Valley", r"spring valley", "Las Vegas"),
    ("Southern Highlands", r"southern highlands", "Las Vegas"),
    ("Queensridge", r"queensridge", "Las Vegas"),
    ("Rhodes Ranch", r"rhodes ranch", "Las Vegas"),
    ("Skye Canyon", r"skye canyone?", "Las Vegas"),
    ("Providence", r"providence", "Las Vegas"),
    ("Desert Shores", r"desert shores", "Las Vegas"),
    ("Silverado Ranch", r"silverado ranch", "Las Vegas"),
    ("Enterprise", r"enterprise", "Las Vegas"),
    ("Summerlin", r"summerlin", "Las Vegas"),
    ("Henderson", r"henderson", "Henderson"),
]
CITIES = {"Henderson", "North Las Vegas", "Summerlin", "Southwest Las Vegas"}
AREA_RE = re.compile("|".join(f"(?P<a{i}>\\b(?:{p})\\b)" for i, (_, p, _) in enumerate(AREAS)), re.I)
# Category name -> AREAS name, for posts whose title names no area
CAT_AREA = {"relocating to summerlin": "Summerlin", "mountains edge": "Mountain's Edge",
            "lakes las vegas": None, "mesquite nv": "Mesquite", "horizons edge": "Horizon's Edge",
            "skye canyone": "Skye Canyon", "southwest": "Southwest Las Vegas"}
AREA_BY_NAME = {a[0].lower(): a for a in AREAS}


def place(name, locality):
    return {"@type": "Place", "name": name,
            "address": {"@type": "PostalAddress", "addressLocality": locality,
                        "addressRegion": "NV", "addressCountry": "US"}}


def places_for(title, cats):
    found = []
    for m in AREA_RE.finditer(title):
        a = AREAS[int(m.lastgroup[1:])]
        if a not in found:
            found.append(a)
    if not found:
        for c in cats:
            key = c.lower()
            name = CAT_AREA.get(key, key)
            if name and name.lower() in AREA_BY_NAME and AREA_BY_NAME[name.lower()] not in found:
                found.append(AREA_BY_NAME[name.lower()])
    if len(found) > 1 and " vs" not in title.lower():
        # "Calico Ridge Henderson": keep the community, drop its parent city/master plan
        specific = [a for a in found if a[0] not in CITIES]
        found = specific or found
    if not found:
        found = [("Las Vegas", "", "Las Vegas")]
    return [place(n, loc) for n, _, loc in found]


def text(s):
    s = re.sub(r"<script.*?</script>|<style.*?</style>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def faq_from_content(content):
    """Question h2/h3 headings + the text under each, up to the next heading."""
    parts = re.split(r"(<h[23][^>]*>.*?</h[23]>)", content, flags=re.S | re.I)
    qa = []
    for i, p in enumerate(parts):
        if not re.match(r"<h[23]", p, re.I):
            continue
        q = text(p)
        if not q.endswith("?"):
            continue
        ans = text(parts[i + 1]) if i + 1 < len(parts) else ""
        if len(ans) >= 40:
            qa.append({"@type": "Question", "name": q,
                       "acceptedAnswer": {"@type": "Answer", "text": ans}})
    return qa


def local_index():
    idx = {}
    for f in CONTENT.rglob("*.html"):
        try:
            raw = f.read_text(encoding="utf-8")
        except Exception:
            continue
        if "ld+json" not in raw:
            continue
        sj, err = aeo.ln.extract_schema(raw)
        if err or not sj:
            continue
        try:
            data = json.loads(sj)
        except Exception:
            continue
        slugs = {re.sub(r"^(?:batch\d+-)?(?:story-|bonus-|post)?\d+-", "", f.stem)}
        m = re.search(r'"@id"\s*:\s*"https?://(?:www\.)?rosehomeslv\.com/blogs?/([a-z0-9-]+)', raw)
        if m:
            slugs.add(m.group(1))
        for s in slugs:
            idx.setdefault(s, data)
    return idx


def split_local(data):
    nodes = data.get("@graph", [data]) if isinstance(data, dict) else data
    art, faq, extra = None, None, []
    for n in nodes:
        t = n.get("@type")
        t = t[0] if isinstance(t, list) else t
        if t in ("Article", "BlogPosting", "NewsArticle") and art is None:
            art = n
        elif t == "FAQPage":
            faq = n
        elif t in ("Person", "Organization", "RealEstateAgent", "WebPage", "BreadcrumbList"):
            continue
        else:
            extra.append(n)
    return art, faq, extra


def kw_string(k):
    if isinstance(k, list):
        return ", ".join(str(x) for x in k)
    return (k or "").strip()


def build(post, local):
    url = f"{SITE}/blog/{post['slug']}"
    cats = post.get("cat") or []
    news = "Local News" in cats
    la, lfaq, lextra = split_local(local) if local else (None, None, [])
    la = la or {}
    pub = datetime.fromtimestamp(post["postDate"] / 1000, timezone(timedelta(hours=-7))).date().isoformat()
    mod = (post.get("updateTime") or "").split(" ")[0].replace("/", "-") or pub
    desc = (post.get("seoDescription") or "").strip() or (la.get("description") or "").strip() \
        or text(post["content"])[:157].rsplit(" ", 1)[0] + "..."
    kws = kw_string(la.get("keywords")) or kw_string(post.get("seoKeyword"))
    if len(kws) >= 500 and not la.get("keywords"):
        kws = kws.rsplit(",", 1)[0].strip()  # Lofty cuts SEO keywords at 500 chars mid-word
    about = la.get("about") or places_for(post["title"], cats)
    if isinstance(about, list) and len(about) == 1:
        about = about[0]
    art = {
        "@type": "NewsArticle" if news else "Article",
        "@id": f"{url}#article",
        "headline": re.sub(r"\s*\|\s*Ryan Rose\s*$", "", post["title"]).strip(),
        "description": desc,
        "image": post.get("featuredImage") or None,
        "author": {"@id": aeo.PERSON_ID},
        "publisher": {"@id": aeo.ORG_ID},
        "datePublished": pub,
        "dateModified": max(mod, pub),
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "articleSection": cats[0] if cats else None,
        "about": about,
        "keywords": kws or None,
        "inLanguage": "en-US",
    }
    art = {k: v for k, v in art.items() if v}
    graph = json.loads(aeo.build_graph(dict(art, mainEntityOfPage={"@type": "WebPage", "@id": url})))
    graph["@graph"][0] = art
    qa = faq_from_content(post["content"])
    if lfaq and lfaq.get("mainEntity"):
        faq = dict(lfaq)
        faq.pop("@context", None)
    elif qa:
        faq = {"@type": "FAQPage", "mainEntity": qa}
    else:
        faq = None
    if faq:
        faq["@id"] = f"{url}#faq"
        faq["mainEntityOfPage"] = {"@id": url}
        graph["@graph"].append(faq)
    for n in lextra:
        n = dict(n)
        n.pop("@context", None)
        if n.get("@type") == "Place" and n == about:
            continue
        graph["@graph"].append(n)
    out = json.dumps(graph, indent=2, ensure_ascii=False)
    out = re.sub(r"https?://(?:www\.)?rosehomeslv\.com/blogs/", f"{SITE}/blog/", out)
    out = re.sub(r"\s*\u2014\s*", ", ", out)  # no em-dashes, workspace rule
    return out


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    posts = json.loads(Path(sys.argv[1]).read_text())
    idx = local_index()
    patches, stats = {}, {"posts": 0, "local": 0, "faq": 0, "news": 0}
    report = []
    for p in posts:
        if (p.get("schema") or "").strip() or not p["title"].strip():
            continue
        local = idx.get(p["slug"])
        s = build(p, local)
        patches[str(p["id"])] = {"customSchema": s}
        g = json.loads(s)["@graph"]
        stats["posts"] += 1
        stats["local"] += bool(local)
        stats["faq"] += any(n.get("@type") == "FAQPage" for n in g)
        stats["news"] += g[0]["@type"] == "NewsArticle"
        ab = g[0].get("about")
        ab = ab if isinstance(ab, list) else [ab]
        report.append((p["slug"], ",".join(p.get("cat") or []), " + ".join(
            f"{a.get('name')} ({(a.get('address') or {}).get('addressLocality', '?')})" for a in ab if a)))
    Path(sys.argv[2]).write_text(json.dumps(patches, ensure_ascii=False))
    print(stats)
    if "--report" in sys.argv:
        for r in report:
            print(" | ".join(r))


if __name__ == "__main__":
    main()
