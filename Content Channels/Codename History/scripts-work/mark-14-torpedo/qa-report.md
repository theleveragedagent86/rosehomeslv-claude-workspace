# QA Report: The Torpedo That Refused to Explode

**QA agent, Wave 3. Blocking gate.** Structural checks run first and written before web verification, per instruction.

---

## Structural checks

All counts produced by script, not by eye. Script: `/private/tmp/.../scratchpad/qa.py`.

**Method for word count.** Extracted only lines matching `**NARRATOR:**` or `**X (character voice):**`, up to but excluding `## PRODUCTION NOTES`. Stripped the leading label and any wrapping quotation marks. Tokenised on whitespace, then discarded tokens containing no alphanumeric character (so a bare punctuation token never counts). Hyphenated forms were counted as one word, which is the correct treatment for TTS timing. I also re-ran with hyphens split as a control.

| Check | Requirement | Measured | Verdict |
|---|---|---|---|
| Narration word count | 1,390 to 1,410 | **1,405** (hyphens as one word); **1,406** with hyphens split | PASS, and the writer's reported 1,405 is exact |
| Narration beats | n/a | 112 | Matches the 112 VISUAL tags one for one |
| Longest beat | 14 words maximum | **max 14, zero violations** | PASS |
| Average beat | reported 12.5 | **12.54** | PASS |
| Shortest beat | reported 6 | **6** ("Seventy eight men died. Nine survived.") | PASS |
| `[VISUAL:]` tag count | near 112 | **112** | PASS |
| REUSE tags | reported 11 | **11** | PASS |
| Unique generations | reported 101 | **101** | PASS |
| REUSE targets valid | must point at a real EARLIER scene with a genuinely matching picture | **11 of 11 point backwards and 11 of 11 repeat the source tag text verbatim, character for character** | PASS |
| Camera moves | none anywhere | **zero.** The only regex hit was "spanning" in scene 16 ("A calendar wall spanning nineteen twenty six...") which is not a camera move | PASS |
| Em-dashes | zero | **zero.** Also zero en-dashes, zero horizontal bars, zero figure dashes across the entire file including notes and sources | PASS |
| Stage directions, brackets, digits or markup inside spoken lines | none | **zero.** No spoken line contains a bracket, parenthesis, asterisk, underscore, hash, angle bracket, or any Arabic numeral. Every number is spelled out ("nineteen forty three", "eight hundred and fifty yards") | PASS |
| Nine required sections, in order | required | COLD OPEN, TITLE CARD, ACT 1, ACT 2, ACT 3, ACT 4, ACT 5, ACT 6, OUTRO, END. Present and in order | PASS |

**REUSE map, verified individually.** scene 21 to 15, 25 to 15, 53 to 17, 61 to 17, 64 to 2, 67 to 5, 69 to 6, 82 to 8, 92 to 9, 93 to 18, 106 to 8. Every target index is lower than its reuse index, and every reuse line reproduces the target's tag text exactly, so the build will re-serve the existing file rather than generate a near-duplicate. Picture-to-content match checked by hand as well: scene 53 and 61 both need "a page of the official ordnance history", and both beats do cite the official history (ten percent prematures; the date footnote), so the picture is not merely reused, it is apt. Scene 106 reusing the three-circled-diagrams spine on "Different weapon, different fault" is the one reuse where the image is doing argumentative work rather than decoration, and it works.

**Act hooks.** Every act ends on a forward hook:
- Cold open, "There were three separate faults. Each one was hiding the next one."
- Act 1, "And nobody had ever fired a production Mark Fourteen at an actual ship."
- Act 2, "So they fixed the depth. And defect two finally had room to appear."
- Act 3, "It is a pin. It hits a cap. You are already ahead of me."
- Act 4, "Twenty one months. Three defects. Each had been hiding the one behind it."
- Act 5, "There is no single villain here. That is the uncomfortable part."
- Act 6, "The torpedoes were not the only reason for that. They were not nothing."
PASS.

---

## Arithmetic, recomputed independently

| # | Claim | My computation | Verdict |
|---|---|---|---|
| A1 | "Twenty one months" for Dec 1941 to Sep 1943 | 7 Dec 1941 to 30 Sep 1943 = 21 months 23 days. Counting Dec 1941 as month zero, Sep 1943 is month 21 | Correct |
| A2 | Jacobs Dec 1941, Navy ordered the same "eighteen months later" | 14 Dec 1941 to 24 Jun 1943 = 18 months 10 days | Correct, and consistent with the script's own 24 June date |
| A3 | 1 Aug 1942 is "nearly eight months into the war" | 7 Dec 1941 to 1 Aug 1942 = 7 months 25 days | Correct. "Nearly eight" is the right word |
| A4 | 1926 to 1941, "Nineteen years" of no destructive test | 1926 + 19 = 1945. The claim is not "1926 to 1941", it is the official history's own "19 years of prewar exploder development", which runs from the 1922 project start. 1922 to 1941 = 19 years | Correct as the history frames it. See issues list for a wording note |
| A5 | Ten warheads, seven duds, "seventy percent failure rate" | 7/10 = 70 percent exactly | Correct |
| A6 | 90-foot drop "matches the Mark Fourteen's forty six knots almost exactly" | v = sqrt(2gh) with g = 32.174 ft/s^2, h = 90 ft. v = 76.10 ft/s = **45.09 knots**. Against 46 knots that is 1.98 percent low. The height that gives exactly 46 knots is 93.7 ft | Correct, and "almost exactly" is the honest qualifier. See test 3 |
| A7 | The 900-foot variant | sqrt(2 x 32.174 x 900) = 240.65 ft/s = **142.6 knots**, roughly three times any torpedo speed ever fielded | Confirms 900 is an error, not a real figure |
| A8 | 52 boats, about 3,500 men, "about one in five" | 3,500 dead against roughly 16,000 men who made war patrols is about 22 percent | Directionally correct, pending source check below |

---

*(web verification appended below)*

---

## Sources I retrieved and read myself

I did not take the research report's word for anything. Retrieved and read in full or grepped in full:

- **Rowland and Boyd, *U.S. Navy Bureau of Ordnance in World War II*, ch. 6** (official BuOrd history), full text pulled from ibiblio and searched locally. Tier 1.
- **NHHC H-Gram 008-3, "Torpedo Versus Torpedo," Samuel J. Cox**, full text pulled and searched locally. Tier 1.
- **CAPT R. A. Bowling, USN (Ret.), PhD, "The Mark 14 Torpedo Tribulations," *The Submarine Review*, July 2002**, full text. Tier 1.
- **Frederick J. Milford, "The Great Torpedo Scandal 1941-43," *The Submarine Review*, October 1996**, full text. Tier 1.
- ***United States Submarine Losses, World War II*, Tang entry**, full text including the crew roster. Tier 1.
- **NHHC, *United States Submarine Losses World War II*, introduction** (personnel loss percentages). Tier 1.
- **National Park Service, "Submarines in World War II."** Tier 1.
- **uboat.net, "The Norwegian Operation and the Torpedo Crisis."** Tier 2.
- **"The Trouble With Torpedoes," *The Submarine Review*, 1997.** Tier 1 journal.
- **NHHC DANFS L-8 and NHHC photo NH 88457** (1926 exploder test), via search summary. Tier 1.
- Wikipedia Mark 14 / Mark 18 articles used **only** to trace where a figure originates, never as authority.

Two sources I could not retrieve directly and therefore did not let carry anything alone: Blair, *Silent Victory* (reached only through secondary quotation), and Wildenberg and Polmar, *Ship Killer*.

---

## Claim-by-claim verification

