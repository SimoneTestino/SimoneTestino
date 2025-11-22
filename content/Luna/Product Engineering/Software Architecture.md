---
title: Software Architecture
date: 2025-11-22
draft: false
---

> [!ABSTRACT]
> Luna's software is divided into two distinct domains: a high-fidelity **Physical Simulation Environment** (Python) for design validation, and a lightweight, real-time **Onboard Safety System** (C++) for operational control. This page details both architectures.

## 1. Ground-Based Physical Simulation (Python)

Before any physical prototype is built, Luna is "flown" in a digital twin environment. This approach saves time and money by validating physics and optimizing parameters virtually.

### Architecture
- **Language**: Python 3.x
- **Libraries**: NumPy (math), SciPy (solvers), Matplotlib (visualization).
- **Structure**: Object-Oriented Design. A `Luna` class integrates sub-models.

### Core Models
1. **External Fluid Dynamics**: 
   - Calculates Drag ($F_D$) and Lift ($F_L$) vectors.
   - Solves for equilibrium angle $\theta$ under wind load $v$.
   - *Output*: Tether tension requirements, max wind rating.

2. **Internal Fluid Dynamics & Thermodynamics**:
   - Models helium flow driven by fans.
   - Solves heat transfer equations: $Q_{LED} \rightarrow Helium \rightarrow Envelope \rightarrow Air$.
   - *Output*: Equilibrium temperatures for LEDs and Gas.

3. **Optical Model**:
   - Simulates light projection from height $h$.
   - Calculates ground illuminance $E(x,y)$.
   - *Output*: Optimal height and LED power for target lux.

4. **Permeation Model**:
   - Uses Arrhenius equation for gas diffusion.
   - *Output*: Refill interval predictions.

> [!TIP]
> The code for these models is available in the [GitHub Repository](https://github.com/SimoneTestino/Luna) and documented in the [[Product Engineering/Physical Models/Physical Models|Physical Models]] section.

## 2. Onboard Safety System (Embedded C++)

The flight software runs on the internal microcontroller (Arduino). It is designed for **determinism, speed, and fail-safety**.

### Architecture
- **Platform**: Arduino (C++).
- **Loop Cycle**: < 100ms (Real-time monitoring).
- **State Machine**: The system operates in defined states (Idle, Flight, Warning, Emergency).

### Core Modules

#### A. Sensor Fusion Engine
- Reads raw data from redundant sensors (Temp A/B, Pressure A/B).
- Applies calibration and filtering.
- **Discrepancy Check**: If $|A - B| > Threshold$, flag error and use worst-case value.

#### B. Safety Logic Controller
- Compares fused sensor data against **Critical Parameters** (derived from Python simulations).
- **Rules Engine**:
    - `IF Temp > T_WARN THEN Fan_Speed = 100%`
    - `IF Tilt > MAX_TILT THEN Trigger_Alert()`
    - `IF Pressure < MIN_P THEN Trigger_Emergency_Land()`

#### C. Communication Manager
- **Telemetry**: Streams status (Temp, Batt, Tilt) to ground @ 1Hz.
- **Command**: Listens for ground commands ("Land", "Dim Lights").
- **Heartbeat**: Sends "I'm Alive" signal. If ground loses heartbeat, it alerts operator.

#### D. Actuator Control
- **LED Driver**: PWM control for dimming.
- **Fan Driver**: PWM control for speed.
- **Valve Control**: Solenoid activation for helium release (Emergency).

## 3. Mobile App (User Interface)

A companion app for ground operators.
- **Connection**: Bluetooth LE (BLE) or WiFi.
- **Features**:
    - Real-time dashboard (Temp, Wind, Battery).
    - Control panel (Brightness, Height - if winch equipped).
    - **"Black Box"**: Logs flight data for post-flight analysis.
    - **Setup Wizard**: Step-by-step guide for safe deployment.

## Development Workflow

1. **Simulate**: Run Python model to find safe limits (e.g., "Max Temp = 85°C").
2. **Code**: Hardcode these limits into the Arduino firmware.
3. **Test**: Verify logic with hardware-in-the-loop (HIL) testing.
4. **Fly**: Deploy code to Luna.

This rigorous separation of "Design Logic" (Python) and "Control Logic" (C++) ensures that the onboard system remains lightweight and bug-free.
