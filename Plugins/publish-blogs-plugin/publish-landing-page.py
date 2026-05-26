#!/usr/bin/env python3
"""
Lofty Landing-Page Publisher — drives Chrome via AppleScript against the
already-logged-in tab on https://crm.lofty.com.

Usage:
    python3 publish-landing-page.py the-bluffs-1
    python3 publish-landing-page.py the-bluffs-1 --inspect
    python3 publish-landing-page.py the-bluffs-1 --no-publish --yes
    python3 publish-landing-page.py /path/to/community-folder --tab 4

Requirements: macOS, Google Chrome with View > Developer > Allow JavaScript
from Apple Events enabled, logged into https://crm.lofty.com on the chosen
tab (default: tab 4 of window 1).
"""

import argparse
import sys
import time
from pathlib import Path

# Allow running from anywhere.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lofty_landing_common import (  # noqa: E402
    LOFTY_LANDING_URL, GA_ID, FB_PIXEL_ID, RECON_OUTPUT,
    chrome_js, chrome_activate, switch_to_newest_tab, set_tab,
    wait_for_element, wait_for_text, retry_field,
    set_input_value, click_by_text, click_selector,
    dump_dom,
    find_community_dir, read_builder_name, derive_dev_name, read_seo_block,
    page_display_name, lead_source_name, url_slug,
    read_source_html,
)

SOURCE_FILENAME = "landing-page.html"
IS_BUYER_GUIDE = False
SEO_SECTION_REGEX = r"Community Landing Page|landing-page\.html"
META_TITLE_SUFFIX = " | Ryan Rose"


# ─── Phase 1: page shell ────────────────────────────────────────────────────

def phase1_create_shell(page_name, lead_source):
    print(f"\n[1/15] Navigating to {LOFTY_LANDING_URL} …")
    chrome_js(f"window.location.href = {repr(LOFTY_LANDING_URL)}")
    if not wait_for_text("+ Add a New Landing Page", timeout=20):
        if not wait_for_text("Add a New Landing Page", timeout=5):
            print("  ERROR: dashboard did not load (couldn't find 'Add a New Landing Page' button).")
            dump_dom("phase1-dashboard-load-failed")
            return False
    time.sleep(1)

    print("[2/15] + Add a New Landing Page → Activity → Build Your Own …")
    if not retry_field(lambda: click_by_text("+ Add a New Landing Page")
                       or click_by_text("Add a New Landing Page"),
                       label="Add a New Landing Page"):
        dump_dom("phase1-add-new-failed")
        return False
    time.sleep(1.5)

    if not retry_field(lambda: click_by_text("Activity"), label="Activity"):
        dump_dom("phase1-activity-failed")
        return False
    time.sleep(1)

    if not retry_field(lambda: click_by_text("Build Your Own"),
                       label="Build Your Own"):
        dump_dom("phase1-build-your-own-failed")
        return False
    time.sleep(1.5)

    print(f"[3/15] Page name + Lead Source: '{page_name}' / '{lead_source}'")
    if not wait_for_element("input", timeout=10):
        dump_dom("phase1-shell-form-load-failed")
        return False

    # The page-name input is pre-filled with "New Page(1)" or similar.
    # Find by value-prefix or by being the first text input in the dialog.
    name_set = chrome_js(f"""
    (function(target) {{
        var inputs = document.querySelectorAll('input[type=text], input:not([type])');
        var hit = null;
        for (var i=0; i<inputs.length; i++) {{
            var v = (inputs[i].value || '').trim();
            if (/^New Page/i.test(v) || /^Untitled/i.test(v)) {{ hit = inputs[i]; break; }}
        }}
        if (!hit && inputs.length) hit = inputs[0];
        if (!hit) return 'FAIL: no input';
        hit.focus();
        hit.select();
        var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        setter.call(hit, target);
        hit.dispatchEvent(new InputEvent('input', {{bubbles:true, data:target, inputType:'insertText'}}));
        hit.dispatchEvent(new Event('change', {{bubbles:true}}));
        hit.blur();
        return 'OK: ' + hit.value;
    }})({repr(page_name)})
    """)
    if not name_set or "OK" not in str(name_set):
        print(f"    page name set: {name_set}")
        dump_dom("phase1-page-name-failed")
        return False

    # Lead source: scope for an input near a label that says "Lead Source",
    # type the value, then click "+ Create Source".
    src_typed = chrome_js(f"""
    (function(target) {{
        var labels = Array.from(document.querySelectorAll('label, .el-form-item__label, span'));
        var leadLabel = labels.find(function(l) {{
            return /lead source/i.test((l.textContent || '').trim());
        }});
        if (!leadLabel) return 'FAIL: no lead source label';
        var container = leadLabel.closest('.el-form-item, .form-item, div') || leadLabel.parentElement;
        var input = container.querySelector('input');
        if (!input) return 'FAIL: no input near lead source label';
        input.focus();
        var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        setter.call(input, target);
        input.dispatchEvent(new InputEvent('input', {{bubbles:true, data:target, inputType:'insertText'}}));
        return 'OK: ' + input.value;
    }})({repr(lead_source)})
    """)
    if not src_typed or "OK" not in str(src_typed):
        print(f"    lead source typed: {src_typed}")
        dump_dom("phase1-lead-source-typed-failed")
        return False
    time.sleep(1)

    # Click "+ Create Source <name>" if the option is offered.
    chrome_js(f"""
    (function(target) {{
        var items = document.querySelectorAll('li, .el-select-dropdown__item, .el-cascader-node, button, span');
        for (var i=0; i<items.length; i++) {{
            var t = (items[i].textContent || '').trim();
            if (t.indexOf('Create Source') !== -1 && t.indexOf(target) !== -1) {{
                items[i].click();
                return 'CREATED';
            }}
        }}
        for (var i=0; i<items.length; i++) {{
            var t = (items[i].textContent || '').trim();
            if (t === target) {{ items[i].click(); return 'PICKED'; }}
        }}
        return 'NONE';
    }})({repr(lead_source)})
    """)
    time.sleep(0.7)

    print("[4/15] Save …")
    tabs_before = None
    from _lofty_landing_common import chrome_tab_count
    tabs_before = chrome_tab_count()
    if not retry_field(lambda: click_by_text("Save"), label="Save"):
        dump_dom("phase1-save-failed")
        return False

    # Lofty opens the builder in a new tab. Wait for it.
    for _ in range(20):
        time.sleep(1)
        if chrome_tab_count() > tabs_before:
            break
    if chrome_tab_count() <= tabs_before:
        print("  WARN: no new tab detected after Save — staying on current tab.")
    else:
        switch_to_newest_tab()
        print(f"    switched to newest Chrome tab ({chrome_tab_count()} tabs total)")

    # Wait for the builder canvas to load.
    chrome_activate()
    time.sleep(3)
    return True


