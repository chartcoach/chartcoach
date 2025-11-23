---
id: use-diverging-scales-for-contrast
title: Use Diverging Scales to Increase Visual Contrast
bibliography: references.bib
description: Use diverging scales to reveal subtle differences in data by compressing
  the gradient range.
labels:
- visual:color
- task:compare
- impact:clarity
- data:density
---

## The Rule <!-- role: advice -->
Use a diverging scale to reveal subtle differences between data points that appear identical on a sequential scale.

## The Logic <!-- role: reason -->
Diverging scales offer higher perceptual resolution because they split the data range into two gradients.
*   **The Principle:** Gradient Compression.
*   **The Evidence:** In a sequential scale covering 0–100%, a 10% difference is a small step along a single gradient. In a diverging scale (e.g., 50–100% on one side), the gradient covers half the numerical range, making a 10% difference visually larger. The blog post demonstrates this with Russia and Turkey: on a sequential map, they look similar; on a diverging map, the contrast between them is obvious [@muth_diverging_vs_sequential_2021].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing values that are numerically close but distinct.
*   **Data Type:** Data clustered around specific ranges where differentiation is critical (e.g., heatmap dates showing slight seasonal increases).
*   **Audience:** Analysts looking for patterns (e.g., "late summer phenomenon" in birth rates) [@muth_diverging_vs_sequential_2021].

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Broad overviews.
*   **Reason:** If precise comparison is not the goal, the increased contrast might look like visual noise.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the simplicity of a single hue.
*   **The Risk:** You may overstate the significance of small differences if the gradient is too steep.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a sequential scale with low contrast for dense data.
*   **Why it fails:** Subtle patterns (like the "weekend effect" vs. "seasonal effect" in birth rates) get washed out because the color steps are too small to perceive [@muth_diverging_vs_sequential_2021].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do two regions look the same color, but the tooltip shows they are 15-20% apart?
*   **The Test:** Check the difference between Russia and Turkey (or similar adjacent data points). If they look identical but shouldn't, the scale needs more contrast.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Switch to a diverging scale centered on the median or average of the dataset to maximize contrast among the visible values.
