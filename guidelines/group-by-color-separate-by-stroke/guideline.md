---
id: group-by-color-separate-by-stroke
title: Group Categories by Color but Separate with Strokes
bibliography: references.bib
description: Assign the same color to related sub-categories and use white strokes
  to distinguish them.
labels:
- chart:treemap
- chart:stacked-bar
- visual:border
- visual:color
- data:hierarchical
---

## The Rule <!-- role: advice -->
If you have many categories that belong to larger groups (e.g., distinct countries within the continent of "Europe"), give all items in the group the same color. Distinguish the individual items by separating them with a visible stroke (usually white).

## The Logic <!-- role: reason -->
This technique reduces the color palette from "number of items" (which could be 50+) to "number of groups" (e.g., 5). The eye perceives the aggregate area of the color as the total share of the group, while the strokes ensure the granular data (the individual pieces) is still visible and accessible [@muth_fewer_colors_2022].

## Where to Apply <!-- role: context -->
*   **User Goal:** Seeing both the macro distribution (totals) and the micro composition (parts).
*   **Data Type:** Hierarchical data, Treemaps, Stacked Bar charts, or Area charts.
*   **Audience:** Readers needing to understand composition without being overwhelmed by a rainbow palette.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The strokes become so thick relative to the data size that they distort the perception of area.
*   **Reason:** In very dense datasets, the ink of the border strokes may overwhelm the ink of the data itself.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to identify specific sub-items by color alone.
*   **The Risk:** Adjacent items of the same color might blend if the stroke is too thin or projected on a low-resolution screen.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using slightly different shades of blue for every country in "Europe."
*   **Why it fails:** The human eye cannot reliably distinguish 20 shades of blue, leading to confusion.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are adjacent blocks merging into a single blob?
*   **The Test:** Can you count the number of individual boxes within a color block? If not, your stroke is missing or too thin.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a white border to all chart elements.
*   **Best Fix:** Use variable stroke widths—thicker strokes to separate major groups, thinner strokes to separate items within a group [@muth_fewer_colors_2022].