| # | Claim (as spoken) | Where | Source(s) checked | Verdict |
|---|---|---|---|---|
| 1 | "An American submarine finds a nineteen thousand ton tanker" | Cold open | Bowling verbatim: "a dead-in-the-water 19,262 ton whale factory, converted to an oil tanker" | VERIFIED |
| 2 | "Over one attack the submarine Tinosa fires fifteen torpedoes at this ship" | Cold open | Rowland and Boyd verbatim: "In all, 15 torpedoes were fired at the oiler" | VERIFIED |
| 3 | "About a dozen of them hit" | Cold open | Rowland and Boyd verbatim: "12 known hits were claimed" | VERIFIED, and "about a dozen" correctly softens a *claimed* figure |
| 4 | "Two exploded. The rest did nothing at all." | Cold open | Rowland and Boyd: "Only the first 2 spreads produced explosions" | VERIFIED |
| 5 | "The official Navy history's own phrase is that the dream target drifted on" | Cold open | Rowland and Boyd verbatim: "yet the dream target drifted on" | VERIFIED, and the attribution to the official history is exact |
| 6 | "The captain kept his final torpedo. He wanted somebody to examine it." | Cold open | Bowling; NHHC H-gram: "Daspit of Tinosa (SS-283) returned from a patrol with convincing data that the contact pistol was defective" | VERIFIED |
| 7 | "Nineteen twenty two. The Naval Torpedo Station at Newport starts a secret project." | Act 1 | Rowland and Boyd: "On May 8, 1926, 4 years of work were crowned by success," which back-dates the project start to 1922 | VERIFIED |
| 8 | "This is the Mark Six exploder" | Act 1 | Rowland and Boyd throughout | VERIFIED |
| 9 | **"May eighth, nineteen twenty six"** | Act 1 | Rowland and Boyd: "On May 8, 1926". **NHHC DANFS L-8 and NHHC photo NH 88457 both give 26 May 1926** | **CONFLICT, UNRESOLVED, ASSERTED FLATLY. See Issue 5** |
| 10 | "Two shots at an old hulk. One worked." / "By the better account the first ran underneath and did nothing at all." | Act 1 | Rowland and Boyd say the hulk was **sunk by the first shot**. Against that: NHHC's own photo caption NH 88457 describes a torpedo that "passed under the hulked submarine L-8 (SS-48)... This torpedo failed to explode," plus Wildenberg and Polmar and Alpher. **NHHC is Tier 1 and contradicts the BuOrd history** | VERIFIED as the better-supported version. The hedge "By the better account" is adequate and correctly placed in a NARRATOR line |
| 11 | "They never destructively tested the magnetic exploder again. Not once. Nineteen years." | Act 1 | Rowland and Boyd verbatim: "Never again during the 19 years of prewar exploder development was a destructive test made" | VERIFIED as to the words. **But see Issue 8: the on-screen calendar mis-frames what the 19 years spans** |
| 12 | "The Navy's own history calls it success being its own deterrent" | Act 1 | Rowland and Boyd verbatim: "How ironic that success should have been its own deterrent!" | VERIFIED, attribution exact |
| 13 | "One torpedo cost ten thousand dollars. In the Depression, destroying one felt unthinkable." | Act 1 | Milford verbatim: "a torpedo was valued at around $10,000... destroying one in testing was a risk that only the fearless were willing to run." NHHC independently: "about $160K in today's dollars" | VERIFIED, two independent sources |
| 14 | "Newport built a decoy exploder, the Mark Five. Identical to the real one, minus the magic. Issued with every torpedo." | Act 1 | Rowland and Boyd verbatim: "the Mark 5, a dummy for the Mark 6. Identical to the latter except for the secret feature, the Mark 5 was issued with each torpedo" | VERIFIED, near-verbatim |
| 15 | BuOrd voice: "If nobody knows it exists, nobody can tell the Germans about it." | Act 1, scene 21 | Rowland and Boyd: "As an added precaution to guard secrecy, even the men working on the mechanism were allowed only the vaguest idea about their project" | VERIFIED as a compression of a documented posture. No invented failing. See test 9 |
| 16 | "The official history says the fleet did not know the weapon existed" | Act 1 | Rowland and Boyd, and the chapter's own language about security that "excluded the operating forces." Milford: "draconian security, which in some cases even excluded the operating forces from full knowledge of the weapons they were expected to use" | VERIFIED, two sources, and correctly framed as the official history's claim |
| 17 | "Britain, Germany and Italy all had magnetic exploders already" | Act 1 | Rowland and Boyd verbatim: "England, Germany, and Italy all had magnetic exploders of their own before the outbreak of World War II" | VERIFIED |
| 18 | "Nineteen thirty eight. A destroyer command reports failures, with sea bottom sand as evidence." | Act 1 | Rowland and Boyd: the Coronado battle practice, "When many surfaced in 90 feet of water with the exercise heads covered with mud, deep running was obvious" | VERIFIED |
| 19 | BuOrd voice: "Have you considered that your men are simply handling them roughly?" | Act 1, scene 25 | Rowland and Boyd verbatim: "evidence of poor maintenance or rough handling impressed the Bureau representative more than the bottom sand which constituted the destroyer command's exhibit A" | VERIFIED as near-verbatim compression. See test 9 |
| 20 | "Nineteen thirty nine. An outside physicist finds four causes of prematures in a week." | Act 1 | Rowland and Boyd: "Admiral Furlong arranged for a physicist to visit the station... For approximately a week... Four sources of prematures were uncovered" | VERIFIED, exact on all three specifics |
| 21 | "And nobody had ever fired a production Mark Fourteen at an actual ship" | Act 1 | NHHC H-gram verbatim: "the U.S. Navy conducted no tests before the war using production torpedoes against an actual target" | VERIFIED |
| 22 | "December fourteenth, nineteen forty one. The submarine Sargo attacks a convoy off Indochina." | Act 2 | Confirmed 14 December 1941, a convoy near Cam Ranh Bay, French Indochina; Milford places Jacobs on Sargo's first war patrol | VERIFIED |
| 23 | "One torpedo exploded about eighteen seconds out of the tube. Nothing was there." | Act 2 | Confirmed: a torpedo "exploded eighteen seconds after leaving the firing tube." The script's "about" is the right hedge | VERIFIED |
| 24 | "Her captain, Tyrrell Jacobs, switched the magnetic feature off on his own authority." | Act 2 | Milford verbatim: "Jacobs, on SARGO's first war patrol, ordered the deactivation of the magnetic influence portion of the Mk 6 exploder in his torpedoes" | VERIFIED. Name and spelling correct |
| 25 | "He was right. It got him into considerable difficulty." | Act 2 | Milford verbatim: "and incidentally got into considerable difficulty for doing so" | VERIFIED. The phrase is Milford's own |
| 26 | "The Navy would order everybody else to do exactly that, eighteen months later" | Act 2 | Milford verbatim: "CINCPAC's order was issued 18 months after Jacobs." My own arithmetic: 14 Dec 1941 to 24 Jun 1943 = 18 months 10 days | VERIFIED, source and arithmetic agree |
| 27 | "The Mark Fourteen ran roughly ten feet too deep" | Act 2 | Rowland and Boyd: "the 10-foot error." Bowling: "10-11 feet deeper than set." NHHC: "about 10 feet deeper than set" | VERIFIED, three sources; "roughly" correctly covers the 10 to 11 spread |
| 28 | "So the magnetic exploder was never close enough to the hull to work" | Act 2 | Rowland and Boyd verbatim: "as long as torpedoes ran so far under a target that the exploder could not be expected to perform." This is the causal hinge of the episode | VERIFIED |
| 29 | "Because the practice heads were built to float" | Act 2 | Rowland and Boyd; NHHC: "All U.S. tests used exercise warheads, with an upward looking camera substituting for the magnetic influence sensor, and since the exercise torpedoes passed under the target ships, as they were supposed to, the tests were deemed a success" | VERIFIED |
| 30 | "The depth recorder had the same flaw as the depth gear" / "The instrument checking for the error was wrong by the error" | Act 2 | Rowland and Boyd: the defect was "hidden by the very instrument designed to expose it"; the measuring devices "checked each other, but both were improperly placed." Milford concurs | VERIFIED, two sources, and the paraphrase is faithful |
| 31 | "January nineteen forty two. The Bureau admits the older Mark Ten runs deep." | Act 2 | Bowling verbatim: "On 5 January 1942, Buord acknowledged that the Mk. 10 ran four feet deeper than set" | VERIFIED |
| 32 | "By March their own tests confirmed a four foot error on the Mark Fourteen" | Act 2 | Milford. Not contradicted by anything I found | VERIFIED |
| 33 | "Admiral Charles Lockwood had finished waiting for Newport to work it out" | Act 2 | NHHC: "Shortly after assuming command of Southwest Pacific Submarines in June 42, Rear Admiral Charles Lockwood ordered a series of tests." Bowling: "Admiral Lockwood took the unusual and career risking action of testing a piece of ordnance without specific approval from Buord" | VERIFIED. Note he was a **Rear** Admiral at this moment. See test 2 |
| 34 | "June twentieth, nineteen forty two. He rigged a fishing net across a bay." | Act 2 | Bowling verbatim: "At Albany, Australia, a fish net was rigged in Frenchman's Bay, and on 20 June 1942, a series of Mk. 14 torpedoes were fired into it from a range of 850 yards" | VERIFIED, date exact |
| 35 | **"Frenchman's Bay at Albany, Western Australia. Not Maine."** | Act 2 | Bowling verbatim (above); *The Submarine Review* 1997: "Rear Admiral Charles Lockwood's arrival at Fremantle in June 1942" and net tests there; NHHC | VERIFIED by two independent Tier 1 journal sources. See test 2 |
| 36 | "One shot set for ten feet went through that net at twenty five" | Act 2 | Blair via secondary quotation: "Jim Coe's Skipjack fired a single torpedo with an exercise head from a distance of 850 yards. Despite being set for a depth of 10 ft, the torpedo pierced the net at a depth of 25 ft." Bowling independently brackets it: "between 11 and 15 feet below set depths" | VERIFIED. The script's "One shot" is the correct hedge; it does not generalise the extreme case to all shots |
| 37 | BuOrd voice: "A net in a current does not hang straight. Your methodology is poor." | Act 2, scene 45 | Bowling: "Admiral Lockwood reported his findings to Buord. **Buord disagreed on technical grounds.**" Milford on BuOrd's reluctance. Rowland and Boyd for the net-in-current principle | VERIFIED as a compression of a documented objection. The specific words are not quoted anywhere, but the line is signposted fake dialogue and invents no failing. See test 9 |
| 38 | "Then Admiral King got involved, and Newport re-investigated" | Act 2 | NHHC verbatim: "When news of the tests reached CNO Ernest J. King, he turned his famous wrath on BuOrd." Rowland and Boyd credit the net firings to the Commander in Chief, US Fleet | VERIFIED, two sources |
| 39 | "August first, nineteen forty two. The Bureau conceded the ten foot error." | Act 2 | Rowland and Boyd verbatim: "On August 1, 1942, the services were officially informed of the 10-foot error." Bowling: "on 1 August 1942, Buord confirmed" | VERIFIED, two sources, date exact |
| 40 | "That is nearly eight months into the war" | Act 2 | My arithmetic: 7 Dec 1941 to 1 Aug 1942 = 7 months 25 days | VERIFIED |
| 41 | **"Pacific submarines had already fired over eight hundred torpedoes. Roughly a year's production."** | Act 2 | NHHC verbatim: "By then, Pacific Fleet submarines had fired over 800 torpedoes (a year's worth of production at that time)" | VERIFIED verbatim. See test 6 |
| 42 | "With the depth corrected, torpedoes started exploding before they arrived" | Act 3 | Rowland and Boyd: "when the error was corrected so that torpedoes were set for shallower depths... the weapons entered the enemy ship's magnetic field some distance from its hull" | VERIFIED, and the causal sequencing is the source's own |
| 43 | **"The official history estimates prematures ruined perhaps ten percent of early war shots"** | Act 3 | Rowland and Boyd do say "on perhaps 10 percent of the early war shots premature explosions made hits impossible." **But the same chapter also says: "submariners were convinced that some 10 percent of the torpedoes they fired were prematures. The Bureau, analyzing combat reports as they were received, concluded that prematures did not exceed 2 percent of the total shots fired. Whatever the truth, ill feeling was the result."** | **DEFECT. The source explicitly declines to settle this and records a competing 2 percent. See Issue 4** |
| 44 | "Lockwood called the Mark Six a Rube Goldberg device with six possible failures" | Act 3 | Rowland and Boyd verbatim: "Vice Admiral Lockwood [called] the exploder a 'Rube Goldberg' device with **5 or 6** things that might go wrong" | VERIFIED, and "six" sits inside the quoted range. Acceptable, though it takes the high end silently |
| 45 | "The Bureau's proposed fix was a longer arming run and a list of rules" | Act 3 | Bowling verbatim: "on 3 and 7 May Buord informed Admiral King, CNO, that the effectiveness of the Mk. 6 would be increased by 10 to 30 percent if the arming distance were increased from 450 to 700 yards and fired under a list of additional limitations" | VERIFIED |
| 46 | BuOrd voice: "It works fine. You simply have to shoot under all of these conditions." | Act 3, scene 56 | Bowling, as above | VERIFIED. This is the tightest of the four Bureau lines. See test 9 |
| 47 | "King said no. He asked for a different exploder instead." | Act 3 | Bowling verbatim: "Admiral King replied that the increased arming distance was unacceptable and concurred with Admiral Lockwood... that the MK. 6 exploder should be replaced" | VERIFIED |
| 48 | **"June twenty fourth, nineteen forty three. Nimitz ordered the magnetic exploders inactivated."** | Act 3 | **Three independent Tier 1 sources agree.** Bowling: "on 24 June, Admiral Nimitz, CincPacFlt, ordered ComSubPac and ComDesPac to inactivate magnetic exploders on all torpedoes." Milford: "CINCPAC ordering the disabling of the magnetic influence feature on 24 June 1943." NHHC: "Deactivation was ordered on 24 June 1943" | VERIFIED. See test 4 |
| 49 | "The next day the Bureau sent him a message asking why" | Act 3 | Bowling verbatim: "next day BuOrd asked why" | VERIFIED |
| 50 | "By the account that survives, he answered that it was simply ineffective" | Act 3 | Bowling, quoting the reply: Nimitz "replied that his decision was made because the Mk. 6 was 'ineffective' and because of 'the impracticability of selecting the proper conditions... under which to fire'" | VERIFIED. The hedge is in a NARRATOR line and is, if anything, more cautious than needed |
| 51 | "The Navy's own official history dates that order a month late" | Act 3 | Rowland and Boyd verbatim: "On July 24, the practice was officially sanctioned when Admiral Nimitz, Commander in Chief, Pacific Fleet, ordered his submarine and destroyer commands to inactivate the magnetic device on all torpedoes" | VERIFIED. The conflict is real and the script names it. See test 4 |
| 52 | **"So the magnetic feature came out."** | Act 3 | Bowling is explicit that this was **not** fleet-wide: "Not so for the boats in ComSubSoWestPac... where Admiral Ralph Christie ordered that the magnetic feature be retained. Still, it was not until March 1944 that it was inactivated in SoWestPac submarines." Milford gives December 1943 | **DEFECT by omission. See Issue 7 and test 10** |
| 53 | "July twenty fourth, nineteen forty three. Back to the Tinosa" | Act 4 | Rowland and Boyd date the Tinosa attack to July 24 | VERIFIED |
| 54 | "Lieutenant Commander Dan Daspit" | Act 4 | Bowling verbatim: "Lieutenant Commander L.R. Dan Daspit in TINOSA." NHHC: "Lieutenant Commander Dan Daspit of Tinosa (SS-283)" | VERIFIED. Rank correct in two Tier 1 sources |
| 55 | "hit her twice, then stopped her dead in the water" | Act 4 | Rowland and Boyd: "Only the first 2 spreads produced explosions." Bowling: "a dead-in-the-water 19,262 ton whale factory" | VERIFIED |
| 56 | "Daspit closed to eight hundred and fifty yards, on a perfect ninety degree track" | Act 4 | Bowling verbatim: "from a point blank range of 850 yards with a optimum 90 degree track, torpedo strikes perpendicular to the target's hull" | VERIFIED |
| 57 | "This is the easiest shot in submarine warfare. They were all duds." | Act 4 | Bowling; NHHC: "torpedoes that hit the target at a 90 degree angle (i.e., a perfect shot) were more likely to fail" | VERIFIED. **No dud count is asserted**, which is correct given circulating figures run from 8 to 11 |
| 58 | "By the crew's account, Japanese sailors came to the rail and pointed at them" | Act 4 | Not in any Tier 1 text I retrieved. The script attributes it to the crew and asserts no sound | HEDGED APPROPRIATELY. The hedge is in a NARRATOR line and the claim is trivial in weight. See test 7 |
| 59 | "Fifteen torpedoes. About a dozen hits. Two explosions. The ship did not sink." | Act 4 | Rowland and Boyd, as at rows 2 to 4. NHHC DANFS Tinosa: "she damaged only a single tanker" | VERIFIED, and this is the official history's own arithmetic |
| 60 | "Daspit stopped with one left, deliberately, and carried it home as evidence" | Act 4 | Bowling; NHHC | VERIFIED |
| 61 | "Weeks later the Haddock put eleven more torpedoes into one damaged tanker. Nothing." | Act 4 | Rowland and Boyd verbatim: "The submarine Haddock, after damaging a 10,500 ton tanker with 2 hits, fired 11 more torpedoes in 3 further attacks on the same ship without getting another explosion" | VERIFIED |
| 62 | "Lockwood started firing live torpedoes at a cliff at Kahoolawe, Hawaii" | Act 4 | Bowling verbatim: "Two Mk. 14's with warheads attached were fired at submerged cliffs at Kahoolawe." NHHC: "firing torpedoes into cliff faces." Rowland and Boyd: "by firing into a cliff" | VERIFIED, three sources. Note only Bowling names Kahoolawe |
| 63 | "Then they hung warheads off a crane and dropped them onto a steel plate" | Act 4 | Bowling: "10 dummy warheads, fitted with Mk. 6 exploders, were dropped from a height of 90 feet onto a steel plate." The **crane** specifically is attested in the Blair-derived account: "a crane to drop warheads filled with sand" | VERIFIED. The crane is not invented |
| 64 | **"Ninety feet. That impact matches the Mark Fourteen's forty six knots almost exactly."** | Act 4 | Bowling verbatim: "dropped from a height of 90 feet." Rowland and Boyd's ibiblio transcription says 900 feet. Mark 14 speed from Rowland and Boyd verbatim: "high, 46 knots to 4500 yards." **My own physics: 90 ft gives 45.09 knots; 900 ft gives 142.6 knots** | VERIFIED, and the physics as stated on screen is correct. See test 3 |
| 65 | "Ten warheads dropped. Seven duds. There is your seventy percent failure rate." | Act 4 | Bowling verbatim: "Seven of the 10 were duds." Blair-derived route independently: "70% of the exploders failed to detonate when they hit the target at 90 degrees." My arithmetic: 7/10 = 70 percent | VERIFIED by two independent routes |
| 66 | "The guide pins bent under the impact. The perfect square hit failed most." | Act 4 | Bowling verbatim: the firing pin "had not traveled far enough along its guide rails to strike the primer cap"; "deceleration equivalent to 500 times the force of gravity with a frictional component of 190 pounds on the firing pin guide rails when the torpedo struck square-on." Rowland and Boyd: "a direct impact produced more friction that the firing pin could overcome." NHHC: a perfect 90 degree shot "were more likely to fail" | VERIFIED, three sources |
| 67 | **"So submarines were told to aim off on purpose. It halved the duds."** | Act 4 | NHHC says only: "The interim fix was for submarines to attempt to hit targets at more oblique angles, and this **actually did help reduce** the dud problem." **NHHC does not quantify.** The halving traces to the Blair-derived account: "encourage 'glancing' shots (which cut the number of duds in half)" | SOURCEABLE to Blair, but **the script's own fact-check log misattributes it to NHHC**. See Issue 6 |
| 68 | "The fix was a lighter firing pin, machined from aluminium instead of steel" | Act 4 | Rowland and Boyd verbatim: "at Pearl Harbor, the submariners got similar results by lightening the firing pin." Milford: "It was a simple solution to make aluminum alloy (rather than steel) firing pin blocks" | VERIFIED, two Tier 1 sources |
| 69 | **"The story in the fleet was the aluminium came from downed Japanese planes"** | Act 4 | Not in Rowland and Boyd, not in Bowling, not in Milford, not in NHHC. Traces to Blair and popular retellings only | **CORRECTLY HEDGED.** It is attributed to fleet story in a NARRATOR line and never asserted as record. See test 7 |
| 70 | "The new pins were not made at Newport. They came off a repair ship." | Act 4 | Bowling verbatim: "Admiral Lockwood approved the production of modified Mk. 6 exploder firing pin mechanisms on the tender HOLLAND" | VERIFIED |
| 71 | "September thirtieth. The Barb sailed with twenty torpedoes that would actually explode." | Act 4 | Bowling verbatim: "On 30 September 1943, BARB departed Pearl on patrol with 20 torpedoes, all equipped with the modified firing pins" | VERIFIED, date and count exact |
| 72 | "Twenty one months. Three defects." | Act 4 | Blair via secondary quotation. My arithmetic: Dec 1941 to Sep 1943 = 21 months. Bowling independently: "Almost two years later" | VERIFIED. See test 5 |
| 73 | **"The German navy had the same three failures"** | Act 5 | Milford: "**Almost the same set**, defective depth control, unsatisfactory and untested magnetic exploder and a contact exploder that did not work at certain striking angles, occurred in the German Navy" | **OVERSTATES THE SOURCE.** Milford hedged; the script dropped the hedge. See Issue 3 |
| 74 | "Depth control. An untested magnetic exploder. A contact pistol that failed at angles." | Act 5 | Milford, near-verbatim as above | VERIFIED as the three-item list |
| 75 | "Off Norway in April nineteen forty, their torpedoes failed on a massive scale" | Act 5 | uboat.net: "between 30 and 35 % of the torpedo attacks during the Norwegian campaign had been failures." *The Submarine Review* 1997 describes failures on a massive scale during the Norway campaign | VERIFIED in substance, and **no percentage is spoken**, which is right because the percentages vary by source |
| 76 | "Dönitz got a board of inquiry" | Act 5 | *The Submarine Review* 1997: Dönitz "persuaded Grand Admiral Raeder to convene a board of inquiry," convened "within a week." uboat.net: "A commission was set up in mid-April to investigate the case thoroughly" | VERIFIED by two sources. The verb "got" is exactly right: Dönitz did not order it, he obtained it |
| 77 | **"Four senior officers were court martialled." / "Convicted and punished."** | Act 5 | **Milford alone gives four**, and attributes the order to Raeder: "four senior officers being tried by court martial, on the order of Grand Admiral Eric Raeder, found guilty and punished." **A competing account gives three**: Rear Admiral Oskar Wehr, head of the Torpedo Testing Institute, "court-martialed and sentenced, along with two of his principal associates." uboat.net and *The Submarine Review* 1997 both confirm convictions and prison terms but **give no number** | **FAIL. The number four is single-sourced and contradicted. See Issue 2** |
| 78 | "In the American case, nobody was held responsible at all" | Act 5 | Milford draws exactly this contrast. No US officer was court-martialled or formally held to account | VERIFIED |
| 79 | **"The best analytical source on this calls that claim certainly an overstatement"** | Act 5 | Milford verbatim, quoting a submariner's claim that all three defects "had been solved by the operating forces in their tenders and bases, without help from Newport or Washington," then: "**This is certainly an overstatement.**" | VERIFIED verbatim, and the quotation is in its correct context. See test 8 |
| 80 | **"The Bureau ran its own tests in Chesapeake Bay and reached the same answer"** | Act 5 | Rowland and Boyd verbatim: "In Chesapeake Bay the Bureau fired torpedoes directly at armor plates suspended in the water and found that a direct impact produced more friction that the firing pin could overcome," and the Pearl Harbor tests "ran concurrently with the Bureau's own investigation," and "**both series of tests gave the same results**" | VERIFIED verbatim, including "the same answer." **Better sourced than the script's own log claims.** See test 8 |
| 81 | "Newport had held a monopoly on American torpedoes since nineteen twenty three" | Act 5 | Milford verbatim: "especially after 1923 when the station secured a monopoly on torpedo development and production" | VERIFIED, date exact |
| 82 | "Cut off from industry, starved of money, and hiding the weapon from its users" | Act 5 | Milford, all three drivers verbatim: "almost total isolation of NTS-Newport from the larger U.S. technical and engineering community"; "the poor state of Navy finances"; "draconian security, which in some cases even excluded the operating forces from full knowledge of the weapons they were expected to use" | VERIFIED, all three |
| 83 | "There is no single villain here" | Act 5 | Editorial, and it is Milford's own structural conclusion | VERIFIED as a sourced judgment, correctly not dressed as a fact |
| 84 | "A number of submarine skippers were relieved of command during those months" | Act 6 | NHHC verbatim: "a number of submarine skippers who had been relieved of command" | VERIFIED verbatim |
| 85 | "The reason recorded was that they were not aggressive enough. Sometimes that was true." | Act 6 | NHHC verbatim: "for supposedly being incompetent or not aggressive enough (**in some cases true**...)" | VERIFIED verbatim |
| 86 | "They were also not helped by torpedoes that did not work" | Act 6 | NHHC verbatim: "but they certainly were not helped by torpedoes that didn't work" | VERIFIED verbatim |
| 87 | "Fifty two American submarines were lost in the Second World War" | Act 6 | NHHC *United States Submarine Losses*: 52. National Park Service: "52 US submarines were lost" | VERIFIED, two sources |
| 88 | "About three thousand five hundred officers and enlisted men died in them" | Act 6 | NHHC introduction: "**374 officers and 3,131 enlisted men**," which I added myself to **3,505**. NPS gives 3,506 | VERIFIED, and "about three thousand five hundred" correctly refuses to pick between 3,505 and 3,506 |
| 89 | **"That was the highest loss rate of any American branch. About one in five."** | Act 6 | NPS verbatim: "The US Navy Submarine Service had the highest casualty percentage of any American forces in the War: **about 20%**." **But NHHC's own volume gives different denominators: "16% of the officer and 13% of the enlisted operational personnel," and separately an 18 percent loss rate for boats** | SOURCED to NPS, but single-sourced on the rate, and the phrase "loss rate" collides with the boat statistic. See Issue 6 |
| 90 | "The torpedoes were not the only reason for that. They were not nothing." | Act 6 | Deliberate limiting statement. No source attributes the loss rate to the torpedoes and the script does not either | VERIFIED as a correct refusal to over-claim. This is good practice |
| 91 | "October nineteen forty four. The submarine Tang, on her fifth war patrol." | Outro | *United States Submarine Losses*: "Tang... set out from Pearl Harbor on 24 September 1944, to begin her fifth war patrol" | VERIFIED. **The script gives only the month, correctly dodging the 24 vs 25 October conflict** between the losses volume and NHHC |
| 92 | "It was the most successful patrol any American submarine made in the war" | Outro | *United States Submarine Losses* verbatim: "the most successful patrol ever made by a U.S. submarine" | VERIFIED verbatim |
| 93 | "She fired her twenty fourth and last torpedo. It circled back toward her." | Outro | *United States Submarine Losses* verbatim: "On her last patrol Tang fired twenty-four torpedoes in four attacks. Twenty-two torpedoes found their mark... and the last torpedo, fired after a careful checkover, sank Tang." "It curved sharply to the left, broached, porpoised and circled" | VERIFIED, and the VISUAL's 24/22 tally is exact |
| 94 | **"That torpedo was a Mark Eighteen electric. It was not a Mark Fourteen."** | Outro | NHHC verbatim: "Tang (SS-306), Lieutenant Commander Richard O'Kane commanding, was sunk on 25 October 1944 by her own circling torpedo, **a new Mark 18**" | VERIFIED. See test 1 |
| 95 | **"Different weapon, different fault."** | Outro | **Contradicted.** NHHC: circular running was "**the fourth major problem with the Mark 14**... this problem was never completely solved." The sourced statement about the Mark 18 is that it "**shared one major flaw with the Mark 14**: it had no protection against circular runs" | **FAIL. Same fault, different weapon. See Issue 1** |
| 96 | **"The Mark Eighteen was rushed into service with no protection against circular runs."** | Outro | **The sentence the script's fact-check log quotes as verbatim NHHC H-gram 008-3 is not in that document.** I pulled and searched the full H-gram: the words "rushed" and "Mark 18 had no protection" do not appear. The wording traces to a Wikipedia article | **FAIL. "Rushed into service" is unsourced editorialising and the supporting citation does not exist. See Issue 1** |
| 97 | "Seventy eight men died. Nine survived." | Outro | *United States Submarine Losses*: "the nine survivors were picked up by a destroyer escort"; crew of 87. 87 minus 9 = **78**. NHHC confirms nine survivors | VERIFIED, and my own arithmetic agrees |
| 98 | "Thirteen tried to escape the forward torpedo room using Momsen lungs" | Outro | *United States Submarine Losses* verbatim: "Thirteen men escaped from the forward room." Momsen lungs are separately and consistently attested for this escape | VERIFIED |
| 99 | "Eight reached the surface. Five were still swimming when help arrived." | Outro | *United States Submarine Losses* verbatim: "Of the 13 men who escaped, only eight reached the surface, and of these but five were able to swim until rescued" | VERIFIED verbatim, all three numbers |
| 100 | "Next time, the German navy's own torpedo crisis, and the men they prosecuted" | Outro | Teaser. Makes no numeric claim | VERIFIED as safe, **provided Issue 2 is fixed**, since the teaser thumbnail currently specifies four officers |

