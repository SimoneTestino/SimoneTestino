---
title: Lighting System
date: 2025-11-22
draft: false
---

> [!ABSTRACT]
> Luna's lighting system is designed to deliver 100,000 lumens of high-quality, diffused light from an elevated position. This page details the optical modeling, LED selection, and the advantages of our balloon-based diffusion approach over traditional point-source towers.

## Optical Model

The core advantage of Luna is its geometry. By elevating the light source and using the balloon envelope as a diffuser, we create a "soft light" effect that covers a large area without the harsh glare and deep shadows associated with traditional light towers.

### Illuminance Distribution

We model the light source as a point emitter at height $h$ with a conical beam of half-angle $\alpha$. The illuminance $E$ (in lux) at a ground point $(x,y)$ is calculated using the inverse square law with cosine correction for the angle of incidence.

$$E(x,y) = \frac{\Phi \cdot h}{4\pi(x^2 + y^2 + h^2)^{3/2}}$$

Where:
- $\Phi$ = Total Luminous Flux (lumens)
- $h$ = Height of the balloon (meters)
- $r = \sqrt{x^2 + y^2}$ = Horizontal distance from center

### Coverage Area vs. Height

A key finding from our [[Product Engineering/Physical Models/Physical Models|Optical Model simulations]] is that **height matters more than raw power** for area coverage.

For a target illuminance of **10 lux** (sufficient for construction safety):
- **Traditional Tower (4m height)**: Covers a small, intensely lit circle. Light drops off rapidly.
- **Luna (20m height)**: Covers a much larger radius with more uniform light.

| Height (m) | 10 Lux Radius (m) | Area ($m^2$) | Uniformity |
| :--- | :--- | :--- | :--- |
| 5 | ~10 | ~314 | Poor (Hotspot) |
| 10 | ~18 | ~1000 | Good |
| **20** | **~25** | **~1960** | **Excellent** |
| 30 | ~28 | ~2460 | Excellent |

> [!NOTE]
> Luna illuminates nearly **6x the area** of a standard 5m tower for the same power output, simply by virtue of geometry.

## LED Module Specification

To achieve our target of **100,000 lumens** (100 klm) while staying within our weight and thermal budgets, we require high-efficiency LED modules.

### Requirements
- **Total Flux**: $\ge 100,000$ lm
- **Efficacy**: $\ge 180$ lm/W (to minimize heat)
- **Power**: $\approx 600$ W total
- **Weight**: Minimal (no heavy heatsinks)
- **Form Factor**: Exposed PCB for helium cooling

### Selected Component: TCI SML280
We have identified the **TCI SML280** (or similar high-density LED boards) as a primary candidate.
- **Type**: Linear / Rectangular LED Engine
- **Efficiency**: High efficacy suited for industrial applications
- **Origin**: Made in Italy (aligns with supply chain preference)

### Configuration
- **Array**: 3 to 4 modules mounted on a lightweight aluminum frame.
- **Orientation**: Downward-facing.
- **Control**: Dimmable drivers located at the ground station (to reduce balloon weight) or lightweight DC-DC converters onboard.

## Diffusion Strategy

The quality of light is determined by the envelope material. We use a hybrid Mylar strategy:

1. **Upper Hemisphere**: **Aluminized Mylar**.
   - Acts as a reflector, bouncing upward-emitted light back down.
   - Prevents light pollution (sky glow).
   - Increases effective downward flux.

2. **Lower Hemisphere**: **High-Haze Transparent Mylar**.
   - **Haze**: 80-90%. Scatters light to soften shadows.
   - **Transparency**: High transmission to minimize absorption loss.
   - Acts as a large "softbox," increasing the apparent size of the light source to reduce glare.

## Comparison with Competitors

| Feature | Luna | LuxTower / Traditional | AirStar (Film) |
| :--- | :--- | :--- | :--- |
| **Source Size** | Large (Balloon $\approx 2m \oslash$) | Small (Lamps) | Large |
| **Glare** | Low | High | Low |
| **Shadows** | Soft / Filled | Hard / Sharp | Soft |
| **Color** | Customizable (RGB option) | Fixed White | High CRI (Film) |
| **Efficiency** | **190 lm/W** | 80-120 lm/W | Variable |

## Smart Features

The lighting system is integrated with the [[Product Engineering/Safety and Sensors|Safety System]]:
- **Thermal Throttling**: If internal temperatures rise, LEDs automatically dim to reduce heat.
- **Emergency Signaling**: In case of communication loss or critical error, the lights can flash a distress pattern.
- **Zone Control**: Potential to switch off individual panels to shape the beam (e.g., 180° lighting).

See [[Product Engineering/Thermal Management]] to understand how we cool these high-power LEDs using helium.
