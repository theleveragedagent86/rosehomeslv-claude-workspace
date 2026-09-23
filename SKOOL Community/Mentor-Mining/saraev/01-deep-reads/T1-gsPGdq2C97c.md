# Build This Automated AI LinkedIn DM System in 1 Hour (N8N)

- **id:** gsPGdq2C97c · **url:** https://youtube.com/watch?v=gsPGdq2C97c
- **tier:** T1-SYSTEM
- **published:** 2025-04-02 · **views:** 86,511 · **views/day:** 177 · **runtime:** 72.4 min

## Hook (0:00–0:20)
> "hey everybody today I'm going to show you how to build your very own LinkedIn Outreach system in naden [sic?] this video is perfect for anybody that wants to automate their LinkedIn Outreach with a system that creates a targeted lead list in Apollo using just natural language enriches those leads with detailed profile data uses AI to generate personalized messages sends connection requests and follow-up safely and tracks the entire campaign within a Google sheet"

**Mechanism:** Demo-first plus capability stack. He lists six concrete capabilities in one breath so the viewer scores their own use case against the list before they can bounce, then immediately drops a credential ("I've made over a million dollars with AI and automation").

## Thesis
Cold LinkedIn outreach can be fully automated with off-the-shelf parts, and the messy live build is the thing worth watching because the finished screenshot teaches nothing.

## Beats
| ts | beat | what he's doing |
|---|---|---|
| 0:00 | hook + credential | capability stack, then authority drop |
| 0:34 | end-state demo | shows the finished result before the work, proof-first |
| 3:59 | reveal | "as of this moment not actually built the system yet", opens the loop and attacks competitor videos |
| 5:02 | roadmap | pre-empts "I don't know these tools" objection by defining Apollo, Apify, Phantom Buster |
| 8:23 | cost dodge | frames Apify as the hack around Apollo's export pricing |
| 12:41 | manual proof | insists on doing it by hand once before automating, credibility move |
| 20:03 | critiques own AI output | rejects three icebreakers on camera, taste signalling |
| 25:28 | manual send verified | "never forget this step", turns his own process into a rule |
| 26:01 | the actual build starts | 45 minutes of live n8n work |
| 41:22 | efficiency aside | pin your test data, teaches craft not content |
| 62:02 | visible failure | webhook and container ID never work, he narrates giving up |
| 68:17 | scope cut | drops the "sent" tracking column and rationalizes it |
| 71:13 | safety caveats | volume limits, reply speed, template rotation |
| 72:17 | CTA | Maker School, single soft mention at the very end |

## System demoed
n8n form takes a plain-English audience description. GPT-4.5 converts it to an Apollo search URL (only organization_locations, keywords, person_titles, organization_num_employees_ranges may be changed). An Apify actor scrapes that Apollo URL for leads plus emails and LinkedIn URLs. A limit node caps volume. OpenAI writes a sub-300-character icebreaker per lead using a template ("hey X, love seeing thing about them, I'm also into other thing, plausible tie in, thought I'd connect") with an instruction to always paraphrase, never reuse the exact field value. Rows append to a Google Sheet (id, first, last, LinkedIn URL, title, email status, icebreaker). An aggregate node collapses to one item, then an HTTP POST to the Phantom Buster agent-launch API fires the LinkedIn Auto Connect phantom, which reads the sheet and sends connection requests carrying the icebreaker, 10 per launch. The planned webhook loop to write "sent" back to the sheet fails live and is abandoned.

## Who it's for
Someone who wants to run their own cold LinkedIn outreach and is willing to sit through a 72-minute unedited build. Secondary audience is the aspiring automation builder: he repeatedly frames it as "how to actually build systems that make people money", and the closing pitch is to entrepreneurs "building and scaling their AI automation agencies".

## Economic argument
Mostly cost-of-inputs, not ROI. Verbatim: "it costs a120 [sic?] per a th000 leads so if we want to scrape a th000 leads cost you 20 [sic?] I should note that you can only do a few um like 100 or 150 LinkedIn connection requests totally cold per week per account so like you can think of this as basically $120 will give you enough money to run this LinkedIn campaign for a whole month um at least in terms of leads you obvious still need to pay for the rest of software platforms". Credential: "my name is Nick I've made over a million dollars with AI and automation". Performance claim: "if you can respond to people on average within a minute your conversion rate um jumps up by something like 400%". Social proof: "over 1,400 entrepreneurs". No price is quoted for selling this system to a client.

## CTA
- **What:** Join Maker School; also drop a comment with results or questions
- **Where:** [71:48] comment ask, [72:17] Maker School
- **How hard:** soft mention, one line at the end, no scarcity and no price

## Title + thumbnail pattern
"Build This <adjective> <platform> System in 1 Hour (<Tool>)" → time-boxed build promise with the tool in parentheses for search intent. "This" implies a specific known artifact exists.

## Transferable to realtors?
- **Verdict:** ADAPTABLE
- **Why:** The spine (scrape a targeted list, AI-personalize the first touch, fire it through a sending tool, log to a sheet) is exactly agent-to-agent referral outreach, relocation/HR prospecting, and vendor partnership outreach. But Apollo and LinkedIn are B2B channels and consumer real estate leads do not live there, and Phantom Buster style automated connection requests violate LinkedIn ToS and risk account loss, so the data source and send channel both need rebuilding.
