# Saraev to Realtor Translation Matrix

Built from all 38 deep-reads in [01-deep-reads/](01-deep-reads/), the velocity numbers in [00-corpus.csv](00-corpus.csv), and [ryan-built-inventory.md](../ryan-built-inventory.md).

One row per distinct **system** (a concrete, repeatable mechanism), not per video. Videos that demo nothing (commentary, benchmark reels, student interviews) contribute zero rows and are handled in "What does NOT transfer" below.

## How to read the "Ryan built it?" column

- `YES (skill-name)` means the realtor equivalent already runs, and the named skill or plugin is the thing that runs it.
- `BUILD QUEUE` means it does not exist and should.
- `DROP` means it is not worth building. For DROP rows the Angle column carries the honest reason not to build it, which is itself a content hook.

**A dagger (†) marks skills that were missing from `ryan-built-inventory.md`.** Status below was re-verified directly on disk, because `_System/plugins/` holds dev/source copies and the running versions live in `~/.claude/`. Presence in `_System/plugins/` alone does NOT mean a thing is running.

| Skill | Path | Status |
|---|---|---|
| `transaction-coordination` | `_System/plugins/tc-plugin/skills/transaction-coordination/` | **LIVE, with real data.** The plugin itself is not installed, but its cadences and templates are actively driven by the installed `daily-checklist` skill, which reads `active-transactions.json`. That index currently holds 3 active deals with real addresses and types: 3550 All Hallows (buyer-new-construction), 8320 Moapa Water (buyer-resale), 29 Amber Rock (seller). 5 transaction folders exist on disk. |
| `digital-cannonball` | `~/.claude/plugins/marketplaces/local-desktop-app-uploads/digital-cannonball/` | **LIVE.** Installed plugin. |
| `excalidraw` | `~/.claude/plugins/marketplaces/local-desktop-app-uploads/excalidraw/` | **LIVE.** Installed plugin. |
| `listing-description` | `_System/plugins/listing-description-plugin/skills/listing-description/` | **NOT RUNNING.** Dev copy only. It is not installed and no installed skill or plugin references it. Corrected from YES to BUILT-NOT-INSTALLED. |

`ryan-built-inventory.md` has been updated to include these four with the statuses above. Everything else marked YES is named directly in that inventory.

**Correction applied:** the `listing-description` row was originally marked `YES`. It is written but was never installed, so Ryan cannot invoke it today. Fixing it is a small task, not a build, but until then it does not qualify as something he runs.

Compliance exposure is flagged inline in the Realtor equivalent column as `[FLAG: ...]`.

---

## The matrix

Sorted by views/day descending inside each "Ryan built it?" group. YES first, because what he already runs is what he can credibly film this week.

