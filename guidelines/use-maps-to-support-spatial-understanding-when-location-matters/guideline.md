---
id: use-maps-to-support-spatial-understanding-when-location-matters
title: Use maps or geo-referencing when location is essential to the message
bibliography: references.bib
description: Use maps or geo-referencing to help readers interpret patterns, scope,
  and comparisons that depend on place.
labels:
- chart:map
- task:compare
- visual:position
- impact:clarity
- data:geospatial
- audience:novice
- complexity:basic
---

## Use maps or geo-referencing when location is essential to the message <!-- role: advice -->

Use a map or geo-referenced view when the audience needs spatial relationships to interpret the data. If the key comparisons depend on where something happens, anchor the data to recognizable places.

## Why maps help viewers interpret place-based meaning <!-- role: reason -->

Maps leverage familiar geographic structure so people can connect data to known locations and reason about distance, proximity, and regional scope. This reduces the translation work readers must do to reconstruct “where” from non-spatial encodings and can shift interpretation from abstract values to situational understanding.

**Mechanism:** Geographic context provides a stable mental reference frame, helping viewers infer spatial patterns (clusters, spread, adjacency) and relate quantities to real-world places.

**Evidence:** Viewers commonly interpreted crisis maps as geographic overviews that raised awareness and supported thinking through implementation and decision scenarios. [@koesten_encountering_2025] Maps and country-to-country comparisons often draw strong reader engagement in practice, indicating they are a compelling format for place-based communication. [@schuster_who_2023]

**Notes:** A map can support both exploratory “where is this happening?” questions and explanatory communication about the geographic extent of an issue.

## When to use a map or geo-referenced display <!-- role: context -->

- **User Goal:** Understand where something is happening and what areas are most affected.
- **Task:** Compare regions, identify hotspots, assess coverage, or communicate geographic scope.
- **Data:** Observations with coordinates, administrative regions (country/state/county), routes, or location-linked aggregates.
- **Chart Setting:** Static reports, dashboards, articles, or briefings where geographic context is available and interpretable.
- **Audience:** Readers who recognize the geography (or can be supported with labels) and benefit from place-based framing.
- **Success Criterion:** Readers can correctly identify affected locations and spatial patterns without mentally mapping categories to places.

## When not to use a map <!-- role: exceptions -->

**Break it when:** The main task is precise value comparison or ranking across many regions and location is not needed to interpret differences. **Why:** Map geometry and unequal area can make comparisons harder and can hide small regions.

## Tradeoffs of using maps <!-- role: costs -->

**Sacrifice:** Maps can consume more space and design time than simpler charts. **Risk:** Readers may over-interpret visual prominence (large areas) or miss small/dense regions, especially without careful labeling. **Mitigation:** Plan for legible labels and consider companion summaries when exact comparisons matter.

## Common ways maps fail <!-- role: mistakes -->

**Mistake:** Using a map just because the data has location fields, even when the message is non-spatial. **Why it fails:** The map adds cognitive load without improving understanding of the intended comparison.

## Quick checks for whether a map is doing useful work <!-- role: check -->

**Failure Sign:** Readers talk about “where” ambiguously (or not at all) and instead ask for a table or ranking to understand differences. **Quick Check:** If you remove the basemap and the graphic still communicates the same takeaway, the map context may be unnecessary. **Stronger Test:** Ask a small set of readers to answer “which places are most affected and where are they relative to each other?” and confirm they can do so quickly and consistently.

## What to do instead if a map is not the right choice <!-- role: fix -->

- Use a ranked bar chart when the primary task is comparing magnitudes across places.
- Use a table with clear sorting and grouping when readers need exact values and lookup.
- Use small multiples by region (or facets) when geographic context is secondary but place-based grouping still matters.
- Use a dot plot or slope chart for country-to-country comparisons when location is only an identifier, not the analytic frame.
