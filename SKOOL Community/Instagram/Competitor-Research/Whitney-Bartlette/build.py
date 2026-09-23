import json, csv, re, collections, datetime, statistics as st

D = 'data/'
OWNER = 'whitneybartlette.social'

META = json.load(open(D + 'wb_meta_228.json'))
C = json.load(open(D + 'wb_comments_228_0.json')) + json.load(open(D + 'wb_comments_228_1.json'))
L = json.load(open(D + 'wb_likers_228_0.json')) + json.load(open(D + 'wb_likers_228_1.json'))

RE_PAT = re.compile(r'realtor|real ?estate|\brealty\b|broker|\bagent\b|homes?\b|properties|property|re/?max|remax|keller ?williams|\bkw\b|compass|coldwell|century ?21|\bc21\b|\bexp\b|sotheby|berkshire|\bbhhs\b|elliman|listing|\bmls\b|sells|selling|\bloan|mortgage|lender|\bnmls\b|escrow|realestate|\bsold\b|relocat|dre ?#|lic ?#', re.I)
CTA = re.compile(r'(?i:comment)\s+["“]?([A-Z][A-Z0-9]{2,20})\b["”]?')


def topic(c):
    c = (c or '').lower()
    if re.search(r'opusclip|\bai\b|automat|manychat|chatgpt|claude|prompt', c): return 'AI/Tools'
    if re.search(r'edit|caption|b-roll|font|story idea|filmstrip|reel|video shot|template', c): return 'Content Craft'
    if re.search(r'membership|community|social shift|coaching|client|student|strategy behind', c): return 'Offer/Proof'
    if re.search(r'grow|follower|viral|algorithm|engagement|sell|sales|niche|audience|bio|profile', c): return 'Growth/Strategy'
    if re.search(r'life|hard|proud|mission|waiting|remind|believe|excited to wake|quit|journey', c): return 'Mindset'
    return 'Other'


def cta(caption):
    m = CTA.search(caption or '')
    return m.group(1).strip().upper() if m else None


def fmt(v):
    if v.get('carousel'): return 'carousel'
    return 'reel' if v.get('mt') == 2 else 'image'


posts = {}
foreign = []
for k, v in META.items():
    if v.get('owner') and v['owner'] != OWNER:
        foreign.append((k, v['owner']))
        continue
    posts[k] = dict(code=k, pk=str(v['pk']), ts=v['t'],
                    date=datetime.datetime.fromtimestamp(v['t']).strftime('%Y-%m-%d'),
                    month=datetime.datetime.fromtimestamp(v['t']).strftime('%Y-%m'),
                    fmt=fmt(v), cta=cta(v['cap']), topic=topic(v['cap']),
                    likes=(None if v['likes'] <= 3 else v['likes']), cc=v['cc'], plays=v['plays'],
                    hook=(v['cap'] or '').split('\n')[0][:90], caption=v['cap'] or '')

BYPK = {p['pk']: p for p in posts.values()}


class P:
    def __init__(s):
        s.name = ''; s.comments = 0; s.likes = 0; s.posts = set()
        s.first = None; s.last = None; s.samples = []; s.ai = 0; s.biz = 0


people = collections.defaultdict(P)
percomment = []
owner_replies = 0
for row in C:
    pk, code, handle, name, text, ts, cl = row
    if not handle: continue
    if handle == OWNER:
        owner_replies += 1
        continue
    p = people[handle]
    p.name = p.name or (name or '')
    p.comments += 1; p.posts.add(code)
    d = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    p.first = min(p.first, d) if p.first else d
    p.last = max(p.last, d) if p.last else d
    if len(p.samples) < 3 and text: p.samples.append((text or '').replace('\n', ' ')[:80])
    post = posts.get(code, {})
    t = post.get('topic')
    if t == 'AI/Tools': p.ai += 1
    if t in ('Offer/Proof', 'Growth/Strategy', 'Content Craft'): p.biz += 1
    percomment.append([code, post.get('date', ''), post.get('hook', ''), handle, name or '',
                       (text or '').replace('\n', ' '), d])

