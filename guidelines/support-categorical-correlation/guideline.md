---
id: support-categorical-correlation
title: Support Correlation of Categorical Attributes
bibliography: references.bib
description: Enable users to find associations and coincidences in non-numeric data.
labels:
- task:correlate
- data:categorical
- data:nominal
- impact:insight
---

## The Rule <!-- role: advice -->
Design correlation tools that accept non-numeric attributes to help users identify associations, coincidences, and category-based predictions.

## The Logic <!-- role: reason -->
Users frequently desire to "correlate" non-numeric attributes (e.g., "Does country of origin correlate with MPG?"). While statistically this refers to predictive models or coincidences rather than mathematical correlation, users frame these inquiries as correlation tasks. Systems must support determining relationships between values regardless of whether the variables are purely numeric [@amar_low-level_2005].

## Where to Apply <!-- role: context -->
*   **User Goal:** Discovering if membership in one category predicts values in another (e.g., "Do comedies win more awards?").
*   **Data Type:** Datasets with rich nominal or categorical data (e.g., film genres, car origins, brand names).
*   **Audience:** General users who use the term "correlation" broadly to mean "relationship."

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Strict statistical analysis requiring Pearson/Spearman coefficients.
*   **Reason:** Categorical associations cannot be measured with the same mathematical tools as numeric linear relationships.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Complexity in visualization logic (e.g., switching from scatterplots to mosaic plots or heatmaps depending on data type).
*   **The Risk:** Users might infer a causal or mathematical relationship where only a weak association exists.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Disabling "correlation" or "relationship" features whenever a non-numeric column is selected.
*   **Why it fails:** It blocks a valid analytic inquiry simply because the statistical definition of correlation doesn't strictly apply.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are scatterplots or relationship views disabled for text columns?
*   **The Test:** Select a categorical column (e.g., "Genre") and a numeric column (e.g., "Revenue"). Can the tool show the relationship?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Allow categorical axes in standard charts (e.g., box plots per category).
*   **Best Fix:** Implement visual techniques specifically for categorical relationships, such as highlighting coincidences or using small multiples.
