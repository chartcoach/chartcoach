---
id: choose-map-type-by-spatial-data-structure
title: Choose choropleth, symbol, or locator maps based on whether data is by region
  or by point
bibliography: references.bib
description: Use choropleths for administrative regions, symbol maps for many locations,
  and locator maps for a few points or events.
labels:
- chart:map
- task:locate
- visual:position
- impact:clarity
- data:geospatial
- audience:mainstream
- complexity:foundational
---

## Match the map type to whether data is regional or point-based <!-- role: advice -->

Use a choropleth map for values defined over administrative regions, a symbol map for many specific locations, and a locator map for a small set of points or events. Choose the map type that matches how your data is geographically defined.

## Why map types depend on spatial units <!-- role: reason -->

Different map forms encode different geographic units, and mismatching the unit (region vs. point) produces misleading or cluttered spatial signals.

**Mechanism:** Choropleths communicate regional variation through area fills, while symbol/locator maps keep discrete locations explicit; aligning the encoding with the data’s spatial unit preserves interpretability.

**Evidence:** Choropleth maps are recommended for data available in administrative regions, symbol maps for lots of specific locations, and locator (pointer) maps for a few points or events in a smaller area [@muth_chart_types_guide_2025].

**Notes:** This guideline is about selecting a map type, not about projection choice or color scaling.

## Context <!-- role: context -->

- **User Goal:** See geographic patterns or find locations.
- **Task:** Compare regions, locate many sites, or understand where events occurred.
- **Data:** Either region-aggregated values (administrative units) or point locations (coordinates/addresses).
- **Chart Setting:** Articles and reports where readers like to locate themselves or familiar places.
- **Audience:** Mainstream readers.
- **Success Criterion:** Readers interpret the spatial unit correctly and can identify higher/lower regions or key locations.

## Exceptions <!-- role: exceptions -->

**Break it when:** Your main message is not spatial, and the map is only decorative. **Why:** Maps add visual complexity and can distract from non-geographic comparisons.

## Costs <!-- role: costs -->

**Sacrifice:** Space and potentially precision in numeric comparison. **Risk:** Viewers may overinterpret geographic differences that are driven by area size or unit choice. **Mitigation:** Treat the spatial unit choice as part of the message and keep it explicit.

## Mistakes <!-- role: mistakes -->

**Mistake:** Using a choropleth map for point-location data. **Why it fails:** The map implies region-level measurement that the data does not support.

## Check <!-- role: check -->

**Failure Sign:** Readers ask whether values are “per region” or “at a location.” **Quick Check:** Identify whether each value belongs to a region or a point; if it’s a point, avoid choropleths. **Stronger Test:** Ask a reader to describe what a colored area means; if they describe the wrong unit, the map type is mismatched.

## Fix <!-- role: fix -->

- Switch from a choropleth to a symbol map when the data is location-based.
- Use a locator map when you only need to show a few places or an event route.
- Aggregate point data to regions only if regional comparison is truly the goal.
- Replace the map with a bar/column chart if the key message is ranking, not geography.