---

## Episode-specific tests

### Test 1. Tang is not a Mark 14 failure. **PARTIAL FAIL.**

- **Mark 18, said in the spoken narration: PASS.** Scene 105 is a NARRATOR line: "That torpedo was a Mark Eighteen electric. It was not a Mark Fourteen." It gets its own dedicated caption-card image. NHHC H-gram 008-3 states it verbatim: "sunk on 25 October 1944 by her own circling torpedo, a new Mark 18." This is the disambiguation the episode most needed and it is done well and unambiguously.
- **78 lost and 9 survivors against NHHC: PASS.** The official losses volume gives nine survivors and an 87-name roster; 87 minus 9 is 78, which I computed rather than accepted. NHHC's Tang page independently confirms nine survivors.
- **Loss date framing: PASS.** The official losses volume dates the attack 24 October 1944, NHHC's H-gram says 25 October. The script says only "October nineteen forty four" and no clock time. Correct handling of a live conflict: it asserts neither.
- **The Mark 18 "rushed into service with no protection against circular runs" claim: FAIL, and it is an overreach.** Two separate problems.
  1. **The citation is not real.** The script's fact-check log presents this as verbatim NHHC H-gram 008-3: "The Mark 18 had no protection against circular runs, a defect which claimed Tang for certain." I pulled the complete H-gram and searched it. That sentence is not in it. Neither "rushed" nor any Mark 18 design claim appears. The wording matches a Wikipedia article on the Mark 18, whose actual sentence is "The Mark 18 shared one major flaw with the Mark 14: it had no protection against circular runs, a defect which claimed Tang for certain."
  2. **The claim is inverted.** The sourced statement is that the Mark 18 **shared** the flaw with the Mark 14. NHHC's H-gram says plainly: "The fourth major problem with the Mark 14 was a tendency to run in circles... Although no U.S. subs are known to have been sunk by a circling Mark 14, **this problem was never completely solved**." So circular running was not a Mark 18 novelty and was not a "different fault." The script's line "Different weapon, different fault" states the opposite of the record.
  3. **"Rushed into service" is unsupported** in any source I retrieved and is editorial characterisation of an engineering programme.

  This matters more than a normal error because it sits on the human-cost beat and because the episode's entire brand claim in this act is that it is correcting other people's sloppiness. Fix is in Issue 1, and the fix makes the episode's thesis stronger rather than weaker.

