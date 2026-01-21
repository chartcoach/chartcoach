---
id: use-rainbow-or-sequential-choropleth-for-filtering-values-when-accuracy-matters
title: Use Choropleth Maps (Rainbow or Sequential) for Filtering Values
bibliography: references.bib
description: For filtering values on quantitative maps, choropleth variants ranked
  above isarithmic variants in accuracy regardless of rainbow vs sequential scheme.
labels:
- chart:map
- task:filter
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- map-type:choropleth
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When the task is to filter/select regions meeting a value condition on a quantitative map, prefer a choropleth map over an isarithmic map; either rainbow hue or sequential saturation can be used.

## The Logic <!-- role: reason -->

In the reported comparison, choropleth designs were more accurate for filter than isarithmic designs, and the top rank was shared by choropleth rainbow and choropleth sequential.

- **The Principle:** Map representation can dominate color-scheme choice for selection tasks
- **The Evidence:** For **filter (accuracy)**, the top rank group is **E-1 (RC-Choro)** and **E-3 (SC-Choro)**, followed by **E-2 (RC-Isa)** and **E-4 (SC-Isa)**; significant differences are reported between each choropleth design and each isarithmic design [@golbiowskaRainbowDashIntuitiveness2022]. This finding is included in the graphical perception knowledge collation for recommendation systems [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Filter/select map units satisfying a condition (e.g., “find areas in the target range”)
- **Data Type:** Quantitative values shown on a map with ordered classes
- **Audience:** General audiences doing map-based value selection

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are optimizing for time rather than accuracy in filtering.
- **Reason:** For **filter (time)**, the extracted results show a tie among E-1/E-2/E-3 with E-4 last, and no significant pairwise differences were recorded; this rule is only supported for **accuracy** [@golbiowskaRainbowDashIntuitiveness2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** If you avoid isarithmic maps, you may lose the continuous-field look that some users expect for smooth phenomena.
- **The Risk:** Choropleth boundaries may suggest artificial discontinuities (a representational tradeoff not evaluated here).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching palettes (rainbow↔sequential) while keeping an isarithmic map, expecting filtering accuracy to improve.
- **Why it fails:** The observed accuracy separation is between **map types** (choropleth vs isarithmic), not between RC vs SC within choropleth [@golbiowskaRainbowDashIntuitiveness2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Users frequently pick regions that are clearly outside the thresholded condition.
- **The Test:** A/B test choropleth vs isarithmic with the same class thresholds and legend; measure selection accuracy for the filter prompt [@golbiowskaRainbowDashIntuitiveness2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Re-render the same data as a choropleth map (keeping your existing palette family if needed).
- **Best Fix:** In a visualization recommender, add a task-conditioned preference: for **filter**, boost choropleth map candidates over isarithmic ones, consistent with the collated evidence [@zengReviewCollationGraphical2023; @golbiowskaRainbowDashIntuitiveness2022].
