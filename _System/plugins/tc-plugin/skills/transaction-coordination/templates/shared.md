# Shared Templates — All Transaction Types

Templates used across buyer and seller transactions. No signature block — Ryan's Gmail signature is applied automatically.

---

## W9 to Builder/Escrow

**Subject:** `[PROPERTY ADDRESS] - W9`
**To:** `[BUILDER REP NAME]` at `[BUILDER REP EMAIL]` (or escrow officer)
**Attachment:** `Real Broker LLC W9 01-01-2026.pdf` (stored in `assets/`)
**Trigger:** Event — escrow officer info received (send alongside intro email)

Hi [RECIPIENT NAME],

Please see attached our brokerage's W9 for the transaction file.

Thank you,

---

## Home Warranty Options to Buyer (CANONICAL TEMPLATE)

**Subject:** `[PROPERTY ADDRESS] — Home Warranty Options`
**To:** `[BUYER NAME]` at `[BUYER EMAIL]`
**CC:** `[REFERRING AGENT NAME]` at `[REFERRING AGENT EMAIL]` (if applicable)
**Attachments:** All 4 brochures from `assets/home-warranty-brochures/`:
- `Old Republic HW.pdf`
- `American Home Shield.pdf`
- `FNHW.pdf`
- `CHW_Realty_Brochure_NA-2023.pdf`
**Trigger:** Day 0–2 — use whenever the contract includes a seller-paid Home Protection Plan / home warranty credit (resale buyer, and any new construction deal where the builder/seller is contributing to a buyer-choice warranty).

Hi [BUYER FIRST NAME],

Per your contract, the seller is providing up to $[WARRANTY CREDIT] toward a home warranty. Any unused portion of that $[WARRANTY CREDIT] goes back to the seller, so it's in your best interest to maximize this credit.

I've attached brochures from four home warranty companies that my clients have used. Please review them and let me know which company and plan you'd like to go with, and I'll take care of ordering it.

A few things to keep in mind:

- Multi-year plans are available if you'd like extended protection. This is a great way to use the full credit
- If the plan you choose costs less than $[WARRANTY CREDIT], the remaining balance goes back to the seller
- If the plan exceeds $[WARRANTY CREDIT], the difference would be your responsibility and handled through escrow at closing

The four options attached are:

1. Old Republic Home Warranty
2. American Home Shield
3. Fidelity National Home Warranty (FNHW)
4. Choice Home Warranty

Please take a look and let me know which company and plan works best for you.

> **CANONICAL — do not change.** This exact wording and these exact 4 brochures are the standard for every buyer transaction with a seller-paid home warranty credit. Only variables to fill are `[PROPERTY ADDRESS]`, `[BUYER FIRST NAME]`, and `[WARRANTY CREDIT]` (dollar amount from contract, no comma). Always attach all 4 PDFs from `assets/home-warranty-brochures/`. CC the referring agent when there is one on the transaction.

---

## Post-Recording Closeout Request to Escrow

**Subject:** `RE: WE ARE RECORDED // [ESCROW NUMBER] — [PROPERTY ADDRESS]` (reply to the escrow officer's "We Are Recorded" email)
**To:** `[ESCROW OFFICER NAME]` at `[ESCROW OFFICER EMAIL]`
**Trigger:** Event — `transaction-recorded` (escrow has confirmed recording). Send same day.

Hi [ESCROW OFFICER FIRST NAME],

Congratulations on closing! Can you please send both the "buyer side only" and "combined" final settlement statements along with proof of commission payment (copy of check or wire transfer confirmation) for our file? Buyer side to be sent to [BROKERAGE BACK OFFICE] as discussed.

Thank you!

> **Notes:**
> - `[BROKERAGE BACK OFFICE]` is typically "REAL/Urban Nest office" but adapt per the deal — confirm before sending.
> - On seller-side transactions, swap "buyer side only" for "seller side only" and update routing accordingly.
> - This email closes out Ryan's file. Wait until escrow confirms recording before sending (otherwise the wire/check won't exist yet). If the "We Are Recorded" email is more than 24 hours old and you still haven't received the final docs, send this as a fresh email — don't wait longer.