| Saraev system | video | views/day | Realtor equivalent | Ryan built it? | Module fit | Effort | Angle |
|---|---|---|---|---|---|---|---|
| SOP converted to an agent-readable markdown skill, authored live from a voice description | [QoQBzR1NIqI] | 12923.6 | Every repeatable realtor job written once as a skill and then invoked by name: listing launch, CMA, weekly seller report | YES (skill-builder) | Module 0 | Low | Every checklist you already keep in your head is one file away from running itself. |
| Bulk list build: parallel scrape, LLM classify, push to a sheet, enrich emails (1,000 leads in 87 seconds) | [QoQBzR1NIqI] | 12923.6 | Pull the week's expired listings out of email, dedupe, classify, and land them in a clean mailing list | YES (expired-workflow) | NEW | Low | The expired list that used to eat my Monday morning now takes about a minute. [FLAG: DNC and TCPA before any call or text to those owners. Mail is the safe channel.] |
| Per-lead custom mockup page auto-generated from one spreadsheet row, roughly 30 seconds each | [QoQBzR1NIqI] | 12923.6 | A property-specific marketing plan page built for one expired listing, generated per address | YES (digital-cannonball)† | NEW | Med | I do not send expired sellers a letter about me. I send them a page about their house. |
| Paste a hosting token, the agent deploys the finished page to a public URL | [KDkR0cJRiJk] | 3751.0 | Generated pages get published into the brokerage CMS, not a throwaway host | YES (publish-blogs, publish-landing-page, publish-buyer-guide) | Module 1 | Low | A page that goes live in one minute is worthless if it does not carry your brokerage and license on it. [FLAG: Nevada license advertising rules. A random Netlify or Vercel subdomain fails brokerage identification requirements.] |
| One maximalist meta-prompt plus tool access plus a self-verification loop plus an autonomy clause, batch-generating sites | [h6G9R4UxR6g] | 3025.0 | Batch-generate neighborhood and new-construction community pages with interlinking and schema | YES (local-seo, new-construction) | Module 1 | Med | I built out a stack of Vegas neighborhood pages in an afternoon and Google found every one of them. [FLAG: Fair housing. No demographic or school-quality steering language in neighborhood copy.] |
| Shared human and AI board where moving a card to a status fires the next action | [8rVQuZlRaqo] | 2095.2 | One board of active listings and transactions where a status change fires the client email and the next task | BUILD QUEUE | Module 2 | Med | My calendar does not remind me what to do next. It does it. [RE-GRADED 2026-08-03: was YES (daily-checklist). Fails the exact-match bar. `daily-checklist` *surfaces* TC actions due today by reading `active-transactions.json`, and `transaction-coordination` generates emails when you trigger an event. Neither auto-fires on a status change. The trigger layer is the missing piece.] |
| Autonomous creative pipeline: stills to video to assembled ad campaigns, run as a role-split agent team | [rbUFFMtKcaQ] | 1456.2 | Vertical listing video from the real photos, then a Meta listing ad and lead-form campaign that syncs leads to the CRM | YES (ig-ads, listing-video) | Module 1 | Med | The ad, the video and the lead form for a new listing all get built the same afternoon the photos come back. [FLAG: Fair housing. Housing ads on Meta must run in the Special Ad Category with no age, gender or ZIP targeting.] |
| Client onboarding email chain fired by an event, built from a directive plus a template plus a script | [MxyRjL7NG18] | 1315.1 | Escrow opening, inspection options and milestone emails generated per address for buyer, new-construction and seller deals | YES (transaction-coordination)† | Module 2 | Med | The day we open escrow, every email my client will get for the next thirty days is already written. |
| Skill that turns a design template into a formatted, branded client PDF deliverable | [MxyRjL7NG18] | 1315.1 | Print-ready seller CMA for the listing presentation, plus the buyer-side comp report | YES (seller-cma, cma) | Module 1 | Med | The listing presentation that used to take me two hours takes about ten minutes now, and it looks better. [FLAG: MLS data usage rules on republishing comp data to consumers.] |
| Diagram-generator skill producing hand-drawn style explainer graphics | [qKU-e0x2EmE] | 1150.3 | Whiteboard-style graphics that explain a process to a client or a student without hiring a designer | YES (excalidraw)† | Module 0 | Low | A drawing beats a paragraph when you are explaining escrow to someone who has never bought a house. |
| Front-end revenue copy generated by a skill instead of written by hand | [sduaTkhIm_w] | 941.2 | MLS listing remarks written to a fixed structure and voice | BUILT-NOT-INSTALLED (listing-description)† | Module 1 | Low | Listing remarks are the highest-leverage 1,000 characters you will write all month. [FLAG: Fair housing language in remarks. GLVAR rules on contact information in public remarks.] [STATUS: written but never installed. Install it and this becomes a YES.] |
| Scrape, enrich, AI icebreaker, then a sequenced outbound campaign | [wLNw-rpklfE] | 786.3 | Reverse prospecting: pull the buyer-agent emails tied to a listing and send them a targeted broadcast | BUILD QUEUE (rebuild) | Module 1 | Med | Real estate was the niche that lost in his own test. Here is the version that actually works, and it is agent to agent. [FLAG: MLS rules on using agent contact data pulled from the MLS. CAN-SPAM on the broadcast.] [RE-GRADED 2026-08-03: was YES (reverse-prospecting). Ryan is rebuilding it. Current skill routes through Kit/ConvertKit; the rebuild sends direct from his own email, which needs a new email template and drops the Kit broadcast step. See the rebuild spec below.] |
| Cyclic long-form content generator: research competitors, outline, write section by section, publish | [jBF48jNWPJE] | 587.4 | Weekly Vegas neighborhood and market blog posts written and pushed live to the site | YES (blog-writer, publish-blogs, local-seo) | Module 1 | Low | Two posts a week, written and published, and I never look at a blank page. |
| One long asset fanned out to per-platform posts on a schedule | [jBF48jNWPJE] | 587.4 | One market-update or listing video becomes the blog post, the Reddit post, the carousel and the short | BUILD QUEUE | Module 1 | Low | I film once a week. Everything else you see from me is a copy of that one recording. [RE-GRADED 2026-08-03: was YES across 5 skills. Fails the exact-match bar. All five destination skills exist, but there is no fan-out orchestration: nothing takes one asset and dispatches it to all five on a schedule. Ryan runs them one at a time by hand. The orchestrator is the build, and it is Low effort because every endpoint already works.] |
| Build the target list you are going to work, before you work it | [2XHgJXX49Jk] | 196.8 | Discover and curate the Vegas accounts worth engaging with every day | YES (ig-research) | NEW | Low | Engagement stops feeling random the day you stop picking accounts at random. |
| Kickoff SOP plus check-in templates plus a delivery email template as the fulfillment stack | [bMmlCPLDk1c] | 190.4 | The listing launch package: phase emails, neighbor letters, social posts, voicemail scripts, coming soon through just sold | YES (listing-marketing) | Module 1 | Med | A listing launch is not a to-do list. It is a package that gets delivered the same way every time. [FLAG: TCPA. Ringless voicemail is treated as a call. Scrub DNC before any voicemail drop. Mailed neighbor letters are fine.] |
| Wire any tool to any tool with one API call plus one webhook | [4PZYb86j4wg] | 190.0 | A Meta lead form writes straight into the CRM the second someone fills it out | YES (ig-ads) | Module 0 | Med | Two primitives, an API call and a webhook, connect basically everything you already pay for. |
| AI-personalized outreach at volume, logged so nobody is contacted twice | [gsPGdq2C97c] | 177.3 | Rotated welcome DMs to new followers and reel likers, plus replies on your own comments, each one checked off a shared log | YES (inbound-dm-followers, inbound-dm-likes, inbound-comments, inbound-research) | NEW | Med | The reason I never message the same person twice is a text file, not a good memory. [FLAG: Platform ToS. His Phantom Buster version violates LinkedIn ToS and risks the account. Ryan's runs human-paced in-app, which is the difference.] |
| Scheduled research pipeline that feeds a script and a content calendar | [9zBtU1mwOR4] | 159.3 | Weekly Clark County news and MLS hotsheet research turned into green-screen scripts, blog posts and long-form video | YES (local-news, youtube-manager, yt-long) | NEW | Med | Local news is the only content topic that regenerates itself every single week for free. [FLAG: Every local claim needs a source. No fabricated prices, school ratings or HOA amounts.] |
| Mine a community feed for the questions that keep repeating, then act on them | [eLqveVYFWc4] | 131.5 | Answer the same recurring Vegas questions publicly on Reddit, then turn them into weekly posts | YES (Reddit, subreddit-post) | NEW | Low | I answer the same five Vegas questions every week on Reddit and it brings me more calls than my ads do. |
| Log stage changes to a sheet, visualize as a client-facing dashboard | [OLwEtOEF36A] | 117.8 | The weekly seller report: showings, feedback, online views, price position | YES (weekly-update) | Module 1 | Low | Sellers stop calling for updates when the update shows up every Friday without being asked for. |
| Screenshot-diff self-verification loop: the agent screenshots its own output, compares it to the reference, and iterates | [QoQBzR1NIqI] | 12923.6 | Visual QA on generated landing pages, buyer guides and carousel slides before anything publishes | BUILD QUEUE | NEW | Med | Nobody talks about the boring half of AI work, which is checking that it actually looks right. |
| CLAUDE.md and the .claude directory as steering: brand voice, hard rules, and a rules-file split | [QoQBzR1NIqI] | 12923.6 | A one-file voice and compliance profile every agent loads before writing anything, packaged so a student can copy it | BUILD QUEUE | Module 0 | Low | One file decides whether your AI sounds like you or like everyone else's AI. |
| Plan mode before any complex build, 15 minutes of planning against 35 minutes of build-and-rebuild | [QoQBzR1NIqI] | 12923.6 | Make the AI write the plan for a listing launch or a CMA and get your approval before it produces anything | BUILD QUEUE | Module 0 | Low | The five minutes you spend approving the plan is the five minutes that saves the rebuild. |
| Verification sub agents: implementer builds, a fresh-context reviewer sees only the output, a resolver fixes | [QoQBzR1NIqI] | 12923.6 | A reviewer agent that checks every piece of client-facing copy for fair housing language and factual accuracy before it reaches you | BUILD QUEUE | NEW | Med | I do not trust my own AI. I make a second one check it. [FLAG: This is the control that makes unattended AI safe in a licensed business.] |
| A skill wrapped in a public URL with a form front end that returns a file | [QoQBzR1NIqI] | 12923.6 | A public "what is your home worth" form that returns a real comp-based report instead of a portal estimate | BUILD QUEUE | NEW | High | Every seller already got a number from a portal. Give them the one with the comps attached. [FLAG: An automated valuation delivered to consumers is advertising. Needs brokerage and license identification, and cannot be presented as an appraisal.] |
| Cinematic scroll-bound microsite: hero video, frame interpolation, scroll binding, deploy | [0zlwXSVmoeg] | 9789.2 | A scroll-driven microsite for a luxury listing or a community page, with real property footage as the hero | BUILD QUEUE | Module 1 | Med | The million-dollar listing deserves more than a photo grid and a Matterport link. [FLAG: The hero must be real footage of the actual property. AI-generated property imagery is misrepresentation.] |
| Auto-ingesting knowledge base with recency-weighted hybrid retrieval, distilled per thread | [eCx3SSCcISo] | 6025.8 | Searchable memory across Gmail threads, transaction folders, CRM notes and past listing packages: "what did we agree to with the lender on 123 Elm" | BUILD QUEUE | NEW | High | The answer is already in your email. The problem is that your email is where answers go to die. [FLAG: Client PII, MLS data licensing, brokerage record retention. The auth and audit layer he skips is the layer you cannot skip.] |
| Self-modifying memory file: the agent appends a learned rule every time you correct it | [EsTrWCV0Ph4] | 3802.9 | Correct the AI on your listing copy once and it never makes that mistake again | BUILD QUEUE | Module 0 | Low | Stop retyping the same correction. Make it write the rule down. |
| Video-to-action: a model watches a screen recording at one frame per second and returns the executable steps | [EsTrWCV0Ph4] | 3802.9 | Record yourself doing the MLS or CRM task once, get a working skill out the other side | BUILD QUEUE | NEW | Med | The fastest way to teach AI your workflow is to stop describing it and just record it. |
| Prompt contracts and reverse prompting: a four-section brief, and five clarifying questions before any work starts | [EsTrWCV0Ph4] | 3802.9 | A standing brief format for any AI task: goal, constraints, format, what failure looks like | BUILD QUEUE | Module 0 | Low | Bad AI output is almost always a bad brief wearing a disguise. |
| Frictionless capture: a global hotkey and a phone button that create a task in seconds | [8rVQuZlRaqo] | 2095.2 | Capture the follow-up while you are still walking out of the showing, not three hours later | BUILD QUEUE | Module 0 | Low | The lead you lose is almost never the one you forgot. It is the one you never wrote down. |
| Scored eval checklist the agent must pass before surfacing work, five criteria scored 0 to 2 with a fail threshold | [8rVQuZlRaqo] | 2095.2 | A fair housing, factual accuracy and brand voice rubric every piece of content is scored against, looping until it passes | BUILD QUEUE | NEW | Med | This is the single most valuable thing in his entire catalog for a licensed agent, and almost nobody is building it. [FLAG: Fair housing, no fabricated prices or ratings, brokerage disclosure.] |
| Call transcript in, structured tasks and follow-ups out in the project tool | [Ob5Vu-gD3mo] | 1511.1 | The buyer consult or listing appointment recording becomes the task list and the follow-up sequence | BUILD QUEUE | Module 2 | Med | I stopped taking notes on appointments. The recording takes them, and it makes the follow-ups too. [FLAG: Recording consent. Nevada is one-party consent, but disclose to the client anyway.] |
| Mass-generate candidates with a vision-based self-QA loop, then let human taste pick | [rbUFFMtKcaQ] | 1456.2 | Twenty hook variants and twenty thumbnails per video, scored by the agent, chosen by you | BUILD QUEUE | NEW | Med | AI is not better than you at picking. It is better than you at producing things to pick from. |
| Unattended runs: webhooks and cron so work happens while you are not at the desk | [MxyRjL7NG18] | 1315.1 | The Friday seller report and the Monday news pull run themselves without anyone opening a laptop | BUILD QUEUE | NEW | Med | The work that reliably gets skipped is the work that requires you to remember to start it. |
| A meta-directive that chains every other directive under one command | [MxyRjL7NG18] | 1315.1 | One command, "launch 123 Main St", runs description, marketing plan, video, ads, reverse prospecting and neighbor letters | BUILD QUEUE | Module 1 | Med | Ten skills is a toolbox. One command that runs all ten is a business. |
| Self-annealing directives: the system patches its own script when a step breaks | [MxyRjL7NG18] | 1315.1 | When a workflow breaks because a site changed, it fixes itself instead of waiting for you | BUILD QUEUE | NEW | Low | Automations that break stay broken. The fix is to let them repair themselves. |
| Automated prompt optimization: an objective metric, an automated scorer, and permission to mutate the prompt on a loop | [qKU-e0x2EmE] | 1150.3 | Run the listing-description skill ten times, score every output against a compliance and accuracy rubric, keep the winner | BUILD QUEUE | NEW | Med | Your prompt is not a thing you tune by feel. It is a thing you can measure. |
| Stage-aware nurture: read the CRM pipeline, pull every prior thread, write the next informal check-in | [sduaTkhIm_w] | 941.2 | Past-client and sphere reactivation, with the check-in written from what actually happened in that relationship | BUILD QUEUE | NEW | Med | The most valuable list you own is the one you already sold to and then stopped talking to. [FLAG: TCPA and DNC if any of it goes by text. CAN-SPAM opt-out on email.] |
| Video-to-video AI editing on footage you actually shot, with the quality seam hidden behind a scene cut | [7Su6W_FlUbk] | 873.5 | An AI effect on your talking-head hook, then cut straight to real listing b-roll | BUILD QUEUE | Module 1 | Low | The effect goes on you, never on the house. [FLAG: Altering footage of the property is misrepresentation.] |
| AI inbox categorization that labels and routes mail automatically | [jBF48jNWPJE] | 587.4 | Triage a lead-heavy inbox into new lead, showing request, active transaction, vendor and noise | BUILD QUEUE | NEW | Low | The first ten minutes of your day should not be spent deciding which emails matter. |
| Speed of response as the conversion lever, with a stated 400 percent claim on sub-minute replies | [gsPGdq2C97c] | 177.3 | Inbound call or form fill triggers a personalized text back in under five minutes, every time, including at 9pm | BUILD QUEUE | NEW | Med | Most agents do not lose leads to better agents. They lose them to faster ones. [FLAG: TCPA. An automated text to a web lead needs prior express consent captured in the form, and STOP must be honored.] |
| Scrape adjacent creators' top-performing posts, transcribe, research, and rewrite as your own script | [9zBtU1mwOR4] | 159.3 | Mine the top-performing Vegas agent and lifestyle reels for angles worth using | BUILD QUEUE | NEW | Med | Borrow the structure of what is working locally, never the words. [FLAG: There is a real reputational cost to visibly parroting other agents in your own market that does not exist in his niche.] |
| Personalized screen-share video sent as a give, not a pitch, closing on a zero-friction reply | [bao3ogOcpiw] | 123.3 | A three-minute personalized marketing plan video recorded for one specific expired listing, closing with "just reply yes" | BUILD QUEUE | NEW | Low | Do not ask an expired seller for an appointment. Show them the plan and ask them to reply. [FLAG: Expired and FSBO outreach is regulated solicitation. Scrub DNC before any call. Nevada license advertising rules apply to the video itself.] |
| Local business email scraping from a maps search, enriched and dropped into a sheet | [eElnA0mCzXw] | 103.6 | Build the lender, title, builder and property manager referral partner list for a specific submarket | BUILD QUEUE | NEW | Low | Your next ten deals are more likely to come from twenty vendors than from two thousand strangers. [FLAG: CAN-SPAM on outreach. RESPA Section 8 on anything that looks like paying for referrals.] |
| Review request triggered at job completion, gated on the technician's own internal report | [4ryBQ9P_p64] | 34.3 | Post-close review request, sent only after your own internal note on how the deal actually went | BUILD QUEUE | NEW | Low | Ask for the review the day it closes, not the week you remember to. [FLAG: Gate on your own internal notes, never on the client's sentiment. Suppressing negative reviews is an FTC problem.] |
| Booking link sent by text during the call, plus a three-stage reminder cadence | [4ryBQ9P_p64] | 34.3 | Consult and showing booking link sent while you are still on the phone, with reminders a week out, a day out and two hours out | BUILD QUEUE | NEW | Low | The appointment you book while they are still on the phone is the one that actually happens. [FLAG: Consent for reminder texts.] |
| Vibe-coded full-stack app handling client PII, e-signature and Stripe payments | [QoQBzR1NIqI] | 12923.6 | NONE. Contracts, signatures and earnest money go through the brokerage's approved platform | DROP | n/a | n/a | The one thing I will not build with AI is anything that touches a contract or a client's money. His own security warning at 130:46 applies double to us. |
| Agent teams and adversarial multi-agent debate, roughly 80 dollars of tokens on one query | [QoQBzR1NIqI] | 12923.6 | NONE at the scale a solo agent or small team operates at | DROP | n/a | n/a | Eighty dollars of tokens to review one codebase is a great demo and a terrible line item in a real estate business. |
| Five parallel browser agents filling contact forms at scale | [EsTrWCV0Ph4] | 3802.9 | NONE. Mass unsolicited contact is a TCPA, DNC and fair housing problem, not a productivity win | DROP | n/a | n/a | The demo everybody shares from that course is the one that would cost me my license. |
| Stochastic multi-agent consensus, N agents vote and you take the mode | [EsTrWCV0Ph4] | 3802.9 | NONE for pricing. A price opinion comes from comps and condition, not from a vote of language models | DROP | n/a | n/a | If your AI gives you a price and cannot show you the four comps it came from, that is not a price. |
| Dithered AI-generated hero art as the top of a page | [KDkR0cJRiJk] | 3751.0 | NONE for a listing page. It needs real photography, compliant copy and IDX, all three of which this fights | DROP | n/a | n/a | Every "make it look like a ten thousand dollar site" trick makes a listing page worse, not better. |
| Fabricated product and property imagery generated at volume for ads | [rbUFFMtKcaQ] | 1456.2 | NONE. Generating or materially altering imagery of a home for sale is misrepresentation | DROP | n/a | n/a | AI can write my ad. It cannot photograph a house that does not look like that. |
| Cold email infrastructure at volume: purchased domains, dozens of warmed mailboxes, deliverability tooling | [wLNw-rpklfE] | 786.3 | NONE on the consumer side. His own real estate test campaign produced three replies and zero opportunities | DROP | n/a | n/a | He ran this exact machine at real estate agents and killed the campaign himself. I am not going to run the version he already proved does not work. |
| A daily platform-application streak as the client acquisition channel | [DbZotE0Ch0g] | 718.7 | NONE. There is no Upwork for listings | DROP | n/a | n/a | The streak idea is right. The channel does not exist for us, and pretending it does wastes a month. |
| Free scraping of business and consumer contact data without paid APIs | [OroDNJl-pyc] | 209.8 | NONE for homeowner data. CAN-SPAM, state DNC and MLS or IDX terms all apply | DROP | n/a | n/a | Every "unlimited free leads" video ends in the same place for us, which is a Do Not Call list. |
| Niche selection framework: pick digital, over a thousand per deal, lightly regulated | [OLwEtOEF36A] | 117.8 | NONE. Real estate fails two of his three rules by definition, it is geographically locked and heavily regulated | DROP | n/a | n/a | By his own filter, my business is the one you should not sell to. He is right about selling and wrong about buying. |

