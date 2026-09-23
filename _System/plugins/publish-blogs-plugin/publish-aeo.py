#!/usr/bin/env python3
"""
Lofty CMS Publisher for slug-named blog folders (the AEO batches)
==================================================================
Reads posts the same way publish.py does (markdown body in a .html file, SEO
from seo-package-batch*.md matched by slug), then publishes with the Chrome
automation from the local news publisher, which is the maintained one: it has
the working Post Now click, the Schema tab, QA, and the duplicate-slug check.

JSON-LD is pulled OUT of the body and entered on Lofty's Schema tab. Lofty's
TinyMCE editor corrupts it when it sits in the body.

Usage:
    python3 publish-aeo.py "AEO Best Choice" --yes
    python3 publish-aeo.py "AEO Local Service" --posts 1-10 --yes
    python3 publish-aeo.py "AEO Best Choice" --no-publish      Preview only
    python3 publish-aeo.py "AEO Questions" --ui --yes          Old editor method

Runs in the background: it calls Lofty's blog API through any open
cms.lofty.com tab (any window, any tab number) and never needs focus, so keep
using your Mac while it runs. --ui restores the old editor-driving method,
which types into Chrome and must be left alone (tab 4, or pass --tab).

Requirements: macOS, Chrome with View > Developer > Allow JavaScript from
Apple Events, logged into Lofty CMS in some tab.
"""

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOCAL_NEWS = HERE.parent / "local-news-plugin" / "publish-local-news.py"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


pb = _load("publish_blogs", HERE / "publish.py")      # data prep
ln = _load("publish_local_news", LOCAL_NEWS)          # Chrome automation

JSONLD_RE = re.compile(
    r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>.*?</script>',
    re.IGNORECASE | re.DOTALL)
PERSON_ID = "https://www.rosehomeslv.com/#ryanrose"
ORG_ID = "https://www.rosehomeslv.com/#org"


def build_graph(article):
    """Wrap the post's Article JSON-LD in the same @graph shape local news uses.

    Person and RealEstateAgent carry fixed @id values on every post so search
    engines and LLMs merge them into one entity for Ryan.
    """
    article = dict(article)
    article.pop("@context", None)
    mep = article.get("mainEntityOfPage")
    if isinstance(mep, str):          # some files store it as a bare URL
        mep = {"@id": mep}
        article["mainEntityOfPage"] = {"@type": "WebPage", "@id": mep["@id"]}
    url = (mep or {}).get("@id", "")
    if url:
        article["@id"] = f"{url}#article"
    article["author"] = {"@id": PERSON_ID}
    article["publisher"] = {"@id": ORG_ID}
    return json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            article,
            {
                "@type": "Person",
                "@id": PERSON_ID,
                "name": "Ryan Rose",
                "jobTitle": "Las Vegas Real Estate Expert",
                "url": "https://www.rosehomeslv.com",
                "worksFor": {"@id": ORG_ID},
            },
            {
                "@type": "RealEstateAgent",
                "@id": ORG_ID,
                "name": "Rose Homes LV",
                "url": "https://www.rosehomeslv.com",
                "telephone": "+1-702-747-5921",
                "areaServed": {"@type": "AdministrativeArea",
                               "name": "Clark County, Nevada"},
            },
        ],
    }, indent=2, ensure_ascii=False)


def lists_to_ul(html):
    """publish.py's markdown converter has no list support, so '- item' lines end
    up inside one <p>. Turn any <p> made only of '- ' lines into a real <ul>."""
    def fix(m):
        lines = [l.strip() for l in m.group(1).strip().split("\n") if l.strip()]
        if not lines or not all(l.startswith("- ") for l in lines):
            return m.group(0)
        items = "".join(f"<li>{l[2:].strip()}</li>" for l in lines)
        return f"<ul>{items}</ul>"
    return re.sub(r"<p>(.*?)</p>", fix, html, flags=re.DOTALL)


def prepare(folder, category, post_filter, allow_no_schema=False):
    posts = pb.prepare_posts(folder, category, post_filter)
    errors = []
    for p in posts:
        raw = (folder / p["file"]).read_text(encoding="utf-8")
        schema_json, err = ln.extract_schema(raw)
        if err or not schema_json:
            if not allow_no_schema:
                errors.append(f"{p['file']}: {err or 'no JSON-LD block'}")
                continue
            p["schema"] = ""          # backfill_schema.py builds it from the live post
            p["body"] = lists_to_ul(JSONLD_RE.sub("", p["body"]).strip())
            p["label"] = f"Post {p['number']}"
            continue
        p["schema"] = build_graph(json.loads(schema_json))
        # Never ship schema in the body
        p["body"] = lists_to_ul(JSONLD_RE.sub("", p["body"]).strip())
        p["label"] = f"Post {p['number']}"
    if errors:
        print("\nDATA ERRORS:\n")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    return posts


def parse_filter(spec):
    if not spec:
        return None
    nums = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            s, e = part.split("-")
            nums.update(range(int(s), int(e) + 1))
        else:
            nums.add(int(part))
    return nums


def clean_slug(slug):
    """Some SEO packages write the slug as '/blogs/name'. Lofty stores that
    verbatim and the post ends up unreachable, so keep only the last segment."""
    return re.sub(r"^/?blogs?/", "", (slug or "").strip()).strip("/")


