---
title: Technical Overview
date: 2025-11-22
draft: false
---

> [!ABSTRACT]
> Luna reimagines portable lighting through a helium balloon platform that combines high-efficiency LEDs, advanced thermal management, and sophisticated stabilization systems. This page provides a high-level technical overview of Luna's core concept, system architecture, and key performance metrics.

## Core Concept

Luna is a **helium-filled balloon lighting system** that elevates powerful LED arrays to heights of 10-50 meters, delivering superior illumination quality through diffused, uniform light distribution. The system operates as an integrated package of five major subsystems:

1. **Buoyancy System**: 5-10 m³ helium balloon providing lift capacity
2. **Lighting System**: High-efficiency LED modules (100 klm output)
3. **Thermal Management**: Forced helium convection cooling
4. **Stabilization System**: Multi-point anchoring with calculated tension
5. **Safety & Control**: Redundant sensors with autonomous emergency response

### Why a Balloon Platform?

Traditional light towers are constrained by their mechanical structure - heavy, expensive to transport, and limited to heights of 4-9 meters. Luna's helium platform eliminates these constraints:

- **Height Advantage**: 10-50m operation vs 4-9m for towers → dramatically larger illumination area
- **Weight Advantage**: <2kg total vs 400kg+ for plug-in towers → negligible transport cost
- **Quality Advantage**: Elevated diffused light vs ground-level point sources → uniform illumination without glare
- **Cost Advantage**: €750 production cost vs €2,000-5,200 for comparable towers

## System Architecture

```
┌─────────────────────────────────────┐
│   Helium Envelope (5-10 m³)         │
│   ┌───────────────────────────┐     │
│   │  Internal Frame           │     │
│   │  ┌─────────────────┐      │     │
│   │  │ Computation     │      │     │
│   │  │ Centers (×2)    │      │     │
│   │  └─────────────────┘      │     │
│   │  ┌─────────────────┐      │     │
│   │  │ LED Arrays      │      │     │
│   │  │ (600W, 100klm)  │      │     │
│   │  └─────────────────┘      │     │
│   │  ┌─────────────────┐      │     │
│   │  │ Cooling Fans    │      │     │
│   │  │ (He circulation)│      │     │
│   │  └─────────────────┘      │     │
│   └───────────────────────────┘     │
│                                     │
│   Sensor Array (dual redundancy):  │
│   • Temperature (He gas + LEDs)    │
│   • Pressure (barometric)          │
│   • Tilt (inclinometers)           │
│   • Acceleration (3-axis)          │
│   • Gas composition                │
└─────────────────────────────────────┘
         ↓ Power + Data Cable
    ┌────────────────────┐
    │  Ground Station    │
    │  • Transformer     │
    │  • Data receiver   │
    │  • Power source    │
    └────────────────────┘
    
    Stabilization Anchors (×3)
    120° spacing, nylon tethers
```

## Key Performance Specifications

| Parameter | Specification | Rationale |
|-----------|--------------|-----------|
| **Balloon Volume** | 5-10 m³ | Optimized for lift vs drag balance |
| **Operating Height** | 10-50 m | Maximum illumination area per watt |
| **LED Power** | 600W | Target 100 klm output |
| **Luminous Output** | 100,000 lumens | Comparable to mid-range light towers |
| **Luminous Efficacy** | 190 lm/W | High-efficiency LEDs + helium cooling |
| **Total Weight** | <2 kg | Solid components only (excludes helium) |
| **Illumination Radius** | 25 m at ≥10 lux | Usable work area |
| **Maximum Wind** | 35 m/s | With 3-point stabilization |
| **Operating Temp Range** | -10°C to +45°C ambient | Thermal management validated |
| **Max Internal Temp** | <50°C (LED surface) | Sustained cooling performance |

## Five Core Subsystems

### 1. [[Lift and Buoyancy|Buoyancy & Lift System]]

**Purpose**: Provide sufficient lift to suspend all internal components and cable

**Key Components**:
- Mylar envelope (125μm, dual-zone: aluminized + transparent)
- Helium gas (5-10 m³ at 1.5× atmospheric pressure)
- Lightweight internal frame (<200g)

**Performance**:
- Gross lift: ~6-12 kg (helium volume dependent)
- Payload budget: ~4-10 kg available after envelope and cable
- Helium advantages: 6× thermal conductivity vs air, chemical inertness

**Design Validation**:
Python models calculate lift capacity as function of:
- Balloon volume
- Envelope material density
- Cable length and mass
- Internal component weight