---

## Calendar Invite Templates

When a new transaction is created, **immediately generate all calendar events** based on the signed purchase contract dates. Add each to the daily checklist's `calendar.json`.

### Buyer-Side Events

| Event | Date Source | Title Format |
|-------|-----------|--------------|
| COE | Contract COE date | `COE — [PROPERTY ADDRESS]` |
| Earnest Money Deadline | Contract or COE - X days | `Earnest Money Due — [PROPERTY ADDRESS]` |
| Inspection Contingency Deadline | Contract | `Inspection Contingency Deadline — [PROPERTY ADDRESS]` |
| Due Diligence / Doc Review Deadline | Contract | `Due Diligence Deadline — [PROPERTY ADDRESS]` |
| Appraisal Contingency Deadline | Contract | `Appraisal Contingency Deadline — [PROPERTY ADDRESS]` |
| Loan Contingency Deadline | Contract | `Loan Contingency Deadline — [PROPERTY ADDRESS]` |
| HOA Doc Review Deadline | Contract (if applicable) | `HOA Review Deadline — [PROPERTY ADDRESS]` |
| Final Walkthrough | TBD (typically 1-2 days before COE) | `Final Walkthrough — [PROPERTY ADDRESS]` |
| Signing Appointment | TBD (once scheduled) | `Signing — [PROPERTY ADDRESS]` |

### Seller-Side Events

| Event | Date Source | Title Format |
|-------|-----------|--------------|
| COE | Contract COE date | `COE — [PROPERTY ADDRESS]` |
| Disclosure Delivery Deadline | Contract | `Disclosure Delivery Deadline — [PROPERTY ADDRESS]` |
| HOA Doc Delivery Deadline | Contract (if applicable) | `HOA Doc Delivery Deadline — [PROPERTY ADDRESS]` |
| Buyer Inspection Window | Contract | `Buyer Inspection Window — [PROPERTY ADDRESS]` |
| Repair Completion Deadline | Negotiated (if applicable) | `Repair Deadline — [PROPERTY ADDRESS]` |
| Final Walkthrough | TBD | `Final Walkthrough (be out) — [PROPERTY ADDRESS]` |
| Signing Appointment | TBD (once scheduled) | `Signing — [PROPERTY ADDRESS]` |

### New Construction Additions

| Event | Date Source | Title Format |
|-------|-----------|--------------|
| Builder Walkthrough / Orientation | TBD (builder schedules) | `Builder Walkthrough — [PROPERTY ADDRESS]` |
| Builder Punch List Deadline | TBD | `Punch List Deadline — [PROPERTY ADDRESS]` |
| Utility Transfer Reminder | COE - 5 days | `Transfer Utilities — [PROPERTY ADDRESS]` |

### Calendar Event JSON Format

```json
{
  "date": "[EVENT DATE]",
  "time": null,
  "title": "[EVENT TITLE] — [PROPERTY ADDRESS]",
  "location": "[PROPERTY ADDRESS or null]",
  "notes": "[BUYER/SELLER NAME] | [relevant details]",
  "transaction": "[ADDRESS-SLUG]",
  "type": "[event-type]"
}
```

**Event types:** `coe`, `earnest-money`, `contingency-deadline`, `inspection`, `appraisal`, `loan-contingency`, `hoa-review`, `walkthrough`, `signing`, `disclosure-deadline`, `repair-deadline`, `builder-walkthrough`, `punch-list`, `utility-transfer`

### How to Compute Dates

1. **If Ryan provides specific dates** from the contract — use those exactly
2. **If only COE is provided** — prompt Ryan for the key contingency dates, as Nevada contracts vary
3. **For TBD events** (walkthrough, signing, builder orientation) — create the event with `"date": "TBD"` and the skill will prompt to update when the date is known
4. **Utility transfer reminder** — auto-compute as COE minus 5 calendar days
