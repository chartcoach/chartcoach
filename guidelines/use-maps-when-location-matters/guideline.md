---
id: use-maps-when-location-matters
title: Use Maps to Show Spatial Patterns
bibliography: references.bib
description: Use maps or geo-referenced views when location is essential to understanding
  the data and its implications.
labels:
- chart:map
- task:locate
- task:compare
- visual:position
- impact:clarity
- data:spatial
- audience:general
- domain:geography
---

## The Rule <!-- role: advice -->

Use a map or geo-referenced chart when location is central to the message; otherwise, use a non-spatial chart.

## The Logic <!-- role: reason -->

Maps leverage familiar place-based mental models so viewers can interpret patterns through spatial relationships and known geography, which can increase comprehension and engagement.

- **The Principle:** Spatial grounding through familiar geographic context
- **The Evidence:** Viewers commonly interpret crisis maps as clear geographic overviews that support awareness and can even inform decisions [@koesten_encountering_2025]. Practitioners report that audiences strongly prefer maps and that cross-country comparisons often perform well in engagement metrics [@schuster_who_2023].

## Where to Apply <!-- role: context -->

Apply this when the key insight depends on where something happens.

- **User Goal:** Understand geographic scope, hotspots, proximity, regional disparities, or country-to-country differences
- **Data Type:** Geo-referenced points, lines, polygons, regions (e.g., countries, states, districts), or values that can be reliably joined to places
- **Audience:** Broad audiences (including non-experts) who benefit from recognizable locations, and decision-makers who need geographic overview [@koesten_encountering_2025]

## When to Break It <!-- role: exceptions -->

Skip the map when geography is incidental or misleading.

- **Scenario:** You need precise value comparison across many categories (e.g., ranking 30 regions by rate)
- **Reason:** Area/shape differences and spatial scanning make exact comparisons harder than bar/dot charts.
- **Scenario:** The data is not meaningfully tied to geography (weak or arbitrary geocoding, unclear boundaries)
- **Reason:** A map implies spatial causality and can invite incorrect interpretations.

## The Price <!-- role: costs -->

Maps trade comparability and simplicity for spatial context.

- **The Sacrifice:** Reduced precision for comparing values across places; more space and design effort (projection, basemap, labels)
- **The Risk:** Overemphasis on large geographic areas, visual clutter at dense locations, or misreads caused by projection and aggregation choices

## Common Mistakes <!-- role: mistakes -->

Common failures come from using maps as decoration or as a default.

- **The Wrong Fix:** Using a choropleth for raw counts (e.g., total cases) without normalization
- **Why it fails:** It conflates population/area with intensity and distorts the message.
- **The Wrong Fix:** Mapping too many categories with many colors
- **Why it fails:** Viewers cannot reliably distinguish many hues on a spatial field.
- **The Wrong Fix:** Forcing country comparisons onto a map when a ranked dot plot would answer the question faster
- **Why it fails:** The map adds scanning burden without improving understanding of differences.

## How to Check <!-- role: check -->

- **Visual Sign:** Readers must hunt for places, can’t tell what’s high/low without repeatedly checking the legend, or the main takeaway is not geographic.
- **The Test:** Ask: “If I remove the geography (replace the map with a ranked dot/bar chart), do I lose the core insight?” If not, the map is unnecessary.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add clear geographic framing (title stating what the map shows, labeled key places, appropriate normalization like per-capita rates, simplified basemap).
- **Best Fix:** Switch to a non-spatial chart for comparisons (ranked dot/bar) and keep a small locator map only if spatial orientation is still helpful.
