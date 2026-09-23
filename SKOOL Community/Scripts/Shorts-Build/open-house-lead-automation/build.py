"""Cut the Open House Lead Automation Reels from the raw July 14 2026 footage.

Sources (raw, in the Final Cut library, not the edited long form):
  cam  IMG_6675.mov  intro, why voice input          1920x1080
  cam  IMG_6677.mov  the plan walkthrough (main take)
  cam  IMG_6680.mov  outro / comment CTA
  scr  Screen Recording 2026-07-14 at 11.04.14 AM.mov  3024x1964
words.json = whisper small.en word timestamps for all four.

PRIVACY: the screen recording shows the prospect's full name and phone number in the
Claude plan, and the camera audio says her first name. So every Reel is face-only
(the pre-sheet Claude home screen was tried for #2 but is mostly empty), and the two spots where
her first name is spoken are cut out of the audio (#7, #9). Re-check before adding clips.

Layout: face-only fills the frame, captions low. Screen segments = screen top, face bottom.
Ends on Brandkit bumper-9x16.mp4.
Run: python3 build.py (all) | python3 build.py 3 (one)
"""
import json, os, re, subprocess, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
M = "/Users/ryanrose/Movies/Untitled.fcpbundle/4-30-25/Original Media"
SRC = {"c6675": f"{M}/IMG_6675.mov", "c6677": f"{M}/IMG_6677.mov", "c6680": f"{M}/IMG_6680.mov",
       "scr": glob.glob(f"{M}/Screen*2026-07-14*")[0]}
OFF = {"c6675": 38.4}          # cam_time - screen_time, from matched 6-word runs
BUMPER = os.path.join(HERE, "../../../Brandkit/YouTube-Bumpers/renders/bumper-9x16.mp4")
OUT = os.path.join(HERE, "../../../Final Videos")
TMP = os.path.join(HERE, "tmp")
os.makedirs(TMP, exist_ok=True)
WALL = json.load(open(os.path.join(HERE, "words.json")))

def norm(w): return re.sub(r"[^a-z0-9']", "", w.lower())

def at(cam, phrase, near):
    W = WALL[cam]; p = [norm(x) for x in phrase.split()]; best = None
    for i in range(len(W) - len(p) + 1):
        if [norm(W[i + k][2]) for k in range(len(p))] == p:
            if best is None or abs(W[i][0] - near) < abs(W[best][0] - near): best = i
    assert best is not None, (cam, phrase)
    return best

def S(cam, phrase, near): return max(0, WALL[cam][at(cam, phrase, near)][0] - 0.12)
def E(cam, phrase, near):
    W = WALL[cam]; i = at(cam, phrase, near) + len(phrase.split()) - 1
    return min(W[i][1], W[i][0] + 0.8) + 0.3

PROMPT = (1800, 1667, 870, 297)
A, B, C = "c6675", "c6677", "c6680"

# (name, [(cam, in, out, layout)])  layout None = face only, or ("sync", crop)
CLIPS = {
 1: ("Open-House-Reel-01-The-Sign-In-Sheets-On-Your-Desk", [
      (A, S(A, "when you do an open house you go", 13.7), E(A, "go to your crm", 35), None),
      (A, S(A, "well let's fix that", 40.7), E(A, "well let's fix that", 41), None),
      (A, S(A, "so every single time you do", 189.8), E(A, "to my crm done", 198), None)]),
 2: ("Open-House-Reel-02-Stop-Typing-Your-Prompts", [
      (A, S(A, "so i have my", 76), E(A, "trying to create something like this", 136), None)]),
 3: ("Open-House-Reel-03-Why-We-Really-Do-Open-Houses", [
      (B, S(B, "the goal is to get them to buy", 121), E(B, "have that direction in here", 160), None)]),
 4: ("Open-House-Reel-04-The-One-Line-I-Forgot", [
      (B, S(B, "at the end i wish i did this", 173), E(B, "make a mistake like that", 204), None)]),
 5: ("Open-House-Reel-05-Buyer-First-Then-Seller", [
      (B, S(B, "because the relationship started at an open house", 245), E(B, "and then go over to that", 282), None)]),
 6: ("Open-House-Reel-06-One-Detail-From-The-Sheet", [
      (B, S(B, "do first", 298), E(B, "not great but you can", 328), None)]),
 7: ("Open-House-Reel-07-The-Day-Zero-Text", [
      (B, S(B, "what that ended up doing", 340), 360.35, None),          # cut before "Hi <name>"
      (B, 360.93, E(B, "and go from there", 380), None)]),
 8: ("Open-House-Reel-08-Follow-Up-Until-You-Die", [
      (B, S(B, "now it also has a voicemail", 380), E(B, "follow until you die", 411), None),
      (B, S(B, "here it has a handwritten note", 419), E(B, "so that's great", 429), None)]),
 9: ("Open-House-Reel-09-One-Video-For-Every-Visitor", [
      (B, S(B, "we got a personal 30 second video", 436), 457.22, None),     # cut "hey <name>"
      (B, 457.72, E(B, "recognition of who you are", 476), None)]),
 10: ("Open-House-Reel-10-A-Photo-And-One-Command", [
      (B, S(B, "building a skill that you can repeat", 500), E(B, "wait for them to reengage", 535), None)]),
 11: ("Open-House-Reel-11-Claude-Code-Is-Not-Scary", [
      (B, S(B, "you can do this in claude chat", 560), E(B, "on it of the person", 594), None),  # skips the phone number line
      (B, S(B, "and then it ultimately asked", 608), WALL[B][-1][1] + 0.4, None)]),
 12: ("Open-House-Reel-12-What-Should-I-Automate-Next", [
      (C, S(C, "because i can guarantee you", 16), WALL[C][-1][1] + 0.4, None)]),
}

