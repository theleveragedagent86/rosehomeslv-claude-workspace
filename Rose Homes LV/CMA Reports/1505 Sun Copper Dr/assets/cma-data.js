/* ============================================================
   ROSE HOMES LV - COMPARATIVE MARKET ANALYSIS
   1505 Sun Copper Dr, Las Vegas, NV 89117
   ------------------------------------------------------------
   This report omits comparables by request. The listings map,
   comparables table, per-comp pages, and the $/sq ft chart are
   removed in cma-render.js (build()). comps[] is intentionally
   empty. Pricing is agent-recommended, not comp-derived.
   Subject data is sourced from MLS #2768628.
   ============================================================ */
window.CMA_DATA = {

  /* ---------- Report meta ---------- */
  report: {
    preparedFor: "The Owner of 1505 Sun Copper Dr",
    date: "June 2026",
    confidential: true,
  },

  /* ---------- Agent / brokerage (used on every page) ---------- */
  agent: {
    name: "Ryan Rose",
    title: "Real Estate Agent",
    license: "S.0185572",
    phone: "(702) 747-5921",
    email: "ryan@rosehomeslv.com",
    address: "9580 W Sahara Ave, Las Vegas, NV 89117",
    web: "rosehomeslv.com",
    brokerage: "Real Broker, LLC",
    headshot: "assets/ryan-main.jpg",
    closingNote:
      "Thank you for the opportunity to help you with your home. This analysis " +
      "reflects current Las Vegas Valley conditions and where your home sits in " +
      "today's market, not a sales pitch. <b>When you're ready, the next step is a " +
      "short, no-pressure walk-through and a real number.</b>",
  },

  /* ---------- Subject property (MLS #2768628) ---------- */
  subject: {
    address: "1505 Sun Copper Dr",
    cityStateZip: "Las Vegas, NV 89117",
    beds: 5,
    baths: 3,
    sqft: 2960,
    lotSize: "7,405 Sqft",
    yearBuilt: 1992,
    garage: 3,
    photoSlot: "subject-hero",
    defaultPhoto: "assets/subject-1505-sun-copper.jpg",
    pin: { x: 41, y: 47 },
    blurb:
      "A five-bedroom, three-bath two-story home in the guard-gated Sienna Ridge " +
      "enclave of Peccole Ranch, with a private pool and spa, fully owned solar, " +
      "and a three-car garage. This analysis sets a price from the home itself " +
      "and current market conditions.",
  },

  /* ---------- Comparables ----------
     Intentionally empty for this report. No comparable set was used,
     so the comp-dependent pages are omitted in cma-render.js.        */
  comps: [],

  /* ---------- Pricing / estimate (agent-recommended) ---------- */
  pricing: {
    estimatedValue: 785000,
    rangeLow: 770000,
    rangeHigh: 810000,
    recommendedList: 799999,
    rationale:
      "This price comes from the home itself, its size, condition, upgrades, " +
      "fully owned solar, pool and spa, and three-car garage, and from where the " +
      "89117 market sits today, not from a comparable set. At its earlier asking " +
      "prices the home drew limited activity across 71 days on market, which tells " +
      "us those numbers read high to buyers. Listing at $799,999, just under the " +
      "round number, positions it as a clear value in its size range and supports " +
      "a sale near $785,000. We expect to find the right buyer in about three to " +
      "five weeks at this price.",
    expectedWindow: "21 to 35 days",
  },

  /* ---------- Estimated net proceeds ----------
     Seller nets ~92 to 94% of final sale price. Line items below are
     illustrative and sum to roughly the 6 to 8% of costs implied by
     that band. Net is shown at the expected sale price of $785,000.  */
  proceeds: {
    salePrice: 785000,
    netLowPct: 92,
    netHighPct: 94,
    costs: [
      { label: "Total real estate commission", note: "Listing + buyer side", pct: 5.0 },
      { label: "Title & escrow", note: "Owner's policy + escrow fee", pct: 0.9 },
      { label: "Transfer tax & recording", note: "Nevada RPTT + county", pct: 0.5 },
      { label: "Seller concessions / misc.", note: "Repairs, home warranty, fees", pct: 0.6 },
    ],
    note:
      "Estimates only. Final proceeds depend on payoff balances, closing date, " +
      "negotiated concessions, and prorations. Mortgage payoff is not included.",
  },

  /* ---------- Marketing action plan (from the Listing Launch Playbook) ----------
     Ryan's real launch system, synthesized from the Ultimate Listing Launch
     Marketing Playbook (Phase 3 launch + Phase 4 active listing, pages 17-20).
     Brand content, kept as the template ships it. Drives the launch timeline,
     weekly strip, price rule, and communication promise on the Marketing page.  */
  marketing: {
    launchDay: [
      { time: "7:00",  label: "Go live on the MLS",          note: "Status to Active; photos, tour, and lockbox verified" },
      { time: "7:30",  label: "\"Just Listed\" email blast",  note: "Full database, with photos, price, and tour link" },
      { time: "8:00",  label: "Social launch blitz",          note: "Reel and carousel across Instagram, Facebook, TikTok, YouTube" },
      { time: "8:30",  label: "Boost paid campaigns",         note: "Promote the strongest post through launch week" },
      { time: "9:00",  label: "Agent-to-agent outreach",      note: "Personal texts to 30 to 50 active buyer agents" },
      { time: "10:00", label: "Sphere texts",                 note: "20 to 30 neighbors and past clients near the home" },
      { time: "11:00", label: "\"Just Listed\" mail drop",    note: "300 surrounding homes" },
      { time: "5:00",  label: "Engagement sweep",             note: "Reply to every comment, DM, and inquiry" },
    ],
    weekTag: "",  // hidden: a weekly-hours figure can read as a negative
    weeklyCadence: [
      { day: "Mon", icon: "phone",       act: "Follow-ups and video thank-yous", hrs: "1.5h" },
      { day: "Tue", icon: "trending-up", act: "Social posts and engagement",     hrs: "45m" },
      { day: "Wed", icon: "handshake",   act: "Sphere and broker outreach",      hrs: "2h" },
      { day: "Thu", icon: "mail",        act: "Deal of the Week and postcards",  hrs: "1.5h" },
      { day: "Fri", icon: "home",        act: "Door-knock open-house invites",   hrs: "3h" },
      { day: "Sat", icon: "key",         act: "Open house and lead capture",     hrs: "4h" },
      { day: "Sun", icon: "camera",      act: "Batch next week's content",       hrs: "2h" },
    ],
    priceRule: {
      title: "The 10·10·0 Price Rule",
      rules: [
        { n: "10", text: "days with no showings, we revisit the price (a 3 to 5% move)" },
        { n: "10", text: "showings with no offers, we review feedback and adjust strategy" },
        { n: "0",  text: "delay after any change; we relaunch as a brand-new listing" },
      ],
    },
    communication: {
      title: "You'll Always Know",
      items: [
        { icon: "mail",      text: "A written update every Monday: showings, views, ad metrics, feedback" },
        { icon: "phone",     text: "A text the moment a showing happens at your home" },
        { icon: "handshake", text: "A strategy review every two weeks, in person or on video" },
      ],
    },
  },

  /* ---------- The value of an agent (stats) ---------- */
  agentValue: [
    { icon: "briefcase", title: "Experience", stat: "92%", text: "of U.S. homes are sold with an agent or broker." },
    { icon: "handshake", title: "Trusted", stat: "90%", text: "of buyers would use their agent again or recommend them." },
    { icon: "trending-up", title: "Profit", stat: "+40%", text: "more on average versus selling for-sale-by-owner." },
    { icon: "clock", title: "Faster", stat: "20 days", text: "quicker to sell with an agent than FSBO." },
  ],
};