**Row counts:** 58 total. 21 YES, 27 BUILD QUEUE, 10 DROP.

---

## The four honest gaps, confirmed and corrected

`ryan-built-inventory.md` lists four things Ryan does not have. Checked against all 38 deep-reads and against the installed skill and plugin directories:

### Gap 1: Missed-lead speed to response. CONFIRMED.

Nothing in the inventory or in `~/.claude/skills/` or the installed plugins does inbound speed to lead. The deep-reads support it as the highest-value miss: `gsPGdq2C97c` states "if you can respond to people on average within a minute your conversion rate um jumps up by something like 400%." That is his number, not a computed one, and it is the only conversion-lift figure of that size anywhere in the corpus.

### Gap 2: Transaction coordination end to end. CLOSED. Strike it from the inventory.

The `transaction-coordination` plugin is live at `/Users/ryanrose/Downloads/Claude/_System/plugins/tc-plugin/skills/transaction-coordination/`. It carries templates for buyer new-construction, buyer resale and seller, cadence JSON files for all three, an inspector contact list, and a shared `active-transactions.json` and `calendar.json` with `daily-checklist`. It is in the live skill roster. Module 2 is not "curriculum only", it runs.

What is genuinely still open inside Module 2 is contract generation and e-signature, which `Module-2-AI-Transaction-Coordinator.md` already carries as "Module 2.5: Contract Automation (Future / Placeholder)". Per the DROP row on `[QoQBzR1NIqI]`, that one should stay closed. Contracts, signatures and earnest money belong on the brokerage platform.

