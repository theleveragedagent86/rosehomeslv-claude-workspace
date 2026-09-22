# CLAUDE.md — Rose Homes LV / Marketing

Listing- and lead-marketing material and campaigns.

- **Listing Marketing Plan/** — the master listing-launch marketing plan / playbook and letter campaigns.
- **Listing Leads Content/** — lead-gen content library (blueprints, direct mail, email campaigns, expired designs, phone/text scripts, social shareables). `scrape_listing_leads*.py` in `_System/tools/` write here.
- **Lead-Magnets/** — downloadable lead magnets (e.g. moving-to-Las-Vegas guide).
- **Relocation Guide/** — the relocation guide site (pages/, assets/).
- **Smart Plans/** — Lofty smart-plan nurture sequences (e.g. Seller Lead Nurture). Emails end with `#signature#`.
- **email-templates.md**, **seller-report-template.html** — reusable templates.

---

## Folder Map — keep this current

```
Marketing/
├── Listing Marketing Plan/     master listing-launch playbook + letter campaigns
├── Listing Leads Content/      lead-gen content library
├── Lead-Magnets/               downloadable lead magnets
├── Relocation Guide/           relocation guide site
├── Smart Plans/                Lofty nurture sequences
├── email-templates.md
└── seller-report-template.html
```

**Maintenance rule:** When you add/move/rename anything here, update this map. If you move `Listing Leads Content/`, update the OUTPUT_DIR in `_System/tools/scrape_listing_leads*.py`. Never leave the map stale.
