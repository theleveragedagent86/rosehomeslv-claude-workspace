#!/usr/bin/env python3
"""
Backfill FAQPage, the Person/RealEstateAgent graph, and featured images
=======================================================================
Input is a dump from `lofty_api.py dump`. Output is a patches file for
`lofty_api.py patch`. Posts already carrying a piece are left alone.

    python3 backfill_schema.py dump.json patches.json [--report] [--min-qa 2]

Three fixes, each applied only where it is missing:
  1. FAQPage built from the post's own question headings and the text under
     them, appended to the graph as <url>#faq. Needs --min-qa pairs (2 by
     default): a one-question FAQPage is not worth shipping.
  2. Schema stored as a bare Article/BlogPosting/NewsArticle is wrapped in the
     same @graph publish-aeo.py ships, so Person #ryanrose and RealEstateAgent
     #org carry fixed @ids on every post and merge into one entity.
  3. featuredImage: Lofty derives it from the first <img> in the body, so posts
     with no image in the body end up with none. Use the body image when there
     is one, otherwise the site default (--default-image).

Never invents a value: an image is either the post's own or Ryan's existing
site default, and FAQ answers are the post's own copy.
"""
import argparse
import importlib.util
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = "https://www.rosehomeslv.com"
# Ryan's own uploaded default, already the featured image on ~3,100 posts
DEFAULT_IMAGE = ("https://cdn.chime.me/image/fs/user-info/2025115/11/"
                 "original_1abb6c8d-85b2-4e1f-ac30-8d7c85288567.png")
ARTICLE_TYPES = ("Article", "BlogPosting", "NewsArticle")


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


bls = _load("build_live_schema", HERE / "build_live_schema.py")
aeo = bls.aeo


def node_type(n):
    t = n.get("@type")
    return t[0] if isinstance(t, list) else t


def nodes_of(data):
    if isinstance(data, dict) and "@graph" in data:
        return list(data["@graph"])
    if isinstance(data, list):
        return list(data)
    return [data]


def clean(s):
    """Workspace rules: no em-dashes, /blog/ is singular."""
    s = re.sub(r"https?://(?:www\.)?rosehomeslv\.com/blogs/", f"{SITE}/blog/", s)
    return re.sub(r"\s*—\s*", ", ", s)


def fix(post, args):
    """Return {field: value} for this post, or {} if nothing is missing."""
    patch = {}
    url = f"{SITE}/blog/{post['slug']}"
    content = post.get("content") or ""

    img = (post.get("featuredImage") or "").strip()
    if not img:
        m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.I)
        img = m.group(1) if m else args.default_image
        patch["featuredImage"] = img

    raw = (post.get("schema") or "").strip()
    if not raw:
        return patch                      # build_live_schema.py owns these
    try:
        data = json.loads(raw)
    except ValueError:
        return patch
    nodes = nodes_of(data)
    types = {node_type(n) for n in nodes}
    changed = False

    art = next((n for n in nodes if node_type(n) in ARTICLE_TYPES), None)
    if art is not None and not types & {"Person", "RealEstateAgent"}:
        art = dict(art)
        mep = art.get("mainEntityOfPage")
        if isinstance(mep, str):            # some posts store it as a bare URL
            mep = {"@type": "WebPage", "@id": mep}
        if not isinstance(mep, dict) or not mep.get("@id"):
            mep = {"@type": "WebPage", "@id": url}
        art["mainEntityOfPage"] = mep
        if not art.get("image") and img:
            art["image"] = img
        wrapped = json.loads(aeo.build_graph(art))
        rest = [n for n in nodes if node_type(n) not in ARTICLE_TYPES]
        for n in rest:
            n = dict(n)
            n.pop("@context", None)
            wrapped["@graph"].append(n)
        data, nodes, changed = wrapped, wrapped["@graph"], True
    elif not isinstance(data, dict) or "@graph" not in data:
        data = {"@context": "https://schema.org", "@graph": nodes}
        changed = True

    art = next((n for n in nodes if node_type(n) in ARTICLE_TYPES), None)
    if art is not None and not art.get("image") and img:
        art["image"] = img              # rich results want the image on the Article too
        changed = True

    if "FAQPage" not in types:
        qa = bls.faq_from_content(content)
        if len(qa) >= args.min_qa:
            data["@graph"].append({"@type": "FAQPage", "@id": f"{url}#faq",
                                   "mainEntityOfPage": {"@id": url},
                                   "mainEntity": qa})
            changed = True

    if changed:
        patch["customSchema"] = clean(json.dumps(data, indent=2, ensure_ascii=False))
    return patch


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("dump")
    ap.add_argument("out")
    ap.add_argument("--min-qa", type=int, default=2,
                    help="Question headings needed before a FAQPage is added (default: 2)")
    ap.add_argument("--default-image", default=DEFAULT_IMAGE)
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    posts = list({p["id"]: p for p in json.loads(Path(args.dump).read_text())}.values())
    patches, stats, rows = {}, {"faq": 0, "graph": 0, "image": 0, "posts": 0}, []
    for p in posts:
        if not p["title"].strip():
            continue
        patch = fix(p, args)
        if not patch:
            continue
        did = []
        if "featuredImage" in patch:
            stats["image"] += 1
            did.append("image")
        if "customSchema" in patch:
            before, after = p.get("schema") or "", patch["customSchema"]
            if "FAQPage" not in before and "FAQPage" in after:
                stats["faq"] += 1
                did.append("faq")
            if "#ryanrose" not in before and "#ryanrose" in after:
                stats["graph"] += 1
                did.append("graph")
        if not did:
            continue
        stats["posts"] += 1
        patches[str(p["id"])] = patch
        rows.append((p["slug"], "+".join(did)))
    Path(args.out).write_text(json.dumps(patches, ensure_ascii=False))
    print(stats)
    if args.report:
        for s, d in rows:
            print(f"  {d:16} /blog/{s}")


if __name__ == "__main__":
    main()