### Test 2. Frenchman's Bay, Albany, Western Australia. **PASS.**

- **Location: verified twice over.** Bowling verbatim: "At Albany, Australia, a fish net was rigged in Frenchman's Bay." *The Submarine Review* 1997 independently places Lockwood at Fremantle in June 1942 running net tests. Two independent Tier 1 journal sources. The script says the town, the state and the country in one NARRATOR line and then says "Not Maine" out loud. This is the correction done properly.
- **Date of the net tests: verified.** Bowling gives 20 June 1942 explicitly; the script says "June twentieth, nineteen forty two."
- **Lockwood's command role for that moment: PASS, by careful avoidance.** This was the trap and the script does not step in it. At Frenchman's Bay in June 1942 Lockwood was a **Rear Admiral commanding Submarines Southwest Pacific**, based at Fremantle. NHHC: "Shortly after assuming command of Southwest Pacific Submarines in June 42, Rear Admiral Charles Lockwood ordered a series of tests." He did not become Commander Submarine Force Pacific until February 1943, which is the job he held for the later Kahoolawe and Pearl Harbor drop tests. Bowling's own text is loose here and calls him "ComSubSoPac" at the net test and notes he was "by then ComSubPac" by May 1943. **The script states no command title at either moment**, saying only "Admiral Charles Lockwood," so it cannot be wrong about a role it never claims. The one imprecision is styling a Rear Admiral as "Admiral," which is ordinary narration convention and which I am not flagging.

### Test 3. The 90-foot drop test. **PASS, and the physics on screen is correct.**

- **Height: verified against a Tier 1 source that is not the OCR.** Bowling verbatim: "10 dummy warheads, fitted with Mk. 6 exploders, were dropped from a height of **90 feet** onto a steel plate. Seven of the 10 were duds." The Blair-derived account independently says "a crane to drop warheads filled with sand instead of high explosive from a height of 90 feet."
- **The 900-foot figure is real in the ibiblio transcription.** I confirmed it with my own eyes: "by dropping inert-loaded torpedo warheads on steel plates from a height of 900 feet." So the script is right that the official history's transcription carries the larger number, and right not to use it.
- **I recomputed the impact speed myself.** Free fall, v = sqrt(2gh), g = 32.174 ft/s^2.
  - h = 90 ft gives v = 76.10 ft/s = **45.09 knots**.
  - h = 900 ft gives v = 240.65 ft/s = **142.58 knots**.
- **Against the Mark 14's own speed**, which Rowland and Boyd give verbatim as "high, 46 knots to 4500 yards": 45.09 against 46 is **1.98 percent low**. The height that would give exactly 46 knots is 93.7 ft. 142.58 knots is roughly three times any torpedo speed ever fielded and simulates nothing.
- **Is the stated physics actually right?** Yes. A drop test of this kind is a velocity-matching test: the point is to reproduce the impact speed at which the firing pin block must overcome friction on its guide rails, and a 90-foot free fall reproduces 46 knots to within two percent. Bowling's own explanation of the mechanism, "deceleration equivalent to 500 times the force of gravity with a frictional component of 190 pounds on the firing pin guide rails when the torpedo struck square-on," is consistent with matching impact velocity rather than drop height.
- **Verdict on the spoken line** "Ninety feet. That impact matches the Mark Fourteen's forty six knots almost exactly": correct, and "almost exactly" is the honest qualifier for a two percent gap. This is the strongest single piece of work in the script. Nothing to fix.

### Test 4. The Nimitz deactivation order, 24 June 1943. **PASS.**

- **The date the script uses is right and is the majority Tier 1 position, by three to one.**
  - Bowling: "on 24 June, Admiral Nimitz, CincPacFlt, ordered ComSubPac and ComDesPac to inactivate magnetic exploders on all torpedoes."
  - Milford: "CINCPAC ordering the disabling of the magnetic influence feature on 24 June 1943."
  - NHHC H-gram 008-3: "Deactivation was ordered on 24 June 1943."
  - Against: Rowland and Boyd, "On July 24, the practice was officially sanctioned when Admiral Nimitz... ordered his submarine and destroyer commands to inactivate the magnetic device."
- **The script names the disagreement rather than hiding it.** Scene 62 is a NARRATOR line: "Small footnote. The Navy's own official history dates that order a month late." It gets its own image. It does not average, does not split the difference, and does not quietly pick a side without telling the audience there is a side to pick. This is exactly the required handling.
- **Is the causal argument sound? Yes, independently of the source count.** The Tinosa attack is 24 July 1943. Tinosa's torpedoes were duds on impact, not prematures, which is only diagnostic if the magnetic feature was already off. Rowland and Boyd's own narrative structure requires the same ordering: they write that deactivation "revealed that the contact exploder had major design flaws as well," and NHHC says the same, "The deactivation of the magnetic exploders solved the premature detonation problem, but revealed that the contact exploder had major design flaws." An order issued on the same day as the attack it supposedly enabled cannot have enabled it. The July 24 date also coincides suspiciously exactly with the Tinosa attack date, which is the signature of a transcription or note-taking slip rather than a second event. **The script is right to prefer 24 June, right to say so, and right not to explain the coincidence on screen**, since airing the coincidence would give the wrong date a foothold in the audience's memory.

