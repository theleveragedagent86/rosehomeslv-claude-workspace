# CLAUDE CODE FULL COURSE 4 HOURS: Build & Sell (2026)

- **id:** QoQBzR1NIqI · **url:** https://youtube.com/watch?v=QoQBzR1NIqI
- **tier:** T3-TEACHING
- **published:** 2026-02-12 · **views:** 2,222,860 · **views/day:** 12,924 · **runtime:** 250.7 min

## Hook (0:00–0:20)
> "Hey, this is the definitive course on Cloud Code [sic?] for beginners. I use Cloud Code every day to manage a business that does over $4 million a year in profit. I also teach over 2,000 people how to use Cloud Code both for personal and then corporate or professional tasks."

**Mechanism:** Proof-first, with a category-claim wrapper. "The definitive course" claims the whole category in six words, then the $4M profit number and the 2,000 students immediately buy the right to say it. No curiosity gap, no threat. It holds because a 4-hour viewer needs to decide in 10 seconds that this teacher is worth 4 hours, and a revenue figure settles that faster than any promise.

## Thesis
Claude Code is not a coding tool, it is a general knowledge-work engine, and the skill that matters is not programming but structuring context (CLAUDE.md, plan mode, skills, sub agents) so the model can verify its own work.

## Beats
| ts | beat | what he's doing |
|---|---|---|
| 0:00 | hook | proof-first credential drop, $4M profit and 2,000 students |
| 0:33 | full curriculum read-out | open 15 loops at once so every viewer finds their reason to stay |
| 2:45 | price anchor | names the $17 Pro plan as the only cost, pre-empts "is this expensive" |
| 3:21 | ROI claim | anchors $10 to $15k/mo of value against $17 to make price irrelevant |
| 4:29 | install and IDE tour | de-risk the scariest step for non-technical viewers, do it live |
| 24:00 | first build | demo-first payoff, promises award-winning sites in under 10 min |
| 25:20 | ship-steering analogy | reframes CLAUDE.md as trajectory, not config, so it feels high stakes |
| 30:22 | three design methods | taxonomy move, makes his own preferred method (screenshot loop) look chosen |
| 36:06 | DevTools full-page screenshot hack | drops a "not a lot of people realize this" secret to reward staying |
| 39:37 | task, do, verify loop | states the single governing principle of the course, the real lesson |
| 54:34 | .claude directory tour | "less than 10% of users understand this", insider framing |
| 70:05 | CLAUDE.md do/don't guide | compresses the module into a checklist, gives a screenshot-able artifact |
| 77:33 | sub agents intro | teaches context isolation as the reason agents exist, not "more robots" |
| 91:12 | permission modes | pre-empts the safety objection, then admits he uses bypass anyway |
| 100:17 | plan mode math | 35 min without plan vs 15 min with, the course's core economic proof |
| 104:32 | full-stack app build | the big demo, builds a PandaDoc [sic?] competitor live |
| 113:41 | salmon marinade cutaway | lifestyle proof, "I cook while it builds", sells the leverage not the tool |
| 130:46 | security warning | credibility-buying disclaimer, "obligatory safety message" |
| 133:41 | context management module | teaches /context, shows him paying for 45k tokens before typing |
| 153:37 | skills module | names skills as "the most economically valuable" use, ranks the features |
| 157:03 | 1,000 leads in 87 sec | hard time-savings proof against his own prior manual process |
| 163:56 | "this is why I no longer hire" | the emotional peak, $300k+/mo profit with no staff |
| 181:56 | MCP to skill conversion | teaches a decision rule (prototype with MCP, ship as skill) |
| 191:05 | sub agent parallelization | 100 emails to 1,000 emails, shows scale where parallelism pays |
| 206:12 | agent teams debunk | contrarian turn, "this is more of the same", positions against hype videos |
| 228:33 | OpenClaw [sic?] repo audit | spends ~$80 of tokens live to dramatize the money-for-time trade |
| 236:02 | git work trees | last technical module, isolation as insurance against agent collisions |
| 242:35 | modal deployment | closes the loop from local build to public URL, skill becomes an endpoint |
| 249:58 | Maker School pitch | single hard close at the very end, guarantee-backed |

## System demoed
Several, each a separate module:

