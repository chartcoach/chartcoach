---
id: nominal-data-color-hue
title: Use Color Hue for Nominal Categories
bibliography: references.bib
description: Use distinct color hues for categorical data to ensure differentiation
  without implying rank.
labels:
- chart:scatter
- chart:bar
- visual:color-hue
- data:nominal
- data:categorical
- task:categorize
- impact:discriminability
---

## The Rule <!-- role: advice -->
Map nominal (categorical) data to distinct color hues. Do not use color saturation or luminance to distinguish between categories.

## The Logic <!-- role: reason -->
Nominal data consists of discrete categories with no inherent order (e.g., "Apple," "Banana," "Cherry").
*   **The Principle:** **Expressiveness.** A visualization should express all facts in the data and only the facts in the data.
*   **The Evidence:** Theoretical reviews in graphical perception indicate that color hue (CH) is effective for nominal data because humans perceive different hues as distinct but not necessarily ranked [@zeng_review_2023]. Conversely, varying saturation or luminance implies a magnitude or order that does not exist in nominal data, potentially misleading the viewer [@bujack_good_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Distinguishing between different groups or classes without comparing their value magnitude.
*   **Data Type:** Nominal or Categorical data (T-2 in the theoretical design space).
*   **Audience:** General audiences needing to quickly identify group membership.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data contains an excessively high number of categories (e.g., > 10).
*   **Reason:** The human eye has limited discriminative power for hue; a palette with too many hues becomes indistinguishable. In such cases, separating data into small multiples or using labels is preferred.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to encode a third quantitative variable using the color channel (e.g., you cannot use the color to show "profit" if you are using it to show "region").
*   **The Risk:** If the luminance of the hues varies significantly (e.g., a bright yellow vs. a dark blue), users may incorrectly perceive an implicit ranking or emphasis.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a single hue and varying the saturation (e.g., light blue for Group A, dark blue for Group B).
*   **Why it fails:** Users will perceive the darker/more saturated group as "more" or "higher" than the lighter group, which is false for nominal data.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the legend look like a gradient (ramp) or a collection of distinct swatches?
*   **The Test:** Ask a viewer, "Is the red category 'greater' than the blue category?" If they say "no" or "that makes no sense," the design is correct.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch the color palette to a categorical scheme (e.g., Tableau 10, Set2).
*   **Best Fix:** Ensure the palette uses colors that are distinct in hue but relatively uniform in perceptual lightness to avoid accidental emphasis.
