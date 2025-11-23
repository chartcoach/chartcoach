---
id: avoid-faceting-for-speed
title: Avoid Faceting When Speed Is Priority
bibliography: references.bib
description: Faceted charts (small multiples) significantly increase task completion
  time compared to single-view plots.
labels:
- chart:small-multiples
- chart:scatterplot
- task:retrieve-value
- impact:efficiency
- visual:row
- visual:column
---

## The Rule <!-- role: advice -->

Avoid splitting data into faceted rows or columns (small multiples) if the user needs to perform rapid visual scanning or lookup tasks.

## The Logic <!-- role: reason -->

While faceted charts are accurate, they force the eye to travel longer distances and often require scrolling, which significantly increases the time required to complete tasks.
*   **The Principle:** Interaction Cost and Eye Travel.
*   **The Evidence:** In the performance rankings collated by Zeng and Battle [@zeng_review_2023], the faceted designs from Kim and Heer [@kim_assessing_2018] (E-11, E-12) consistently ranked lower in the `time` metric for retrieval tasks, despite often having acceptable accuracy rankings.

## Where to Apply <!-- role: context -->

*   **User Goal:** Rapid assessment or quick lookup of values (e.g., a dashboard for real-time monitoring).
*   **Data Type:** Categorical data used to split the view (e.g., Product Category).
*   **Audience:** Users under time pressure.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** When the dataset is extremely dense and suffers from severe occlusion (overplotting) in a single view.
*   **Reason:** In high-density scenarios, the accuracy penalty of occlusion in a single chart outweighs the time penalty of faceting.

## The Price <!-- role: costs -->

*   **The Sacrifice:** You lose the ability to isolate categories completely, potentially leading to occlusion if all data is in one chart.
*   **The Risk:** Clutter increases in a single view, which might make specific points harder to distinguish even if the general lookup is faster.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Creating a "trellis" or grid of 20+ small charts to show every category clearly.
*   **Why it fails:** The user must scan sequentially through many disparate axes, slowing down the search process dramatically.

## How to Check <!-- role: check -->

*   **Visual Sign:** Does the visualization require the user to scroll or move their eyes across multiple distinct axes to see the whole picture?
*   **The Test:** Time yourself finding a specific data point. Compare it to finding the same point in a single color-coded scatterplot.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Combine the facets into a single view and use color (hue) to distinguish the categories.
*   **Best Fix:** Use a single view with interactive filtering or highlighting to allow users to focus on specific categories without breaking the spatial continuity.
