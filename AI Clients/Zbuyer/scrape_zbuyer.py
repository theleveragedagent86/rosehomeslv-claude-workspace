"""
Zbuyer lead scraper.

Usage:
    pip install -r requirements.txt
    playwright install chromium
    python scrape_zbuyer.py

First run: a Chromium window opens. Log in manually at app.zbuyer.com,
then return to the terminal and press Enter. Subsequent runs reuse the
saved session in ./.zbuyer_session/.

Scrapes pages 1..LAST_PAGE, stopping after STOP_NAME is captured.
Appends to leads.csv as it goes; re-running skips leads already saved
(dedupe by name+email) so credits aren't burned re-revealing numbers.

Selectors are intentionally loose (text-based + role-based) since the
exact DOM is confirmed at runtime. Adjust the SELECTOR_* constants below
if anything misses on first run.
"""

import csv
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from playwright.sync_api import (
    Page,
    Playwright,
    TimeoutError as PWTimeout,
    sync_playwright,
)

ROOT = Path(__file__).parent
SESSION_DIR = ROOT / ".zbuyer_session"
CSV_PATH = ROOT / "leads.csv"

START_URL = "https://app.zbuyer.com/leads/prospecting"
LAST_PAGE = 13
STOP_NAME = "Guadalupe Vincent"

CSV_FIELDS = [
    "scraped_at",
    "lead_type",
    "name",
    "email",
    "phone",
    "street",
    "city_state_zip",
    "summary_line",
    "last_updated",
    "bedrooms",
    "bathrooms",
    "size_sqft",
    "year_built",
    "avm_low",
    "avm_high",
    "avm_estimate",
    "reason_selling",
    "lead_description",
    "public_data",
    "page_num",
]

PHONE_RE = re.compile(r"\(?\d{3}\)?[\s\-.]?\d{3}[\s\-.]?\d{4}")
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
LAST_UPDATED_RE = re.compile(r"Last updated\s+([0-9/]+)", re.I)
SIZE_RE = re.compile(r"Size:\s*([\d,]+)\s*SqFt", re.I)
BUILT_RE = re.compile(r"Built:\s*(\d{4})", re.I)
AVM_RE = re.compile(
    r"Automated Valuation Range:\s*\$?([\d,]+)\s*-\s*\$?([\d,]+).*?Estimated at\s*\$?([\d,]+)",
    re.I | re.S,
)
REASON_RE = re.compile(r"Reason Selling:\s*([^\n]+)", re.I)


def load_seen() -> set:
    seen = set()
    if CSV_PATH.exists():
        with CSV_PATH.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                seen.add((row.get("name", "").strip(), row.get("email", "").strip()))
    return seen


def open_csv_writer():
    new_file = not CSV_PATH.exists()
    f = CSV_PATH.open("a", newline="", encoding="utf-8")
    writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
    if new_file:
        writer.writeheader()
        f.flush()
    return f, writer


def ensure_logged_in(page: Page) -> None:
    page.goto(START_URL, wait_until="domcontentloaded")
    page.wait_for_timeout(1500)

    def looks_logged_in() -> bool:
        # Logged-in prospecting list shows "Last updated" on every row.
        try:
            if page.locator("text=/Last updated/i").first.is_visible(timeout=1500):
                return True
        except Exception:
            pass
        try:
            if page.locator("text=/Prospecting List/i").first.is_visible(timeout=800):
                return True
        except Exception:
            pass
        return False

    if looks_logged_in():
        return

    print("\n" + "=" * 60)
    print(">>> Please log in to zbuyer.com in the Chromium window.")
    print(">>> Navigate to the leads dashboard so you can see lead rows.")
    print(">>> Then come back here and press Enter to continue.")
    print("=" * 60)
    input(">>> Press Enter once you're on the leads page... ")

    # Re-confirm. If still not logged in, let the user try again.
    for _ in range(3):
        if looks_logged_in():
            return
        page.wait_for_timeout(1000)
        if looks_logged_in():
            return
        input(
            ">>> Still don't see leads. Make sure the dashboard is loaded, "
            "then press Enter again... "
        )
    print("!! Proceeding anyway — scraping may fail if not logged in.")