- **Setup and IDE** [4:29, 12:23, 21:54]. Terminal install via curl, then Claude Code as a VS Code extension, then Antigravity [sic?] (Google's VS Code fork) as the course's working environment.
- **Screenshot-loop website builder** [24:00 to 53:32]. Inputs: a reference site from godly.website [sic?], a full-page screenshot captured via Chrome DevTools "capture full size screenshot", copied CSS from the body tag, and a CLAUDE.md whose rule is "when the user provides a reference image, screenshot, and optionally some CSS classes or style notes, you should generate a website". Claude builds, screenshots its own output, diffs, and iterates to ~99%. Output: a deployable index.html. He runs two instances in parallel.
- **.claude directory architecture** [54:34 to 74:50]. settings.json, settings.local.json, CLAUDE.md, CLAUDE.local.md, /agents, /skills, /rules, .mcp.json, plus the global ~/.claude layer and an enterprise layer. Includes splitting one CLAUDE.md into rules files, and /init to auto-generate a repo summary.
- **Plan mode full-stack app** [104:32 to 133:41]. A PandaDoc-style [sic?] proposal generator. Inputs: a voice-transcript dump of requirements, a PDF proposal template, Supabase [sic?] keys, Stripe sandbox keys, an Anthropic API key. Steps: plan mode interrogates him with a generated question UI, produces a spec doc, he switches to bypass permissions, it builds front end, auth, database, e-signature and Stripe checkout, he tests page by page, then deploys to Netlify [sic?]. Output: a live public app with login, AI proposal generation, public share URLs, signature and payment.
- **scrape-leads skill** [153:37 to 158:35]. A skill folder with SKILL.md as the checklist plus a /scripts folder of Python. Steps: test scrape 25, verify, full parallel scrape (4 workers x 250), LLM classification, upload to Google Sheets, enrich emails. Output: 1,000 US dentist leads in 87 seconds, destined for his cold email tool "instantly".
- **Skill authoring live** [164:28 to 170:53]. Builds a prospect-website-generator skill from a screenshot plus pasted HTML plus a sample Google Sheet row. Output: a custom mockup site per lead in ~30 seconds.
- **MCP demos** [170:53 to 187:47]. Chrome DevTools MCP driving a browser and shopping Amazon.ca; a ClickUp MCP creating tasks; a Gmail MCP labeling an inbox. Then the key move: he converts the Gmail MCP workflow into a token-cheap skill calling the Gmail API directly.
- **Sub agents** [191:05 to 206:12]. Turns the Gmail-label skill into 10 parallel classifier sub agents on Sonnet 4.5. Then builds three standing sub agents: code-reviewer, researcher, QA, and writes the ship workflow (edit, review, QA, ship) into CLAUDE.md.
- **Agent teams** [206:12 to 236:02]. Enabled via a settings.json env flag. Demo one: three parallel agents building three personal-site designs, then three research agents, then four iteration agents. Demo two: 10 scanner agents on the OpenClaw [sic?] codebase, four security documenters, and two adversarial "devil" agents that debate findings to consensus, producing 15 flaws and 15 fixer agents.
- **Git work trees** [236:02 to 242:35]. Three isolated worktree folders (about, contact, services) so parallel agents cannot collide on the same files, then merge.
- **Modal deployment** [242:35 to 249:24]. Wraps the scrape-leads skill in a public URL with a form front end that returns a CSV, using modal for the endpoint.

## Who it's for
A non-technical operator, explicitly not a developer, who already runs or wants to run a service business and wants to stop hiring contractors for repeatable knowledge work. He says the focus "is not software per se, so you don't need to have a technical background", and repeatedly frames tasks as things he "would have just given to somebody and delegated away". The end-of-video CTA reveals the true target: someone who wants to sell app development or workflow building as a service and does not yet have a first customer.

## Economic argument
He argues the tool is nearly free relative to output, then proves it with time-collapse numbers and one deliberate cost horror story.

- [3:21] "despite the fact that it's $17, I personally would not even raise an eyebrow. It's no small stretch to say that Cloud Code probably delivers me productivity benefits on the order of $10 to $15,000 a month"
- [102:07] on planning: "not only have you spent the 15 minutes to build the thing, not only have you spent the 5 minutes to test the thing, you also have to rebuild the thing, which can take 15 minutes... That means that the total amount of time it takes you is 35 minutes plus a fair number of tokens" versus the plan path at "5 minutes plus 5 minutes 10 minutes and then maybe your actual build time... is only 5 minutes or 15"
- [130:15] on the app he just built: "it's probably better for my purposes than Panda [sic?] was which I was paying out the ass for... In my case I'm doing all that now basically for free."
- [158:35] "this takes a pre-existing process that would have taken me at least half an hour, probably more, and it turns into one that I literally did in 87 seconds"
- [163:56] "This is why I no longer hire. I mean, you know, my businesses collectively still make over 300 something thousand per month right now in profit... I don't have staff members to do these things for me anymore."
- [187:47] "The end result was it was 36 seconds to fetch, classify, and label 100 emails."
- [198:27] "I'm now at 173 bucks in additional usage on top of my cloud code usage"
- [234:57] "I've spent close to probably 80 or so dollars directly on this one query. And that's what I mean by trading money for time. I mean, like obviously if I had a team of developers doing this... it also would have taken them presumably several weeks"
- [234:57] the closing frame on agent teams: "They're almost like a nuclear weapon, just one aimed directly at your wallet."

## CTA
- **What:** Join Maker School, his 90-day accountability program, guaranteed first customer or full refund.
- **Where:** [153:37] soft mention of a separate agentic-workflows course. [249:58] to [250:31] the actual pitch.
- **How hard:** Hard close, but deferred to the final 40 seconds of a 250-minute video, and explicitly labeled: "That's my last and only pitch of this video." The restraint is the selling technique.

## Title + thumbnail pattern
"<TOOL> FULL COURSE <N> HOURS: <Build> & <Sell> (<YEAR>)" → runtime-as-value-proof plus year-stamp for freshness plus a two-verb outcome pair that promises both the skill and the money. Steal the shape: the hour count signals completeness so viewers stop shopping for other tutorials, and "& Sell" converts a tutorial into a business promise.

## Transferable to realtors?
- **Verdict:** ADAPTABLE
- **Why:** The flagship builds are agency-specific (proposal SaaS, cold-email lead scraper, Upwork applier) and would need full rebuilds against MLS, CRM and compliance realities. But the architecture underneath is exactly what a realtor AI curriculum needs: CLAUDE.md as brand-voice steering, /init, plan mode before any complex build, skills as SOP-to-checklist conversion, the task-do-verify screenshot loop for listing marketing, and research/reviewer sub agents. The beat table above is also the single most reusable asset here, it is a working module spine for a "Leveraged Agent" course, with the caveat that his security warning at [130:46] about not publishing vibe-coded apps that handle client data applies double to anyone touching buyer and seller PII.
