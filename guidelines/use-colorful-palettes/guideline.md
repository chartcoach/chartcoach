---
id: use-colorful-palettes
title: Use a Broad Color Palette
bibliography: references.bib
description: Visualizations with seven or more colors are statistically more memorable
  than those with few colors.
labels:
- visual:color
- impact:memorability
- style:aesthetic
---

## The Rule <!-- role: advice -->
Use a colorful palette (specifically 7 or more distinct colors) to enhance the memorability of the visualization.

## The Logic <!-- role: reason -->
There is a statistically significant correlation between the number of distinct colors in a visualization and its memorability score. Visualizations with 7+ colors performed better than those with 2–6 colors, which in turn performed better than those with 1 color or black-and-white gradients. [@borkin_what_2013] suggests this may be because colorful images are easier to discriminate and store as distinct distinct scenes in memory.

*   **The Principle:** Visual Discrimination
*   **The Evidence:** [@borkin_what_2013] (Section 7.2, Fig 4)

## Where to Apply <!-- role: context -->
*   **User Goal:** Creating an impression that lasts.
*   **Data Type:** Nominal data with many categories, or complex diagrams.
*   **Audience:** General audiences where aesthetic appeal and retention are drivers.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Precise data comparison or accessible design for colorblind users.
*   **Reason:** Using 7+ colors often leads to "rainbow messes" that make analytical comparison difficult or impossible for color-deficient viewers. Standard perception guidelines (like Few or Tufte) warn against excessive color for this reason.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Analytical clarity and accessibility.
*   **The Risk:** Creating a "fruit salad" effect where the colors have no semantic meaning, confusing the data analysis.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Applying random distinct colors to a single data series (e.g., a bar chart where every bar is a different color for no reason).
*   **Why it fails:** While memorable, this destroys the grouping logic of the chart, making the data harder to read even if the image is easier to remember.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart look monochromatic or duotone?
*   **The Test:** Count the distinct hues. If the count is 1, 2, or 3, the visualization is in the lower tier for predicted memorability.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Introduce color coding for categories that were previously monochrome.
*   **Best Fix:** Use color strategically to differentiate complex parts of a diagram or map, ensuring the variety creates visual distinctiveness without compromising data grouping.