def goto_page(page: Page, page_num: int) -> None:
    """Navigate to a leads-list page. Prefer clicking pagination (same SPA state)."""
    if page_num == 1:
        try:
            page.goto(START_URL, wait_until="domcontentloaded", timeout=15000)
            page.wait_for_selector("text=/Last updated/i", timeout=10000)
        except Exception:
            pass
        return

    # Ensure we're on the prospecting list before paginating.
    if "prospecting" not in page.url.lower():
        try:
            page.goto(START_URL, wait_until="domcontentloaded", timeout=15000)
            page.wait_for_selector("text=/Last updated/i", timeout=10000)
        except Exception:
            pass

    # Try clicking a pagination control with this number.
    for getter in (
        lambda: page.get_by_role("button", name=str(page_num), exact=True).first,
        lambda: page.get_by_role("link", name=str(page_num), exact=True).first,
        lambda: page.locator(f'[aria-label="Page {page_num}"]').first,
        lambda: page.locator("nav").get_by_text(str(page_num), exact=True).first,
    ):
        try:
            el = getter()
            if el.is_visible(timeout=1000):
                el.scroll_into_view_if_needed(timeout=1500)
                el.click(timeout=3000)
                page.wait_for_timeout(1200)
                return
        except Exception:
            continue

    # Fallback: click "Next" (page_num - current) times.
    try:
        for _ in range(page_num):
            nxt = page.get_by_role("button", name=re.compile("^next$", re.I)).first
            if nxt.is_visible(timeout=1000):
                nxt.click(timeout=2000)
                page.wait_for_timeout(800)
    except Exception:
        print(f"  ! Could not navigate to page {page_num}.")


def list_lead_rows(page: Page):
    """Return locators for each lead row card visible on the current page."""
    page.wait_for_timeout(500)
    # Each row contains a "Last updated <date>" line. Find the nearest card
    # ancestor that also contains a tag like "Buyer"/"Seller".
    rows = page.locator(
        'xpath=//*[contains(normalize-space(.), "Last updated")]'
        '[.//*[normalize-space(text())="Buyer" or normalize-space(text())="Seller"]]'
        '[not(.//*[contains(normalize-space(.), "Last updated") and '
        './/*[normalize-space(text())="Buyer" or normalize-space(text())="Seller"]])]'
    )
    return rows


def get_row_name(row) -> str:
    """Row layout: tag line(s) ('Buyer'/'Seller [Cash Offer]'), NAME, descriptor, 'Last updated ...'."""
    try:
        text = row.text_content(timeout=2000) or ""
    except PWTimeout:
        return ""
    skip_exact = {"Buyer", "Seller", "Cash Offer", "Cash Value", "New", "Prospecting Lead"}
    skip_prefix = ("Buying", "Selling", "Last updated", "Reason", "Cash Value",
                   "Thinking about", "Curious about", "Size:", "Built:", "$")
    for line in (l.strip() for l in text.splitlines()):
        if not line:
            continue
        if line in skip_exact:
            continue
        if line.startswith(skip_prefix):
            continue
        # Names don't contain $ or pure-digit content.
        if "$" in line or line.replace(",", "").replace(".", "").isdigit():
            continue
        return line
    return ""


def open_lead(page: Page, row, list_url: str) -> bool:
    """Detail view renders in place (no URL change). Detect via content signals."""
    try:
        row.scroll_into_view_if_needed(timeout=3000)
        row.click(timeout=5000)
        # Wait for detail-only content to appear in the DOM (ignore CSS visibility).
        page.wait_for_function(
            """() => {
                const t = document.body.innerText || '';
                // Detail view has 'Lead Description' AND either 'Prospecting Lead'
                // header or a visible 'Back' control. List view has neither.
                return /Lead Description/.test(t) && (/Prospecting Lead\\b/.test(t) || /\\bBack\\b/.test(t));
            }""",
            timeout=10000,
        )
        page.wait_for_timeout(500)
        return True
    except Exception as e:
        print(f"  ! Failed to open lead: {e}")
        return False


