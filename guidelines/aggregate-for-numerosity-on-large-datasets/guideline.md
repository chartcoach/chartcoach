---
id: aggregate-for-numerosity-on-large-datasets
title: Aggregate Marks for Distribution Tasks on Large Datasets
bibliography: references.bib
description: Switch to density-based encodings when estimating numerosity or distribution
  in large, overplotted datasets.
labels:
- chart:scatterplot
- task:characterize-distribution
- task:aggregate
- visual:density
- impact:scalability
- data:big-data
---

## The Rule <!-- role: advice -->
When visualizing large datasets where marks overlap significantly, switch from individual point encodings to grouping strategies (such as binning or density plots) to support distribution and numerosity tasks.

## The Logic <!-- role: reason -->
Traditional scatterplots fail to scale as data complexity increases.
*   **The Principle:** Overdraw Mitigation. When too many marks compete for screen space, they mask the true density of the data, making it impossible to judge "how many" points are in a cluster.
*   **The Evidence:** [@sarikaya_scatterplots_2018] identifies that while standard scatterplots support object tasks, they fail at `characterize numerosity` and `characterize distribution` when overdraw exists. They recommend "point grouping" strategies (like binning) which sacrifice individual detail to accurately communicate the "numerosity differences in different regions." [@zeng_review_2023] reinforces that effectiveness changes dramatically depending on data characteristics like cardinality.

## Where to Apply <!-- role: context -->
*   **User Goal:** The user wants to see where the "most" data is or understand the overall shape/structure of the dataset.
*   **Data Type:** "Large" (100–1000 points) to "Very Large" (>1000 points) datasets where points overlap.
*   **Audience:** Analysts looking for high-level patterns rather than individual row details.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset is small (<100 points) or sparse.
*   **Reason:** Aggregation in sparse datasets creates misleading visual artifacts and hides the exact position of the few data points available [@sarikaya_scatterplots_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Interaction fidelity. You often lose the ability to implement simple tooltips for individual points.
*   **The Risk:** Misinterpretation of outliers. Outliers might be smoothed away by a Kernel Density Estimation (KDE) or swallowed into a large bin.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Lowering the opacity of individual points (alpha blending) without aggregation.
*   **Why it fails:** While it helps slightly, it eventually saturates ("alpha saturation") and still fails to provide a quantitative measure of density in the most crowded areas [@sarikaya_scatterplots_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the chart a solid blob of color in the center?
*   **The Test:** Can you visually distinguish between a region with 1,000 points and a region with 10,000 points? If both look like a solid block of the same color, you need to aggregate.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Implement hexagonal or rectangular binning (heatmaps).
*   **Best Fix:** Use a "Splatterplot" technique that combines density contours for the dense regions while drawing individual points for the outliers [@sarikaya_scatterplots_2018].
