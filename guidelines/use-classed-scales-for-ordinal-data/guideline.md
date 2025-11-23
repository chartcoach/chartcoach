---
id: use-classed-scales-for-ordinal-data
title: Use Classed Scales for Ordinal Data
bibliography: references.bib
description: Use discrete color steps (classed) for data that has distinct ranks or
  categories to avoid implying non-existent intermediate values.
labels:
- visual:color
- data:categorical
- data:ordinal
- impact:clarity
- chart:map
---

## The Rule <!-- role: advice -->
When visualizing ordinal data—such as Likert scales, clothing sizes, or official ranks—always use a classed (discrete) color scale rather than a continuous gradient.

## The Logic <!-- role: reason -->
A continuous (unclassed) color scale implies fluidity and the existence of values between points. If the data consists of distinct steps (e.g., "Agree" vs. "Strongly Agree," or size "S" vs. "M"), a gradient suggests that intermediate options exist when they do not [@muth_classed_vs_unclassed_2021]. A classed scale aligns the visual representation with the discrete nature of the data structure.

## Where to Apply <!-- role: context -->
*   **Data Type:** Ordinal data (ranked categories) like survey responses (Likert scales), clothing sizes, or star ratings.
*   **Data Type:** Integers representing ranks where decimals are impossible.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Continuous data that has been artificially binned.
*   **Reason:** While continuous data *can* be classed, it does not *have* to be. This rule specifically prohibits unclassed scales for naturally discrete ordinal data.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the smooth aesthetic of a gradient.
*   **The Risk:** If the categories are numerous (e.g., 20 different ranks), a classed scale may become visually cluttered or require too many distinct color steps to distinguish easily.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Applying a smooth gradient to a map of survey responses (e.g., "Agree" to "Disagree").
*   **Why it fails:** It implies a respondent could have selected a value mathematically halfway between "Neutral" and "Agree," which is often impossible in the survey design.

## How to Check <!-- role: check -->
*   **The Test:** Look at the legend. If the data points are text labels (XS, S, M) or integers (Rank 1, 2, 3) but the legend is a smooth fading bar, the rule is broken.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the color scale settings in your visualization tool from "continuous" or "linear" to "steps" or "classed."
*   **Best Fix:** Assign a specific, distinct color shade to each available category defined in the dataset.
