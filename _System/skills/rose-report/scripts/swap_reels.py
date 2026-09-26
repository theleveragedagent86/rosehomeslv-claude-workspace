#!/usr/bin/env python3
"""Swap "Reel drops ..." lines for live reel links in a Rose Report issue.

Each unposted reel line sits right after a marker comment like
  <!-- P06 S01: swap to exact /reel/ URL once live -->
This replaces the text of the line that follows with a linked
"Watch the 60-second version on Instagram" and flips the marker to LIVE.

Usage:
  swap_reels.py <issue_dir> P06=https://www.instagram.com/reel/XXXX/ [P10=...]
  swap_reels.py <issue_dir> --list      # show markers still waiting
Edits newsletter.html and beehiiv-snippet.html in place (whichever exist).
"""
import re, sys, pathlib

LINK_STYLE = ("color:#050E3D;text-decoration:underline;text-decoration-color:#1768E5;"
              "text-decoration-thickness:2px;text-underline-offset:3px;")
MARK = re.compile(r'<!-- (P\d+) (S\d+): ([^>]*?)-->')

def pending(html):
    return [(m.group(1), m.group(2)) for m in MARK.finditer(html) if not m.group(3).startswith('LIVE')]

def swap(html, post, url):
    m = next((m for m in MARK.finditer(html) if m.group(1) == post), None)
    if not m:
        return html, 'no marker'
    if m.group(3).startswith('LIVE'):
        return html, 'already live'
    # the text cell of the line right after the marker
    cell = re.compile(r'(<td[^>]*class="t-muted"[^>]*>)(.*?)(</td>)', re.S)
    c = cell.search(html, m.end())
    if not c or c.start() - m.end() > 1500:
        return html, 'line not found after marker'
    new_text = f'<a class="link" href="{url}" style="{LINK_STYLE}">Watch the 60-second version on Instagram</a>'
    html = html[:c.start(2)] + new_text + html[c.end(2):]
    html = html[:m.start()] + f'<!-- {post} {m.group(2)}: LIVE {url} -->' + html[m.end():]
    return html, 'swapped'

def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    d = pathlib.Path(sys.argv[1])
    files = [f for f in (d / 'newsletter.html', d / 'beehiiv-snippet.html') if f.exists()]
    if not files:
        sys.exit(f'no newsletter.html or beehiiv-snippet.html in {d}')
    if sys.argv[2] == '--list':
        for f in files:
            print(f.name, ' '.join(f'{p}/{s}' for p, s in pending(f.read_text())) or 'none pending')
        return
    pairs = [a.split('=', 1) for a in sys.argv[2:]]
    for f in files:
        html = f.read_text()
        for post, url in pairs:
            if not re.match(r'https://www\.instagram\.com/reel/[\w-]+/?$', url):
                sys.exit(f'{post}: not an instagram /reel/ URL: {url}')
            html, status = swap(html, post.upper(), url)
            print(f'{f.name} {post}: {status}')
        f.write_text(html)

if __name__ == '__main__':
    main()
