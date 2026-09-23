# Fragment contract

**Read this before writing a single page.** It is binding on all three chapter writers. It exists so
that three people working in parallel produce one document instead of three documents.

Companion files, all authoritative, all of which you must read for your own pages:

| File | What it governs |
|---|---|
| [`../outline/guide-outline.md`](../outline/guide-outline.md) | **what each page says.** Section titles, the numbered points, the claim-ids, the CTA plan. LOCKED. |
| [`../outline/page-budget.md`](../outline/page-budget.md) | **how big each page is.** Word ceilings, content type, spread rules. |
| [`../outline/audience-path-map.md`](../outline/audience-path-map.md) | who each path is for and what the tabs have to do |
| [`../research/fact-ledger.md`](../research/fact-ledger.md) | **every number you are allowed to use.** If it is not here it does not exist. |
| [`design-system.md`](design-system.md) | **the only classes, hexes and type sizes you may use.** |
| [`svg/index.md`](svg/index.md) | which diagram goes on which page |
| [`../assets/image-manifest.md`](../assets/image-manifest.md) | which photograph goes on which page, with its reviewed alt text |
| [`../research/internal/voice-exemplars.md`](../research/internal/voice-exemplars.md) | the voice, and the banned-words table |

---

## One file per page

Write `build/fragments/p01.html` through `p39.html`. One file, one printed page, no exceptions.

Per-page files rather than per-chapter files, because:
- a 39 page document has 39 hard breaks anyway, so the file boundary and the page boundary agree
- the quarterly `refresh` mode regenerates exactly p33, p34, p36 and p37 and touches nothing else
- a QA defect points at a file instead of a line offset inside a chapter
- no single write is large enough to truncate

A fragment is a **bare `.page` element**. No `<html>`, no `<head>`, no `<style>`, no `<body>`. The
assembler splices it into [`shell.html`](shell.html), which already carries every style rule.

---

## The two page skeletons

Every page in the guide is one of these two. Do not invent a third.

### A. Section opener, the first page of a block

Used on p1 (special, see below), p2, p6, p10, p14, p18, p28, p32, p36, p38. A photograph dissolves
into the paper and the headline sits over the bottom of it.

```html
<!-- p18. Everyone back together, the sequence -->
<div class="page gp" id="p18">
  <div class="body">

    <div class="opener">
      <img src="assets/img/open-core.jpg" alt="ALT TEXT FROM image-manifest.md, VERBATIM">
      <div class="dissolve"></div>
    </div>
    <div class="opener-chip"><span class="rh-a">The shared core</span></div>

    <div class="op-body">
      <p class="op-eyebrow">Chapter three &nbsp;&middot;&nbsp; Everyone back together</p>
      <h1 class="op-h">One sentence that lands hard.</h1>
      <p class="op-line">A second line that turns it.</p>
      <p class="op-deck">Two sentences of setup. <b>The clause worth bolding.</b></p>

      <div class="cols">
        <div> ... left column ... </div>
        <div> ... right column ... </div>
      </div>
    </div>
  </div>

  <div class="foot foot-l">
    <span class="srcnote" data-srcnote></span>
    <span class="folio">18</span>
  </div>
</div>
```

### B. Interior page

Everything else. A 52px photographic running-head band, then padded content.

```html
<!-- p20. SID and LID, part 2 -->
<div class="page gp" id="p20">
  <div class="body">
    <div class="band">
      <img src="assets/img/open-core.jpg" alt="ALT TEXT FROM image-manifest.md, VERBATIM">
      <div class="tone"></div>
      <div class="head">
        <span class="rh-a">The shape of the cost</span>
        <span class="rh-b">SID and LID</span>
      </div>
    </div>

    <div class="pad" style="padding-top:16pt">
      ... content ...
    </div>
  </div>

  <div class="foot foot-r">
    <span class="folio">20</span>
    <span class="srcnote" data-srcnote></span>
  </div>
</div>
```

### Which foot, and why it alternates

`foot-l` puts the folio hard right, `foot-r` puts it hard left. Odd pages are right-hand pages, so
the folio has to sit on the outside edge or a reader thumbing the stack cannot find it.

| Page | Foot class | Folio sits |
|---|---|---|
| odd, right-hand | `foot-l` | outside right |
| even, left-hand | `foot-r` | outside left |

Get this backwards and the folios march up the gutter.

---

## Citations: you write claim-ids, never numbers and never URLs

This is the part most likely to go wrong, so it is mechanical.

**Every external fact gets this, immediately after the fact, inside the sentence's punctuation:**

```html
Nevada taxes 35 percent of taxable value<sup class="src" data-claim="tax-assessment-ratio">*</sup>, not market value.
```

- `data-claim` is a claim-id from the fact ledger, exactly as spelled there.
- The visible content is a literal asterisk `*`. `assemble.py` replaces it with the real number.
- **Numbering is global and generated.** Do not write `1`, `2`, `3`. Three writers hand-numbering in
  parallel would collide on the first shared page.
- `assemble.py` **fails the build** on any `data-claim` that is not in the ledger. That check is what
  makes this safe, so a typo costs you nothing but a rebuild.
