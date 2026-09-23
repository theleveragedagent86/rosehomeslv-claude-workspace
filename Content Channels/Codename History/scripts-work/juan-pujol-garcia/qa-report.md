# QA Report (Pass 2, revised script): Hitler Gave This Fake Spy A Medal (Juan Pujol Garcia / Agent GARBO)

**Script reviewed:** `script.md`, revised, 469 lines
**Scope of this pass:** confirm the 11 corrections from Pass 1 landed with the exact wording specified, confirm the edits broke nothing, and scan for new factual error introduced by the edits. Items marked VERIFIED in Pass 1 were not re-litigated.

**Pass 1 result:** FAIL, 4 WRONG claims, 11 corrections issued.
**Pass 2 result:** all 11 corrections landed. All narration is now clean. Three internal-documentation lines were left stale by the edits and now contradict the corrected narration, one of which is a standing instruction to production to reinstate an unverified detail.

---

## 1. Correction-by-correction confirmation

| # | Correction | Line | Landed? |
|---|---|---|---|
| 1 | Act 3, "listing exactly what he used as sources" to "naming three of the sources he used" | 112 | YES, exact wording |
| 1b | PRODUCTION NOTES, "Lisbon reference material is exactly three items" to "given as three named items from the memo, not as an exhaustive list" | 394 | YES, exact wording |
| 2 | Act 6, "Roughly two thousand four hundred fell at Omaha alone" to "Roughly two thousand four hundred of those casualties were at Omaha alone" | 264 | YES, exact wording |
| 3 | Act 6, "more than any other single source" to "more than from any other agent" | 294 | YES, exact wording |
| 4 | Act 7, "roughly fifty seven thousand houses" to "about fifty four thousand houses were damaged and more than two hundred people were killed" | 316 | YES, exact wording |
| 4b | FACT-CHECK LOG V-1 line updated to 54,000 damaged, over 200 killed, English Heritage and Forces War Records | 438 | YES |
| 5 | Act 3 VISUAL, ship count dropped | 130 | YES, exact wording |
| 6 | Act 4, "a Royal Air Force non-commissioned officer" to "a man in the Royal Air Force" | 172 | YES, exact wording |
| 7 | Act 8 VISUAL, shop replaced with "A quiet street in Venezuela. Pujol, older, walking home with a bag of shopping, entirely unremarkable." | 352 | YES, exact wording |
| 8 | Act 8, "That May," to "He came to London, and" | 358 | YES, exact wording |
| 9 | SOURCES, IWM V-Weapons URL swapped to `/history/the-terrifying-german-revenge-weapons-of-the-second-world-war` | 458 | YES |
| 10 | SOURCES, Harris book reference changed from "(TNA KV 2/42)" to "(Public Record Office, intro. Mark Seaman)" | 469 | YES |
| 11 | SOURCES, English Heritage "The First Flying Bomb of London" added | 462 | YES |

The retained "TNA KV 2/41 and KV 2/42" on the Hubbard-Hall line (463) and in the Araceli FACT-CHECK LOG entry (428) is correct and was never in scope: those are the file references Hubbard-Hall herself cites.

---

## 2. Regression checks

| Check | Result |
|---|---|
| Em-dashes anywhere in the file | 0 |
| En-dashes | 0 |
| Realtor / Las Vegas / Lofty / Rose Homes content | 0 |
| Narration word count (all spoken lines before PRODUCTION NOTES) | 2,083 words across 81 spoken lines (2,020 NARRATOR, 63 character-voice). Was 2,068. Still inside the 1,900 to 2,200 Standard-tier band |
| Header block, ACCURACY NOTE, VOICE NOTE | Present |
| COLD OPEN with TITLE CARD | Present, line 32 |
| Acts with timecodes | 8 acts, 0:00 to 14:00, contiguous, unchanged |
| OUTRO with subscribe CTA, Mincemeat teaser, [END] | Present, line 374 |
| PRODUCTION NOTES, FACT-CHECK LOG, SOURCES | All present |
| Every act ends on a hook | Yes, all 8. Corrections 5, 7 and 8 did not touch an act-closing beat except Act 8, whose closer is now "a room of retired intelligence officers gathered at the Special Forces Club to greet a man they had been told was dead", which still lands as a hook |
| TONE: STRAIGHT beats still tagged | 14 tagged beats, unchanged: 2 Spanish Civil War, 5 Araceli, 2 D-Day casualty, 4 V-1, 1 Normandy 1984 |
| Comedy inside any straight beat | None. Every tagged beat is NARRATOR-only. No character-voice line falls inside any of them. The Araceli act still carries no character-voice line at all |
| Straight beats touched by edits | Only the D-Day casualty beat (Correction 2) and the Croydon beat (Correction 4). Both remain flat, factual and joke-free. Correction 4 adds a death figure, which deepens the human cost rather than softening it |

---

