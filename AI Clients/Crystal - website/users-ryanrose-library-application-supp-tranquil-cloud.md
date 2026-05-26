# viewvegasnow.com Rebuild Plan
**Client:** Crystal Schriefer, Sphere Real Estate
**Prepared:** May 2026
**Engagement:** 90-day done-with-you website rebuild

---

## Context

Your website at viewvegasnow.com has the right pieces in place. WordPress, Elementor, Yoast SEO, IDX Broker, and Follow Up Boss are all installed. The site is set to be indexed by Google. There are 28 quality blog posts already published. Your /about-crystal/ page is well-built and converts.

The problem is that the pieces are not connected. IDX Broker is installed but listings are not displaying on www.viewvegasnow.com (only on the bare subdomain). The /buyers/, /sellers/, and /investors/ pages are essentially empty (about 90 words each, just navigation and footer). The /contact/ page returns a 404. Every page is missing the H1 tags, meta descriptions, and image alt text that Google uses to understand and rank a page. Forms are not wired to Follow Up Boss, so even if a lead came in, it would not reach you in a way you could act on.

The result: a site that loads, but does not generate leads.

This plan fixes those connections in three phases over 90 days. Phase 1 produces visible changes you can see in the first week. Phase 2 builds the lead-capture engine. Phase 3 grows the organic traffic and authority that compounds over months 4 through 12.

---

## What's Different About This Engagement

You've worked with two prior consultants who did not deliver. The structural reason: they treated the site as a design project. Your goal is leads, not aesthetics. Three things this engagement does differently:

1. **Visible wins in week one.** By Day 7 you will see live listings on your homepage, a working contact page, a sticky "Talk to Crystal" button on every page, and your first test lead landing in Follow Up Boss. Every change comes with a Loom walkthrough so you see the proof, not just the report.
2. **Receiving end before sending end.** Day 1 work wires Follow Up Boss to receive leads. Every form, phone call, and IDX inquiry built after that has a working destination from the moment it goes live.
3. **You own the credentials.** Every login, every API key, every plugin license is stored in a shared 1Password vault you control. If this engagement ends, nothing breaks.

---

## Recommended Approach

### Phase 0: Discovery and Access (Day 0)

A 90-minute kickoff call to capture credentials, audit the current setup, and lock the Phase 1 start date. Without this, every later phase risks slipping a few days while we wait on logins.

