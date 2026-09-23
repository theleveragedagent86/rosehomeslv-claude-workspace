#!/usr/bin/env python3
"""Assemble relocation-guide.html from fragments/p*.html.

The CSS is lifted verbatim from the new construction guide's generated shell
(build/shell.html), which is the frozen design contract described in
../new-construction-guide/build/design-system.md. Lifting rather than
transcribing is deliberate: that shell is a base plus an override layer, so
hand-copying reintroduces exactly the bug the design lock exists to catch.

The output is self-contained apart from assets/img/ and Google Fonts.

    python3 build.py
"""

import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SHELL = os.path.join(HERE, "..", "new-construction-guide", "build", "shell.html")
OUT = os.path.join(HERE, "relocation-guide.html")

TITLE = "Moving to Las Vegas | A Relocation Guide from Ryan Rose, Real Broker, LLC"
DESC = (
    "Neighborhoods, cost of living, schools, and the steps of a Las Vegas move, "
    "in plain English. Every number sourced and dated. Ryan Rose, Real Broker, LLC."
)


def main():
    if not os.path.exists(SHELL):
        sys.exit("shell.html not found at %s" % SHELL)
    shell = open(SHELL, encoding="utf-8").read()

    head, _, _ = shell.partition("<body>")
    head = head.replace(
        re.search(r"<title>.*?</title>", head, re.S).group(0), "<title>%s</title>" % TITLE
    )
    head = re.sub(
        r'<meta name="description" content=".*?">',
        '<meta name="description" content="%s">' % DESC,
        head,
        flags=re.S,
    )

    frags = sorted(glob.glob(os.path.join(HERE, "fragments", "p*.html")))
    if not frags:
        sys.exit("no fragments found")

    body = []
    for f in frags:
        body.append(open(f, encoding="utf-8").read().rstrip())

    doc = head + '<body>\n<a class="skip" href="#p2">Skip to the contents</a>\n\n' \
        + "\n\n".join(body) + "\n\n</body>\n</html>\n"

    # Hard gates. Both have shipped as bugs in this workspace before.
    if "—" in doc or "&mdash;" in doc:
        sys.exit("FAIL: em-dash in output")
    if "position:fixed" in doc.replace(" ", ""):
        sys.exit("FAIL: position:fixed in a print-first document")

    open(OUT, "w", encoding="utf-8").write(doc)
    print("wrote %s, %d pages, %d bytes" % (OUT, len(frags), len(doc)))


if __name__ == "__main__":
    main()
