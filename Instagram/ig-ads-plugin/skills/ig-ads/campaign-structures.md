# Campaign Structures & Targeting Reference

Reference for the Ads Strategist agent. Covers campaign structures, audience targeting, and Meta best practices.

---

## Campaign Hierarchy

```
Campaign (1 per effort)
  └── Ad Set (1-2 per campaign, defines audience + budget)
       └── Ads (2-5 variations per ad set, Meta optimizes delivery)
```

### When to Use Multiple Ad Sets
- **Split testing audiences:** e.g., one ad set for local homeowners, another for out-of-state relocators
- **Different budgets for different audiences**
- **Usually 1 ad set is enough** for most listing and brand campaigns

### Number of Ad Variations to Recommend

| Campaign Type | Recommended Variations | Rationale |
|---------------|----------------------|-----------|
| Just Listed | 3-4 | Feature hook, lifestyle hook, urgency hook, open house hook |
| Just Sold | 2-3 | Results hook, social proof hook, neighbor hook |
| Brand Awareness | 2-3 | Local expert, market update, neighborhood spotlight |
| Buyer Lead Gen | 2-3 | First-time buyer, relocation, general buyer |
| Seller Lead Gen | 2 | Home value, results-driven |
| Listing Lead Form | 3-4 | Similar homes hook, alerts hook, lifestyle hook, price point hook |
| General/Topic | 2-3 | Depends on the topic angle variety |

---

## Objectives Guide

| Objective | When to Use | Optimization |
|-----------|-------------|--------------|
| **Traffic** | Drive people to listing page, website, or virtual tour | Link clicks or landing page views |
| **Leads** | Capture contact info via lead form or messenger | Lead form submissions |
| **Engagement** | Boost a post for visibility (rare, brand awareness only) | Post engagement |

**Default for this skill: Traffic or Leads.** Use Traffic for listing campaigns (drive to listing page). Use Leads for seller/buyer campaigns (capture contact info) and Listing Lead Form campaigns (capture buyer leads via Instant Form using the listing as the hook).

---

## Audience Targeting Presets

### IMPORTANT: Housing Special Ad Category Restrictions

All real estate ads MUST use the **Housing** Special Ad Category. This is a Meta legal requirement that restricts targeting:

- **NO age targeting** (cannot set min/max age)
- **NO gender targeting**
- **NO zip code targeting**
- **NO detailed interest or behavior targeting** (Meta removes most options)
- **Minimum 15-mile radius** for location targeting
- Lookalike audiences become "Special Ad Audiences" with limited similarity matching

**What you CAN do:** Location radius (15+ miles) and broad location targeting. That's essentially it. Meta's algorithm handles the rest through Advantage+ optimization.

### Listing Campaign — Just Listed (Default)
- **Special Ad Category:** Housing (REQUIRED)
- **Location:** 20-mile radius centered on downtown Las Vegas (89101). Do NOT center on the listing address — center on downtown LV to cover the full metro (Summerlin/89166, Enterprise/89178, Henderson, North Las Vegas).
- **All other targeting:** Advantage+ (let Meta optimize — Housing category removes most manual options)

### Listing Campaign — Just Sold
- **Special Ad Category:** Housing (REQUIRED)
- **Location:** 20-mile radius centered on downtown Las Vegas (89101). Same as Just Listed — always center on downtown LV, not the listing address.
- **All other targeting:** Advantage+ (same Housing restrictions apply)

### Brand Awareness / Community (Non-Housing)
*Only use this if the ad does NOT promote a specific listing or real estate services. Most real estate ads still require Housing category.*
- **Location:** Las Vegas metro area (25-mile radius from Las Vegas Strip or downtown)
- **Age:** 25-65
- **Interests:** Las Vegas living, Real estate investing, Home ownership, Las Vegas events
- **Behaviors:** Homeowners, Recent movers

### Listing Lead Form (Buyer Lead Capture from Listing)
- **Special Ad Category:** Housing (REQUIRED)
- **Location:** 20-mile radius centered on downtown Las Vegas (89101). Same targeting as Just Listed — covers Summerlin, 89178, Henderson, North LV.
- **All other targeting:** Advantage+ (Housing category restrictions)
- **Objective:** Leads (Instant Form)
- **Note:** Uses the listing as the hook but captures buyer leads interested in similar homes via Meta Instant Form. Week 2+ of listing launch, after initial Traffic ads have run.

### Buyer Lead Generation
- **Special Ad Category:** Housing (REQUIRED)
- **Location:** Las Vegas metro + feeder markets (Los Angeles, Phoenix, Seattle)
- **All other targeting:** Advantage+ (Housing category restrictions)

### Seller Lead Generation
- **Special Ad Category:** Housing (REQUIRED)
- **Location:** 20-mile radius centered on downtown Las Vegas (89101)
- **All other targeting:** Advantage+ (Housing category restrictions)