See [[Lift and Buoyancy]] for detailed buoyancy calculations and material selection.

### 2. [[Lighting System|Optical & Lighting System]]

**Purpose**: Deliver 100 klm luminous flux with optimal distribution pattern

**Key Components**:
- LED modules: 3-4× high-efficiency arrays (e.g., TCI SML280)
- Diffusion envelope: High-haze Mylar (80-90% haze, good transparency)
- Reflective cone: Directs light downward

**Light Distribution Model**:
- Point source approximation at height h
- Conical beam with optimized half-angle α
- Illuminance E(x,y) calculated from inverse-square law with cosine correction:

$$E(x,y) = \frac{\Phi \cdot h}{4\pi(x^2 + y^2 + h^2)^{3/2}}$$

Where:
- Φ = luminous flux (lumens)
- h = height above ground
- x, y = ground coordinates

**Performance Advantage**:
At 20m height, Luna illuminates 3× the area per watt compared to 4m tower due to geometric efficiency and diffusion quality.

See [[Lighting System]] for complete optical modeling and LED specifications.

### 3. [[Thermal Management|Thermodynamic & Cooling System]]

**Purpose**: Maintain LED temperatures <50°C and helium gas <40°C

**Challenge**: 600W LED input with ~30% waste heat (180W) inside closed envelope

**Solution**: Forced helium convection

**Key Components**:
- Cooling fans (4×): Aluminum blades, low power draw
- Fan configuration: 
  - 2× below LEDs, angled upward
  - 2× above LEDs, pulling heat away
- Helium circulation: 6× thermal conductivity vs air enables efficient heat transfer

**Heat Transfer Model**:

Helium temperature equilibrium:
$$T_{He} = T_{ambient} + \frac{P_{waste}}{h_{conv} \cdot A_{envelope}}$$

LED surface temperature (forced convection + radiation):
$$P_{in} = h_{conv}(v) \cdot A_{LED} \cdot (T_{LED} - T_{He}) + \varepsilon\sigma A_{LED}(T_{LED}^4 - T_{He}^4)$$

**Validated Performance**:
- LED surface temp: 45-48°C at 35°C ambient
- Helium bulk temp: 38-42°C at 35°C ambient  
- Fan power: <20W total
- Convection coefficient: 50-80 W/m²K at 7 m/s helium flow

See [[Thermal Management]] for complete thermal analysis and fan specifications.

### 4. [[Wind Stability|Wind Mitigation & Stability System]]

**Purpose**: Maintain position and prevent excessive tilt in wind up to 35 m/s

**Challenge**: Large surface area (4-6 m² projected) creates significant drag

**Solution**: Three-point nylon anchoring with calculated tension distribution

**Stabilization Geometry**:
- 3× nylon tethers at 120° spacing
- Anchor distance d = 2× operating height (optimal tension balance)
- Each tether rated for maximum tension (wind-aligned case)

**Force Balance**:

Horizontal drag:
$$F_D = \frac{1}{2}\rho_{air} C_D A v^2$$

Tether tension (wind-aligned):
$$T_h = \frac{F_D}{\cos\alpha}$$

Where α = arctan(h/d)

**Performance**:
- 15 m/s wind: <5° tilt, <3m lateral displacement
- 25 m/s wind: <15° tilt, <8m lateral displacement
- 35 m/s wind: <30° tilt, emergency protocols activate

See [[Wind Stability]] for complete stability calculations and tether specifications.

### 5. [[Safety and Sensors|Safety Systems & Sensors]]

**Purpose**: Autonomous detection and response to emergency conditions

**Architecture**: Dual redundant computation centers
- Primary: Wired communication via power cable
- Secondary: Wireless (radio) communication
- Both: Independent sensor suites and processing

**Monitored Parameters**:
- Temperature (helium gas, LED surface) - 4× sensors
- Pressure (internal barometric) - 2× sensors  
- Tilt angle (inclinometers) - 2× 3-axis units
- Acceleration (sudden movement) - 2× accelerometers
- Gas composition (helium concentration proxy) - 2× sensors
- Cable integrity (voltage/current monitoring)

**Emergency Protocols**:
1. **Minor alerts**: Log event, notify ground, continue operation
2. **Moderate alerts**: Reduce LED power, increase cooling, await acknowledgment
3. **Critical alerts**: Emergency descent via controlled helium release
   - Light-signal fallback if communication lost
   - Automatic power cutoff prevents fire risk
   - Slow descent rate (<2 m/s) for safe ground impact

