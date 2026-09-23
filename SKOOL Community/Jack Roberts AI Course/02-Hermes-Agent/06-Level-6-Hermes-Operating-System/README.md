# Level 6: Hermes Operating System

**Section:** 🥇 Hermes Agent  
**Course:** Claude Code Course (AI Automations by Jack)  
**Lesson URL:** https://www.skool.com/aiautomationsbyjack/classroom/af686ad3?md=b859c13bdbf0440895d3505fb19f9aad  
**Video length:** 27m 50s  
**Lesson ID:** `b859c13bdbf0440895d3505fb19f9aad`

---

## Description (as posted by Jack)

📆 Launch Date: Sunday 19th July

![image.png](images/2ea091e7b19e448883ab817f.png)

🔥 Glaido: [https://bit.ly/4eGoI3R](https://bit.ly/4eGoI3R) (use code: `WHSAAKXO`for 1 FREE month)

### 💪 TailScale install (run this on VPS)

`curl -fsSL https://tailscale.com/install.sh | sh`

`sudo tailscale up`

### 📊 Setup OS on TailScale

`I want you to set up permanent access to my Claude Code Agentic OS, which`

`lives on my personal computer. You are running on my VPS. Both machines`

`are on my Tailscale network. Configure everything yourself, step by step,`

`and only ask me for what you genuinely need.`

`STEP 1 — Check the ring.`

`Run tailscale status. Confirm this VPS is on a tailnet and list the`

`other devices you see. Ask me which one is my main computer, and note its`

`MagicDNS name and Tailscale IP.`

`STEP 2 — Build the bridge.`

`Test whether you can already reach it over SSH. If not, guide me through`

`it ONE instruction at a time:`

` a) On my computer: System Settings → General → Sharing → Remote Login → ON`

` b) On this VPS: generate an SSH key for yourself (ssh-keygen, no passphrase)`

` c) Give me the exact one-line command to run on my computer to authorize`

`    that key.`

`Ask me for my computer's username. Verify with a passwordless SSH test`

`before moving on.`

`STEP 3 — Find my OS.`

`Over SSH, locate my Claude Code Agentic OS and its data on that machine:`

`the OS folder itself, ~/.claude/projects (my chat transcripts),`

`~/.claude/CLAUDE.md, and any memory folders. Search first, then confirm`

`the paths with me. Do not copy anything yet.`

`STEP 4 — Prove it.`

`Read ONE small file (my most recent chat transcript or the OS readme) and`

`summarize it back to me in one line, so we both know the bridge works`

`end to end.`

`STEP 5 — Remember it.`

`Save to your memory: the device name, username, and every confirmed path —`

`plus these standing rules: access is READ-ONLY unless I explicitly ask;`

`never modify or delete anything on my computer; pull specific folders`

`with rsync when needed, never the whole disk.`

`STEP 6 — Make it useful.`

`Suggest three automations this now makes possible (for example: a nightly`

`summary of my Claude Code sessions, fetching any file from my computer on`

`request, or a weekly digest of what my OS has been doing). Set up the`

`ones I approve.`

`SECURITY RULES, ALWAYS:`

`- Connect only via Tailscale names or 100.x addresses. Never a public IP.`

`- Never copy .env files, API keys or credentials off my computer.`

`- If any step fails, show me the exact error. Do not guess or work around it.`

⏱️ Timestamps  
00:00 – Welcome & Why You Need an Agentic OS  
01:22 – Downloading the Hermes/Claude OS Files  
02:08 – Running the Claude OS Setup Wizard  
02:41 – Auto-Detecting Your Installed AI Tools  
03:01 – Connecting Pinecone, Obsidian & Notion  
03:56 – Tracking AI Usage Costs & Time Saved  
04:46 – Setting Up the Daily "Dream" Analysis  
05:33 – Dashboard Homepage Walkthrough  
06:42 – Graphify: Visualizing & Chatting With Codebases  
09:12 – Hermes Agent Panel & Model Switching  
10:04 – Pantheon: Adding Custom Personas  
10:33 – Ministry of Experts: Assigning Models to Roles  
10:57 – Max Tokens Per Call Settings  
11:22 – GitHub Backup & Pushing Personas  
11:56 – Claude OS Bridge for Cross-Model Access  
12:17 – Saved Skills & Artifacts Overview  
12:46 – Obsidian Memory Demo With Glido Voice Tool  
15:44 – Setting Up Glido + Hermes MCP Integration  
19:18 – Creating Voice-Activated Reminders & Cron Jobs  
21:10 – Five Ways to Access Hermes  
22:00 – Portable Brain Folder & GitHub Syncing  
22:44 – Using Tailscale for Cross-Device File Access  
24:05 – Setting Up the Telescope App  
25:08 – Remote Login & Cross-Computer Access  
25:34 – Bridging a VPS Setup With Local Data  
26:11 – How the Mesh VPN (WireGuard) Works Securely  
27:10 – Security Rules & Session Wrap-Up

#### Hey, in this video, you're gonna learn:

🖥️ How to download, install, and run the Hermes Agentic Operating System (OS) locally using Claude Code — including the setup wizard, profile configuration, and first-run onboarding

📊 How to use the Hermes OS dashboard — tracking monthly AI spend, skill savings, dream insights, mission control goals, Pantheon personas, Ministry of Experts, and the AI model leaderboard

🗺️ How Graphify works inside the OS — mapping GitHub repo relationships into a knowledge graph so Claude and Hermes can query codebases without reading every file (saving up to 480,000 tokens per session)

🎙️ How to connect Glider (speech-to-text tool) to Hermes as a one-button voice interface — sending tasks, setting cron job reminders, summarizing YouTube videos, and ingesting content directly into Obsidian memory from anywhere on your desktop

🔗 How the Claude OS Bridge works — enabling Hermes to read your Claude chat logs, dream outputs, and memory files so both agents share a unified, cross-platform knowledge system

🌐 How to install Tailscale and set up a private WireGuard mesh VPN — connecting your Mac, laptop, and VPS so Hermes can access files across all devices securely without exposing open ports

💾 How to keep the Hermes OS portable and version-controlled — using a private GitHub repo to back up your memory, skills, and personas so you can move between local hardware and VPS without losing anything

#### In this video, I cover:

You'll start by understanding why a model-agnostic agentic OS is the missing layer — a single command center that connects Claude, Hermes, Obsidian, Pinecone, Notion, and every other tool you use, without being locked into any one platform.

You'll then download the OS from the classroom, open it in Claude Code, run the setup wizard, and configure your profile — including API key tracking, time value calculator, dream schedule, and which engine (Hermes or Claude) runs your daily briefing.

You'll get a full walkthrough of every dashboard section: monthly AI spend, skill savings tracker, dream insights, mission control goal-setting (with task split between Hermes and you), Pantheon persona builder, Ministry of Experts model roster, project knowledge graph, and the AI model leaderboard with pre-built cost routing playbooks.

You'll see how Graphify maps the full relationship graph of any GitHub repo so Hermes can answer questions about codebases by querying a graph instead of reading every file — dropping token cost dramatically per session.

You'll connect Glider (speech-to-text) to Hermes as a one-button voice layer: highlight text on any webpage, speak a command, and Hermes will summarize a YouTube video, set a 30-minute reminder, or ingest an article directly into your Obsidian vault — all without opening a terminal.

You'll finish by installing Tailscale to create a private encrypted mesh between your desktop, laptop, and VPS — giving Hermes secure cross-device file access while keeping everything invisible to the public internet.

#### Who this is for:

- Hermes users who have completed setup and memory configuration and are ready to centralize their entire AI stack — Claude, Hermes, Obsidian, GitHub, and external tools — into one model-agnostic operating system.

- Builders and agency owners who want to access Hermes from anywhere (voice, browser, terminal, desktop app) and keep their agent portable, version-controlled, and securely connected across multiple devices or a VPS.

## Linked resources

| Resource | Link |
|---|---|
| 📈 Hermes Curriculum | https://hermes-masterclass.vercel.app/ |
| 🎙️ Glaido | https://bit.ly/4eGoI3R |
| 🧵 Tail Scale | https://tailscale.com |

## Downloaded attachments

| Resource | File | Size | Path |
|---|---|---|---|
| 📊 Chapter 6 Slides | `Chapter 6 - The Hermes Operating System.html` | 3580 KB | `attachments/Chapter 6 - The Hermes Operating System.html` |
| transcript | `Hermes Operating System.txt` | 36 KB | `attachments/Hermes Operating System.txt` |

## Transcript

Full word-for-word transcript: [transcript.md](transcript.md)