- Multiple claims on one fact: one `<sup>` each, adjacent.

**Leave `<span class="srcnote" data-srcnote></span>` empty.** The assembler fills it from the ledger
with the marker range, the source organizations, and the verified date. If you write text in there it
will be overwritten.

`design-system.md` has the reasoning under "Citations, the two tier contract". Short version: the
guide cites 254 unique URLs, the frozen design gives the strip one line, so full URLs ship in a
generated companion source list and the printed strip carries organizations and dates.

### The NOT FOUND token

When the ledger's NOT FOUND register covers your subject, say so out loud and tell the reader how to
go get the answer. Never write around it silently, and never substitute a number from anywhere else.

```html
<span class="tok tok-nf"><i aria-hidden="true"></i>Not found</span>
```

---

## Diagrams

The thirteen SVGs are built and locked. Reference one with a placeholder comment; the assembler
inlines the file's markup in place of the comment.

```html
<figure class="fig">
  <!-- SVG-04 -->
  <figcaption class="figcap">A visible caption that adds something. Do not restate the diagram's own
  description, which is already inside the file for screen readers.</figcaption>
</figure>
```

Add `class="fig narrow"` when the diagram sits in one column of a two column grid.

**Never `<img src="...svg">`.** The files carry `role="img"`, `<title>` and `<desc>` wired to
`aria-labelledby`, and an `<img>` hides all of it from a screen reader and blocks print color
adjustment from reaching the fills.

**Do not edit an SVG and do not invent one.** If a page needs a diagram that does not exist, write the
page without it and say so in your handback note.

---

## Photographs

Alt text comes from [`../assets/image-manifest.md`](../assets/image-manifest.md) **verbatim.** It was
written and human-reviewed against the fair housing gate. Do not paraphrase it, do not shorten it, do
not write your own.

Paths are relative to the folder root, because the assembled guide sits there: `assets/img/open-core.jpg`.

An interior page's band reuses its block's opener photograph. Only p28 to p31 have their own insets.

---

## Hard rules, all mechanically checked

1. **No em-dashes.** Not in prose, not in a comment, not in an attribute. `qa-check.py` greps the
   source, the HTML entities, and the extracted PDF text. Use a comma, a period, or "and".
2. **No number that is not in the fact ledger.** No rounding a stale figure to look current, no
   back-filling from a blog post, no "about" in front of a guess.
3. **Only classes in `design-system.md`.** A component that does not exist is a request to that
   document, not something you improvise locally. Raise it in your handback note.
4. **No hex codes.** The palette is frozen and every class already carries its color. The one
   exception is an inline `style` on a `.seam` bar, which the cover already does.
5. **No `position:fixed`.** It repeats on every printed page and fails the build.
6. **No `position:absolute` inside an `li::before`.** This bug has shipped twice in this workspace and
   drops bullets onto the first letter under multi-column. Both list components use flexbox markers.
   Keep it that way.
7. **Stay under the page's word ceiling** in `page-budget.md`. 360 total set words, except p32 at 430
   and p33/p34 at 400. **If a page overruns, cut content. Never shrink type.** A guide written for
   cold traffic at a 6th grade reading level cannot be set at 9pt.
8. **`&middot;` and `&nbsp;` are the only HTML entities you may use.** Everything else goes in as a
   literal character.
9. **Clark County only.** Nothing about Pahrump, Mesquite, or Boulder City, ever.
10. **`Real Broker, LLC` and Nevada license `S.0185572`** appear on p1, p32 and p39. Non-negotiable,
    NRS 645.
11. **Blog links use `/blog/<slug>`, singular.** Plural `/blogs/` returns 404 on rosehomeslv.com.
    Write them as `<a href="https://rosehomeslv.com/blog/SLUG">`.

---

## Voice, in one paragraph

Plain-spoken protective insider. First person singular, because Ryan is the one talking. Mean 12 to 14
words a sentence, median 13, at least 30 percent of sentences under 10 words. Paragraphs of 2 to 4
sentences. Sixth grade reading level, and that is a measured gate, not a vibe. Soft CTAs that invite
rather than push. No "premier", no "exclusive opportunity", no "nestled", no "boasts". Check the
banned-words table in `voice-exemplars.md` before you reach for an adjective.

The tone that makes this guide work: **nobody in the picture is a villain.** The on-site rep has a job
and it is not representing the buyer. Say the role difference plainly and let the reader draw the
conclusion.

---

## Your handback note

When you finish, write `build/fragments/_handback-<yourblock>.md` with:

1. Every page you wrote and its **actual** total word count against its budget.
2. Every claim-id you used, so the fact auditor can diff against the ledger.
3. Every blog slug you linked. These are a **build-blocking gate**: `blog-corpus-map.md` records all
   110 as NOT FOUND for publish status, and every one has to be loaded live and confirmed before the
   guide ships. List them so that check has an input.
4. Anything you could not write, and why. A ledger gap, a missing class, a page that would not fit.
   **Say it rather than inventing around it.** An honest gap is cheap to fix and a fabricated number
   is not.
