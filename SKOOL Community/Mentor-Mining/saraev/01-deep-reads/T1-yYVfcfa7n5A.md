# I Built An AI Asset-Based Lead Gen System (Free Template)

- **id:** yYVfcfa7n5A · **url:** https://youtube.com/watch?v=yYVfcfa7n5A
- **tier:** T1-SYSTEM
- **published:** 2025-04-18 · **views:** 32,867 · **views/day:** 70 · **runtime:** 40.5 min

## Hook (0:00–0:20)
> "Today I'm going to be building an assetbased AI lead generation system. Essentially, we're going to be scraping customer data and then generating a custom lead magnet or asset for them using artificial intelligence and some pretty smart prompting before finally adding them to an email campaign and running this on autopilot."

**Mechanism:** Proof-first, with the number landing seconds later ("reply rates of over 5, 10, or even 15%"). He names the whole pipeline in one breath so the viewer can see the shape of the payoff before committing 40 minutes.

## Thesis
Cold email's bar has risen past personalization tokens, so the only way through the noise now is to spend AI compute manufacturing a genuinely valuable custom asset for every single prospect before you ever ask for anything.

## Beats
| ts | beat | what he's doing |
|---|---|---|
| 0:00 | hook | names the full pipeline plus the reply-rate claim |
| 0:36 | walkthrough of the finished build | shows the whole scenario before teaching it, demo-first |
| 1:14 | credential drop | "a format that I've used before for my own newsletter that had the founder of HubSpot follow me" |
| 1:48 | honest downside | admits the Google Doc "doesn't look beautifully formatted", pre-empts the obvious criticism |
| 2:24 | show the email | reads the actual outreach copy, then reframes it as "how high quality people are doing cold outreach today" |
| 2:56 | social proof | "over 2,400 people collectively across my two communities" experimenting with this |
| 2:56 | why now | argues the bar for cold email is rising and AI only recently got good enough to write real assets |
| 3:59 | build-live framing | "I haven't built the system yet... I want to show you guys what a real build process looks like" |
| 4:58 | data sourcing | Apollo people search, filters on job title and location, 2,149 records |
| 6:06 | scraper setup | Apify actor `code_crafter/apollo-io-scraper`, capped at 500 for the test |
| 7:19 | inspect the raw data | dumps the CSV into Google Sheets and reasons out loud about which fields matter |
| 10:08 | teach a technique | hardcodes a dataset ID to avoid re-running, calls it "iterative testing" |
| 11:14 | pre-empt breakage | adds a filter for missing website or missing email |
| 12:27 | parse step | HTML to text so the model can read it |
| 13:38 | two-model split | one OpenAI call to extract structured context, a second to write the newsletter |
| 15:57 | the real trick | pastes his own past newsletter in as a style example so the model mirrors his voice |
| 22:04 | delivery detail | names the Doc "for <FirstName>" because the title shows in the Gmail attachment preview |
| 23:24 | show the output | reads the generated newsletter aloud as proof of quality |
| 27:57 | debug live | wrong module, wrong send type, fixes it on camera |
| 29:12 | scope honestly | says Docs API formatting is "a little unnecessarily technical for this video" |
| 29:50 | campaign build | writes the Instantly sequence, explicitly "We're not even making an ask on here" |
| 33:00 | API plumbing | Instantly V2 API, bearer token, JSON body, mapping personalization variables |
| 35:48 | debug live again | stray quote breaks the JSON, fixes it in a JSON formatter |
| 38:00 | recap | replays the narrated overview verbatim to reinforce the architecture |
| 40:02 | CTA | Maker School, "just under 2,000 members", price rises every hundred |

## System demoed
A make.com scenario (transcribed at 4:29 as "new.com" [sic?]). Chain: (1) Apify [sic? transcribed as "Appify"/"Ampify"] Run an Actor node running `code_crafter/apollo-io-scraper` against a saved Apollo.io people-search URL; (2) Get Dataset Items; (3) a filter requiring both a website and an email; (4) HTTP GET the prospect's website; (5) Text Parser HTML-to-text; (6) OpenAI call one, GPT-4.1, extracts a JSON object of three fields, `website context`, `person context`, `unique angles`, with a rule to write at least two paragraphs of website context; (7) OpenAI call two writes a full newsletter in markdown ATX, returning JSON with title, subheading, and letter body, using one of his own real past newsletters pasted in as the voice template; (8) Markdown to HTML; (9) Google Docs create-document named "for <FirstName> custom newsletter"; (10) HTTP POST to the Instantly V2 API `add lead` endpoint with a bearer token, mapping email, first name, company name, and the Doc web view link into a `custom variable` object. The email itself makes no ask, the CTA is only "if you want more, just say the word."

## Who it's for
An AI automation operator doing cold outbound who is already sending email and watching reply rates fall, plus the Maker School beginner who wants a sellable system. His own target audience in the demo is founders and co-founders at creative agencies.

## Economic argument
He anchors on reply rate, not dollars. Verbatim: "The same approach is being used by myself and many other people in the AI and automation industry to generate reply rates of over 5, 10, or even 15%." On throughput: "we can realistically go through a,000 leads a day, creating a,000 custom assets, um, significantly improving the probability that somebody gets back to us." [sic? "a,000" appears to be a garbled "1,000"] On why it works: "This is how high quality people are doing cold outreach today. Because the bar has gone up so much, you got to deliver value. You got to do it up front. And usually, you got to do it without some sort of super crazy hard ask." Other figures: the Apify actor "allows you to scrape up to 50,000 leads per search URL", he tested with 500 records, Apollo returned 2,149, he claims "over 2,400 people collectively across my two communities", and Maker School is "just under 2,000 members right now... and I increase the price every hundred". **No cost figures, no cost-per-lead, no cost-per-asset, and no revenue figures are stated anywhere.**

## CTA
- **What:** Free template in the description; comment with future video ideas; join Maker School (zero-to-one automation community, price increases every 100 members); or makemoneywithmake.com, the premier community that bundles Maker School.
- **Where:** 39:30, 40:02
- **How hard:** soft mention until the very end, then a stacked two-tier close with a price-increase urgency lever.

## Title + thumbnail pattern
"I Built An AI <category> System (Free Template)" → builder-credibility plus zero-risk parenthetical. The "(Free Template)" carries the click, the "I Built" claims it is real rather than theoretical.

## Transferable to realtors?
- **Verdict:** ADAPTABLE
- **Why:** The core mechanism, generate a genuinely useful custom asset per prospect and lead with it instead of an ask, is the single strongest idea in this batch for realtors. A Rose Homes version would swap Apollo and Apify for MLS expireds, FSBOs, or absentee-owner records, and swap the newsletter for a per-property mini-CMA or neighborhood market snapshot. The rebuild is not optional though: consumer cold email hits CAN-SPAM and state DNC rules that B2B prospecting does not, and any auto-generated valuation must be factual and fair-housing safe, so the AI step needs real data plumbed in rather than a website scrape.
