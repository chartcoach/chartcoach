---
id: prioritize-data-tables-for-value-retrieval
title: Prioritize Data Tables for Precise Value Retrieval
bibliography: references.bib
description: Tables outperform visualizations when the primary task is retrieving
  specific numerical values.
labels:
- chart:table
- chart:scatterplot
- chart:parallel-coordinates
- task:retrieve-value
- impact:accuracy
- impact:speed
---

## The Rule <!-- role: advice -->
If the user's primary task is to read or look up specific values for specific data points, use a Data Table rather than a Scatterplot or Parallel Coordinates Plot.

## The Logic <!-- role: reason -->
Visualizations require the user to map a geometric position back to an axis scale to estimate a value, a process prone to error and cognitive delay. Reading a number directly from a table eliminates this step. Knowledge collation by [@zeng_review_2023] highlights that in the experiments by [@kanjanabose_multi-task_2015], Data Tables resulted in the fastest response times for value retrieval tasks and were statistically equal to Parallel Coordinates in accuracy, while Scatterplots performed significantly worse.

*   **The Principle:** Direct Lookup vs. Visual Decoding.
*   **The Evidence:** [@kanjanabose_multi-task_2015]; [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Looking up exact metrics (e.g., "What was the exact revenue for Item X?").
*   **Data Type:** Quantitative data where precision is required.
*   **Audience:** Users performing audits, detailed reporting, or operational checks.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to find a value *relative* to the distribution (e.g., "Is this value high or low?").
*   **Reason:** While tables provide the *number*, they do not provide the *context*. Visualizations (SP/PCP) excel at showing where a value sits within the dataset range.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Pattern recognition. Tables obscure clusters, outliers, and correlations that are immediately visible in charts.
*   **The Risk:** Information overload. Tables are harder to scan for "gist" or summary information.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding tooltips to a chart to solve the "precise value" requirement while removing the table entirely.
*   **Why it fails:** Tooltips require interaction (hovering) and sequential search, which is slower than scanning a structured grid for a known identifier.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the user mousing over points one by one just to read the numbers?
*   **The Test:** Ask the user, "Find the exact value for Item ID #42." Measure how long it takes.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add labels directly to the data points in the chart (though this causes clutter).
*   **Best Fix:** Provide a companion Data Table alongside the visualization or allow a toggle to switch to a table view.
