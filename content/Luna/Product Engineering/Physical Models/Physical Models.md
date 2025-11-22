---
title: Physical Models
date: 2025-11-22
draft: false
---

> [!ABSTRACT]
> Luna is designed "Digital First." Before any physical prototype is built, every subsystem is modeled and simulated in Python. This page outlines the five core physical models used in our development process.

## The Modeling Framework

Our simulation environment (hosted on [GitHub](https://github.com/SimoneTestino/Luna)) allows us to iterate rapidly on design parameters.

### 1. External Fluid Dynamics Model
*Simulating Wind & Flight*
- **Purpose**: Determine stability and tether tension.
- **Inputs**: Wind speed, balloon radius, tether geometry.
- **Outputs**: Drag force, lean angle, required anchor weight.
- **See**: [[Product Engineering/Wind Stability|Wind Stability]] for results.

### 2. Internal Fluid Dynamics Model
*Simulating Helium Flow*
- **Purpose**: Optimize cooling efficiency.
- **Inputs**: Fan power, fan geometry, envelope shape.
- **Outputs**: Convection coefficients, flow velocity.
- **See**: [[Product Engineering/Thermal Management|Thermal Management]] for results.

### 3. Optical Model
*Simulating Light*
- **Purpose**: Maximize area coverage and uniformity.
- **Inputs**: LED flux, height, envelope haze.
- **Outputs**: Ground illuminance map (Lux), glare rating.
- **See**: [[Product Engineering/Lighting System|Lighting System]] for results.

### 4. Thermodynamic Model
*Simulating Heat*
- **Purpose**: Ensure component safety.
- **Inputs**: LED power, ambient temp, convection coefficients (from Model 2).
- **Outputs**: Equilibrium temperatures for LEDs, Helium, and Envelope.
- **See**: [[Product Engineering/Thermal Management|Thermal Management]] for results.

### 5. Barometric Pressure Model
*Simulating Gas Loss*
- **Purpose**: Predict maintenance intervals.
- **Inputs**: Mylar permeability, internal pressure, temperature.
- **Outputs**: Helium loss rate over time.
- **See**: [[Product Engineering/Lift and Buoyancy|Lift & Buoyancy]] for results.

## Code Access

The complete source code for these models is available to the team and collaborators.
- **Repository**: [Luna Project Software](https://github.com/SimoneTestino/Luna)
- **Documentation**: [Overleaf Technical Docs](https://www.overleaf.com/read/ffqrvgjfghgx#559440)