---
id: bubble-chart-size-distance
title: Minimize Distance and Size Variation in Bubble Comparisons
bibliography: references.bib
description: In bubble charts, both distance and circle radius negatively impact the
  ability to compare values.
labels:
- chart:bubble
- chart:scatter
- task:compare
- visual:area
- visual:radius
- impact:precision
---

## The Rule <!-- role: advice -->
Avoid using bubble charts for precise comparisons, particularly when bubbles are large or far apart.

## The Logic <!-- role: reason -->
Bubble charts suffer from a compound perceptual penalty. The Just Noticeable Difference (JND) increases significantly based on *both* the object intensity (radius) and the separation distance. This makes them less accurate than bar charts (affected mainly by distance) or pie charts (affected mainly by intensity). Large bubbles separated by large distances are the most difficult to compare accurately.

*   **The Principle:** Compound JND Effects (Intensity + Distance)
*   **The Evidence:** [@lu_modeling_2022], collated by [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** visualizing three dimensions of data (x, y, and size).
*   **Data Type:** Multivariate quantitative data.
*   **Audience:** Exploratory analysis rather than precise reporting.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Showing general trends or clusters in data where exact size comparison is secondary to position.
*   **Reason:** The "bubble" aspect is often a secondary encoding (weight) rather than the primary comparison key.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to encode a third dimension on a 2D plane without using color (which has its own limitations).
*   **The Risk:** Users will fail to detect differences between values that are statistically distinct but perceptually indistinguishable due to layout.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Increasing the scale of all bubbles to make them "clearer."
*   **Why it fails:** Increasing the radius (intensity) actually increases the JND, making it *harder* to distinguish fine differences, not easier.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there bubbles of similar size located at opposite ends of the chart?
*   **The Test:** Select two bubbles of similar size. Ask a user which is larger without showing the data.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add text labels or interactive tooltips to display exact values.
*   **Best Fix:** If size comparison is critical, use a bar chart. If the spatial position is critical, map the third variable to color saturation or hue (though this also has precision limits), or use small multiples.