liker_only = collections.defaultdict(P)
for row in L:
    pk, code, handle, name = row
    if not handle or handle == OWNER: continue
    tgt = people[handle] if handle in people else liker_only[handle]
    tgt.name = tgt.name or (name or '')
    tgt.likes += 1; tgt.posts.add(code)

TODAY = datetime.date(2026, 9, 9)


def recent(p, days):
    if not p.last: return False
    return (TODAY - datetime.date(*map(int, p.last.split('-')))).days <= days


def score(h, p):
    s = p.ai * 12 + p.biz * 4 + p.likes * 1
    if RE_PAT.search(h) or RE_PAT.search(p.name or ''): s += 25
    if recent(p, 60): s += 15
    if recent(p, 30): s += 15
    return s


def w(fn, header, rows):
    with open(fn, 'w', newline='', encoding='utf-8') as f:
        c = csv.writer(f); c.writerow(header); c.writerows(rows)
    print(fn, len(rows))


allp = list(people.items()) + list(liker_only.items())
w('MASTER-PEOPLE-LOG.csv',
  ['handle', 'name', 'comments', 'likes', 'posts_touched', 'first_seen', 'last_seen', 'sample_1', 'sample_2', 'sample_3'],
  sorted([[h, p.name, p.comments, p.likes, len(p.posts), p.first or '', p.last or ''] + (p.samples + ['', '', ''])[:3]
          for h, p in allp], key=lambda r: (-r[2], -r[3])))

ai = [[h, p.name, p.comments, p.likes, p.last or ''] for h, p in people.items() if p.ai > 0]
w('LIST-A-hot-AI-commenters.csv', ['handle', 'name', 'comments', 'likes', 'last_seen'], sorted(ai, key=lambda r: -r[2]))
biz = [[h, p.name, p.comments, p.likes, p.last or ''] for h, p in people.items() if p.biz > 0]
w('LIST-B-business-commenters.csv', ['handle', 'name', 'comments', 'likes', 'last_seen'], sorted(biz, key=lambda r: -r[2]))
rep = [[h, p.name, p.comments, p.likes, p.last or ''] for h, p in people.items() if p.comments >= 3]
w('LIST-C-repeat-engagers.csv', ['handle', 'name', 'comments', 'likes', 'last_seen'], sorted(rep, key=lambda r: -r[2]))
red = [[h, p.name, p.comments, p.likes, p.last or ''] for h, p in allp if RE_PAT.search(h) or RE_PAT.search(p.name or '')]
w('LIST-D-RE-name-signal.csv', ['handle', 'name', 'comments', 'likes', 'last_seen'], sorted(red, key=lambda r: -r[2]))
lo = [[h, p.name, 0, p.likes, ''] for h, p in liker_only.items()]
w('LIST-E-likers-only.csv', ['handle', 'name', 'comments', 'likes', 'last_seen'], sorted(lo, key=lambda r: -r[3]))
w('PER-POST-COMMENTER-LOG.csv',
  ['post_code', 'post_date', 'post_hook', 'handle', 'name', 'comment_text', 'comment_date'], percomment)

ranked = sorted(((score(h, p), h, p) for h, p in allp), key=lambda x: -x[0])[:300]
w('TOP-300-DM-TARGETS.csv',
  ['rank', 'handle', 'name', 'score', 'ai_comments', 'biz_comments', 'likes', 'posts_touched', 'last_seen', 'sample_comment'],
  [[i + 1, h, p.name, s, p.ai, p.biz, p.likes, len(p.posts), p.last or '', (p.samples[0] if p.samples else '')]
   for i, (s, h, p) in enumerate(ranked)])


def med(x):
    x = [v for v in x if v is not None]
    return round(st.median(x), 1) if x else 0


PV = list(posts.values())
print('\nDATE RANGE', min(p['date'] for p in PV), 'to', max(p['date'] for p in PV))
print('foreign/collab posts skipped:', len(foreign), foreign[:5])
print('owner reply rows:', owner_replies)

