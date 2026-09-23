#!/usr/bin/env python3
"""
Mechanical QA gate for the New Construction buyer guide.

Everything here is a check a human should never have to run by eye. The three
human-judgment audits (does the prose actually read at a 6th-grade level, is the
page break in a sensible place, does this image contain a person) live with the
QA agents. This file owns the checks that are objectively decidable.

    python3 qa-check.py              # all checks
    python3 qa-check.py --strict     # non-zero exit on any WARN as well as FAIL
    python3 qa-check.py --only emdash,print-css

Exit code 0 = every FAIL-level check passed.
"""

import argparse
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(HERE, "new-construction-buyer-guide.html")
PDF = os.path.join(HERE, "new-construction-buyer-guide.pdf")
LANDING = os.path.join(HERE, "landing-page.html")

PASS, WARN, FAIL, SKIP = "PASS", "WARN", "FAIL", "SKIP"
results = []


def record(status, name, detail=""):
    results.append((status, name, detail))


def read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def text_files():
    pats = ["*.html", "*.md", "*.json", "build/**/*.html", "build/**/*.svg",
            "build/**/*.json", "research/**/*.md", "outline/*.md", "design/**/*.html",
            "design/**/*.md", "snapshot/**/*.md", "assets/*.md"]
    out = set()
    for p in pats:
        out.update(glob.glob(os.path.join(HERE, p), recursive=True))
    return sorted(f for f in out if os.path.isfile(f))


# --------------------------------------------------------------------- em-dash
def check_emdash():
    """Hard workspace rule, zero tolerance. The risk is not the writers; it is
    quoted builder marketing and BBB text carried in through research."""
    hits = []
    for f in text_files():
        body = read(f)
        for i, line in enumerate(body.splitlines(), 1):
            if "—" in line:
                hits.append(f"{os.path.relpath(f, HERE)}:{i}")
            if re.search(r"&mdash;|&#8212;|&#x2014;", line, re.I):
                hits.append(f"{os.path.relpath(f, HERE)}:{i} (entity)")
    if hits:
        record(FAIL, "em-dash: source files", f"{len(hits)} occurrences: " + ", ".join(hits[:12]))
    else:
        record(PASS, "em-dash: source files", f"{len(text_files())} files clean")

    if not os.path.isfile(PDF):
        record(SKIP, "em-dash: extracted PDF text", "no PDF yet")
        return
    try:
        import pypdf
        txt = "".join((p.extract_text() or "") for p in pypdf.PdfReader(PDF).pages)
        n = txt.count("—")
        record(PASS if n == 0 else FAIL, "em-dash: extracted PDF text", f"{n} found")
    except Exception as e:
        record(WARN, "em-dash: extracted PDF text", f"could not extract: {e}")


def check_endash():
    """En-dashes are legal, but only inside numeric ranges. Used as punctuation
    they are an em-dash wearing a disguise."""
    bad = []
    for f in text_files():
        for i, line in enumerate(read(f).splitlines(), 1):
            for m in re.finditer(r"(.{0,12})–(.{0,12})", line):
                before, after = m.group(1), m.group(2)
                if not (re.search(r"[\d]\s*$", before) and re.search(r"^\s*[\d$]", after)):
                    bad.append(f"{os.path.relpath(f, HERE)}:{i} ...{m.group(0)}...")
    if bad:
        record(WARN, "en-dash used as punctuation", f"{len(bad)}: " + "; ".join(bad[:6]))
    else:
        record(PASS, "en-dash used as punctuation", "none, or numeric ranges only")