**Replacement gap 2: there is no eval or QA layer.** Two separate deep-reads point straight at it. `[8rVQuZlRaqo]` at 2095.2 views/day builds a scored checklist the agent must pass before surfacing work, and `[qKU-e0x2EmE]` at 1150.3 builds an automated loop that optimizes a prompt against a rubric. Ryan has hard content rules written into `CLAUDE.md`, but nothing scores output against them before he sees it. In a licensed business with fair housing and factual-accuracy exposure, that is a larger hole than cold email infrastructure.

### Gap 3: Database reactivation at scale. CONFIRMED, and the deep-reads name it three separate times.

`[sduaTkhIm_w]` opens with a production `follow-up-nurture` skill that walks the CRM pipeline and writes stage-aware check-ins. `[YIl-awY250k]` draws the universal business shape and lists "reactivation" as a named stage every service business has. `[4ryBQ9P_p64]` prices it directly, both the seasonal blast to the past-customer list and the realtor pie story, which is a reactivation story told to plumbers.

### Gap 4: Paid cold email infrastructure. CONFIRMED as a gap, but demote it to last.

`[wLNw-rpklfE]` is the strongest evidence against building this. Real estate was one of his three live test niches and it lost outright: "The real estate campaign has had three replies ... we've had zero opportunities ... I have a feeling this real estate campaign probably just ain't it, dog." On the consumer side it collides with CAN-SPAM, state DNC and solicitation rules. On the agent-to-agent side, `reverse-prospecting` plus Kit already covers the only use case that is both legal and useful.

