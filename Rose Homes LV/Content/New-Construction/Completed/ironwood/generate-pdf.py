#!/usr/bin/env python3
"""Generate buyer guide PDF with styled page numbers using Chrome DevTools Protocol."""

import asyncio
import json
import base64
import subprocess
import time
import urllib.request
import websockets
import sys
import os

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT = 9222
HTML_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "buyer-guide.html")
PDF_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "buyer-guide.pdf")

FOOTER_TEMPLATE = '<div style="width:100%;text-align:center;padding:8px 0;font-family:Bebas Neue,sans-serif;font-size:12px;letter-spacing:2px;color:#4A104A;"><span class="pageNumber"></span></div>'

HEADER_TEMPLATE = "<div></div>"


async def generate_pdf():
    file_url = f"file://{HTML_FILE}"

    proc = subprocess.Popen(
        [CHROME, "--headless", "--disable-gpu", f"--remote-debugging-port={PORT}",
         "--no-first-run", "--no-default-browser-check", file_url],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

    ws_url = None
    for _ in range(30):
        try:
            resp = urllib.request.urlopen(f"http://localhost:{PORT}/json")
            tabs = json.loads(resp.read())
            for tab in tabs:
                if tab.get("type") == "page":
                    ws_url = tab["webSocketDebuggerUrl"]
                    break
            if ws_url:
                break
        except Exception:
            pass
        time.sleep(0.5)

    if not ws_url:
        print("ERROR: Could not connect to Chrome page target")
        proc.kill()
        sys.exit(1)

    try:
        async with websockets.connect(ws_url, max_size=50 * 1024 * 1024) as ws:
            msg_id = 0

            async def send(method, params=None):
                nonlocal msg_id
                msg_id += 1
                msg = {"id": msg_id, "method": method}
                if params:
                    msg["params"] = params
                await ws.send(json.dumps(msg))

                while True:
                    resp = json.loads(await ws.recv())
                    if resp.get("id") == msg_id:
                        if "error" in resp:
                            print(f"ERROR in {method}: {resp['error']}")
                        return resp.get("result", {})

            await send("Page.enable")
            await asyncio.sleep(3)

            result = await send("Page.printToPDF", {
                "printBackground": True,
                "paperWidth": 8.5,
                "paperHeight": 11,
                "marginTop": 0.6,
                "marginBottom": 0.75,
                "marginLeft": 0.75,
                "marginRight": 0.75,
                "displayHeaderFooter": True,
                "headerTemplate": HEADER_TEMPLATE,
                "footerTemplate": FOOTER_TEMPLATE,
            })

            pdf_data = base64.b64decode(result["data"])
            with open(PDF_FILE, "wb") as f:
                f.write(pdf_data)

            print(f"PDF saved: {PDF_FILE} ({len(pdf_data):,} bytes)")

    finally:
        proc.kill()
        proc.wait()


if __name__ == "__main__":
    asyncio.run(generate_pdf())
