---
title: Wind Stability
date: 2025-11-22
draft: false
---

> [!ABSTRACT]
> As a tethered balloon, Luna is susceptible to wind drag. This page details the aerodynamic forces at play and the "String Stabilization" system designed to keep Luna stable in winds up to 35 m/s (Force 8-9).

## The Aerodynamic Challenge

A spherical balloon has a high drag coefficient ($C_D \approx 0.47$). In wind, drag forces push the balloon sideways and down, potentially causing it to lean excessively or hit the ground.

### Forces at Play
1. **Lift ($F_L$)**: Upward force from helium.
2. **Drag ($F_D$)**: Horizontal force from wind.
   $$F_D = \frac{1}{2} \rho_{air} C_D A v^2$$
3. **Tension ($T$)**: Force from the tether/anchors holding it back.

Without stabilization, a single-tether balloon will lean at an angle $\theta$ where $\tan(\theta) = F_D / F_L$. In strong winds, $F_D$ easily exceeds $F_L$, causing extreme lean.

## String Stabilization System

To counteract drag, we do not rely on lift alone. We use a **3-point anchoring system**.

### Configuration
- **Main Tether**: Carries power/data, vertical (or near-vertical).
- **Guy Lines (x3)**: Lightweight Nylon ropes attached to the balloon's equator.
- **Geometry**: Anchors placed on the ground at 120° intervals, at a radius $d \approx 2h$ (twice the flight height).

### How it Works
1. **Triangulation**: The three lines form a tripod pyramid. This geometrically constrains the balloon's movement.
2. **Load Transfer**: Wind load is transferred directly to the upwind guy lines as tension, rather than requiring buoyant lift to fight the wind.
3. **Virtual Stiffness**: The system creates a "stiff" structure out of tension elements, minimizing sway.

## Performance Analysis

Using our [[Product Engineering/Physical Models/Physical Models|Wind Effect Model]], we simulated the displacement of Luna under various wind speeds with this stabilization system.

| Wind Speed (m/s) | Beaufort Scale | Behavior |
| :--- | :--- | :--- |
| **0 - 5** | Breeze | Perfectly stable. Vertical. |
| **5 - 15** | Moderate Gale | Slight lean (< 5°). Tethers taut. |
| **15 - 25** | Strong Gale | Noticeable lean (< 15°). Safe operation. |
| **25 - 35** | Storm | Significant lean (< 30°). **Max Rated Limit.** |
| **> 35** | Hurricane | Emergency descent recommended. |

> [!SUCCESS]
> The 3-point system allows Luna to operate in winds that would topple standard light towers or make them unsafe.

## Tether Specifications

To handle these loads, the tethers must be strong yet lightweight.

- **Material**: High-strength Nylon or Dyneema.
- **Diameter**: 2-3 mm.
- **Break Strength**: > 200 kg (Safety Factor > 5x max wind load).
- **Weight**: Negligible (~150g total).

## Active Monitoring

The [[Product Engineering/Safety and Sensors|Safety System]] includes:
- **Accelerometers**: Detect turbulence and sudden gusts.
- **Inclinometers**: Measure the lean angle.

**Safety Logic**:
- If **Tilt > 30°** for > 10 seconds: Send "High Wind" alert to ground.
- If **Tilt > 45°**: Initiate emergency descent or power down to reduce profile/risk.

## Comparison to Alternatives

- **Single Tether**: Unstable in > 5 m/s wind. Requires massive lift (huge balloon) to stay upright.
- **Rigid Pole**: Heavy, difficult to transport, limited height.
- **Luna (3-Point)**: **Stable, Lightweight, High Altitude.**

This stabilization strategy is key to making Luna a practical tool for outdoor construction and events, not just a fair-weather toy.
