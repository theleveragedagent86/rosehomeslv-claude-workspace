---
title: AppFolio
type: entity
created: 2026-04-05
updated: 2026-04-05
sources: [2026-04-05-initial-meeting-transcript-and-analysis.md]
tags: [system, software, property-management]
---

# AppFolio

## Overview
Cloud-based property management software. Nick pays for the top-tier AI package. Considered the "Ferrari of property management" in industry circles.

## Features Discussed
- Universal search bar (like Google) for properties, owners, tenants
- Closed-circuit system — only shows TNG's own data
- Anonymized comp tool for rental pricing comparisons with other AppFolio users
- User settings with customizable permissions (can restrict accounting, allow owner/tenant/HOA data)
- Built-in texting capability for tenant communication
- Full maintenance/work order management
- Maintenance communication handled within AppFolio (not email)
- AI features already built in (Nick pays for top tier)

## Access Plan
- Nick will create a dedicated Claude user login with full permissions
- Ryan will explore the structure before next meeting (read-only)
- Need to verify: does AppFolio have an API, or is all interaction browser-based? This determines Cowork vs. API approach.
- Need to verify: does AppFolio's TOS allow automated/bot logins?

## Workflows That Touch AppFolio
- [[workflow-appfolio-maintenance-followup]] — Check "no action for 7 days" report
- [[workflow-email-classifier]] — Cross-reference tenant/lease data for email responses
- [[workflow-cross-reference-audit]] — Compare Drive PDFs against AppFolio data

## Open Questions
- API availability vs. browser-only access
- TOS compliance for automated logins
- What specific follow-up actions after 7-day no-action flag? (template to tenant, vendor, both?)

## Related Pages
- [[entity-tng-property-management]] — The company using it
- [[entity-nick-nolf]] — Account owner
