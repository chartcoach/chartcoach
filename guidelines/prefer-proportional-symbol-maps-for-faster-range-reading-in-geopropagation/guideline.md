---
id: prefer-proportional-symbol-maps-for-faster-range-reading-in-geopropagation
title: Use Proportional-Symbol Maps When Speed Matters for Range Reading
bibliography: references.bib
description: For range-reading tasks, proportional-symbol maps were faster than small-multiple
  maps in one geospatial propagation comparison study.
labels:
- chart:map
- task:determine-range
- visual:color-saturation
- visual:position
- impact:speed
- data:geospatial
- data:temporal
- audience:expert
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use a proportional-symbol map rather than small-multiple maps when the primary goal is faster performance on determine-range tasks.

## The Logic <!-- role: reason -->

Using one map view with symbols avoids scanning many small choropleth panels, reducing visual search overhead when judging ranges.

- **The Principle:** Reduce cross-panel scanning for range judgments.
- **The Evidence:** The collated results report proportional-symbol map (E-2) ranked faster than small-multiple maps (E-1) for determine-range-1 and determine-range-2 time outcomes in [@pena-arayaComparisonGeographicalPropagation2020], as recorded by [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Determining ranges (span) quickly.
- **Data Type:** Geo-temporal propagation data encoded on a map.
- **Audience:** Analysts/expert users performing timed analytic tasks.

## When to Break It <!-- role: exceptions -->

- **Scenario:** When determine-range accuracy is the overriding goal (not speed).
- **Reason:** The same collated record ranks small-multiple maps (E-1) above proportional-symbol maps (E-2) for determine-range-2 accuracy (no reported significant pair).

## The Price <!-- role: costs -->

- **The Sacrifice:** You may not gain accuracy for range judgments.
- **The Risk:** If users need exactness, the faster option may not be the most accurate in all range task variants.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to proportional symbols and assuming it will also improve accuracy for range tasks.
- **Why it fails:** The collated outcomes include a range-accuracy ordering that can reverse depending on the specific range task variant.

## How to Check <!-- role: check -->

- **Visual Sign:** Users spend time bouncing across many small panels to gauge span.
- **The Test:** Time a short pilot (or think-aloud) on a range question; if participants take longer with small multiples than with a single symbol map, this rule likely applies.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace small multiples with a single proportional-symbol map for the range-focused view.
- **Best Fix:** Provide both views and default to proportional-symbol for range-reading workflows where time is critical, while offering small multiples when accuracy is prioritized.
