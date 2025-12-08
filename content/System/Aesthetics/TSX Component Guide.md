---
date: 2025-12-08
draft: false
tags: [Development, TSX, Components]
---

# TSX Component Development Guide

Guide for creating custom TSX components in this Quartz site.

---

## File Organization

Every custom page component requires **two files**:

```
quartz/
├── components/
│   ├── YourComponent.tsx      # Component logic
│   └── styles/
│       └── yourcomponent.scss  # Component styles
```

---

## Basic Component Template

```tsx
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/yourcomponent.scss"

export default (() => {
    const YourComponent: QuartzComponent = ({ displayClass }: QuartzComponentProps) => {
        return (
            <div class={`your-component ${displayClass ?? ""}`}>
                {/* Content */}
            </div>
        )
    }

    YourComponent.css = style
    return YourComponent
}) satisfies QuartzComponentConstructor
```

---

## Registration Steps

### 1. Add to `components/index.ts`

```typescript
import YourComponent from "./YourComponent"

export {
  // ... other exports
  YourComponent,
}
```

### 2. Configure routing in `quartz.layout.ts`

```typescript
Component.ConditionalRender({
  component: Component.YourComponent(),
  condition: (page) => page.fileData.slug === "your-page",
}),
```

---

## Multi-Style Block Pattern

This site uses **scoped CSS variables** for different visual styles within the same page:

```scss
// CL Earth-Tone Block
.cl-block {
  --cl-light: #F7F5F3;
  --cl-moss: #4A6741;
  
  background: var(--cl-light);
  // Uses CL palette inside this block
}

// Luna Dark Block
.luna-block {
  --luna-void: #050810;
  --luna-blue: #4da6ff;
  
  background: var(--luna-void);
  // Uses Luna palette inside this block
}
```

---

## Common Patterns

### Hero Section

```tsx
<section class="hero">
    <h1>Title</h1>
    <p class="tagline">Subtitle</p>
    <div class="quick-links">
        <a href="/page" class="link-pill">Link</a>
    </div>
</section>
```

### Feature Grid

```tsx
<div class="features-grid">
    <a href="/page" class="feature-card">
        <span class="icon">📝</span>
        <h3>Title</h3>
        <p>Description</p>
    </a>
</div>
```

---

## Link Casing

> [!WARNING]
> **Internal links are CASE-SENSITIVE**

```tsx
// ✅ Correct - matches file casing
<a href="/Academia/Active-&-Works/Academic-Writings">Link</a>

// ❌ Wrong - will 404
<a href="/academia/active-&-works/academic-writings">Link</a>
```

---

## Reference

See [[SimoneHome.tsx]] for a complete multi-style homepage example.
