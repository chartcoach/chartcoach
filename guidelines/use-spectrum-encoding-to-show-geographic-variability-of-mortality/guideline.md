---
id: use-spectrum-encoding-to-show-geographic-variability-of-mortality
title: Use Saturation-Based Spectrum Encoding to Show Geographic Variability
bibliography: references.bib
description: Represent geographic mortality variation with a map (Area) plus a spectrum
  scale (saturation) and a legend.
labels:
- chart:map
- task:explore
- visual:color
- impact:pattern-detection
- data:geospatial
- audience:expert
- visual:saturation
---

## The Rule <!-- role: advice -->

When the goal is to explore geographic variability of mortality, use an Area-based map and encode magnitude with a Spectrum (e.g., darker saturation = higher rate), with a clear legend.

## The Logic <!-- role: reason -->

To present mortality through the lens of geography, the visualization should organize entities by spatial attributes (Area). To help users assess variability across the globe, the paper uses Spectrum encoding via color saturation and provides a Token+Spectrum legend to interpret the scale. [@olaSimpleChartsDesign2016]

- **The Principle:** Spatial organization + spectral magnitude encoding supports geographic pattern finding
- **The Evidence:** [@olaSimpleChartsDesign2016]

## Where to Apply <!-- role: context -->

- **User Goal:** See where mortality (cause- or risk-specific) is high/low and compare regions broadly
- **Data Type:** Geospatial data aggregated by regions/country clusters; continuous rates
- **Audience:** Public health professionals exploring regional burden patterns

## When to Break It <!-- role: exceptions -->

- **Scenario:** Geography is not the analytical focus and spatial location would not aid the task (e.g., purely demographic comparison).
- **Reason:** The paper sometimes represents geographic entities without spatial dimensions when geography is not central to the question. [@olaSimpleChartsDesign2016]

## The Price <!-- role: costs -->

- **The Sacrifice:** Exact value reading may be less immediate than in a table/precise chart.
- **The Risk:** Without a legend, saturation differences can be misread. [@olaSimpleChartsDesign2016]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing a map without a spectrum legend or without clear aggregation boundaries.
- **Why it fails:** Users cannot interpret saturation values reliably or understand what geographic unit each area represents. [@olaSimpleChartsDesign2016]

## How to Check <!-- role: check -->

- **Visual Sign:** Users ask “What does this shade mean?” or confuse units/regions.
- **The Test:** Remove hover/tooltips and see if the legend alone supports correct qualitative judgments (higher vs lower). [@olaSimpleChartsDesign2016]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a Spectrum legend with representative swatches and numeric ranges.
- **Best Fix:** Combine the map with linked views that let users drill from cluster-level map patterns to within-cluster comparisons (as in the paper’s geography visualization). [@olaSimpleChartsDesign2016]
