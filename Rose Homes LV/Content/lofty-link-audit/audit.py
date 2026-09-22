#!/usr/bin/env python3
"""
Audit rosehomeslv.com blog posts for internal links missing the /blog/ prefix.
For each post, identify links of the form href="/<slug>" where /<slug> 404s
but /blog/<slug> would 200.
"""
import urllib.request
import urllib.parse
import re
import json
import sys
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
BASE = "https://www.rosehomeslv.com"

def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return 0, f"ERR:{e}"

def status(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        # Some servers reject HEAD; fall back to GET
        try:
            req2 = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req2, timeout=timeout) as r:
                return r.status
        except urllib.error.HTTPError as e:
            return e.code
        except Exception:
            return 0

def get_blog_post_urls():
    """Try sitemap first, then fall back to crawling /blog index."""
    urls = set()
    # Try sitemaps
    candidates = ["/sitemap.xml", "/sitemap_index.xml", "/blog/sitemap.xml", "/sitemap-blog.xml"]
    for path in candidates:
        code, body = fetch(BASE + path)
        if code == 200 and "<" in body:
            try:
                root = ET.fromstring(body)
                # Sitemap index?
                ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                # Direct urlset
                for loc in root.findall(".//sm:url/sm:loc", ns):
                    u = (loc.text or "").strip()
                    if "/blog/" in u and u.startswith(BASE):
                        urls.add(u)
                # Sub-sitemaps
                for loc in root.findall(".//sm:sitemap/sm:loc", ns):
                    sub = (loc.text or "").strip()
                    code2, body2 = fetch(sub)
                    if code2 == 200:
                        try:
                            sub_root = ET.fromstring(body2)
                            for loc2 in sub_root.findall(".//sm:url/sm:loc", ns):
                                u = (loc2.text or "").strip()
                                if "/blog/" in u and u.startswith(BASE):
                                    urls.add(u)
                        except ET.ParseError:
                            pass
            except ET.ParseError:
                pass
            if urls:
                break
    if urls:
        return sorted(urls)

    # Fallback: crawl /blog index pages
    for page in range(1, 30):
        url = f"{BASE}/blog" if page == 1 else f"{BASE}/blog?page={page}"
        code, body = fetch(url)
        if code != 200:
            break
        found = re.findall(r'href="(/blog/[a-z0-9][a-z0-9\-]*)"', body)
        new = {BASE + p for p in found}
        before = len(urls)
        urls |= new
        if len(urls) == before:
            break
    return sorted(urls)

LINK_RE = re.compile(r'href="(/[^"#?\s][^"]*)"')
BAD_LINK_RE = re.compile(r'href="(/[a-z0-9][a-z0-9\-]+)"')

# Heuristic to decide a link is a candidate to be a missing /blog/ prefix:
# - starts with / and is a single path segment (no further slashes)
# - not /blog (we'd skip /blog itself)
# - not in a known short-list of legitimate root paths
ROOT_ALLOWED = {
    "/", "/blog", "/listing", "/featured-listing", "/sold-listing", "/sell",
    "/evaluation", "/about", "/contact", "/affordability-calculator-1",
    "/mortgage-calculator", "/sitemap", "/accessibility",
}

def candidate_bad_links(html):
    """Return ordered unique list of candidate links missing /blog/ prefix."""
    seen = []
    seen_set = set()
    for m in BAD_LINK_RE.finditer(html):
        href = m.group(1)
        if href in ROOT_ALLOWED:
            continue
        # single-segment path only (no slashes after the leading one)
        if "/" in href[1:]:
            continue
        # skip /las-vegas-NV/... style — already filtered (multi-segment)
        if href in seen_set:
            continue
        seen_set.add(href)
        seen.append(href)
    return seen

def isolate_article_html(html):
    """Try to extract just the article body so we don't flag nav/footer links."""
    # Look for <article ...>...</article>
    m = re.search(r"<article\b[^>]*>(.*?)</article>", html, flags=re.S | re.I)
    if m:
        return m.group(1)
    # Fall back to a div with class blog content
    m = re.search(r'<div[^>]+class="[^"]*(?:blog|post|entry|content)[^"]*"[^>]*>(.*?)</div>\s*</div>', html, flags=re.S | re.I)
    if m:
        return m.group(1)
    return html

