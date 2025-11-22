---
title: Safety and Sensors
date: 2025-11-22
draft: false
---

> [!ABSTRACT]
> Safety is paramount for an autonomous flying object. Luna features a robust, redundant safety architecture designed to detect anomalies and execute failsafe protocols instantly. This page details the sensor array, onboard logic, and emergency procedures.

## Safety Philosophy

Luna is designed to be **fail-safe**. 
- **Redundancy**: Critical sensors are duplicated.
- **Autonomy**: Safety logic runs onboard, not dependent on ground connection.
- **Passive Safety**: In worst-case power loss, the system remains benign (balloon floats or slowly descends).

## Sensor Architecture

The "Electronic Core" houses a comprehensive sensor suite monitored by dual Computation Centers (Arduino-based).

### 1. Environmental Sensors
- **Internal Temperature**: Monitors Helium gas temp.
- **Internal Pressure**: Barometric sensor to detect leaks or over-pressure.
- **Humidity**: Monitors internal moisture levels.

### 2. Component Health
- **LED Thermometers**: Direct PCB temperature monitoring.
- **Voltage/Current Sensors**: Monitor power delivery and consumption.

### 3. Flight Dynamics
- **Inclinometers (Tilt)**: Measures lean angle (wind effect).
- **Accelerometers (IMU)**: Detects turbulence, impact, or sudden tether failure (free flight).
- **GPS (Optional)**: For geofencing in free-flight scenarios.

### 4. Gas Monitoring
- **Helium Concentration**: Indirect measurement (via Oxygen sensors) to detect envelope rupture or air ingress.

## The "Two-Tiered" Logic

As described in [[Product Engineering/Software Architecture]], the safety logic is simple and deterministic.

### Tier 1: Warning (Yellow State)
*Condition: Parameter exceeds normal range but is not critical.*
- **Action**: 
    - Send telemetry alert to ground app.
    - Adjust active systems (e.g., 100% Fan Speed, Dim LEDs 20%).
- **Example**: LED Temp reaches 85°C.

### Tier 2: Critical (Red State)
*Condition: Parameter reaches dangerous limit.*
- **Action**: 
    - **Cut Power** to non-essential systems (LEDs).
    - **Flash Emergency Signal** (if LEDs operational).
    - **Audible Alarm** (Piezo buzzer).
- **Example**: LED Temp > 105°C, or Pressure drops rapidly (leak).

### Tier 3: Emergency Descent (Black State)
*Condition: Catastrophic failure or "Ground Loss" (tether break).*
- **Action**: 
    - **Controlled Helium Release**: Opens a small electronic valve to reduce lift.
    - **Goal**: Slow, safe descent (< 2 m/s) to the ground.
    - **Strobe Lights**: Visual warning to bystanders.

## Sensor Discrepancy Protocol

With dual sensors, what happens if they disagree?
- **Small Deviation**: Average the two values. Log a "Sensor Drift" warning.
- **Large Deviation**: 
    - Assume the **Worst Case** value is true (Fail-Safe).
    - Example: If Temp A = 40°C and Temp B = 90°C, system acts as if Temp is 90°C.
    - Trigger "Sensor Failure" alert.

## Communication Redundancy

Safety alerts are transmitted via two independent channels:
1. **Wired (Primary)**: Data over Power (PLC) or dedicated twisted pair in the tether.
2. **Wireless (Secondary)**: LoRa or Wi-Fi link to ground station/phone.

If the wired link is cut (tether failure), the wireless link takes over to trigger emergency protocols or receive manual "Land Now" commands.

## Physical Safety Features

- **Non-Flammable**: Helium is inert. Materials are self-extinguishing where possible.
- **Low Voltage Control**: User interface is low voltage; high voltage is contained.
- **Soft Impact**: The balloon is lightweight and flexible; impact risk to people/property is minimal compared to falling metal towers.

This comprehensive approach ensures Luna meets or exceeds safety standards for construction and event equipment.