# ─── Phases 2-6: TODO_RECON ─────────────────────────────────────────────────
#
# These phases need DOM data from the recon run before we can lock down
# selectors for the drag-and-drop embed block, the form-template list, the
# page-style dropdown, etc. Run with --inspect to dump the relevant panels,
# then we replace these stubs with real selectors.

def phase2_embed_html(html_body, inspect=False):
    print("[5/15] Embed block + paste HTML …  (TODO_RECON)")
    if inspect:
        chrome_js("(function(){var p=document.querySelector('button[aria-label=\"Add\"], .panel-add, .add-button, .icon-add'); if(p) p.click();})()")
        time.sleep(1.5)
        dump_dom("phase2-add-panel-open")
    print("    [stub] needs Lofty +panel selector + Embed item selector + drag mechanism.")
    print("    [stub] needs HTML CODE textarea selector + Update Code button.")
    print("    [stub] needs the two padding fields below Update Code (default 60/20 → 0/0).")
    return False


def phase3_settings(tag_name, meta_title, meta_description, inspect=False):
    print("[6/15] Settings panel …  (TODO_RECON)")
    if inspect:
        dump_dom("phase3-settings-panel-open")
    print("    [stub] needs Settings gear selector + Page Style dropdown + 'No header, no footer' option.")
    print("    [stub] needs Lead Source field, Registration toggle, TAG add, Welcome Email checkbox.")
    print(f"    [stub] would set Meta Title: {meta_title!r}")
    print(f"    [stub] would set Meta Description: {meta_description!r}")
    return False


def phase4_tracking(inspect=False):
    print(f"[7/15] Page tracking — GA={GA_ID}, FB={FB_PIXEL_ID} …  (TODO_RECON)")
    if inspect:
        dump_dom("phase4-tracking-panel-open")
    print("    [stub] needs Google Analytics input + Facebook Pixel input selectors.")
    return False


def phase5_form(tag_name, dest_slug, inspect=False):
    print("[8/15] Lofty form block …  (TODO_RECON)")
    if inspect:
        dump_dom("phase5-form-panel-open")
    print("    [stub] needs +panel → Form → 11th option's stable identifier.")
    print("    [stub] needs form edit pane selectors (heading, title1, TAG, Add Field, Destination URL).")
    print(f"    [stub] would tag the form with: {tag_name!r}")
    print(f"    [stub] would point Destination URL slug at: {dest_slug!r}")
    return False


def phase6_publish(inspect=False):
    print("[9/15] Publish …  (TODO_RECON)")
    if inspect:
        dump_dom("phase6-publish-button-area")
    print("    [stub] needs Publish button selector + post-publish URL capture.")
    return False


# ─── Main ───────────────────────────────────────────────────────────────────

def confirm(prompt, auto_yes):
    if auto_yes:
        return True
    return input(prompt).strip().lower() == "y"


def main():
    parser = argparse.ArgumentParser(
        description="Publish a community landing page to Lofty.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("community", nargs="?",
                        help="Community slug, folder name, or absolute path "
                             "to the community directory.")
    parser.add_argument("--tab", type=int, default=4,
                        help="Chrome tab index to use (default: 4).")
    parser.add_argument("--inspect", action="store_true",
                        help="Recon mode: navigate, dump DOM at key points, "
                             "do not publish. Output: " + str(RECON_OUTPUT))
    parser.add_argument("--no-publish", action="store_true",
                        help="Run through Phases 1-5 but do not click Publish.")
    parser.add_argument("--yes", action="store_true",
                        help="Skip the proceed prompt.")
    parser.add_argument("--builder",
                        help="Override builder short name (e.g. 'Century').")
    parser.add_argument("--dev",
                        help="Override development name (e.g. 'Bluffs 1').")
    args = parser.parse_args()

    if not args.community:
        print("ERROR: community argument required.")
        print("Available communities under /Users/ryanrose/Downloads/Claude/New-Construction/:")
        from _lofty_landing_common import NEW_CONSTRUCTION_BASE
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
        print(f"ERROR: could not derive builder name from "
              f"{community_dir}/research-report.md. Use --builder.")
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

    # Reset recon log on every fresh run so we don't accumulate stale dumps.
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
        # Walk far enough to dump each panel's DOM, but don't try to drag.
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
        print(f"Run with --inspect first; inspect output will be at {RECON_OUTPUT}")
        sys.exit(2)


if __name__ == "__main__":
    main()
