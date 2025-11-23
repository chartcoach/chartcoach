---
id: explicit-aggregation-for-summaries
title: Explicitly Encode Aggregates for Summary Tasks
bibliography: references.bib
description: Visualizing raw data is insufficient for determining averages; explicitly
  encoded summary marks significantly improve performance.
labels:
- chart:composite-graph
- chart:box-plot
- task:aggregate
- visual:length
- visual:color-saturation
- data:time-series
- impact:accuracy
---

## The Rule <!-- role: advice -->
Overlay explicit summary marks (such as bars representing means) on top of raw time-series data when the user needs to estimate averages.

## The Logic <!-- role: reason -->
Viewers struggle to accurately compute mathematical averages visually from raw data points alone.
*   **The Evidence:** In the collation by [@zeng_review_2023] of the study by [@albers_task-driven_2014], the "Composite Graph" (E-4)—which overlays a bar chart of means onto a line chart—ranked first for aggregation tasks. It significantly outperformed the standard line graph (E-1) and raw color fields (E-5). Even in color-based charts, the "Color Stock Chart" (E-6), which explicitly encodes the mean as a block, significantly outperformed the continuous "Colorfield" (E-5).
*   **The Principle:** Explicit Encoding. Reducing the cognitive load of "visual math" by pre-calculating and rendering the statistical summary allows for faster and more accurate retrieval.

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying or comparing average values across time periods (e.g., "Which month had the highest average sales?").
*   **Data Type:** High-density quantitative time-series data where local noise might obscure global trends.
*   **Audience:** Analysts or general users who need to switch between granular details and high-level summaries.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the user's primary task is strictly to identify specific raw data points or anomalies without regard for the general trend.
*   **Reason:** The overlay (e.g., the bars in the Composite Graph) can introduce visual clutter that might distract from individual data points, though Albers et al. [@albers_task-driven_2014] found the Composite Graph still performed reasonably well for extremum tasks.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual simplicity and data-ink ratio. You are effectively doubling the number of marks for the same time period (raw line + aggregate bar).
*   **The Risk:** Occlusion. The aggregate bars might hide underlying raw data points if transparency or layering is not handled correctly.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on a standard line chart (E-1) and expecting users to "eyeball" the average.
*   **Why it fails:** The standard line chart ranked last (7th) for aggregation tasks in the experimental results [@albers_task-driven_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart only show the "wiggly" raw line?
*   **The Test:** Ask a user to quickly point to the time period with the highest average. If they trace the whole line with their finger to estimate, the design is lacking explicit aggregation.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a horizontal reference line for the global mean.
*   **Best Fix:** Switch to a Composite Graph (E-4) where the underlying raw data (line) is superimposed over discrete bars representing the local average for each time step.