# ------------------------------------------------------------------- print CSS
def check_print_css():
    if not os.path.isfile(HTML):
        record(SKIP, "print CSS", "guide not built yet")
        return
    css = read(HTML)

    if re.search(r"@page\s*\{[^}]*size\s*:\s*letter", css, re.I):
        record(PASS, "print CSS: @page size letter", "")
    else:
        record(FAIL, "print CSS: @page size letter", "missing @page { size: letter }")

    if re.search(r"print-color-adjust\s*:\s*exact", css, re.I):
        record(PASS, "print CSS: print-color-adjust exact", "")
    else:
        record(FAIL, "print CSS: print-color-adjust exact",
               "backgrounds and accent fills will drop out on print")

    n_avoid = len(re.findall(r"break-inside\s*:\s*avoid", css, re.I))
    record(PASS if n_avoid >= 5 else WARN, "print CSS: break-inside avoid",
           f"{n_avoid} rules (cards, tables, callouts, figures should each have one)")

    if re.search(r"break-after\s*:\s*page", css, re.I):
        record(PASS, "print CSS: page-break utility", "")
    else:
        record(FAIL, "print CSS: page-break utility", "no break-after: page rule")

    if re.search(r"thead\s*\{[^}]*display\s*:\s*table-header-group", css, re.I) or \
       re.search(r"display\s*:\s*table-header-group", css, re.I):
        record(PASS, "print CSS: thead repeats across pages", "")
    else:
        record(FAIL, "print CSS: thead repeats across pages",
               "builder table will split without its header")

    if re.search(r"position\s*:\s*fixed", css, re.I):
        record(FAIL, "print CSS: no position fixed",
               "fixed elements repeat on every printed page")
    else:
        record(PASS, "print CSS: no position fixed", "")

    # The bug that has shipped twice in this workspace: an absolutely positioned
    # ::before bullet gets dropped onto the first letter under CSS multi-column.
    for m in re.finditer(r"li::before\s*\{([^}]*)\}", css, re.I):
        if re.search(r"position\s*:\s*absolute", m.group(1), re.I):
            record(FAIL, "print CSS: li::before not absolutely positioned",
                   "known bug, use the flexbox bullet pattern instead")
            break
    else:
        record(PASS, "print CSS: li::before not absolutely positioned", "")


# ----------------------------------------------------------------------- PDF
def check_pdf():
    if not os.path.isfile(PDF):
        record(SKIP, "PDF geometry", "no PDF yet")
        return
    out = subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout
    pages = re.search(r"^Pages:\s+(\d+)", out, re.M)
    size = re.search(r"^Page size:\s+([\d.]+) x ([\d.]+)", out, re.M)

    if pages:
        n = int(pages.group(1))
        # 39 content pages from guide-outline.md plus a 5 page source appendix
        # generated by assemble.py. The original 32 to 40 window predated the
        # appendix; this folder's CLAUDE.md has described a 44 page guide since the
        # design rounds, and the design sample's own running foot already pointed
        # at "the source appendix, page 41".
        record(PASS if 42 <= n <= 46 else FAIL, "PDF page count", f"{n} (target 42-46)")
    if size:
        w, h = round(float(size.group(1))), round(float(size.group(2)))
        record(PASS if (w, h) == (612, 792) else FAIL, "PDF page size", f"{w} x {h} pts (want 612 x 792)")

    try:
        import fitz
        doc = fitz.open(PDF)
        blanks = []
        for i, page in enumerate(doc, 1):
            if not page.get_text().strip():
                pix = page.get_pixmap(dpi=36)
                if len(set(pix.samples)) <= 2:      # effectively one flat color
                    blanks.append(i)
        record(PASS if not blanks else FAIL, "PDF blank pages",
               "none" if not blanks else f"pages {blanks}")
        doc.close()
    except Exception as e:
        record(WARN, "PDF blank pages", f"check skipped: {e}")


def check_table_header_repeat():
    """If the builder table spans pages, its header row must appear on each."""
    if not (os.path.isfile(PDF) and os.path.isfile(HTML)):
        record(SKIP, "builder table header repeat", "not built yet")
        return
    try:
        import fitz
        doc = fitz.open(PDF)
        # Two fixes here. The column names are the ones that actually shipped, read
        # off p33/p34; the original check looked for "In-house lender" and "Build
        # timeline", planned names that were never built. And the comparison is done
        # against a space-stripped copy of the text, because the column headers are
        # uppercase with letter-spacing, and a PDF text layer records that as
        # "L E N D E R  T I E". Matching the literal string reported "table not
        # located" on a table that was sitting right there.
        def squash(s):
            return re.sub(r"\s+", "", s).lower()

        texts = [squash(p.get_text()) for p in doc]
        pages_with = [i for i, t in enumerate(texts, 1) if squash("Lender tie") in t]
        pages_with_builder = [
            i for i, t in enumerate(texts, 1)
            if squash("Warranty as published") in t and squash("Price band") in t
        ]
        doc.close()
        if not pages_with_builder:
            record(WARN, "builder table header repeat", "table not located in PDF text")
        elif len(pages_with_builder) == 1:
            record(PASS, "builder table header repeat", "table fits on one page")
        else:
            ok = len(pages_with) >= len(pages_with_builder)
            record(PASS if ok else FAIL, "builder table header repeat",
                   f"header on {len(pages_with)} of {len(pages_with_builder)} table pages")
    except Exception as e:
        record(WARN, "builder table header repeat", f"skipped: {e}")