### Test 5. Twenty one months. **PASS.**

Checked against the dates the script itself uses, not against the source's assertion. The script's own bookends are 14 December 1941 (Sargo, Act 2) and 30 September 1943 (Barb, Act 4). December 1941 to September 1943 is **21 months**. The script's other duration claims are internally consistent with it: "eighteen months later" for Dec 1941 to 24 June 1943 is 18 months 10 days, and "nearly eight months into the war" for 7 December 1941 to 1 August 1942 is 7 months 25 days. Bowling independently characterises the span as "Almost two years later," which brackets 21 months correctly. No arithmetic error anywhere in the script.

### Test 6. No hard total for wasted torpedoes. **PASS.**

- **I grepped every spoken line for a waste total.** There is none. The only large quantities spoken anywhere in the episode are: nineteen thousand tons (a ship), ten thousand dollars (a torpedo's cost), over eight hundred torpedoes (fired), ten percent (prematures), eight hundred and fifty yards (a range), seventy percent (a failure rate), and three thousand five hundred (men). No cumulative dud, waste, or loss figure exists.
- **The eight hundred figure is verbatim NHHC** and it is a *fired* figure: "By then, Pacific Fleet submarines had fired over 800 torpedoes (a year's worth of production at that time)."
- **The wording does not imply a waste total.** The spoken line is "Pacific submarines had already fired over eight hundred torpedoes. Roughly a year's production." The verb is "fired." Notably the script declines to carry NHHC's own following clause, "with very little to show for it," which would have edged toward implying waste. The one appearance of the word "wastes" is at scene 51, "A premature wastes the torpedo, warns the target, and announces where you are," which is a generic description of what a single premature does and asserts no total.

### Test 7. The hedges are in the spoken narration. **PASS on all four placements. PASS on strength for three; the fourth is fine but see the note.**

I grepped the four hedges against the extracted NARRATOR and character-voice lines. All four sit inside `**NARRATOR:**` lines, not in notes, not in VISUAL tags:

| Hedge | Line | In a NARRATOR line? | Strength against the sourcing |
|---|---|---|---|
| "By the better account" (1926 two-shot test) | 76 | Yes | **Adequate.** This contradicts the official BuOrd history, so a hedge is mandatory. It is supported by NHHC's own photo caption NH 88457 and DANFS L-8, plus Wildenberg and Polmar and Alpher, so calling it "the better account" is a defensible adjudication rather than a guess. Keep it |
| "The story in the fleet was" (aluminium from Japanese aircraft) | 348 | Yes | **Strong, and correctly so.** This is the one the brief singled out and it is handled properly. The claim appears in **none** of Rowland and Boyd, Bowling, Milford or NHHC. It traces to Blair and popular retellings. The script asserts the sourced half as fact ("The fix was a lighter firing pin, machined from aluminium instead of steel," which is verbatim Milford and Rowland and Boyd) and quarantines the unsourced provenance behind "The story in the fleet was." That is exactly the right seam. **This must not be flattened in the build.** The preceding VISUAL is "A wrecked Japanese aircraft propeller," which is fine as an illustration of a stated fleet story but should not be captioned as fact |
| "By the account that survives" (Nimitz reply) | 268 | Yes | **Adequate, arguably over-cautious.** Bowling quotes the exchange directly and is a credentialed Tier 1 author in a professional journal. The hedge costs nothing and I would keep it |
| "By the crew's account" (Japanese sailors at the rail) | 304 | Yes | **Adequate.** Not in any Tier 1 text I retrieved, and the claim carries no argumentative weight. Correctly, no sound is asserted, so the audible-clang versions in circulation are avoided |

**No memoir-only or single-sourced claim is asserted as fact in narration.** The one that would have been, the propeller aluminium, is hedged.

### Test 8. The inverted myth test. **FAIL on one specific, PASS on the rest.**

This is the most important check and the act mostly survives it, but not entirely.

- **"Were there exactly four German officers?" FAIL.** The number four rests on **Milford alone**: "The German Navy's problems were closed out, however, with four senior officers being tried by court martial, on the order of Grand Admiral Eric Raeder, found guilty and punished." A competing account, traceable to Blair, gives **three**: Rear Admiral Oskar Wehr, chief of the Torpedo Trials Command and long-time head of the Torpedo Testing Institute, "court-martialed and sentenced, along with two of his principal associates." uboat.net says "the personnel of the Torpedo Experimental Institute responsible for that SNAFU were court-martialed and sentenced to prison terms" with no number. *The Submarine Review* 1997 says "Senior officials were tried and condemned by court martial, served time, and humbled and chastised, were returned to duty," again with no number. **So a specific integer, spoken flatly, in the act whose whole job is to correct other people's overconfidence, is single-sourced and contradicted.** It also drives three VISUAL tags including the next-episode teaser thumbnail. Fix in Issue 2.
- **"Were they convicted?" PASS, robustly.** Three independent sources agree on conviction and punishment: Milford ("found guilty and punished"), uboat.net ("sentenced to prison terms"), *The Submarine Review* 1997 ("tried and condemned by court martial, served time"). The script's "Convicted and punished" is safe and should be kept.
- **"Dönitz got a board of inquiry" PASS.** *The Submarine Review* 1997 says Dönitz "persuaded Grand Admiral Raeder to convene a board of inquiry," convened within a week; uboat.net says a commission was set up in mid-April and reported in late July. The verb "got" is precisely right and avoids the error of saying Dönitz ordered it, which he could not have. Note that Milford attributes the court-martial order to **Raeder**, and the script does not claim otherwise, so no error there.
- **"Is the substantially identical three failures characterisation defensible?" MOSTLY, but the script drops the source's own hedge.** Milford writes "**Almost** the same set, defective depth control, unsatisfactory and untested magnetic exploder and a contact exploder that did not work at certain striking angles, occurred in the German Navy and many of the responses of the shore establishment to the problems were also the same." The script says "the same three failures," deleting "almost." Milford also notes a real asymmetry the script glosses: the German magnetic exploder had a latitude-sensitivity compensation that the US device lacked, and the Germans abandoned it fairly quickly. Small, but it is precisely the over-correction the brief warns about: an episode that debunks confidently should not itself be more confident than its source. Fix in Issue 3.
- **"Did the Bureau's parallel Chesapeake Bay testing actually reach the same diagnosis?" PASS, and it is better sourced than the script's own log claims.** The script's log credits this to Milford; Milford does not mention Chesapeake Bay at all. The real source is Rowland and Boyd, the official history, verbatim: "In Chesapeake Bay the Bureau fired torpedoes directly at armor plates suspended in the water and found that a direct impact produced more friction that the firing pin could overcome," that the Pearl Harbor tests "ran concurrently with the Bureau's own investigation," and that "**both series of tests gave the same results.**" The spoken line "The Bureau ran its own tests in Chesapeake Bay and reached the same answer" is therefore accurate on both halves. **No change needed on screen**, but the log's citation is wrong and should not be trusted downstream.
- **"Certainly an overstatement" PASS, verbatim and in context.** Milford is answering a named-but-unnamed "distinguished and truly great submariner" who claimed all three defects "had been solved by the operating forces in their tenders and bases, without help from Newport or Washington," and replies "This is certainly an overstatement." The script's line describes exactly that claim and quotes exactly that phrase. The quotation is authentic and is not wrenched out of context.

### Test 9. The four Bureau of Ordnance voice lines. **PASS on all four. No invented failing, no invented quotation.**

| Scene | Line | Documented posture behind it | Verdict |
|---|---|---|---|
| 21 | "If nobody knows it exists, nobody can tell the Germans about it." | Rowland and Boyd on the secrecy regime: "As an added precaution to guard secrecy, even the men working on the mechanism were allowed only the vaguest idea about their project. A selected group from the research section at Newport did all of the assembling and testing in rigidly maintained seclusion." Milford on "draconian security" | PASS. Compresses a real posture. Invents no failing. The irony that follows (Britain, Germany and Italy already had them) is itself documented verbatim |
| 25 | "Have you considered that your men are simply handling them roughly?" | Rowland and Boyd verbatim: "evidence of **poor maintenance or rough handling** impressed the Bureau representative more than the bottom sand which constituted the destroyer command's exhibit A" | PASS, and the log's claim that it is near-verbatim from the official history **checks out**. "Rough handling" is the history's own phrase, and the shift to a question is comedic framing, not an added accusation |
| 45 | "A net in a current does not hang straight. Your methodology is poor." | Bowling verbatim: "Admiral Lockwood reported his findings to Buord. **Buord disagreed on technical grounds.**" Milford on BuOrd's reluctance to accept the Frenchman's Bay results. Rowland and Boyd for the underlying net-in-current principle | PASS, with a note. The **specific** technical objection is not quoted in any source I retrieved; what is documented is that BuOrd disagreed on technical grounds and that nets in current are a known measurement problem. Because the format signals fake dialogue and the line attributes no failing BuOrd did not have, this is legitimate comedic compression. It is the loosest of the four and I would not want a fifth like it |
| 56 | "It works fine. You simply have to shoot under all of these conditions." | Bowling verbatim: "on 3 and 7 May Buord informed Admiral King, CNO, that the effectiveness of the Mk. 6 would be increased by 10 to 30 percent if the arming distance were increased from 450 to 700 yards **and fired under a list of additional limitations**" | PASS. The tightest of the four. It is almost a translation of the document |

- **The invented "you are aiming wrong" document: CONFIRMED ABSENT.** I searched every spoken line. No BuOrd quotation of that kind exists anywhere in the script. The blame posture is instead carried by narration and by the 1938 sand beat, both of which are real, and it is independently documented by NHHC: "The initial response from the Bureau of Ordnance (BuOrd) was to blame the submarine skippers ('operator error') because the torpedoes had worked fine in pre-war tests. Actually, they hadn't." The script had every temptation to invent this line and did not. Good discipline.
- **The Manager's one-voice decision is sound.** Reusing scene 15 for scenes 21 and 25 and voicing all four identically is consistent with the sources, which describe an institutional posture and never a single named speaker.

### Test 10. Deliberate omissions. **ONE DEFECT FOUND.**

I checked each omission for whether it leaves a *remaining* statement false or misleading, which is the standard the brief sets.

- **Christie, Withers and English unnamed: acceptable, with one exception below.** Act 5's remaining statement, "In the American case, nobody was held responsible at all," is true: no US officer was court-martialled or formally held to account. Not naming the three does not make that sentence misleading.
- **Cavite cut: acceptable.** No remaining statement depends on it and no torpedo-loss figure is asserted.
- **The Southwest Pacific holdout cut: NOT acceptable as currently worded. This is the defect.** Act 3 says "June twenty fourth, nineteen forty three. Nimitz ordered the magnetic exploders inactivated," and the next beat says "**So the magnetic feature came out.**" With the holdout omitted, that sentence tells the audience the magnetic exploder left the US submarine force in June 1943. It did not. Bowling is explicit: "Not so for the boats in ComSubSoWestPac, Lockwood's former command but not under Nimitz's theater command, where Admiral Ralph Christie ordered that the magnetic feature be retained. Still, it was not until March 1944 that it was inactivated in SoWestPac submarines." Milford gives December 1943 for the same event. Nimitz as CincPacFlt could only order **his own** commands, which Bowling names as ComSubPac and ComDesPac. So the omission leaves a remaining statement that is false as heard, even though the beat before it is accurate. **The fix costs one word and needs no names, so the no-single-villain rule is preserved.** See Issue 7.
- **O'Kane unnamed: good.** It sidesteps the Lieutenant Commander versus Commander conflict entirely. NHHC styles him Lieutenant Commander in October 1944; the official losses volume styles him Commander. Not naming him removes the trap and keeps the outro on the boat.
- **Tullibee omitted: correct.** NHHC says its torpedo type is unknown, so it could support nothing.
- **The Tinosa dud count omitted: correct**, and the script uses the official history's arithmetic instead.


---

## Issues to fix

Eight items. Two are hard fails, four are defects, two are build notes. **Every replacement below is written to the same beat length, and the eight replacements are word-count neutral in total: the script stays at exactly 1,405 narration words.** No replacement exceeds the 14-word ceiling. I have given exact verbatim lines so the Manager can apply them surgically.

---

**1. HARD FAIL. Outro, scenes 106 and 107.**

> **Claim as spoken:** "Different weapon, different fault. The Mark Fourteen's defects had been fixed a year earlier." and "The Mark Eighteen was rushed into service with no protection against circular runs."

**What is wrong.** Three things at once.
- The fact-check log presents a supporting sentence as verbatim NHHC H-Gram 008-3: "The Mark 18 had no protection against circular runs, a defect which claimed Tang for certain." **That sentence is not in H-Gram 008-3.** I retrieved the complete document and searched it; neither "rushed" nor any Mark 18 design claim appears. The wording matches a Wikipedia article. The citation does not exist.
- The claim is **inverted**. The actual sourced statement is that the Mark 18 "**shared** one major flaw **with the Mark 14**: it had no protection against circular runs." And NHHC states plainly that circular running was "the fourth major problem with the Mark 14... this problem was never completely solved." So it was the *same* fault, not a different one. "Different weapon, different fault" says the opposite of the record.
- "Rushed into service" is unsourced editorial characterisation and appears in no source I retrieved.

This is the inverted-myth trap in its purest form, on the episode's most sensitive beat, in an episode whose brand claim is that it does not do this.

**Replacement, line 468:**
> `**NARRATOR:** Different weapon. The Mark Fourteen's own defects had been fixed a year earlier.`

*(14 words to 13, minus one.)*

**Replacement, line 472:**
> `**NARRATOR:** Both marks shared one flaw. Neither had any protection against a circular run.`

*(13 words to 13, no change.)*

This is not just a correction, it is a **better ending for the argument the episode is making**. The episode's thesis is institutional: a weapon shipped without adequate testing. "The same unfixed hazard, shipped twice" lands harder than "a different weapon with a different problem," and it is what the record actually says. Keep the VISUAL at line 470 ("A technical note on plain paper describing an unsolved circular run problem") as is; it now matches the narration better than before.

---

**2. HARD FAIL. Act 5, scene 88.**

> **Claim as spoken:** "Dönitz got a board of inquiry. Four senior officers were court martialled."

**What is wrong.** The number **four** is single-sourced to Milford and is contradicted. Milford: "four senior officers being tried by court martial, on the order of Grand Admiral Eric Raeder, found guilty and punished." Against that, a Blair-derived account gives **three**: Rear Admiral Oskar Wehr, head of the Torpedo Testing Institute, "court-martialed and sentenced, along with two of his principal associates." uboat.net and *The Submarine Review* 1997 both confirm the court-martials and the prison terms but **give no number at all**. A specific integer, spoken flatly, unresolved between sources, inside the act whose entire function is to correct other people's overconfidence.

**Replacement, line 384:**
> `**NARRATOR:** Dönitz got a board of inquiry. Senior officers were tried by court martial.`

*(12 words to 13, plus one.)*

**Keep line 388 exactly as written.** "Convicted and punished. In the American case, nobody was held responsible at all." is triple-sourced (Milford "found guilty and punished"; uboat.net "sentenced to prison terms"; *The Submarine Review* 1997 "tried and condemned by court martial, served time") and is the hinge of the act. Nothing wrong with it.

**Three VISUAL tags must change too**, since they currently specify four. No narration impact.
- Line 382: `**[VISUAL: A German naval board of inquiry in session, several officers standing before a panel.]**`
- Line 386: `**[VISUAL: German officers being led out of a courtroom, verdict papers left on the table.]**`
- Line 490: `**[VISUAL: Teaser thumbnail, German naval officers standing before a court martial panel.]**`

---

**3. DEFECT. Act 5, scene 84.**

> **Claim as spoken:** "The record is more annoying. The German navy had the same three failures."

**What is wrong.** Milford wrote "**Almost** the same set." The script deleted the source's own hedge and stated the identity flatly. Milford also records a real asymmetry the script glosses: the German magnetic exploder carried a latitude-sensitivity adjustment the US device lacked, and the Germans abandoned it fairly quickly. Small, but this is the act that must not out-claim its evidence.

**Replacement, line 372:**
> `**NARRATOR:** The record is more annoying. Germany had almost exactly the same three failures.`

*(13 words to 13, no change.)* "Almost exactly" keeps the comic deflation while restoring Milford's hedge.

---

**4. DEFECT. Act 3, scene 52.**

> **Claim as spoken:** "The official history estimates prematures ruined perhaps ten percent of early war shots."

**What is wrong.** Rowland and Boyd do contain that sentence, so the line is not fabricated. But **the same chapter explicitly refuses to settle the figure and records a competing number**: "submariners were convinced that some 10 percent of the torpedoes they fired were prematures. The Bureau, analyzing combat reports as they were received, concluded that prematures did not exceed 2 percent of the total shots fired. **Whatever the truth**, ill feeling was the result." Presenting 10 percent as "the official history estimates" tells the audience the matter is settled when the cited source says in terms that it is not.

**Replacement, line 240:**
> `**NARRATOR:** Crews said ten percent were prematures. The Bureau's own analysis said two.`

*(13 words to 12, minus one.)*

Both numbers are verbatim from the same Tier 1 page, the line is now double-anchored instead of single-anchored, and it is **funnier and more on-theme** than the original: the gap between what the fleet saw and what the Bureau's paperwork concluded is the whole joke of Act 3. Keep the REUSE of scene 17 (the official history page); it still fits.

---

**5. DEFECT. Act 1, scene 13.**

> **Claim as spoken:** "May eighth, nineteen twenty six. Two shots at an old hulk. One worked."

**What is wrong.** Unresolved Tier 1 date conflict, asserted flatly. Rowland and Boyd give "May 8, 1926." **NHHC's own DANFS entry for L-8 and NHHC photograph NH 88457 both give 26 May 1926.** The day carries no argumentative weight whatever, so there is no reason to take a side.

**Replacement, line 72:**
> `**NARRATOR:** Nineteen twenty six. Two shots at an old submarine hulk. One of them worked.`

*(13 words to 14, plus one.)* The freed syllables go into "submarine hulk," which is also clearer for a listener than "old hulk."

**The two-shot version itself is fine and should be kept.** It contradicts the BuOrd official history, but NHHC is Tier 1 and its photo caption describes a torpedo that "passed under the hulked submarine L-8 (SS-48)... This torpedo failed to explode," corroborated by Wildenberg and Polmar and by Alpher. The hedge "By the better account" at line 76 stays.

---

**6. DEFECT, wording only. Act 6, scene 100.**

> **Claim as spoken:** "That was the highest loss rate of any American branch. About one in five."

**What is wrong.** "About one in five" is sourced, but to **one** source: NPS, "The US Navy Submarine Service had the highest casualty percentage of any American forces in the War: about 20%." NHHC's own losses volume gives different figures on different denominators: "16% of the officer and 13% of the enlisted operational personnel," and separately an 18 percent loss rate for **boats**. The word "loss rate" is the problem: it is the phrase NHHC attaches to boats, so on a beat about men dying it invites the listener to attach the wrong statistic to the wrong noun.

**Replacement, line 440:**
> `**NARRATOR:** That was the highest casualty rate of any American branch. About one in five.`

*(14 words to 14, no change.)* One word, "loss" to "casualty." It matches the NPS source's own noun exactly, it separates men from boats, and "About" already carries the hedge the spread requires. I am not asking for more than this: the claim is genuinely in a .gov source in these terms, and Act 6 must not be cluttered.

---

**7. DEFECT by omission, found by test 10. Act 3, scene 63.**

> **Claim as spoken:** "So the magnetic feature came out. Now the plain contact pistol had to work."

**What is wrong.** As heard, this tells the audience the magnetic exploder left the US submarine force in June 1943. It did not. Nimitz as CincPacFlt ordered only his own commands; Bowling names them: "ComSubPac and ComDesPac." Bowling continues: "**Not so for the boats in ComSubSoWestPac**, Lockwood's former command but not under Nimitz's theater command, where Admiral Ralph Christie ordered that the magnetic feature be retained. Still, it was not until March 1944 that it was inactivated in SoWestPac submarines." Milford gives December 1943 for the same event. The holdout was deliberately cut, which is a defensible call, but the cut leaves a remaining sentence that is false as spoken.

**Replacement, line 276:**
> `**NARRATOR:** At Pearl the magnetic feature came out. Now the contact pistol had to work.`

*(14 words to 14, no change.)* One added word, "Pearl," and one dropped, "plain." It scopes the claim correctly, needs no dates, and **names nobody**, so the no-single-villain rule of Act 5 is untouched.

---

**8. BUILD NOTES. No narration change required.**

- **Scene 16, line 82.** The VISUAL reads "A calendar wall spanning nineteen twenty six to nineteen forty one" while the narration says "Nineteen years." 1926 to 1941 is fifteen years. The official history's "19 years of prewar exploder development" runs from the **1922** project start, which is the year the script itself gives at scene 9. The narration is faithful to the source; the picture mis-frames it and invites the listener to think nineteen years elapsed after 1926. **Fix the tag, not the line:** `**[VISUAL: A calendar wall spanning nineteen twenty two to nineteen forty one, every year blank.]**`
- **Spelling for TTS, lines 344 and 348.** "aluminium" will be read by a US narrator voice as *al-yoo-MIN-ee-um*. This is a US Navy episode. Change the spelling in both spoken lines to **"aluminum"**. Not a word-count change and not a factual change; Milford's own text uses "aluminum alloy."
- **Pronunciation flags for the VO pass:** "Dönitz" (DOH-nits), "Kahoolawe" (kah-hoh-oh-LAH-vay), "Tinosa" (tih-NOH-sah), "Daspit" (DAS-pit).

---

## Tone check

**PASS. No joke touches a death beat.**

- **The jokes stop before the casualties, and they do not resume.** I read every beat from scene 95 to the end. Act 6 opens on "A number of submarine skippers were relieved of command during those months" and contains no joke, no sarcasm, no aside, and no second-person address. The outro contains none either. The last comic beat in the episode is in the first third of Act 5; Act 5 then tapers deliberately through "There is no single villain here. That is the uncomfortable part," which is thesis, not punchline. That taper is better craft than a hard cliff would have been, because the audience is already quiet by the time Act 6 starts.
- **The death beats are clean.** "About three thousand five hundred officers and enlisted men died in them," "Fifty two American submarines were lost in the Second World War," and "Seventy eight men died. Nine survived." carry nothing but the fact. "Seventy eight men died. Nine survived." is the shortest beat in the episode at six words, over a still dark image with floating debris. That is the right instinct and the build note to hold it longest is right.
- **The one beat I checked hardest and cleared:** the German court-martial beat, "Convicted and punished. In the American case, nobody was held responsible at all." There is a version of this that reads as gloating over prosecuted men. As written it is flat comparison, not cheering, and the build note already says it "must not sound like cheering." Keep that note and enforce it in the VO.
- **The other beat I checked hardest and cleared:** "By the crew's account, Japanese sailors came to the rail and pointed at them." The humiliation lands on the Americans, not on the enemy crew, and nobody dies in the scene, because the ship survives. Not a human-cost beat. Clean.
- **No music sting anywhere from Act 6 to END**, per the build notes. Enforce it.

**The non-straight acts are genuinely funny. This is not a flat documentary read.** The comedy is where it should be, in the paperwork and the physics, and the strongest beats are structural rather than gag-based: "The instrument checking for the error was wrong by the error. Take a second." is the best line in the script. "It is a pin. It hits a cap. You are already ahead of me." earns the act break. "Then Admiral King got involved, and Newport re-investigated with impressive new enthusiasm" is the right register of dry. The four Bureau lines work as a running character and the decision to voice them as one smug institution rather than three officials is correct. Issue 4's replacement adds a joke rather than removing one, so the comedy density does not drop.

---

## Cold read notes

Read end to end aloud, as TTS will hit it.

- **Nothing to trip the reader.** Zero em-dashes, zero brackets, zero digits, zero markup inside any spoken line. Every number is spelled out. This is clean and I have nothing to add.
- **The 9 / 8 / 5 sequence in the outro may sound like broken arithmetic on first listen.** The audience hears "Nine survived," then "Eight reached the surface. Five were still swimming when help arrived." The real accounting is five from the escape trunk plus three from the bridge plus one from the conning tower, which is nine. Nothing false is said and every figure is verbatim from the official losses volume, so I am **not** requiring a change and I would not want words added to that beat. Flagging it only so the edit does not cut the hold short: the pause between those two beats is doing the work.
- **"Twenty one months. Three defects. Each had been hiding the one behind it."** closing Act 4 is the best structural payoff in the script and the REUSE of scene 8 there is well judged.
- **The cold open plant and payoff works.** Scenes 2, 5 and 6 return at 64, 67 and 69, and the audience does not learn until Act 4 that the cold open was the third defect rather than the first. That is a real structural argument and it survives all the fixes above untouched.
- **Act 5 is the best-sourced act in the script** once Issues 2 and 3 are applied, and it is the act most likely to draw comments. The "certainly an overstatement" quotation is authentic, in context, and correctly attributed to an unnamed "best analytical source" rather than over-claimed.
- **After the fixes, the running time is unchanged:** 1,405 narration words, 8:54 at the measured 158 wpm, 8:07 at the fast end of the observed range. Still clear of the 8:00 mid-roll floor.

---

## Standing warning about the fact-check log

**The script's own FACT-CHECK LOG contains at least three wrong citations and must not be trusted downstream as a build reference.** The claims are mostly fine; the attributions are not.

1. **The Mark 18 sentence is attributed to NHHC H-Gram 008-3 as verbatim. It is not in that document.** It is Wikipedia wording, and its real version says the opposite of what the script built on it. This is Issue 1 and it is the most serious.
2. **The Chesapeake Bay parallel investigation is attributed to Milford.** Milford does not mention Chesapeake Bay anywhere. The real and better source is Rowland and Boyd, verbatim, including "both series of tests gave the same results." The on-screen line is correct; only the citation is wrong.
3. **The oblique-shot halving is attributed to NHHC H-Gram 008-3.** NHHC says only that oblique angles "actually did help reduce the dud problem" and **does not quantify**. The halving traces to Blair. The on-screen line survives, because Blair is a named credentialed historian, but it is single-sourced and the log misrepresents its strength.

Two of the three are harmless to the audience. The first is not. The pattern to note is that all three errors move a claim *up* the source tier, which is the direction that hides risk. Whoever builds from this script should re-verify against the sources listed at the top of this report rather than against the log.

---

## Summary of verdicts

**Verified and strong (no action):** the Tinosa cold open and the official history's own arithmetic; the 1922 project start; the Mark 5 decoy exploder; the 1938 sand incident; the 1939 physicist; no pre-war live-fire test; Sargo, Jacobs and the eighteen seconds; the ten-foot depth error and the self-cancelling depth recorder; Frenchman's Bay at Albany, Western Australia; the 850-yard net shot; King's intervention; 1 August 1942; over eight hundred fired; the Rube Goldberg quotation; the BuOrd arming-distance proposal and King's refusal; **24 June 1943 and the named conflict with the official history**; Daspit's rank, range and track; the Haddock; Kahoolawe; **the 90-foot drop test and its physics**; seven of ten and seventy percent; the bent guide pins; the aluminium firing pin; the Holland; the Barb on 30 September; twenty one months; the Chesapeake Bay parallel investigation; the Newport monopoly from 1923; the three structural causes; all four Bureau of Ordnance voice lines; the Act 6 skipper beats verbatim from NHHC; 52 boats and about 3,500 men; Tang's patrol record, the Mark 18 identification, 78 and 9, and 13, 8 and 5.

**Structural:** clean on every count. 1,405 words, zero beats over 14, 112 tags, 11 valid backward reuses, zero camera moves, zero em-dashes, zero shorthand in spoken lines, nine sections in order, every act on a hook.

**Tone:** clean. No joke touches a death beat. The straight material is straight and the comic material is funny.

**Must fix before build:** Issues 1 and 2 are hard fails. Issues 3 through 7 are defects. Issue 8 is build notes. All fixes are supplied verbatim and are word-count neutral in aggregate.

Once Issues 1 through 7 are applied as written, I would pass this script. As it stands, it ships an inverted correction about the Mark 18 on the Tang beat and an unresolved single-sourced number in the myth-correction act, and those are exactly the two failure modes this episode exists to avoid.

*(The verdict above was loop 1. It is superseded by the re-gate below.)*

---
---

# RE-GATE, LOOP 2 OF 2

Scoped as instructed. **I did not re-verify the roughly ninety claims I passed in loop 1.** This pass covers only: whether my seven items were applied and applied correctly, collateral damage from the edits, a full re-audit of the fact-check log against the actual sources, a fresh structural run, and a diff for unreviewed changes.

## 1. Were the seven items applied, and applied correctly?

**All seven applied. All seven verbatim, character for character, against the wording I supplied.** No paraphrase, no drift.

| # | Item | Line | Applied wording | Match |
|---|---|---|---|---|
| 1a | Mark 18, "different fault" removed | 468 | "Different weapon. The Mark Fourteen's own defects had been fixed a year earlier." | EXACT |
| 1b | Shared-flaw replacement | 472 | "Both marks shared one flaw. Neither had any protection against a circular run." | EXACT |
| 2 | German integer dropped | 384 | "Dönitz got a board of inquiry. Senior officers were tried by court martial." | EXACT |
| 2 | Convictions line untouched | 388 | "Convicted and punished. In the American case, nobody was held responsible at all." | UNCHANGED, as required |
| 2 | Three VISUAL tags de-numbered | 382, 386, 490 | "several officers standing before a panel" / "German officers being led out of a courtroom" / "Teaser thumbnail, German naval officers standing before a court martial panel" | EXACT on all three |
| 3 | Milford's hedge restored | 372 | "The record is more annoying. Germany had almost exactly the same three failures." | EXACT |
| 4 | Both premature figures spoken | 240 | "Crews said ten percent were prematures. The Bureau's own analysis said two." | EXACT |
| 5 | 1926 day dropped | 72 | "Nineteen twenty six. Two shots at an old submarine hulk. One of them worked." | EXACT |
| 6 | Noun corrected | 440 | "That was the highest casualty rate of any American branch. About one in five." | EXACT |
| 7 | Claim rescoped | 276 | "At Pearl the magnetic feature came out. Now the contact pistol had to work." | EXACT |
| 8 | Calendar VISUAL recut | 82 | "A calendar wall spanning nineteen twenty two to nineteen forty one, every year blank." | EXACT |
| 8 | Spelling for TTS | 344, 348 | "aluminum" in both spoken lines | EXACT |

**The recut calendar span is right.** Rowland and Boyd's phrase is "the 19 years of prewar exploder development," and the script's own scene 9 dates the project start to "Nineteen twenty two." 1922 to 1941 is nineteen years. The old tag said 1926 to 1941, which is fifteen, and made the spoken "Nineteen years" look like an error on screen. Now the picture and the line agree.

## 2. Collateral damage from the edits

This was the real risk and I checked all four of the coordinator's specific questions.

**a) Does "Different weapon." still stand alone, heard in sequence with no pause?** **Yes, and the pair is stronger than what it replaced.** As a viewer hears it:

> "That torpedo was a Mark Eighteen electric. It was not a Mark Fourteen."
> "Different weapon. The Mark Fourteen's own defects had been fixed a year earlier."
> "Both marks shared one flaw. Neither had any protection against a circular run."

"Different weapon" is now a statement of **identity**, not of fault, and it is simply true: the Mark 18 is a different weapon from the Mark 14. The fault claim, which was the wrong part, has moved to the third beat where it is stated correctly. There is no contradiction between beats two and three, and the reason is the word **"own"**, which is doing real load-bearing work. The episode has defined "three defects" explicitly and repeatedly, in the cold open ("There were three separate faults") and at the close of Act 4 ("Twenty one months. Three defects."). So "the Mark Fourteen's **own** defects" reads unambiguously as those three, and the third beat then introduces a fourth thing that was shared and never fixed. That is exactly NHHC's structure: "The fourth major problem with the Mark 14 was a tendency to run in circles... this problem was never completely solved." Three fixed, one shared and unfixed. The arc resolves rather than confuses, and the Tang beat now lands on the episode's actual institutional thesis instead of on a false distinction. **No replacement wording needed.**

**b) Is "Senior officers were tried by court martial" supportable as plural, and does the teaser still match?** **Yes on both.** Plural is supported by every source regardless of whether the true count is three or four: Milford "four senior officers"; the Blair-derived account, Wehr "along with two of his principal associates," which is three; uboat.net "the personnel of the Torpedo Experimental Institute... were court-martialed and sentenced to prison terms"; *The Submarine Review* 1997 "Senior officials were tried and condemned by court martial." Plural is the one thing all four agree on, which is precisely why dropping the integer works. The elliptical next beat, "Convicted and punished," still attaches cleanly to "Senior officers" as its subject. The teaser thumbnail now reads "German naval officers standing before a court martial panel" against narration "the men they prosecuted": both plural, neither numbered, so the next episode is no longer pre-committed to a count it may not be able to defend. **Match confirmed.**

