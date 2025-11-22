---
title: Materials Guide
date: 2025-11-22
draft: false
---

> [!ABSTRACT]
> Building a high-performance, lightweight, and durable balloon requires careful material selection. This page details the specifications for the envelope, frame, electronics, and helium, including cost analysis and supplier options.

## 1. The Envelope (Cover)

The envelope is the most critical component, requiring a balance of:
- **Gas Barrier**: Keeping helium inside.
- **Optical Properties**: Transmitting and diffusing light.
- **Strength**: Resisting pressure and tears.
- **Weight**: Maximizing lift.

### Material Selection: Mylar (PET)
We use **Biaxially-oriented Polyethylene Terephthalate (BoPET)**, commonly known as Mylar.

#### Configuration: Hybrid Design
- **Upper Hemisphere (70%)**: **Aluminized Mylar**
    - **Thickness**: 125 $\mu m$
    - **Function**: Blocks light escape (reflector), excellent gas barrier.
    - **Permeability**: Extremely low (metal barrier).
- **Lower Hemisphere (30%)**: **Transparent High-Haze Mylar**
    - **Thickness**: 125 $\mu m$
    - **Haze**: 80-90% (Matte finish).
    - **Function**: Diffuses LED light, creates "softbox" effect.
    - **Permeability**: Higher than aluminized, but acceptable for short-term use.

### Helium Permeability
Based on our [[Product Engineering/Physical Models/Physical Models|Permeation Model]]:
- **Rate**: $< 5\%$ volume loss per 1000 hours.
- **Impact**: Negligible. The balloon is typically deflated/re-inflated for transport between events.

### Construction Method
- **Sealing**: **Heat Welding** (Impulse Sealing) at ~200°C.
- **Why not Glue?**: Glue adds weight, can degrade, and is messy. Welding creates a fused bond as strong as the material itself.
- **Gore Design**: The sphere is constructed from "gores" (orange-slice shapes) calculated to form a perfect sphere when inflated.

## 2. The Frame

The internal skeleton holds the electronics and transfers the lift force from the envelope to the tether.

- **Material**: **Carbon Fiber** or **Aluminum 6061-T6** tubing.
- **Design**: "Four-Pod" structure.
    - Distributes weight over a circular base on the envelope (preventing point-stress).
    - **Transparent Sections**: Where the frame crosses the light path, we use clear polycarbonate or acrylic rods to avoid shadows.
- **Weight Target**: < 200g.

## 3. Electronics & LEDs

### LED Modules
- **Spec**: High-efficiency, aluminum-core PCBs.
- **Candidate**: **TCI SML280** (Made in Italy).
- **Power**: ~150W per module (x4).
- **Cooling**: Exposed PCB back for helium convection.

### Computation Center
- **Microcontroller**: **Arduino** (e.g., Nano 33 IoT or Portenta).
- **Why**: Low power, lightweight, built-in connectivity (WiFi/BLE), robust ecosystem.
- **Sensors**: Off-the-shelf modules (Bosch BME280 for Env, MPU6050 for IMU).

## 4. Helium Gas

- **Grade**: **Balloon Gas** (99% purity) is sufficient. High-purity lab helium is not required and too expensive.
- **Supply**: Standard industrial cylinders (e.g., T-size).
- **Cost**: ~€5-10 per $m^3$.
- **Recycling**: For frequent use, a recovery system (compressor) can be developed, but initially, it is a consumable.

## Cost Analysis (Bill of Materials)

| Component | Estimated Cost | Notes |
| :--- | :--- | :--- |
| **Envelope** | €50 - €100 | Mylar film + labor/sealing |
| **Frame** | €10 - €20 | Carbon/Alu tubing |
| **LED Modules** | €80 - €110 | 4x High-power boards |
| **Electronics** | €120 - €150 | Arduino, Sensors, Fans, Power |
| **Cable** | €20 | 50m Power/Data |
| **Tethers** | €10 | Nylon rope |
| **Helium** | €30 - €50 | Per fill (consumable) |
| **TOTAL COGS** | **€320 - €490** | *Excludes assembly labor* |

> [!SUCCESS]
> Even with a conservative estimate, the **Total BOM Cost (< €500)** allows for a very healthy margin at a **€1,250 sales price**, validating the business model.

## Suppliers

- **Mylar**: EasyComposites (EU), Alibaba (China - bulk).
- **LEDs**: TCI (Italy), Lumileds.
- **Electronics**: Arduino, DigiKey, Mouser.
- **Helium**: Local industrial gas suppliers (SOL Group, Linde).

See [[Financials/Business Model]] for how these costs fit into the larger financial picture.
