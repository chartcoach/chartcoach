---
id: align-grouping-channels
title: Align Visual Grouping with Data Categories
bibliography: references.bib
description: Use proximity and color to visually group data points that belong to
  the same conceptual category.
labels:
- chart:scatter
- chart:bar
- visual:color
- visual:proximity
- impact:clarity
- task:cluster
---

## The Rule <!-- role: advice -->

Organize visual patterns so that grouping by proximity, shape, and color reflects the true grouping in the data. Ensure that data points belonging to the same category are spatially close or share distinct visual features.

## The Logic <!-- role: reason -->

The visual system automatically clusters objects based on Gestalt principles like proximity, shared color, and orientation. If visual groups (e.g., clusters of dots) do not match the semantic data groups (e.g., regions), the viewer will struggle to process the information. Effective grouping guides attention and facilitates comparison [@zacks_designing_2020].

*   **The Principle:** Perceptual Grouping
*   **The Evidence:** Viewers can effortlessly compare large groups of symbols if they are grouped by color or space. Lack of such grouping forces slow, serial reading of labels [@zacks_designing_2020].

## Where to Apply <!-- role: context -->

*   **User Goal:** Comparing aggregates or clusters (e.g., "How does the Northern region compare to the Southern region?").
*   **Data Type:** Categorical data or data with distinct subsets.
*   **Audience:** Users needing to see relationships between categories without reading every individual label.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** When individual data points are outliers that naturally fall far from their semantic group (e.g., a geographical map).
*   **Reason:** In a map, spatial proximity is dictated by geography, not category. You cannot move a country to make it fit a visual cluster; you must rely on color/shape instead [@zacks_designing_2020].

## The Price <!-- role: costs -->

*   **The Sacrifice:** Sorting by category (to create spatial proximity) prevents sorting by value (ranking high to low), which might obscure the "top 10" rankings.
*   **The Risk:** Outliers within a group might be overlooked if the visual grouping is too strong or if the data point falls far away from its peers (e.g., in a scatterplot).

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Randomly arranging bars or points and relying solely on text labels to distinguish categories.
*   **Why it fails:** It prevents the visual system from utilizing its automatic clustering abilities, forcing the user to read text serially [@zacks_designing_2020].

## How to Check <!-- role: check -->

*   **Visual Sign:** Do items of the same category appear scattered randomly across the chart?
*   **The Test:** Squint your eyes. Do the blobs of color or clusters of dots correspond to meaningful categories in your data?

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Color-code the bars or points by category.
*   **Best Fix:** Re-sort the axis to place items of the same category next to each other (spatial proximity) AND use color to reinforce that grouping.
