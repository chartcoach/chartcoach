---
id: prefer-proportional-symbols-over-embedded-bars
title: Prefer Proportional Symbols Over Embedded Bar Charts on Maps
bibliography: references.bib
description: When visualizing quantitative data on maps, proportional symbols outperform
  embedded bar charts for correlation tasks.
labels:
- chart:proportional-symbol-map
- chart:map
- visual:area
- visual:length
- task:correlate
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
Use proportional symbols (like circles) to encode quantitative values on maps instead of embedding axis-based charts (like bar charts) on geographic regions.

## The Logic <!-- role: reason -->
While length is generally a more precise encoding than area, embedding length-based charts (bar charts) onto a map creates visual interference and complexity that degrades performance for correlation tasks.
*   **The Evidence:** Experimental rankings collated by Zeng et al. [@zeng_review_2023] show that Proportional Symbol Maps (E-2) ranked higher in both accuracy and time efficiency than Single Map Bar Charts (E-3) for correlation tasks [@pena-araya_comparison_2020].
*   **The Principle:** **Symbol Holism.** A proportional symbol (a filled circle) is perceived as a single coherent object, making it easier to compare across locations or small multiples. An embedded bar chart is a composite object that requires more cognitive effort to parse into its constituent values.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing values or finding correlations across geographic regions.
*   **Data Type:** Quantitative data associated with geographic locations.
*   **Visual Design:** When chosing between overlaying glyphs on a map.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Precise value retrieval for a single location.
*   **Reason:** If the primary task is reading the exact numerical value (e.g., "What was the sales figure in Texas in 2019?"), a bar chart's length encoding is perceptually more accurate than estimating the area of a circle.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision in reading individual values. Humans are worse at judging area changes than length changes.
*   **The Risk:** Symbol overlap (occlusion) in dense geographic regions.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using 3D bars extruding from the map to "save space."
*   **Why it fails:** 3D projection adds perspective distortion, making comparisons even harder than 2D bar charts.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there axes or multiple bars sitting on top of map regions?
*   **The Test:** Can you instantly see the "hot spots" on the map, or do you have to stop and compare bar heights?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Replace the bar charts with circles sized by the variable of interest.
*   **Best Fix:** If representing two variables, use circle size for one and color saturation/hue for the other (as used in the top-performing design E-2 in [@zeng_review_2023]).
