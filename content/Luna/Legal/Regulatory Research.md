---
title: Regulatory Research and Compliance
date: 2025-11-22
draft: false
---

> [!ABSTRACT]
> This page documents the comprehensive regulatory research conducted to ensure Luna's compliance with European and Italian aviation regulations. It details our engagement with ENAC and EASA, the regulatory frameworks analyzed, and the open questions awaiting official guidance.

## Overview

Luna is classified as a **tethered gas balloon for commercial operations** under aviation regulations. Unlike remotely piloted aircraft systems (drones), Luna has no propulsion or remote control capabilities - it is anchored to the ground and controlled only through power modulation and safety systems.

This unique classification requires careful navigation of both European (EASA) and national (ENAC) regulations. Our research has identified applicable frameworks while revealing gaps in existing regulations for our specific use case.

## Regulatory Classification

### European Classification (EASA)

Following definitions in **EASA Balloon Rule Book**, Luna is classified as:

- **Type**: Tethered gas balloon (pallone a gas vincolato)
- **Purpose**: Commercial operations
- **Regulation Code**: [CS 31GB.28](https://aviation.bot/easa/sdt/-594305269?f=file_MOkpammkZdh)

**Key Finding**: Page 22 of the regulation explicitly states: *"This Regulation does not apply to air operations with tethered gas balloons."*

This indicates that tethered gas balloons for commercial use are **regulated at the national level**, not European level. No further stringent regulations were found in [EASA Regulations](https://www.easa.europa.eu/en/regulations).

### Reference Guidelines

While not legally binding for Luna, the [SORA guidelines](https://www.easa.europa.eu/en/domains/drones-air-mobility/operating-drone/specific-category-civil-drones/specific-operations-risk-assessment-sora) (Specific Operations Risk Assessment) provide useful risk management frameworks developed for drones in the [specific category](https://elistair.elistair.com/resources/general-information-about-tethered-drones/tethered-drones-in-the-new-european-regulation/).

## Italian National Regulations (ENAC)

### Tethered Balloon Regulations

[ENAC](https://www.enac.gov.it/) specifies that [balloon regulations](https://www.enac.gov.it/sicurezza-aerea/operazioni-di-volo/operazioni-di-volo-con-palloni/) cover tethered gas balloons at the national level. However, existing documentation primarily addresses [passenger transport balloons](https://www.enac.gov.it/la-normativa/normativa-enac/regolamenti/regolamenti-ad-hoc/norme-tecniche-condizioni-di-esercizio-per-palloni-frenati-destinati-al-trasporto-di-persone), which clearly does not apply to Luna.

Available [forms and modules](https://www.enac.gov.it/sicurezza-aerea/operazioni-di-volo/operazioni-di-volo-con-palloni/modulistica/modulistica-relativa/) may be relevant but require official clarification.

### Harmlessness Criteria Analysis

Though Luna is not a remotely piloted aircraft (APR), we analyzed the **LG 2016/003 NAV** guidelines on harmlessness to confirm Luna's safety profile:

#### Mass Requirement ✓
- **Limit**: < 2 kg total solid mass
- **Luna**: ~1.9 kg (0.2kg payload + 1.4kg envelope + 0.3kg cable)
- **Status**: Compliant (assuming helium mass is excluded)

#### Structural Integrity (§5.1) ✓
- Mylar 125μm and nylon materials meet standard structural requirements
- Materials commonly used in similar applications with proven track record

#### Fire Protection (§5.7) ✓
- High helium concentration prevents combustion
- No lithium battery required (only sensors with backup)
- Internal temperature continuously monitored
- Automatic power reduction on critical temperature

#### Other Criteria (§5.2-5.6, §5.8) ✓
- Easily satisfied or not applicable to Luna's design

### Operational Restrictions

The most relevant restriction comes from **ENAC APR Regulation §10.7**:

> "Flight over assemblies of people, for parades, sporting events or forms of entertainment or otherwise where there are unusual concentrations of people is in any case prohibited."

However, this regulation applies to **remotely piloted aircraft (APR)**, a category Luna does not fall under.

#### Congested Areas Definition

From ENAC APR Regulations:

> **Congested Areas**: areas or agglomerations used as residential, industrial, commercial, sports zones, and in general areas where there may be gatherings, even temporary, of people.

**Key distinction**: The regulation does **not** prohibit APR flight over all congested areas - only over assemblies/unusual concentrations. This suggests construction sites and industrial areas without significant gatherings may be permitted.

#### Potential Compliance Strategy

Even if similar restrictions were applied to tethered balloons, Luna could maintain functionality by:
- Positioning the ground projection of Luna at sufficient distance (20-50m) from the illuminated area
- Angling internal LED arrays to direct light away from directly beneath the balloon
- This strategy preserves Luna's key advantage of elevated, diffused illumination

## Official Inquiry to ENAC

### Email Submitted: May 2025

We submitted a formal inquiry to ENAC addressing our regulatory questions. The email was sent to:
- certificazione.prodotti@enac.gov.it
- operazioni.volo@enac.gov.it

### Email Content Summary

**Subject**: Domanda ENAC - Pallone Aerostatico ad Elio per Illuminazione (Luna Project)

The inquiry provided:
1. **Project Description**: Technical overview of Luna's construction, operation, and commercial purpose
2. **Realistic Parameters**: Estimated specifications (subject to physical validation)
   - Payload weight: < 200g
   - Total solid mass: < 2kg
   - Luminous output: 75 klm
   - Operating temperature: < 50°C
   - Wind resistance: 15 m/s operational, resistant to extreme weather
3. **Regulations Consulted**: Summary of EASA and ENAC frameworks reviewed
4. **Target Markets**: Construction sites, industrial areas, and events (luxury and recreational)

### Attachments Provided

- **Domanda ENAC.tex**: Detailed regulatory questions (this page's source)
- **Project: Type One**: Complete [[Product Engineering/Technical Overview|technical documentation]]
- **Business Plan**: [[Financials/Market Analysis|Market analysis]] and [[Financials/Business Model|business model]]

## Open Questions Awaiting ENAC Response

### 1. Flight Over Assemblies

**Q**: Is flight over assemblies permitted for Luna?

If not, do any of the following conditions change the answer?

a) If harmlessness criteria (outlined above) are met?
b) If locations are congested areas (e.g., construction/industrial sites) rather than assemblies of people?
c) If 20-50m distance is maintained between ground projection and assembly/worksite?

### 2. Operational Procedures

**Q**: What process must be followed to conduct flight operations with Luna?

Reference: ENAC NI-2018-006 states it does not apply to tethered gas balloons except those for passenger transport.

Specific sub-questions:

a) **NOTAM Requirement**: Is a NOTAM (Notice to Airmen) required for each operation, as mentioned in [this article](https://www.dronezine.it/26606/enac-guinzaglio-corto-per-palloni-aquiloni-e-droni-vincolati/)?

b) **Response Timeline**: If NOTAM is required, what are expected approval timelines? (Concern: a user comment mentioned 20-day wait times, making rental business model impractical)

c) **Type Certification**: Can a Luna model receive single certification allowing operations under defined safety conditions, requiring only notification rather than per-operation approval?

d) **Operator Requirements**: 
   - Is an attendant required during flight operations?
   - Is an attendant required during setup/installation?
   - What qualifications/certifications are needed for setup personnel or monitoring personnel?

