---
id: explicitly-label-diverging-legends
title: Explicitly Label Diverging Color Scales
bibliography: references.bib
description: Always include a clear legend or key for diverging scales, as they lack
  the intuitive logic of sequential scales.
labels:
- visual:color
- visual:text
- impact:usability
- audience:general
---

## The Rule <!-- role: advice -->
Always provide an explicit legend, color key, or annotated title when using a diverging color scale. Do not rely on the reader's intuition.

## The Logic <!-- role: reason -->
Diverging scales are less intuitive than sequential scales.
*   **The Principle:** Perceptual ambiguity.
*   **The Evidence:** While sequential scales (light to dark) intuitively map to "low to high," diverging scales are ambiguous. A red color might mean "hot" (more), "danger" (bad), or "fewer" (as seen in the U.S. births heatmap). Without a key, readers may incorrectly assume red means "more" when it actually means "less" [@muth_diverging_vs_sequential_2021].

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurate interpretation of values.
*   **Data Type:** Any dataset visualized with two opposing hues.
*   **Audience:** All audiences, but especially those unfamiliar with the specific dataset.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Standardized Conventions.
*   **Reason:** If the color mapping is culturally universal in that specific context (e.g., Blue=Democrat / Red=Republican in US politics), a legend *might* be skippable, though still risky.

## The Price <!-- role: costs -->
*   **The Sacrifice:** It takes up more space and requires more design effort than a "self-explanatory" sequential chart.
*   **The Risk:** If the legend is missed, the chart is unreadable.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assuming "Red is always bad" or "Red is always high."
*   **Why it fails:** In the example of U.S. births, red indicated *fewer* births, reversing the standard "heat map" expectation [@muth_diverging_vs_sequential_2021].

## How to Check <!-- role: check -->
*   **The Test:** Show the chart to someone without the title. Can they tell you which color represents the "high" value and which represents the "low" value? If they hesitate, you need a better legend.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a standard color bar legend.
*   **Best Fix:** Turn the chart title into a color key (coloring the words "High" and "Low" to match the data) or add annotations directly pointing to extreme values explaining what they mean [@muth_diverging_vs_sequential_2021].
