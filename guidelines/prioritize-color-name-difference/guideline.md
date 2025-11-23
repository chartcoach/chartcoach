---
id: prioritize-color-name-difference
title: Select Colors with Distinct Linguistic Names
bibliography: references.bib
description: Use color naming probability to select palette colors, as it predicts
  discriminability better than mathematical color distance.
labels:
- chart:scatterplot
- chart:map
- task:identify
- visual:color
- impact:accuracy
- data:nominal
- data:categorical
---

## The Rule <!-- role: advice -->
When selecting a categorical color palette, choose colors that are linguistically distinct (e.g., "Red" vs. "Green") rather than relying solely on mathematical perceptual distance (e.g., CIELAB distance).

## The Logic <!-- role: reason -->
While mathematical models like CIEDE2000 measure perceptual distance, human performance in distinguishing categories is better predicted by "Name Difference"—the degree to which two colors have distinct color-name association probabilities.
*   **The Principle:** Name Difference (ND).
*   **The Evidence:** In controlled experiments comparing scatterplots and maps, Gramazio et al. [@gramazio_colorgorical_2017] demonstrated that Name Difference was a stronger predictor of response time and accuracy than standard Perceptual Distance. This finding is highlighted in the review by Zeng and Battle [@zeng_review_2023].

## Where to Apply <!-- role: context -->
This applies to any visualization using color to separate distinct categories.
*   **User Goal:** Rapidly identifying or discriminating between category members.
*   **Data Type:** Nominal (categorical) data.
*   **Chart Types:** Scatterplots, Maps, Bar Charts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Continuous Data.
*   **Reason:** When visualizing gradients or continuous values (ordinal/quantitative), linguistic distinctness is less important than perceptual ordering (luminance/saturation).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Aesthetic preference often correlates with hue similarity. Maximizing naming distinctness often results in high-contrast, "clashing" colors that users may rate as less aesthetically pleasing.
*   **The Risk:** Users may find the visualization "ugly" or "chaotic" if the colors are too disparate.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a palette where colors look different side-by-side but share a common name (e.g., "Chartreuse" and "Lime").
*   **Why it fails:** If a user mentally categorizes both as "Green," the cognitive load to distinguish them increases during visual search tasks.

## How to Check <!-- role: check -->
*   **The Test:** The "Telephone" Test. Can you describe the colors to someone over the phone using simple names (Blue, Red, Pink, Orange) without them getting confused? If you have to say "The darker teal" and "the lighter teal," the Name Difference is too low.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Replace ambiguous colors with primary or secondary colors that have strong, single-word names.
*   **Best Fix:** Use a palette generation tool that incorporates Name Difference or naming probability models (like Colorgorical) to ensure semantic separation.
