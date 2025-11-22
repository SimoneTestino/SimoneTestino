---
title: Thermal Management
date: 2025-11-22
draft: false
---

> [!ABSTRACT]
> Managing the heat from 600W of LEDs inside a sealed helium balloon is one of Luna's critical engineering challenges. This page details our unique "Helium Cooling System" which leverages the superior thermal properties of helium to maintain safe operating temperatures without heavy heatsinks.

## The Thermal Challenge

We are placing a **600W heat source** (the LEDs) inside a thermally isolated plastic sphere.
- LEDs are ~40-50% efficient.
- This means ~300-360W of energy is converted directly into **heat**.
- Without active cooling, the LEDs would rapidly overheat and fail, or melt the Mylar envelope.

## Helium: The Secret Weapon

Luna turns the lifting gas itself into a coolant. Helium has exceptional thermal properties compared to air:

| Property | Helium | Air | Ratio (He/Air) |
| :--- | :--- | :--- | :--- |
| **Thermal Conductivity ($k$)** | **0.151** $W/(m \cdot K)$ | 0.025 $W/(m \cdot K)$ | **~6.0x** |
| **Specific Heat ($c_p$)** | **5193** $J/(kg \cdot K)$ | 1005 $J/(kg \cdot K)$ | **~5.2x** |

> [!IMPORTANT]
> Helium conducts heat **6 times better than air**. This means a fan blowing helium over a hot surface removes heat much more effectively than the same fan blowing air.

## Cooling System Architecture

Our system uses **forced convection** to transfer heat from the LEDs to the helium, and then from the helium to the envelope, where it dissipates into the outside air.

### 1. Active LED Cooling
- **Fans**: 4x lightweight, transparent-blade fans.
- **Placement**: 
    - 2x **Below** the LED plate, angled upwards.
    - 2x **Above** the LED plate, pulling hot gas away.
- **Mechanism**: High-velocity helium flow strips the thermal boundary layer from the bare LED PCBs.
- **Result**: We eliminate heavy aluminum heatsinks entirely. The helium *is* the heatsink.

### 2. Envelope Heat Rejection
- The warmed helium circulates against the large surface area of the Mylar envelope ($>15 m^2$).
- Heat conducts through the thin film (125 $\mu m$) and convects into the surrounding atmosphere.
- **Equilibrium**: The system reaches a steady state where Heat Generated = Heat Lost to Environment.

## Thermal Model Results

Our [[Product Engineering/Physical Models/Physical Models|Thermodynamic Python Model]] predicts the equilibrium temperatures:

### Scenario: 600W Input, 25°C Ambient Air

1. **Helium Bulk Temperature**: Stabilizes at **~35-40°C**.
   - This is well below the melting point of Mylar (~250°C) and safe for electronics.
   
2. **LED Junction Temperature**: Stabilizes at **~60-70°C**.
   - Safe operating range for LEDs is typically up to 85-105°C.
   - We have a healthy safety margin.

### Extreme Conditions
Even in **35°C ambient heat**, the model shows LED temperatures remaining safe (<85°C) due to the efficiency of the helium loop.

## Safety Mechanisms

The [[Product Engineering/Safety and Sensors|Safety System]] continuously monitors thermal health:

1. **Sensors**:
   - **Thermistor A**: Measures Helium gas temperature.
   - **Thermistor B**: Measures LED PCB temperature directly.
   
2. **Logic**:
   - **Warning Threshold**: If LEDs > 85°C $\rightarrow$ Increase fan speed to 100%.
   - **Critical Threshold**: If LEDs > 95°C $\rightarrow$ Linearly reduce LED brightness (dimming).
   - **Emergency Cutoff**: If LEDs > 105°C $\rightarrow$ Cut power to LEDs immediately.

## Advantages over Traditional Cooling

| Feature | Traditional Light Tower | Luna System |
| :--- | :--- | :--- |
| **Cooling Medium** | Air | Helium |
| **Heatsink** | Large Aluminum Fins (Heavy) | None (Direct Gas Contact) |
| **Weight** | High | Negligible (Fans only) |
| **Efficiency** | Standard | Superior (High $k$) |

This thermal innovation is a key reason Luna can achieve such a high power-to-weight ratio.
