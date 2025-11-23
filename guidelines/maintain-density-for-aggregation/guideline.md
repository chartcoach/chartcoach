---
id: maintain-density-for-aggregation
title: Maintain High Point Density for Aggregation Tasks
bibliography: references.bib
description: Increasing the number of points in a scatterplot does not hinder the
  user's ability to estimate averages.
labels:
- chart:scatterplot
- task:aggregate
- data:density
- impact:fidelity
- complexity:intermediate
---

## The Rule <!-- role: advice -->
Do not aggressively sample down or simplify scatterplot data solely because you fear users cannot estimate averages in dense displays.

## The Logic <!-- role: reason -->
The human visual system is capable of extracting summary statistics (like mean position) from large sets of objects roughly as efficiently as from smaller sets (within reasonable limits).
*   **The Principle:** Ensemble Coding. The brain processes "sets" of items to extract summary statistics rapidly, independent of the individual item count.
*   **The Evidence:** Collated experimental results show no significant performance decrease when increasing point count per class from 50 (E-1) to 75 (E-3) [@zeng_review_2023]. The original study concluded that judgments are no harder when each set contains more points, and performance remains good or even improves with more data [@gleicher_perception_2013].

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating the general trend or average location of groups.
*   **Data Type:** Dense scatterplots (e.g., 50–100 points per category).
*   **Audience:** Analytical users looking for representative overviews.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Overplotting is so severe that points completely occlude one another (rendered as a solid block of color).
*   **Reason:** Visual aggregation requires perceiving the distribution of elements; total occlusion destroys the position signals needed for the brain to compute the average.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Rendering time may increase with more DOM elements or shapes.
*   **The Risk:** Visual clutter increases, which might affect *other* tasks like finding a specific outlier (though it does not hurt aggregation).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Filtering a dataset of 100 points down to 10 "representative" points to make the chart "cleaner."
*   **Why it fails:** It removes data fidelity without actually helping the user perceive the average, as they could have processed the full set effectively [@gleicher_perception_2013].

## How to Check <!-- role: check -->
*   **Visual Sign:** The chart looks sparse despite the dataset being large.
*   **The Test:** Check the data-ink ratio. If you are hiding data points that fit comfortably in the view, you are over-filtering.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the sample size limit in your visualization renderer.
*   **Best Fix:** Use smaller mark sizes or slight transparency to manage occlusion while maintaining the full point count for accurate ensemble perception.
