# Demo Email Automation — Property Management Tenant Inbox

## Purpose
Show Nick a LIVE working demo during the meeting. This is the "wow" moment. He sees his problem being solved in real-time.

---

## What the Demo Does

**Scenario:** A tenant sends an email to the property management inbox. The AI:

1. **Reads** the email and classifies it (maintenance, lease question, payment, complaint, general)
2. **Drafts** an appropriate response using the company's tone/templates
3. **Routes** urgent items (emergency maintenance) to the right person immediately
4. **Logs** the interaction for records
5. **Follows up** automatically if no response within X days

---

## Demo Script (What to Say While Showing It)

### Setup (30 seconds)
> "Let me show you exactly what this looks like in practice. I've built a working prototype of what your tenant email system could look like."

### Show Email #1 — Maintenance Request (60 seconds)
> "Here's a tenant emailing about a leaky faucet. Watch what happens..."
>
> - AI reads the email
> - Classifies it as: **Maintenance — Non-Emergency — Plumbing**
> - Drafts a response: acknowledges the issue, sets expectations ("our team will reach out within 24 hours"), asks for photos
> - Creates a maintenance ticket (or flags for your team)
> - Logs everything
>
> "That just saved someone 5-10 minutes per email. Multiply that by how many maintenance requests you get per week."

### Show Email #2 — Lease Question (60 seconds)
> "Now here's a tenant asking about their lease renewal terms..."
>
> - AI reads the email
> - Classifies it as: **Lease — Renewal Inquiry**
> - Pulls relevant lease info
> - Drafts a response with renewal terms, timeline, and next steps
> - Flags for your team if custom negotiation is needed
>
> "No one on your team had to touch this. The tenant gets a fast, professional answer."

### Show Email #3 — Urgent/Emergency (30 seconds)
> "Now watch what happens with an emergency..."
>
> - AI reads: "Water is flooding my apartment from the ceiling"
> - Classifies as: **Maintenance — EMERGENCY**
> - Immediately sends alert to on-call person (text/email)
> - Auto-responds to tenant: "Emergency received. Our team has been notified and will contact you within 15 minutes."
>
> "This is the one that saves you at 2am."

### Close the Demo (30 seconds)
> "Every email your team handles manually today — this system can draft, route, and follow up on automatically. Your team just reviews and approves. Instead of spending 2-3 hours a day in the inbox, they spend 15-20 minutes."

---

## How to Build This Demo in Claude Cowork

### Pre-Meeting Setup Checklist:
- [ ] Create a sample Gmail/Outlook inbox (or use your own for demo)
- [ ] Prepare 3-5 sample tenant emails (maintenance, lease, payment, emergency, general)
- [ ] Build the Claude Cowork automation that:
  - Reads incoming email
  - Classifies by category + urgency
  - Generates a draft reply
  - Outputs the classification + draft side by side

### Minimum Viable Demo:
You don't need a fully integrated system for the demo. You need:
1. **Input:** A real-looking tenant email (paste or forward it in)
2. **Process:** Claude reads, classifies, and drafts a response
3. **Output:** Show the classification + drafted response on screen

That's it. The "integration with his actual systems" is what he's paying you to build.

### Sample Tenant Emails for the Demo:

**Email 1 — Maintenance (Non-Emergency):**
```
Subject: Faucet leaking in kitchen
From: Sarah Johnson <tenant@email.com>

Hi,

The kitchen faucet in unit 204 at Sunset Apartments has been dripping
for the past two days. It's getting worse. Can someone come take a look?

Thanks,
Sarah
```

**Email 2 — Lease Question:**
```
Subject: Lease renewal question
From: Mike Chen <tenant@email.com>

Hello,

My lease at 1520 Desert Palm Dr, Unit 12 is up in 60 days. I'd like
to renew but wanted to know if there will be a rent increase and what
the new terms would be. Also, can I switch to a month-to-month?

Thanks,
Mike
```

**Email 3 — Emergency:**
```
Subject: URGENT - Water flooding apartment
From: Lisa Martinez <tenant@email.com>

HELP - Water is pouring from my ceiling in the master bedroom.
Unit 308, The Palms complex. It won't stop. I've put towels down
but it's getting worse. Please send someone ASAP!!

Lisa
```

**Email 4 — Payment Question:**
```
Subject: Payment question
From: James Wright <tenant@email.com>

Hi there,

I sent my rent payment on the 3rd through the portal but it's still
showing as unpaid. Can you check on this? I have the confirmation
number if needed.

James - Unit 115
```

**Email 5 — General Inquiry:**
```
Subject: Guest parking
From: Amy Torres <tenant@email.com>

Quick question — where can my guests park when they visit? I just
moved in last week and haven't figured out the parking situation yet.
Unit 410.

Thanks!
Amy
```

---

## Expected AI Output Format (What Nick Sees on Screen):

```
============================================
INCOMING EMAIL ANALYSIS
============================================

FROM: Sarah Johnson (tenant@email.com)
SUBJECT: Faucet leaking in kitchen
PROPERTY: Sunset Apartments, Unit 204

CLASSIFICATION: Maintenance
URGENCY: Non-Emergency
CATEGORY: Plumbing
PRIORITY: Medium

============================================
DRAFTED RESPONSE:
============================================

Hi Sarah,

Thank you for letting us know about the kitchen faucet in Unit 204.
We've logged this as a maintenance request and our plumbing team will
reach out to you within 24 hours to schedule a repair.

In the meantime, if you're able to send a quick photo of the faucet,
that helps our team come prepared with the right parts.

If the leak worsens or becomes an emergency, please call our
emergency line at [PHONE].

Best regards,
[Property Management Team Name]

============================================
ACTIONS TAKEN:
============================================
[x] Email classified and logged
[x] Maintenance ticket created — Plumbing, Non-Emergency
[x] Response drafted (awaiting team approval)
[ ] Follow-up scheduled: 48 hours if no resolution
```

---

## Pro Tips for the Demo:

1. **Use HIS property names** if you know them — makes it feel real, not generic
2. **Let him pick an email to test** — "give me a real email your team got this week" (ultimate power move)
3. **Show speed** — time it. "That took 4 seconds. How long does your team take?"
4. **Don't oversell perfection** — say "the draft is 90% there, your team just reviews and hits send. You stay in control."
5. **Show the emergency routing** — this is emotional. Property managers DREAD the 2am emergency. This sells itself.
