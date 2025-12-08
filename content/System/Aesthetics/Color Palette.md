---
date: 2025-12-08
draft: false
tags: [Design, Colors]
---

# Complete Color Palette

This document defines all colors used across the three visual styles.

---

## 1. Personal/Academic (Monochrome)

Defined in `quartz.config.ts`. Uses desaturated blue-gray tones.

### Light Mode

| Variable | Hex | RGB | Description |
|:---------|:----|:----|:------------|
| `--light` | `#FAFAFA` | `rgb(250,250,250)` | Background |
| `--lightgray` | `#F0F0F0` | `rgb(240,240,240)` | Secondary BG |
| `--gray` | `#D8D8D8` | `rgb(216,216,216)` | Borders |
| `--darkgray` | `#5A5A5A` | `rgb(90,90,90)` | Secondary text |
| `--dark` | `#0A0A0A` | `rgb(10,10,10)` | Primary text |
| `--secondary` | `#3B4A5A` | `rgb(59,74,90)` | Links, accents |
| `--tertiary` | `#6B7A8A` | `rgb(107,122,138)` | Hover states |

### Dark Mode

| Variable | Hex | RGB | Description |
|:---------|:----|:----|:------------|
| `--light` | `#0A0A0A` | `rgb(10,10,10)` | Background |
| `--lightgray` | `#1A1A1A` | `rgb(26,26,26)` | Secondary BG |
| `--gray` | `#2A2A2A` | `rgb(42,42,42)` | Borders |
| `--darkgray` | `#A0A0A0` | `rgb(160,160,160)` | Secondary text |
| `--dark` | `#F0F0F0` | `rgb(240,240,240)` | Primary text |
| `--secondary` | `#A5B5C5` | `rgb(165,181,197)` | Links, accents |
| `--tertiary` | `#8595A5` | `rgb(133,149,165)` | Hover states |

---

## 2. ColivingLiguria (Earth Tones)

Used in `.cl-block` sections. Nature-inspired Ligurian palette.

| Name | Hex | RGB | Usage |
|:-----|:----|:----|:------|
| **Warm Alabaster** | `#F7F5F3` | `rgb(247,245,243)` | Block background |
| **Light Sand** | `#E5E0D8` | `rgb(229,224,216)` | Secondary surfaces |
| **Deep Moss Green** | `#4A6741` | `rgb(74,103,65)` | Primary accent, buttons |
| **Raw Sienna/Clay** | `#A67B5B` | `rgb(166,123,91)` | Hover states |
| **Deep Peat** | `#2C2A24` | `rgb(44,42,36)` | Text |
| **Bark** | `#4E4B42` | `rgb(78,75,66)` | Secondary text |

### CSS Custom Properties (in `.cl-block`)

```css
--cl-light: #F7F5F3;
--cl-lightgray: #E5E0D8;
--cl-moss: #4A6741;
--cl-clay: #A67B5B;
--cl-dark: #2C2A24;
```

---

## 3. Luna (Dark Space)

Used in `.luna-block` sections. Futuristic space-tech palette.

| Name | Hex | RGB | Usage |
|:-----|:----|:----|:------|
| **Void Black** | `#050810` | `rgb(5,8,16)` | Primary background |
| **Deep Space** | `#0a0f1a` | `rgb(10,15,26)` | Secondary background |
| **Electric Blue** | `#4da6ff` | `rgb(77,166,255)` | Primary accent |
| **Light Blue** | `#80bfff` | `rgb(128,191,255)` | Hover states |
| **Star White** | `#ffffff` | `rgb(255,255,255)` | Headings, buttons |
| **Nebula Gray** | `#e0e0e0` | `rgb(224,224,224)` | Body text |
| **Cosmic Mist** | `#a0a0a0` | `rgb(160,160,160)` | Muted text |

### CSS Custom Properties (in `.luna-block`)

```css
--luna-void: #050810;
--luna-space: #0a0f1a;
--luna-blue: #4da6ff;
--luna-light-blue: #80bfff;
--luna-white: #ffffff;
--luna-gray: #a0a0a0;
```

---

## Usage Guidelines

1. **Never hardcode colors** - Always use CSS variables
2. **Scope-specific palettes** - CL and Luna palettes are scoped to their blocks
3. **Dark mode** - Personal palette auto-transforms; CL and Luna maintain their styles
4. **Brand consistency** - Each block maintains its project's visual identity
