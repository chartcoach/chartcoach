---
id: use-multi-hue-ucs-for-precision
title: Use Perceptually Uniform Multi-Hue Colormaps for Precision
bibliography: references.bib
description: Prioritize multi-hue schemes like Viridis over single-hue schemes when
  fine-grained data discrimination is required.
labels:
- visual:color
- task:compare
- impact:accuracy
- data:quantitative
- data:continuous
---

## The Rule <!-- role: advice -->
Encode continuous quantitative data using perceptually uniform multi-hue colormaps (such as Viridis) rather than single-hue schemes when users need to distinguish small value differences.

## The Logic <!-- role: reason -->
While single-hue colormaps preserve order well, they lack the necessary resolution for fine-grained comparisons. By ramping through both hue and luminance simultaneously, multi-hue schemes provide greater color separation.
*   **The Principle:** Perceptual Resolution.
*   **The Evidence:** In triplet comparison tasks, single-hue maps (like *Blues*) exhibited significantly higher error rates when the data span was small. In contrast, the multi-hue *Viridis* colormap maintained high accuracy across both small and large data spans [@liu_somewhere_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** When the viewer needs to discern both small local variations and large global differences.
*   **Data Type:** Continuous scalar fields, such as heatmaps or high-resolution density plots.
*   **Audience:** Users performing analytical tasks requiring precise similarity judgments.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data represents discrete categories or very coarse buckets (e.g., 5-7 classes).
*   **Reason:** The study found that single-hue colormaps perform comparably to multi-hue maps when the value distance between points is large [@liu_somewhere_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the extreme simplicity of a monotonic single-hue ramp, which some users may find intuitively easier to order (dark is more, light is less) without a legend.
*   **The Risk:** If the multi-hue map is not perceptually uniform, it may introduce false artifacts (banding).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a standard single-hue ramp for a high-density heatmap.
*   **Why it fails:** Details in the data will be lost because the visual system cannot discriminate the subtle luminance steps in a single hue as well as it can distinct hue-luminance combinations [@liu_somewhere_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the visualization look "flat" or featureless in areas where you know there is data variation?
*   **The Test:** Select two data points with values close to each other (e.g., 5% difference). Can you easily distinguish their colors without reference to the legend?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch the colormap to *Viridis*, *Plasma*, or *Magma*.
*   **Best Fix:** Use a perceptually uniform multi-hue scale generated in the CAM02-UCS color space.
