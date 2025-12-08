---
date: 2025-12-08
draft: false
tags: [Design, Aesthetics, Documentation]
---

# Design System Overview

This website features a **multi-style design system** with three distinct visual identities.

## Documentation Index

- **[[Color Palette]]**: Complete colour specifications for all three styles
- **[[Typography]]**: Font standards (Tinos, JetBrains Mono)
- **[[TSX Component Guide]]**: Development patterns for custom components
- **[[Markdown Style Guide]]**: Content creation standards
- **[[Code Examples]]**: Practical implementation examples

---

## The Three Visual Styles

### 1. Personal/Academic (Monochrome)

The default site style—clean, professional, and focused on readability.

| Element | Light Mode | Dark Mode |
|:--------|:-----------|:----------|
| Background | `#FAFAFA` | `#0A0A0A` |
| Text | `#0A0A0A` | `#F0F0F0` |
| Accent | `#3B4A5A` | `#A5B5C5` |

**Usage**: All personal pages, academic content, research areas, and navigation.

---

### 2. ColivingLiguria (Earth Tones)

Warm, nature-inspired palette representing the coliving venture.

| Mode | Background | Accent | Text |
|:-----|:-----------|:-------|:-----|
| Light | `#F7F5F3` | `#4A6741` | `#2C2A24` |
| Dark | `#1A1F1A` | `#6FA360` | `#E5E0D8` |

**Usage**: ColivingLiguria block linking to [colivingliguria.pages.dev](https://colivingliguria.pages.dev).

---

### 3. Luna (Dark Space)

Futuristic theme for the Luna lighting project.

| Mode | Background | Accent | Text |
|:-----|:-----------|:-------|:-----|
| Light | `#050810` | `#4DA6FF` | `#FFFFFF` |
| Dark | `#F0F8FF` | `#2D7DD2` | `#0A0F1A` |

**Usage**: Luna block linking to [luna-st.pages.dev](https://luna-st.pages.dev).

---

## Homepage Structure

The homepage (`SimoneHome.tsx`) contains these sections:

1. **Hero** — Name, tagline, contacts, quick links
2. **About Me** — Brief introduction
3. **Research Areas** — Mathematics and Philosophy fields
4. **Academic Work** — Links to writings, papers, diary
5. **ColivingLiguria** — Earth-tone styled block
6. **Luna** — Space-themed styled block
7. **Utilities** — Contacts, availability, payments, documents

---

## Design Philosophy

Each project maintains its unique identity whilst coexisting on a unified personal site. The CL and Luna blocks adapt to light/dark mode with inverted colour schemes.
