# Lead Follow-Up Sequence Reference

Complete 30-day multi-channel follow-up sequence for Listing Lead Form campaigns. Used by the ig-ads skill when creating Lofty Action Plans.

---

## Branching Logic (3 Tracks)

Qualifying questions from the Meta Instant Form determine the track:

| Track | Timeline Answer | Pre-Approved | Action Plan Name |
|-------|----------------|-------------|-----------------|
| **Hot** | ASAP or 1-3 months | Yes | `[Address] Follow-Up - Hot` |
| **Warm** | 1-3 or 3-6 months | Any | `[Address] Follow-Up - Warm` |
| **Nurture** | Just browsing | Any | `[Address] Follow-Up - Nurture` |

**Lead tags match the Action Plan name:** e.g., "29 Amber Rock - Hot", "29 Amber Rock - Warm", "29 Amber Rock - Nurture"

**Stop on reply:** All Action Plans MUST have "stop on reply" enabled. When a lead responds to any text, email, or answers a call, the automated sequence pauses and Ryan takes over personally.

---

## Template Variables

**Baked in at Action Plan creation time** (replaced with actual listing data):
- `{AREA}` — broader city/area: "Henderson", "Las Vegas", "Summerlin" (used Day 1+ for broader buyer interest)
- `{NEIGHBORHOOD}` — specific community: "Champion Village" (used Day 0 only to reference the listing they clicked)
- `{LISTING_FEATURE}` — standout feature: "that 3-car garage", "the resort-style backyard"
- `{PRICE}` — listing price or price range
- `{BEDS}` / `{BATHS}` — bed/bath count

**Lofty merge field** (auto-replaced per lead):
- `#lead_first_name#` — contact's first name

---

## Copy Guidelines

1. **NO em-dashes.** Use commas, periods, or "and" instead.
2. **Texts under 300 characters.** Keep them short — like texting a friend.
3. **Warm, personal, local.** Sound like Ryan texting from his phone, not a CRM bot.
4. **Value-first.** Every touch offers something useful — a listing, market data, a stat. Never just "checking in."
5. **Specific over generic.** Use real numbers, real neighborhoods, real features.
6. **Questions, not statements.** End texts with a question to invite a reply.
7. **No jargon.** No "pursuant to your inquiry" or "as your trusted advisor."

---

## The Sequence

### DAY 0 — Immediate (within minutes of lead sync)

**Touch 1 — Text (ALL TRACKS)**
Delay: Immediate
```
Hey #lead_first_name#, it's Ryan Rose. I saw you were checking out that home in {NEIGHBORHOOD}. Great taste. Are you looking for something similar or was there something specific about that one that caught your eye?
```

**Touch 2 — Email (ALL TRACKS)**
Delay: Immediate
Subject: `The {NEIGHBORHOOD} home you were looking at`
```
Hey #lead_first_name#,

Thanks for reaching out about the {BEDS}-bed in {NEIGHBORHOOD}. That one's getting a lot of attention and I totally see why. {LISTING_FEATURE} is hard to find at that price point.

I pulled a few things for you:
- There are several homes on the market in {AREA} right now in the {PRICE} range
- Things are moving fast. Homes in this area are going under contract quickly.
- I have a few options that hit the same marks as the one you saw

Want me to send those over? Just reply here or text me at 702-747-5921.

Ryan Rose
Real Broker, LLC
702-747-5921
rosehomeslv.com
```

**Touch 3 — Call Task (HOT ONLY)**
Delay: 30 minutes
Task note:
```
HOT LEAD. #lead_first_name# is ready to buy and pre-approved. Call now. They looked at the {NEIGHBORHOOD} listing ({BEDS}/{BATHS}, {PRICE}). Ask what caught their eye and if they want to see it or similar homes this week.
```

---

### DAY 1

**Touch 4 — Text (ALL TRACKS)**
Delay: 1 day, 10:00 AM
```
#lead_first_name#, I put together a quick list of homes in {AREA} that match what you were looking at. Want me to text you the link or email it over?
```

**Touch 5 — Voicemail Task (HOT + WARM)**
Delay: 1 day, 12:00 PM
Task note:
```
Send Slybroadcast voicemail to #lead_first_name#. Script: "Hey #lead_first_name#, it's Ryan Rose, local real estate agent here in Vegas. I saw you were checking out a home in {NEIGHBORHOOD} and I wanted to reach out personally. I've got a few options in {AREA} I think you'd really like. Give me a call back at 702-747-5921 or just reply to the text I sent you. Talk soon."
```

