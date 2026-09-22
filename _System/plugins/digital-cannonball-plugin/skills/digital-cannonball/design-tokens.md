# Design Tokens — Digital Cannonball

Reference for the HTML Generator agent. These define the visual system for the cannonball page.

---

## CSS Custom Properties

```css
:root {
  /* Primary palette */
  --coral: #FF5C4D;
  --coral-light: #FF7A6E;
  --amber: #FF8C42;

  /* Neutrals */
  --ink: #0a0a0a;
  --charcoal: #3a3a3a;
  --stone: #8a8680;
  --warm-gray: #9a9590;
  --border-light: rgba(10, 10, 10, 0.1);
  --border-dark: rgba(255, 255, 255, 0.08);
  --border-dark-strong: rgba(255, 255, 255, 0.18);

  /* Backgrounds */
  --bg-page: #ffffff;
  --bg-cream: #faf7f0;
  --bg-dark: #0a0a0a;
  --bg-dark-card: #0a0a0a;

  /* Text on light */
  --text-primary: #0a0a0a;
  --text-secondary: #3a3a3a;
  --text-muted: #8a8680;

  /* Text on dark */
  --text-on-dark: #ffffff;
  --text-on-dark-muted: rgba(255, 255, 255, 0.55);
  --text-on-dark-body: #faf7f0;
  --text-on-dark-body-opacity: 0.78;
}
```

## Typography

### Font Families
- **Display/headings:** `'Playfair Display', Georgia, serif` (editorial weight, similar to Boska)
- **Body/UI:** `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`
- **Data/stats:** `'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace`

### Google Fonts CDN
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

### Type Scale
| Element | Font | Size | Weight | Line-height | Letter-spacing |
|---------|------|------|--------|-------------|----------------|
| Hero address | Playfair Display | clamp(30px, 5.1vw, 72px) | 500 | 0.98 | -0.025em |
| Section heading | Playfair Display | clamp(32px, 4.3vw, 58px) | 500 | 1.02 | -0.025em |
| Plan heading | Playfair Display | clamp(38px, 5.1vw, 70px) | 500 | 0.98 | -0.03em |
| Subheading (italic) | Playfair Display italic | clamp(14px, 1.3vw, 18px) | 400 | 1.45 | 0.005em |
| Pull quote | Playfair Display italic | clamp(19px, 2.4vw, 29px) | 400 | 1.25 | -0.01em |
| Section kicker | Inter | 11px | 700 | — | 0.22em uppercase |
| Stat label | Inter | 11px | 600 | — | 0.18em uppercase |
| Body text | Inter | 18px | 300 | 1.72 | normal |
| Body secondary | Inter | 16-17px | 300 | 1.65-1.72 | normal |
| Card item title | Playfair Display | clamp(17px, 1.7vw, 21px) | 500 | 1.25 | -0.01em |
| Card item body | Inter | 15px | 300 | 1.6 | normal |
| Stat number | Playfair Display | clamp(32px, 4.5vw, 51px) | 500 | 0.95 | -0.03em |
| Large stat | Playfair Display | clamp(38px, 4.3vw, 54px) | 500 | 0.95 | -0.035em |
| Mono label | JetBrains Mono | 10.5-13px | 500 | — | 0.14em uppercase |
| Comp address | Inter | 16px | 400 | 1.35 | -0.005em |
| Comp detail | Inter | 13px | 300 | — | 0.02em |
| Comp price | Playfair Display | 20-22px | 500 | — | -0.015em |

## Spacing

| Token | Value | Usage |
|-------|-------|-------|
| Section padding vertical | clamp(72px, 9vw, 128px) | Between major sections |
| Section padding horizontal | clamp(20px, 5vw, 56px) | Page gutters |
| Max content width | 1140px | Content container |
| Stat strip padding | 32px vertical, clamp(16px, 3vw, 28px) horizontal | Hero stat cells |
| Card padding | clamp(24px, 3.5vw, 36px) | Dark data cards |
| Plan act grid | clamp(70px, 10vw, 140px) label + 1fr content | Plan section layout |
| Step grid | 48px number + 1fr content, 20px gap | Plan step items |

## Responsive Breakpoints

| Breakpoint | Changes |
|------------|---------|
| ≤1100px | Hide side navigation dots |
| ≤1024px | Tighter section padding |
| ≤820px | Collapse gutter grids to single column |
| ≤720px | All multi-column widgets stack, stat grids to 1 column |
| ≤640px | Plan act grid stacks, signature stacks, hero photo 4:3 aspect |
| ≤560px | Hero stat ticker auto-fit, smaller stat strip |
| ≤400px | Reduced horizontal page padding (16px) |

## Component Patterns

### Section Kicker
```
font: Inter 11px/700, letter-spacing 0.22em, uppercase
color: var(--coral)
format: "01 / SECTION NAME"
margin-bottom: 22px
```

### Dark Data Card
```
background: var(--bg-dark)
border: 1px solid var(--ink)
border-radius: 12px
padding: clamp(24px, 3.5vw, 36px)
```

### Stat Cell (in dark card)
```
padding: 28px 22px 24px (or 36px 28px 32px for market stats)
border-right: 1px solid var(--border-dark)
last cell: no right border
```

### Timeline Node
```
dot: 11px circle, border 2px solid
active (most recent): filled coral, coral border
past: white fill, ink border
connector line: 1px solid var(--border-light), absolute positioned
```

### Pull Quote Block
```
border-top: 1px solid var(--ink)
border-bottom: 1px solid var(--border-light)
padding: 32px 0
font: Playfair Display italic
```

### Callout (bottom line / why this matters)
```
border-top: 1px solid var(--ink)
padding-top: 28px
grid: minmax(0, 160px) 1fr, gap 32px
label: Inter 11px/700, 0.22em uppercase, coral
body: Inter 19px/500, line-height 1.55
```

### Contact CTA Buttons
```
Primary (call): bg var(--ink), color white, padding 24px 26px
Secondary (email): bg transparent, border 1px solid var(--ink), color var(--ink)
```

## Scroll Animations

Use Intersection Observer with threshold 0.15. Each element fades in with:
```css
/* Hidden state */
opacity: 0;
transform: translateY(10px);

/* Visible state */
opacity: 1;
transform: translateY(0);
transition: opacity 0.55s cubic-bezier(0.33, 1, 0.68, 1),
            transform 0.55s cubic-bezier(0.33, 1, 0.68, 1);
```

Stagger child elements with increasing transition-delay (0ms, 60ms, 120ms, 160ms, 200ms, 240ms).
