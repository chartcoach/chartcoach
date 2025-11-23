---
id: compact-scatterplots-class-separation
title: Use Compact Scatterplots for Faster Class Separation
bibliography: references.bib
description: Smaller scatterplot dimensions can lead to significantly faster performance
  when separating visual clusters.
labels:
- chart:scatterplot
- task:cluster
- visual:size
- impact:speed
- visual:position
---

## The Rule <!-- role: advice -->
When the user's task is to identify or separate distinct clusters (classes) in a scatterplot, consider using a smaller, more compact chart size rather than filling a large high-resolution display.

## The Logic <!-- role: reason -->
Experimental results highlight that smaller visualization footprints can accelerate cluster recognition. In the review by @zeng_review_2023, the design labeled E-4 (referenced as the "Previous Study" or "S" condition in @micallef_towards_2017) ranked first for speed in the cluster separation task. This design was significantly smaller (300px width) compared to the optimized (1120px) or standard (480px) variants, allowing users to perceive the gestalt of the groups faster.

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapidly assessing how many groups or classes exist in the data.
*   **Data Type:** Multiclass 2D quantitative data.
*   **Audience:** Exploratory data analysis tools where users scan many plots quickly (e.g., scatterplot matrices/SPLOMs).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Dense, overlapping clusters.
*   **Reason:** If the clusters are extremely tight or overlapping, a small plot will exacerbate occlusion, making separation impossible regardless of speed benefits.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Resolution and detail.
*   **The Risk:** Users might miss fine-grained boundaries between classes or confuse noise for a cluster due to the lower pixel count.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Making every scatterplot full-screen to "see it better."
*   **Why it fails:** For simple cluster perception, larger distances between points require more eye movement, slowing down the cognitive process of grouping.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart require eye-scanning to see all groups, or can the whole pattern be seen in a single glance?
*   **The Test:** If you have to move your eyes significantly to compare two clusters, the chart may be too large for this specific task.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reduce the width and height of the scatterplot container.
*   **Best Fix:** Use "Small Multiples" or a scatterplot matrix approach, keeping individual plots compact to facilitate rapid scanning.