def close_lead(page: Page, list_url: str) -> None:
    """Detail renders in place — click the 'Back' control to return to list."""
    # Try several Back selectors in order of specificity.
    getters = [
        lambda: page.get_by_role("link", name=re.compile(r"^\s*(←|&larr;|<)?\s*Back\s*$", re.I)).first,
        lambda: page.get_by_role("button", name=re.compile(r"^\s*Back\s*$", re.I)).first,
        lambda: page.locator('a:has-text("Back")').first,
        lambda: page.locator('button:has-text("Back")').first,
        lambda: page.get_by_text(re.compile(r"^\s*<?\s*Back\s*$", re.I)).first,
    ]
    for get in getters:
        try:
            el = get()
            if el.is_visible(timeout=600):
                el.click(timeout=3000)
                # Wait for list to re-render (detail text gone, rows present).
                try:
                    page.wait_for_function(
                        """() => {
                            const t = document.body.innerText || '';
                            return !/Lead Description/.test(t) && /Last updated/.test(t);
                        }""",
                        timeout=8000,
                    )
                except Exception:
                    pass
                return
        except Exception:
            continue
    # Last-resort fallbacks.
    try:
        page.go_back(wait_until="domcontentloaded", timeout=5000)
        page.wait_for_selector("text=/Last updated/i", timeout=5000)
        return
    except Exception:
        pass
    try:
        page.goto(list_url, wait_until="domcontentloaded", timeout=10000)
        page.wait_for_selector("text=/Last updated/i", timeout=8000)
    except Exception:
        print("  ! Could not return to list view.")


def handle_fcc_popup(page: Page) -> None:
    """If the FCC Compliance Reminder modal appeared, click through it."""
    try:
        modal = page.get_by_text("FCC Compliance Reminder", exact=False).first
        if not modal.is_visible(timeout=1500):
            return
    except PWTimeout:
        return
    except Exception:
        return
    # Try common confirm-button labels first.
    for label in ("I Understand", "I Agree", "Continue", "Accept", "Confirm", "OK"):
        try:
            btn = page.get_by_role("button", name=label, exact=False).first
            if btn.is_visible(timeout=500):
                btn.click(timeout=2000)
                page.wait_for_timeout(500)
                return
        except Exception:
            continue
    # Fallback: red-styled button inside the modal (bg-red / btn-danger / etc.).
    selectors = [
        'button.btn-danger',
        'button[class*="bg-red"]',
        'button[class*="red"]',
        'div[role="dialog"] button',
        '.modal button',
    ]
    for sel in selectors:
        try:
            btn = page.locator(sel).last
            if btn.is_visible(timeout=500):
                btn.click(timeout=2000)
                page.wait_for_timeout(500)
                return
        except Exception:
            continue


def ensure_phone_revealed(page: Page) -> None:
    """If 'Call: (xxx) xxx-xxxx' isn't shown, click Get Number and handle FCC popup."""
    # The site renders the reveal trigger as <li class="phone-reveal-prompt">Get Number</li>.
    # When already revealed, that element is hidden (display:none) — visibility check
    # tells us which state we're in.
    get_number = None
    candidates = [
        'li.phone-reveal-prompt',
        '.phone-reveal-prompt',
        'a.phone-reveal-prompt',
        'button.phone-reveal-prompt',
    ]
    for sel in candidates:
        try:
            loc = page.locator(sel)
            n = loc.count()
            for i in range(n):
                el = loc.nth(i)
                if el.is_visible(timeout=400):
                    get_number = el
                    break
            if get_number:
                break
        except Exception:
            continue
    # Last-resort: any visible element with the text.
    if get_number is None:
        try:
            loc = page.get_by_text(re.compile("^\\s*Get\\s*Number\\s*$", re.I))
            n = loc.count()
            for i in range(n):
                el = loc.nth(i)
                if el.is_visible(timeout=400):
                    get_number = el
                    break
        except Exception:
            pass

    if get_number is None:
        # Phone already revealed (or unavailable).
        return

    try:
        get_number.scroll_into_view_if_needed(timeout=2000)
        get_number.click(timeout=3000)
    except Exception as e:
        print(f"  ! Get Number click failed: {e}")
        return
    page.wait_for_timeout(800)
    handle_fcc_popup(page)
    # After FCC dismissal, the page may re-render; give the phone a moment.
    try:
        page.wait_for_selector("text=/Call:\\s*\\(?\\d{3}/", timeout=8000)
    except PWTimeout:
        print("  ! Phone didn't appear after Get Number + FCC.")