FIX = {"cloud": "Claude", "claude": "Claude", "claw": "Claude", "clawcode": "Claude Code", "school": "Skool",
       "lofty": "Lofty", "formosie": "Hormozi", "hormozi": "Hormozi", "surhan": "Serhant", "mac": "Mackin",
       "ford": "FORD", "crm": "CRM", "reengage": "re-engage", "reengages": "re-engages"}

def fixword(w):
    core = norm(w)
    if core in FIX:
        lead = re.match(r"^\W*", w).group(0); tail = re.search(r"\W*$", w).group(0)
        return lead + FIX[core] + tail
    return w

def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;")

def captions(n, segs):
    states = []; tl = 0.0
    for cam, a, b, lay in segs:
        ws = [w for w in WALL[cam] if w[0] >= a - 0.05 and w[1] <= b + 0.05 and not w[2].startswith("(")]
        y = 1000 if lay else 1480
        for i in range(0, len(ws), 3):
            chunk = ws[i:i + 3]
            for j, w in enumerate(chunk):
                s = tl + max(0, w[0] - a)
                e = tl + ((chunk[j + 1][0] if j + 1 < len(chunk) else min(w[1] + 0.25, b)) - a)
                html = " ".join(("<b>%s</b>" if k == j else "%s") % esc(fixword(x[2]).strip().strip('"'))
                                for k, x in enumerate(chunk))
                states.append({"s": s, "e": e, "html": html, "y": y})
        tl += b - a
    json.dump(states, open(os.path.join(TMP, f"{n}_caps.json"), "w"))
    r = subprocess.run(["node", os.path.join(HERE, "caps.mjs"), str(n)], capture_output=True, text=True)
    if r.returncode: print(r.stderr[-2000:]); sys.exit(1)
    d = f"caps{n}"; lines = ["ffconcat version 1.0"]; t = 0.0
    for i, st in enumerate(states):
        if st["s"] > t + 0.01:
            lines += [f"file '{d}/blank.png'", f"duration {st['s'] - t:.3f}"]; t = st["s"]
        dur = max(0.034, st["e"] - t)
        lines += [f"file '{d}/{i:04d}.png'", f"duration {dur:.3f}"]; t += dur
    lines += [f"file '{d}/blank.png'", "duration 1.000", f"file '{d}/blank.png'"]
    fp = os.path.join(TMP, f"{n}.ffconcat"); open(fp, "w").write("\n".join(lines) + "\n")
    return fp

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=TMP)
    if r.returncode: print(r.stderr[-2000:]); sys.exit(1)

FACE_SPLIT = "crop=1268:1080:326:0,scale=1080:920"
FACE_FULL = "crop=608:1080:656:0,scale=1080:1920"

def build(n):
    name, segs = CLIPS[n]; parts = []
    for k, (cam, a, b, lay) in enumerate(segs):
        d = b - a; p = os.path.join(TMP, f"{n}_{k}.mp4")
        if lay is None:
            fc = f"[0:v]{FACE_FULL},fps=30,setsar=1[v]"
            inputs = ["-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", SRC[cam]]
        else:
            _, (cw, ch, cx, cy) = lay
            sin = a - OFF[cam]; pre = min(sin, 30.0)
            inputs = ["-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", SRC[cam],
                      "-ss", f"{sin - pre:.3f}", "-t", f"{d + pre + 1:.3f}", "-i", SRC["scr"]]
            fc = (f"[1:v]fps=30,trim=start={pre:.3f}:duration={d:.3f},setpts=PTS-STARTPTS,"
                  f"crop={cw}:{ch}:{cx}:{cy},scale=1080:1000,setsar=1[top];"
                  f"[0:v]{FACE_SPLIT},fps=30,setsar=1[bot];[top][bot]vstack[v]")
        run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc,
             "-map", "[v]", "-map", "0:a:0", "-t", f"{d:.3f}", "-c:v", "libx264", "-crf", "18", "-preset", "fast",
             "-c:a", "aac", "-ar", "48000", "-ac", "2", p])
        parts.append(p)
    caps = captions(n, segs)
    body = os.path.join(TMP, f"{n}_body.mp4"); k = len(parts)
    ins = sum((["-i", p] for p in parts), [])
    cat = "".join(f"[{i}:v][{i}:a]" for i in range(k)) + f"concat=n={k}:v=1:a=1[jv][ja]"
    run(["ffmpeg", "-v", "error", "-y", *ins, "-f", "concat", "-safe", "0", "-i", caps,
         "-filter_complex", f"{cat};[{k}:v]format=rgba[c];[jv][c]overlay=0:0:eof_action=pass[v];"
                            "[ja]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]",
         "-map", "[v]", "-map", "[a]", "-shortest",
         "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-c:a", "aac", "-ar", "48000", "-ac", "2", body])
    out = os.path.join(OUT, name + ".mp4")
    run(["ffmpeg", "-v", "error", "-y", "-i", body, "-i", BUMPER,
         "-f", "lavfi", "-t", "3", "-i", "anullsrc=r=48000:cl=stereo",
         "-filter_complex", "[1:v]fps=30,setsar=1[b];[0:v][0:a][b][2:a]concat=n=2:v=1:a=1[v][a]",
         "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out])
    print(name, round(sum(b - a for _, a, b, _ in segs) + 3, 1), "s")

if __name__ == "__main__":
    for n in ([int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else CLIPS):
        build(n)