**You provide access to:**
- WordPress admin
- IDX Broker dashboard (to confirm plan tier and grab API key)
- Follow Up Boss (admin role)
- Google Search Console, Google Analytics 4 (or confirm they don't exist yet), Google Business Profile
- Domain registrar (for one DNS change)
- Confirmation of which form plugin is in use (Elementor Pro Forms, WPForms, or Contact Form 7)

**You decide on:**
1. Subdomain name for IDX listings (recommended: `search.viewvegasnow.com`)
2. Whether to swap your published phone number to a Follow Up Boss tracked number
3. Brokerage compliance review process (does Sphere need to approve new IDX templates and investor content?)

**Deliverable:** Access and audit memo, plus a 1Password vault you control.

---

### Phase 1: Foundation Week (Days 1 to 7)

**Goal:** A website you can screenshot and send to your sphere by Day 8. Real listings on the homepage. Working forms. Leads flowing into Follow Up Boss.

**Day 1: Wire Follow Up Boss to receive leads**
- Install the FUB Pixel site-wide for automatic form-submission tracking
- Configure FUB Connected Email so IDX Broker lead notifications auto-create contacts
- Set up your FUB Company Number for tracked inbound calls and 2-way text
- Verify with a test submission landing in your inbox within 90 seconds

**Day 2: Restore /contact/ and add sticky CTA**
- Rebuild /contact/ in Elementor using /about-crystal/ as the template (your one strong page)
- New contact form wired to FUB
- Embedded Google Map of the Sphere office
- Sticky "Talk to Crystal" button on every page (desktop floating button, mobile bottom bar with Call, Text, and Email)
- Fix the broken footer link

**Days 3 to 4: IDX Broker showing real listings on viewvegasnow.com**

This is the centerpiece visible win. Your IDX Broker is installed but the WordPress plugin (IMPress for IDX Broker) is either missing or unconfigured. Once configured:
- Live listings grid on your homepage ("New Las Vegas Listings This Week," "Featured Homes Under $500K," "Luxury $1M+")
- Search bar in the global header so visitors can search like Zillow
- All search results pages styled to match your site (not the bare subdomain)
- New subdomain `search.viewvegasnow.com` with SSL provisioned automatically
- IDX Broker leads route directly to Follow Up Boss

DNS change happens Day 3 morning so SSL is ready by Day 4 afternoon.

**Day 5: SEO foundation pass**

The work that unlocks Google's ability to understand your site:
- Rewrite title tags on every page (your homepage will go from "Home, VIEW VEGAS" to "Las Vegas Homes for Sale | Crystal Schriefer, Realtor | View Vegas Now")
- Add meta descriptions to every page (currently zero except /about-crystal/)
- Add H1 tags to every Elementor page (currently zero on homepage, /buyers/, /sellers/, /investors/, neighborhoods)
- Bulk-add image alt text site-wide (zero today)
- Redirect /las-vegas-neighborhoods-v2/ to clean /las-vegas-neighborhoods/

**Day 6: Google stack**
- Verify domain in Google Search Console
- Submit your XML sitemap
- Install Google Analytics 4
- Verify and optimize your Google Business Profile
- Send 5 review requests to your most recent closed clients

**Day 7: Walkthrough and handoff**
- 30-minute screen-share showing every change
- Loom video tour of the new site
- Lead-response playbook so you know exactly what to do when a new lead lands in FUB

**Phase 1 deliverable bundle:**
- Handoff doc with every change made and every credential location
- 10 to 15 minute site-tour Loom video
- Before/after screenshots of homepage, contact page, mobile view, search results
- Lead-response playbook (1 page)
- 7-day baseline analytics snapshot

**Phase 1 risks to know about:**
- DNS propagation takes 24 to 48 hours. Day 3 timing protects against this.
- IDX Broker Lite plan does not support the dynamic wrapper. If you're on Lite, an upgrade to Platinum is required ($30 to $55 per month).
- Sphere may need to review new IDX page templates before they go live.
- Aggressive WordPress caching can prevent IDX widgets from refreshing. May need to exclude IDX pages from cache.

---

### Phase 2: Conversion Infrastructure (Weeks 2 to 3)

**Goal:** Every page that should be capturing leads is now a real page with a real form wired to Follow Up Boss. Your analytics show you which pages are converting.

**Week 2: Rebuild the empty service pages and add the home-valuation tool**

- **/buyers/** rebuilt as a 1,500-word real page: how you help buyers, your step-by-step process, neighborhoods you specialize in, embedded IDX search, testimonials, lead form
- **/sellers/** rebuilt: why sellers work with you, your pricing methodology, marketing approach, sold-listings widget, CTA to home valuation
- **/investors/** rebuilt: investment markets you cover (long-term rentals, short-term rental zones, fix and flip), embedded investor-friendly IDX search, lead form
- **/home-valuation/** new page with IDX Broker's valuation widget, wired to FUB and tagged "Seller, Valuation Request"
- Refresh 11 existing blog posts that already half-cover target keywords (add meta, alt text, internal links, lead capture form)

**Week 3: Tracking and automation**

- Google Tag Manager events fire on form submit, phone tap, email click, IDX listing view, IDX account signup, valuation form submit
- All events flow to GA4 and FUB Pixel so you can see what's converting
- Follow Up Boss Action Plans set up for each lead type:
  - Buyer leads: 7-touch nurture sequence
  - Seller and valuation leads: 1-hour personal outreach plus auto comp report
  - Investor leads: 4-hour personal outreach with investor tag
- Refresh 11 more blog posts (22 of 28 total now optimized)
- Reusable lead-capture block you can drop into any new blog post going forward

**You provide:**
- Content for /buyers/, /sellers/, /investors/ (we provide the outline and prompts; you fill in your voice). Optional add-on: we can write these if you prefer.
- Top 22 blog posts to refresh (we'll pull this from Search Console once it has data)
- FUB Action Plan email and text copy
- Optional: 60-second mobile phone intro video for /buyers/ and /sellers/

**Phase 2 deliverable bundle:**
- Updated handoff doc
- 10-minute Loom of all 4 new pages
- FUB Action Plan content backup
- Lead response playbook update
- Mid-engagement check-in call

---

### Phase 3: Authority and Traffic (Weeks 4 to 12)

**Goal:** Compound organic traffic, earn local backlinks, and become citation-worthy in AI search results (ChatGPT, Perplexity, Google AI Overview). This is the long game that turns the site into a steady lead source over months 4 through 12.

**Workstream A: 8 neighborhood pillar pages (Weeks 4 to 8)**

One per week: Summerlin, Henderson, Mountains Edge, Centennial Hills, Aliante, Lake Las Vegas, Inspirada, Sun City Summerlin and Anthem.

Each page: 1,800 to 2,500 words, embedded IDX search filtered to that area, embedded listings widget showing 9 most recent homes for sale, FAQ schema with 6 to 8 common questions, lead form pre-tagged with neighborhood interest, internal links to related blog posts and service pages.

**Workstream B: Conversion expansion (Weeks 4 to 6)**
- /relocating-to-las-vegas/ hub for high-intent out-of-state buyers
- /seller-guide/ cluster: pricing strategy, prep checklist, marketing process, closing
- Refreshed downloadable Las Vegas Buyer Guide PDF gated by email capture

**Workstream C: Monthly market reports (Weeks 4 onward)**
- Templated /las-vegas-market-report/ blog you fill in monthly with current MLS data
- Auto-text to recent valuation leads when each report drops

**Workstream D: Local backlink campaign (Weeks 5 to 12)**
- Outreach to LV Review-Journal, LV Weekly, KTNV, Vegas PBS, Greater LV Chamber, neighborhood HOA newsletters, local nonprofits
- 3 pitch angles: market commentary, neighborhood expert, woman in business
- HARO, Qwoted, and Featured.com profiles set up for ongoing earned media

**Workstream E: AI search optimization (Weeks 6 to 10)**
- FAQ schema on every pillar page
- RealEstateAgent schema with full credentials on /about-crystal/
- /las-vegas-real-estate-stats/ citation-bait page (built to be quoted by ChatGPT and Perplexity)
- Robots.txt updated to explicitly allow GPTBot, ClaudeBot, PerplexityBot
- 4 answer-engine articles in Q&A format on highest-volume questions

**Phase 3 deliverable bundle:**
- Per-pillar handoff (live URL, Loom, screenshot) shipped weekly as each pillar goes live
- Monthly market report template plus publishing instructions
- Backlink outreach tracker (live shared spreadsheet) reviewed weekly with you
- AI-search audit at Week 10 showing inclusion in AI Overview and Perplexity citations
- 90-day final report at Week 12: traffic vs. baseline, leads vs. baseline, top-converting pages, recommended Phase 4

**Phase 3 risks to know about:**
- Earned media has a 30 to 60 day lag. Phase 3 means "we sent 30 pitches and 2 to 4 will land in 60 days," not "10 backlinks in a month."
- Content velocity is the most common stall point. We'll decide in Phase 2 whether you write the pillar pages yourself or we write them on your behalf.
- Some MLS-derived stats require IDX Broker disclaimers. Run the stats page past Sphere compliance.

---

## Expected Results by Day 90

- Site fully indexed in Google with 40 to 70 indexed pages (up from 8 today)
- Search Console shows growing impressions for at least 8 of the easy keywords identified in the audit
- First 5 to 15 organic leads attributed to the website per month
- Foundation in place for compounding traffic over months 4 to 12

---

## Critical Pages and Systems to Be Modified

**WordPress pages:**
- / (homepage): new title, H1, meta, IDX listings sections, sticky CTA
- /buyers/: full rebuild
- /sellers/: full rebuild
- /investors/: full rebuild
- /contact/: rebuild from 404
- /home-valuation/: new
- /las-vegas-neighborhoods/: rebuild from thin v2 hub
- 8 new neighborhood pillar pages
- /relocating-to-las-vegas/: new hub
- /seller-guide/: new cluster
- /las-vegas-market-report/: new recurring URL
- /las-vegas-real-estate-stats/: new citation-bait page
- 22 of 28 existing blog posts: refresh meta, alt, internal links, lead capture

**Plugins to install or configure:**
- IMPress for IDX Broker (Wordpress.org, free)
- FUB Pixel (snippet, free)
- Google Tag Manager
- UpdraftPlus or similar (for backups before each phase change)
- Sticky button plugin or Elementor sticky CTA widget

**Outside-WordPress systems:**
- Follow Up Boss: Pixel, Connected Email, Company Number, Action Plans for 3 lead types
- IDX Broker: API key, dynamic wrapper, lead routing to FUB, custom subdomain
- Domain registrar: one CNAME record for `search.viewvegasnow.com`
- Google Search Console: domain verification, sitemap submission
- Google Analytics 4: install via GTM
- Google Business Profile: claim, verify, optimize, review requests

---

## Verification

You'll know it's working at three checkpoints:

**End of Phase 1 (Day 7):** Submit a test contact form on the live site. The lead appears in your Follow Up Boss inbox within 90 seconds. Visit the homepage and see live MLS listings refreshed daily. Search for a Las Vegas home in the header search bar and land on a styled results page. Tap the sticky button on your phone and your phone dialer opens to the FUB tracked number.

**End of Phase 2 (Day 21):** Submit a home valuation form. The lead lands in FUB tagged "Seller, Valuation Request" and triggers the comp-report follow-up automatically. Open Google Analytics and see events firing for every lead-capture action across the site. Read /buyers/, /sellers/, and /investors/ as a prospect would and confirm they answer real questions.

**End of Phase 3 (Day 90):** Search Google for "Summerlin homes for sale" or "first time home buyer Las Vegas" and find one of your pages in the results (page 1 to 3 by Day 90 is realistic). Open Google Search Console and see weekly impressions trending up. Open FUB and see the first 5 to 15 organic leads attributed to the website that month. Search ChatGPT for "best Las Vegas neighborhoods for families" and find your name or site cited.

---

## What You'll Be Asked to Do

- 90-minute kickoff call (Day 0)
- 30-minute walkthrough call at the end of each phase (3 total)
- Provide content for /buyers/, /sellers/, /investors/ in Week 2 (or opt in to writing add-on)
- Provide FUB Action Plan email and text copy in Week 3
- Decide on neighborhood pillar content approach in Week 3
- Approve backlink pitches before they go out in Phase 3
- Request Google reviews from 5 past clients in Week 1

Total time investment from you: roughly 30 to 50 hours across the 90 days, mostly in Phase 2 content writing.

---

## What Happens After Day 90

The site will be a working lead source. Some clients run their own maintenance from there. Others prefer ongoing support for monthly market reports, content production, backlink outreach, and SEO monitoring. We can discuss a Phase 4 maintenance retainer at the Day 90 final report if you'd like to keep momentum going.
