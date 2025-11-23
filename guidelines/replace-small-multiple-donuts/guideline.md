---
id: replace-small-multiple-donuts
title: Unroll Small Multiple Donut Charts into Bars
bibliography: references.bib
description: Replace repeating donut charts with stacked bars to improve comparability
  across multiple entities.
labels:
- chart:donut
- chart:bar
- task:compare
- impact:clarity
- visual:shape
---

## The Rule <!-- role: advice -->
When visualizing part-to-whole data across many different entities (small multiples), do not use donut charts. Instead, "unroll" the donuts into stacked bar charts, ideally organized within a table structure.

## The Logic <!-- role: reason -->
Donut charts are visually repetitive when duplicated many times; they often "all look the same," making nuance hard to spot.
*   **The Principle:** Linear Comparison. Unrolling donuts into bars makes it easier to compare categories (e.g., "Good condition") both within a single entity and between different entities [@mintzer_donuts_into_bars_2025].
*   **The Evidence:** As noted by [@mintzer_donuts_into_bars_2025], changing donuts to bars allows for scanning horizontally (breakdown within one state) or vertically (comparing shares across states) on a 0-100 scale.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing shares or proportions across a large list of items (e.g., 50 U.S. States).
*   **Data Type:** Categorical part-to-whole data (e.g., percentages of Good/Fair/Poor) repeated for many categories.
*   **Audience:** General audiences who need to scan for outliers or specific values quickly.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Single Aggregate View.
*   **Reason:** If you are only showing *one* chart representing the total average of all data, a single donut chart may be acceptable for aesthetic variety, provided precise comparison isn't the primary goal.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "whimsical" or distinctive circular shape that some designers feel breaks up the monotony of text.
*   **The Risk:** Stacked bars can still be difficult to compare if the segments are not aligned to a common baseline (though 100% stacked bars mitigate this for the first and last segments).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding numerical labels inside every donut without changing the chart type.
*   **Why it fails:** It adds clutter without solving the visual comparison difficulty. The user still has to read numbers rather than rely on visual pattern recognition.

## How to Check <!-- role: check -->
*   **Visual Sign:** A grid of circles where the differences in arc lengths are difficult to distinguish at a glance.
*   **The Test:** Try to find the entity with the highest percentage of the middle category (e.g., "Fair condition"). If you have to read every number to find it, the chart type is failing.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Convert the radial projection (donut) to a linear projection (bar).
*   **Best Fix:** Place the stacked bars inside a table row, allowing the user to sort by specific categories (e.g., sort by "Poor condition").
