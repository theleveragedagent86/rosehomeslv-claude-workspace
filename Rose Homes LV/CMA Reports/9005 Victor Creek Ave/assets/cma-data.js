/* ============================================================
   ROSE HOMES LV — COMPARATIVE MARKET ANALYSIS
   ------------------------------------------------------------
   Subject: 9005 Victor Creek Ave, Las Vegas, NV 89149
   Comps:   6 nearby homes from the MLS Agent Full Detail
            (1 sold, 3 active, 1 expired, 1 withdrawn)
   Subject facts sourced from the Zillow property record.
   ============================================================ */
window.CMA_DATA = {

  /* ---------- Report meta ---------- */
  report: {
    preparedFor: "The Owner of 9005 Victor Creek Ave",
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
      "reflects current Las Vegas Valley conditions and the most comparable nearby " +
      "sales, not a sales pitch. <b>When you're ready, the next step is a short, " +
      "no-pressure walk-through and a real number.</b>",
  },

  /* ---------- Subject property (the home being analyzed) ---------- */
  subject: {
    address: "9005 Victor Creek Ave",
    cityStateZip: "Las Vegas, NV 89149",
    beds: 3,
    baths: 2.5,
    sqft: 1988,
    lotSize: "3,484 Sqft",
    yearBuilt: 2007,
    garage: 2,
    photoSlot: "subject-hero",
    defaultPhoto: "assets/subject-9005-victor-creek.jpg",
    pin: { x: 41, y: 47 },
    blurb:
      "A three-bedroom home in the Clare Ridge neighborhood off Centennial Parkway, " +
      "built in 2007. At 1,988 square feet it is the largest floor plan in this " +
      "comparable set, with more living space than every nearby home that recently " +
      "sold or is now on the market. Priced against the six closest comparables below.",
  },

  /* ---------- Comparables ----------
     Ordered: the one recent sale first (the anchor), then the active
     competition, then the two homes that did not sell. Status text shows
     exactly as listed; Expired and Withdrawn render in neutral styling.   */
  comps: [
    {
      address: "8949 Ryan Creek Ave", cityStateZip: "Las Vegas, NV 89149",
      type: "Single Family Home", status: "Sold",
      beds: 3, baths: 3, sqft: 1830,
      listPrice: 385000, soldPrice: 391500, soldDate: "May 2026",
      dom: 22, mls: "2771367", lotSize: "3,485 Sqft", yearBuilt: 2006,
      garage: 2, hoa: "$50 / mo", ppsf: null,
      pin: { x: 22, y: 30 },
      description:
        "The one home in this set that actually sold, and the closest size match to yours. " +
        "It closed in May 2026 at $391,500, about $214 a square foot, and sold above its " +
        "$385,000 list price after only 22 days. An open two-story plan with a high entry " +
        "foyer, a large living room, a separate family room, a kitchen with a center island, " +
        "an upstairs loft, and a primary suite with two walk-in closets.",
      features: {
        Interior: "Two stories, upstairs loft, primary suite with two walk-in closets, ceiling fans",
        Kitchen: "Large kitchen with center island",
        Heating: "Central, gas",
        Exterior: "Desert landscaping, fully fenced backyard, back yard access",
      },
    },
    {
      address: "9069 Amanda Creek Ct", cityStateZip: "Las Vegas, NV 89149",
      type: "Single Family Home", status: "Active",
      beds: 3, baths: 3, sqft: 1830,
      listPrice: 415000, soldPrice: null, soldDate: "",
      dom: 15, mls: "2789115", lotSize: "3,485 Sqft", yearBuilt: 2007,
      garage: 2, hoa: "$50 / mo", ppsf: null,
      pin: { x: 30, y: 38 },
      description:
        "A fresh active listing the same size as the recent sale, currently asking $415,000, " +
        "or $227 a square foot. Recently repainted throughout, with a stainless steel kitchen " +
        "island, a primary walk-in closet, double sinks in the primary bath, and a covered " +
        "patio leading to a fully fenced backyard. Vacant and easy to show.",
      features: {
        Interior: "Fresh interior paint, primary walk-in closet, alarm system owned",
        Kitchen: "Stainless steel appliances, functional island",
        Heating: "Central, gas",
        Exterior: "Covered patio, fully fenced backyard, desert landscaping",
      },
    },
    {
      address: "6513 Delicate Petal Ct", cityStateZip: "Las Vegas, NV 89149",
      type: "Single Family Home", status: "Active",
      beds: 3, baths: 3, sqft: 1799,
      listPrice: 415000, soldPrice: null, soldDate: "",
      dom: 28, mls: "2785439", lotSize: "3,485 Sqft", yearBuilt: 2007,
      garage: 2, hoa: "$50 / mo", ppsf: null,
      pin: { x: 36, y: 56 },
      description:
        "An active listing on a premium corner cul-de-sac lot with no rear neighbors, asking " +
        "$415,000, or $231 a square foot. Open floor plan with a flexible front room, an " +
        "upstairs tech area, a primary suite with a large walk-in closet and dual sinks, and a " +
        "low-maintenance backyard with synthetic grass, a covered patio, and a tall privacy wall.",
      features: {
        Interior: "Open floor plan, upstairs tech area, primary walk-in closet, dual sinks",
        Lot: "Premium corner lot, cul-de-sac, no rear neighbors",
        Heating: "Central, gas",
        Exterior: "Covered patio, synthetic grass, tall perimeter wall, extended driveway",
      },
    },
    {
      address: "8944 Ryan Creek Ave", cityStateZip: "Las Vegas, NV 89149",
      type: "Single Family Home", status: "Active",
      beds: 3, baths: 3, sqft: 1830,
      listPrice: 424900, soldPrice: null, soldDate: "",
      dom: 111, mls: "2760392", lotSize: "3,485 Sqft", yearBuilt: 2006,
      garage: 2, hoa: "$60 / mo", ppsf: null,
      pin: { x: 58, y: 44 },
      description:
        "An active listing the same size as the recent sale but asking $424,900, or $232 a " +
        "square foot. It has been on the market 111 days without selling, a sign the price is " +
        "ahead of what buyers are paying. The home has a separate family room, a kitchen with " +
        "granite, a center island and stainless steel appliances, an upstairs loft, and a " +
        "primary suite with two walk-in closets.",
      features: {
        Interior: "Upstairs loft, separate family room, primary with two walk-in closets, ceiling fans",
        Kitchen: "Granite counters, center island, stainless steel appliances",
        Heating: "Central, gas",
        Exterior: "Low-maintenance rear yard, fully fenced, private yard",
      },
    },
    {
      address: "9111 Brilliant Prairie Ct", cityStateZip: "Las Vegas, NV 89149",
      type: "Single Family Home", status: "Expired",
      beds: 3, baths: 3, sqft: 1610,
      listPrice: 430000, soldPrice: null, soldDate: "",
      dom: 127, mls: "2750811", lotSize: "3,485 Sqft", yearBuilt: 2007,
      garage: 2, hoa: "$55 / mo", ppsf: null,
      pin: { x: 50, y: 60 },
      description:
        "A cautionary data point. This is the smallest home in the set at 1,610 square feet, yet " +
        "it carried the highest asking price per square foot at $267, listed at $430,000. It " +
        "expired after 127 days without selling. A well-kept home with a private courtyard entry, " +
        "granite counters, a breakfast bar, an oversized primary suite, and a covered patio with " +
        "a gazebo, but the price was simply too high for the market.",
      features: {
        Interior: "Private courtyard entry, oversized primary suite, walk-in closets, ceiling fans",
        Kitchen: "Granite countertops, breakfast bar",
        Heating: "Central, gas",
        Exterior: "Covered patio, gazebo, fully fenced backyard",
      },
    },
    {
      address: "9123 Grand Sunburst Ct", cityStateZip: "Las Vegas, NV 89149",
      type: "Single Family Home", status: "Withdrawn",
      beds: 3, baths: 3, sqft: 1800,
      listPrice: 440000, soldPrice: null, soldDate: "",
      dom: 43, mls: "2756985", lotSize: "3,485 Sqft", yearBuilt: 2006,
      garage: 2, hoa: "$50 / mo", ppsf: null,
      pin: { x: 30, y: 70 },
      description:
        "Another home that started high and did not sell. It opened at $445,000, dropped to " +
        "$440,000, or $244 a square foot, and was withdrawn after 43 days. A nicely finished " +
        "two-story with vaulted ceilings, a separate family room, custom cabinets, granite, a " +
        "center island, artificial turf, and a paver patio. It also carries a Tesla solar lease, " +
        "which not every buyer wants to take over.",
      features: {
        Interior: "Vaulted ceilings, formal living and dining, separate family room, custom cabinets",
        Kitchen: "Granite counters, center island, pendant lights, stainless steel appliances",
        Energy: "Tesla solar lease (PPA), low NV Energy bills",
        Exterior: "Artificial turf, paver patio, oversized garage, extended driveway",
      },
    },
  ],

  /* ---------- Pricing / estimate ---------- */
  pricing: {
    estimatedValue: 419900,
    rangeLow: 400000,
    rangeHigh: 425000,
    recommendedList: 419900,
    rationale:
      "The one home in this set that actually sold, 8949 Ryan Creek Avenue at 1,830 square feet, " +
      "closed in May 2026 at $391,500, about $214 a square foot, and it sold above its list price " +
      "in only 22 days. Your home offers roughly 160 more square feet than that sale. The two homes " +
      "that pushed to $430,000 and $440,000 did not sell: one expired after 127 days and the other " +
      "was withdrawn. Three smaller active homes sit between $415,000 and $424,900, and the $424,900 " +
      "listing has lingered 111 days. We recommend listing at $419,900, which places your larger home " +
      "just above the fresh competition and well clear of the prices that failed to sell. Final " +
      "positioning depends on condition: if the home shows superior to these comps, $424,900 is " +
      "supportable, and if it needs updates, $400,000 to $415,000 better fits current market conditions.",
    expectedWindow: "21–35 days",
  },

  /* ---------- Estimated net proceeds ----------
     Seller nets ~92–94% of final sale price; line items sum to ~7%.        */
  proceeds: {
    salePrice: 419900,
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

  /* ---------- Marketing action plan (from the Listing Launch Playbook) ---------- */
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
