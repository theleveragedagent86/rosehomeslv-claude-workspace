# I Deep-Personalized 1000+ Cold Emails Using THIS AI System (FREE TEMPLATE)

- **id:** oAWe5wFwHlo · **url:** https://youtube.com/watch?v=oAWe5wFwHlo
- **tier:** T1-SYSTEM
- **published:** 2025-05-05 · **views:** 112,551 · **views/day:** 247 · **runtime:** 30.4 min

## Hook (0:00–0:20)
> "Today I'm going to be building out a multi-line icebreaker generator in NADN that makes use of deep website scraping in order to personalize the first few lines of a highquality cold email."

**Mechanism:** Demo-first, stated as a build order with no throat-clearing. It holds because the promise is falsifiable and concrete, the viewer knows within one sentence exactly what artifact will exist at the end. [NADN is n8n, sic?]

## Thesis
Cold email replies come from depth of research, not volume, so scraping every page of a prospect's site and summarizing each one produces an opener that reads like a human spent an hour on it.

## Beats
| ts | beat | what he's doing |
|---|---|---|
| 0:00 | hook | names the exact artifact, no preamble |
| 0:34 | output-first demo | shows the filled spreadsheet before any build, proof before process |
| 1:42 | proof drop | attaches a reply-rate number and the $72,000/month credential |
| 2:16 | live campaign proof | opens the actual Instantly campaign, second-order evidence |
| 2:51 | pre-empt objection | "it's a little bit more complicated than just scraping a bunch of leads off Apollo and then sending" |
| 3:23 | build begins | switches to real-time construction, no cuts |
| 6:44 | shows the attrition | 96 in, 28 out, sets honest expectations instead of hiding losses |
| 8:21 | normalize failure | 21 scrape successes, 7 errors, "not all websites scrapes work" |
| 12:10 | teaches the hard part | walks the loop node slowly because it is where beginners quit |
| 17:42 | cost control | HTML to markdown to cut token spend, signals operator credibility |
| 20:16 | the payoff | aggregate the abstracts, second AI node writes the icebreaker |
| 24:28 | prompt craft | the anti-detection rules, shorten company names, avoid obvious praise |
| 28:18 | expansion loop | "it's just a nugget, it's a stem", lists eight upgrades he did not build |
| 29:45 | CTA | free template plus Maker School with a money-back guarantee |

## System demoed
An n8n [NADN sic?] flow. Manual trigger, then Google Sheets "get rows" pulling Apollo search URLs from a tab. HTTP POST to the Apify `run-sync-get-dataset-items` endpoint (accept application/json header, authorization bearer token) to scrape the Apollo list. Filter node keeps only records with both an email and a website URL. HTTP request node hits each homepage with follow-redirects (max 21) and "continue using error output" set. HTML extract node pulls every `a` tag `href` into a `links` array. Edit Fields node trims the record down to first name, last name, website, headline, location, phone. Loop Over Items, then Split Out on `links`, filter to strings starting with `/`, remove duplicates, then concatenate the base website URL with each relative link and HTTP-request each page. HTML to Markdown node to cut tokens, then a slice capping content at 5,000 characters. OpenAI GPT-4.1 node with a system prompt ("you're a helpful intelligent website scraping assistant") and a user prompt asking for a two-paragraph JSON abstract per page. Aggregate node collects all abstracts per lead, feeds a second OpenAI node that writes the multi-line icebreaker against a fill-in-the-blank template plus rules, then Google Sheets "append row" writes the lead plus icebreaker back. Output feeds an Instantly cold email sequence.

## Who it's for
Someone already sending cold email for an AI automation agency and getting weak replies. He assumes prior familiarity with Apollo, Instantly, and n8n basics, and links a separate API video for anyone who is not there yet.

## Economic argument
The justification is reply rate, not cost. Verbatim: "this is the sort of thing that routinely gets me 5 to 10% reply rates on my cold email campaigns. And it's one of the ways that I scaled my own AI and automation agency to $72,000 per month." On the live campaign: "this specific pitch has already got me a 4% reply rate and something like over 30 qualified leads that have wanted to book calls or meetings with me." On lead economics he argues waste is acceptable because supply is unlimited: "if I could do this for 20 out of 100 leads fed in, well, in Apollo, I'm just going to make sure that my audience size is really big, like 10,000. Therefore, I'm going to get about 2,000 of those." And: "To me, the leads are never the bottleneck here, just because we have platforms like Apollo and Appify and stuff that let us get an almost infinite number of them." He states no dollar cost for the OpenAI, Apify, or Instantly spend, and no revenue figure for the system itself. Token math is the only cost discussion: "This is 18,000 characters to tokens. One token is around four characters."

## CTA
- **What:** Download the free n8n template from the description, then join Maker School
- **Where:** [29:45] free template, [29:45]-[30:17] Maker School with "If you don't get your first customer within 90 days, I give you all your money back"
- **How hard:** mid-roll pitch, softened by the risk reversal and placed only at the end

## Title + thumbnail pattern
"I <verb>ed <big round number>+ <artifact> Using THIS AI System (FREE TEMPLATE)" → volume-as-proof, plus a demonstrative "THIS" that withholds the name to force the click, plus a parenthetical free-asset bribe that raises CTR without changing the promise.

## Transferable to realtors?
- **Verdict:** ADAPTABLE
- **Why:** The mechanism, scrape every page of a target's public web presence, summarize each with AI, then synthesize a personalized opener, works for a realtor doing agent-to-agent, lender, builder, property manager, or investor outreach, where the targets have websites and B2B email is legal. It does not port to consumer prospecting: Apollo has no consumer-side equivalent, and cold-emailing homeowners at this volume collides with CAN-SPAM and state solicitation rules, so the data source and channel both need rebuilding.
