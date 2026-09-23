"""Cut the 5 Weekly Seller Update Reels/Shorts from the raw footage.

Sources (raw, not the edited long form):
  camera  ~/Downloads/IMG_7285.MOV                     1920x1080, the audio source
  screen  ~/Downloads/Screen Recording 2026-09-17 at 9.08.47 AM.mov  (scr1)
  screen  ~/Downloads/Screen Recording 2026-09-17 at 9.20.30 AM.mov  (scr2)
words.json = whisper word timestamps for all three. Screen offsets were found by
matching 6-word runs between the camera and screen transcripts.

Layout: screen on top (1080x1000), face below (1080x920), captions on the seam.
Face-only segments fill the frame. Ends on Brandkit bumper-9x16.mp4.

Run: python3 build.py            (all)   python3 build.py 3   (one)
"""
import json, os, re, subprocess, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
DL = os.path.expanduser("~/Downloads")
CAM = os.path.join(DL, "IMG_7285.MOV")
SCR = {"scr1": glob.glob(os.path.join(DL, "Screen*9.08.47*"))[0],
       "scr2": glob.glob(os.path.join(DL, "Screen*9.20.30*"))[0]}
OFF = {"scr1": 49.52, "scr2": 723.09}          # cam_time - screen_time
BUMPER = os.path.join(HERE, "../../../Brandkit/YouTube-Bumpers/renders/bumper-9x16.mp4")
OUT = os.path.join(HERE, "../../../Final Videos")
TMP = os.path.join(HERE, "tmp")
os.makedirs(TMP, exist_ok=True)

W = json.load(open(os.path.join(HERE, "words.json")))["cam"]   # [from, to, word]

def norm(w): return re.sub(r"[^a-z0-9']", "", w.lower())

def at(phrase, near):
    """Start time of the first word of `phrase` closest to `near` (cam seconds)."""
    p = [norm(x) for x in phrase.split()]
    best = None
    for i in range(len(W) - len(p) + 1):
        if [norm(W[i + k][2]) for k in range(len(p))] == p:
            if best is None or abs(W[i][0] - near) < abs(W[best][0] - near):
                best = i
    assert best is not None, phrase
    return best

def start(phrase, near): return max(0, W[at(phrase, near)][0] - 0.12)
def end(phrase, near):
    i = at(phrase, near) + len(phrase.split()) - 1
    return min(W[i][1], W[i][0] + 0.8) + 0.3   # whisper stretches a last word through silence

# crop boxes on the 3024x1964 screen, all 1.08 aspect (fits 1080x1000)
REPORT = (1862, 1724, 380, 240)
PLAN   = (1800, 1667, 1224, 100)
PROMPT = (1800, 1667, 870, 297)
PLAN2  = (1800, 1667, 1100, 0)
LOFTY  = (1800, 1667, 612, 150)

