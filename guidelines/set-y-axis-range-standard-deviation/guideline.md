---
id: set-y-axis-range-standard-deviation
title: Set Y-Axis Range to 1.5 Standard Deviations
bibliography: references.bib
description: Optimize the y-axis range based on standard deviation to accurately communicate
  effect sizes in scientific data.
labels:
- chart:bar
- chart:line
- task:compare
- visual:scale
- impact:accuracy
- data:statistical
- audience:expert
- source:witt_2019
---

## The Rule <!-- role: advice -->
When plotting group means for scientific data where effect sizes are standardized, set the y-axis range to approximately 1.5 standard deviations (SDs). Calculate this by centering the axis on the grand mean and extending it 0.75 SDs in either direction. Avoid defaulting to the full theoretical range (e.g., 0–100) or the minimal range required to fit the data.

## The Logic <!-- role: reason -->
This range maximizes the congruence between the *visual size* of an effect and the *actual size* of the effect (e.g., Cohen’s *d*). 
*   **The Principle:** Visual-Conceptual Size Compatibility. When the visual magnitude aligns with the statistical magnitude, readers process effect sizes automatically with less mental effort [@witt_graph_2019].
*   **The Evidence:** In five experiments, participants were most sensitive to differences in effect sizes and showed the least bias when the axis range was set to ~1.5 SDs. A "Full" range (0-100) biased users to see effects as small, while a "Minimal" range biased users to see effects as big [@witt_graph_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurately estimating the magnitude of an effect (e.g., distinguishing a "medium" effect from a "large" effect).
*   **Data Type:** Behavioral science data (or similar fields) where effect size is standardized based on standard deviation and interpreted via conventions like Cohen's *d*.
*   **Audience:** Readers interpreting statistical significance and magnitude, particularly in academic or research contexts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Fields where Standard Deviation is unknown or irrelevant.
*   **Reason:** The 1.5 SD rule relies on the reader's implicit or explicit understanding of SD as a benchmark for "large" or "small" effects. In these cases, Tufte’s Lie Detector Ratio may be more appropriate [@witt_graph_2019].
*   **Scenario:** When the calculation results in nonsensical numbers.
*   **Reason:** If extending 0.75 SDs down creates negative numbers for a metric that cannot be negative (e.g., accuracy percentage), the range must be adjusted [@witt_graph_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may lose the "zero baseline" for bar charts, which contradicts common design advice (e.g., "Bar charts must always start at zero").
*   **The Risk:** If the audience is unfamiliar with the 1.5 SD convention, they might misinterpret the truncated axis as an attempt to exaggerate differences, unless clearly captioned.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Letting software default to the "Minimal" range (just above/below the data points).
*   **Why it fails:** This consistently causes users to overestimate effect sizes, labeling small or non-significant effects as "big" [@witt_graph_2019].
*   **The Wrong Fix:** Always defaulting to the "Full" theoretical range (e.g., 0 to 100% for test scores).
*   **Why it fails:** This causes users to underestimate effect sizes, creating a bias where almost all effects look "small" or "null" [@witt_graph_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the graph show a vast amount of empty white space (Full Range) or look dramatically zoomed in on minor variances (Minimal Range)?
*   **The Test:** Calculate the Grand Mean of your data. Calculate the Standard Deviation. Check if the Y-axis Max is roughly `Mean + (0.75 * SD)` and Y-axis Min is roughly `Mean - (0.75 * SD)`.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Manually set the axis start and end points in your graphing software to the calculated 1.5 SD range.
*   **Best Fix:** Programmatically calculate the limits based on the data's standard deviation to ensure consistency across multiple plots (e.g., `ylim = c(mean - 0.75*sd, mean + 0.75*sd)`).
