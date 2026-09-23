# The Transaction Folder

The structure behind the AI transaction coordinator I run on every deal. It is not fancy.
That is the point.

---

## The rule

**One folder per property. One file inside it that holds the facts. One separate folder that
holds the templates. Everything reads from those two places.**

If a date, a name or an email address exists in two places, one of them is already wrong.

---

## The two halves

Most agents try to build this as one thing and it collapses. It is two.

**Half one, the deals.** One folder per property. Facts only. Changes constantly.

**Half two, the system.** Templates, cadences, attachments. No client data in it at all.
Written once, reused on every file forever.

```
Transactions/                          <- half one, the deals
├── 123-Example-St/
│   ├── transaction.json               <- the single source of truth
│   ├── documents/                     <- executed contract, addenda, disclosures, reports
│   ├── day-0-emails.md                <- what went out the day it opened
│   └── calendar-invites/              <- .ics files for every deadline
├── 456-Sample-Ave/
│   ├── transaction.json
│   └── documents/
└── 789-Placeholder-Ln/
    └── transaction.json

transaction-coordination/              <- half two, the system
├── templates/
│   ├── buyer-resale.md
│   ├── buyer-new-construction.md
│   ├── seller.md
│   └── shared.md                      <- W9, home warranty, closeout, calendar invites
├── cadences/
│   ├── buyer-resale.json              <- 13 steps
│   ├── buyer-new-construction.json    <- 16 steps
│   └── seller.json
└── assets/
    ├── W9.pdf
    ├── Transaction-Intake-Form.pdf
    └── home-warranty-brochures/       <- all 4, always sent together

active-transactions.json               <- the index: which deals are open, and their COE
calendar.json                          <- every deadline across every deal, one file
```

Folder name is the address, slugged. No dates in the folder name, no "FINAL v3", no client
initials. The address is the only name that never changes.

`documents/` and `calendar-invites/` are optional. `transaction.json` is not.

---

## What goes in transaction.json

**Deal basics.** Address, slug, APN, type (buyer resale, buyer new construction, seller),
status, purchase price, loan amount, loan type, contract date, COE date.

**People, each with name, email and phone.** Buyer. Seller. Buyer agent. Listing agent, plus
their TC as its own entry. Escrow officer, with the team email, the escrow number and the
company. Lender. Inspector. Referring agent if there is one. Builder rep if it is new
construction.

**Financials.** Earnest money amount and how it was delivered, down payment, buyer broker
compensation, home warranty and who pays for it, fee splits.

**Dates, pulled straight off the executed contract.** This is the part that matters. My last
new build had **17 dated items** in this section:

| # | Deadline |
|---|---|
| 1 | Acceptance |
| 2 | Open escrow |
| 3 | Earnest money |
| 4 | Loan application |
| 5 | Preapproval letter |
| 6 | HOA resale package request |
| 7 | Utilities on |
| 8 | Seller disclosures |
| 9 | Due diligence |
| 10 | Appraisal contingency |
| 11 | PTR delivery |
| 12 | HOA cancellation right |
| 13 | Loan contingency |
| 14 | Seller vacate |
| 15 | Walkthrough window opens |
| 16 | Walkthrough window closes |
| 17 | Close of escrow |

**Progress.** Completed steps, triggered events, next step, next step date.

A blank copy of the file is included as `transaction-template.json`. Fill it in, delete the
`_README` and `_DATES_NOTE` lines, and you are running.

---

## The cadence file, the part people skip

A cadence is just a list of steps, and every step is one of two kinds.

**Day-based.** Fires on a day offset from acceptance.

```json
{
  "id": "day0-accepted-offer-email",
  "day": 0,
  "type": "email",
  "trigger": "day-based",
  "title": "Send Accepted Offer Email to Buyer",
  "template_ref": "buyer-resale:template-R1",
  "notes": "Send immediately after acceptance. CC referring agent if applicable."
}
```

**Event-based.** Fires when something happens that you cannot schedule.

```json
{
  "id": "escrow-intro-all-parties",
  "trigger": "event-based",
  "event": "escrow-info-received",
  "title": "Introduction Email to All Transaction Parties",
  "template_ref": "shared:intro-all-parties"
}
```

That second kind is the whole difference between a checklist and a system. A checklist
cannot know that escrow info just came in. A trigger can. My events are: buyer picks an
inspector, escrow info received, prelim title received, inspection date confirmed,
walkthrough confirmed, signing confirmed, recorded.

My buyer resale cadence is 13 steps. New construction is 16, because the builder adds an
escrow handoff and an orientation walkthrough.

**Date rule, do not skip this one.** Calendar days from acceptance count Day 1 as the day
*after* acceptance. Business days exclude weekends and federal holidays. Write the rule down
once, because you will get it wrong from memory at 9pm.

---

## How it actually runs

1. Contract gets executed. Make the folder, drop the PDF in `documents/`.
2. Claude reads the executed contract and the counters and fills `transaction.json` in one
   pass. Counters override the RPA, always read them second.
3. Every deadline in `contract_dates` becomes a calendar event immediately. All of them, at
   open. Not as they come up.
4. Every email after that reads the file first. Escrow opening, inspection options, appraisal
   update, clear to close. Right dates, right people copied, every time.
5. Step completes, it goes in `completed_steps` and `next_step` moves forward.

The CC list is part of the template, not something you remember. Listing agent and their TC
on every transaction email. Build it into the file so you never forget it at 9pm.

Follow-up rule that lives in the cadence file itself: never let more than one business day
pass on an open item.

---

## Where to start

Do not build this for a future deal. **Build it for the file you are most behind on right
now.** That one has the most missing information, so it is the one that pays you back
fastest.

Build half one first. One folder, one `transaction.json`, filled off the contract. Do not
touch templates until that exists, because templates with nothing to read from are just a
template pack, and you already have one of those.

The value is not deal one. It is deal two. The templates you write once run the next file
for free.

---

*Ryan Rose | The Leveraged Agent*
