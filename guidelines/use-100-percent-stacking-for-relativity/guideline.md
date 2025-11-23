---
id: use-100-percent-stacking-for-relativity
title: Use 100% Stacking to Create a Top Baseline
bibliography: references.bib
description: Normalize stacks to 100% when relative shares matter more than absolute
  totals, creating a second baseline at the top.
labels:
- chart:stacked-column
- task:part-to-whole
- visual:scale
- impact:clarity
---

## The Rule <!-- role: advice -->
If the relative size of parts is more important than absolute totals, normalize the columns to 100% and place the second most important category at the very top.

## The Logic <!-- role: reason -->
Standard stacked column charts only offer one baseline (the bottom). By stacking percentages so every total equals 100%, you gain a second baseline at the top of the chart. This allows the reader to easily compare the category placed at the top, in addition to the category anchored at the bottom [@muth_stacked_columns_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the *share* or *ratio* of categories rather than raw counts.
*   **Data Type:** Part-to-whole data where the aggregate total is irrelevant or distracting.
*   **Chart Type:** 100% Stacked Column Chart.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The absolute totals vary significantly and that variation is crucial context.
*   **Reason:** Making all columns the same height (100%) hides the fact that one group might be vastly larger than another.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to see the absolute magnitude of the data.
*   **The Risk:** A reader might think a 50% share in a small column is equivalent in volume to a 50% share in a massive column.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a standard stacked column chart when totals are irrelevant.
*   **Why it fails:** The varying heights of the columns distract the eye from comparing the internal proportions.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the tops of your columns align perfectly in a straight line?
*   **The Test:** Ask, "Does the reader need to know that Column A is totally larger than Column B?" If no, use 100% stacking.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the chart axis setting to "Stack to 100%".
*   **Best Fix:** Place the primary category at the bottom and the secondary priority category at the top to maximize the utility of both baselines.
