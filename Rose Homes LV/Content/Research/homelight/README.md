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

## Status

Complete. Every HomeLight-required column is filled on all nine rows. Ryan supplied
the original list prices and the missing sides on 2026-09-23.

**29 Amber Rock is entered as Both, not Buyer.** Ryan's "buyer side for all" answered
a question about three other deals. `Clients/Transactions/29-Amber-Rock-St/transaction.json`
records Amber Rock as dual agency, "Ryan represents both buyer and seller in this
transaction." Change it to Buyer only if that note is wrong.

**The two builder deals still cannot be verified** against an MLS production report,
because they were never listed. 3550 All Hallows and 659 Semitone may be rejected on
that basis, which is a HomeLight decision, not a data problem.

## Two things to know about the data

**LISTING DATE is real on the seven MLS rows.** It was pulled from the Cross Property
Agent Full DETAIL report (`~/Downloads/Agent_Full_DETAIL1223.pdf`), which carries an
explicit List Date per property. An earlier version of this file derived those dates as
close date minus DOM, and every one of them was wrong by two to six weeks, because DOM
does not count every day a listing sits. Do not reintroduce that shortcut.

The two builder deals still have no listing, so their purchase agreement dates stand in:
2026-03-21 for All Hallows, 2026-08-12 for Semitone.

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
