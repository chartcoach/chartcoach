---
id: manual-labeling-area-charts
title: Place Area Chart Labels Manually
bibliography: references.bib
description: Disable auto-labeling and place labels directly on the chart for faster
  reading.
labels:
- chart:area
- visual:text
- visual:position
- impact:accessibility
- task:identify
---

## The Rule <!-- role: advice -->
Turn off automatic labeling and place the labels yourself, ideally directly on the colored areas.

## The Logic <!-- role: reason -->
Standard legends or axis labels separate the identifier from the data, increasing cognitive load.
*   **The Principle:** Proximity.
*   **The Evidence:** [@muth_area_charts_2018] argues that readers will be able to read the chart "faster" if labels are placed manually and strategically within the visual field.

## Where to Apply <!-- role: context -->
*   **User Goal:** Quick identification of data series.
*   **Data Type:** Any area chart with sufficient vertical height to contain text.
*   **Audience:** All audiences, particularly those reading quickly.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Extremely thin areas.
*   **Reason:** If an area is too thin to hold text, a direct label might obscure the data. In this case, a line callout or side legend might be necessary.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Automation and time.
*   **The Risk:** Manual labels are static; if the data updates, the labels might overlap or look misplaced.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a separate color legend box.
*   **Why it fails:** It forces eye scanning back and forth.

## How to Check <!-- role: check -->
*   **Visual Sign:** A box of colored squares next to the chart (a standard legend).
*   **The Test:** Can I identify what the blue chunk is without moving my eyes off the blue chunk?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Delete the legend and use text boxes to label the largest areas.
*   **Best Fix:** Use data annotation tools to place labels inside the areas or directly to the right of the final data point.
