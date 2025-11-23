---
id: sub-jnd-visual-enhancement
title: Enhance Objects Below the JND Threshold
bibliography: references.bib
description: Use secondary visual cues like gridlines or text when data differences
  are smaller than the predicted perceptual threshold.
labels:
- chart:bar
- chart:pie
- chart:bubble
- task:compare
- impact:accessibility
- visual:annotation
---

## The Rule <!-- role: advice -->
Explicitly annotate or add reference lines to data points where the value difference is smaller than the Just Noticeable Difference (JND) threshold.

## The Logic <!-- role: reason -->
Human perception has hard limits. When the difference between two visual elements (height, angle, or area) falls below the JND threshold, they become perceptually indistinguishable. To prevent misinterpretation (perceiving different values as identical), secondary visual cues are required. Empirical models can predict these thresholds based on element size and distance.

*   **The Principle:** JND Enhancement / Auxiliary Encodings
*   **The Evidence:** [@lu_modeling_2022], as discussed in [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurate discrimination of similar values.
*   **Data Type:** Any quantitative data where values are clustered closely together.
*   **Audience:** Users making data-driven decisions where small margins matter (e.g., financial reporting).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-level overviews or "infographic" styles.
*   **Reason:** Excessive annotation can cause clutter (chart junk) that obscures the overall trend.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Cleanliness and minimalism.
*   **The Risk:** The chart may become text-heavy, shifting the user from "reading the chart" to "reading the table."

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Ignoring the ambiguity and assuming the user can see the 1 pixel difference.
*   **Why it fails:** Visual illusions and distance effects make small pixel differences invisible to the naked eye.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do you have elements that look identical but represent different numbers?
*   **The Test:** Calculate the JND based on distance and intensity (using models like those in [@lu_modeling_2022]). If the data difference < JND, the design fails.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a specific text label to the items in question.
*   **Best Fix:** Add adaptive gridlines or "difference overlays" (brackets showing the delta) specifically for the indistinguishable pairs.
