# Responder Comments -- Target Accounts

Last updated: 2026-06-01
Maintained by: `/first-responder-engagement:responder-research`
Status: Web-verified seed list (department, unit, association, and charity accounts). Individual first responder accounts still need to be added via the in-Cowork Instagram browse. See "What still needs the Cowork run" below.

> **This is the FIRST RESPONDER list. Keep it separate.** It must never be merged with the `lender-engagement` plugin's `target-accounts.md`. Different audience (community presence with first responders, not competitor loan officers), different voice (28-year Vegas neighbor, never a lender), different goals. If you ever find a lender LO on this list, remove it.

---

## What was done on this run (2026-06-01)

This run was executed from Claude Code (CLI), which does **not** have the Playwright Instagram browser attached. Discovery was therefore done by **web verification**, not by browsing Instagram. Every handle in the Active Accounts table below was confirmed to be a real, public, active account via web search on 2026-06-01.

Corrected handles (the prior seed file had several wrong guesses):

- Henderson Fire is **@hendfiredept** (was `@hendersonfire`)
- Las Vegas Fire & Rescue is **@lasvegasfd** (was `@lasvegasfirerescue`)
- UMC is **@umcsn** (was `@umc_lasvegas`)
- Henderson PD is **@hendersonpolicedepartment** (was `@hendersonnvpd`, which is the X/Twitter handle)
- Nevada Highway Patrol rolls up under **@nvstatepolice** (was `@nvhighwaypatrol`)

## What still needs the Cowork run

The core of this skill is finding **individual** first responders (the personal accounts of firefighters, officers, airmen, nurses). Those cannot be added responsibly from web search alone without risking adding the wrong person, so they are intentionally NOT invented here. To populate them:

1. Open Cowork with the `playwright-instagram` MCP connected and @espohomeloans logged in.
2. Run `/first-responder-engagement:responder-research`.
3. It will mine the verified seed accounts below (who they tag, who comments) to find real individuals, verify each per `references/research-methodology.md`, and append them to this table.

Biggest gap: **healthcare individuals.** Hospital corporate accounts are easy to verify; individual nurses and doctors are not. Prioritize that category on the first Cowork run.

---

## Active Accounts (web-verified 2026-06-01)

Type key: **Official** = department/agency PR account; **Unit** = sub-unit (K9, residency, etc.); **Assoc** = union/association/personnel account; **Charity** = foundation/nonprofit.

### Military / Veterans
| Handle | Name | Branch | Type | Notes |
|--------|------|--------|------|-------|
| @nellisafb | Nellis Air Force Base | USAF | Official | ~158k followers. Airshow, mission, and community content. High volume, well moderated. |
| @creechafb | Creech AFB / 432nd Wing | USAF | Official | ~5.7k. Smaller base (Indian Springs). |
| @nevadanationalguard | Nevada National Guard | Army/Air NG | Official | ~6.3k. "Battle Born, Battle Ready." Community and service content. |

### Police / Law Enforcement
| Handle | Name | Agency | Type | Notes |
|--------|------|--------|------|-------|
| @lvmpd | Las Vegas Metro PD | LVMPD | Official | ~117k. Main Metro account. |
| @lvmpdk9 | LVMPD K9 Section | LVMPD | Unit | ~18k. K9 content is some of the safest, warmest engagement on this whole list. |
| @lvmpdfoundation | LVMPD Foundation | LVMPD | Charity | ~6.9k. Fundraisers and community programs. Strong fit for Brian's charity and Par for the Cure voice. |
| @hendersonpolicedepartment | Henderson PD | HPD | Official | Community and recruiting content. |
| @northlasvegaspd | North Las Vegas PD | NLVPD | Official | Confirm activity in-app. |
| @nvstatepolice | Nevada State Police | NSP / NHP | Official | Includes the Highway Patrol. Statewide, so filter for Southern Command / Vegas posts. |

