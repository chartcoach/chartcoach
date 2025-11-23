---
id: start-design-process-unclassed
title: Start the Design Process with Unclassed Scales
bibliography: references.bib
description: Begin with an unclassed view to understand the data structure before
  deciding whether to simplify with classes.
labels:
- process:design
- visual:color
- task:analysis
- impact:accuracy
---

## The Rule <!-- role: advice -->
Always start your design process by looking at an unclassed (continuous) version of your map, even if you intend to publish a classed version.

## The Logic <!-- role: reason -->
Starting with an unclassed view allows you to see the raw distribution of the data, including subtle differences between regions and potential outliers. This informs whether you *should* simplify the data into classes and helps you make a conscious decision about where those class breaks should occur [@muth_classed_vs_unclassed_2021].

## Where to Apply <!-- role: context -->
*   **Phase:** The exploration and drafting phase of any data visualization project involving color scales.
*   **User:** The designer or analyst creating the chart.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Strictly ordinal/categorical data.
*   **Reason:** As established in other guidelines, ordinal data should not be viewed as continuous.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Time. It requires an extra step of analysis before finalizing the design.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** applying default class breaks (like equal interval or quantiles) immediately without looking at the data distribution.
*   **Why it fails:** You might accidentally split a cluster of similar values into different colors, or group outliers with normal values, misrepresenting the reality of the data.

## How to Check <!-- role: check -->
*   **The Test:** Did you see the "noisy" version of the map before you made the "clean" version? If not, you skipped this step.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Toggle your tool's settings to "continuous" temporarily to inspect the data.
