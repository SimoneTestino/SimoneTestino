---
date: 2025-12-08
draft: false
tags: [Design, Typography]
---

# Typography Standards

This document defines the official typography used across the site.

---

## Font Families

### Headers & Body Text

- **Font**: Tinos
- **Weights**: 400 (Regular), 700 (Bold)
- **Usage**: All text - headers, body, paragraphs
- **Source**: Google Fonts
- **Rationale**: Serif font providing a classic, academic aesthetic

```css
font-family: 'Tinos', serif;
```

### Code & Monospace

- **Font**: JetBrains Mono
- **Usage**: Code blocks, technical content
- **Source**: Google Fonts

```css
font-family: 'JetBrains Mono', monospace;
```

---

## Configuration

From `quartz.config.ts`:

```typescript
typography: {
  header: "Tinos",
  body: "Tinos",
  code: "JetBrains Mono",
}
```

---

## Font Sizes

### Headings

| Element | Size | Weight |
|:--------|:-----|:-------|
| H1 | 3.5rem (hero) / 2rem (section) | Bold |
| H2 | 2rem | Bold |
| H3 | 1.2rem | Bold |
| H4-H6 | 1rem | Bold |

### Body

| Element | Size | Line Height |
|:--------|:-----|:------------|
| Body text | 1rem (16px) | 1.6-1.7 |
| Small text | 0.9rem | 1.5 |
| Taglines | 1.2rem | 1.6 |

---

## Best Practices

✅ **Do**:
- Use Tinos consistently for all text
- Maintain readable line heights (1.6-1.7 for body)
- Use weight changes plus size for hierarchy

❌ **Don't**:
- Use fonts outside Tinos + JetBrains Mono
- Use font sizes below 14px
- Use pure black (`#000`) for text - use `var(--dark)` instead