---

## Budget Recommendations

These are suggestions for the Ads Strategist to offer when the user asks for recommendations. The user always sets the final budget.

| Campaign Type | Suggested Daily | Suggested Duration | Estimated Reach |
|---------------|----------------|-------------------|-----------------|
| Just Listed | $15-30/day | 7-14 days | 5,000-15,000 |
| Just Sold | $10-20/day | 7-10 days | 5,000-12,000 |
| Open House | $20-40/day | 3-5 days | 3,000-10,000 |
| Brand Awareness | $10-20/day | 30 days ongoing | 10,000-30,000/mo |
| Lead Gen (Buyer/Seller) | $15-25/day | 14-30 days | 5,000-15,000 |
| Listing Lead Form | $15-25/day | 14-30 days | 5,000-15,000 |

---

## Ad Format Recommendations

| Format | Best For | Specs |
|--------|----------|-------|
| **Single Image** | Listing showcase, home value ads | 1080x1080 (1:1) or 1080x1350 (4:5) |
| **Carousel** | Multiple listing photos, feature highlights | 1080x1080 per card, 2-10 cards |
| **Video** | Virtual tours, neighborhood spotlights, personal brand | 1080x1920 (9:16) for Stories/Reels, 1080x1080 for Feed |

**Default recommendation:** Single image for most campaigns. Carousel if the user has 3+ strong listing photos. Video only if the user provides video content.

---

## CTA Button Types

| Button | When to Use |
|--------|-------------|
| **Learn More** | Listing pages, blog posts, neighborhood info |
| **Send Message** | Direct inquiries, "text me" campaigns |
| **Sign Up** | Lead forms, home value requests, newsletter |
| **Book Now** | Showing appointments (if booking link available) |
| **Get Directions** | Open house events |

---

## Meta Ad Policies — Key Rules

- **Text on images:** Keep under 20% of the image area. Meta may reduce delivery if too much text.
- **No misleading claims:** Don't promise specific ROI, home value appreciation, or guaranteed results.
- **Housing ads (Special Category):** Real estate ads are classified as Special Ad Category: Housing. This restricts targeting:
  - Cannot target by age, gender, or zip code in housing category
  - Must use a minimum 15-mile radius
  - Limited interest targeting
  - **This is automatically applied when "Housing" is selected as the special ad category. Always select it.**
- **No discriminatory content:** Cannot exclude audiences based on race, ethnicity, religion, etc.
- **Landing page must match ad:** The destination URL must be relevant to the ad content.

### Special Ad Category: Housing (CRITICAL)

When creating any real estate ad, the **Special Ad Category** must be set to **Housing**. This is a Meta requirement, not optional. The Ads Strategist must always include this in the campaign structure. In the browser automation, look for the "Special Ad Categories" section at the campaign level and select "Housing."

This restricts some targeting options but is legally required for real estate advertising.

---

## Instant Form Configuration (Listing Lead Form Campaigns)

When using the Leads objective with Instant Form, the form is created within the Ad level of the campaign. This section defines the default form setup for Listing Lead Form campaigns.

### Form Type
- **More Volume** (recommended) — shorter form, auto-fills from Facebook profile, higher completion rate
- **Higher Intent** — adds a review step before submission, lower volume but higher quality leads

### Default Form Fields
1. **Full Name** (auto-filled from Facebook)
2. **Email** (auto-filled from Facebook)
3. **Phone Number** (auto-filled from Facebook)

### Qualifying Questions (both included by default)

**Question 1: "When are you looking to buy?"**
- Type: Multiple choice
- Options: ASAP / 1-3 months / 3-6 months / Just browsing

**Question 2: "Are you pre-approved for a mortgage?"**
- Type: Multiple choice
- Options: Yes / No / Not yet

### Form Content
- **Form Headline:** "Find Similar Homes in [NEIGHBORHOOD]" or "Get [NEIGHBORHOOD] Home Alerts"
- **Form Description (1-2 sentences):** "Get new listings in [NEIGHBORHOOD] and surrounding areas sent directly to you. No spam, no pressure."
- **Privacy Policy URL:** `https://www.rosehomeslv.com/site/privacy-terms` (REQUIRED by Meta for lead forms)
- **Thank You Screen:**
  - Headline: "You're All Set!"
  - Description: "Ryan will send you matching listings within 24 hours. In the meantime, check out what's available now."
  - CTA Button: "View Website" → rosehomeslv.com (or listing landing page URL)

### Housing Special Ad Category — Form Restrictions
- Cannot ask about race, religion, ethnicity, national origin, disability, familial status, or sex
- Cannot ask about income directly (but "Are you pre-approved?" is acceptable)
- Keep custom questions focused on timeline and readiness, not demographics
