---
id: avoid-bars-for-unequal-sample-sizes
title: Avoid Bar Charts for Averages with Unequal Sample Sizes
bibliography: references.bib
description: Bar charts cause bias when comparing averages of groups with different
  counts, as users conflate total area with average value.
labels:
- chart:bar
- data:statistical
- task:compare
- impact:bias
- visual:area
---

## The Rule <!-- role: advice -->
Never use bar charts to display individual data points for comparison if the groups have different sample sizes (e.g., comparing the average of 6 items vs. 10 items).

## The Logic <!-- role: reason -->
The visual system struggles to ignore the "weight" of the ink used in bar charts.
*   **The Principle:** The "Summed Area" Proxy. When users look for an average in a bar chart, they use the total summed area of the bars as a shortcut. If one group has more items (larger N), it has more bars and more total area. This acts as an "incongruent signal" if the group with more items actually has a lower average.
*   **The Evidence:** In experiments where one group had 6 items and the other had 10, performance on bar charts dropped drastically compared to dot plots. Users were biased toward selecting the group with more items (more area) as having the higher average, even when it didn't [@yuan_perceptual_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing averages or general trends between two distinct groups.
*   **Data Type:** Discrete data sets where $N$ (count) varies between groups (e.g., average salary of 100 men vs. 12 women).
*   **Audience:** Analysis requiring statistical accuracy without bias.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The sample sizes are identical.
*   **Reason:** If both groups have the same number of bars, the "summed area" correlates perfectly with the "average height," so the visual bias does not result in a mathematical error (though precision is still lower than dot plots) [@yuan_perceptual_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the visual "heft" of bars which can make data feel substantial.
*   **The Risk:** You must explicitly explain that the density/count of points does not determine the average value in the alternative visualization.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Reducing the width of bars in the larger group to equalize total ink.
*   **Why it fails:** This introduces a new variable (width) that implies a different data meaning or uncertainty, confusing the reader further.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there more bars in one cluster than the other?
*   **The Test:** If the group with *more* bars has a *lower* average height, does it still look "bigger" or "more important" at a glance? If yes, the chart is misleading.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch to a Dot Plot. Dot plots are significantly less impaired by differences in set size because users can estimate the centroid (center of mass) regardless of the number of points.
*   **Best Fix:** Use a summary mark (like a single point for the mean with error bars) rather than showing the raw data bars, or use a Dot Plot if showing the distribution is necessary.
