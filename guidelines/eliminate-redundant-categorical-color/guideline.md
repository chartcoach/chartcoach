---
id: eliminate-redundant-categorical-color
title: Remove Redundant Color in Categorical Charts
bibliography: references.bib
description: Use position rather than color to distinguish categories in simple bar
  charts to avoid visual clutter.
labels:
- chart:bar
- chart:column
- visual:color
- impact:simplicity
- data:categorical
---

## The Rule <!-- role: advice -->
Do not assign different colors to every category in a simple bar or column chart. If the bars are already separated by position and gaps, use a single color for all bars.

## The Logic <!-- role: reason -->
In a standard bar chart, categories are spatially separated (position) and often labeled on an axis. Adding a unique color to each bar performs a job that is already being done by the chart's layout. Removing these colors reduces visual noise and prevents the chart from looking like a "confetti party" [@muth_fewer_colors_2022].

## Where to Apply <!-- role: context -->
*   **User Goal:** Showing a simple distribution or comparison of categories.
*   **Data Type:** Categorical data where no sub-grouping or additional encoding is required.
*   **Audience:** General audience needing quick readability without distraction.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The color encodes a meaningful data variable (e.g., performance vs. target).
*   **Reason:** The color is data, not just decoration.
*   **Scenario:** You need to highlight a specific bar.
*   **Reason:** You would use one color for the highlight and a neutral color (gray) for the rest.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The chart may look less "fun" or vibrant initially.
*   **The Risk:** Without distinct colors, it is impossible to reference bars by color name (e.g., "Look at the red bar").

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a rainbow palette for 12 different regions just to make them look distinct.
*   **Why it fails:** It creates visual overwhelm and implies differences in data classification that don't exist.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does every bar have a different hue (red, blue, green) even though they represent the same metric?
*   **The Test:** Turn the chart to grayscale. If the data is still perfectly readable and understandable, the colors were likely redundant.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Set all bars to the same neutral or brand color (e.g., all blue).
*   **Best Fix:** Use a single color for all bars, then use a second color only if you need to highlight a specific category for storytelling.
