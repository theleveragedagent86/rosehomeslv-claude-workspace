#!/usr/bin/env python3
"""Minimal beehiiv API helper for The Rose Report.

The API key is read from macOS Keychain only (service beehiiv-api-key).
Create and update are Max/Enterprise-plan features. On a 403 or 404 from
those calls, fall back to the browser flow in references/beehiiv.md.

Usage:
  beehiiv.py list                          # recent posts: id, status, date, web_url, title
  beehiiv.py create "<title>" <snippet.html>
  beehiiv.py update <post_id> <snippet.html>
  beehiiv.py get <post_id>                 # status, platform, web_url, reel-line count
"""
import json, subprocess, sys, urllib.request, urllib.error

PUB = 'pub_2d01a48c-d852-446f-a2ef-90428ddc6545'
BASE = f'https://api.beehiiv.com/v2/publications/{PUB}'

def key():
    return subprocess.run(['security', 'find-generic-password', '-a', 'ryan', '-s', 'beehiiv-api-key', '-w'],
                          capture_output=True, text=True, check=True).stdout.strip()

def call(method, path, body=None):
    req = urllib.request.Request(BASE + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={'Authorization': f'Bearer {key()}', 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        msg = e.read().decode()[:300]
        if e.code in (403, 404) and method in ('POST', 'PATCH'):
            sys.exit(f'HTTP {e.code}: {msg}\nLikely not on the Max plan. Use the browser flow in references/beehiiv.md.')
        sys.exit(f'HTTP {e.code}: {msg}')

def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == 'list':
        for p in call('GET', '/posts?status=all&limit=20&order_by=created&direction=desc')['data']:
            print(p['id'], p['status'], p.get('publish_date'), p.get('web_url'), '|', p['title'][:60])
    elif a[0] == 'get':
        p = call('GET', f'/posts/{a[1]}?expand[]=free_web_content')['data']
        web = p.get('content', {}).get('free', {}).get('web', '')
        print(json.dumps({k: p.get(k) for k in ('id', 'status', 'platform', 'publish_date', 'web_url', 'title')}, indent=1))
        print('reel lines still "drops":', web.count('drops'), '| live reel links:', web.count('instagram.com/reel/'))
    elif a[0] == 'create':
        body = open(a[2]).read()
        p = call('POST', '/posts', {'title': a[1], 'status': 'draft', 'body_content': body})['data']
        print(p['id'], p.get('web_url'))
    elif a[0] == 'update':
        body = open(a[2]).read()
        p = call('PATCH', f'/posts/{a[1]}', {'body_content': body})['data']
        print('updated', p['id'], p.get('status'), p.get('web_url'))
    else:
        sys.exit(__doc__)

if __name__ == '__main__':
    main()