e) **Geographic Restrictions**: Do regulations vary by location type (urban spaces, beaches, natural parks)?

### 3. Weight Calculation Methodology

**Q**: What components must be included in Luna's weight calculation?

Given that helium mass is obviously excluded, must we include:
- Power cable weight?  
- Nylon anchor tether weight?
- Mylar envelope weight, or only internal payload (electronics and frame)?

### 4. Design Recommendations

**Q**: Do you have recommendations for modifications to Luna's design that would facilitate compliance with European and national regulations?

**Q**: Do you have safety design recommendations based on similar systems?

**Q**: Can you provide contacts for technical or legal expertise relevant to this project?

## Current Status

**Status as of November 2025**: Awaiting official response from ENAC

The regulatory approval process is on our [[System/Calendar Luna|critical path]] for Q4 2025. We have allocated October-November 2025 for legal clarity before committing to physical prototype construction.

### Contingency Planning

If Italian regulations prove prohibitive:

**Strategy**: Manufacturing in Italy for export to countries with more favorable tethered balloon regulations. This preserves:
- Technical development and IP protection in Italy
- Manufacturing jobs and supply chain
- Export revenue and market validation in permissive jurisdictions
- Option to revisit Italian market if regulations evolve

## Helium Transportation Regulations

While not a flight regulation, helium transport has compliance requirements.

### European Framework

[ECHA](https://echa.europa.eu/home) lists regulations for [helium](https://echa.europa.eu/substance-information/-/substanceinfo/100.028.334), particularly [Directive 2008/68](https://eur-lex.europa.eu/eli/dir/2008/68/oj) on dangerous goods transport.

**Key Finding**: Article 6 provides routine exemptions for small quantities. Regulations are primarily national-level.

**Practical Impact**: [Unofficial sources](https://www.bozzettodigitale.com/news/trasporto-e-stoccaggio-del-gas-elio.html) indicate this should not constitute a difficulty. The main challenge may be finding shipping companies willing to handle the material rather than regulatory prohibition.

## Related Documentation

- [[Legal/Patent Information|Patent Status]]
- [[Legal/Legal Concerns on Luna|General Legal Concerns]]
- [[Product Engineering/Safety and Sensors|Safety System Design]]
- [[Financials/Business Model|Business Model Impact]]

## References

1. **EASA Balloon Rule Book** (IR + AMC/GM & CS + AMC/GM) eRules, 2020. [Link](https://www.easa.europa.eu/en/downloads/46026/en)

2. **ENAC LG 2016/003 NAV** - Risk Assessment Guidelines for Remotely Piloted Aircraft Operations, 2016. [Link](https://www.enac.gov.it/sites/default/files/allegati/2018-Set/LG_2016_003_NAV.pdf)

3. **ENAC APR Regulation** - Remotely Piloted Aircraft Systems Regulation, Ed. 2, Amendment 3, October 2024. [Link](https://www.enac.gov.it/app/uploads/2024/10/Regolamento_APR_Ed_2_Emend_3.pdf)

4. **ENAC NI-2018-006** - Operational Guidance on Provincial Airworthiness Activities, April 2024. [Link](https://www.enac.gov.it/app/uploads/2024/04/NI_2018_006.pdf)

5. **EU Directive 2008/68** - Dangerous Goods Transport. [Link](https://eur-lex.europa.eu/eli/dir/2008/68/oj)

---

*Last updated: November 2025*
