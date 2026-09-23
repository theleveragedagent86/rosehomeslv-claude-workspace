# Hermes Agent Section: Structural Teardown and Content Map

Source: [`02-Hermes-Agent/`](02-Hermes-Agent/) (9 lesson folders, README + transcript each), cross-referenced against [`01-Claude/05-Level-5-Hermes-Agent/`](01-Claude/05-Level-5-Hermes-Agent/) and [`01-Claude/11-Claude-Code-Hermes-OS/`](01-Claude/11-Claude-Code-Hermes-OS/).

**Transcript quality note:** every transcript is machine-generated and badly mangled in places. "Hermes agent" appears as "him is agent," "homies agent," "hermy's." "Docker" appears as "darker." "Claude Code" appears as "cloud code" and "called code." "cron job" appears as "crun job" and "Chron." Quotes below are reproduced as they appear in the files, with the intended word noted where the garble obscures meaning.

---

## 1. What Hermes Actually Is

**Hermes Agent is an open-source, self-hosted, model-agnostic agent harness.** Not a model, not a chatbot, not a SaaS product. It is the wrapper (Jack's word: "harness") that sits around whatever LLM you point it at and gives that model memory, tools, scheduling, and channels.

Concretely, from Levels 1 through 6:

**What it is built on**
- An open-source GitHub project. Level 1 says "Hermes Agent is one project from the new research team." Level 4 cites "214,000 stars" and "1777 people that are actually [contributing]." The Claude-section Level 5 lesson cites "154,000 stars," which is the same repo at an earlier recording date.
- Installed with a **single terminal command** copied from the Hermes website (Level 2). No coding background assumed.
- Runs in one of three environments (Level 2): **local machine** (Jack's recommendation, he runs it on a Mac Mini class machine 24/7), **Docker container** (isolation, "carve out a piece of space on your computer and Hermes lives in this container"), or **VPS** (Hostinger managed Hermes shown at $5.99/mo).
- Ships a **terminal alias `herk`** in the Docker path, so `herk version` and `herk` replace the long docker-prefixed command.

**Four-layer anatomy (Level 1, the core mental model of the whole section)**

| Layer | What it is |
|---|---|
| **Gateway** | The senses. One always-on process listening on every channel (Telegram, WhatsApp, terminal, dashboard, voice). |
| **Brain** | The model. Reads the message, reasons, picks the tool. Swappable. |
| **Body** | The hands. Terminal, files, browser, computer control (moves the mouse and clicks), MCP connectors. |
| **Memory** | Persistent knowledge base. "What keeps it who you are." |

Plus **a four-step learning loop**: observe, write to memory, review, improve. Jack's image: "a snowball rolling downhill, every session it picks up a little bit more about you."

**What it actually does**
- Drafts emails, does deep research, reads and amends files on your desktop, browses the web, moves your mouse, downloads YouTube videos and reads transcripts.
- Runs **scheduled missions** (cron jobs) and messages you proactively. The canonical example throughout the section is the **morning brief** at 8am with weather, calendar, last 50 emails, an inspirational quote, and a suggested priority based on the whole conversation history.
- **Writes its own skills.** `/learn` turns a completed workflow, or a pointed-at GitHub repo, into a reusable named skill saved to long-term memory.
- **Switches models on command**, mid-conversation, either by `/model` dropdown or by just telling it ("switch to DeepSeek"). Jack's framing: "the agent who is executing is also the agent that can do its own settings."

**Memory system (Level 4, technically the most specific lesson)**
- Real memory is **two markdown files**: `memory.md` (approx 2,200 characters) and `user.md` (approx 1,400 characters). Both are injected into every session at the start. Total roughly 4,000 characters, or 650 to 700 words.
- Anything older is retrieved via **session search: full-text search over SQLite**, described as "zero token cost until it opens up and gets a hit."
- Three tiers: **working memory, session, long-term archive.**
- Context is explicitly not memory: "a million token context window is not a memory."
- `soul.md` (introduced Level 1) is a separate markdown file holding personality, preferences, business context, and voice. Template link is a Notion page. Jack's line: "one markdown file tells Hermes who it is and who you are."

**What a user ends up with after Level 8**

A complete personal agent stack, specifically:

1. Hermes installed locally (or Docker/VPS), with an OpenRouter API key carrying a hard monthly spend cap.
2. A `soul.md` filled out with the student's own voice and business.
3. Telegram wired as the home channel, locked to a single user ID.
4. Gmail, Google Calendar, and a meeting-note tool (Granola) connected via Zapier MCP, with credentials passed through the terminal so they never land in chat logs.
5. A **daily automatic GitHub backup to a private repo**, giving version-controlled rollback of the whole agent ("I like the Hermes I spoke to six weeks ago. We can bring it back to life").
6. A memory stack: `memory.md` + `user.md` + an **Obsidian LLM wiki** built on the Karpathy self-referential method + **Graphify** knowledge graphs of code repos + a **Claude OS Bridge** letting Hermes read Claude Code chat logs and vice versa.
7. Named model routing: a **Pantheon** of personas, a **Ministry of Experts** roster, a **Council / Ministry of Agents** mixture-of-agents pipeline.
8. The **Hermes/Claude Agentic Operating System**: a local dashboard (downloaded as a zip from the Skool classroom, opened in Claude Code, run on localhost) showing monthly AI spend, skill savings in dollars, dream insights, mission control goals, memory browser, project knowledge graph, and a model leaderboard.
9. Voice access via Glider (Jack's own speech-to-text startup) wired to Hermes over MCP, so any highlighted text on any webpage can be sent to the agent with one button.
10. Cross-device access via **Tailscale** (WireGuard mesh VPN), so a VPS Hermes can read files on the home Mac over a 100.x address with no open ports.
11. A security posture: four permission tiers, an always-gate list, three kill switches, spend caps, key rotation, Helicone/Langfuse observability.
12. A monetization model: setup fee plus AI back office retainer ($2K to $8K/mo, $3,200 average cited), outcome-based pricing, a niche, and a "fleet" of client Hermes instances on the student's own hosting.

---

## 2. The Level Ladder

| Level | Title | Runtime | What it unlocks | Hard dependency |
|---|---|---|---|---|
| **0** | Start Here | 4m 33s | Curriculum map only. No build. Tells you the section is "an evolving curriculum" and routes you to Claude-section Level 5 if the Hermes chapters have not dropped yet. | None |
| **1** | Foundations | 18m 07s | Vocabulary and mental models: agent vs chatbot, harness vs model, four-layer anatomy, learning loop, `soul.md`, Hermes vs Claude Code. One live demo (YouTube research). | None |
| **2** | Setup Hermes | 25m 08s | A running agent. Local one-line install, Docker walkthrough, OpenRouter key with spend cap, model selection, Telegram + QR + user-ID lock, `herk` alias, first cron job, **daily GitHub backup**. | L1 (needs to know what a harness is) |
| **3** | Powering Hermes | 37m 17s (longest) | Hands and brains. MCP connections (Granola, Gmail, Calendar via Zapier), secure credential passing, `/steer`, `/restart`, `/model`, the routing decision tree, OpenRouter as master key, Ollama local models, Hermes Cloud, **Pantheon**, **Ministry of Experts**, **the Council / Ministry of Agents**. | L2 (agent must exist and be reachable) |
| **4** | Hermes Memory | 29m 52s | Memory that compounds. Context vs memory, three tiers, `memory.md` + `user.md`, SQLite session search, `/learn`, **Claude OS Bridge**, the **dreaming function**, **Obsidian LLM wiki (Karpathy method)**, **Graphify**, memory pruning by recency/importance/relevance, **memory poisoning**. | L3 (connectors extend memory; models must be routable) |
| **5** | Power Features | 24m 23s | The command layer and autonomy. `/steer`, `/queue` (`/q`), `/stop`, `/undo`, `/compress`, `/journey`, `/MOA`, `/learn`, **Completion Contracts** (`/goal` with verify + constraints + boundaries, 20-turn judge loop), **the Curator** (7-day skill grading cycle), **proactivity's three wires**, **parallelized sub-agents** (concurrency of 3), parallel tool calling. | L4 (skills and goals are written to memory; `/learn` is meaningless without it) |
| **6** | Hermes Operating System | 27m 50s | The command center. Download the OS zip, open in Claude Code, run setup wizard, auto-detect installed CLIs, connect Pinecone/Obsidian/Notion, set your hourly value, configure the dream, then the full dashboard. Plus Glider voice MCP, five ways to access Hermes, portable brain folder, **Tailscale mesh**. | L5 (dashboard surfaces Pantheon, Ministry, goals, skills that L3 to L5 created) |
| **7** | Security & Compliance | 20m 34s | Guardrails. Locked by design, principle of least access, four permission tiers, "prompts are not permissions," always-gate list, approval gates with 30-minute windows, three kill switches, verify rule, spend and loop protection, secret management, Helicone/Langfuse, GDPR right to erasure, EU AI Act transparency (Aug 2, 2026), three office rules, 20-minute lockdown checklist. | L6 (you cannot lock down an attack surface you have not built; Tailscale kill switch requires L6) |
| **8** | Make Money with Hermes | 15m 21s (shortest after L0) | Business model. Two income paths, locksmith analogy, setup fee + AI back office retainer, retainer benchmarks, billing-cycle stickiness, outcome pricing at ~10% of first-year value, engineer's parable, niching down, build once sell many, the bottleneck exercise, the fleet model. | L7 (you cannot sell to a business without a compliance answer) |

**The dependency chain in one line:** understand the harness (L1), make it exist (L2), give it hands and brains (L3), give it memory that compounds (L4), give it autonomy and a command layer (L5), give it a cockpit and reach across devices (L6), put walls around it (L7), sell it (L8).

Levels 1 through 6 are strictly cumulative. Level 7 is retro-applied to everything built in 2 through 6. Level 8 is entirely business, no build.

**Build order stated inside the lessons themselves:**
1. Install locally with one line.
2. OpenRouter key with a credit limit before you pick a model.
3. Pick a model.
4. Pick a terminal backend.
5. Pick a messaging platform, then lock the user ID.
6. Select CLI tools.
7. Set the `herk` alias.
8. Test with `herk version`.
9. **Set the GitHub daily backup before you connect anything else.** Level 2 is explicit: "before we go into connections that are going to completely open up your world in the next level, I want you to do one of the most important things."
10. Then, and only then, MCP connections in Level 3.

---

## 3. Lesson Anatomy: The Repeatable Jack Template

Read closely: Levels 0, 1, 2, 4, 6 (plus 3, 5, 7, 8 for confirmation). The template is remarkably rigid.

### Opening 30 seconds: five moves, same order, every single lesson

1. **Fixed greeting.** "Hey there, beautiful AI automator." Verbatim in Levels 0, 1, 2, 4, 5, 7, 8. Level 3 opens "So beautiful AI automator." Level 6 varies it to "Howdy, beautiful AI automator." The greeting is a brand asset, not a throwaway.
2. **Name the level and the section by number.** "welcome to level two in the Hermes masterclass," "welcome to chapter six," "welcome to level four of the Hermes masterclass." The student always knows exactly where they are in the ladder.
3. **Superlative claim about this specific lesson.** L0: "the most comprehensive, most informative, no fluff." L1: "the most comprehensive Hermes Masterclass on planet Earth, potentially even the galaxy." L5: "This one is amazing. You are going to love it." L3: "I have some incredible things for you in today's video."
4. **The coffee ritual.** A physical state-change instruction. L1: "grab that phone, put it on, do not disturb and put it off to the side then. I want you to grab that beautiful coffee, sit down and lock in." L5: "I hope you caffeinated. I hope you got that beautiful coffee. I hope the phone is on do not disturb." L6: "I hope you've got your beautiful water, and most importantly, that coffee lockdown." L7: "I have my spicy water. I have my beverages." This is the single most consistent device in the whole section.
5. **Spoken table of contents.** Never a slide read-off, always a run-through in his own voice of the four to seven things this lesson covers. L3: "First thing we're gonna do is we're gonna go through connections. We're gonna go through the concept of owning the agent and renting the brain. We're gonna go through the routing decision tree..."

Levels 5 and 8 add a sixth move: **a recap of the ladder so far.** L5: "So let's recap. We built it. We powered it. We've given it a memory." L8: "Every chapter has been building up to this stage."

### How he frames the promise

Never "you will learn X." Always **"you will be ahead of people who don't know X,"** plus a scarcity claim that the material is not available elsewhere.

- L0: "stuff I have never shared anywhere else."
- L1: "why this is your unfair advantage and one of the most important modules that you're ever going to go through."
- L3: "you are ahead of 99.999999% of people with this stuff. You literally have knowledge that most people don't even know."
- L3: "I get emails from companies wanting to pay me to set this up. And I just share it here with you guys."
- L2: transparency framing as proof of trustworthiness. He spends a full minute explaining that VPS recommendations elsewhere are sponsored, then says "I always try to do what I personally do and I'm not for sale on that way."

He also **credentials himself by hours spent, not by results**: "I've spent so much time in Hermes agent. I've literally seen every Hermes masterclass on the planet. I live in it. I teach it every day" (L0). "I actually spent over seven hours alone on the onboarding" (L6).

### Demo vs theory sequencing

The pattern is **analogy, then concept, then live demo, then the actual prompt, then confirm it worked**, repeated in a loop, roughly 3 to 6 minutes per cycle.

The analogy always comes first and it is always a physical, non-technical object:
- Vending machine vs chief of staff (L1, agent vs chatbot)
- Engine vs car (L1 and L3, model vs harness)
- Race car vs cargo ship (L1, Claude Code vs Hermes)
- Three houses, one tenant (L2, local vs Docker vs VPS)
- Shipping container, cookie cutter vs live copy (L2, Docker image vs container)
- Dispatcher at a switchboard, CEO answering phones, Elon Musk painting walls (L3, model routing)
- Master key ring (L3, OpenRouter)
- Workshop with the door shut (L3, local models)
- RAM vs desk, whiteboard vs filing cabinet, hotel front desk ledger, librarian reshelving (L4, memory)
- Building inspector (L5, completion contracts)
- Butler who actually knocks (L5, proactivity)
- Neo downloading Kung Fu (L5, `/learn`)
- Runners on a racetrack (L5, parallel tool calls)
- Cockpit / engine room / control panel, Lego block set (L6, the OS)
- Hospital lobby vs surgical theater, bank teller with a time-locked vault, dead man's switch, fuse box, doctor's office rules (L7)
- Locksmith, watermill, cookbook, compound interest (L8)

Theory is never allowed to run long without a demo. In Level 4 the memory theory runs about three minutes before he cuts to "I can actually show you this as an example. I came over here I said hey could you tell me one message I sent to you on the 11th of July."

**The demo always includes the literal prompt, read aloud, word for word.** This is the highest-value structural move in the section. He does not paraphrase what to type. Levels 3, 4, 5, and 6 all contain full spoken prompts the student can transcribe. Level 3's Granola connection prompt and Level 4's Obsidian wiki prompt are complete, copyable, and delivered in a normal speaking voice.

**Failures stay in the cut.** L2: "Where is Docker? Docker is eluding us." L3: "the first one wasn't actually successful. I said, hey dude, try this one again." L5: "I need to go ahead and fix the model because the model isn't working." L6: "I need to retry this one here and repair the install." He never edits out a broken step, and he never apologizes for one.

### How he handles setup tedium

Four distinct techniques, and this is the most transferable part of the whole teardown.

1. **Delegate the tedium to the AI itself.** Level 2's Docker install is not a click-by-click tutorial. He copies the entire written setup guide, pastes it into a fresh Claude conversation, and says "I want you to configure anything that needs to be configured... and then let me know if there's any other information that I need to know in this process." Then: "cloud can shepherd you through the entire process."
2. **Teach the meta-move, not the steps.** Level 3, on connecting Zapier MCP: "the reason I'm doing it this way, guys, rather than just entering the command, it's because I want you to learn the process of how to fish, how to connect anything. So literally anything you're never going to be stuck by doing it this way at all."
3. **Pre-emptively de-jargon.** Every technical word gets a one-sentence civilian definition on first use, plus a personal disclaimer. Terminal: "just fancy way of... I have a non-coding background. I actually studied law... All you do, all this is, is just code and it talks to the computer." Cron: "nerd speak... effectively, a cron job is essentially just a reminder." GitHub: "basically an online repo full of loads of information and bits and bobs." He also tells students to make the AI explain it: "explain to me how containers work inside Docker, like I'm five years old. Actually, not like quite five years old, but like I am maybe 10 or 12 years old."
4. **Mark the optional path clearly and give an honest recommendation.** Level 2 spends five minutes on a comparison table (fastest to set up / full file access / isolated / always-on / cost) and then says flatly: "My honest take, as I say, is to start on your machine." Docker and VPS are presented, demoed, and then explicitly labeled "optional, as I say, not required. It's an additional step."

### How he closes and hands off

Five moves, again in fixed order:

1. **Declare the level complete and congratulate.** L1: "congratulations by the way, for completing the foundations of Hermes agent. You now have a great and excellent understanding of the architecture."
2. **Compress what was just gained into one sentence.** L3: "And so now you have a full understanding of the [Hermes] agent, we've connected it, and you can substitute the brain."
3. **Pose the next level as an open question, not a topic.** L3: "But it does take us on to one interesting question here. And that is, how do we give it a memory that never forgets?" L4: "it does lead us nicely onto the power features. Now we've got the memory, what powerful things can we do with this?"
4. **Bullet the next lesson's contents out loud.** L2: "I'm going to show you the routing decision tree. We're going to go through an [OpenRouter] masterclass... I'm going to show you how you can get your own models running."
5. **The coffee handoff.** Verbatim closer in seven of nine lessons. L1: "So grab that coffee, relax, and I'll catch you inside chapter two." L2: "get that coffee and lockdown and I'll catch you inside the next training." L4: "grab that beautiful coffee and I will catch you inside the next chapter." L5: "grab that beautiful coffee and get ready to lock in for the next training." L6: "grab that coffee and I'll catch you inside the next training." L7: "Grab that coffee and I look forward to catching you inside the next training."

Level 8 breaks the pattern deliberately: instead of a coffee handoff to a next level, it ends with a **membership upsell** ("join annual. Not only you going to save over 50% on your membership") and a route back to the Claude Code masterclass.

**Also present in most closes: an action step.** L4: "do these steps today, we're going to do everything I just showed you, get your obsidian wiki set up." L7: "run the three kill switches at once today with the timer." L7 also gives a copy-paste homework hack: "give it control A this entire presentation. Ctrl + C, drop it in Hermes agent and say, I want to go through this and come up with an action plan."

---

## 4. Hook and Transition Language

Twenty short phrases, verbatim from the transcripts, with the lesson each appears in.

**Openers and hooks**
1. "Hey there, beautiful AI automator." (every lesson, Levels 0 through 8)
2. "grab that phone, put it on, do not disturb and put it off to the side" (Level 1: Foundations)
3. "I hope you caffeinated. I hope you got that beautiful coffee." (Level 5: Power Features)
4. "We built it. We powered it. We've given it a memory." (Level 5: Power Features)
5. "Every chapter has been building up to this stage." (Level 8: Make Money with Hermes)

**Concept-setting one-liners**
6. "you got a vending machine versus a chief of staff" (Level 1: Foundations)
7. "the more that you use it, the better it gets" (Level 1: Foundations)
8. "Three different houses it could live in for one tenant." (Level 2: Setup Hermes)
9. "let's not hire Elon Musk to paint our walls" (Level 3: Powering Hermes)
10. "a million token context window is not a memory" (Level 4: Hermes Memory)
11. "The building doesn't decide the house is finished. The inspector does." (Level 5: Power Features)
12. "prompts as they're not as permissions" [prompts are not permissions] (Level 7: Security & Compliance)
13. "You didn't invent the lock. You learned how to fit it." (Level 8: Make Money with Hermes)

**Re-motivators and status claims**
14. "you are ahead of 99.999999% of people with this stuff" (Level 3: Powering Hermes)
15. "It's the fastest path to, oh, my goodness, it freaking works." (Level 2: Setup Hermes)
16. "I want you to learn the process of how to fish, how to connect anything." (Level 3: Powering Hermes)
17. "this is the stuff that really separates the pros from the Joe's" (Level 7: Security & Compliance)

**Transitions and closers**
18. "This takes us very nicely on to the soul.md" (Level 1: Foundations)
19. "So grab that coffee, relax, and I'll catch you inside chapter two." (Level 1: Foundations)
20. "grab that beautiful coffee and I will catch you inside the next chapter" (Level 4: Hermes Memory)

---

## 5. Named Systems, Frameworks, and Conventions

### Named frameworks and mental models

| Name | Level | What it is |
|---|---|---|
| **Agent vs Chatbot** | L1 | Vending machine vs chief of staff. The founding distinction of the whole section. |
| **Model vs Harness** | L1, L3 | Engine vs car. "The harness is everything around the model." The reason Hermes matters. |
| **The Anatomy of Hermes (four layers and a loop)** | L1 | Gateway, Brain, Body, Memory + observe/write/review/improve. |
| **The four-step learning loop** | L1 | Observe, write to memory, review and learn, improve. |
| **One brain for every interface** | L1, L6 | Same memory whether you are in Telegram, WhatsApp, voice, terminal, dashboard. |
| **Context engineering** | L1 | Jack's claimed differentiator: one universal knowledge base across Claude, Hermes, anti-gravity. |
| **Race car vs cargo ship** | L1 | Claude Code (fast, precise, desktop, session-bound) vs Hermes (never stops, on the go, long-term). |
| **Own the agent, rent the brain** | L3 | You own the harness, you swap the model per task. Stated as the core philosophy of L3. |
| **The Routing Decision Tree** | L3 | "Big brain to plan, cheap brain to execute." A dispatcher at a switchboard. |
| **The Five Frontier-Model Areas** | L3 | Bring the top model in only for: taste, architecture, strategy, review, codification. |
| **One key for every model** | L3 | Master key ring = OpenRouter. |
| **The Effort Dial** | L3 | Minimal / low / medium / high, set per model in the OS. |
| **The 100% Private AI Lab** | L3 | Ollama + local model + Hermes, no internet required. "A workshop with the door shut." |
| **Three Tiers of Memory** | L4 | Working memory, session, long-term archive. |
| **Whiteboard vs Filing Cabinet** | L4 | Chatbot context vs Hermes memory. |
| **The Hotel Front Desk** | L4 | Every stay goes in the ledger; at night the day is distilled into the book. |
| **The Self-Improving Wiki / Karpathy Method** | L4 | Self-referential, self-cross-linking Obsidian wiki that finds contradictions. |
| **Recency, Importance, Relevance** | L4 | The three-signal scoring rule for pruning memories. Explicitly called "a classic stamp for the [retrieval] and generative agents." |
| **Memory Poisoning / Hostile Import** | L4 | A forged note slipped into your files "not to be read now but to be trusted or acted on later." |
| **The Command Deck** | L5 | The slash-command layer. |
| **Completion Contracts** | L5 | `/goal` + verify + constraints + boundaries + judge loop. Building inspector analogy. |
| **Judge in the loop** | L5 | Worker model does the work, a separate judge model rules done or continue after every turn. Default budget: 20 turns. |
| **The Curator** | L5 | 7-day background cycle: grade, consolidate, cut dead weight. Zero token cost, fully deterministic. |
| **Proactivity's Three Wires** | L5 | Home channel + schedule + goals. "Proactivity itself is not a magic toggle. It's three wires." |
| **One Brain and a Team of Hands / The Fan Out** | L5 | Parallelized sub-agents. Recommended concurrency: 3. |
| **The Operator and the Contractor** | L5 | Hermes runs your world all day; Claude Code is the specialist you hire for a job. |
| **Locked by Design / Principle of Least Access** | L7 | Hospital lobby vs surgical theater. |
| **The Four Permission Tiers** | L7 | See table below. |
| **Prompts Are Not Permissions** | L7 | The one rule of the chapter. "The decision lives in code, not the prompt." |
| **The Always-Gate List** | L7 | Deploy, comms, money, delete, permissions. Enforced by a hook that runs before the tool does. Bank teller and time-locked vault. |
| **Propose-Then-Confirm** | L7 | Tier 3+ produces a plan, not an act. 30-minute approval window, then dropped and logged. Never auto-approved. |
| **The Verify Rule** | L7 | "Act, then verify, then continue." Any state change must be followed by a step proving it happened. |
| **Three Kill Switches** | L7 | Stop the gateway service; revoke the model API key; pull the box off the Tailscale ring. |
| **Three Office Rules** | L7 | Agent announces itself on calls; client data only in per-client stores; produce where data lives on request. |
| **Three Numbers Every Morning** | L7 | A 6am governance brief: yesterday's spend, spend by model, single most expensive run. |
| **The Locksmith** | L8 | You did not invent the lock, you learned to fit it. Every door in town still needs one. |
| **The AI Back Office** | L8 | The retainer offer. Watermill: you charge for the stream, not for turning the wheel. |
| **The Engineer's Parable** | L8 | "Tapping $1, knowing where $9,999." Sell the know-how, not the time. |
| **Stickier Billing** | L8 | "The less frequent the billing cycle, the stickier the individual is." Push annual. |
| **Build Once, Sell Many** | L8 | Perfect the dish in one kitchen, then the cookbook cooks a thousand times. GoHighLevel white-label reseller math cited as proof. |
| **The Bottleneck / Theory of Constraints** | L8 | Find the single biggest limiting factor, not ten small ones. |
| **The Priority-Ranking Exercise** | L8 | Write every priority down, rank by three-month impact, cross off everything from 2 down, do only #1. |
| **The Fleet Model** | L8 | Multiple client Hermes instances on your own VPS, recurring income from each. |

### Numbered systems

- **Four layers** of the Hermes anatomy (L1)
- **Four steps** in the learning loop (L1)
- **Three ways to run Hermes**: local, Docker, VPS (L2)
- **Five frontier-model areas**: taste, architecture, strategy, review, codification (L3)
- **Three tiers of memory** (L4)
- **Three signals** for memory pruning: recency, importance, relevance (L4)
- **Three commands** in the core Command Deck: `/steer`, `/queue`, `/stop` (L5)
- **Three parameters** on a Completion Contract: verify, constraints, boundaries (L5)
- **20-turn budget** on a goal loop (L5)
- **7-day cycle** for the Curator (L5)
- **Concurrency of 3** for sub-agents (L5)
- **Five ways to access Hermes** (L6): terminal, dashboard chat, desktop app chat, Kanban, OS console
- **Four permission tiers** (L7)
- **Five always-gate categories** (L7)
- **Three kill switches** (L7)
- **Three office rules** (L7)
- **Three numbers** in the governance brief (L7)
- **20-minute lockdown checklist** (L7)
- **Two ways** Hermes increases income (L8)
- **~10%** of first-year value as the pricing rule (L8)

**The Four Permission Tiers (Level 7), in full:**

| Tier | Contents | Policy |
|---|---|---|
| 1. Read-only | Looking, searching, summarizing, reading files, checking calendars, browsing docs | Allow automatically. Worst case you waste tokens. |
| 2. Reversible | Drafts, editing version-controlled GitHub repos | Allow and log. "Everything's an undo." |
| 3. External | Sending, posting, spending, emails, payments, deploys, anything another human sees | Must ask first. "Undo does not exist in the real world." |
| 4. Irreversible | Deleting, dropping, force pushing, production credentials | Deny, or require human execution. |

Homework as stated: "Take 10 minutes, list what your agent can currently touch and stamp each item tier 1 to four. Anything in tier three to four that isn't [gated] is your homework."

### File and folder conventions

- **`soul.md`** (L1, L6): personality, preferences, business context, voice. "The DNA of the Hermes agent." Filled out from a Notion template, optionally by pasting the template into Claude and saying "based on our entire conversation, fill out as much of this as you can."
- **`memory.md`** (L4): the agent's own notes. ~2,200 characters. Injected every session.
- **`user.md`** (L4): who you are. ~1,400 characters. Injected every session.
- **SQLite session store** (L4): full-text search over every message ever sent.
- **Private GitHub repo** (L2, L6): daily identical copy of the whole agent. The versioning and rollback layer.
- **Obsidian vault** (L4, L6): "they call the folders vault." Sub-structure shown live: `raw` (source articles), `assets` (images), `concepts` (linked notes), plus an index and a `claude.md` skimmer that tells the LLM how to maintain it. Graph view enabled for visualization.
- **One portable brain folder** (L6): "one folder that manages everything for [Hermes] agent, that has your memory, [skills], your [context] session," which is why the GitHub backup matters. Move it VPS to metal or metal to metal without loss.
- **Glider Skills folder** (L6): where voice-invokable skills are written, then imported into Glider via its import button.
- **`.gitignore` and `.dockerignore`** (L7): secret management. Any key that ever touched git history must be rotated.
- **Artifacts / documents pane** (L6): everything Hermes builds gets saved to the OS so it is "not kind of lost to time."

### Slash commands (the full inventory across L3, L4, L5)

`/steer` (redirect a running task without killing it), `/queue` or `/q` (stack sequential follow-ups), `/stop` (kill all background processes), `/model` (dropdown model switch), `/restart` (gracefully restart the gateway, required after adding connections or changing models), `/learn` (turn a conversation or a repo into a reusable skill), `/goal` (set a completion contract) plus `/goal status`, `pause`, `resume`, `clear`, `/MOA` (Ministry of Agents from Telegram), `/blueprint` (schedule tasks in plain English instead of cron syntax), `/suggestions` (agent proposes its own automations), `/journey` (playable timeline of memories and skills), `/undo` and rollback to auto-snapshot, `/compress`, `/handoff`.

### Rules of thumb

- "Nothing from the open web or your inbox writes to memory unguarded." (L4, called "the one rule, the so what of the section")
- "You do not need a $50 model to run a loop of well-specified edits." (L3)
- "Don't assume that it knows what not to do." Explicit don'ts must be spoken. (L5)
- "The pro move is to point the judge at a cheap model. The worker thinks expensive, the referee costs pennies." (L5)
- "If stopping your agent takes more than 60 seconds, you don't have a kill switch. You have a hope, a prayer, a dream." (L7)
- "The AI did it is not a defense that regulators accept." (L7)
- "You're going to charge for the operating burden you remove, not the minutes that you log." (L8)
- "Hourly is the very first step. In fact, the first step is free." (L8)

### Level 6 in detail: the Hermes Operating System

This is the longest-described lesson and the one with the most concrete deliverables. Full breakdown:

**Why it exists.** "You need a location that is model agnostic, that can bring your entire world, your entire AI world, your entire systems, for all the different apps using into one location. You're not dependent on Hermes, you're not dependent on open claw, or claw or anti-gravity." Framed as the missing layer that makes everything else compose.

**How you get it.** It is a **downloadable zip from the Skool classroom, not a GitHub repo**, and Jack says so explicitly in the Claude-section lesson: "the reason why this is a file, rather than a GitHub repo, is because it is 100% exclusive to this community." You download it, upload the zip into Claude Code, and say "hey there, I just downloaded this operating system, I would like you to open it up and follow the instructions." A `claude.md` inside the zip carries the configuration instructions. It runs on localhost. Updates are handled by re-downloading and asking Claude "could you check for any new updates, explain what those updates are."

**The setup wizard, step by step as demoed:**
1. Name and profile photo. ("It really personalizes it. And if you're given this to... clients... I think it's great, they get to see something visual.")
2. **Auto-detection of installed AI tooling.** In the demo it finds OpenAI Codex, Hermes Agent, the Anthropic API, anti-gravity, Claude, and terminal activity. "It means it can automatically [route] everything."
3. **External knowledge connections**: Pinecone (vector DB), Obsidian (auto-detected vault paths), Notion.
4. **API keys for live cost tracking.**
5. **Your time value.** You enter what an hour of your time is worth. The OS then computes dollar savings per skill. Jack's example: automating YouTube descriptions and timestamps that used to take an hour a week.
6. **Dream configuration.** When it dreams (morning or evening), whether web search is allowed during the dream, whether to generate a fresh cosmos hero image.
7. **Which engine runs the dream**: Codex or Hermes.
8. Activate. Confetti. Dashboard opens.

**The dashboard sections, in order:**
- Monthly AI spend
- Skill savings (dollars saved)
- Last month's activity, plans and usage limits per model
- **Dream insights** with skip / apply / mark done / cycle, plus source attribution. The dream analyzes: conversational analysis, cost intelligence, skill performance, memory health, session hygiene, external opportunities, workflow patterns, and business outcomes. In the Claude-section demo it surfaced a real finding: "Claude Max 20 is sitting at 10% weekly utilization... 5X covers you for half the price," saving $100/month.
- **Mission Control**: mid-term goal setting. You give it a goal, it breaks it into 4 to 10 tasks and **splits them between Hermes and you**. "One will be Hermes, create an outline, then it says, Jack, you're going to record, and when you record your five videos, let me know."
- Skills browser
- Memory overview (with the Obsidian topic browser: click a topic like "YouTube," see everything linked to it, click "hooks," see every note referencing hooks)
- **Project Knowledge Graph** (Graphify). Drop a GitHub repo URL in, it maps the relationships, shows estimated token savings per session (480,000 tokens cited), and lets you chat with the codebase from the dashboard.
- **Hermes Agent panel**: all connections, agent version, active model with live update, context window, memory, usage counts, in-dashboard chat, stats, goals.
- **Pantheon**: add a persona with name, title, description, system prompt, and assigned model. Named examples in the material: the Oracle (deep research, GPT 5.6 Sol), Athena, Mercury, the Alchemist, the Scribe.
- **Ministry of Experts**: assign models to roles, with a performance comparison view showing each model's agent performance, speed, and cost.
- **Max tokens per call** setting. Jack's reasoning: cost, plus "you don't always need it... It's like me saying, ask a politician a question."
- **GitHub connect prompt** and **push personas to GitHub prompt**. Both are copy-paste blocks you drop into Hermes.
- **Claude OS Bridge**: the copy-paste prompt that lets Hermes read the dashboard, dreams, and Claude chat logs. "What did my dream say? What's my Claude [quota]?"
- Obsidian connection prompt
- Saved skills and artifacts
- **AI model leaderboard** plus **cost routing Playbooks** ("cheap parallel models, processing portions... copy to JSON").

**Glider voice layer.** Glider (Jack's own speech-to-text startup, promo code in the README) has a beta "tools" mode. Enable beta features in settings, then point Hermes at Glider's docs and say "go ahead and learn this... come back and suggest for me three skills that might be helpful." Hermes writes an MCP server into a Glider Skills folder; you import it in Glider. Demonstrated live: highlight any text on any webpage, speak a command, and Hermes summarizes a YouTube video into three bullets, sets a 30-minute cron reminder, or ingests an article into the Obsidian vault. "Hermes is now one button click away anywhere I am."

**Five ways to access Hermes:** terminal, dashboard chat, desktop app chat, Kanban board, OS console.

**Portability:** one folder holds memory, skills, sessions. Backed by GitHub. Move between VPS and local metal freely.

**Tailscale.** Install on every device, sign in, each gets a stable private 100.x address and a MagicDNS name "that survives sleep, [reboots], networks." WireGuard mesh: every device connects directly to every other, encrypted end to end, the coordination server "only introduces them, your traffic never touches them." No open ports, NAT punch-through outbound, firewall stays shut to the public. Demoed live by asking Hermes on one machine to report the last file saved to the desktop of a second MacBook Pro (answer: "B-roll retention handover"). Requires Remote Login enabled on the target machine. The README carries a **six-step Tailscale bridging prompt** (check the ring, build the bridge, find my OS, prove it, remember it, make it useful) with hard standing rules: read-only unless explicitly asked, never modify or delete, rsync specific folders only, never a public IP, never copy `.env` files or credentials.

---

## 6. How the Claude Section and the Hermes Section Interlock

The two tracks are **parallel curricula that share three overlapping assets**, and the intended path is stated explicitly in the material.

**The two crossover lessons in the Claude section:**

1. **[`01-Claude/05-Level-5-Hermes-Agent/`](01-Claude/05-Level-5-Hermes-Agent/)** (30m 37s, launched 17 May 2026). This is a **condensed, complete Hermes build inside the Claude course**. Its timestamps cover: why Hermes, Hermes vs Claude Code, local install, Docker, Docker images vs containers, initial setup, model choice, Telegram, **installing the Agentic OS**, the OS dashboard, Pantheon personas, GitHub backup, soul.md, Obsidian memory, NotebookLM integration, creating a Scribe skill. That is a compressed version of Hermes Levels 2, 3, 4, and 6, plus one thing the Hermes section does not cover: **NotebookLM integration via browser cookie session**.

2. **[`01-Claude/11-Claude-Code-Hermes-OS/`](01-Claude/11-Claude-Code-Hermes-OS/)** (9m 39s, no written description). This is the **installer and dashboard tour for the Agentic OS itself**. It is the source of truth for the OS zip. It is where the Hermes section repeatedly sends students: Level 2 says the OS "will be available in the [Claude] masterclass just above this one." Level 4 says "you're going to open up the [Claude] code and the Hermes agentic operating system and I've got a full tutorial guide explaining it in the [Claude] code section above." Level 6 says "come over to the classroom, head over to chapter two, and I want you to come down here to the [Claude] section, and then you're going to have the [Claude] Code and Hermes operating system. So this is always going to have the latest, greatest OS."

**The intended order, as stated in the material:**

- **Level 0 gives the branching instruction directly.** Because the Hermes section was released two chapters per week and was not fully live when Level 0 was recorded: "You're going to come over to chapter two... And you can come down and do level five Hermes agent inside the [Claude] course. This is a great first step whilst the first two chapters come out... But if you scroll down, you can see another one here, which says Hermes [Agentic], or basically Hermes full course right here on the left hand side. **If that exists, I want you to get started and begin in level one.**"
- So: **if the full Hermes section exists, start at Hermes Level 1 and ignore Claude Level 5.** Claude Level 5 was the placeholder.
- **Level 8 gives the closing instruction:** "the next thing to do if you have not already is to complete the [Claude] code masterclass."

**Net order for a student today:** Hermes Levels 0 through 8, detouring into [`01-Claude/11-Claude-Code-Hermes-OS/`](01-Claude/11-Claude-Code-Hermes-OS/) to download and install the OS at the point Level 6 calls for it, then the full Claude Code course afterward.

**The three shared assets that make them one system:**
1. **The Agentic Operating System.** Lives in the Claude section, is the dashboard for the Hermes section. It is not Hermes software; it is Jack's own community-exclusive layer that sits above both.
2. **The Claude OS Bridge.** A copy-paste prompt inside the OS that lets Hermes read the Claude Code chat logs stored on the desktop, and lets Claude read Hermes memory. Level 4: "we break the divide and we [were] the first people ever to do this... so that we have a full universal memory system." Demoed live: Hermes reporting on what Jack had been discussing in Claude that day.
3. **The Obsidian LLM wiki.** Built by Claude Code (Level 4 gives the Claude Code prompt to create it), read by both.

**The division of labor, stated four separate times in four different metaphors:**

| Level | Metaphor | Claude Code | Hermes |
|---|---|---|---|
| L1 | Race car vs cargo ship | Fast, precise laps. Deep in a codebase, in-the-loop session, you at the desk. | Never stops moving. Always-on, reachable from your phone, remembers you, runs on schedule. |
| L1 | Plain statement | "Building your apps" | "Personal [assistant] and system" |
| L5 | Operator vs contractor | The specialist you hire for a job, who keeps the receipts. | The operator who runs your world all day. |
| L5 | Desktop vs phone | "Should I search the web on my desktop" | "or should I search the web on my phone" |

Jack is explicit that the overlap is real and mostly irrelevant: "Technically speaking, anything you do in one, you could potentially do on the other... it's not the [model] because the same model you're using in Claude Code is in Hermes. It's just a case of where is the coding happening as the harness." He also notes Claude Code can be spawned as a Hermes sub-agent.

---

## 7. Transferable to Real Estate: 12 Concrete Moves

Each of these is a structure lifted directly from the Hermes section and remapped for The Leveraged Agent.

**1. Replace "topics" with a numbered Level ladder that gates on a working artifact.**
Jack's L0 through L8 works because each level ends with something that exists, and the next level is useless without it. A real estate version: Level 0 Start Here, Level 1 Foundations (agent vs chatbot, what an AI assistant can actually do in a real estate business), Level 2 Setup (Claude installed, working), Level 3 Connect (MLS export, Gmail, Google Calendar, CRM), Level 4 Memory (your farm areas, your voice, your listings, your past clients), Level 5 Power Features (skills, scheduling, contracts), Level 6 The Agent Dashboard, Level 7 Compliance (fair housing, MLS rules, license law, client data), Level 8 Make Money. The gating is the point. An agent who has not done Level 3 cannot do Level 4.

**2. Steal the four-layer anatomy diagram wholesale.**
Gateway / Brain / Body / Memory is the single most useful teaching object in the section because every later lesson hangs off it. A realtor version: **inbox and phone** (where the agent hears from you), **the model**, **your tools** (MLS, CRM, Canva, email, calendar, Docusign), **what it knows about your business** (farm, price points, past clients, your voice). Draw it once in Level 1 and refer back in every subsequent lesson.

**3. Build a `soul.md` equivalent and make filling it out the Level 1 homework.**
Jack's soul.md is one markdown file holding voice, preferences, business context. A realtor version: brokerage, license state, farm areas, price bands, typical client, tone rules (no em-dashes, 6th-grade reading level, soft CTAs), contact block, signature conventions. Give a template. Give the shortcut he gives: paste it into Claude and say "fill out as much of this as you can based on everything you know about me." Making this the very first deliverable is what makes every later output sound like the agent instead of like ChatGPT.

**4. Put the backup and rollback lesson BEFORE the connections lesson.**
This is Jack's smartest ordering decision and almost nobody does it. Level 2 sets up a private daily GitHub backup before Level 3 connects Gmail and Calendar. The realtor equivalent: before an agent connects anything to their CRM or MLS, teach them how to snapshot their skills folder and roll it back. "I like the version I had six weeks ago, bring it back" is a safety net that removes the fear that makes agents stop experimenting.

**5. Delegate setup tedium to the AI on camera.**
Jack does not click through Docker. He copies the whole setup doc into Claude and says "configure anything that needs to be configured... and let me know if there's any other information that I need to know." Do the same with MLS exports, Lofty CMS quirks, Canva template wiring. The lesson is not "here are 14 steps," it is "here is the one prompt that makes the AI walk you through the 14 steps." This scales across brokerages, CRMs, and MLS systems you cannot possibly cover individually.

**6. Teach the meta-move explicitly: "I want you to learn the process of how to fish."**
Level 3's whole connector segment is framed as teaching a repeatable connection procedure rather than one connector. For agents: teach one canonical "connect a new tool" prompt that works for Follow Up Boss, kvCORE, Lofty, Sierra, whatever. Say out loud why you are doing it this way.

**7. Adopt the routing decision tree, priced in agent terms.**
"Big brain to plan, cheap brain to execute." Reserve the expensive model for the five areas Jack names (taste, architecture, strategy, review, codification), which map cleanly to: listing strategy, CMA pricing narrative, negotiation approach, reviewing anything a client will read. Cheap model for: reformatting listing data, batch social captions, transcribing, renaming files. His line lands with a commission-earner audience: "you wouldn't have the CEO answering the phone calls."

**8. Ship Completion Contracts as the way agents delegate anything risky.**
`/goal` with **verify, constraints, boundaries** is a complete delegation framework and it translates perfectly. Example: goal = draft the weekly seller update for 123 Main. Verify = includes showing count, feedback summary, and current DOM, ends with a recommended next step. Constraints = do not send it, do not quote a price change, do not contact the client. Boundaries = read this listing folder only. Teach agents that "telling it the negative is just as important" and that a judge step is what stops an AI from declaring itself done.

**9. Build the two-file memory structure, not a mega-prompt.**
`memory.md` + `user.md`, both small, both injected every session, with everything else searchable. The realtor version is a small business-facts file plus a small about-you file, plus a searchable archive of past listings, past CMAs, and past client threads. Teach Jack's rule against committing everything: "we as humans don't remember everything we only remember the important things." Then teach the pruning triad: recency, importance, relevance. Real estate data goes stale fast, so this rule is more urgent for agents than it was for Jack.

**10. Keep the analogy-first, prompt-verbatim, failure-included demo pattern.**
Three specific mechanics: (a) every technical concept gets a physical analogy before any explanation, (b) every demo reads the actual prompt out loud, word for word, so it can be transcribed, (c) broken steps stay in the video. Agents are a non-technical audience with high anxiety about looking stupid. Watching things break and get fixed on camera is what converts.

**11. Run the Level 7 compliance chapter, but built on real estate's own nightmare files.**
Jack's four permission tiers plus "prompts are not permissions" plus three kill switches is a transferable skeleton. Populate it with real estate specifics: fair housing language in AI-written descriptions, MLS rules on data reuse, license law on advertising and disclosure, client PII in a CRM, state-level AI disclosure. Use his device of real incidents rather than abstract rules. His framing that this "separates the pros from the Joe's" is exactly the right posture for an audience that would otherwise skip a compliance module. His copy-paste homework hack works verbatim: select the whole lesson, paste it into Claude, ask for a personal action plan.

**12. Close with a Level 8 that is business, not build, and split it two ways.**
Jack's L8 is the shortest lesson and it does two jobs: make yourself more efficient, and sell this to others. Real estate splits the same way: (a) use the agent to remove your own bottleneck so you list more, (b) sell it. Directly transferable pieces: the **bottleneck exercise** (write every priority down, rank by three-month impact, cross off everything from 2 down, do only #1), the **engineer's parable** on charging for know-how not time, **niching down** ("who doesn't get remembered? The generalists"), and **build once sell many**. For a Skool community teaching agents, the honest version of the fleet model is teaching top producers to install and run this for their own teams and for referral partners.

**Two more structural notes worth stealing:**

- **The coffee ritual.** A fixed physical state-change instruction at the top of every video and a fixed handoff at the bottom. It is cheap, it is memorable, and after three lessons it is a brand. Pick one and never vary it.
- **The next-lesson question, not the next-lesson topic.** Jack never ends with "next up, memory." He ends with "how do we give it a memory that never forgets?" Open loops are what get an onboarding sequence finished.

---

## Things Not in the Material

- No Level 0 through 8 assessment, quiz, or completion checkpoint of any kind. Progression is honor system.
- No written companion doc per level beyond the README description and timestamps. Slides exist as HTML attachments for Levels 1, 2, 3, 5, 6, 7 but not 0, 4, or 8.
- Level 4 and Level 8 have **no slide attachment**, only a transcript.
- Level 3's slides are a `.zip`, not an `.html`.
- The Hermes repo URL is never stated in any transcript or README. Only `hermes-masterclass.vercel.app` (Jack's own curriculum site) and the Graphify repo appear.
- No pricing is given for Hermes itself. Hermes Cloud is mentioned as "20 bucks a month, 30 bucks, 10 bucks, loads of different levels" but not detailed.
- The model names throughout (Fable 5, GPT 5.6 Sol, Opus 4.8, DeepSeek V4 Pro/Flash, GLM 5.2, Grok 4.5, Qwen 3.30B, Kimi K3, MiniMax M3) are reported as they appear in the transcripts, unverified.
- Level 0's timestamps reference a "Hermes Exclusive Masterclass" lesson ID identical to Claude Level 5's, confirming they are the same video.
