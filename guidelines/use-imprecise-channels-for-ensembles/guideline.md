---
id: use-imprecise-channels-for-ensembles
title: Use Imprecise Channels for Aggregate Tasks
bibliography: references.bib
description: Utilize channels like color or area for tasks involving averages, clusters,
  or summary statistics.
labels:
- chart:heatmap
- task:summarize
- task:cluster
- visual:color
- visual:area
- impact:speed
---

## The Rule <!-- role: advice -->
Use visual channels often considered "imprecise" (such as color intensity or area) when the user's task involves summarizing sets of values, such as finding averages, clusters, or outliers, rather than comparing individual points.

## The Logic <!-- role: reason -->
The ranking of visual variables (where position is best and color is worst) applies primarily to individual value extraction. For "ensemble" tasks, this hierarchy changes.
*   **The Principle:** **Ensemble Coding**. The human visual system can rapidly process aggregate properties (like mean or variance) from channels like color and area, sometimes more effectively than from positional encodings [@bertini_why_2020].
*   **The Evidence:** [@bertini_why_2020] cite recent work on perceptual psychology showing that encodings imprecise for individual values (like color) provide performance benefits for aggregate tasks like summarizing a set of values by a single number (e.g., mean, cluster).

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying the average value of a group, finding clusters, or detecting "oddball" outliers.
*   **Data Type:** High-volume data where individual points are less important than the group behavior.
*   **Audience:** Users performing statistical estimation or exploratory data analysis.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Pairwise Comparison.
*   **Reason:** If the user needs to compare the magnitude of exactly two items within the group, color or area will be too ambiguous compared to position on an axis.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision in decoding any single data point is significantly reduced.
*   **The Risk:** Users might perceive differences in values that are not statistically significant due to the lower resolution of the visual channel.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Forcing all data into bar charts or dot plots to ensure "accuracy."
*   **Why it fails:** This can clutter the view and make it harder to see the "forest for the trees" (the aggregate property) [@bertini_why_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using a complex positional chart (like a box plot or detailed scatter) when the user just needs to know "is this region generally hot or cold?"
*   **The Test:** Can the user instantly identify the average or cluster without scanning individual marks?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Apply color coding (redundantly) to existing positional marks to aid in clustering.
*   **Best Fix:** Use a density plot, heatmap, or color-coded grid to represent the aggregate values directly.
