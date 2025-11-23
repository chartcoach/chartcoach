---
id: avoid-horizon-graphs-for-rapid-similarity-search
title: Avoid Horizon Graphs For Rapid Similarity Comparisons
bibliography: references.bib
description: Horizon graphs perform significantly slower than line charts or colorfields
  when users must scan for similar time series patterns.
labels:
- chart:horizon-graph
- chart:line-chart
- task:cluster
- task:compare
- visual:shape
- visual:color
- impact:efficiency
- data:time-series
---

## The Rule <!-- role: advice -->
Do not use horizon graphs when the primary user task involves quickly scanning, clustering, or identifying similar patterns across multiple time series; use standard line charts or colorfields instead.

## The Logic <!-- role: reason -->
While horizon graphs are space-efficient, the mental cost of decoding the "banded" encoding (where values are split and layered by color) significantly impedes rapid visual processing. Experimental results collated by Zeng and Battle [@zeng_review_2023] and conducted by Gogolou et al. [@gogolou_comparing_2019] demonstrate that horizon graphs are consistently the slowest visualization for similarity tasks. Users must mentally reconstruct the signal shape from the bands to assess similarity, creating a cognitive bottleneck that does not exist with standard positional or color-density encodings.

*   **The Principle:** Decoding Latency
*   **The Evidence:** [@zeng_review_2023], [@gogolou_comparing_2019]

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapidly identifying similar trends, clustering waveforms, or finding "nearest neighbor" patterns.
*   **Data Type:** Multiple dense time series (e.g., EEG signals, server metrics).
*   **Audience:** Domain experts or analysts performing high-volume visual scanning.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Vertical screen space is extremely limited (e.g., a dashboard tracking hundreds of metrics in a small list).
*   **Reason:** The spatial compactness of horizon graphs may outweigh the speed penalty if standard line charts would be too flat to read or require excessive scrolling.
*   **Scenario:** The task is reading precise values rather than comparing overall shapes.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the high data density and vertical space-saving benefits of horizon graphs.
*   **The Risk:** In tasks involving similarity judgment, using horizon graphs can slow down user performance by approximately 33% to 40% compared to line charts or colorfields [@gogolou_comparing_2019].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Increasing the number of bands in a horizon graph to increase precision.
*   **Why it fails:** This adds more visual complexity and color boundaries, making the shape even harder to perceive quickly for similarity comparisons.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using layered bands of color to represent a single time series in a context where users need to compare shapes?
*   **The Test:** Ask a user to find "two matching signals" in a set of 20. If they hesitate or trace the bands with their eyes/finger, the visualization is likely too complex for the task.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Revert to standard Line Charts (small multiples).
*   **Best Fix:** If the data density is high and the task is purely about spotting clusters or trends, switch to Colorfields (1D heatmaps), which were found to be the fastest for this specific task [@gogolou_comparing_2019].