# ------------------------------------------------------------- accessibility
def check_a11y():
    for label, path in (("guide", HTML), ("landing page", LANDING)):
        if not os.path.isfile(path):
            record(SKIP, f"a11y: {label}", "not built yet")
            continue
        doc = read(path)

        if re.search(r"<html[^>]+lang\s*=", doc, re.I):
            record(PASS, f"a11y: {label} html lang", "")
        else:
            record(FAIL, f"a11y: {label} html lang", "missing lang attribute")

        imgs = re.findall(r"<img\b[^>]*>", doc, re.I)
        noalt = [t for t in imgs if not re.search(r'\balt\s*=\s*"[^"]+"', t, re.I)]
        record(PASS if not noalt else FAIL, f"a11y: {label} image alt text",
               f"{len(imgs) - len(noalt)}/{len(imgs)} have non-empty alt")

        svgs = re.findall(r"<svg\b.*?</svg>", doc, re.I | re.S)
        bad = [s for s in svgs if not (re.search(r'role\s*=\s*"img"', s, re.I)
                                       and "<title" in s.lower() and "<desc" in s.lower())]
        if svgs:
            record(PASS if not bad else FAIL, f"a11y: {label} inline svg labels",
                   f"{len(svgs) - len(bad)}/{len(svgs)} have role+title+desc")

        tables = re.findall(r"<table\b.*?</table>", doc, re.I | re.S)
        if tables:
            no_scope = [t for t in tables if "<th" in t.lower() and "scope=" not in t.lower()]
            no_cap = [t for t in tables if "<caption" not in t.lower()]
            record(PASS if not no_scope else FAIL, f"a11y: {label} th scope",
                   f"{len(tables) - len(no_scope)}/{len(tables)} tables scoped")
            record(PASS if not no_cap else WARN, f"a11y: {label} table caption",
                   f"{len(tables) - len(no_cap)}/{len(tables)} tables captioned")

        vague = re.findall(r">\s*(click here|read more|learn more)\s*<", doc, re.I)
        record(PASS if not vague else WARN, f"a11y: {label} link text",
               "descriptive" if not vague else f"{len(vague)} vague link labels")


