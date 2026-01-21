---
id: prefer-proportional-symbol-map-small-multiples-over-dorling-cartogram-small-multiples-for-correlation
title: Prefer Proportional Symbol Map Small Multiples Over Dorling Cartogram Small
  Multiples
bibliography: references.bib
description: Within small-multiple geo-temporal designs for correlation identification,
  proportional-symbol map small multiples ranked above Dorling-cartogram small multiples
  for both time and accuracy in this study.
labels:
- chart:map
- chart:small-multiples
- task:correlate
- visual:area
- visual:color-saturation
- visual:position
- data:spatiotemporal
- data:quantitative
- audience:expert
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

If you are already using small-multiple maps to judge correlation over space and time, prefer proportional-symbol maps over Dorling cartograms.

## The Logic <!-- role: reason -->

Both options present time as facets, but this study’s overall correlate rankings place proportional-symbol small multiples ahead of Dorling-cartogram small multiples for both accuracy and completion time (without reporting a significant pairwise difference between them).

- **The Principle:** Choose the within-family variant that ranks best under the same task and metrics.
- **The Evidence:** For the correlate task, E-2 (proportional symbol map small multiples) ranked above E-1 (Dorling cartogram small multiples) for both accuracy and time; significance pairs were not reported between E-2 and E-1 (pairs list empty for accuracy; time significance only reported vs E-3) [@pena-arayaComparisonVisualizationsIdentifying2020]. This guideline is expressed in the structured collation style proposed in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify correlation (and related evolution characterization as tested) across locations and time.
- **Data Type:** Geographical entities over multiple time steps; two+ quantitative variables encoded using area and color saturation.
- **Audience:** Visualization-literate analysts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You specifically need a cartogram representation (e.g., you must encode a variable via region size/topology distortion as a primary requirement).
- **Reason:** This comparison does not override non-negotiable representational requirements; it only reports relative performance rankings under the tested task.

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up the cartogram-specific representational style (circles placed to reflect regions in a Dorling cartogram).
- **The Risk:** If users rely on cartogram conventions in your domain, switching to proportional symbols may reduce familiarity (not measured in the extracted results).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating “ranked higher” as “statistically proven better” for this specific pair.
- **Why it fails:** The extracted significance pairs do not include E-2 > E-1 for either metric, so you should interpret this as a preference based on ranking, not a confirmed significant difference [@pena-arayaComparisonVisualizationsIdentifying2020].

## How to Check <!-- role: check -->

- **Visual Sign:** You are using Dorling cartogram small multiples even though proportional symbols would meet the same encoding needs (area + color saturation) and you do not require cartogram-specific distortion.
- **The Test:** List your hard requirements; if none requires a cartogram, you can likely switch.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Keep the small-multiple layout but replace Dorling cartogram circles-as-regions with proportional symbols over a base map.
- **Best Fix:** Implement the proportional-symbol small-multiple design pattern that ranked highest in this study’s correlate results (E-2), as captured in the collation dataset format described by [@zengReviewCollationGraphical2023] and sourced from [@pena-arayaComparisonVisualizationsIdentifying2020].
