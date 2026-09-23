# Lofty embed constraints for `landing-page.html`

Verified against Ryan's own shipped Lofty page
`Rose Homes LV/Content/New-Construction/arroyo-at-skyeview/landing-page.html`
and the porting research in `Rose Homes LV/Marketing/nrg-research/08-lofty-porting-constraints.md`.
Everything below is confirmed from a page that is live, not inferred.

---

## 1. HARD: no `<form>` element in the embed

> Lofty does not ingest leads from in-embed forms.
> Source: `~/.claude/skills/new-construction/landing-page-template.md:435`

The shipped Arroyo page contains **zero** `<form>` tags. Confirmed by grep.

**The pattern:**
1. The landing page is an **HTML embed** pasted into the Lofty landing-page builder.
2. Lofty appends **its own form block below the embed** at publish time.
3. Every CTA inside the embed is `<a href="#contact">`, and page JS rewrites the click to
   scroll to the bottom of the document, landing the reader on the Lofty form.

This means the guide's landing page keeps its CTA rhythm (a CTA every couple of sections)
without ever owning a form. Do not add one. Do not post to a webhook. Do not collect a
single field inside the embed.

**Reuse this verbatim** (from the shipped page, lines 1191 to 1207):

```js
/* Scroll #contact CTAs to bottom (where Lofty form lives once wired) */
function scrollToContact(e) {
    if (e) e.preventDefault();
    var target = Math.max(
        document.body.scrollHeight,
        document.documentElement.scrollHeight
    );
    window.scrollTo({ top: target, behavior: 'smooth' });
}
function bindContactScroll(root) {
    var links = (root || document).querySelectorAll('a[href="#contact"]');
    links.forEach(function(a) {
        if (a.dataset.scrollBound) return;
        a.dataset.scrollBound = '1';
        a.addEventListener('click', scrollToContact);
    });
}
bindContactScroll();
```

## 2. `position: fixed` is SAFE inside a Lofty embed

Previously flagged as the build's top technical risk, now settled. The shipped Arroyo page
uses it twice and both render correctly live:

```css
.header   { position: fixed; top:0; left:0; right:0; z-index:1000; }  /* line 127 */
.lightbox { position: fixed; inset:0; z-index:9999; }                 /* line 528 */
```

So Lofty's wrapper applies no `transform`, `filter`, or `contain` that would re-anchor a
fixed element. A sticky header or a fixed CTA bar on the landing page is fine.

**This does NOT apply to the guide.** `new-construction-buyer-guide.html` is print-first,
and a fixed element repeats on every printed page. `qa-check.py` fails the build on any
`position: fixed` in the guide. Two files, two opposite rules.

## 3. Do not use `:has()`

Zero usages across every shipped page, so its behavior under Lofty's CSS handling is
untested. There is no need for it here. Put a real class on the container instead.

## 4. Flat root slugs

The Arroyo page publishes to `https://rosehomeslv.com/arroyo-at-skyeview`. Lofty does not
do nested paths. Blog posts are the one exception and live at `/blog/<slug>`, singular;
`/blogs/` returns 404.

**Slug collision warning:** the New Construction **hub** is targeting `/new-construction`.
This guide's landing page must not take that slug. Use something distinct, for example
`/new-construction-guide`.

## 5. Analytics are injected by Lofty, not hardcoded

Do not put GA or Pixel tags in the embed. Lofty injects them at publish:
GA `G-50N1D59DW6`, Meta Pixel `621835647008401`. Publish settings are
"No header, no footer" with embed padding zeroed from 60/20 to 0/0.

## 6. Self-contained

No external CSS or JS except Google Fonts. All styles inline in a single `<style>` block.
Images either inlined as data URIs or referenced absolutely.

---

## Related but separate: the New Construction hub

`Content/New-Construction/new-construction-hub/landing-page.html` is a different asset:
a top-of-funnel SEO authority page for the whole valley, on-brand in brass `#c9a86e` over
navy `#1c2333`, targeting `/new-construction`.

This lead magnet is deliberately **off-brand** with its own researched conversion palette,
and is fed by paid Facebook traffic rather than organic search. They overlap on subject
matter (both cover builders and areas) but not on funnel role, audience, or slug. Keep
them visually distinct on purpose, and do not let the hub's palette leak into the guide.
