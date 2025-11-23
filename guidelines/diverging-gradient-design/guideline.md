---
id: diverging-gradient-design
title: Design Diverging Gradients with a Light Grey Center
bibliography: references.bib
description: Use diverging gradients for deviations from a baseline, ensuring the
  center is light grey, not white.
labels:
- visual:color
- chart:heatmap
- chart:choropleth
- data:diverging
---

## The Rule <!-- role: advice -->
When visualizing deviation from a baseline (like a national average), use a diverging color palette with clearly distinguishable hues for both sides. Ensure the center color—representing the baseline or zero—is a light grey, not pure white.

## The Logic <!-- role: reason -->
A diverging palette emphasizes how variables divert from a norm. The center needs to be neutral to signify the baseline. According to [@muth_colors_2018], the center should be "ideally a light grey, not white," likely to maintain some visual presence and distinguish "no data" (often white) from "average data" (grey).

## Where to Apply <!-- role: context -->
*   **User Goal:** Seeing positive or negative growth, or performance above/below average.
*   **Data Type:** Diverging quantitative data (e.g., profit/loss, temperature anomaly).
*   **Audience:** Analysts looking for extremes.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Sequential data (0 to 100).
*   **Reason:** Diverging palettes imply a neutral middle point. If data is strictly positive and sequential, use a single-direction gradient.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You need three colors (two hues + grey) rather than just two.
*   **The Risk:** If the two hues are not distinct enough (e.g., red vs. orange), readers can't quickly distinguish positive from negative.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a rainbow or continuous single-hue scale for diverging data.
*   **Why it fails:** It hides the "neutral" point and makes it hard to see where the data crosses the baseline.

## How to Check <!-- role: check -->
*   **Visual Sign:** A map where the average value is bright white or invisible.
*   **The Test:** Look at the areas with "average" values. Do they disappear completely into the page background?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the center point color code to a very light grey (e.g., #f0f0f0).
*   **Best Fix:** Use a standard diverging scheme (like Purple-Grey-Orange) ensuring distinct hues on the extremes.