# segment: (cam_in, cam_out, layout)  layout = None (face only) or
#   (screen, screen_in or "sync", crop)
CLIPS = {
 1: ("Weekly-Seller-Update-Reel-01-My-Sellers-Get-This-Every-Friday", [
      (0.0, end("we can go from there", 39.3), None),
      (start("so here it just has", 137), end("through the whole thing", 128), ("scr1", "sync", REPORT)),
    ]),
 2: ("Weekly-Seller-Update-Reel-02-Pick-The-Tone-Before-AI-Writes-It", [
      (start("so in the executive summary i have", 97), end("in the executive summary", 135), ("scr1", "sync", REPORT)),
    ]),
 4: ("Weekly-Seller-Update-Reel-04-Youre-Using-AI-Backwards", [
      (start("it's going to ask you questions which", 844), end("win in this whole setup", 855), ("scr2", "sync", PLAN)),
      (start("at some point you can ask", 545), end("create this landing page", 564), ("scr1", "sync", PROMPT)),
      (start("i'm a big tom", 673), end("specific to you guys", 690), ("scr2", 134.0, PLAN)),
      # NOT synced on purpose: the synced screen here shows an offer amount and a buyer's name
    ]),
 3: ("Weekly-Seller-Update-Reel-03-One-Command-One-Paste-Publish", [
      (start("and then it goes", 1122), end("build that too", 1142), ("scr1", 88.0, REPORT)),
      (start("so i copied it", 1243), end("literally all i do", 1250), ("scr2", "sync", LOFTY)),
    ]),
 5: ("Weekly-Seller-Update-Reel-05-The-Listing-Appointment-Promise", [
      (start("and at that point", 1253), W[-1][1] + 0.4, ("scr1", 0.5, REPORT)),
    ]),
 6: ("Weekly-Seller-Update-Reel-06-Where-Every-Online-View-Comes-From", [
      (start("now below that it has the actual performance", 150), end("so it's very helpful", 192), ("scr1", "sync", REPORT)),
    ]),
 7: ("Weekly-Seller-Update-Reel-07-Showing-Feedback-In-The-Right-Tone", [
      (start("as far as showings go", 193), end("tone that you're kind of looking for", 232), ("scr1", "sync", REPORT)),
    ]),
 8: ("Weekly-Seller-Update-Reel-08-Show-Your-Seller-The-Work", [
      (start("so other than that i also put", 234), end("a don't fire me report", 291), ("scr1", "sync", REPORT)),
    ]),
 9: ("Weekly-Seller-Update-Reel-09-Talk-Dont-Type-Your-Prompt", [
      (start("basically what i'll do is i pull", 336), end("say what you're looking for", 366), ("scr1", "sync", PROMPT)),
    ]),
 10: ("Weekly-Seller-Update-Reel-10-Read-The-Plan-Before-You-Build", [
      (start("now this right here is what you need to read", 759), end("create all of this for you", 806), ("scr2", "sync", PLAN)),
    ]),
 11: ("Weekly-Seller-Update-Reel-11-Make-It-Your-Brand", [
      (start("you can put your own brand colors", 922), end("fully build what you're looking for", 955), ("scr1", 110.0, REPORT)),
      # not synced: the synced screen jumps between the plan and the browser mid-clip
    ]),
 12: ("Weekly-Seller-Update-Reel-12-Why-I-Let-Claude-Run-Without-Asking", [
      (start("what i do you don't have to do this", 971), end("give it all that information", 1033), ("scr2", "sync", PROMPT)),
    ]),
}

FIX = {"school": "Skool", "cloud": "Claude", "claude": "Claude", "lofty": "Lofty",
       "redfin": "Redfin", "zillow": "Zillow", "tom": "Tom", "ferry": "Ferry",
       "mac": "Mack", "and": "and"}

def fixword(w):
    core = norm(w)
    if core in FIX and core not in ("and",):
        lead = re.match(r"^\W*", w).group(0); tail = re.search(r"\W*$", w).group(0)
        return lead + FIX[core] + tail
    return w

def ass_time(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;")

def captions(n, segs):
    """3-word chunks, active word in accent-inv blue, rendered by caps.mjs, returns an ffconcat path."""
    states = []
    tl = 0.0
    for a, b, lay in segs:
        ws = [w for w in W if w[0] >= a - 0.05 and w[1] <= b + 0.05]
        y = 1000 if lay else 1480
        for i in range(0, len(ws), 3):
            chunk = ws[i:i + 3]
            for j, w in enumerate(chunk):
                s = tl + max(0, w[0] - a)
                e = tl + ((chunk[j + 1][0] if j + 1 < len(chunk) else min(w[1] + 0.25, b)) - a)
                html = " ".join(("<b>%s</b>" if k == j else "%s") % esc(fixword(x[2]).strip())
                                for k, x in enumerate(chunk))
                states.append({"s": s, "e": e, "html": html, "y": y})
        tl += b - a
    json.dump(states, open(os.path.join(TMP, f"{n}_caps.json"), "w"))
    r = subprocess.run(["node", os.path.join(HERE, "caps.mjs"), str(n)], capture_output=True, text=True)
    if r.returncode: print(r.stderr[-2000:]); sys.exit(1)
    d = f"caps{n}"
    lines = ["ffconcat version 1.0"]
    t = 0.0
    for i, st in enumerate(states):
        if st["s"] > t + 0.01:
            lines += [f"file '{d}/blank.png'", f"duration {st['s'] - t:.3f}"]
            t = st["s"]
        dur = max(0.034, st["e"] - t)
        lines += [f"file '{d}/{i:04d}.png'", f"duration {dur:.3f}"]
        t += dur
    lines += [f"file '{d}/blank.png'", "duration 1.000", f"file '{d}/blank.png'"]
    fp = os.path.join(TMP, f"{n}.ffconcat")
    open(fp, "w").write("\n".join(lines) + "\n")
    return fp

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=TMP)
    if r.returncode: print(r.stderr[-2000:]); sys.exit(1)

