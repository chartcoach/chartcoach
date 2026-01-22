---
id: create-observational-annotations-for-extreme-values-to-highlight-outlier-locations
title: Create observational annotations for extreme values to highlight outlier locations
bibliography: references.bib
description: Add callouts pointing to highest and lowest regions so readers can quickly
  identify extremes.
labels:
- chart:map
- task:find-extremes
- visual:text
- impact:attention
- data:geospatial
- audience:novice
- pipeline:annotation
---

## Call out the highest and lowest regions as observational annotations <!-- role: advice -->

Add observational annotations that point to the locations with the highest and lowest values on the map when extremes help summarize the distribution.

## Why extreme-value callouts guide attention on maps <!-- role: reason -->

Readers may not know where to look first on a dense choropleth. Marking extremes provides an immediate entry point for interpreting the distribution and can complement additive annotations that supply external context.

**Mechanism:** Labeling extrema reduces search effort and directs attention to salient data features that are commonly used in narrative graphics.

**Evidence:** The system includes observational annotations that point to extreme values on thematic maps, described as common in narrative visualizations and implemented as part of map output options [@gaoNewsViewsAutomatedPipeline2014].

**Notes:** This is distinct from additive annotations sourced from other articles.

## When extreme-value annotations apply <!-- role: context -->

- **User Goal:** Quickly understand what stands out in the mapped distribution.
- **Task:** Identify maxima and minima and use them as anchors for interpretation.
- **Data:** A mapped numeric variable with meaningful extremes.
- **Chart Setting:** Thematic map with limited time/space for explanation.
- **Audience:** General readers; benefits from guided attention.
- **Success Criterion:** Readers can immediately find at least one salient fact from the map.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Extreme values are not meaningful due to noise or measurement artifacts in the dataset. **Why:** Calling out such extremes can mislead interpretation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Uses annotation space that could be allocated to explanatory context. **Risk:** Over-emphasizes single regions and can imply causality or importance without support. **Mitigation:** Keep the annotation phrasing descriptive and tied to the mapped measure.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding many extreme-value callouts (e.g., top ten) on a small map. **Why it fails:** Visual clutter increases and the map becomes difficult to read.

## Quick tests <!-- role: check -->

**Failure Sign:** Callouts overlap or hide key parts of the map, or readers focus only on one region. **Quick Check:** Limit to a small number of extrema and ensure they are visually distinct. **Stronger Test:** Ask users to report the highest and lowest locations and measure time-to-answer with and without callouts.

## What to do instead <!-- role: fix -->

- Reduce the number of observational annotations to the single highest and single lowest location.
- Use additive annotations only for a small number of locations most related to the story.
- If extremes are unstable, omit observational annotations and rely on overall pattern description.
