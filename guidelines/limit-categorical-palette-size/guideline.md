---
id: limit-categorical-palette-size
title: Limit Categorical Palettes to Five Colors
bibliography: references.bib
description: Reduce palette size to minimize discrimination errors and maintain aesthetic
  preference.
labels:
- visual:color
- task:identify
- impact:accuracy
- data:categorical
---

## The Rule <!-- role: advice -->
Restrict categorical color palettes to 5 or fewer colors whenever possible. If you must go higher, expect a significant drop in user performance.

## The Logic <!-- role: reason -->
Visual discrimination accuracy degrades linearly as palette size increases. In experiments by [@gramazio_colorgorical_2017], the number of discrimination errors increased significantly from 3-color palettes (79 errors) to 5-color (119 errors) to 8-color palettes (190 errors). Furthermore, the predictability of aesthetic preference models breaks down as palette size increases (specifically at 5 colors), making it harder to balance aesthetics and function.

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurate data retrieval and comparison.
*   **Data Type:** Nominal/Categorical data.
*   **Audience:** All users.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-cardinality data where grouping is impossible.
*   **Reason:** If you must show 10 categories, you have no choice, but you should switch strategies (e.g., use labeling or interactivity) rather than relying solely on color discrimination.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Information Density.
*   **The Risk:** You may need to group smaller categories into an "Other" bin, potentially hiding granular details.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using 10+ distinct colors (e.g., the "Tableau 10" approach) for complex layouts without secondary cues.
*   **Why it fails:** Even with maximally distinct colors, error rates roughly double between 3-color and 8-color palettes [@gramazio_colorgorical_2017].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you relying on a legend with more than 5 items?
*   **The Test:** Count the distinct hues required to decode the chart. Is it > 5?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Group low-frequency categories into "Other" (gray).
*   **Best Fix:** Use "small multiples" or facet the data to reduce the number of categories displayed in a single view.
