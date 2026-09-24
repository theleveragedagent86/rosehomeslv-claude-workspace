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

Ryan supplied original list prices and the missing sides on 2026-09-23, so the
seven MLS rows are complete.

**The two new construction rows have no ORIGINAL LISTING PRICE**, which HomeLight
marks REQUIRED. 3550 All Hallows and 659 Semitone were never listed in the MLS, so
no original list price exists for them. Either supply the builder's pre-discount
contract price, or drop those two rows. They also cannot be verified against a
production report, for the same reason.

**29 Amber Rock is entered as Both, not Buyer.** Ryan said buyer side for the three
unknowns, and Amber Rock was not one of them:
`Clients/Transactions/29-Amber-Rock-St/transaction.json` records it as dual agency,
"Ryan represents both buyer and seller in this transaction." Change it to Buyer only
if that note is wrong.

## Two things to know about the data

**LISTING DATE is derived, not reported.** It is close date minus DOM. That is a
close approximation, not the MLS list date, because DOM does not count every day a
listing sits. Confirm before upload if HomeLight is strict about it.

**29 Amber Rock St has a price conflict.** The MLS says $457,000 closed 5/29/2026.
`Clients/Transactions/29-Amber-Rock-St/transaction.json` says $475,000 with a COE of
2026-06-01. Both agree the original list price was $485,000, which is the figure the
production report confirmed, so the transaction file is right about the listing and
looks wrong about the close. The CSV uses the MLS figure, since that is what
HomeLight verifies against. Worth correcting the transaction file.

## Verification, the other half of the upload

HomeLight will not count these toward referral ranking without proof. They want a
link to the MLS site or a PDF or screenshot of the production report. Ryan has the
report, it just needs to be saved as a PDF and uploaded alongside the CSV.
