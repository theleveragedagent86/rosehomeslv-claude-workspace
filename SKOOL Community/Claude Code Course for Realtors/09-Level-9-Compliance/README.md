# Level 9: Compliance

**Course:** Claude Code Course for Realtors
**Target runtime:** 18-22 min (shortest core level, on purpose)
**Artifact after this level:** permission tiers set, `compliance.md` in the Brain, setup locked down
**Enemy named on camera:** running client data through tools you have never once thought about

---

## Skool description (paste-ready)

📆 Launch date: [DATE]

![four-permission-tiers](images/level-9-tiers.png)

**The four permission tiers:**

```
TIER 1  READ ONLY      Reading, searching, summarizing.
                       Allow. Worst case you waste tokens.

TIER 2  REVERSIBLE     Drafts, edits to files you can undo.
                       Allow and log.

TIER 3  EXTERNAL       Sending, posting, anything a client or
                       the public sees. ASK FIRST. Always.

TIER 4  IRREVERSIBLE   Deleting, anything touching a signed
                       document or a live MLS entry.
                       You do it yourself. Not the AI.
```

⏱️ Timestamps
00:00 – Welcome & Yes, This One
00:50 – What You've Actually Built an Exposure To
02:10 – Fair Housing in AI-Written Copy
04:40 – The Words It Will Reach For If You Let It
06:20 – MLS Data Rules and What You Can Reuse
08:15 – Advertising, Attribution and License Law
10:00 – Client PII: What Should Never Be in a Prompt
12:15 – The Four Permission Tiers
14:30 – Prompts Are Not Permissions
15:45 – Red Teaming Your Own Setup
17:50 – The Brokerage Conversation
19:15 – The 20-Minute Lockdown Checklist
20:30 – Recap & Homework

#### Hey, in this video, you're gonna learn:

⚖️ **Keep Fair Housing Violations Out of AI-Written Copy** by learning the specific words and framings it reaches for when unconstrained, so you catch them before they reach the MLS.

📊 **Understand What MLS Data You Can Actually Reuse** including where the line sits on scraping, republishing and attribution, so your landing pages do not become a board complaint.

📢 **Get Advertising and Attribution Right** covering brokerage identification, license display and disclosure on AI-assisted content, so your marketing holds up to scrutiny in your state.

🔒 **Keep Client PII Out of Your Prompts** by knowing what never gets pasted and what to do with a document that contains it, so you are not handing over a social security number to solve a formatting problem.

🎚️ **Apply the Four Permission Tiers to Everything You Built** from read-only through irreversible, so the AI's reach is a decision you made rather than a default you inherited.

🚫 **Understand That Prompts Are Not Permissions** because telling it not to do something is a request, not a control, so the guardrails live in your setup and not in your instructions.

🕵️ **Red Team Your Own Setup** using a prompt that hunts for the thing you would be embarrassed about, so you find it instead of a client finding it.

🗣️ **Have the Brokerage Conversation Before It Happens** by knowing what your broker will ask and having the answer ready, so you are not explaining this for the first time after something goes wrong.

#### In this video, Ryan covers:

Eight levels in, there is a folder on your computer holding client names, transaction documents, disclosure PDFs and contact information, connected to an AI with access to your email and your calendar. That is genuinely useful and it is also an exposure nobody walked you through, because the courses that teach the fun parts tend to stop before this one.

The system is **the Four Permission Tiers** plus one rule: **prompts are not permissions**. Read-only work runs freely. Reversible work runs and gets logged. Anything a client or the public sees asks first, every time. Anything irreversible you do yourself. Telling the AI to be careful is a request. The tier is the control.

The practical steps are auditing AI-written copy for fair housing language, understanding MLS reuse and attribution limits, checking your advertising and disclosure obligations, removing PII from your prompt habits, assigning a tier to every capability you built in Levels 1 through 8, running the red team prompt against your own setup, and working the 20-minute lockdown checklist.

#### Who this is for:

- **Every agent who completed Levels 1 through 8** because the exposure exists whether or not this level gets watched.

- **Team leads and brokers** who need a defensible answer for how AI is being used on client data before somebody asks them for one.

## Linked resources

| Resource | Link |
|---|---|
| ⚖️ Fair housing advertising guidance | NOT FOUND, add before publish |
| 📊 Local MLS rules and regulations | NOT FOUND, add before publish |
| 🏛️ State license law, advertising section | NOT FOUND, add before publish |

## Downloaded attachments

| Resource | File |
|---|---|
| 🕵️ Red Team Prompt | `red-team-prompt.md` |
| ✅ 20-Minute Lockdown Checklist | `lockdown-checklist.md` |
| ⚖️ compliance.md Template | `compliance-template.md` |
| transcript | `Level 9.txt` |

---

## Production notes (not for Skool)

**Acknowledge it out loud in the first ten seconds, then compress hard.** Shortest core level in the course. Beat every minute for twenty minutes.

> "Compliance. Everybody's favorite. Here's the deal: this is nineteen minutes, it's the shortest level in the course, and it's the one that lets you keep doing all the other ones. Let's go."

**Posture is pro versus amateur, not fear.** Do not scare them out of using the system they just built.

> "This is the stuff that separates the agents doing this professionally from the ones who are gonna get a phone call."

**Fair housing gets the most time because it is the highest-frequency real risk.** Show it happening: prompt for a listing description without constraints and let it produce something that describes the buyer instead of the property. Then show the KEEP OUT block from Level 1 stopping it.

**Be explicit about jurisdiction, once, and do not hedge everything afterward:**

> "I'm licensed in Nevada. Your state is different, your MLS is different, and your brokerage has its own policy on top of both. I'm giving you the framework and the questions. Take the answers to your broker."

**PII: give the concrete never-paste list.** Social security numbers, dates of birth, full account numbers, driver's license numbers, wire instructions. Then the alternative: redact first, or point it at the file rather than pasting the contents.

**Prompts are not permissions is the line of the level.** Say it twice.

> "You can tell it 'don't send anything without asking me' and it will mostly listen. Mostly. The tier is what makes it true."

**Run the red team on Ryan's own setup, live, and leave the finding in.** If it finds something real and slightly embarrassing, that is the best moment in the level. Do not re-record it clean.

**The brokerage conversation.** Give them the three questions a broker will ask and a good answer to each. This turns compliance from a burden into a thing they can lead with.

**Homework, and make it uncomfortable on purpose:**

> "Take ten minutes today and list everything your setup can currently touch. Stamp each one tier one through four. Anything in tier three or four that isn't gated, that's your homework, and you already know which one it is."

**Close on Level 10:**

> "That's the medicine. Last one is the fun one, and there's no software in it at all. Level 10 is what all of this was actually for."
