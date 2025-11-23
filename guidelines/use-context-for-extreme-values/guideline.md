---
id: use-context-for-extreme-values
title: Use Integrated Contexts for Extreme Values
bibliography: references.bib
description: Use stacked bars or framed axes for values near 0% or 100% to improve
  precision.
labels:
- chart:stacked-bar
- chart:dot-plot
- task:estimate
- visual:position
- impact:precision
- data:proportion
---

## The Rule <!-- role: advice -->
Use stacked bars or encodings that explicitly visualize the full range (0% to 100%) when displaying values that are very high (near 100%) or very low (near 0%).

## The Logic <!-- role: reason -->
Providing visual boundaries (the start and end of the range) allows the viewer to anchor their perception.
*   **The Principle:** Endpoint Anchoring (Weber's Law mitigation). For a lone bar, error increases as the bar gets taller (Weber's Law). However, in a bounded context, the 100% mark resets the percept. A 95% bar is perceived as "5% away from the top," which is as precise as perceiving a 5% bar from the bottom [@mccoleman_no_2021].
*   **The Evidence:** The study found that overall reproduction error was lower (~10%) in "integrated" conditions (like stacked bars) compared to stand-alone bars, particularly because the end-point helps triangulate the value [@mccoleman_no_2021].

## Where to Apply <!-- role: context -->
*   **User Goal:** High-precision estimation of values at the extremes of a scale.
*   **Data Type:** Percentages or proportions that are <25% or >75%.
*   **Audience:** Users needing to assess how close a value is to completion or emptiness.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the value is near 50%.
*   **Reason:** The integrated context creates a "category repulsion" effect around the midpoint, causing systematic bias (overestimating values above 50% and underestimating those below) [@mccoleman_no_2021].

## The Price <!-- role: costs -->
*   **The Sacrifice:** While *absolute* error decreases (the spread of mistakes is smaller), *signed* error (bias) may increase in the middle of the chart.
*   **The Risk:** You introduce a systematic bias where values are pushed away from the 50% mark.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a simple floating bar chart for values like 98%.
*   **Why it fails:** Without the 100% anchor, the viewer must estimate the length of a very long bar, which is prone to underestimation (regression to the mean) [@mccoleman_no_2021].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do extreme values (e.g., 90%+) have a visible "ceiling" or reference line nearby?
*   **The Test:** If you cover the top of the chart, is it hard to tell if the bar is 90% or 95%? If yes, you need the context.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a clear grid line or axis mark at 100%.
*   **Best Fix:** Convert the chart to a stacked bar or a "thermometer" style graphic where the empty space is clearly visible.