### Ranked by content value times buildability

1. **Missed-lead speed to response.** Highest content value in the set, because every agent already knows they are slow and nobody has shown them the fix. Buildability is Medium: the trigger is easy, the TCPA consent hygiene is the real work.
2. **The eval and compliance gate (replacement gap 2).** High content value precisely because nobody in the realtor-AI space is talking about it, which makes it defensible territory. Buildability Medium. It is also the unlock for everything else, since you cannot run anything unattended until something is checking it.
3. **Database reactivation.** High content value and high dollar value, but buildability is Medium to High because it needs CRM write access, a DNC scrub, and per-contact consent state before a single message goes out.
4. **Cold email infrastructure.** Lowest on both axes. Saraev's own real estate test failed, and the compliance ceiling on the consumer side is hard. Build it last or not at all.

### Also correct the inventory

Four running skills are missing from `ryan-built-inventory.md`: `transaction-coordination`, `listing-description`, `digital-cannonball`, `excalidraw`. Paths are listed at the top of this document.

---

## What does NOT transfer, and why

These are the stretches. They are here instead of in the matrix.

- **B2B contact databases.** Apollo, LinkedIn Sales Navigator, Any Mail Finder, Bright Data. There is no consumer equivalent, and homeowner contact data is governed by DNC, CAN-SPAM, state solicitation rules and MLS or IDX licensing. Every "scrape unlimited leads" video in the corpus dies on this.
- **Automated platform outreach.** Phantom Buster connection requests, mass browser form-filling. Platform ToS violations that risk account loss, plus TCPA and fair housing exposure the moment the recipients are consumers.
- **Freelance marketplace acquisition.** Upwork applications, Instantly campaigns to businesses. No realtor equivalent exists.
- **Niche selection.** A licensed agent has one geography and one license. There is no niche to choose, which makes the entire `[g_Q15Ibn3Iw]` and `[OLwEtOEF36A]` selection apparatus inapplicable.
- **Model cost routing.** The 60-30-10 rule in `[EsTrWCV0Ph4]`. Agents run on flat monthly plans. There is nothing to route and no bill to optimize.
- **Toolchain depth with no payoff.** Git worktrees for parallel agent isolation, converting MCP servers to token-cheap skills, agent-team orchestration. Real techniques, zero realtor return, and teaching them makes the curriculum look harder than it is.
- **Selling the automation itself.** Most of the T1 catalog prices systems at 1,500 to 15,000 dollars per build. That is the AI Clients business, not the realtor business. Mixing the two confuses what The Leveraged Agent actually promises, which is a realtor running their own practice better, not a realtor becoming an automation consultant.
- **Seven videos carry no system at all.** `[k1DTxuBur-Y]` 6214.1, `[ikxxjRWX0Yg]` 1901.2, `[esXXuejofgk]` 1037.0, `[YIl-awY250k]` 1492.2, `[36xOZ1e6tuM]` 98.1, `[g_Q15Ibn3Iw]` 163.1 and `[TxMAUMUn-is]` 198.9 are commentary, benchmark reels or student interviews. Steal the packaging from these, never the content. Worth noting that `[ikxxjRWX0Yg]` is a seven-minute single-take commentary with no editing and no build, and at 1,901.2 views per day it outperforms most of his multi-hour courses on a per-minute-of-production basis.