### Fire / EMS
| Handle | Name | Agency | Type | Notes |
|--------|------|--------|------|-------|
| @clarkcountyfd | Clark County Fire Dept | CCFD | Official | ~10k. Covers the Strip. Bio notes it is not monitored 24/7. |
| @clarkcountyfirefighters | Clark County Firefighters | CCFD | Assoc | Personnel/association account, more human-interest than the dept PR account. Screen for political posts. |
| @hendfiredept | Henderson Fire Dept | HFD | Official | ~9.6k. |
| @hendersonpff | Henderson Pro Fire Fighters | HFD | Assoc | Firefighters association account. Good people content; screen for endorsement/political posts. |
| @lasvegasfd | Las Vegas Fire & Rescue | LVFR | Official | City of Las Vegas fire department. |
| @lasvegasfirefighters | Las Vegas Firefighters | LVFR | Assoc | Firefighters association. Charity and people content; screen for political posts. |
| @nlvfiredepartment | North Las Vegas Fire | NLVFD | Official | Confirm activity in-app. |

### Healthcare
| Handle | Name | System | Type | Notes |
|--------|------|--------|------|-------|
| @umcsn | UMC Southern Nevada | UMC | Official | Nevada's only Level I Trauma, transplant, and burn center. |
| @sunrisechildrenshospitallv | Sunrise Hospital & Children's | Sunrise | Official | ~2.5k. |
| @sunrisehealth_emresidency | Sunrise EM Residency | Sunrise | Unit | Resident physicians. More personal than the corporate account. |

**Healthcare NOT FOUND via web (confirm in-app):** St Rose Dominican (Dignity Health) and Henderson Hospital Instagram handles were not confirmed by web search (Facebook pages exist, Instagram unconfirmed). Valley Hospital, MountainView, Spring Valley, and Summerlin Hospital handles also not yet verified.

---

## Screening note for Assoc / union accounts

The association and union accounts (@clarkcountyfirefighters, @hendersonpff, @lasvegasfirefighters, and similar) post the best human-interest content (promotions, charity, line-of-duty honors), which makes them great engagement targets. But they also occasionally post **endorsements, ballot measures, or contract/political content.** Apply the skip guardrails strictly on those accounts: skip any political, endorsement, or labor-dispute post entirely.

---

## Additional agencies to mine (handles unverified, confirm in-app)

These are legitimate Vegas-area sources to mine for individuals during the Cowork run, but their handles were not web-verified on this pass. Confirm each in-app before adding.

- **Police:** Boulder City PD, Clark County School District PD, UNLV Police, @nlvpdrecruiting (NLVPD recruiting)
- **Fire / EMS:** Boulder City Fire, AMR Las Vegas, MedicWest Ambulance, Nevada State Fire Marshal
- **Military / Veterans:** local VFW posts (search "VFW Post [number] Las Vegas"), American Legion local posts, Nevada veteran community groups
- **Healthcare:** St Rose Dominican (Siena/San Martin/Rose de Lima campuses), Henderson Hospital, Valley Hospital, MountainView, Spring Valley, Summerlin Hospital

---

## Excluded Accounts (never target)

- Out-of-state first responder accounts (and out-of-area Nevada, e.g. Reno-only such as @nevadaairguard, which is Reno-based)
- Department accounts that ONLY post PR releases with no community/human content
- Accounts that primarily post political / activist / endorsement content
- Accounts with comments turned off
- Any mortgage or real estate accounts (those belong to the lender plugin, not here)

---

## Research Hashtags / Search Terms

For the `/first-responder-engagement:responder-research` skill to discover individual accounts during the Cowork run:

**Hashtags (filter for Vegas / Henderson / Clark County geo):**
- #lvmpd #vegaspolice #thinblueline
- #vegasfire #vegasff #clarkcountyfire #hendersonfire #lvfr
- #nellisafb #nellisstrong #nvguard
- #vegasnurse #vegasrn #umclasvegas #vegashealthcare

**Search terms / bio keywords:**
- "Las Vegas police officer," "Henderson firefighter," "Vegas paramedic," "Nellis airman"
- "Vegas veteran," "Vegas nurse," "RN UMC," "Sunrise nurse," "Henderson Hospital ICU"
- "LVMPD," "CCFD," "LVFR," "USAF Nellis"

---

## Notes

- Aim for 20-30 active **individual** accounts once the Cowork run populates them, balanced across all four categories (5-8 each). The institutional/association accounts above are seeds and immediate engagement targets, not the end state.
- Remove accounts that move out of the Vegas area, go inactive (no posts 60+ days), or shift to primarily political content.
- This list is for community presence engagement only, never business prospecting.
