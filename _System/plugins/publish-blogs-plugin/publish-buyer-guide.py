#!/usr/bin/env python3
"""
Lofty Buyer-Guide Publisher — uploads buyer-guide.html into Lofty as a
landing page with " BG" suffixed naming. Otherwise identical to
publish-landing-page.py.

Usage:
    python3 publish-buyer-guide.py the-bluffs-1
    python3 publish-buyer-guide.py the-bluffs-1 --inspect
    python3 publish-buyer-guide.py the-bluffs-1 --no-publish --yes
"""

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lofty_landing_common import (  # noqa: E402
    LOFTY_LANDING_URL, GA_ID, FB_PIXEL_ID, RECON_OUTPUT,
    chrome_js, chrome_activate, switch_to_newest_tab, set_tab,
    wait_for_element, wait_for_text, retry_field,
    set_input_value, click_by_text, click_selector,
    dump_dom,
    find_community_dir, read_builder_name, derive_dev_name, read_seo_block,
    page_display_name, lead_source_name, url_slug,
    read_source_html, NEW_CONSTRUCTION_BASE, chrome_tab_count,
)

# Re-import phase functions from the landing-page driver — they're identical.
import importlib.util
_lp_spec = importlib.util.spec_from_file_location(
    "publish_landing_page",
    str(Path(__file__).resolve().parent / "publish-landing-page.py"),
)
_lp = importlib.util.module_from_spec(_lp_spec)
_lp_spec.loader.exec_module(_lp)
phase1_create_shell = _lp.phase1_create_shell
phase2_embed_html = _lp.phase2_embed_html
phase3_settings = _lp.phase3_settings
phase4_tracking = _lp.phase4_tracking
phase5_form = _lp.phase5_form
phase6_publish = _lp.phase6_publish

SOURCE_FILENAME = "buyer-guide.html"
IS_BUYER_GUIDE = True
SEO_SECTION_REGEX = r"Buyer Guide Landing Page|buyer-guide(?:-landing-page)?\.html"
META_TITLE_SUFFIX = " | Ryan Rose"


def confirm(prompt, auto_yes):
    if auto_yes:
        return True
    return input(prompt).strip().lower() == "y"


def main():
    parser = argparse.ArgumentParser(
        description="Publish a community buyer guide to Lofty (with ' BG' "
                    "suffix on page name, lead source, tag, and URL slug).",
    )
    parser.add_argument("community", nargs="?",
                        help="Community slug, folder name, or absolute path.")
    parser.add_argument("--tab", type=int, default=4)
    parser.add_argument("--inspect", action="store_true")
    parser.add_argument("--no-publish", action="store_true")
    parser.add_argument("--yes", action="store_true")
    parser.add_argument("--builder")
    parser.add_argument("--dev")
    args = parser.parse_args()

    if not args.community:
        print("ERROR: community argument required.")
        print("Available communities:")
        for d in sorted(NEW_CONSTRUCTION_BASE.iterdir()):
            if d.is_dir() and (d / SOURCE_FILENAME).exists():
                print(f"  - {d.name}")
        sys.exit(1)

    set_tab(f"tab {args.tab}")

    community_dir = find_community_dir(args.community)
    if not community_dir:
        print(f"ERROR: community not found: {args.community}")
        sys.exit(1)

    source_path = community_dir / SOURCE_FILENAME
    if not source_path.exists():
        print(f"ERROR: missing {source_path}")
        sys.exit(1)

    builder = args.builder or read_builder_name(community_dir)
    if not builder:
        print(f"ERROR: could not derive builder name. Use --builder.")
        sys.exit(1)
    dev = args.dev or derive_dev_name(community_dir, builder_short=builder)
    if not dev:
        print(f"ERROR: could not derive development name. Use --dev.")
        sys.exit(1)

    page_name = page_display_name(builder, dev, IS_BUYER_GUIDE)
    lead_source = lead_source_name(builder, dev, IS_BUYER_GUIDE)
    slug = url_slug(builder, dev, IS_BUYER_GUIDE)
    meta_title, meta_desc = read_seo_block(community_dir, SEO_SECTION_REGEX)
    if meta_title and not meta_title.endswith(META_TITLE_SUFFIX):
        meta_title = meta_title + META_TITLE_SUFFIX

    html_body = read_source_html(community_dir, SOURCE_FILENAME)

    if RECON_OUTPUT.exists():
        RECON_OUTPUT.unlink()

    print()
    print(f"Source:      {source_path}  ({len(html_body or ''):,} chars)")
    print(f"Builder:     {builder}")
    print(f"Dev name:    {dev}")
    print(f"Page name:   {page_name}")
    print(f"Lead source: {lead_source}")
    print(f"URL slug:    {slug}")
    print(f"Meta title:  {meta_title or '(missing — will fail Phase 3)'}")
    print(f"Meta desc:   {(meta_desc or '(missing — will fail Phase 3)')[:80]}")
    print(f"Mode:        {'INSPECT (recon, no publish)' if args.inspect else ('NO-PUBLISH' if args.no_publish else 'FULL PUBLISH')}")
    print(f"Chrome tab:  tab {args.tab}")
    print()
    print("Make sure Chrome is logged into https://crm.lofty.com on the chosen tab.")
    if not confirm("Proceed? (y/n): ", args.yes):
        print("Cancelled.")
        return

    chrome_activate()

    if not phase1_create_shell(page_name, lead_source):
        print("\nPhase 1 failed. Recon dump (if any) at: " + str(RECON_OUTPUT))
        sys.exit(2)

    if args.inspect:
        phase2_embed_html(html_body, inspect=True)
        phase3_settings(lead_source, meta_title, meta_desc, inspect=True)
        phase4_tracking(inspect=True)
        phase5_form(lead_source, slug, inspect=True)
        phase6_publish(inspect=True)
        print(f"\nINSPECT complete. Recon dump at: {RECON_OUTPUT}")
        return

    ok = phase2_embed_html(html_body)
    ok = phase3_settings(lead_source, meta_title, meta_desc) and ok
    ok = phase4_tracking() and ok
    ok = phase5_form(lead_source, slug) and ok
    if args.no_publish:
        print("\n--no-publish set; stopping before Phase 6.")
        return
    ok = phase6_publish() and ok

    if ok:
        print(f"\nPUBLISHED: {page_name}")
    else:
        print(f"\nIncomplete — Phases 2-6 still need recon-locked selectors.")
        sys.exit(2)


if __name__ == "__main__":
    main()