---

## The thesis problem

Source: `[TxMAUMUn-is]`, "Why I Don't Sell AI to Local Businesses (Despite What Gurus Claim)", published 2025-04-15, 94,462 views, 198.9 views/day.

### His three reasons

**1. The lead pool is too small to iterate on.** He makes it visceral at 1:01 with "How many HVAC businesses are there in Chattanooga?" and then does the funnel math on screen at 7:59: roughly 1,500 potential clients, 1,500 emails, about 10 responses, 3 sales calls, 1 client. Then you have exhausted the city and have to move to a new one. You cannot run enough volume in one geography to learn anything.

**2. The sales call becomes unpaid education.** At 1:57, then developed at 11:28 with two sales calls compared minute by minute. A low-technical-literacy buyer does not know what they are buying, so you spend the call teaching instead of selling, and you are not paid for that time. The dental seminar failure story at 9:31 is his own evidence against himself, which is why it lands.

**3. Thin margins and no tech budget.** From 3:52, peaking with the Craigslist story at 14:06: a business "making over $2 million a year" whose owner answered "Oh, we're between 6 to 10%" on margin, so "120 grand a year profit, and he splitting us with a partner." Against that he sets his own zero-rent internet business. He does concede the counter-case: moving a company from 5 percent to 10 percent margin "objectively" adds five points and "subjectively" doubles their bottom line.

