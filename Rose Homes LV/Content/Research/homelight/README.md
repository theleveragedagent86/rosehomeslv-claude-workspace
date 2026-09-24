# HomeLight transaction upload, September 23, 2026

`homelight-transactions-2026-09-23.csv` is formatted to HomeLight's own template
(`~/Downloads/homelight_agent_transaction_upload_format.csv`). It is NOT ready to
upload yet. Two columns are still incomplete, see below.

## Where the rows came from

Ryan's MLS production report, pulled 2026-09-23, listed 11 transactions. Four were
rentals (P. Type `RNT`): 9975 Peace Way #2165, 1416 Santa Margarita St #A, 2927
Sapphire Sands Ct, 6250 W Arby Ave #184. HomeLight's upload checklist takes
residential SALES only, so those four are dropped. That leaves seven.

Two more come from Ryan's own transaction files and are NOT in the MLS report,
because they are builder new construction: 3550 All Hallows Ave (Pulte, closed
2026-05-21) and 659 Semitone Ln (Taylor Morrison, closed 2026-09-23, same day as
the report). They will not verify against an MLS production report. Keep them or
drop them, but know that going in.

Total: 9 rows.

## What is still missing

**ORIGINAL LISTING PRICE is blank on every row and HomeLight marks it REQUIRED.**
It is not in the production report Ryan exported. It has to come from the MLS, or
be filled from memory per deal.

**REPRESENTING is blank on three rows.** The production report does not say which
side Ryan was on, and these three have no local transaction file:

- 3780 Territory St, closed 2025-12-15, $425,000
- 146 Samantha Rose St, closed 2025-12-08, $405,000
- 1275 White Dr, closed 2025-09-19, $461,000

The other six sides are known from the transaction files: Moapa Water, Tardando
and Robin Knot are buyer side, Amber Rock is dual agency (Both), and the two new
construction deals are buyer side.

## Two things to know about the data

**LISTING DATE is derived, not reported.** It is close date minus DOM. That is a
close approximation, not the MLS list date, because DOM does not count every day a
listing sits. Confirm before upload if HomeLight is strict about it.

**29 Amber Rock St has a price conflict.** The MLS says $457,000 closed 5/29/2026.
`Clients/Transactions/29-Amber-Rock-St/transaction.json` says $475,000 with a COE
of 2026-06-01, and a list price of $485,000. The CSV uses the MLS figure, since
that is what HomeLight verifies against. The transaction file may have a
transposition, 457 and 475, and is worth a look either way.

## Verification, the other half of the upload

HomeLight will not count these toward referral ranking without proof. They want a
link to the MLS site or a PDF or screenshot of the production report. Ryan has the
report, it just needs to be saved as a PDF and uploaded alongside the CSV.
