# Cerebras Killed Notion, Obsidian, and Your "Second Brain"

- **id:** eCx3SSCcISo · **url:** https://youtube.com/watch?v=eCx3SSCcISo
- **tier:** T2-PACKAGING
- **published:** 2026-07-19 · **views:** 90,387 · **views/day:** 6026 · **runtime:** 23.8 min

## Hook (0:00–0:20)
> "So this is really interesting. This company Sarah [sic?] just built a knowledge base that I think is not total And that's hard for me to say because up until now, virtually every instance of knowledge bases or second brains or whatever have just been total hot air."

**Mechanism:** Contrarian plus grudging-admission. He attacks a category the viewer is emotionally invested in ("second brains"), then signals reluctance ("that's hard for me to say"), which reads as honesty rather than hype. The title layers a threat frame on top by naming products people already pay for. Note: the transcript garbles Cerebras throughout as "Sarah", "Cabris", "Cerebrus", and "Cerus" [sic?].

## Thesis
A second brain that actually works is an automatic ingestion pipeline with metadata-weighted retrieval, not a visualization, and the credible blueprint comes from a real engineering team rather than a productivity influencer.

## Beats
| ts | beat | what he's doing |
|---|---|---|
| 0:00 | contrarian hook | kill the category, then exempt one example to create the curiosity gap |
| 0:42 | list the sources | make the scale concrete: Slack, wiki, Confluence, GitHub, custom databases |
| 1:20 | promise the build | convert commentary into a tutorial so viewers stay past the explainer |
| 1:53 | RAG primer | pre-empt "I don't understand this" before it costs him retention |
| 2:26 | "how tall is Nick" | toy example plus a self-deprecating joke to carry a dry concept |
| 6:06 | credit the authors | borrow authority, and drop "15,000 questions every day" as scale proof |
| 10:06 | embedding as metadata | reframe a technical term as a camera's EXIF data |
| 11:49 | recency weighting | isolate the one detail that separates this from "naive rag" |
| 15:09 | the build starts | show the whole method is pasting a blog post into a coding agent |
| 17:37 | the fake question | ask the agent how it would set up email access "hypothetically" to compress the demo |
| 19:58 | the proof artifact | 17 of 20 with the knowledge base versus 0 of 20 without |
| 20:32 | live queries | prove it on his own business data, sponsorship pitches and GitHub pushes |
| 22:16 | disclaim the sponsorship | "this is not a sponsored post" to protect the recommendation's credibility |
| 23:22 | CTA | Maker School with a 90-day refund guarantee |

## System demoed
Copy the Cerebras [sic?] engineering blog post into a coding agent (he uses "Claude Code V2.1.211") and prompt it: build ingestion pipelines for Slack, three Gmail addresses, GitHub, and a YouTube channel for his company. The agent handles auth where accounts are already logged in, and for anything new it walks the OAuth setup (Google Cloud project, enable the Gmail API, consent screen, desktop OAuth client, one-time consent, refresh token), which he claims is "about 5 to 10 minutes for every pipeline." Each source's threads pass a distillation step through a small model ("ha coup" [sic?], likely Haiku) that produces a structured artifact of question, summary, resolution, systems, source ID, and timestamps. Those artifacts land in a single table in what he reads as "postgrql" [sic?]. Retrieval runs two ways in parallel, full text for exact token matching plus embeddings, and is queried via MCP, a web UI, or agents. He uses a second Claude Code thread with `/btw` to have the agent draw the architecture in ASCII while the main thread builds.

## Who it's for
Operators of small to mid-sized teams who have institutional knowledge scattered across Slack, email, and repos, and who have already tried and been disappointed by Obsidian or Notion second brains. He explicitly positions himself as small: "I've already built one of these for my own business and it's quite useful already and that's just as a small team."

## Economic argument
He never prices the build. The value case is entirely accuracy and scale. On Cerebras: "currently they're being asked something like 15,000 questions every day." On his own benchmark: "the same model asked the same 20 questions, one with the knowledge base and one without. You can see that the one that had the knowledge base answered 17 out of 20 questions correctly. Um the other three were just honest partials or declines... Whereas without the knowledge base, I answered zero." On setup effort: "This would realistically take you about 5 to 10 minutes for every pipeline of information that you want to set up." On corpus size: "I only had 640ish documents inside of my system. A company like Cerebrus [sic?] probably has, you know, hundreds of thousands." And the credibility argument in place of an ROI number: "These guys aren't screwing around. They're not going to do something like this if it doesn't actually generate a return on their time and energy." No dollar figures stated.

## CTA
- **What:** Maker School, framed as a 90-day roadmap to a first paying customer selling exactly this kind of build, or your money back. One earlier mention of his 4-hour Claude Code course.
- **Where:** 15:43 (course), 23:22 (Maker School)
- **How hard:** soft mention

## Title + thumbnail pattern
"<Credible tech company> Killed <beloved tool 1>, <tool 2>, and Your '<identity noun>'" → obituary framing. It borrows a serious company's name for authority, names two products the viewer actively pays for, and finishes with a possessive that makes it personal rather than industry news.

## Transferable to realtors?
- **Verdict:** ADAPTABLE
- **Why:** The mechanism is a real fit. A realtor's institutional memory is scattered across Gmail threads, transaction files, CRM notes, and past listing packages, and the same distill-then-retrieve pipeline would answer "what did we agree to with the lender on 123 Elm" or "which title rep handled the Summerlin new-build." The rebuild is not trivial: the connectors change (Gmail, the CRM, transaction management, Drive rather than Slack and GitHub), and client PII plus MLS data-use rules mean the auth-and-audit layer he skips as "I'm going to assume anybody in my business is probably okay" is the layer a realtor cannot skip.