---

### DAY 2

**Touch 6 — Text (ALL TRACKS)**
Delay: 2 days, 9:00 AM
```
Quick update on {AREA}, #lead_first_name#. A couple new listings hit the market this week in your price range. Want me to send details?
```

**Touch 7 — Call Task (HOT + WARM)**
Delay: 2 days, 5:00 PM
Task note:
```
Follow-up call for #lead_first_name#. If no answer, leave a voicemail. Reference the {NEIGHBORHOOD} listing and the similar homes you've found in {AREA}. Ask if they'd like to tour this weekend.
```

---

### DAY 3

**Touch 8 — Email (ALL TRACKS)**
Delay: 3 days
Subject: `Homes in {AREA} you should see`
```
#lead_first_name#,

Wanted to follow up with some real numbers on the {AREA} market since you showed interest the other day.

Here's what I'm seeing right now:
- Several active listings in the {PRICE} range
- Homes are going under contract fast
- A couple new listings hit the market in the past week

I've already flagged a few that match what you were looking at. I can send you a curated list. Just say the word.

The best homes in this area go fast. I'd hate for you to miss one because you didn't know about it yet.

Ryan
702-747-5921
```

---

### DAY 4

**Touch 9 — Text (HOT + WARM)**
Delay: 4 days, 11:00 AM
```
#lead_first_name#, one of the homes I flagged in {AREA} just got a showing request. If you want to see it before offers come in, I can get us in this week. Want me to set it up?
```

**Touch 10 — Call Task (HOT ONLY)**
Delay: 4 days, 4:00 PM
Task note:
```
Third call attempt for #lead_first_name#. If still no contact, leave voicemail: "I've been trying to reach you about some homes in {AREA}. I have a few picked out. Text me back if that's easier, 702-747-5921."
```

---

### DAY 5

**Touch 11 — Text (ALL TRACKS)**
Delay: 5 days, 10:00 AM
```
No pressure at all, #lead_first_name#. But I found a home in {AREA} with {LISTING_FEATURE} that just listed under {PRICE}. Thought of you. Here if you want details.
```

---

### DAY 7

**Touch 12 — Email (ALL TRACKS)**
Delay: 7 days
Subject: `Weekly {AREA} market snapshot`
```
#lead_first_name#,

Quick weekly update on what's happening in {AREA}:

- New listings this week: several in your price range
- Homes going under contract quickly
- The market is active right now

I put these together every week for my buyers. If you want to keep getting them, just reply "yes" and I'll add you to the list. No spam, just real market intel.

Ryan
702-747-5921
```

**Touch 13 — Call Task (ALL TRACKS)**
Delay: 7 days, 2:00 PM
Task note:
```
Week 1 check-in call for #lead_first_name#. Be direct: "Hey #lead_first_name#, I wanted to make sure you got the listings I sent. Did any of them look interesting?" If no answer, leave voicemail with the same message.
```

---

### DAY 10

**Touch 14 — Text (ALL TRACKS)**
Delay: 10 days, 9:30 AM
```
Hey #lead_first_name#, heads up. A home in {AREA} went under contract yesterday at {PRICE}. The market's competitive right now. If you're still looking, I can set you up with instant alerts so you see new listings before most buyers do.
```

---

### DAY 14

**Touch 15 — Email (ALL TRACKS)**
Delay: 14 days
Subject: `Honest question, #lead_first_name#`
```
#lead_first_name#,

I've sent a few messages and I want to be respectful of your time. So here's an honest question:

Are you still interested in finding a home in {AREA}?

If yes, great. I'll keep sending you relevant listings and market updates.
If the timing isn't right, totally fine. Just let me know and I'll check back in a few months instead.

Either way, no pressure. I'm here when you're ready.

Ryan
702-747-5921
```

**Touch 16 — Call Task (ALL TRACKS)**
Delay: 14 days, 3:00 PM
Task note:
```
"Check-in or close-out" call for #lead_first_name#. Goal: get a response one way or another. If they answer: ask where they are in the process. If voicemail: "Hey, it's Ryan. Sent you a few listings in {AREA}. Just want to make sure I'm sending the right stuff. Text me back when you get a sec, 702-747-5921."
```

---

### DAY 18