print('\nCTA LIFT')
for f in sorted(set(p['fmt'] for p in PV)):
    wi = [p['cc'] for p in PV if p['fmt'] == f and p['cta']]
    wo = [p['cc'] for p in PV if p['fmt'] == f and not p['cta']]
    print(f, 'n_cta', len(wi), 'med', med(wi), '| n_nocta', len(wo), 'med', med(wo),
          '| x', round(med(wi) / med(wo), 1) if med(wo) else 'NA')

print('\nBY TOPIC')
for t in sorted(set(p['topic'] for p in PV)):
    g = [p for p in PV if p['topic'] == t]
    print(t, len(g), 'medC', med([p['cc'] for p in g]), 'medL', med([p['likes'] for p in g]),
          'nL', sum(1 for p in g if p['likes'] is not None),
          'medP', med([p['plays'] for p in g if p['plays']]), 'ctaShare',
          round(100 * sum(1 for p in g if p['cta']) / len(g)))

print('\nFORMAT')
for f in sorted(set(p['fmt'] for p in PV)):
    g = [p for p in PV if p['fmt'] == f]
    print(f, len(g), 'shareposts', round(100 * len(g) / len(PV)), 'shareC',
          round(100 * sum(p['cc'] for p in g) / sum(p['cc'] for p in PV)),
          'medC', med([p['cc'] for p in g]), 'medL', med([p['likes'] for p in g]),
          'ratio', round(sum(p['cc'] for p in g if p['likes'] is not None) / max(1, sum(p['likes'] for p in g if p['likes'] is not None)), 3))

print('\nMONTH')
for m in sorted(set(p['month'] for p in PV)):
    g = [p for p in PV if p['month'] == m]
    print(m, 'posts', len(g), 'pctCTA', round(100 * sum(1 for p in g if p['cta']) / len(g)),
          'medC', med([p['cc'] for p in g]), 'totC', sum(p['cc'] for p in g),
          'medL', med([p['likes'] for p in g]), 'medP', med([p['plays'] for p in g if p['plays']]))

print('\nCAPTION KEYWORDS ASKED')
print(collections.Counter(p['cta'] for p in PV if p['cta']).most_common(20))

print('\nWHAT PEOPLE TYPED')
words = collections.Counter()
for row in C:
    h = row[2]; t = (row[4] or '').strip().lower()
    if h == OWNER: continue
    if 1 <= len(t.split()) <= 3: words[t] += 1
print(words.most_common(30))

print('\nTOP 20 POSTS BY COMMENTS')
for p in sorted(PV, key=lambda x: -x['cc'])[:20]:
    print(p['date'], p['fmt'], p['topic'], 'C', p['cc'], 'L', p['likes'], 'P', p['plays'], '|', p['cta'], '|', p['hook'][:70])

print('\nBOTTOM 20 POSTS BY COMMENTS')
for p in sorted(PV, key=lambda x: x['cc'])[:20]:
    print(p['date'], p['fmt'], p['topic'], 'C', p['cc'], 'L', p['likes'], 'P', p['plays'], '|', p['cta'], '|', p['hook'][:70])

with open('POST-CATALOGUE-2026.md', 'w') as f:
    f.write('# Post catalogue, Whitney Bartlette\n\n')
    f.write('%d posts, %s to %s. Grid capture, not the full account. See README for method and limits.\n\n'
            % (len(PV), min(p['date'] for p in PV), max(p['date'] for p in PV)))
    f.write('| date | type | CTA keyword | topic | likes | comments | plays | link | hook |\n|---|---|---|---|---|---|---|---|---|\n')
    for p in sorted(PV, key=lambda x: -x['ts']):
        f.write('| %s | %s | %s | %s | %s | %s | %s | https://www.instagram.com/p/%s/ | %s |\n' % (
            p['date'], p['fmt'], p['cta'] or '', p['topic'],
            (p['likes'] if p['likes'] is not None else 'NOT FOUND'), p['cc'], p['plays'] or '',
            p['code'], p['hook'].replace('|', '/')))

json.dump({k: {kk: vv for kk, vv in v.items() if kk != 'caption'} for k, v in posts.items()},
          open(D + 'posts_derived.json', 'w'), indent=1)
print('\nposts', len(PV), 'people', len(allp), 'commenters', len(people), 'likers_only', len(liker_only),
      'commentrows', len(C), 'likerrows', len(L))
