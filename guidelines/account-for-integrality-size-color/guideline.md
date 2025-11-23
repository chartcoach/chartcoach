---
id: account-for-integrality-size-color
title: Account for Integrality When Mixing Size and Color
bibliography: references.bib
description: Size and color are perceptually integral; large differences in one can
  mask differences in the other.
labels:
- visual:size
- visual:color
- chart:bubble
- chart:scatter
- task:compare
- impact:readability
- complexity:advanced
---

## The Rule <!-- role: advice -->
When encoding data using both **Size** and **Color** on the same marks, treat them as interfering (integral) dimensions. Ensure that differences in one channel (e.g., Size) are not so dominant that they flatten the perception of the other (e.g., Color).

## The Logic <!-- role: reason -->
Visual dimensions are not always processed independently. While Shape and Color are "separable" (perceived effectively via a city-block metric), Size and Color show "integrality" (interacting in a Euclidean-like metric). Large distances in one variable can dominate the perceptual space.
*   **The Principle:** Dimensional Integrality
*   **The Evidence:** [@demiralp_learning_2014] found that for Size-Color combinations, the perceptual distance is best modeled where interactions occur ($n$ value intermediate between 1 and 2). Large differences in one variable dominated smaller distances in the other, distorting the perceived structure.

## Where to Apply <!-- role: context -->
*   **User Goal:** Evaluating multidimensional data points (e.g., a bubble chart where radius = population and hue = region).
*   **Data Type:** Bivariate quantitative or categorical data.
*   **Audience:** General viewers who might focus on the most salient feature.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Shape and Color combinations.
*   **Reason:** [@demiralp_learning_2014] indicate that Shape and Color are largely **separable**. You can treat them as independent channels with less concern for perceptual interference compared to Size and Color.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may need to reduce the dynamic range of your size encoding to ensure color differences remain noticeable.
*   **The Risk:** If you do not balance them, users may perceive two data points as "very different" solely because of size, missing a crucial color difference.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Maximizing the range of both variables independently.
*   **Why it fails:** This ignores the interaction effects. A massive size difference will perceptually "swallow" the color encoding.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the largest bubbles in your chart look like they belong to a different group than the smallest bubbles of the same color?
*   **The Test:** Use visual embedding or MDS to map the perceived distances. If the structure of the data (e.g., color clusters) is lost in the projection because size is pulling them apart, the encoding is unbalanced.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reduce the maximum size of your elements to prevent size from dominating the visual field.
*   **Best Fix:** Use a "weighted power model" to predict perceptual distances and adjust the scaling parameters ($b_1$ and $b_2$) of your visual variables to ensure both contribute appropriately to the overall perceived difference [@demiralp_learning_2014].