### Each one against Ryan's actual situation

**Reason 1 does not apply, because Ryan is not selling to local businesses. He is one.** Saraev's argument is about the economics of acquiring local businesses as clients. Ryan has two markets and neither is that. Rose Homes LV sells to Clark County buyers and sellers, a pool that replenishes continuously through moves, life events and new construction rather than being consumed once. The Leveraged Agent sells to licensed agents nationally, which is not geographically capped at all. The distinction between *serving* local businesses and *being* one is the entire answer to reason 1, and it is a distinction the video never makes because it never needs to.

**Reason 2 lands, and it is the real threat.** Agents are exactly the low-technical-literacy buyer he describes. Anyone selling AI to realtors will spend a large share of every conversation teaching rather than selling. But note what Saraev does with that same cost: he charges for it. Maker School *is* the unpaid education converted into a paid product. Ryan's structure is identical, and Module 0 already handles the specific risk, since "Day 1: Your First AI Workflow (The Quick Win)" is designed to produce a result before the student's patience runs out. The threat is not that education is expensive. The threat is education that arrives before the first win.

**Reason 3 inverts.** A solo agent is not a 6 to 10 percent margin business. Gross commission per transaction is large relative to the marginal cost of doing one more, and the tool bill Saraev is comparing against is his own stated 17 dollars a month for Claude Pro, cited at 2:45 in `[QoQBzR1NIqI]`. On pure unit economics, agents are closer to the buyer profile he tells you to look for than the one he tells you to avoid. Where real estate genuinely fails his own filter is `[OLwEtOEF36A]` at 5:47, "low regulation", where he says stay away from regulated verticals. Real estate is heavily regulated and geographically locked, and it fails that test outright. That is an honest limitation and it belongs on the record.

**The counter-evidence Ryan actually holds.** `ryan-built-inventory.md` documents paying local-business AI clients: Brian Esposito, Nick Nolf Property Management, Crystal, Zbuyer. That is a live counterexample to the "structurally impossible" framing. Be precise about what it does and does not prove. It disproves "you cannot do this." It does not by itself disprove his margin math or his funnel math, and claiming it does would be the kind of overreach the video is designed to punish.

**The counter-evidence that runs the other way.** `[wLNw-rpklfE]` at 786.3 views/day is Saraev running real estate as one of three live test niches, and the campaign lost: three replies, zero opportunities, killed on camera. That is real evidence, but read it narrowly. It proves cold email to realtors is a bad channel. It does not prove realtors are a bad market, and the two get conflated constantly.

