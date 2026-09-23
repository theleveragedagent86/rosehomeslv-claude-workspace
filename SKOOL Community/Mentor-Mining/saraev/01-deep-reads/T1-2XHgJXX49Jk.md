# How to get SO many leads you don't know what to do with them

- **id:** 2XHgJXX49Jk · **url:** https://youtube.com/watch?v=2XHgJXX49Jk
- **tier:** T1-SYSTEM
- **published:** 2025-11-10 · **views:** 52,337 · **views/day:** 197 · **runtime:** 32.6 min

## Hook (0:00–0:20)
> "Hey, this is an exhaustive and updated list of every way that I currently know of to scrape and generate leads for services. I use these every day over at Left Click to generate hundreds of thousands of dollars across a variety of industries for clients using outbound. So, this is the sauce. There is no sauce like it."

**Mechanism:** Completeness plus proof-first. "Exhaustive" and "every way I currently know of" promise the viewer will not need another video, and the revenue claim is attached to daily use rather than a one-off result. "There is no sauce like it" is a deliberate swagger line that makes the completeness claim memorable.

## Thesis
Lead data is not the bottleneck in outbound, because any list you want can be assembled cheaply from a scraper plus an email enrichment tool, so the only real constraint is whether you send.

## Beats
| ts | beat | what he's doing |
|---|---|---|
| 0:00 | hook | completeness claim, revenue proof, free-doc promise |
| 0:31 | first principles | teaches the two underlying mechanics before any tool, so the list survives tool churn |
| 1:06 | nominative enrichment | explains why guessing email patterns works, demystifies the whole category |
| 2:55 | method 1 live | Air Scape [sic?] to domains to An Email Finder, full screen-share |
| 5:38 | method 2 | Sales Navigator to Vain [sic?] to enrichment |
| 9:20 | arbitrage reveal | the "little-known" 1 credit to 40 emails hack, the video's real payload |
| 11:32 | honest kill | admits the Apollo method is broken now, credibility through subtraction |
| 13:51 | method 5 | Apify Google SERP scraper, cheap-volume play |
| 16:18 | local pivot | Google Maps scraper, lower enrichment but geo-targeted |
| 18:35 | automated version | n8n flow that scrapes sites and has GPT-5 extract contacts |
| 21:26 | buy vs scrape | Bright Data marketplace, reports his own worse results honestly |
| 23:41 | social scraping | Instagram, then generalizes to TikTok and X |
| 26:10 | intent play | LinkedIn Jobs as buying-signal data, the highest-quality idea in the video |
| 29:39 | custom scrape | Skool listings scraped by hand, ends on his own 11.5% reply rate |
| 32:23 | CTA | free Google Doc for an email address |

## System demoed
Not one system, a catalog of roughly ten lead-sourcing routes that all terminate in the same enrichment step. Routes: Air Scape [sic?] company search to domains; LinkedIn Sales Navigator to Vain [sic?]; An Email Finder company-search credit arbitrage; Apollo exported via Leads Rapidly or Ample Leads (declared mostly dead); Apify Google SERP scraper; Apify Google Maps scraper for local; Bright Data purchased datasets; Apify Instagram/TikTok/X profile scrapers; Apify LinkedIn Jobs scraper for intent; Instantly Supersonic Leads; and direct HTTP scraping of a source nobody else scrapes. One actual build is shown: an n8n workflow that runs the Apify SERP actor, limits results, fetches each company website's raw HTML, parses phone numbers procedurally, then feeds the unstructured blob to GPT-5 for structured extraction (owner name, title, email, pitch angles) into a Google Sheet.

## Who it's for
Service sellers running cold outbound who are stuck on list-building, and his own students. He speaks to people who will "create SOPs or give this off to your team", so a small agency owner with at least one helper, not a total beginner.

## Economic argument
Cost-per-lead arbitrage, stated repeatedly. Verbatim: "The exchange rate ends up being about one credit to 40 emails, which is bonkers." On the SERP scraper: "it only costs something like, I don't know, $3 uh per 1,000 records." On Bright Data: "The actual total cost of this is $0.0025 per record" and "You got 100,000 leads for $250." On Instantly: "you buy them for 4,500 um $97 per month for 4,500 leads [sic?]". Enrichment rates given as 70%, 80%, 50%, "somewhere around like 20 to 30%", "like 20 to 40% or so". Outcome proof: "reply rates as high as this one is now at 11.5%. That is 11.5% of all the people that I emailed responding to me. And it looks like about a third of those responded positively." Framing line: "the marginal cost of sending a cold email nowadays tends to zero if you guys have all the infrastructure set up."

## CTA
- **What:** Download the free Google Doc listing every method, email opt-in
- **Where:** [0:31] promised, [32:23] delivered
- **How hard:** soft, lead magnet only; Maker School gets a single incidental mention at [30:09] while explaining a scrape target

## Title + thumbnail pattern
"How to get SO many <resource> you don't know what to do with them" → abundance and overwhelm framing instead of a number. Promises a surplus problem rather than a solved problem, which reads as higher status than "get 100 leads a day".

## Transferable to realtors?
- **Verdict:** ADAPTABLE
- **Why:** The scrape-then-enrich spine works for the B2B edges of a real estate business (agent-to-agent referrals, relocation contacts, investors, property managers, builder reps, local vendor partnerships) and the Google Maps and LinkedIn Jobs intent plays are genuinely usable. It does not transfer to consumer lead gen, where cold-emailing scraped homeowners runs into CAN-SPAM, DNC, state solicitation rules, and MLS data licensing.
