# MLS Matrix Residential Listing Entry — Claude Instructions

## PURPOSE
This document gives Claude all the context needed to fill out a Las Vegas MLS Matrix Residential Listing Input form (https://las.mlsmatrix.com) from a structured data sheet. The user (Ryan Rose, Real Broker LLC) will provide a completed data sheet (PDF or text) and have the MLS Matrix "Add/Edit > Residential" input form open in Chrome. Claude will use Claude-in-Chrome browser tools to fill in each tab systematically.

---

## CRITICAL RULES

1. **Tab-by-tab workflow.** Complete one tab fully, then tell the user "Tab X is done — hit Next when ready." The user must click Next to advance tabs (Claude cannot navigate between tabs reliably by clicking the tab links while editing).
2. **Accuracy over speed.** Double-check every value against the data sheet before moving on.
3. **Use `find` tool first.** When you can't see a field, use `find` to locate it by label text rather than guessing ref IDs. Ref IDs change between sessions.
4. **Dropdowns use `form_input`.** Set dropdown/combobox values with `form_input` using the option's `value` attribute (e.g., `value="1"` for Yes, `value="0"` for No).
5. **Checkboxes use `left_click`.** Click checkboxes directly — do NOT use `form_input` with boolean.
6. **Multi-select listboxes use JavaScript.** When a field needs multiple selections (e.g., Kitchen description = Island + Pantry), use `javascript_tool` to set multiple `.selected = true` on the `<select>` element, then dispatch a `change` event.
7. **Yellow fields are required.** If the data sheet is missing a required field value, note it to the user so they can fill it manually.
8. **Screenshot after each section** to verify entries visually.

---

## TAB 1: GENERAL

### Field Order (top to bottom, left to right)

| Field | Type | Notes |
|-------|------|-------|
| Property Type | dropdown | Usually pre-set to "SFR" (Single Family Residential) |
| Listing Type | dropdown | ER = Exclusive Right, EX = Exclusive Agency, etc. |
| List Price | text | Numbers only, no $ or commas (e.g., `485000`) |
| Street Number | text | e.g., `29` |
| Street Name | text | e.g., `Amber Rock` |
| Street Suffix | dropdown | St, Ave, Dr, Ln, Blvd, etc. |
| Direction Prefix/Suffix | dropdown | N, S, E, W if applicable |
| Unit Number | text | If applicable |
| City | dropdown | Henderson, Las Vegas, North Las Vegas, etc. |
| State | dropdown | Usually pre-set NV |
| Zip Code | text | 5-digit zip |
| County | dropdown | Clark |
| APN (Parcel Number) | text | Format: XXX-XX-XXX-XXX |
| Subdivision | text | Builder subdivision name |
| Year Built | text | 4-digit year |
| # Stories | dropdown | 1, 2, 3, etc. |
| # Bedrooms | text | Number |
| # Full Baths | text | Number |
| # Half Baths | text | Number |
| # Three Quarter Baths | text | Number |
| Approx SF (Above Grade) | text | Living square footage |
| Lot Size (SF) | text | Lot square footage |
| Lot Size (Acres) | text | Decimal acres |
| Garage | dropdown | Number of cars |
| Garage Type | dropdown | Attached, Detached, etc. |
| Builder Name | text | Original builder |
| Zoning | dropdown | Single Family, Multi-Family, etc. |
| Built Description | dropdown | Resale, New, Under Construction |
| Legal Description | text | If provided |

### Key Tips for General Tab
- The `find` tool works well for locating fields like "Subdivision" or "APN"
- List Price field often reformats after entry — verify with screenshot
- Parcel number format varies — enter exactly as on data sheet
- After filling all visible fields, scroll down to check for additional fields below the fold

---

## TAB 2: FEATURES

### Field Order

| Field | Type | Notes |
|-------|------|-------|
| Appliances | multi-checkbox | Check each that applies: Dishwasher, Disposal, Dryer, Gas Oven, Microwave, Oven, Range, Refrigerator, Washer, etc. |
| Cooling | multi-checkbox | Central, Evaporative, None, Wall Unit, etc. |
| Heating | multi-checkbox | Central, Electric, Gas, None, etc. |
| Fireplace | dropdown (Y/N) + count + checkboxes | If Yes, enter count and check types (Gas, Wood, etc.) |
| Flooring | multi-checkbox | Carpet, Ceramic Tile, Hardwood, Laminate, Tile, Vinyl, etc. |
| Pool | dropdown (Y/N) + type | Private Pool Y/N, then Community/Private/None, In-Ground/Above |
| Spa | dropdown (Y/N) + type | Similar to pool |
| Construction | multi-checkbox | Block, Frame/Wood, Stucco, etc. |
| Roof | multi-checkbox | Tile, Composition/Shingle, Flat, etc. |
| Fence | multi-checkbox | Block, Wrought Iron, Partial, Complete, etc. |
| Landscape | multi-checkbox | Desert/Natural, Full, Front Only, None, etc. |
| Parking | multi-checkbox | Garage Door Opener, etc. |
| Lot Description | multi-checkbox | Corner, Cul-de-Sac, Irregular, etc. |
| Interior | multi-checkbox | Blinds, Ceiling Fan, etc. |
| Exterior | multi-checkbox | Covered Patio, Built-in BBQ, etc. |
| Furnished | dropdown (Y/N) | |
| Bed Down | dropdown (Y/N) | Is a bedroom downstairs? |
| Bath Down | dropdown (Y/N) | + type: Full, Half, 3/4 |
| Conversion | dropdown | If applicable |

### Key Tips for Features Tab
- Features tab is the most checkbox-heavy — use `find` to locate each checkbox group by name
- For each checkbox group, use `left_click` on each individual checkbox
- After clicking a checkbox, verify it turned blue in a screenshot
- Scroll down frequently — this tab has many fields below the fold
- Some checkbox groups have a "Max" limit noted (e.g., "Appliances Max 15")

---

## TAB 3: ROOMS

### Structure
The Rooms tab has a table with rows. Each row has 3 columns:
- **Room Type** (combobox) — Kitchen, Primary Bedroom, 2nd Bedroom, Living Room, etc.
- **Description** (combobox/multi-select) — Room-specific features like Island, Pantry, Walk-In Closet, Downstairs, etc.
- **Dimensions** (text) — Format: WxL (e.g., `16x14`)

### Default Rows
The form starts with 5 rows. Click the **"More"** button to add additional rows (adds 1 row at a time). You may need up to 7+ rows depending on the property.

### Key Tips for Rooms Tab
- **Multi-select descriptions require JavaScript.** For example, if Kitchen needs both "Island" and "Pantry":
```javascript
const desc = document.querySelector('select[name="_Input_182__REPEAT0_180"]');
Array.from(desc.options).forEach(opt => {
  if (opt.value === 'ISLAND' || opt.value === 'PANTRY') opt.selected = true;
});
desc.dispatchEvent(new Event('change', {bubbles: true}));
```
- The `name` attribute pattern for descriptions is `_Input_182__REPEAT{rowIndex}_180` where rowIndex starts at 0
- Room Type name pattern: `_Input_182__REPEAT{rowIndex}_178`
- Dimensions name pattern: `_Input_182__REPEAT{rowIndex}_184`
- After clicking "More" for new rows, the new elements get different ref IDs — use `find` to locate them
- Description is required for each room — if the data sheet doesn't specify one, leave a note for the user

---

## TAB 4: VOW/FINANCIAL/LISTING INFORMATION

### Financial Section (top)

| Field | Type | Notes |
|-------|------|-------|
| ASSOC/CIC Y/N | dropdown | Yes/No — if Yes, the association detail rows become required |
| ASSOC/CIC Fee Includes | multi-select listbox | Select from: Alarm System, Cable, Common Area Taxes, Ground Maintenance, Insurance, Management, None, Recreation, Reserves, Security, Sewer, Trash, Water, etc. |
| Special Assessment YN | dropdown | Yes/No |
| Special Assessments $ | text | Dollar amount (no $) |
| Special Assessment Flag | dropdown | Q (Quarterly), Y (Yearly), M (Monthly) |

### Association Detail Rows (3 rows)

| Field | Type | Notes |
|-------|------|-------|
| Name | text | Association name — REQUIRED when ASSOC/CIC = Yes |
| ASSOC/CIC Dues | text | Dollar amount |
| How Billed | dropdown | Monthly, Quarterly, Semiannual, Yearly, None |
| Transfer | text | Transfer fee dollar amount |
| Set Up | text | Setup fee dollar amount |
| Other | text | Other fee dollar amount |
| Phone | text | Association phone — REQUIRED when ASSOC/CIC = Yes |
| ASSOC/CIC Type | dropdown | Master, Sub, Landscape, Condominium, Townhome — REQUIRED |

### Financial Fields (middle section)

| Field | Type | Notes |
|-------|------|-------|
| SID/LID YN | dropdown | Yes/No |
| SID/LID Balance | text | If Yes |
| SID/LID Annual Amount | text | If Yes |
| Annual Property Taxes | text | Dollar amount — REQUIRED |
| Earnest Deposit | text | Dollar amount |
| Court Approval | dropdown | Yes/No — REQUIRED |
| Short Sale | dropdown | Yes/No |
| Foreclosure Commenced | dropdown | Yes/No |
| NOD Date | date picker | If foreclosure = Yes |
| Probate YN | dropdown | Yes/No |
| Repo/Reo | dropdown | Yes/No |
| Litigation | dropdown | Yes/No |
| Litigation Type | dropdown | If litigation = Yes |
| Subject to FIRPTA | dropdown | Yes/No — REQUIRED |
| Financing Considered | multi-checkbox (Max 8) | Cash, Conventional, FHA, VA, USDA, Owner Will Carry, etc. — REQUIRED |

### Listing Information Fields (below fold — scroll down)

| Field | Type | Notes |
|-------|------|-------|
| Existing Rent | text | If applicable |
| Possession Desc | dropdown | Close of Escrow, By Agreement, etc. |
| Lockbox Type | dropdown | Electronic, Combination, None, etc. |
| Lockbox Location | text | |
| Photo Instructions | dropdown | Agent will upload Photos in Matrix, etc. |
| Photo Excluded | dropdown | |
| Resident Name | text | Owner/tenant name |
| Resident Phone # | text | Phone number |
| Owner Licensee | dropdown | Yes/No |
| Showing Desc (Max 1) | checkbox group | Appointment, Key-Any, Key-Call, No Showings, Showing Time |
| Show Additional (Max 3) | checkbox group | Showing Time, Agent, Owner, Tenant, Vacant, Alarm, Restrictions, Warning Pets |
| Occupancy Desc | checkbox group | Occupied By Owner, Occupied By Tenant, Vacant — NOTE: "Select Showing Desc first" must be done before this works |
| Lease End | dropdown | |
| Combo L/B | text | |
| Lease End Date | date picker | |
| Power On or Off | dropdown | Power ON, Power OFF |
| Lockbox ID | text | |
| Gated Y/N | dropdown | REQUIRED (yellow) |
| Gate Code / Gate Code 2 | text | |
| IDX | text | |
| Internet YN | dropdown | Yes/No |
| Public Address | dropdown | Yes/No (VOW) |
| AVM | dropdown | Yes/No (VOW) |
| Commentary | dropdown | Yes/No (VOW) |
| Auction Date | date picker | |
| Auction Type | dropdown | |
| Virtual Tour Link | text | URL |
| Virtual Tour Link 2 | text | URL |
| Branded Virtual Tour Link | text | URL |
| Submit Offer Site | text | URL |

### Key Tips for VOW/Financial Tab
- This is the longest tab — scroll down multiple times to reach all fields
- The Showing Desc MUST be selected before Occupancy Desc will accept input
- Financing Considered checkboxes require `left_click` on each one
- For ASSOC/CIC Fee Includes multi-select, use `form_input` if single value, or JavaScript for multiple values
- VOW fields (Public Address, Commentary, AVM) are at the very bottom — use `find` to locate them

---

## TAB 5: OFFICE & AGENT INFO

| Field | Type | Notes |
|-------|------|-------|
| List Date | date/text | Format: MM/DD/YY or as shown |
| Expire Date | date/text | |
| Agent ID | text | e.g., `255492` |
| Office Code | text | e.g., `RLBR06` |
| Listing Agent Name | auto-populated | Usually auto-fills from Agent ID |
| Agent Phone | text | |
| Office Name | auto-populated | Usually auto-fills from Office Code |
| Office Phone | text | |
| Email | text | Agent email |
| Co-List Agent ID | text | If applicable |
| Co-List Office Code | text | If applicable |

### Key Tips
- Agent ID and Office Code usually auto-populate the agent name and office name
- Verify auto-populated fields are correct after entering IDs
- This tab is usually quick

---

## TAB 6: REMARKS/DIRECTIONS

| Field | Type | Notes |
|-------|------|-------|
| Public Remarks | textarea | Main property description visible to public — character limit applies |
| Agent Remarks | textarea | Private remarks visible only to agents |
| Driving Directions | textarea | Directions to property |

### Key Tips
- Public Remarks has a character limit (usually 1000 chars) — verify length
- Use `form_input` or `triple_click` then `type` to enter text in textareas
- If the data sheet doesn't have remarks, note this to the user

---

## WORKFLOW SUMMARY

```
1. User opens MLS Matrix > Add/Edit > Residential
2. User provides data sheet (PDF or filled form)
3. Claude reads the data sheet
4. Tab 1 (General): Fill all fields → screenshot → "General tab done, hit Next"
5. Tab 2 (Features): Fill all checkboxes/dropdowns → screenshot → "Features tab done, hit Next"
6. Tab 3 (Rooms): Add rows as needed, set types/descriptions/dimensions → screenshot → "Rooms tab done, hit Next"
7. Tab 4 (VOW/Financial): Fill financial, listing info, VOW fields → screenshot → "VOW tab done, hit Next"
8. Tab 5 (Office & Agent): Fill dates, agent/office IDs → screenshot → "Office tab done, hit Next"
9. Tab 6 (Remarks): Fill public/agent remarks, directions → screenshot → "Remarks tab done"
10. User reviews and clicks "Validate" then "Submit Listing"
```

---

## COMMON DROPDOWN VALUES REFERENCE

### Yes/No Dropdowns
- Yes = `value="1"`
- No = `value="0"`

### City Values (common)
- Las Vegas, Henderson, North Las Vegas, Boulder City, Mesquite, Pahrump

### Property Type
- SFR = Single Family Residential

### Listing Type
- ER = Exclusive Right to Sell
- EX = Exclusive Agency

### Garage Type
- Attached, Detached, Carport, None

### Built Description
- Resale, New (never occupied), Under Construction

---

## AGENT INFO (Ryan Rose — Real Broker LLC)
- **Agent Name:** Ryan Rose
- **Agent ID:** 255492
- **Office Code:** RLBR06
- **Agent Phone:** 702-747-5921
- **Office Name:** Real Broker, LLC
- **Office Phone:** 702-853-8444
- **Email:** ryan@rosehomeslv.com

---

## HOW TO USE THIS DOCUMENT

Paste the following prompt at the start of a new conversation:

> "I need you to fill out an MLS Matrix Residential listing form. I have the MLS Matrix input form open in Chrome on the Residential tab. Please read the file `MLS_Matrix_Entry_Instructions.md` from my workspace folder for detailed field-by-field instructions, then read my data sheet `[FILENAME]` and begin filling in the General tab. Tell me when each tab is done so I can hit Next."
