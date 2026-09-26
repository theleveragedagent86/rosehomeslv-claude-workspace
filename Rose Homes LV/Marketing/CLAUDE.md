# CLAUDE.md — Rose Homes LV / Marketing

Listing- and lead-marketing material and campaigns.

- **Listing Marketing Plan/** — the master listing-launch marketing plan / playbook and letter campaigns.
- **Listing Leads Content/** — lead-gen content library (blueprints, direct mail, email campaigns, expired designs, phone/text scripts, social shareables). `scrape_listing_leads*.py` in `_System/tools/` write here.
- **Lead-Magnets/** — downloadable lead magnets (moving-to-Las-Vegas guide, area-wide new-construction guide). **Has its own CLAUDE.md** — read it first.
- **Relocation Guide/** — the relocation guide site (pages/, assets/).
- **Smart Plans/** — Lofty smart-plan nurture sequences (e.g. Seller Lead Nurture). Emails end with `#signature#`.
- **nrg-research/** — competitor teardown of nevadarealestategroup.com, used to spec the Rose Homes LV New Construction hub. Numbered research notes (`00-master-sitemap-architecture.md`, `02-builder-pages.md`, `08-lofty-porting-constraints.md`, …) plus `_raw-*.txt` URL dumps.
- **email-templates.md**, **seller-report-template.html** — reusable templates.

---

## Folder Map — keep this current

```
Marketing/
├── Listing Marketing Plan/     master listing-launch playbook + letter campaigns
├── Listing Leads Content/      lead-gen content library
├── Lead-Magnets/               downloadable lead magnets            → its own CLAUDE.md
├── Newsletter/                 The Rose Report: NEWSLETTER-TEMPLATE.md + issues/<send-date>/ (sections/, assets/, final email HTML).
│                               Email styling = Leveraged Agent v2.0 "Vector" kit (SKOOL Community/Brandkit), adopted 2026-09-23.
│                               issues/2026-09-24/newsletter-v1-navy-gold.html = archived pre-Vector version
│                               issues/2026-09-24/beehiiv-snippet.html = body-only version pasted into a beehiiv HTML snippet block (no <style>, fluid width)
│                               Weekly routine = /rose-report skill (source _System/skills/rose-report). Each issue has beehiiv.json (post id + web_url).
│                               beehiiv strips sms: links, so its Text-me button goes to theleveragedagent86.github.io/rhlv-site-images/text-ryan/ (GitHub Pages redirect into Messages)
├── Relocation Guide/           relocation guide site
├── Smart Plans/                Lofty nurture sequences
├── nrg-research/               NRG competitor teardown (New Construction hub spec)
├── email-templates.md
└── seller-report-template.html
```

**Maintenance rule:** When you add/move/rename anything here, update this map. If you move `Listing Leads Content/`, update the OUTPUT_DIR in `_System/tools/scrape_listing_leads*.py`. Never leave the map stale.
