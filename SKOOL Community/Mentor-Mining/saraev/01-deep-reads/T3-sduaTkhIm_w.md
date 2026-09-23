# CLAUDE SKILLS FULL COURSE: Automate Your Work (2026)

- **id:** sduaTkhIm_w · **url:** https://youtube.com/watch?v=sduaTkhIm_w
- **tier:** T3-TEACHING
- **published:** 2026-03-02 · **views:** 144,948 · **views/day:** 941 · **runtime:** 47.7 min

## Hook (0:00–0:20)
> "Hey, welcome to the definitive resource all about skills. I currently run a business that does over $4 million a year in profit and I manage it primarily through AI agents and skills and I teach over 2,000 people how to do the same thing. I think a lot of demos and walkthroughs of skills right now are like really flashy and they're typically centered around the personal assistant angle, but a lot of people are leaving tons of money on the table because they're not applying them to specific business use cases that actually tend to produce large returns on investment."

**Mechanism:** Proof-first plus contrarian. The $4M number buys authority in one sentence, then he immediately dismisses the entire existing genre of skills content as toys, which reframes his 47 minutes as the only serious version.

## Thesis
A skill is nothing more than a standard operating procedure translated into agent-readable markdown, so if you already have an SOP you already have a skill, and the only ones worth building are the front-end revenue ones.

## Beats
| ts | beat | what he's doing |
|---|---|---|
| 0:00 | hook | revenue proof, then dismisses competing content as "glorified personal assistants" |
| 1:03 | show, don't tell | opens five live skills in anti-gravity [sic?] before teaching anything |
| 1:37 | skill 1 | follow-up nurture, reads the CRM pipeline and drafts stage-aware check-ins |
| 2:44 | quality argument | insists the copy be informal "so they think it's us", jabs at other automated follow-up tools |
| 3:47 | skill 2 | one-shot thumbnail generator, face-swap onto a viral reference image |
| 5:22 | mid-roll ask | interrupts himself for a subscribe plea, "something like 69% of you guys aren't subscribed" |
| 5:51 | skill 3 | LinkedIn Sales Navigator lead scraper into a Google Sheet |
| 7:40 | skill 4 | cold email campaign writer that clones his high performers for a new client |
| 9:51 | skill 5 | website builder that ships to Netlify, framed as free-value outreach |
| 10:25 | new concept | "knowledge arbitrage", you have the tool, the prospect does not |
| 11:31 | humanize | WeWork auto-booking and Amazon shopping skills, deliberately unserious |
| 15:19 | pivot to teaching | "skills are basically the evolution of standard operating procedures just for agents" |
| 15:59 | analogy | the PB and J sandwich checklist as an SOP for a new hire |
| 16:48 | de-scare markdown | explains headers and backticks, then says you will never write one yourself |
| 18:41 | de-risk the choice | notes OpenAI and Gemini adopted near-identical skill formats |
| 19:22 | the rule | "if you guys have a standard operating procedure, if you have an SOP, you have a skill" |
| 20:41 | the selling point | skills are "self-healing over time", they patch themselves on failure |
| 21:18 | the free asset | grab `skillspec.md`, "you don't need to sign up or give me your email" |
| 21:54 | how he made it | compressed Anthropic's docs page from 500 lines to 150 to 200 |
| 23:06 | build live | voice-transcribes an inbox cleanup SOP into Claude Code via Whisper Flow |
| 25:42 | dissect the output | walks the generated skill.md field by field, name, description, allowed tools |
| 27:35 | human in the loop | refuses the bulk action, asks to review all 97 emails first |
| 30:03 | teach front matter | explains progressive disclosure, ~500 tokens down to ~60 or 70 |
| 32:44 | name the mechanic | "skill matching", the agent scans front matter descriptions to pick a skill |
| 33:59 | build three at once | parallel Claude Code panes: meeting notes, invoice extractor, content repurposer |
| 37:34 | show self-healing | the invoice script hits a subtotal bug and rewrites its own filtering logic |
| 38:44 | honest caveat | the generated tweet thread is "pretty LLM-y", not award-winning |
| 39:19 | file structure | walks `.claude/skills/<name>/skill.md`, complains it is needlessly nested and hidden |
| 42:40 | the real lesson | "what skills are actually worth making" |
| 43:19 | contrarian close | most demos build backend fulfillment pipelines, "most people that do these sorts of things still don't make any money" |
| 44:36 | prescription | build front-end skills, sales and marketing, and actually use them |
| 45:11 | credibility from grind | "50 to 100 cold calls every single day", "80 knocks on physical doors per day" |
| 45:50 | anti-list | names what NOT to build: skills that build skills, AGI design frameworks |
| 46:27 | CTA | second, longer subscribe ask, plus comment for future topics |

