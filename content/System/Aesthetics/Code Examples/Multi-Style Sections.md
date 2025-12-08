---
date: 2025-12-08
draft: false
tags: [Code, TSX, Styling]
---

# Multi-Style Sections

How to create sections with different visual identities in the same page.

---

## The Pattern

Use **scoped CSS custom properties** for each style:

```scss
// Style 1: ColivingLiguria Earth-Tones
.cl-block {
  --cl-light: #F7F5F3;
  --cl-moss: #4A6741;
  --cl-clay: #A67B5B;
  
  background: var(--cl-light);
  border-top: 4px solid var(--cl-moss);
}

// Style 2: Luna Dark Space
.luna-block {
  --luna-void: #050810;
  --luna-blue: #4da6ff;
  
  background: linear-gradient(135deg, var(--luna-void), #0a0f1a);
}
```

---

## TSX Structure

```tsx
{/* CL Block */}
<section class="cl-block">
    <div class="cl-content">
        <h2>ColivingLiguria</h2>
        <p>Description...</p>
        <a href="..." class="cl-button">Visit →</a>
    </div>
</section>

{/* Luna Block */}
<section class="luna-block">
    <div class="luna-content">
        <h2>Luna</h2>
        <p>Description...</p>
        <a href="..." class="luna-button">Explore →</a>
    </div>
</section>
```

---

## Key Points

1. **Scope variables** to the block class
2. **Don't use global `--light`/`--dark`** inside styled blocks
3. **Each block is self-contained** - styles don't leak
4. **Dark mode doesn't affect** CL/Luna blocks (they have fixed themes)

---

## Reference

See `quartz/components/SimoneHome.tsx` and `simonehome.scss` for the complete implementation.