def trim_keywords(kw, limit=500):
    """Lofty rejects a save outright (error 601) when seoKeyword runs past 500
    characters. Cut at a comma so a keyword is never left half-written."""
    kw = (kw or "").strip()
    if len(kw) <= limit:
        return kw
    cut = kw[:limit]
    return (cut.rsplit(",", 1)[0] if "," in cut else cut).strip()


def api_publish(posts, args):
    """Publish through Lofty's API from any open cms.lofty.com tab: no focus,
    no tab number, nothing to leave alone."""
    L = _load("lofty_api", HERE / "lofty_api.py")
    print("\nRuns in the background through any open Lofty tab. You can keep using your Mac.")
    if not args.yes and input("Proceed? (y/n): ").strip().lower() != "y":
        print("Cancelled.")
        return
    print("\nChecking for slugs that already exist in Lofty...")
    for p in posts:
        p["slug"] = clean_slug(p["slug"])
    existing = L.find_by_slug([p["slug"] for p in posts])
    if existing:
        print(f"  Already published: {', '.join(sorted(existing))}")
        if not args.force_duplicates:
            posts = [p for p in posts if p["slug"] not in existing]
            print(f"  Skipping those. {len(posts)} left.")
        if not posts:
            print("\nNothing left to publish. Done.")
            return
    else:
        print("  None. All slugs are new.")
    print(f"\nPublishing {len(posts)} posts...")
    rows = L.create([{
        "title": p["title"], "slug": clean_slug(p["slug"]), "content": p["body"],
        "seoTitle": p["meta_title"], "seoKeyword": p["meta_keywords"],
        "seoDescription": p["meta_description"], "customSchema": p["schema"],
    } for p in posts], args.category)
    ok = [r for r in rows if r[1].startswith("OK")]
    print(f"\n{'='*60}\nPublished: {len(ok)}/{len(posts)}\n{'='*60}")
    for r in rows:
        if not r[1].startswith("OK"):
            print(f"  [!!] /blog/{r[0]}  {r[1]}")


def main():
    ap = argparse.ArgumentParser(description="Publish a slug-named blog folder to Lofty")
    ap.add_argument("folder", help="Folder name under Claude Blogs, e.g. 'AEO Best Choice'")
    ap.add_argument("--posts", help="Post numbers from the preview list: '1-10' or '1,5,8'")
    ap.add_argument("--slugs", nargs="+", help="Only these slugs")
    ap.add_argument("--allow-no-schema", action="store_true",
                    help="Publish files that have no JSON-LD; backfill_schema.py fills it after")
    ap.add_argument("--category", default="Las Vegas Real Estate")
    ap.add_argument("--ui", action="store_true",
                    help="Old way: drive the editor on a focused Chrome tab (needs --tab)")
    ap.add_argument("--tab", type=int, default=4, help="Chrome tab number for --ui (default: 4)")
    ap.add_argument("--no-publish", action="store_true", help="Prepare and list only")
    ap.add_argument("--yes", action="store_true", help="Skip the confirmation prompt")
    ap.add_argument("--force-duplicates", action="store_true",
                    help="Try slugs that already exist in Lofty anyway")
    args = ap.parse_args()

    folder = pb.BLOGS_BASE / args.folder
    if not folder.is_dir():
        print(f"ERROR: Folder not found: {folder}")
        sys.exit(1)
    ln.TAB = f"tab {args.tab}"

    posts = prepare(folder, args.category, parse_filter(args.posts), args.allow_no_schema)
    if args.slugs:
        want = set(args.slugs)
        posts = [p for p in posts if p["slug"] in want]
        for s in sorted(want - {p["slug"] for p in posts}):
            print(f"  [!!] slug not found in folder: {s}")
    print(f"\nFound {len(posts)} posts in {args.folder} (category: {args.category}):")
    for p in posts:
        print(f"  {p['label']}: {p['title'][:60]}")
        print(f"    Slug: {p['slug']}")

    if args.no_publish:
        print("\n--no-publish set. Done.")
        return

    if not args.ui:
        return api_publish(posts, args)

    if not ln.check_accessibility_permission():
        sys.exit(1)
    print(f"\nUsing Chrome {ln.TAB}. Be logged into Lofty on the blog dashboard.")
    if not args.yes and input("Proceed? (y/n): ").strip().lower() != "y":
        print("Cancelled.")
        return

    ln.chrome_activate()

    print("\nChecking for slugs that already exist in Lofty...")
    existing = ln.find_existing_slugs([p["slug"] for p in posts])
    if existing:
        print(f"  Already published: {', '.join(existing)}")
        if not args.force_duplicates:
            posts = [p for p in posts if p["slug"] not in set(existing)]
            print(f"  Skipping those. {len(posts)} left.")
        if not posts:
            print("\nNothing left to publish. Done.")
            return
    elif existing is not None:
        print("  None. All slugs are new.")

    report = []
    for post in posts:
        ln.publish_post(post, report)

    ok = sum(1 for r in report if "OK" in r["status"])
    print(f"\n{'='*60}\nPublished: {ok}/{len(posts)}\n{'='*60}")
    for r in report:
        icon = "OK" if "OK" in r["status"] else "!!"
        print(f"  [{icon}] {r['post']} — /blog/{r['slug']}")


if __name__ == "__main__":
    main()
