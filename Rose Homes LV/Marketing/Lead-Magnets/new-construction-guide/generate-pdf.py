#!/usr/bin/env python3
"""
Render the area-wide New Construction buyer guide to a print-ready PDF.

Hardened fork of Content/New-Construction/Completed/delemar-by-pulte/generate-pdf.py.
Four things changed, each because the original breaks on a 38-page document:

  1. Readiness is *measured*, not slept on. The original waits a flat 3 seconds.
     This guide loads six font weights plus roughly twenty images, and a font that
     is not ready at print time silently falls back to a system face and repaginates
     the entire document. We poll document.fonts.ready and decode every <img>.
  2. A free port is picked at runtime. The original hardcodes 9222, which the Lofty
     publishing flow also uses; a collision there attaches us to a logged-in browser.
  3. A throwaway --user-data-dir keeps this out of the real Chrome profile.
  4. Chrome is terminated in a finally block, gracefully, so a crash cannot leave an
     orphaned headless process holding the port.

Usage:
    python3 generate-pdf.py
    python3 generate-pdf.py --html some.html --pdf out.pdf --accent "#1b75a1"
    python3 generate-pdf.py --no-footer
"""

import argparse
import asyncio
import base64
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request

try:
    import websockets
except ImportError:
    sys.exit("ERROR: pip3 install websockets")

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Letter, matched to the @page rule in the guide's print CSS. If you change one,
# change the other, or Chrome and the stylesheet will disagree about the text box.
PAPER_W, PAPER_H = 8.5, 11.0
MARGIN_TOP, MARGIN_BOTTOM = 0.6, 0.75
MARGIN_LEFT, MARGIN_RIGHT = 0.75, 0.75

# How long to wait for fonts and images before giving up and printing anyway.
READY_TIMEOUT_S = 45

READY_JS = """
(async () => {
  await document.fonts.ready;
  const imgs = Array.from(document.images);
  await Promise.all(imgs.map(i => i.decode().catch(() => null)));
  // Let layout settle after late webfont metrics land.
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  return JSON.stringify({
    fonts: document.fonts.status,
    fontCount: document.fonts.size,
    images: imgs.length,
    broken: imgs.filter(i => !i.complete || i.naturalWidth === 0).map(i => i.currentSrc || i.src),
    height: document.documentElement.scrollHeight
  });
})()
"""


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def footer_template(accent: str) -> str:
    """Chrome renders header/footer in a sandboxed context: no page CSS, no webfonts.
    Only the magic classes (pageNumber, totalPages, title, url, date) resolve, and
    only inline styles apply. Keep the font stack to system faces."""
    return (
        '<div style="width:100%;text-align:center;padding:0 0 6px;'
        'font-family:Helvetica,Arial,sans-serif;font-size:9px;'
        f'letter-spacing:1.6px;color:{accent};">'
        '<span class="pageNumber"></span>'
        "</div>"
    )


async def render(html_path: str, pdf_path: str, accent: str, show_footer: bool,
                 prefer_css_page_size: bool) -> int:
    if not os.path.isfile(html_path):
        sys.exit(f"ERROR: no such HTML file: {html_path}")

    port = free_port()
    profile = tempfile.mkdtemp(prefix="ncguide-chrome-")
    file_url = "file://" + urllib.request.pathname2url(os.path.abspath(html_path))

    proc = subprocess.Popen(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            f"--remote-debugging-port={port}",
            f"--user-data-dir={profile}",
            "--no-first-run",
            "--no-default-browser-check",
            "--disable-extensions",
            "--hide-scrollbars",
            "--allow-file-access-from-files",
            "--font-render-hinting=none",
            file_url,
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    try:
        ws_url = None
        deadline = time.time() + 30
        while time.time() < deadline:
            if proc.poll() is not None:
                sys.exit(f"ERROR: Chrome exited early with code {proc.returncode}")
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{port}/json", timeout=2) as r:
                    for tab in json.loads(r.read()):
                        if tab.get("type") == "page" and tab.get("webSocketDebuggerUrl"):
                            ws_url = tab["webSocketDebuggerUrl"]
                            break
            except Exception:
                pass
            if ws_url:
                break
            time.sleep(0.25)

        if not ws_url:
            sys.exit("ERROR: could not reach a Chrome page target")

        async with websockets.connect(ws_url, max_size=200 * 1024 * 1024) as ws:
            counter = {"id": 0}

            async def send(method, params=None):
                counter["id"] += 1
                mid = counter["id"]
                await ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
                while True:
                    resp = json.loads(await ws.recv())
                    if resp.get("id") == mid:
                        if "error" in resp:
                            sys.exit(f"ERROR in {method}: {resp['error']}")
                        return resp.get("result", {})

            await send("Page.enable")
            await send("Runtime.enable")

            # Block until fonts and images are genuinely ready.
            try:
                res = await asyncio.wait_for(
                    send("Runtime.evaluate", {
                        "expression": READY_JS,
                        "awaitPromise": True,
                        "returnByValue": True,
                    }),
                    timeout=READY_TIMEOUT_S,
                )
                info = json.loads(res.get("result", {}).get("value") or "{}")
                print(f"  fonts:  {info.get('fonts')} ({info.get('fontCount')} faces)")
                print(f"  images: {info.get('images')} decoded")
                if info.get("broken"):
                    print("  WARNING: images failed to load, PDF will have gaps:")
                    for src in info["broken"]:
                        print(f"    - {src}")
            except asyncio.TimeoutError:
                print(f"  WARNING: assets not ready after {READY_TIMEOUT_S}s, printing anyway")

            params = {
                "printBackground": True,
                "paperWidth": PAPER_W,
                "paperHeight": PAPER_H,
                "marginTop": MARGIN_TOP,
                "marginBottom": MARGIN_BOTTOM,
                "marginLeft": MARGIN_LEFT,
                "marginRight": MARGIN_RIGHT,
                "preferCSSPageSize": prefer_css_page_size,
                "displayHeaderFooter": show_footer,
            }
            if show_footer:
                params["headerTemplate"] = "<div></div>"
                params["footerTemplate"] = footer_template(accent)

            result = await send("Page.printToPDF", params)
            data = base64.b64decode(result["data"])
            with open(pdf_path, "wb") as fh:
                fh.write(data)

            print(f"  wrote:  {pdf_path} ({len(data):,} bytes)")
            return len(data)

    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
        shutil.rmtree(profile, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--html", default=os.path.join(HERE, "new-construction-buyer-guide.html"))
    ap.add_argument("--pdf", default=os.path.join(HERE, "new-construction-buyer-guide.pdf"))
    ap.add_argument("--accent", default="#1a1a1a",
                    help="page-number color; set to the locked design accent after the design gate")
    ap.add_argument("--no-footer", action="store_true", help="omit page numbers")
    ap.add_argument("--prefer-css-page-size", action="store_true",
                    help="let the stylesheet's @page rule win over the margins above")
    args = ap.parse_args()

    print(f"Rendering {os.path.basename(args.html)}")
    asyncio.run(render(args.html, args.pdf, args.accent,
                       not args.no_footer, args.prefer_css_page_size))

    # Report what actually came out, so pagination problems surface here and not
    # three steps later during visual QA.
    if shutil.which("pdfinfo"):
        out = subprocess.run(["pdfinfo", args.pdf], capture_output=True, text=True).stdout
        for line in out.splitlines():
            if line.startswith(("Pages:", "Page size:")):
                print(f"  {line}")


if __name__ == "__main__":
    main()