## 3. New-error scan on the edited lines

- **Line 112.** "naming three of the sources he used" is accurate to the 12 July 1943 memo as quoted by The Local, which lists those three as examples. No new claim introduced.
- **Line 130.** Removing the ship count removes a claim. Nothing added.
- **Line 172.** "a man in the Royal Air Force" is supported by every version of the Agent THREE sub-network and asserts no rank. No new claim.
- **Line 264.** "of those casualties" now correctly attaches the ~2,400 Omaha figure to the casualty total rather than the killed total. The three preceding figures are untouched and still match the National WWII Museum D-Day Fact Sheet.
- **Line 294.** "more than from any other agent" matches the National WWII Museum's "the highest number of all the D-Day spies". No overreach.
- **Line 316.** 54,000 damaged and over 200 killed are both carried by the English Heritage flying-bomb page and by Forces War Records. Note the figures are for the wartime Borough of Croydon over the ~80-day V-1 campaign, which is what the line says. No new error.
- **Line 352.** Removing the shop removes the conflicting-occupation claim. A man walking home with shopping asserts nothing about his job.
- **Line 358.** "He came to London" is supported: the London trip, the Special Forces Club reception and the Buckingham Palace audience followed the 20 May 1984 New Orleans meeting, on the trip that reached Normandy on 6 June 1984. No month is now asserted.
- **Lines 458, 462, 469.** URL and citation changes only. The English Heritage flying-bomb URL returns HTTP 200. The IWM path 403s to automated fetch, which is the site's standard bot block, and is the path search indexing resolves for the IWM page titled "V-Weapons".

**No new factual error was introduced by any of the 11 edits.**

---

## Issues to fix

### CORRECTIONS REQUIRED

**1. PRODUCTION NOTES still instructs production to reinstate the RAF rank that Correction 6 removed.**
Offending line 396:
> - The Gibraltarian waiter and the Welsh fascist group are stated as separate fictions. The RAF man is a non-commissioned officer. No Wren in the War Office.

This sits inside the block headed "Accuracy corrections baked in (do not undo)", so it is a live instruction to put the rank back. The rank is not settled across sources, which is why the narration no longer states it.

Replace with:
> - The Gibraltarian waiter and the Welsh fascist group are stated as separate fictions. The RAF man's rank is deliberately not stated, because sources disagree (non-commissioned officer in some, Pilot Officer in others). No Wren in the War Office.

**2. FACT-CHECK LOG still logs the RAF rank as confirmed.**
Offending line 425:
> - **Gibraltarian NAAFI waiter and Welsh fascist group as separate fictions, RAF non-commissioned officer.** Confirmed and kept distinct per the correction list.

Replace with:
> - **Gibraltarian NAAFI waiter and Welsh fascist group as separate fictions, plus an unranked RAF sub-agent.** Waiter and group confirmed and kept distinct. Rank NOT FOUND with agreement across sources, so no rank is stated on screen.

**3. FACT-CHECK LOG still repeats the killed-versus-casualties conflation that Correction 2 fixed in the narration.**
Offending line 432:
> - **D-Day casualties: at least 4,414 Allied killed, 2,501 American, over 10,300 total, roughly 2,400 at Omaha.** Confirmed (National WWII Museum). Played straight, never as a punchline.

Read in sequence after "4,414 Allied killed", the bare "roughly 2,400 at Omaha" still reads as killed. The National WWII Museum figure is casualties.

Replace with:
> - **D-Day casualties: at least 4,414 Allied killed, 2,501 American, over 10,300 total casualties, roughly 2,400 of those casualties at Omaha.** Confirmed (National WWII Museum). Played straight, never as a punchline.

---

## Cold read notes

The narration, the visuals and the SOURCES block are clean. Every Pass 1 correction landed verbatim, nothing regressed, and the edits introduced no new claim that fails checking. The three items above are all inside the production-facing apparatus rather than the spoken script, but two of them are explicitly framed as standing instructions under "do not undo", and one of those would put an unverifiable rank straight back into the episode. They are one-line fixes and this should clear on the next pass.

---

## PASS 3 (Manager close-out)

All three remaining items were production-apparatus lines, not narration. Applied verbatim as specified by QA:

1. PRODUCTION NOTES "Accuracy corrections baked in" line now states the RAF man's rank is deliberately unstated because sources disagree.
2. FACT-CHECK LOG entry now records the RAF rank as NOT FOUND with agreement, no rank on screen.
3. FACT-CHECK LOG D-Day entry now reads "over 10,300 total casualties, roughly 2,400 of those casualties at Omaha," matching the corrected narration.

Narration, visuals and SOURCES were already certified clean on Pass 2: 0 em-dashes, 2,083 narration words, all sections present, all 8 acts hook, all 14 TONE: STRAIGHT beats tagged and comedy-free, no new factual error. No further blockers.

VERDICT: PASS