def audit_post(post_url):
    code, html = fetch(post_url)
    if code != 200:
        return {"url": post_url, "status": code, "candidates": [], "broken": [], "fixable": []}
    body = isolate_article_html(html)
    cands = candidate_bad_links(body)
    return {"url": post_url, "status": code, "candidates": cands, "html_len": len(html), "body_len": len(body)}

def main():
    print("[1/3] Enumerating blog posts...", file=sys.stderr)
    posts = get_blog_post_urls()
    print(f"  found {len(posts)} blog post URLs", file=sys.stderr)
    with open("/tmp/lofty-audit/posts.txt", "w") as f:
        f.write("\n".join(posts))

    print("[2/3] Auditing each post for candidate broken links...", file=sys.stderr)
    results = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(audit_post, u): u for u in posts}
        for i, fut in enumerate(as_completed(futs), 1):
            r = fut.result()
            results.append(r)
            if i % 10 == 0 or i == len(posts):
                print(f"  audited {i}/{len(posts)}", file=sys.stderr)

    print("[3/3] Verifying which candidates are actually broken (404 at root, 200 at /blog/)...", file=sys.stderr)
    # Collect unique candidate slugs across all posts
    all_cands = set()
    for r in results:
        for c in r.get("candidates", []):
            all_cands.add(c)
    print(f"  {len(all_cands)} unique candidate slugs to verify", file=sys.stderr)

    # Verify each candidate slug
    verdict = {}  # slug -> "fixable" | "ok" | "unknown"
    def verify(slug):
        root_code = status(BASE + slug)
        blog_code = status(BASE + "/blog" + slug)
        if root_code == 404 and blog_code == 200:
            return slug, "fixable", root_code, blog_code
        if root_code == 200:
            return slug, "ok-as-is", root_code, blog_code
        if blog_code == 200:
            return slug, "fixable", root_code, blog_code
        return slug, "unknown", root_code, blog_code

    with ThreadPoolExecutor(max_workers=10) as ex:
        futs = [ex.submit(verify, c) for c in sorted(all_cands)]
        for i, fut in enumerate(as_completed(futs), 1):
            slug, v, rc, bc = fut.result()
            verdict[slug] = (v, rc, bc)
            if i % 20 == 0 or i == len(all_cands):
                print(f"  verified {i}/{len(all_cands)}", file=sys.stderr)

    # Summarize per-post
    posts_with_fixes = []
    for r in results:
        fixable = []
        for c in r.get("candidates", []):
            v, rc, bc = verdict.get(c, ("unknown", 0, 0))
            if v == "fixable":
                fixable.append({"from": c, "to": "/blog" + c, "root_status": rc, "blog_status": bc})
        if fixable:
            posts_with_fixes.append({"url": r["url"], "fixable": fixable})

    out = {
        "total_posts": len(posts),
        "posts_with_broken_links": len(posts_with_fixes),
        "unique_fixable_slugs": sum(1 for v in verdict.values() if v[0] == "fixable"),
        "details": posts_with_fixes,
        "verdict_summary": {
            "fixable": sum(1 for v in verdict.values() if v[0] == "fixable"),
            "ok-as-is": sum(1 for v in verdict.values() if v[0] == "ok-as-is"),
            "unknown": sum(1 for v in verdict.values() if v[0] == "unknown"),
        }
    }
    with open("/tmp/lofty-audit/report.json", "w") as f:
        json.dump(out, f, indent=2)

    print("\n=== SUMMARY ===")
    print(f"Total blog posts found:          {out['total_posts']}")
    print(f"Posts with broken /<slug> links: {out['posts_with_broken_links']}")
    print(f"Unique broken slugs (fixable):   {out['verdict_summary']['fixable']}")
    print(f"Slugs ok at root as-is:          {out['verdict_summary']['ok-as-is']}")
    print(f"Slugs that are 404 everywhere:   {out['verdict_summary']['unknown']}")
    print(f"\nReport written to /tmp/lofty-audit/report.json")

if __name__ == "__main__":
    main()
