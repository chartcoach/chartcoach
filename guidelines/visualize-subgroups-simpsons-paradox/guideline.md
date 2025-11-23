---
id: visualize-subgroups-simpsons-paradox
title: Visualize Subgroups to Detect Simpson's Paradox
bibliography: references.bib
description: Global trends can reverse within subgroups; visualize both levels.
labels:
- chart:scatter
- task:compare
- impact:validity
- data:multivariate
- audience:analyst
---

## The Rule <!-- role: advice -->
When analyzing aggregate trends, explicitly plot the data broken down by subgroups (categories/clusters). Do not assume the global trend applies to individual groups.

## The Logic <!-- role: reason -->
Simpson's Paradox occurs when a trend appears in individual groups but disappears or reverses when the groups are combined. It is possible to construct a dataset with a strong positive correlation overall ($r = +0.81$) that is composed entirely of subgroups with strong negative correlations. Visualizing the data color-coded by group reveals these conflicting internal structures immediately.
*   **The Principle:** Simpson's Paradox
*   **The Evidence:** [@matejka_same_2017]

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing performance across departments, regions, or experimental groups.
*   **Data Type:** Multivariate data involving a dependent variable, an independent variable, and a categorical grouping variable.
*   **Audience:** Decision-makers interpreting trends (e.g., "Sales are up overall, so all regions must be doing well").

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The grouping variable is irrelevant or noise.
*   **Reason:** Breaking data down by arbitrary categories (e.g., "Sales by Day of Week" when typical variance is seasonal) can create "spurious correlations" or noise.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The chart becomes more complex, requiring legends or interaction to distinguish groups.
*   **The Risk:** Viewers may become confused by the visual contradiction between the global slope (e.g., a regression line) and the local cluster slopes.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Plotting only the global regression line.
*   **Why it fails:** It hides the fact that the underlying mechanism for every single subgroup might be operating in the opposite direction of the global average.

## How to Check <!-- role: check -->
*   **Visual Sign:** A scatter plot with a single trend line, where the cloud of points seems to form distinct "clumps" or stripes that tilt against the main trend.
*   **The Test:** Color the points by category. If the "stripes" of color go down while the whole cloud goes up, you have Simpson's Paradox.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Color-code scatter plot points by category.
*   **Best Fix:** Plot "Small Multiples" (faceted charts) for each subgroup alongside the aggregate chart to make the reversal obvious.
