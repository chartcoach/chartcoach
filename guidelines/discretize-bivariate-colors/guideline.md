---
id: discretize-bivariate-colors
title: Discretize Colors in Bivariate Maps
bibliography: references.bib
description: Use discrete bins rather than continuous gradients for bivariate value/uncertainty
  maps.
labels:
- chart:heatmap
- chart:choropleth
- task:identification
- visual:color
- impact:readability
- data:continuous
---

## The Rule <!-- role: advice -->
Quantize your data into discrete color bins (classes) rather than using a continuous, smooth color gradient, especially when mapping two variables (value and uncertainty) simultaneously.

## The Logic <!-- role: reason -->
Continuous color maps impose a high "perceptual error" cost—humans struggle to decode exact quantitative values from a smooth gradient. In bivariate maps, where colors are complex mixes of hue, saturation, and lightness, this decoding becomes even harder. Discretization simplifies the matching task.
*   **The Principle:** Reduction of Perceptual Error vs. Quantization Error.
*   **The Evidence:** In the study by [@correll_value-suppressing_2018], discrete maps significantly outperformed continuous maps (63% accuracy vs 47%). Continuous maps performed the worst of all tested conditions.

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying specific values or categories (e.g., "Is this region high-risk or medium-risk?").
*   **Data Type:** Continuous quantitative data being mapped to color.
*   **Audience:** Users who need to read values from a legend.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data requires extremely high precision and the perceptual error is deemed acceptable compared to quantization bias.
*   **Reason:** Discretization introduces "quantization error" (values near the border of a bin look vastly different, while values at opposite ends of a bin look the same). If smooth gradients are vital for seeing subtle transitions, continuous might be preferred, though difficult to read accurately [@correll_value-suppressing_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Data nuances within a bin are lost.
*   **The Risk:** Arbitrary bin boundaries can create artificial sharp edges in the visualization where none exist in the real world (statistically spurious visual patterns).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a smooth 2D gradient (e.g., the "square" continuous legend).
*   **Why it fails:** It forces the user to perform complex inverse color interpolation mental math, which is highly error-prone.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does your legend look like a smooth wash of colors?
*   **The Test:** Can you name the specific color of a data point? In a continuous map, the answer is usually "sort of greenish-blue," which is imprecise.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Bin the data into 3-4 classes per variable (e.g., Low, Med, High).
*   **Best Fix:** Create a 3x3 or 4x4 discrete grid of colors (bivariate legend) to represent the combinations of value and uncertainty.
