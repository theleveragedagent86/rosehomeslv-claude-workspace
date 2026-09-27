#!/usr/bin/env python3
"""Upload the 24 Reels to The Leveraged Agent YouTube channel as scheduled Shorts.

Stdlib only, no pip installs. Reads yt_manifest.json (built from YOUTUBE-SHORTS-METADATA.md
and POSTING-SCHEDULE.md). Each video goes up private with a publishAt, so YouTube publishes it
on schedule with no further action.

One-time setup, in this order:
  1. Google Cloud console: a project with YouTube Data API v3 enabled.
  2. An OAuth client of type "TV and Limited Input devices".
  3. Save it as ~/.config/yt-upload/client.json  ->  {"client_id": "...", "client_secret": "..."}
Then run this script and approve the code it prints, once. The refresh token is cached at
~/.config/yt-upload/token.json and every later run is hands off.

  python3 yt_upload.py            # upload everything still pending
  python3 yt_upload.py --dry-run  # print what would go up
Progress is written to yt_upload_state.json, so a rerun resumes and never double-posts.
"""
import json, os, sys, time, urllib.request, urllib.parse, urllib.error, mimetypes

CFG = os.path.expanduser("~/.config/yt-upload")
CLIENT, TOKEN = f"{CFG}/client.json", f"{CFG}/token.json"
HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST, STATE = f"{HERE}/yt_manifest.json", f"{HERE}/yt_upload_state.json"
SCOPE = "https://www.googleapis.com/auth/youtube.upload"
CHUNK = 8 * 1024 * 1024


def post(url, data, headers=None):
    body = urllib.parse.urlencode(data).encode() if isinstance(data, dict) else data
    req = urllib.request.Request(url, body, headers or {})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def device_login(cid, secret):
    d = post("https://oauth2.googleapis.com/device/code", {"client_id": cid, "scope": SCOPE})
    print(f"\nOpen {d['verification_url']} and enter code: {d['user_code']}\n", flush=True)
    while True:
        time.sleep(d.get("interval", 5))
        try:
            t = post("https://oauth2.googleapis.com/token", {
                "client_id": cid, "client_secret": secret, "device_code": d["device_code"],
                "grant_type": "urn:ietf:params:oauth:grant-type:device_code"})
            return t
        except urllib.error.HTTPError as e:
            err = json.load(e).get("error")
            if err not in ("authorization_pending", "slow_down"):
                raise SystemExit(f"authorization failed: {err}")


def access_token():
    c = json.load(open(CLIENT))
    if not os.path.exists(TOKEN):
        tok = device_login(c["client_id"], c["client_secret"])
        json.dump(tok, open(TOKEN, "w"))
    tok = json.load(open(TOKEN))
    fresh = post("https://oauth2.googleapis.com/token", {
        "client_id": c["client_id"], "client_secret": c["client_secret"],
        "refresh_token": tok["refresh_token"], "grant_type": "refresh_token"})
    return fresh["access_token"]


def upload(item, token):
    meta = {"snippet": {"title": item["title"], "description": item["description"],
                        "tags": item["tags"], "categoryId": "22"},
            "status": {"privacyStatus": "private", "publishAt": item["publishAt"],
                       "selfDeclaredMadeForKids": False}}
    size = os.path.getsize(item["file"])
    req = urllib.request.Request(
        "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
        json.dumps(meta).encode(),
        {"Authorization": f"Bearer {token}", "Content-Type": "application/json; charset=UTF-8",
         "X-Upload-Content-Length": str(size),
         "X-Upload-Content-Type": mimetypes.guess_type(item["file"])[0] or "video/mp4"})
    with urllib.request.urlopen(req) as r:
        session = r.headers["Location"]
    sent = 0
    with open(item["file"], "rb") as f:
        while sent < size:
            buf = f.read(CHUNK)
            put = urllib.request.Request(session, buf, method="PUT")
            put.add_header("Content-Length", str(len(buf)))
            put.add_header("Content-Range", f"bytes {sent}-{sent+len(buf)-1}/{size}")
            try:
                with urllib.request.urlopen(put) as r:
                    return json.load(r)["id"]
            except urllib.error.HTTPError as e:
                if e.code != 308:
                    raise
                sent += len(buf)
                print(f"    {sent*100//size}%", flush=True)


def main():
    dry = "--dry-run" in sys.argv
    items = json.load(open(MANIFEST))
    state = json.load(open(STATE)) if os.path.exists(STATE) else {}
    token = None if dry else access_token()
    for i, it in enumerate(items, 1):
        name = os.path.basename(it["file"])
        if name in state:
            print(f"[{i:02d}/24] already up as {state[name]}, skipping"); continue
        print(f"[{i:02d}/24] {it['publishAt']}  {it['title']}")
        if dry:
            continue
        vid = upload(it, token)
        state[name] = vid
        json.dump(state, open(STATE, "w"), indent=1)
        print(f"    https://youtu.be/{vid}", flush=True)
    print("done")


if __name__ == "__main__":
    main()
