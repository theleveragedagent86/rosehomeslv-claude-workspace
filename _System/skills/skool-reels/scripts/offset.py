"""Screen-to-camera offset (cam_time - screen_time) from matching 6-word runs.

  python3 offset.py words.json cam scr1 [scr2 ...]

Median of every unique 6-word run found in both transcripts. FFT sync needs numpy, which
is not installed, and this is accurate to a word anyway. Needs ~5+ matches to trust.
"""
import json, re, statistics, sys

W = json.load(open(sys.argv[1])); cam = sys.argv[2]
def norm(w): return re.sub(r"[^a-z0-9']", "", w.lower())
def runs(ws, n=6):
    d = {}
    for i in range(len(ws) - n + 1):
        key = " ".join(norm(w[2]) for w in ws[i:i + n])
        d.setdefault(key, []).append(ws[i][0])
    return {k: v[0] for k, v in d.items() if len(v) == 1}   # unique runs only
C = runs(W[cam])
for s in sys.argv[3:]:
    S = runs(W[s])
    diffs = [C[k] - S[k] for k in C.keys() & S.keys()]
    if not diffs: print(s, "no matching runs, screen may be silent: sync it by eye"); continue
    print(f"{s}: offset {statistics.median(diffs):.2f}s  ({len(diffs)} matches, spread {min(diffs):.1f}..{max(diffs):.1f})")
