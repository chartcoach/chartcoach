---
id: permute-pixels-for-aggregation
title: Scramble Pixels Within Colorfields for Aggregation
bibliography: references.bib
description: Randomly permuting pixels within a data block improves the user's ability
  to perceive the average color.
labels:
- chart:colorfield
- visual:texture
- task:aggregate
- complexity:advanced
- data:high-density
---

## The Rule <!-- role: advice -->
When designing color-based visualizations (like colorfields) specifically for judging averages over fixed blocks, randomly permute or shuffle the pixels within those blocks.

## The Logic <!-- role: reason -->
Scrambling the data points within a region places different colors closer together, facilitating the eye's ability to "pool" them into a single average perception.
*   **The Principle:** Spatial Frequency and Visual Pooling.
*   **The Evidence:** [@correll_comparing_2012] found that permuted (shuffled) colorfields yielded statistically better performance than ordered colorfields. By breaking local patterns, the visual system processes the region as a texture or ensemble, making the summary statistic (the average) more accessible.

## Where to Apply <!-- role: context -->
This is a specialized technique for high-density data where the summary of a region is more important than the sequence within it.
*   **User Goal:** Comparing the average density or value of two distinct blocks of data (e.g., "Is Month A hotter than Month B?").
*   **Data Type:** Dense series data where the aggregation boundaries (e.g., months, gene blocks) are fixed and known.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the sequential trend *within* the block is relevant (e.g., "Did sales increase *during* January?").
*   **Reason:** Permutation destroys the internal time-ordering and low-level patterns (like slopes) within the shuffled block [@correll_comparing_2012].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You completely destroy the local topology and continuity of the data. The user cannot see if the values were rising or falling within that specific time block.
*   **The Risk:** The visualization may look like "static" or noise, potentially confusing users unfamiliar with the encoding.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Permuting a line graph (shuffling the x-positions of the points).
*   **Why it fails:** [@correll_comparing_2012] showed that while permuting colorfields helps, permuting line graphs offers no performance benefit and breaks shape continuity.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the colorfield block look like a smooth gradient?
*   **The Test:** If the block looks like a gradient, the user might be biasing their average based on the largest contiguous area of color. Permutation should make the block look like a uniform texture or noise field.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If you cannot permute, ensure the color scale is perceptually linear to aid averaging.
*   **Best Fix:** Implement a "2D Permuted Colorfield" where the pixels inside the specific aggregation bin (e.g., the rectangle representing January) are randomly shuffled spatially.
