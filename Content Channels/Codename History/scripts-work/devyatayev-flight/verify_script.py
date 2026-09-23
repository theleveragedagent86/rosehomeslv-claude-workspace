#!/usr/bin/env python3
"""Verify hard constraints on script-v2-final.md.

A beat = all spoken text between one **[VISUAL n: tag and the next,
counting **NARRATOR:** and any **SOMEONE (character voice):** line.
"""
import re, sys, collections, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "script-v2-final.md")

VIS = re.compile(r'^\*\*\[VISUAL (\d+):')
SPOKEN = re.compile(r'^\*\*(NARRATOR|[A-ZÄÖÜ][A-ZÄÖÜ \'\.]*\(character voice\)):\*\*\s*(.*)$')
REUSE = re.compile(r'\(REUSE:')

def main():
    text = open(PATH, encoding='utf-8').read()
    lines = text.split('\n')

    order = []           # visual numbers in file order
    beats = {}           # visual number -> list of spoken strings
    cur = None
    reuse = 0
    for ln in lines:
        m = VIS.match(ln)
        if m:
            cur = int(m.group(1))
            order.append(cur)
            beats[cur] = []
            if REUSE.search(ln):
                reuse += 1
            continue
        s = SPOKEN.match(ln)
        if s and cur is not None:
            beats[cur].append(s.group(2).strip().strip('"'))

    counts = {n: len(' '.join(beats[n]).split()) for n in order}
    total = sum(counts.values())
    dist = collections.Counter(counts.values())
    mx = max(counts.values())
    fourteens = sorted(n for n, c in counts.items() if c == 14)
    contiguous = order == list(range(1, len(order) + 1))
    em = text.count('—')
    en = text.count('–')

    print("FILE:", PATH)
    print("total spoken words          :", total)
    print("visual tag count            :", len(order))
    print("contiguity 1..112           :", "OK" if contiguous and len(order) == 112 else "FAIL")
    print("REUSE tags                  :", reuse)
    print("beat word distribution      :", ", ".join(f"{d[1]}@{d[0]}" for d in sorted(dist.items())))
    print("max beat length             :", mx)
    print("14-word beat scene numbers  :", fourteens)
    print("beats over 14 words         :", sorted(n for n, c in counts.items() if c > 14))
    print("em-dash count               :", em)
    print("en-dash count               :", en)
    print("beats with zero spoken words:", [n for n in order if counts[n] == 0])
    print("brackets in spoken lines    :",
          [n for n in order if any(re.search(r'[\[\]\(\)]', s) for s in beats[n])])

if __name__ == '__main__':
    main()