# --------------------------------------------------------------- compliance
def check_compliance():
    if not os.path.isfile(HTML):
        record(SKIP, "compliance", "guide not built yet")
        return
    doc = read(HTML)

    n_broker = len(re.findall(r"Real Broker,?\s*LLC", doc, re.I))
    record(PASS if n_broker >= 3 else FAIL, "NRS 645 brokerage identification",
           f'"Real Broker, LLC" appears {n_broker}x (need cover, note page, back matter)')

    for label, pat in (("phone", r"702[.\-\s]?747[.\-\s]?5921"),
                       ("email", r"ryan@rosehomeslv\.com")):
        record(PASS if re.search(pat, doc, re.I) else FAIL,
               f"contact: {label}", "present" if re.search(pat, doc, re.I) else "missing")

    # Excluded geography. A bare keyword count cannot tell a violation from a
    # disclosure, and the guide has to be able to SAY these places are out of scope:
    # the area schematic states they are not drawn, and the market snapshot has to
    # admit that county level medians include them. Those are honesty, not leakage.
    # So a mention passes only when exclusion language sits next to it.
    excluded_ok = re.compile(
        r"(outside|not drawn|excluded?|not (?:in|part of|cover)|beyond|"
        r"sit inside these|does not (?:include|cover))", re.I)
    for term in ("Pahrump", "Mesquite", "Boulder City"):
        hits = [m.start() for m in re.finditer(term, doc, re.I)]
        bare = []
        for pos in hits:
            window = doc[max(0, pos - 240):pos + 240]
            if not excluded_ok.search(window):
                bare.append(pos)
        if not hits:
            record(PASS, f"excluded area: {term}", "no mentions")
        elif not bare:
            record(PASS, f"excluded area: {term}",
                   f"{len(hits)} mentions, all disclosures of exclusion")
        else:
            record(FAIL, f"excluded area: {term}",
                   f"{len(bare)} of {len(hits)} mentions are NOT framed as excluded")

    # CTA counting. The original check looked for cta-primary / cta-seller classes
    # that were never in the design system, so this gate silently reported zero on a
    # guide that carries six CTAs. The blocks now carry data-cta, which is semantics
    # without a visual class, and the plan's "exactly one seller CTA" gate can fire.
    n_primary = len(re.findall(r'data-cta="primary"', doc))
    n_seller = len(re.findall(r'data-cta="seller"', doc))
    record(PASS if n_primary >= 4 else FAIL, "primary CTA placements",
           f"{n_primary} (outline plans 5: p4, p9, p17, p27, p38)")
    record(PASS if n_seller == 1 else FAIL, "seller CTA appears exactly once",
           f"{n_seller} (must be exactly 1, inside Path B only)")

    if re.search(r"third[- ]party", doc, re.I) and re.search(r"not.{0,40}opinion", doc, re.I):
        record(PASS, "builder table disclaimer", "third-party findings language present")
    else:
        record(FAIL, "builder table disclaimer",
               "missing the third-party-findings / not-an-opinion disclaimer")


def check_citations():
    tbl = os.path.join(HERE, "research", "builder-table.md")
    if not os.path.isfile(tbl):
        record(SKIP, "builder table citations", "table not built yet")
        return
    doc = read(tbl)
    urls = len(re.findall(r"https?://", doc))
    verified = len(re.findall(r"verified:", doc, re.I))
    notfound = len(re.findall(r"NOT FOUND", doc))
    record(PASS if urls >= 20 else WARN, "builder table: source URLs", f"{urls} URLs")
    record(PASS if verified >= 20 else WARN, "builder table: verified-as-of stamps", f"{verified}")
    record(PASS, "builder table: NOT FOUND cells", f"{notfound} (expected, not a defect)")

    banned = re.findall(r"\b(best builder|worst|top[- ]rated|#1|our pick|we recommend)\b", doc, re.I)
    record(PASS if not banned else FAIL, "builder table: no ranking language",
           "clean" if not banned else f"found: {set(w.lower() for w in banned)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="treat WARN as failure")
    ap.add_argument("--only", default="", help="comma list: emdash,print-css,pdf,a11y,compliance,citations")
    args = ap.parse_args()

    checks = {
        "emdash": [check_emdash, check_endash],
        "print-css": [check_print_css],
        "pdf": [check_pdf, check_table_header_repeat],
        "a11y": [check_a11y],
        "compliance": [check_compliance],
        "citations": [check_citations],
    }
    selected = [k.strip() for k in args.only.split(",") if k.strip()] or list(checks)

    for key in selected:
        for fn in checks.get(key, []):
            fn()

    width = max(len(n) for _, n, _ in results) + 2
    icon = {PASS: "  ok  ", WARN: " WARN ", FAIL: " FAIL ", SKIP: " skip "}
    print()
    for status, name, detail in results:
        print(f"[{icon[status]}] {name.ljust(width)} {detail}")

    n_fail = sum(1 for s, _, _ in results if s == FAIL)
    n_warn = sum(1 for s, _, _ in results if s == WARN)
    n_skip = sum(1 for s, _, _ in results if s == SKIP)
    print(f"\n{len(results)} checks: {len(results)-n_fail-n_warn-n_skip} pass, "
          f"{n_warn} warn, {n_fail} fail, {n_skip} skipped")

    sys.exit(1 if n_fail or (args.strict and n_warn) else 0)


if __name__ == "__main__":
    main()
