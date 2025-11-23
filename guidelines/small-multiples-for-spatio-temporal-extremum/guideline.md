---
id: small-multiples-for-spatio-temporal-extremum
title: Use Small Multiples to Identify Spatio-Temporal Extrema
bibliography: references.bib
description: Small multiple maps outperform glyph maps for finding maximum values
  in propagation data.
labels:
- chart:small-multiples
- chart:glyph-map
- task:find-extremum
- data:spatio-temporal
- visual:juxtaposition
- impact:accuracy
- impact:efficiency
---

## The Rule <!-- role: advice -->
When visualizing propagation data (such as disease spread) on a map over time, use **Small Multiples** (juxtaposed maps) rather than **Glyph Maps** (superimposed symbols) if the user needs to find extreme values (peaks).

## The Logic <!-- role: reason -->
Research comparing visualization techniques for geographical propagation shows that Small Multiples significantly outperform Glyph Maps in both **accuracy** and **time** for finding extrema. Juxtaposing time steps allows the user to scan for peak color/value intensities across the grid more effectively than decoding complex superimposed glyphs on a single map.
*   **The Evidence:** In experimental results, Small Multiples (E-1) ranked significantly higher than Proportional Symbol/Glyph Maps (E-2) for the `find-extremum` task in both accuracy and completion time [@zeng_review_2023; @pena-araya_comparison_2020].

## Where to Apply <!-- role: context -->
*   **User Goal:** The user needs to identify when and where a phenomenon reached its maximum intensity (e.g., "In which region and time step was the infection rate highest?").
*   **Data Type:** Spatio-temporal data where values change across regions over time steps.
*   **Visual Encoding:** Comparing a grid of choropleth maps (Small Multiples) versus a single map with complex glyphs (e.g., area-circles encoding time steps).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to determine the specific arrival time or propagation direction (e.g., "When did the disease first reach Region X?").
*   **Reason:** While Small Multiples excel at peaks, some evidence suggests Glyph Maps may perform better for specific range-based or arrival-time queries where the user focuses on a single location [@pena-araya_comparison_2020].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate. Small multiples require displaying many maps simultaneously, which reduces the resolution of each individual map compared to a single full-screen Glyph Map.
*   **The Risk:** If the geographic details are very fine, the reduced size of small multiples might make it hard to distinguish small regions.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using complex "clock" glyphs or "timeline" glyphs overlaid on every region of a single map.
*   **Why it fails:** This creates visual clutter and increases the cognitive load required to compare values across different regions and time steps simultaneously.

## How to Check <!-- role: check -->
*   **The Test:** Ask a user to find the "highest value" in the dataset. Measure how long it takes them.
*   **Visual Sign:** If using Glyphs, does the map look cluttered? Do glyphs overlap? If using Small Multiples, are the maps too small to read?

## How to Fix <!-- role: fix -->
*   **Best Fix:** unroll the time dimension into a grid of Small Multiples, ensuring the color scale is consistent across all frames to allow pre-attentive processing of "darkest" (peak) spots.