## System demoed
Two things. First, a tour of production skills: `follow-up-nurture` (walks a CRM pipeline, pulls every prior email chain, writes stage-appropriate informal check-ins in-thread), a thumbnail generator (face-swap onto a reference image, multiple variants), a LinkedIn Sales Navigator scraper (natural language request to filtered search URLs to a Google Sheet of names and emails), a cold email campaign writer (clones high-performing existing campaigns for a new client's offer, sets them up in the sending platform), a website builder that deploys to Netlify, plus browser-automation one-offs (WeWork booking, Amazon product research) built on Chrome DevTools MCP. Second, the build method: download his condensed `skillspec.md`, make it your `CLAUDE.md` so every workspace knows the format, open a Claude Code window, voice-describe the SOP, let it write `.claude/skills/<name>/skill.md` plus any Python scripts, run it once to test and amend, and it self-patches on future failures. He then builds three more live in parallel: meeting-notes-to-action-items (prompt only, no code), an invoice PDF to structured JSON extractor (markdown plus Python), and a content repurposer (transcript to tweet thread, LinkedIn post, and newsletter via parallel Sonnet sub-agents).

## Who it's for
A business owner or side-hustler already doing sales and marketing work by hand, someone with existing SOPs and a CRM, explicitly not the hobbyist building personal assistant demos. He says the audience is "probably going to have some sort of side hustle going on or they're going to be looking to get into that realm."

## Economic argument
Authority figure up front, time savings in the middle, no per-skill ROI math. Verbatim: "I currently run a business that does over $4 million a year in profit and I manage it primarily through AI agents and skills and I teach over 2,000 people how to do the same thing." On the cold email skill: "a step that previously might have taken me 30 to 60 minutes just logistically is now taken care of... So, yeah, I mean, this takes something that might be 3 or 4 hours into something that takes minutes." On the website builder: "nowadays, you can generate these deliverables for basically cents on the dollar and then get like high-quality animations and stuff like that um with literally you just putting one prompt." On token cost via front matter: "we could be adding 373 words, which is approximately 500 tokens into context, okay? But with front matter... we store a much smaller summary, which is closer to like 60 or 70 tokens." On what earns money: "The difference between people that use new, upcoming, and trend-breaking technology to make money and actually have big, you know, success outcomes versus people that play shiny object syndrome all day... the former group focuses primarily on the front end of their business." Other figures: he runs "probably close to 30 or 40" skills, a $2,500 quote appears in a sample follow-up, the inbox skill triaged 97 emails of which 79 came from a broken make scenario, and his own grind numbers are "50 to 100 cold calls every single day" and "80 knocks on physical doors per day."

## CTA
- **What:** Subscribe (the primary ask, made twice with an unusually naked emotional appeal), grab the free skills and `skillspec.md` from the Google Drive link with no email gate, comment with future topic requests. He references his full 4-hour Claude Code course and a Gemini course but does not pitch or price them.
- **Where:** 5:22, 21:18, 42:40, 46:27, 47:00
- **How hard:** soft on the products, unusually hard on the subscribe. He explicitly says "most of my videos bomb" without subscribers.

## Title + thumbnail pattern
"<TOOL NAME> FULL COURSE: <Outcome Verb> Your <Thing> (<year>)" → free-course framing plus recency stamp. Capitalized "FULL COURSE" signals length is the value, and the year makes it re-shootable annually.

## Transferable to realtors?
- **Verdict:** DIRECT
- **Why:** This is the closest match in the batch to what Ryan teaches. The follow-up nurture skill is a realtor's daily job with the CRM name swapped, Lofty instead of his sheet, and stages swapped to new lead, showing, offer out, under contract. Inbox triage, meeting-notes-to-action-items, and content repurposing all work unmodified. Most importantly, "if you have an SOP, you have a skill" plus his front-end-only rule is exactly the right filter for realtors, who tend to want to automate transaction paperwork when the money is in follow-up and listing marketing. The only piece that does not carry is the LinkedIn Sales Navigator scraper, which is B2B lead data with no consumer real estate equivalent.
