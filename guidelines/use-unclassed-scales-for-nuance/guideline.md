---
id: use-unclassed-scales-for-nuance
title: Use Unclassed Scales for Nuance and Patterns
bibliography: references.bib
description: Use continuous color scales to reveal subtle data variations, outliers,
  and smooth transitions across geography.
labels:
- visual:color
- impact:discovery
- task:explore
- data:quantitative
- chart:choropleth
---

## The Rule <!-- role: advice -->
Use an unclassed (continuous) color scale when you want to display the most truthful, nuanced view of the data, specifically to reveal general geographical patterns, outliers, and smooth transitions.

## The Logic <!-- role: reason -->
An unclassed map is the "most exact representation of the data model possible" because it does not artificially group numbers [@muth_classed_vs_unclassed_2021]. It allows readers to see subtle differences between neighboring regions and identify outliers that might otherwise be hidden inside a broad statistical bin. It answers the question "How does my region compare?" with higher fidelity.

## Where to Apply <!-- role: context -->
*   **User Goal:** Highlighting outliers (e.g., a region with slightly higher unemployment than its neighbors).
*   **User Goal:** Showing smooth geographic transitions (e.g., temperature gradients).
*   **User Goal:** Avoiding interpretation for the reader and letting them explore the data's complexity.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The map is intended for specific value retrieval.
*   **Reason:** Humans are poor at matching specific points on a gradient to a legend to extract exact numbers (e.g., "Is this 6.1% or 6.5%?").

## The Price <!-- role: costs -->
*   **The Sacrifice:** Readability of specific values. Readers can only make "good guesses" about the numbers.
*   **The Risk:** The map may look "noisy" or complex compared to a simplified classed map.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a classed map with very few classes (e.g., 2 classes) to show a trend.
*   **Why it fails:** This removes almost all nuance. The fewer classes you use, the less nuanced the map becomes [@muth_classed_vs_unclassed_2021].

## How to Check <!-- role: check -->
*   **The Test:** Look at a region that you know is an outlier or slightly different from its neighbors. If it shares the exact same color as its neighbors, your scale (likely classed) is hiding that nuance.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove the bins/steps to create a continuous gradient.
*   **Best Fix:** Use a continuous scale but ensure the interpolation (color ramp) is adjusted so distinct values are still visually differentiable.
