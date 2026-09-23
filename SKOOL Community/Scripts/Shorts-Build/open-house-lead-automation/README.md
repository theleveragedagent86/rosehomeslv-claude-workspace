# Open House Lead Automation: clipped Reels

12 vertical clips cut from the RAW July 14 2026 footage (Final Cut library `~/Movies/Untitled.fcpbundle/4-30-25/Original Media/`: IMG_6675, IMG_6677, IMG_6680 + the 11.04.14 AM screen recording). Captions to paste: `../../Open-House-Lead-Automation-Instagram-Reel-Captions.md`. Covers: `covers/cover-01.png` to `cover-12.png` (built by `../reel-covers/`).

Output: `SKOOL Community/Final Videos/Open-House-Reel-NN-*.mp4` (1080x1920, 30fps, -14 LUFS, 3s bumper-9x16 end card, git-ignored).

| # | Reel | Cut from |
|---|---|---|
| 01 | The Sign-In Sheets On Your Desk | 6675 0:13, 0:40, 3:09 |
| 02 | Stop Typing Your Prompts | 6675 1:16 to 2:19 |
| 03 | Why We Really Do Open Houses | 6677 2:01 to 2:42 |
| 04 | The One Line I Forgot | 6677 2:54 to 3:24 |
| 05 | Buyer First, Then Seller | 6677 4:05 to 4:44 |
| 06 | One Detail From The Sheet | 6677 4:58 to 5:30 |
| 07 | The Day Zero Text | 6677 5:41 to 6:21 (name cut) |
| 08 | Follow Up Until You Die | 6677 6:21 to 7:13 |
| 09 | One Video For Every Visitor | 6677 7:16 to 7:57 (name cut) |
| 10 | A Photo And One Command | 6677 8:20 to 8:58 |
| 11 | Claude Code Is Not Scary | 6677 9:20 to 10:17 (phone line cut) |
| 12 | What Should I Automate Next | 6680 0:16 to end |

**Privacy (read before adding clips):** the screen recording shows the open house visitor's full name and phone number in the Claude plan, so every Reel is face-only. Her first name is spoken twice; both are cut from the audio (Reels 7, 9). The "we got her phone number" line is skipped (Reel 11). The coworker whose sheets these were is never named in a clip.

**Rebuild:** `python3 build.py` (all) or `python3 build.py 3 7` (some). `words.json` = whisper small.en word timestamps for the three camera files and the screen. Same pipeline as `../weekly-seller-update/` (Playwright caption PNGs via `caps.mjs`, ffconcat overlay, loudnorm, bumper).
