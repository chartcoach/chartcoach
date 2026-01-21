---
id: choose-map-type-by-geometry-of-your-data
title: Choose Choropleth, Symbol, or Locator Maps Based on Your Geographic Data
bibliography: references.bib
description: Use choropleths for region-level values, symbol maps for many locations,
  and locator maps for a few points or event locations.
labels:
- chart:map
- task:show-geography
- visual:position
- impact:clarity
- data:geospatial
- audience:mainstream
- source:datawrapper
---

## The Rule <!-- role: advice -->

Match the map type to the geographic form of your data: choropleth for administrative regions, symbol map for many specific locations, and locator map for a few points or event locations.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Geographic encoding works best when the visual mark matches the data’s spatial unit (areas vs points) so readers don’t infer false precision.
- **The Evidence:** The post distinguishes choropleth maps (region-level values), symbol maps (many specific locations), and locator maps (few points/events in smaller areas) [@muth_chart_types_guide_2025].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Seeing geographic patterns and locating places.
- **Data Type:** Geospatial data as either (1) region-aggregated values, (2) many point locations, or (3) a small number of points/events.
- **Audience:** Mainstream/general readers (who “like maps,” especially when they can find themselves) [@muth_chart_types_guide_2025].

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** Your data isn’t meaningfully geographic (location is incidental to the message).
- **Reason:** The post frames maps as a good choice when the goal is explicitly to show geographic patterns; otherwise, other chart families may be clearer [@muth_chart_types_guide_2025].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Maps can emphasize place recognition over precise comparison of values.
- **The Risk:** Choosing the wrong map type can imply the wrong spatial unit (e.g., showing point phenomena as region shading) [@muth_chart_types_guide_2025].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Using a choropleth when you actually have many precise locations.
- **Why it fails:** Choropleths are for administrative-region data; point locations should be symbols so readers see actual distribution [@muth_chart_types_guide_2025].

## How to Check <!-- role: check -->

- **Visual Sign:** The map’s marks (areas vs points) don’t match how the data is collected (regions vs locations).
- **The Test:** Ask: “Is each value tied to a boundary (municipality/province) or to a coordinate (place/event)?” Then pick choropleth vs symbol/locator accordingly [@muth_chart_types_guide_2025].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap to the correct map type (choropleth ↔ symbol ↔ locator) without changing the underlying data.
- **Best Fix:** If you have both region values and key points, split into two maps (or a map plus a chart) so each layer uses the right mark type [@muth_chart_types_guide_2025].
