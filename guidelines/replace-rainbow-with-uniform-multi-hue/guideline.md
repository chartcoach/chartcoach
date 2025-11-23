---
id: replace-rainbow-with-uniform-multi-hue
title: Replace Rainbow Colormaps with Perceptually Uniform Multi-Hue Scales
bibliography: references.bib
description: Use perceptually uniform scales like Viridis instead of Jet to improve
  accuracy and speed in value retrieval tasks.
labels:
- chart:heatmap
- chart:scatterplot
- visual:color-saturation
- visual:color-hue
- task:retrieve-value
- impact:accuracy
- impact:speed
---

## The Rule <!-- role: advice -->
Do not use rainbow colormaps (like Jet) for quantitative data. Instead, use perceptually uniform multi-hue scales (like Viridis) that ramp through both hue and luminance simultaneously.

## The Logic <!-- role: reason -->
Rainbow colormaps lack perceptual ordering and often mislead users regarding the magnitude of data changes. Empirical evidence shows that perceptually uniform multi-hue scales significantly outperform rainbow scales in both accuracy and speed for retrieving values.
*   **The Principle:** Perceptual Uniformity and Luminance Ramping
*   **The Evidence:** In controlled experiments, the "Viridis" scale (E-5) consistently ranked higher in accuracy and response time compared to the "Jet" rainbow scale (E-9) [@liu_somewhere_2018]. The systematic review by Zeng and Battle confirms that while rainbow maps are common, they are the most error-prone and slowest for value tasks [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** When users need to estimate values or compare distances between data points based on color.
*   **Data Type:** Quantitative, continuous scalar data.
*   **Audience:** General audiences, particularly where accurate data reading is prioritized over aesthetic familiarity with rainbow schemes.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Categorical (Nominal) Data
*   **Reason:** If the data represents distinct, unordered categories, a rainbow-like palette (qualitative scheme) may be appropriate to maximize distinguishability between unrelated groups, as long as no ordering is implied.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the high saturation variety that some users find aesthetically "colorful" or familiar in legacy scientific visualizations.
*   **The Risk:** Users accustomed to legacy "Jet" scales might initially feel the visualization looks "dull" or different from standard domain conventions.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a standard Single-Hue scale (like Blues) when high resolution is needed.
*   **Why it fails:** While better than rainbow for ordering, single-hue scales may lack the discriminability (resolution) of multi-hue scales for fine-grained differences [@liu_somewhere_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the color scale look like a prism (ROYGBIV)? Do bright yellow/cyan bands appear in the middle of the scale arbitrarily?
*   **The Test:** Convert the visualization to grayscale. If the gradient becomes a jumbled mess of light and dark rather than a smooth ramp, it is likely a rainbow map.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch the colormap to "Viridis," "Magma," or "Plasma."
*   **Best Fix:** Use a perceptually uniform multi-hue scale like Viridis, ensuring the range is calibrated so that the luminance ramp is preserved.
