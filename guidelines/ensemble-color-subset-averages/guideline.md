---
id: ensemble-color-subset-averages
title: Use Color to Support Subset Averaging
bibliography: references.bib
description: Use color hue to encode categories when users need to visually estimate
  the average value of a specific subgroup.
labels:
- chart:scatterplot
- task:aggregate
- visual:color
- impact:efficiency
- data:multivariate
- audience:analyst
---

## The Rule <!-- role: advice -->
Encode categorical data using distinct color hues when the user needs to visually estimate the average value (mean) of a specific subset of data points within a larger collection.

## The Logic <!-- role: reason -->
The human visual system utilizes "ensemble coding" to extract statistics from groups of objects in parallel. While spatial position is generally more precise for reading individual values, color allows the visual system to effectively "filter" or segment the scene. This filtering enables the viewer to compute the ensemble mean of just the "red" points or just the "blue" points without the interference caused by spatially overlapping distributions.
*   **The Principle:** Ensemble Coding and Feature Filtering
*   **The Evidence:** [@szafir_four_2016] as collated in [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the average performance of two different groups (e.g., "Is the red team averaging higher than the blue team?") within a dense distribution.
*   **Data Type:** Multivariate data with at least one quantitative axis and one nominal (categorical) attribute.
*   **Audience:** Users performing rapid visual aggregation or summary tasks rather than precise point reading.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to identify the precise value of individual outliers or specific data points.
*   **Reason:** Spatial position (e.g., a dot's location on an axis) is far more precise for retrieving specific values than color encoding, which is better for summary statistics [@szafir_four_2016].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose precision in reading individual values if you rely solely on color for the value encoding (though in a colored scatterplot, position is usually retained for the value itself, while color handles the grouping).
*   **The Risk:** If the colors chosen are not distinct enough, the "filtering" mechanism fails, and the ensemble calculation becomes inaccurate.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using different shapes (e.g., triangles vs. circles) to distinguish groups for averaging.
*   **Why it fails:** Shape is a weaker segmentation cue than color; it is much harder for the eye to "average the position of all triangles" than to "average the position of all red dots" [@szafir_four_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you immediately see the "cloud" of one category separate from another?
*   **The Test:** Ask a user to quickly point to the approximate center of mass for one specific category. If they have to scan serially, the encoding is failing.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the categorical encoding from shape to distinct color hues.
*   **Best Fix:** Ensure high perceptual distance between the color hues used for the categories to maximize the efficiency of the ensemble filtering.
