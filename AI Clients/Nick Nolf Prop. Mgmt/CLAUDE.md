# Nick Nolf / TNG Property Management — Wiki Schema

This project is an **LLM Wiki** — a persistent, structured knowledge base maintained by Claude for the Nick Nolf / TNG Property Management AI workflow engagement.

## Architecture

```
raw/          # Immutable source documents (meeting transcripts, emails, screenshots, etc.)
wiki/         # LLM-generated and LLM-maintained markdown pages
CLAUDE.md     # This file — schema and conventions
```

## Wiki Conventions

### Page Types

| Type | Prefix | Purpose | Example |
|------|--------|---------|---------|
| Entity | `entity-` | A person, company, system, or tool | `entity-nick-nolf.md` |
| Workflow | `workflow-` | A specific automation the client wants built | `workflow-email-classifier.md` |
| Concept | `concept-` | A recurring idea, pattern, or convention | `concept-naming-convention.md` |
| Source Summary | `source-` | Summary of a raw source document | `source-initial-meeting.md` |
| Comparison | `comparison-` | Side-by-side analysis | `comparison-appfolio-vs-drive.md` |
| Overview | `overview.md` | Single high-level page summarizing the entire engagement | `overview.md` |

### Page Structure

Every wiki page uses this template:

```markdown
---
title: Page Title
type: entity | workflow | concept | source | comparison | overview
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [list of raw/ filenames this page draws from]
tags: [relevant tags]
---

# Page Title

[Content organized with ## and ### headers as needed]

## Related Pages
- [[linked-page-name]] — one-line description of relationship
```

### Naming Convention for Files
- All lowercase, hyphens between words
- Prefix matches the page type
- Example: `workflow-vendor-work-order-processing.md`

### Cross-References
- Use `[[wiki-page-name]]` wikilink syntax for internal links
- Every page should have a "Related Pages" section at the bottom
- Orphan pages (no inbound links) should be flagged during lint

### Special Files

| File | Purpose |
|------|---------|
| `wiki/index.md` | Content catalog — every page listed with link, one-line summary, and metadata |
| `wiki/log.md` | Chronological append-only record of ingests, queries, lint passes |
| `wiki/overview.md` | High-level engagement summary — the "front page" of the wiki |

## Operations

### Ingest
When a new source is added to `raw/`:
1. Read the source fully
2. Discuss key takeaways with the user (if interactive)
3. Create a `source-` summary page in `wiki/`
4. Create or update entity pages for every person, company, or system mentioned
5. Create or update workflow pages for every automation described
6. Create or update concept pages for recurring patterns or conventions
7. Update `wiki/index.md`
8. Append an entry to `wiki/log.md`

### Query
When the user asks a question:
1. Read `wiki/index.md` to find relevant pages
2. Read those pages
3. Synthesize an answer with citations to wiki pages
4. If the answer is substantive, offer to file it as a new wiki page

### Lint
Periodically check for:
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages with no inbound links
- Concepts mentioned but lacking their own page
- Missing cross-references
- Data gaps worth investigating

## Domain Context

- **Client:** Nick Nolf, owner of TNG (The Next Generation) Property Management, Las Vegas
- **Engagement:** Ryan Rose is building AI automation workflows using Claude Code and Claude Cowork
- **Primary systems:** Gmail, AppFolio, Google Drive
- **Priority:** Email management is the central nervous system; all other workflows are secondary
- **First build:** Vendor work order email processing (Campbell's Appliance + NWHS)
- **Next meeting:** Monday, April 6, 2026, ~1 PM, same conference room, ~1 hour
