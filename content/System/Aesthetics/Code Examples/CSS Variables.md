---
date: 2025-12-08
draft: false
tags: [Code, CSS]
---

# CSS Variables Usage

How to properly use the site's color system.

---

## Available Variables

```css
/* Core palette - auto-adapts to dark mode */
var(--light)       /* Background */
var(--lightgray)   /* Secondary backgrounds */
var(--gray)        /* Borders */
var(--darkgray)    /* Secondary text */
var(--dark)        /* Primary text */
var(--secondary)   /* Links, accents */
var(--tertiary)    /* Hover states */
```

---

## Correct Usage

```css
/* ✅ CORRECT - Uses variables */
.card {
  background: var(--lightgray);
  color: var(--dark);
  border: 1px solid var(--gray);
}

.button {
  background: var(--secondary);
  color: var(--light);
}
```

---

## Wrong Usage

```css
/* ❌ WRONG - Hardcoded colors */
.card {
  background: white;
  color: #0A0A0A;
  border: 1px solid #D8D8D8;
}
```

---

## Why This Matters

Variables automatically transform for dark mode:

| Variable | Light Mode | Dark Mode |
|:---------|:-----------|:----------|
| `--light` | `#FAFAFA` | `#0A0A0A` |
| `--dark` | `#0A0A0A` | `#F0F0F0` |

Hardcoded colors don't transform, breaking dark mode.