def parse_detail(page: Page, page_num: int) -> dict:
    """Pull the visible detail panel's text and regex out the fields."""
    # Find the smallest ancestor that contains "Lead Description" — that's the detail panel.
    text = ""
    try:
        text = page.evaluate(
            """() => {
                const all = Array.from(document.querySelectorAll('div, section, article, main, aside'));
                let best = null;
                let bestLen = Infinity;
                for (const el of all) {
                    const t = el.innerText || '';
                    if (!t.includes('Lead Description')) continue;
                    // Must also contain the contact block (Call: or Get Number).
                    if (!/Call:|Get\\s*Number/.test(t)) continue;
                    if (t.length < bestLen) { bestLen = t.length; best = el; }
                }
                return best ? best.innerText : '';
            }"""
        ) or ""
    except Exception:
        text = ""

    if not text:
        # Fallback: grab body but truncate at the footer marker.
        try:
            text = page.locator("body").text_content(timeout=2000) or ""
        except Exception:
            text = ""

    # Strip known footer noise (kills the 800 support number + JS config garbage).
    for marker in ("My Notes", "QUESTIONS?", "Visit our Resource Center",
                   "Privacy Policy", "appConfiguration", "MORE ABOUT ZBUYER"):
        idx = text.find(marker)
        if idx != -1:
            text = text[:idx]

    lines = [l.strip() for l in text.splitlines() if l.strip()]

    # Name + summary line: name precedes "Curious about ..." or "Thinking about ..."
    name = ""
    summary_line = ""
    for i, line in enumerate(lines):
        if line.startswith("Curious about") or line.startswith("Thinking about"):
            summary_line = line
            if i > 0:
                name = lines[i - 1]
            break

    email_m = EMAIL_RE.search(text)
    email = email_m.group(0) if email_m else ""

    phone = ""
    call_idx = text.find("Call:")
    if call_idx != -1:
        m = PHONE_RE.search(text, call_idx)
        if m:
            phone = m.group(0)

    last_updated_m = LAST_UPDATED_RE.search(text)
    last_updated = last_updated_m.group(1) if last_updated_m else ""

    # Address: lines after the Call: phone, before the bed/bath block.
    street = ""
    city_state_zip = ""
    if phone:
        # Find lines after the "Call:" line up to "Bedrooms".
        try:
            phone_line_idx = next(
                i for i, l in enumerate(lines) if "Call:" in l and phone.split()[0][:3] in l
            )
        except StopIteration:
            phone_line_idx = next((i for i, l in enumerate(lines) if "Call:" in l), -1)
        if phone_line_idx != -1:
            tail = lines[phone_line_idx + 1 :]
            # Skip the FCC notice line if present.
            tail = [l for l in tail if "No Call or Text Automations" not in l]
            # Stop at "Bedrooms" / digit-only line preceding it.
            addr_lines = []
            for l in tail:
                if l == "Bedrooms" or l.endswith("Bedrooms"):
                    break
                # Skip stray single digits (the bed/bath count appears alone).
                if re.fullmatch(r"\d+", l):
                    continue
                addr_lines.append(l)
                if len(addr_lines) >= 2:
                    break
            if addr_lines:
                street = addr_lines[0]
            if len(addr_lines) >= 2:
                city_state_zip = addr_lines[1]

    # Beds / baths: digit on a line followed by "Bedrooms" / "Bathrooms".
    bedrooms = ""
    bathrooms = ""
    for i, l in enumerate(lines):
        if l == "Bedrooms" and i > 0 and re.fullmatch(r"\d+", lines[i - 1]):
            bedrooms = lines[i - 1]
        if l == "Bathrooms" and i > 0 and re.fullmatch(r"\d+", lines[i - 1]):
            bathrooms = lines[i - 1]

    size_m = SIZE_RE.search(text)
    size_sqft = size_m.group(1) if size_m else ""
    built_m = BUILT_RE.search(text)
    year_built = built_m.group(1) if built_m else ""

    avm_low = avm_high = avm_estimate = ""
    avm_m = AVM_RE.search(text)
    if avm_m:
        avm_low, avm_high, avm_estimate = avm_m.group(1), avm_m.group(2), avm_m.group(3)

    reason_m = REASON_RE.search(text)
    reason_selling = reason_m.group(1).strip() if reason_m else ""

    # Lead Description: text between "Lead Description" header and "Public Data" (or end).
    lead_description = ""
    ld_idx = text.find("Lead Description")
    if ld_idx != -1:
        rest = text[ld_idx + len("Lead Description") :]
        pd_idx = rest.find("Public Data")
        chunk = rest[:pd_idx] if pd_idx != -1 else rest
        lead_description = " ".join(chunk.split()).strip()

    # Public Data: everything after that header.
    public_data = ""
    pd_idx = text.find("Public Data")
    if pd_idx != -1:
        public_data = " ".join(text[pd_idx + len("Public Data") :].split()).strip()

    lead_type = "seller" if (street or avm_estimate or "Curious about selling" in summary_line) else "buyer"

    return {
        "scraped_at": datetime.now().isoformat(timespec="seconds"),
        "lead_type": lead_type,
        "name": name,
        "email": email,
        "phone": phone,
        "street": street,
        "city_state_zip": city_state_zip,
        "summary_line": summary_line,
        "last_updated": last_updated,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "size_sqft": size_sqft,
        "year_built": year_built,
        "avm_low": avm_low,
        "avm_high": avm_high,
        "avm_estimate": avm_estimate,
        "reason_selling": reason_selling,
        "lead_description": lead_description,
        "public_data": public_data,
        "page_num": page_num,
    }


