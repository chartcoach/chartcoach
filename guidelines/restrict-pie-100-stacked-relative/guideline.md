---
id: restrict-pie-100-stacked-relative
title: Use Pie and 100% Stacked Charts Only for Relative Values
bibliography: references.bib
description: Limit the use of Pie Charts and 100% Stacked Bar Charts to tasks involving
  relative comparisons, not absolute value retrieval.
labels:
- chart:pie
- chart:stacked-bar
- task:compare
- data:part-to-whole
- audience:general
---

## The Rule <!-- role: advice -->
Do not use Pie Charts or 100% Stacked Bar Charts if the user needs to retrieve absolute values (e.g., "What was the exact sales revenue?"). Use them only for relative value tasks (e.g., ratios, percentages, proportions).

## The Logic <!-- role: reason -->
These chart types visually encode proportion, not magnitude.
*   **The Principle:** **Visual Encoding Limits.** In the VLAT Test Blueprint, specific visualizations are categorized by the tasks they support. Pie Charts and 100% Stacked Bar Charts are explicitly marked as supporting "Only Relative Value" tasks.
*   **The Evidence:** Table 1 in [@lee_vlat_2017] classifies the "Dataset Type" for these charts as "One quantitative attribute... Only Relative Value." The authors acknowledge that while users utilize visual objects, in these specific charts, they "only represent the transformed values of absolute values."

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing parts to a whole, or comparing ratios between categories.
*   **Data Type:** Categorical data with a quantitative attribute that sums to a meaningful whole.
*   **Audience:** Users needing to understand composition rather than volume.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Annotating with Absolute Values.
*   **Reason:** If you directly label the slices or segments with the absolute numbers (e.g., "500 units"), the user can technically "retrieve" the value by reading the text, even if the visual shape doesn't encode it.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision regarding the total size or magnitude. A pie chart of a million dollars looks identical to a pie chart of ten dollars if the proportions are the same.
*   **The Risk:** Users might assume a larger segment implies a larger absolute number compared to a segment in a different chart, which may not be true if the totals differ.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Asking users to compare the total size of two different pie charts.
*   **Why it fails:** The radius/area of pie charts is difficult to compare accurately to determine total magnitude.
*   **The Wrong Fix:** Using a 100% Stacked Bar to show growth over time.
*   **Why it fails:** It obscures the fact that the total market size might be shrinking even if a specific segment's percentage is growing.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the axis scale go from 0% to 100%? If yes, you cannot ask "How many widgets were sold?"
*   **The Test:** Look at the chart without data labels. Can you tell if the total dataset size is 100 or 1,000,000? If no, the chart does not support absolute value retrieval.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add data labels showing the absolute values directly on the segments.
*   **Best Fix:** If absolute values are important, switch to a standard Stacked Bar Chart (which shows total magnitude) or a Side-by-Side Bar Chart.