FACE_SPLIT = "crop=1268:1080:326:0,scale=1080:920"
FACE_FULL = "crop=608:1080:656:0,scale=1080:1920"

def build(n):
    name, segs = CLIPS[n]
    parts = []
    for k, (a, b, lay) in enumerate(segs):
        d = b - a
        p = os.path.join(TMP, f"{n}_{k}.mp4")
        if lay is None:
            fc = f"[0:v]{FACE_FULL},fps=30,setsar=1[v]"
            inputs = ["-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", CAM]
        else:
            src, sin, (cw, ch, cx, cy) = lay
            sin = a - OFF[src] if sin == "sync" else sin
            # screen recordings are variable frame rate and write nothing while the
            # screen is still, so seek early and let fps= fill the gap before trimming
            pre = min(sin, 30.0)
            inputs = ["-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", CAM,
                      "-ss", f"{sin - pre:.3f}", "-t", f"{d + pre + 1:.3f}", "-i", SCR[src]]
            fc = (f"[1:v]fps=30,trim=start={pre:.3f}:duration={d:.3f},setpts=PTS-STARTPTS,"
                  f"crop={cw}:{ch}:{cx}:{cy},scale=1080:1000,setsar=1[top];"
                  f"[0:v]{FACE_SPLIT},fps=30,setsar=1[bot];[top][bot]vstack[v]")
        run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc,
             "-map", "[v]", "-map", "0:a:0", "-t", f"{d:.3f}", "-c:v", "libx264", "-crf", "18", "-preset", "fast",
             "-c:a", "aac", "-ar", "48000", "-ac", "2", p])
        parts.append(p)
    # join (concat filter, not the demuxer: the demuxer drifted the audio), caption, loudness
    caps = captions(n, segs)
    body = os.path.join(TMP, f"{n}_body.mp4")
    k = len(parts)
    ins = sum((["-i", p] for p in parts), [])
    cat = "".join(f"[{i}:v][{i}:a]" for i in range(k)) + f"concat=n={k}:v=1:a=1[jv][ja]"
    run(["ffmpeg", "-v", "error", "-y", *ins, "-f", "concat", "-safe", "0", "-i", caps,
         "-filter_complex", f"{cat};[{k}:v]format=rgba[c];[jv][c]overlay=0:0:eof_action=pass[v];"
                            "[ja]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]",
         "-map", "[v]", "-map", "[a]", "-shortest",
         "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-c:a", "aac", "-ar", "48000", "-ac", "2", body])
    # + bumper (silent)
    out = os.path.join(OUT, name + ".mp4")
    run(["ffmpeg", "-v", "error", "-y", "-i", body, "-i", BUMPER,
         "-f", "lavfi", "-t", "3", "-i", "anullsrc=r=48000:cl=stereo",
         "-filter_complex", "[1:v]fps=30,setsar=1[b];[0:v][0:a][b][2:a]concat=n=2:v=1:a=1[v][a]",
         "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out])
    print(name, round(sum(b - a for a, b, _ in segs) + 3, 1), "s")

for n in ([int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else CLIPS):
    build(n)
