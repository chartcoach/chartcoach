---
id: support-derived-values
title: Enable On-the-Fly Aggregation
bibliography: references.bib
description: Allow users to create and visualize aggregate data points that do not
  exist in the raw dataset.
labels:
- task:aggregate
- task:compare
- data:categorical
- impact:insight
- task:compute-derived-value
---

## The Rule <!-- role: advice -->
Provide mechanisms for users to compute and visualize derived aggregate values (such as averages, counts, or sums) that are not explicitly present in the raw data cases.

## The Logic <!-- role: reason -->
Users frequently ask questions that compare categories (e.g., "Which cars are more fuel-efficient: Japanese or American?") without the dataset containing those specific pre-calculated group averages. To answer these questions, the user must compute a numeric representation for a set of data cases. This "Compute Derived Value" task is a fundamental analytic primitive distinct from simply retrieving existing values [@amar_low-level_2005].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing groups or categories (e.g., comparing performance by manufacturer).
*   **Data Type:** Atomic data rows where the user is interested in group properties (e.g., a list of individual sales transactions).
*   **Audience:** Analysts performing exploratory data analysis who need to generate insights beyond row-level data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset is already fully pre-aggregated (e.g., a summary table).
*   **Reason:** Further aggregation may be mathematically invalid (e.g., averaging averages) or unnecessary.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Requires more complex interface controls (e.g., formula builders or "group by" operations) than a simple data viewer.
*   **The Risk:** Users may select inappropriate aggregation functions (e.g., summing values that should be averaged).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Forcing users to export data to a spreadsheet to calculate simple averages or counts.
*   **Why it fails:** It breaks the analytic flow and removes the data from the visualization context.

## How to Check <!-- role: check -->
*   **Visual Sign:** Can I answer "What is the average [Attribute A] for [Category B]?" without leaving the visualization?
*   **The Test:** Try to answer a comparison question about a category that doesn't have its own row in the data table.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a simple summary row or tooltip showing averages/counts for selected items.
*   **Best Fix:** Implement dynamic aggregation features that allow users to group data by attribute and visualize the resulting derived values.
