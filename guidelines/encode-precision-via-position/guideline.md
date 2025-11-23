---
id: encode-precision-via-position
title: Encode Precise Values Using Position or Length
bibliography: references.bib
description: Prioritize position and length over area or intensity when viewers need
  to make precise quantitative judgments.
labels:
- chart:bar
- chart:scatter
- visual:position
- visual:length
- impact:precision
- task:estimate
---

## The Rule <!-- role: advice -->

When precise quantitative judgments are required, map data values to position or length. Avoid mapping these values to area (size) or intensity (color saturation/brightness).

## The Logic <!-- role: reason -->

Human vision processes specific visual features with varying degrees of precision. Research shows that viewers can estimate ratios between values with high precision when encoded by position along a common scale, and slightly less precision with length. Area and intensity are far less precise features for extracting specific values [@zacks_designing_2020].

*   **The Principle:** Hierarchy of Graphical Perception
*   **The Evidence:** Studies asking viewers to guess ratios between values show lower error rates for position/length compared to area/intensity [@zacks_designing_2020].

## Where to Apply <!-- role: context -->

*   **User Goal:** The viewer needs to read specific values or make fine-grained comparisons between data points (e.g., "Is A exactly twice as large as B?").
*   **Data Type:** Quantitative data requiring accuracy.
*   **Audience:** Decision-makers needing to evaluate specific metrics rather than general "big picture" trends.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Overview or "Big Picture" Analysis
*   **Reason:** Area and intensity are effective for summarizing statistics across large arrays (e.g., heatmaps) where the goal is identifying broad patterns or outliers rather than reading specific numbers [@zacks_designing_2020].

## The Price <!-- role: costs -->

*   **The Sacrifice:** Charts using position/length (like bar charts or dot plots) may require more spatial dimensions or screen real estate compared to compact forms like heatmaps or color-coded grids.
*   **The Risk:** Visual clutter increases if too many data points are plotted using position/length, potentially obscuring the pattern.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Using color saturation (heatmaps) to represent precise financial or scientific data.
*   **Why it fails:** The visual system is poor at judging precise ratios based on color intensity, and background contrast can create illusions that distort perceived values [@zacks_designing_2020].

## How to Check <!-- role: check -->

*   **Visual Sign:** Are you using a color scale or bubble size to represent the primary metric that users need to compare accurately?
*   **The Test:** Ask a user to estimate the numerical ratio between two data points. If they struggle or have high error rates, the encoding is likely too low-precision.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Add text labels to the area/color visualizations to provide the precise values.
*   **Best Fix:** Change the chart type to a bar graph, dot plot, or line chart where the primary variable is mapped to spatial position.