**c) Does "At Pearl" read as a dangling qualifier?** **No.** Pearl Harbor is established three times in the immediately preceding beats: the Nimitz VISUAL at scene 58 ("at a desk at Pearl Harbor"), the message VISUAL at scene 60 ("arriving at Pearl Harbor"), and most importantly the VISUAL sitting directly on this line, "Crews at Pearl Harbor pulling magnetic units out of a rack of torpedo exploders." So "At Pearl" lands on a picture of Pearl Harbor and reads as a plain location anchor. For a viewer who does not know the Pearl versus Southwest Pacific distinction, the line simply says "at Pearl Harbor they pulled the magnetic units," which is what the image shows. It raises no unanswered question and draws no attention to the omission. That is the correct behaviour for a cut we chose to make: it stops the false universality without importing the holdout story. "Pearl" alone is also authentic naval usage and reads naturally for TTS.

**d) Does the scene 110 VISUAL re-imply the cut "rushed into service" claim?** **No, and leaving it was right.** The tag reads "A technical note on plain paper describing an unsolved circular run problem." The word "unsolved" is now the most defensible word in the tag: it is NHHC's own claim, "this problem was never completely solved." Critically, the tag no longer attaches that to the Mark 18 specifically, because the narration it sits under says "Both marks shared one flaw." So the image now supports the corrected narration rather than the cut one. No change needed.