**Touch 17 — Text (ALL TRACKS)**
Delay: 18 days, 10:00 AM
```
#lead_first_name#, new listing alert for {AREA}: {BEDS} bed / {BATHS} bath, {LISTING_FEATURE}, listed at {PRICE}. Want the full details?
```

---

### DAY 21

**Touch 18 — Email (ALL TRACKS)**
Delay: 21 days
Subject: `{AREA} price trends you should know about`
```
#lead_first_name#,

Whether you're buying now or later, this is worth knowing:

Home prices in {AREA} have been active lately. Here's the snapshot:
- The market is competitive with multiple offers on well-priced homes
- Homes with features like {LISTING_FEATURE} are especially popular
- Timing matters. The longer you wait, the more competition you'll face

I keep a close eye on this stuff because timing matters more than most people realize. If you ever want to hop on a quick call about your options, I'm here.

Ryan
702-747-5921
```

**Touch 19 — Call Task (WARM ONLY)**
Delay: 21 days, 4:00 PM
Task note:
```
Three-week check-in for warm lead #lead_first_name#. Goal: determine if timeline has changed. "Hey #lead_first_name#, just checking in on your home search. Have your plans changed at all since we last connected?"
```

---

### DAY 25

**Touch 20 — Text (ALL TRACKS)**
Delay: 25 days, 11:00 AM
```
Happy [DAY], #lead_first_name#. Just saw a price drop on a {BEDS}-bed in {AREA}. Now listed at {PRICE}. Want me to grab the details for you?
```

---

### DAY 30

**Touch 21 — Email (ALL TRACKS)**
Delay: 30 days
Subject: `Monthly {AREA} market report`
```
#lead_first_name#,

Here's your monthly snapshot of the {AREA} market:

- The market continues to be active
- Homes in your price range are moving
- Well-priced homes with strong features are getting multiple offers

Top insight: If you're thinking about buying in {AREA}, the spring and summer months tend to see the most inventory. That means more options for you, but also more competition.

I send these every month to my buyer network. If you're still keeping an eye on {AREA}, I'll keep them coming. If you're ready to start touring, just text me and we'll set something up.

Ryan Rose
Real Broker, LLC
702-747-5921
ryan@rosehomeslv.com
```

**Touch 22 — Text (ALL TRACKS)**
Delay: 30 days, 2:00 PM
```
#lead_first_name#, it's been about a month since you first reached out about {AREA}. Where are you at in your search? Still looking, or has anything changed?
```

---

## Post-Day-30: Monthly Nurture

After Day 30, leads that have not responded move to long-term monthly nurture. This continues until the lead responds, unsubscribes, or buys.

**Monthly Text (send around the 1st of each month):**
```
#lead_first_name#, quick {AREA} update: [INSERT TIMELY MARKET STAT OR NEW LISTING]. Keeping an eye out for you. Text me if anything changes on your end.
```

**Monthly Email:**
Subject: `{AREA} market update — [MONTH]`
```
#lead_first_name#,

Monthly {AREA} market snapshot:
- [2-3 bullet points with current market data]
- [One specific listing or trend worth noting]

Still here if you need anything. No pressure, just keeping you informed.

Ryan
702-747-5921
```

---

## Track Summary: Which Touches Apply

| Touch | Day | Channel | Hot | Warm | Nurture |
|-------|-----|---------|-----|------|---------|
| 1 | 0 | Text | X | X | X |
| 2 | 0 | Email | X | X | X |
| 3 | 0 | Call Task | X | | |
| 4 | 1 | Text | X | X | X |
| 5 | 1 | VM Task | X | X | |
| 6 | 2 | Text | X | X | X |
| 7 | 2 | Call Task | X | X | |
| 8 | 3 | Email | X | X | X |
| 9 | 4 | Text | X | X | |
| 10 | 4 | Call Task | X | | |
| 11 | 5 | Text | X | X | X |
| 12 | 7 | Email | X | X | X |
| 13 | 7 | Call Task | X | X | X |
| 14 | 10 | Text | X | X | X |
| 15 | 14 | Email | X | X | X |
| 16 | 14 | Call Task | X | X | X |
| 17 | 18 | Text | X | X | X |
| 18 | 21 | Email | X | X | X |
| 19 | 21 | Call Task | | X | |
| 20 | 25 | Text | X | X | X |
| 21 | 30 | Email | X | X | X |
| 22 | 30 | Text | X | X | X |

**Total touches:** Hot = 22, Warm = 19, Nurture = 15
