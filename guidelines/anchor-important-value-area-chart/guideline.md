---
id: anchor-important-value-area-chart
title: Place the Most Important Value at the Bottom
bibliography: references.bib
description: Anchor the most critical data series to the bottom baseline to ensure
  readability.
labels:
- chart:area
- visual:position
- visual:color
- task:compare
- impact:readability
---

## The Rule <!-- role: advice -->
Arrange your data so the most important value is at the bottom of the area chart and use color to make it stand out.

## The Logic <!-- role: reason -->
In a stacked area chart, only the bottom layer has a straight baseline (the x-axis). All upper layers "float" on top of others, making it difficult for the eye to judge their true size or trend.
*   **The Principle:** Common Baseline Comparison.
*   **The Evidence:** [@muth_area_charts_2018] states that readers can compare values easier with each other if they have the same baseline.

## Where to Apply <!-- role: context -->
*   **User Goal:** Emphasizing a specific category within a whole.
*   **Data Type:** Stacked time-series data.
*   **Audience:** Audiences who need to track a primary metric accurately while still seeing context.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Natural ordering required.
*   **Reason:** If the data has a strict ordinal hierarchy (e.g., "Low," "Medium," "High" scores), changing the order to put the "important" one at the bottom might confuse the logical structure.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Flexibility in ordering.
*   **The Risk:** You can only prioritize one variable perfectly. Secondary variables will still suffer from the "wandering baseline" effect.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Alphabetical sorting.
*   **Why it fails:** Arbitrary sorting usually buries the most critical insights in the middle of the stack where they are hardest to read.

## How to Check <!-- role: check -->
*   **Visual Sign:** The most highlighted or discussed category is floating in the middle of the chart.
*   **The Test:** Look at the layer you care about most. Is its bottom edge flat? If not, move it down.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reorder the data series in your tool so the key category is first (or last, depending on how the tool stacks).
*   **Best Fix:** Move the key category to the bottom and assign it a distinct, high-contrast color compared to the other layers.