def run(pw: Playwright) -> None:
    SESSION_DIR.mkdir(exist_ok=True)
    context = pw.chromium.launch_persistent_context(
        str(SESSION_DIR),
        headless=False,
        viewport={"width": 1400, "height": 900},
    )
    page = context.pages[0] if context.pages else context.new_page()

    ensure_logged_in(page)

    seen = load_seen()
    print(f"Loaded {len(seen)} previously-scraped leads from {CSV_PATH.name}.")

    csv_file, writer = open_csv_writer()
    total_new = 0
    stop = False

    try:
        for page_num in range(1, LAST_PAGE + 1):
            if stop:
                break
            print(f"\n=== Page {page_num} ===")
            goto_page(page, page_num)
            list_url = page.url
            rows = list_lead_rows(page)
            count = rows.count()
            print(f"  Found {count} leads on page {page_num}.")

            for idx in range(count):
                # Re-query rows each iteration — returning from detail re-renders the list.
                rows = list_lead_rows(page)
                if idx >= rows.count():
                    print(f"  ! Row {idx} no longer present (list changed); re-navigating.")
                    goto_page(page, page_num)
                    list_url = page.url
                    rows = list_lead_rows(page)
                    if idx >= rows.count():
                        break
                row = rows.nth(idx)
                name_preview = get_row_name(row)

                # Only use name_preview as an early dedupe shortcut; if empty,
                # we still open the row and get the real name from the detail.
                if name_preview:
                    already = any(n == name_preview for (n, _e) in seen)
                    if already:
                        print(f"  [{idx}] {name_preview}  — already scraped, skipping.")
                        if name_preview == STOP_NAME:
                            stop = True
                            break
                        continue
                    print(f"  [{idx}] Opening: {name_preview}")
                else:
                    print(f"  [{idx}] Opening: (name unknown — will read from detail)")

                if not open_lead(page, row, list_url):
                    close_lead(page, list_url)
                    continue

                ensure_phone_revealed(page)
                lead = parse_detail(page, page_num)

                key = (lead["name"], lead["email"])
                if lead["name"] and key not in seen:
                    writer.writerow(lead)
                    csv_file.flush()
                    seen.add(key)
                    total_new += 1
                    print(
                        f"      saved: {lead['name']} | {lead['lead_type']} | "
                        f"{lead['email']} | {lead['phone']}"
                    )
                else:
                    print(f"      (no name parsed or duplicate, not saved)")

                reached_stop = (lead["name"] == STOP_NAME) or (name_preview == STOP_NAME)
                close_lead(page, list_url)

                if reached_stop:
                    print(f"\nReached stop name: {STOP_NAME}. Done.")
                    stop = True
                    break
    finally:
        csv_file.close()
        print(f"\nWrote {total_new} new lead(s). CSV: {CSV_PATH}")
        try:
            context.close()
        except Exception:
            pass


def main() -> int:
    with sync_playwright() as pw:
        run(pw)
    return 0


if __name__ == "__main__":
    sys.exit(main())