### Where his own revenue actually comes from

Across all 38 deep-reads, the CTA in nearly every video is Maker School, a 90-day program with a first-client-or-refund guarantee, priced with member-count scarcity. His stated numbers are "over $4 million a year in profit" `[QoQBzR1NIqI]`, "over 400 grand a month" `[eLqveVYFWc4]`, "My business is going to do over $400,000 this month" `[8rVQuZlRaqo]`, and community sizes climbing from "just under 1500 members" `[4PZYb86j4wg]` to "almost 1,800" `[TxMAUMUn-is]` to "over 2,500" `[bMmlCPLDk1c]`.

So the argument "do not sell AI services to local businesses" is being made by someone whose revenue does not come from selling AI services to local businesses. It comes from selling education about selling AI services. That is not hypocrisy, and it should not be presented as a gotcha. It is a disclosure that belongs alongside the argument, and it is the single most useful fact in the video, because it tells you which of his claims are load-bearing for him and which are not. The margin math is not something he has to be right about. The education product is.

### Verdict: opportunity, with one real threat inside it

**It is an opportunity, and it is the best-packaged one available.** `[TxMAUMUn-is]` is the most credible public objection The Leveraged Agent will ever have to answer, it already has 94,462 views, and it was written by someone with more authority on the topic than any competitor Ryan will face. Ryan can answer it with something Saraev structurally cannot: he is the local business, he runs 30-plus of these systems in a live Vegas brokerage, and he has paying local-business AI clients on the side. The video writes itself. "The guy who told everyone not to sell AI to local businesses is right, and it is the best news a realtor has gotten all year." Saraev even asks for the fight at 16:24: "feel free to drop a comment down below. I'm happy to debate you guys."

**The threat is reason 2, and it is inside the product, not outside it.** If The Leveraged Agent's promise is "buy this and your business runs itself," Ryan inherits the unpaid-education cost Saraev is warning about. It just moves from the sales call into churn. The defense is the one Saraev already uses and the one Module 0 already implements: charge for the education, ladder it, and make the first win land before the explanation does.

**The second, smaller threat is his own filter in `[OLwEtOEF36A]`.** Real estate is regulated and geographically locked, so an outside vendor selling AI into real estate has a capped, compliance-heavy business. That is a real constraint on *the agency play* and it is exactly why Ryan should not position The Leveraged Agent as an agency. It is not a constraint on Ryan, because the license and the geography that cap an outsider are the two things that make him credible to the people he is actually selling to. The regulation is the moat.

---

# Re-grade, 2026-08-03

Ryan's instruction: **"build new stuff unless what is in the table is basically an exact match."** The original YES bar was "a skill exists that covers this." The new bar is stricter: the existing skill must already do the realtor equivalent as written, not merely be adjacent to it.

Three rows failed and moved to BUILD QUEUE. Revised counts: **17 YES, 30 BUILD QUEUE, 10 DROP, 1 BUILT-NOT-INSTALLED.**

| Row | Was | Now | Why it failed the bar |
|---|---|---|---|
| Status change fires the next action [8rVQuZlRaqo] | YES (daily-checklist) | BUILD QUEUE | `daily-checklist` surfaces TC actions, `transaction-coordination` generates emails on a manual trigger. Nothing fires automatically on a status change. The trigger layer does not exist. |
| Sequenced outbound campaign [wLNw-rpklfE] | YES (reverse-prospecting) | BUILD QUEUE (rebuild) | Ryan is rebuilding it. Kit routing comes out, direct-from-email goes in. |
| One asset fanned out to every platform [jBF48jNWPJE] | YES (5 skills) | BUILD QUEUE | All five endpoints work. The orchestrator that dispatches one asset to all five does not exist. Low effort, because only the dispatch layer is missing. |

The 17 surviving YES rows all clear the exact-match bar: the skill already produces the stated realtor deliverable.

## Rebuild spec: reverse-prospecting

Per Ryan, 2026-08-03. Current skill pushes a Kit (ConvertKit) broadcast. He wants it sent direct from his own email instead.

**What changes**

1. **Drop the Kit broadcast step.** Kit was the send mechanism; direct email replaces it.
2. **Build a new email template** for direct send. This is the piece that does not exist yet and is the actual blocker.
3. **Keep** the MLS agent-email extraction, which is the part that already works.

**Decide before building**

- **Send mechanism.** Gmail API, an SMTP script, or paste-into-compose. This determines whether it can batch at all or stays one-at-a-time.
- **Volume per listing.** A reverse-prospecting pull can return a lot of agent emails. Direct-from-Gmail has daily send caps that Kit did not have, and burning your primary domain's sending reputation is a real risk that Kit was absorbing for you.
- **Unsubscribe handling.** Kit managed CAN-SPAM compliance. Sending direct moves that obligation onto you. Every commercial email still needs a working opt-out and a physical mailing address.

**FLAG:** CAN-SPAM applies to agent-to-agent commercial email. MLS rules restrict what you may do with agent contact data pulled from the MLS. Confirm GLVAR's position before sending at volume.
