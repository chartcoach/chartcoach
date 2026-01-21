---
id: stack-only-the-parts-of-the-total-and-never-include-the-total-as-a-segment
title: Stack Only Parts of the Total and Never Include the Total
bibliography: references.bib
description: In stacked columns, include every component category that sums to the
  total, but do not add the total itself as another stacked segment.
labels:
- chart:stacked-column
- task:part-to-whole
- visual:position
- impact:integrity
- data:categorical
- audience:novice
- complexity:basic
- source:datawrapper
---

## The Rule <!-- role: advice -->

Include all and only the parts that sum to the total in a stacked column chart—never include the total itself as an additional stack segment.

## The Logic <!-- role: reason -->

Stacked columns are a part-to-whole display; adding the total as another segment double-counts and breaks the meaning of the stack as “components that sum to the whole” [@muth_stacked_columns_2018].

- **The Principle:** Part-to-whole consistency (no double counting)
- **The Evidence:** [@muth_stacked_columns_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand how components add up to totals
- **Data Type:** Data where categories are mutually exclusive parts of a whole for each column
- **Audience:** Any audience; especially those who may not check arithmetic carefully [@muth_stacked_columns_2018]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your “parts” are not actually components of a whole (they overlap or don’t sum).
- **Reason:** Then a stacked column chart is the wrong chart type for the data structure [@muth_stacked_columns_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to restructure your data to cleanly define mutually exclusive parts.
- **The Risk:** If parts are missing, the stack suggests completeness when it’s not true [@muth_stacked_columns_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding a “Total” row/series into the stack to “help readers.”
- **Why it fails:** It duplicates the information the full column height already represents and corrupts the sums [@muth_stacked_columns_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** A segment labeled “Total” appears inside the stack.
- **The Test:** For each column, verify: (sum of segments) = total; and ensure “total” is not itself one of the segments [@muth_stacked_columns_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove the total series from the stack; keep only components.
- **Best Fix:** If you need totals explicitly, label the top of each column or annotate totals separately rather than stacking them [@muth_stacked_columns_2018].
