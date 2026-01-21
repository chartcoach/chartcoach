---
id: design-for-representational-consistency-across-devices-and-tables
title: Keep Quantitative Representations Consistent Across Artifacts
bibliography: references.bib
description: Avoid format-switch confusion by aligning how the same patient measurements
  are represented across devices, tables, and screens.
labels:
- task:track
- task:interpret
- impact:usability
- impact:accessibility
- data:clinical-measurements
- audience:general-public
- domain:health
- artifact:device
- source:ancker-2007
---

## The Rule <!-- role: advice -->

When the same measurement appears in multiple places (device, table, portal), represent it in consistent, easily mappable formats.

## The Logic <!-- role: reason -->

Users may read a value successfully on a familiar device yet fail to recognize the same value in a different representation (e.g., tabular display), reflecting limits in representational fluency and document literacy.

- **The Principle:** Representational fluency failures across artifacts
- **The Evidence:** [@anckerRethinkingHealthNumeracy2007]

## Where to Apply <!-- role: context -->

- **User Goal:** Tracking personal clinical measurements over time (e.g., blood pressure, glucose)
- **Data Type:** Repeated numeric readings shown in devices, logs, tables, charts
- **Audience:** Patients (including older adults) using home health technologies and portals [@anckerRethinkingHealthNumeracy2007]

## When to Break It <!-- role: exceptions -->

- **Scenario:** A new representation is required because the task changes (e.g., from single reading to trend analysis).
- **Reason:** Trend tasks may require tables/graphs; consistency should be preserved through explicit mapping rather than forcing identical formats. [@anckerRethinkingHealthNumeracy2007]

## The Price <!-- role: costs -->

- **The Sacrifice:** Less freedom to optimize each screen independently
- **The Risk:** Over-standardization may prevent using the most effective representation for a specific task [@anckerRethinkingHealthNumeracy2007]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming tabular displays are “obvious” because they are common in clinical settings.
- **Why it fails:** Some patients are unfamiliar with row/column conventions and cannot equate device-format values with tabular ones. [@anckerRethinkingHealthNumeracy2007]

## How to Check <!-- role: check -->

- **Visual Sign:** Users can read the meter but can’t find or interpret the same reading in a portal table.
- **The Test:** Ask users to match a device reading to its entry in the table; frequent mismatches indicate representation inconsistency. [@anckerRethinkingHealthNumeracy2007]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit labels and formatting that mirrors the device (e.g., “120/90” shown identically) next to the table entry.
- **Best Fix:** Provide dual representations (device-like value + table + optional graphic) with clear mappings so users can translate confidently. [@anckerRethinkingHealthNumeracy2007]
