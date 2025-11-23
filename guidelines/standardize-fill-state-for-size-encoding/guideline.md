---
id: standardize-fill-state-for-size-encoding
title: Do Not Mix Filled and Unfilled Shapes When Encoding Size
bibliography: references.bib
description: Avoid combining filled and unfilled marks in the same visualization if
  size is used to encode data, as this creates perceptual bias.
labels:
- chart:scatterplot
- chart:bubble-chart
- visual:size
- visual:shape
- task:estimate
- impact:accuracy
---

## The Rule <!-- role: advice -->
If you are encoding a quantitative value using **mark size**, ensure all marks share the same fill state (all filled or all unfilled). Do not mix filled shapes with unfilled outlines or line-based symbols (like stars or plus signs).

## The Logic <!-- role: reason -->
Perceived size is not determined solely by mathematical diameter; it is influenced by visual density and fill. A filled object appears larger than an unfilled object of the same actual diameter.
*   **The Principle:** Perceptual Bias in Size Estimation.
*   **The Evidence:** [@zeng_review_2023] notes that "filled shapes... are perceived as larger than their unfilled counterparts." Furthermore, specific shapes (like stars) are perceived as smaller than squares or circles of the same diameter. [@smart_measuring_2019] confirmed this asymmetry, finding that shape strongly influences size perception, leading to systematic underestimation or overestimation depending on the mark type.

## Where to Apply <!-- role: context -->
This advice is critical for visualizations that map a data variable to the area or radius of a point.
*   **User Goal:** Accurately comparing the magnitude of values based on symbol size.
*   **Data Type:** Quantitative data mapped to Size, combined with Nominal data mapped to Shape.
*   **Audience:** Any user attempting to gauge relative values.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The size encoding is purely ornamental or redundant (not used for actual data comparison).
*   **Reason:** If the user does not need to extract values from the size, the perceptual bias is less harmful.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to use "fill vs. no-fill" as a way to encode a binary category (e.g., "Open" vs. "Closed" status) alongside a size variable.
*   **The Risk:** Restricting shape diversity might make it harder to distinguish many categories if you are limited to only "solid" shapes.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a solid circle for "Category A" and a hollow circle for "Category B" while varying the size of both to show "Revenue."
*   **Why it fails:** The hollow circle will look systematically smaller than the solid circle, making Category B's revenue appear lower than it actually is [@smart_measuring_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the legend. Are you mapping a variable to Size while also mapping a variable to Shape?
*   **The Test:** Create two data points with the exact same "Size" value but different shapes (one filled, one hollow). Place them side-by-side. If one looks significantly smaller, you have a bias problem.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Force all shapes to be filled. Differentiate categories by shape geometry (square vs. circle) rather than fill state.
*   **Best Fix:** If size comparison is critical, separate the data into small multiples (facets) or use a bar chart, as area/size comparisons are vulnerable to these shape-induced biases.