**Redundancy Strategy**:
- Dual sensors for each parameter
- Statistical discrepancy detection
- Failsafe defaults (e.g., if pressure sensors disagree, assume worst case)
- Ground must acknowledge critical alerts within timeout window

See [[Safety and Sensors]] for complete safety system architecture and sensor specifications.

## Physical Modeling Framework

All Luna subsystems are validated through **Python-based physical models** before prototyping:

1. **External Fluid Dynamics**: Wind drag, turbulence, tether forces
2. **Internal Fluid Dynamics**: Helium circulation, thermal convection
3. **Optical Model**: Illuminance distribution, diffusion efficiency  
4. **Thermodynamic Model**: Heat generation, transfer, and dissipation
5. **Barometric Pressure Model**: Helium permeation through envelope

These models enable rapid iteration on:
- Material selection (Mylar thickness, fan size, cable gauge)
- Dimensional optimization (balloon size, height, tether length)
- Safety parameter definition (critical temperature, pressure, tilt)

Models are implemented in NumPy/SciPy with full documentation on GitHub and Overleaf.

See [[Product Engineering/Physical Models/Physical Models|Physical Models]] and [[Software Architecture]] for complete modeling framework.

## Materials and Construction

### Primary Materials

**Envelope**: Mylar (PET film) 125μm thickness
- Upper 70%: Aluminized (helium barrier, light reflection)
- Lower 30%: Transparent high-haze (light diffusion)
- Sealed via heat fusion (200°C, superior to adhesive)

**Frame**: Lightweight aluminum or carbon fiber
- 4-pod design: distributes weight over circular base
- Total frame mass: <200g
- Transparent sections where light path crosses

**Tethers**: Nylon rope (3× anchors)
- Rated for 200-300N tension per line
- UV-resistant outdoor grade
- Total mass: ~150g

**Cable**: Copper power + data (twisted pair)
- Voltage: 120-240V AC stepped up for efficiency
- Data: Redundant channels for sensor telemetry
- Mass: ~15-20 g/m, optimized gauge

See [[Materials Guide]] for complete materials specifications, suppliers, and cost breakdown.

## Cost Structure

| Component Category | Cost Estimate |
|-------------------|---------------|
| Envelope (Mylar) | €50-100 |
| Frame | €10 |
| LED modules | €80-110 |
| Electronics (sensors, Arduino, fans) | €120-150 |
| Cable & connectors | €20 |
| Helium (per use) | €30-50 |
| Tethers & hardware | €10 |
| **Total COGS** | **€320-450** |
| **With assembly & overhead** | **€650-750** |

Compare to light tower COGS of €2,000-5,200 for similar performance.

See [[Financials/Business Model|Business Model]] for complete cost analysis and pricing strategy.

## Competitive Advantages Summary

| Advantage | Luna | Traditional Towers | Impact |
|-----------|------|-------------------|--------|
| **Height** | 10-50m | 4-9m | 4-10× illumination area |
| **Weight** | <2kg | 400-800kg | Negligible transport cost |
| **Light Quality** | Diffused, uniform | Point source, harsh | Superior work environment |
| **Efficiency** | 190 lm/W | 80-120 lm/W | 50-100% better |
| **Cost** | €750 COGS | €2,000-5,200 COGS | 60-85% cost reduction |
| **Portability** | Single person carry | Truck + forklift | Deployment flexibility |
| **Ecological** | 0.05 g CO₂/hr·m² | 0.77 g CO₂/hr·m² | 94% emissions reduction |

## Development Resources

- **GitHub**: [Luna Software Repository](https://github.com/SimoneTestino/Luna)
- **Overleaf**: [Complete Technical Documentation](https://www.overleaf.com/read/ffqrvgjfghgx#559440)
- **Colab**: [Physical Models Notebook](https://colab.research.google.com/drive/1efjAjN-BGo0PpHR_8qp5AJvTG5l-25yk)

## Next Steps

See detailed subsystem documentation:
- [[Lift and Buoyancy]] - Helium system and envelope design
- [[Lighting System]] - Optical modeling and LED selection
- [[Thermal Management]] - Cooling system design
- [[Wind Stability]] - Stabilization and tether calculations
- [[Safety and Sensors]] - Safety architecture and sensors
- [[Materials Guide]] - Component specifications and suppliers
- [[Software Architecture]] - Physical models and embedded systems

Return to [[index|Luna Homepage]] or explore [[Financials/Market Analysis|Market Analysis]].
