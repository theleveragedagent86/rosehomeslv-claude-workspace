/* ============================================================
   ROSE HOMES LV — COMPARATIVE MARKET ANALYSIS
   ------------------------------------------------------------
   THIS IS YOUR FILLABLE TEMPLATE.
   Edit the values below for each new client. Everything in the
   report rebuilds from this single object — addresses, comps,
   prices, photos, net-proceeds math, and the chart.

   Quick reference:
     • report.preparedFor / .date  → cover line + footer date
     • agent.*                     → cover card + every footer + closing
     • subject.*                   → cover, map, estimate, proceeds pages
     • comps[]                     → table, per-property pages, map pins,
                                     chart points, and all averages
     • pricing.*                   → estimate + recommended list price
     • proceeds.netLowPct/HighPct  → seller-nets band (you said 92–94%)
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
    headshot: "assets/ryan-main.jpg",   // swap per agent if needed
    closingNote:
      "Thank you for the opportunity to help you with your home. This analysis " +
      "reflects current Las Vegas Valley conditions and the most comparable nearby " +
      "sales, not a sales pitch. <b>When you're ready, the next step is a short, " +
      "no-pressure walk-through and a real number.</b>",
  },

  /* ---------- Subject property (the home being analyzed) ---------- */
  subject: {
    address: "1505 Sun Copper Dr",
    cityStateZip: "Las Vegas, NV 89117",
    beds: 5,
    baths: 3,
    sqft: 2960,
    lotSize: "6,098 Sqft",
    yearBuilt: 1996,
    garage: 2,
    photoSlot: "subject-hero",          // drop a hero photo here
    defaultPhoto: "assets/subject-1505-sun-copper.jpg", // baked-in example; a drop overrides it
    pin: { x: 41, y: 47 },              // position on the stylized map (%)
    blurb:
      "A five-bedroom, three-bath single-story-plus home in the established " +
      "89117 corridor, central to Summerlin, the 215, and Downtown. Priced " +
      "against six of the closest recent comparables below.",
  },

  /* ---------- Comparables (you asked for 6) ----------
     status: "Active" | "Pending" | "Sold"
     soldPrice / soldDate only apply to Sold (leave "" otherwise)
     ppsf is computed automatically if left null
     PHOTOS (optional, per comp — same pattern as subject.defaultPhoto):
       heroPhoto: "assets/comp-1-hero.jpg"   // main photo for this comp page
       gallery:   ["assets/comp-1-a.jpg", "assets/comp-1-b.jpg", "assets/comp-1-c.jpg"]
       Drop the image files into assets/ and point to them here. Any slot left
       without a path stays an editorial drop placeholder.                     */
  comps: [
    {
      address: "8981 Rivers Edge Dr", cityStateZip: "Las Vegas, NV 89117",
      type: "Single Family Home", status: "Active",
      beds: 3, baths: 2, sqft: 2162,
      listPrice: 798000, soldPrice: null, soldDate: "",
      dom: 3, mls: "2787822", lotSize: "5,662 Sqft", yearBuilt: 1994,
      garage: 2, hoa: "$450 / mo", ppsf: null,
      pin: { x: 22, y: 30 },
      description:
        "Beautifully renovated 3-bedroom, 2-bath single-story home with a versatile " +
        "den/flex space in the guard-gated Canyon Gate golf community. Over $100,000 " +
        "in improvements: spa-inspired bathrooms, a dramatic fireplace feature wall, " +
        "premium turf, new irrigation, landscape lighting, and an upgraded garage. The " +
        "private backyard enjoys the rare advantage of no rear and no front-facing neighbors.",
      features: {
        Interior: "Bedroom on Main Level, Ceiling Fan(s), Primary Downstairs, Paneling/Wainscoting",
        Utilities: "Electricity Available",
        Heating: "Central, Electric",
        Exterior: "Patio, Private Yard, Sprinkler/Irrigation",
      },
      photos: 6,
    },
    {
      address: "8964 Echo Ridge Dr", cityStateZip: "Las Vegas, NV 89117",
      type: "Single Family Home", status: "Active",
      beds: 3, baths: 2, sqft: 2473,
      listPrice: 724990, soldPrice: null, soldDate: "",
      dom: 4, mls: "2787894", lotSize: "6,098 Sqft", yearBuilt: 1994,
      garage: 2, hoa: "$450 / mo", ppsf: null,
      pin: { x: 30, y: 38 },
      description:
        "Single-story living in the guard-gated Canyon Gate Country Club. Over $120,000 " +
        "in upgrades: rich mahogany flooring, a new roof, new Trane HVAC, and paid-off " +
        "solar. The gourmet kitchen showcases quartz counters, custom cabinetry, high-end " +
        "stainless appliances, and dual ovens around a breakfast bar.",
      features: {
        Interior: "Bedroom on Main Level, Ceiling Fan(s), Primary Downstairs, Window Treatments, Programmable Thermostat",
        Utilities: "Cable Available, Underground Utilities",
        Heating: "Central, Gas, High Efficiency, Zoned",
        View: "Mountain(s)",
        Exterior: "Barbecue, Patio, Private Yard, Sprinkler/Irrigation",
      },
      photos: 6,
    },
    {
      address: "1605 Brocado Ln", cityStateZip: "Las Vegas, NV 89117",
      type: "Single Family Home", status: "Active",
      beds: 3, baths: 2, sqft: 1888,
      listPrice: 565000, soldPrice: null, soldDate: "",
      dom: 5, mls: "2786410", lotSize: "9,583 Sqft", yearBuilt: 1992,
      garage: 2, hoa: "None", ppsf: null,
      pin: { x: 36, y: 56 },
      description:
        "Move-in ready single-story on an oversized 9,500+ sqft lot with mature landscaping " +
        "and room for a pool. Updated kitchen and baths, open living areas, and a covered " +
        "patio built for Las Vegas evenings. No HOA.",
      features: {
        Interior: "Ceiling Fan(s), Primary Downstairs, Window Treatments",
        Utilities: "Electricity Available, Cable Available",
        Heating: "Central, Gas",
        Exterior: "Covered Patio, Private Yard, Sprinkler/Irrigation",
      },
      photos: 6,
    },
    {
      address: "9421 Crown Vista Ln", cityStateZip: "Las Vegas, NV 89117",
      type: "Single Family Home", status: "Pending",
      beds: 5, baths: 3, sqft: 3113,
      listPrice: 740000, soldPrice: null, soldDate: "",
      dom: 4, mls: "2785551", lotSize: "6,534 Sqft", yearBuilt: 1998,
      garage: 3, hoa: "$95 / mo", ppsf: null,
      pin: { x: 58, y: 44 },
      description:
        "Spacious two-story with five true bedrooms and a three-car garage, the closest " +
        "size-and-layout match to the subject. Formal living and dining, an open family room " +
        "off the kitchen, and a large primary suite. Went pending in under a week.",
      features: {
        Interior: "Bedroom on Main Level, Ceiling Fan(s), Window Treatments, Programmable Thermostat",
        Utilities: "Cable Available, Underground Utilities",
        Heating: "Central, Gas, Zoned",
        Exterior: "Patio, Private Yard, Sprinkler/Irrigation",
      },
      photos: 6,
    },
    {
      address: "9744 Lost Colt Cir", cityStateZip: "Las Vegas, NV 89117",
      type: "Single Family Home", status: "Sold",
      beds: 3, baths: 3, sqft: 2016,
      listPrice: 489000, soldPrice: 482000, soldDate: "Apr 2026",
      dom: 31, mls: "2779120", lotSize: "4,356 Sqft", yearBuilt: 1995,
      garage: 2, hoa: "$110 / mo", ppsf: null,
      pin: { x: 50, y: 60 },
      description:
        "Recently closed three-bedroom with a downstairs primary and a low-maintenance lot. " +
        "Sold close to ask after a month on market, a useful data point for realistic pricing " +
        "in the current rate environment.",
      features: {
        Interior: "Primary Downstairs, Ceiling Fan(s), Window Treatments",
        Utilities: "Cable Available",
        Heating: "Central, Gas",
        Exterior: "Patio, Sprinkler/Irrigation",
      },
      photos: 6,
    },
    {
      address: "7213 Pinedale Ave", cityStateZip: "Las Vegas, NV 89145",
      type: "Single Family Home", status: "Sold",
      beds: 4, baths: 2, sqft: 1519,
      listPrice: 389000, soldPrice: 380000, soldDate: "Mar 2026",
      dom: 18, mls: "2778685", lotSize: "6,534 Sqft", yearBuilt: 1989,
      garage: 2, hoa: "None", ppsf: null,
      pin: { x: 30, y: 70 },
      description:
        "Closed single-story in neighboring 89145 with a renovated kitchen, updated baths, " +
        "and a large backyard. A strong recent sold comp for the lower end of the range and " +
        "for buyers prioritizing single-level living.",
      features: {
        Interior: "Ceiling Fan(s), Window Treatments",
        Utilities: "Electricity Available",
        Heating: "Central, Electric",
        Exterior: "Private Yard, Sprinkler/Irrigation",
      },
      photos: 6,
    },
  ],

  /* ---------- Pricing / estimate ---------- */
  pricing: {
    estimatedValue: 570000,
    rangeLow: 512000,
    rangeHigh: 627000,
    recommendedList: 570000,
    // short rationale shown on the estimate page
    rationale:
      "The subject sits in the middle of the comparable set on size and condition. " +
      "We recommend listing at the estimated value to be the buyer's first call, " +
      "with room to hold firm given the limited single-story inventory in 89117.",
    expectedWindow: "21–35 days",
  },

  /* ---------- Estimated net proceeds ----------
     You said: seller nets ~92–94% of final sale price.
     The line items below are illustrative and sum to roughly the
     6–8% of costs implied by that band. Edit freely.            */
  proceeds: {
    salePrice: 570000,
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
     Ryan's real launch system, synthesized from the playbook. This is brand
     content, not per-client filler — keep as-is unless a seller's situation
     calls for changes. Drives the launch timeline, weekly strip, price rule,
     and communication promise on the Marketing page.                          */
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
