# Level 7: Security & Compliance

**Section:** 🥇 Hermes Agent  
**Course:** Claude Code Course (AI Automations by Jack)  
**Lesson URL:** https://www.skool.com/aiautomationsbyjack/classroom/af686ad3?md=8445a7f7154f4a00b7a04ab761de7a83  
**Video length:** 20m 34s  
**Lesson ID:** `8445a7f7154f4a00b7a04ab761de7a83`

---

## Description (as posted by Jack)

📆 Launch Date: Sunday 26th July

![image.png](images/fc6e441d47ba4ce0846cfe72.png)

⏱️ Timestamps  
00:00 – Welcome & Security/Compliance Overview  
00:38 – Locked-by-Design & Principle of Least Access  
01:29 – Case Study: Replit Agent Deleted a Production Database  
02:35 – The Four Tiers of Agent Permissions  
03:59 – "Prompts Are Not Permissions" — The Key Rule  
04:49 – The Always-Gate List (5 Categories Needing Human Approval)  
05:21 – Case Study: Malicious VS Code Extension Prompt Injection  
05:56 – Approval Gates & Kill Switches  
06:30 – Case Study: Gemini CLI Destroyed a User's Files  
07:16 – Propose-Then-Confirm Action Plans & Approval Windows  
07:50 – Hermes' New Second-Model Auto-Approval Feature  
08:27 – The Verify Rule: Act, Then Verify  
08:58 – Setting Up Your Three Kill Switches Today  
09:23 – Spend & Loop Protection Against Runaway Costs  
09:57 – Case Study: The $72,000 Google Cloud Run Loop  
10:45 – Setting Spending Caps in OpenRouter & Anthropic Console  
12:25 – Secret & API Key Management Best Practices  
13:04 – Case Study: Leaked AWS Keys Exploited in Minutes  
13:52 – Rotating Keys & Cleaning Up Unused Repos  
14:18 – Observability & Cost Governance Tools  
14:42 – Case Studies: Runaway Claude & LangChain Token Burns  
15:16 – Helicone & Langfuse for Logging Agent Activity  
15:59 – Building a Daily 6am Cost Governance Brief  
16:50 – Privacy & the Law: When Agents Touch Client Data  
17:22 – Case Study: Samsung's ChatGPT Leak & OpenAI's Italy Fine  
18:13 – GDPR Right to Erasure & Structured Data Storage  
18:54 – EU AI Act Transparency Requirements  
19:24 – What a Regulated Client Will Ask You For  
20:00 – Three Office Rules & the Full Lockdown Checklist  
20:25 – Wrap-Up & Next Topic: Monetization

#### Hey, in this video, you're gonna learn:

🔒 Apply the "principle of least access" and "locked by design" concepts to restrict what your Hermes agent can do

🚦 Classify agent actions into 4 permission tiers (read-only, reversible, external, irreversible) to decide what needs human approval

🛑 Set up approval gates, 30-minute timeout windows, and 3 kill switches (stop gateway service, revoke API key, pull the device off Tailscale) to halt a runaway agent

✅ Use the "verify rule" (act then verify then continue) to catch destructive or hallucinated agent actions before they cause damage

💸 Prevent runaway spend using OpenRouter key limits, Anthropic console budget caps, and prepaid/no-auto-recharge cards vs. usage-based billing

🔑 Manage secrets properly with .gitignore and .dockerignore, and rotate any API key that ever touched git history

📊 Set up observability tools like Helicone and Langfuse for full request tracing, cost logging, and spend alerts (75%/90% thresholds)

⚖️ Understand compliance requirements from GDPR "right to erasure," the EU AI Act transparency rule (Aug 2, 2026), and real fines like OpenAI's €15M Italy penalty

#### In this video, Jack covers:

This video addresses the security and compliance risks that emerge when AI agents (like Hermes agent) are given real access to production systems, money, and client data.

The framework taught is a 4-tier permission system (read-only, reversible, external, irreversible) combined with an "always gate" list (deploys, payments, deletions, permission changes) that forces human approval regardless of model confidence.

Practical implementation steps include: auditing what your agent currently has access to and tagging each capability by tier, building approval gates with timeout windows instead of relying on prompt instructions alone, setting hard spending caps via OpenRouter/Anthropic console and prepaid cards rather than notification-only budget limits, rotating any secrets exposed to git history, and instrumenting agents with observability tools (Helicone, Langfuse) to track token spend, latency, and errors in real time.

Real incident case studies are used throughout, including Replit deleting a production database despite explicit instructions not to, a supply-chain attack on a VS Code extension, a Google Cloud Run test that generated a $72,000 bill, and Samsung's data leak into ChatGPT that triggered a €15M GDPR fine against OpenAI.

#### Who this is for:

- AI agency owners, automation builders, and developers deploying autonomous AI agents (e.g., Hermes agent, Claude Code) into production or client-facing systems who need practical guardrails around permissions, spend, and data compliance.

## Linked resources

| Resource | Link |
|---|---|
| 📈 Hermes Curriculum | https://hermes-masterclass.vercel.app/ |

## Downloaded attachments

| Resource | File | Size | Path |
|---|---|---|---|
| ⭐️ Slides | `Chapter 7 - Security & Compliance.html` | 4329 KB | `attachments/Chapter 7 - Security & Compliance.html` |
| transcript | `Level 7.txt` | 30 KB | `attachments/Level 7.txt` |

## Transcript

Full word-for-word transcript: [transcript.md](transcript.md)
