"""Word-level transcripts for every source file -> words.json + readable <key>.txt dumps.

  python3 transcribe.py <out_dir> cam=/path/IMG_7285.MOV scr1="/path/Screen*9.08.47*" ...

Keys are yours to pick (cam, scr1, c6675 ...). Globs are expanded, because macOS screen
recording names hide a U+202F before "AM" and cannot be typed. whisper-cli small.en, stdlib only.
"""
import glob, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

MODEL = os.path.expanduser("~/.cache/hyperframes/whisper/models/ggml-small.en.bin")
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
srcs = {}
for a in sys.argv[2:]:
    k, p = a.split("=", 1)
    m = glob.glob(os.path.expanduser(p))
    if len(m) != 1: sys.exit(f"{k}: {len(m)} matches for {p}")
    srcs[k] = m[0]

def one(k):
    wav, base = os.path.join(out, k + ".wav"), os.path.join(out, k)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", srcs[k], "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
    subprocess.run(["whisper-cli", "-m", MODEL, "-f", wav, "-ml", "1", "-sow", "-ojf", "-of", base, "-t", "4", "-np"],
                   check=True, capture_output=True)
    words = []
    for s in json.load(open(base + ".json"))["transcription"]:
        t = s["text"].strip()
        if t and not t.startswith("["):
            words.append([s["offsets"]["from"] / 1000, s["offsets"]["to"] / 1000, t])
    os.remove(wav)
    return k, words

with ThreadPoolExecutor(4) as ex:
    W = dict(ex.map(one, srcs))
json.dump(W, open(os.path.join(out, "words.json"), "w"))
for k, ws in W.items():   # readable dump, one line per ~12 words, to pick clips from
    with open(os.path.join(out, k + ".txt"), "w") as f:
        for i in range(0, len(ws), 12):
            t = ws[i][0]
            f.write(f"[{int(t // 60)}:{int(t % 60):02d}] " + " ".join(w[2] for w in ws[i:i + 12]) + "\n")
print({k: len(v) for k, v in W.items()}, "->", os.path.join(out, "words.json"))
json.dump(srcs, open(os.path.join(out, "sources.json"), "w"), indent=1)
