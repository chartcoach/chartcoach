---
id: order-line-charts-correlation
title: Sort Line Charts to Improve Correlation Perception
bibliography: references.bib
description: Ordering line charts by the X-axis variable significantly improves the
  perception of correlation compared to standard line charts.
labels:
- chart:line
- task:correlation
- task:sort
- visual:order
- impact:rank
---

## The Rule <!-- role: advice -->
If you must use a line chart to depict correlation, order the data along the X-axis based on the variable's magnitude (an "Ordered Line Chart").

## The Logic <!-- role: reason -->
Standard line charts often obscure correlation due to visual noise (spikes). Sorting the data transforms the visualization into a monotonic curve where deviations (correlation strength) are easier to judge.
*   **The Principle:** **Perceptual Simplification.** An ordered line chart explicitly maps the variable order, making it perform symmetrically for positive and negative correlations and significantly reducing the Just-Noticeable Difference (JND) compared to unordered line charts [@harrison_ranking_2014].
*   **The Evidence:** In the study's ranking, "Ordered Line" charts significantly outperformed standard line charts and radar charts. They were the only chart besides scatterplots to show symmetric performance for positive and negative correlations [@harrison_ranking_2014].

## Where to Apply <!-- role: context -->
*   **User Goal:** Showing the relationship between variables when a scatterplot is not an option.
*   **Data Type:** Bivariate quantitative data.
*   **Audience:** Audiences who might find scatterplots too abstract (though scatterplots remain superior).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Time-series data.
*   **Reason:** You generally cannot reorder time. If the X-axis is time, you are stuck with a standard line chart (which performs poorly for correlation) or must switch to a scatterplot.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the context of the original index (e.g., if the data was originally ordered by ID or time, that context is destroyed by sorting).
*   **The Risk:** Users might confuse the sorted axis for a time axis if not clearly labeled.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a Radar chart to show correlation.
*   **Why it fails:** While Radar charts performed better than standard line charts in the study, they were still outperformed by Ordered Line charts and Scatterplots [@harrison_ranking_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the line chart jagged and spiky?
*   **The Test:** Sort the data by the X-variable. Does the line become a smooth curve (sigmoid-like)? If so, the correlation is easier to read.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Sort the dataset by the dimension mapped to the horizontal axis.
*   **Best Fix:** Use a scatterplot, which uses position rather than line connectivity to show the relationship.