## 3. Re-audit of the FACT-CHECK LOG, against the sources rather than the writer's description

I re-read every rewritten row and checked its quotations against the source texts I retrieved myself in loop 1. **The three misattributions are genuinely fixed, and fixed honestly rather than cosmetically.** Eight further rows were rewritten and I checked those too.

| Row | What it now claims | Verified against source | Verdict |
|---|---|---|---|
| Oblique shots / halving | NHHC "does not quantify it" and supports only the tactic, quoting "actually did help reduce the dud problem"; the halving "is not NHHC. It traces to Blair"; explicitly labels it single-sourced and states the row "previously credited it to NHHC, which moved the claim up a tier it had not earned" | Both quotations match the H-Gram and the Blair-derived wording exactly as I pulled them | **CORRECTED, and correctly self-critical** |
| Chesapeake Bay | "Chesapeake Bay is Rowland and Boyd, not Milford," with three verbatim quotations; "Milford does not mention Chesapeake Bay anywhere"; Milford retained only for the separate "notably prompt" assessment | All three Rowland and Boyd quotations are character-for-character correct. My grep of Milford confirms zero occurrences of "Chesapeake." **I also checked the one remaining Milford attribution: "notably prompt" is verbatim Milford**, "their response, once the difficulty had been identified, was notably prompt" | **CORRECTED, and the residual attribution checks out** |
| Mark 18 / circular runs | States plainly that the previously quoted sentence "is NOT in H-gram 008-3," identifies it as Wikipedia wording, quotes Wikipedia's real opening "The Mark 18 **shared one major flaw with the Mark 14**," calls that "the opposite of the 'different fault' the narration had been built on," and records that "'Rushed into service' was unsourced editorialising and is gone" | Matches my own retrieval exactly, including the H-Gram quotation on the Mark 14 | **CORRECTED. This is the model of how a log row should own an error** |
| German court martial | Convictions triple-sourced with correct verbatim from Milford, uboat.net and the 1997 article; records that "four" is Milford alone and contradicted by the three-officer account; notes the integer is gone from narration and all three VISUAL tags | Every quotation matches my retrieval | **ACCURATE** |
| German three failures | Restores Milford's "**Almost** the same set" with the full verbatim sentence; records the deleted hedge; notes the latitude-sensitivity asymmetry is not contradicted on screen | Milford quotation is exact | **ACCURATE** |
| Prematures | Both figures, with the full Rowland and Boyd passage including "Whatever the truth, ill feeling was the result"; records that the earlier draft "told the audience a matter was settled that the cited source explicitly declines to settle" | Exact | **ACCURATE** |
| 1926 test | Now carries **both** conflicts: the one-shot versus two-shot dispute, hedged on screen, and the 8 May versus 26 May date conflict, avoided by not stating a day. Quotes the NHHC photo caption correctly | Exact | **ACCURATE, and more complete than my loop 1 note required** |
| Casualty rate | Boat and death counts double-sourced with my own 374 plus 3,131 arithmetic reproduced; the rate explicitly labelled as resting on NPS alone, with NHHC's 16/13 percent and 18 percent figures set out; records the "loss rate" to "casualty rate" correction | Every figure matches | **ACCURATE, and correctly declares the single-sourcing rather than hiding it** |
| Southwest Pacific holdout | Records that Nimitz could order only ComSubPac and ComDesPac, that the earlier "So the magnetic feature came out" was "false as heard," and that "At Pearl" scopes it | Matches Bowling | **ACCURATE, and it documents why "At Pearl" is load-bearing, which protects it from being trimmed later** |

**The log is now trustworthy.** Every correction moves a claim **down** the source tier or admits single-sourcing, which is the opposite of the pattern I flagged in loop 1, where all three errors moved claims up. Nothing in the rewritten log overstates support.

## 4. Structural checks, re-run with my own script

Verified, not accepted.

| Check | Requirement | Measured | Verdict |
|---|---|---|---|
| Narration words | 1,390 to 1,410 | **1,405** (1,406 with hyphens split) | PASS, unchanged, exactly as I predicted the eight edits would net out |
| Longest beat | max 14 | **max 14, zero violations** | PASS |
| Average / shortest | 12.5 / 6 | **12.54 / 6** | PASS |
| VISUAL tags | near 112 | **112** | PASS |
| REUSE | 11, all backwards, all matching | **11 of 11 resolve to a lower scene index and repeat the source tag character for character** | PASS |
| Camera moves | none | **zero.** Only regex hit is "spanning" in the recut scene 16, which is not a camera move | PASS |
| Em-dashes / en-dashes | zero | **zero of both**, across the entire file including notes, log and sources | PASS |
| Shorthand in spoken lines | none | **zero** brackets, parentheses, digits or markup in any of the 112 spoken lines | PASS |
| Nine sections in order | required | Present and in order, ending [END] | PASS |

The word count landing back on exactly 1,405 confirms the edits were applied as specified rather than approximated.

## 5. Was anything touched that I did not raise?

**No. Zero unreviewed content.** I dumped all 112 spoken lines and all 112 VISUAL tags from the revised script and compared them line by line against the original I hold verbatim from loop 1. **The only differences anywhere in the script body are the twelve changes listed in section 1**, every one of which I specified. Nothing else moved: not a word of narration, not a VISUAL tag, not a section header, not an act boundary. I also re-derived the scene indices and confirmed the numbers the production notes cite are still right (Frenchman's Bay at scene 42, Bureau voices at 21, 25, 45 and 56).

## 6. What is still wrong, and it is all off screen

**Nothing the audience sees or hears is wrong.** Every remaining defect is in the build-facing documentation, and two of them create a live path for the cut claim to come back.

**A. The ACCURACY NOTE still carries the cut framing, and it is the document that instructs the build.** Point (5) reads: "Tang is framed as the Navy shipping another **under-tested** torpedo, never as the Mark 14's last victim." Nothing in the record supports the Mark 18 being under-tested; that is the same unsourced characterisation family as the "rushed into service" line we cut, sitting in the one note headed "Do not re-simplify any of them back into the myth." A build agent following this directive could reintroduce exactly the claim that was the most serious error in loop 1. **This is the highest-risk item remaining.**

**B. Log row on the Mark 18 disambiguation still quotes the cut line as current script content.** It says the disambiguation is "spoken twice, once as the type and once as the **'different weapon, different fault'** line." That line no longer exists. The row immediately below correctly kills it, but this row asserts it as present.

**C, D, E.** Three stale quotations of superseded narration, caught by testing every quoted string in the notes against the actual spoken lines: production notes point 1 quotes "Now the plain contact pistol had to work" (the word "plain" was dropped); production notes point 8 and one log row quote "aluminium" in what they present as current narration (now "aluminum"); and one log row title still frames the gap as "the nineteen years after 1926," which is the mis-framing the recut calendar fixed.

## 7. Required edits, verbatim and surgical

Five find-and-replace operations. **None touches a spoken line. Narration stays at exactly 1,405 words and no VISUAL tag changes.**

**A. Line 8, ACCURACY NOTE.**
Find: `Tang is framed as the Navy shipping another under-tested torpedo, never as the Mark 14's last victim.`
Replace: `Tang is framed as the same unfixed hazard shipped twice, never as the Mark 14's last victim.`

**B. Line 606, log row on the Mark 18.**
Find: `**This is the episode's single most important disambiguation and it is spoken twice, once as the type and once as the "different weapon, different fault" line**`
Replace: `**This is the episode's single most important disambiguation and it is spoken twice, once as the type at scene 105 and once as the "Different weapon" line at scene 106. The "different fault" half of that line was wrong and was cut; see the row below**`

**C. Line 513, production notes point 1.**
Find: `"Now the plain contact pistol had to work"`
Replace: `"Now the contact pistol had to work"`

**D. Lines 520 and 591, three quotations of current narration.**
Find: `machined from aluminium instead of steel` Replace: `machined from aluminum instead of steel`
Find (two occurrences, line 520 and line 591): `the aluminium came from downed Japanese planes` Replace: `the aluminum came from downed Japanese planes`

**E. Line 552, log row title.**
Find: `No destructive test of the magnetic exploder in the nineteen years after 1926`
Replace: `No destructive test of the magnetic exploder across the nineteen years of prewar exploder development, 1922 to 1941`

**Optional, cosmetic, not required:** the VISUAL at line 342 still reads "a small bright aluminium component." It is an image prompt and is never spoken, so it carries no TTS or accuracy risk. Change it only if you want spelling consistency. Also pre-existing and not raised by me: the voice-choices bullet says the Bureau "speaks three times" and then describes a fourth voice; the Manager decision line below it already resolves this by naming all four scenes, so no action is needed.

## 8. Verdict reasoning

Everything that reaches the audience is now verified and correct. The two hard fails from loop 1 are properly fixed, not papered over: the Mark 18 beat now states the sourced relationship and, as I said it would, ends the episode on a stronger institutional argument than the error did; and the German court-martial beat asserts only what all four sources agree on. The five defects are fixed exactly as specified. The structural profile is unchanged and clean. The log has gone from actively misleading to genuinely useful, and it now documents its own former errors, which is the best protection against their return.

What remains is documentation hygiene, but items A and B are not cosmetic: they are a directive and a claim-of-record that still carry the cut wording, in the two documents a build agent is most likely to follow. They must be applied before build. They are five text replacements in non-spoken material and change no word of the episode.

**This is a conditional pass. Applying the five edits in section 7 converts it to an unconditional PASS. No spoken word, VISUAL tag, or word count changes when you apply them.** I am passing rather than failing because the broadcast content is clean and fully verified, and because blocking on stale wording in a note, when the fix is five find-and-replaces, would be disproportionate at loop 2 of 2.

VERDICT: PASS

---

## Manager close-out

The five documentation edits specified in section 7 (A through E, six replacements including the two occurrences of the aluminium spelling) were applied verbatim on 2026-09-01. Each was verified to occur exactly the expected number of times before replacement, so nothing was over-applied.

No spoken line, VISUAL tag, or word count changed. Narration remains 1,405 words across 112 beats, 112 VISUAL tags, 11 REUSE, 101 unique generations.

Per the QA agent's own statement, "Applying the five edits in section 7 converts it to an unconditional PASS." That condition is now satisfied. This is the QA agent's conditional PASS taking effect, not a new Manager judgement, and no Manager edit was made to any spoken content.

The optional cosmetic item (the "aluminium" spelling inside the VISUAL at line 342) was deliberately left alone. It is an image prompt, never spoken, and carries no TTS or accuracy risk.

VERDICT: PASS
