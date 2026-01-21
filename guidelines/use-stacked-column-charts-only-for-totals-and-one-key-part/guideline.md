---
id: use-stacked-column-charts-only-for-totals-and-one-key-part
title: Use Stacked Column Charts Only to Compare Totals and One Key Segment
bibliography: references.bib
description: Use stacked column charts when the main task is comparing overall totals
  and a single important segment that can share a common baseline.
labels:
- chart:stacked-column
- task:compare
- visual:position
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use a stacked column chart only when your primary message is comparing the totals and (at most) one important part of those totals.

## The Logic <!-- role: reason -->

Stacked column charts make most segments hard to compare because only the bottom segment shares a consistent baseline; segments floating above it start at different heights, which slows and degrades comparisons [@muth_stacked_columns_2018].

- **The Principle:** Shared baseline supports easier comparison
- **The Evidence:** [@muth_stacked_columns_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare overall totals and one highlighted component across categories
- **Data Type:** Part-to-whole data across a small set of categories (each total split into parts)
- **Audience:** General readers who need quick, accurate takeaways [@muth_stacked_columns_2018]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need to compare multiple parts across all totals (e.g., how every segment changes across categories)
- **Reason:** Most segments don’t share a baseline, so cross-category comparison becomes unreliable; use split bars or small multiples instead [@muth_stacked_columns_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose easy comparability for all but the baseline segment (and sometimes the top edge).
- **The Risk:** Readers focus on totals and miss important differences between non-baseline segments [@muth_stacked_columns_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using stacked columns to compare many segments across categories.
- **Why it fails:** Floating segment baselines vary, making differences hard to see and easy to misread [@muth_stacked_columns_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Readers must “trace” segment bottoms across columns to compare them.
- **The Test:** Ask: “Can I compare the segment of interest across columns without mentally aligning baselines?” If not, the chart type is wrong [@muth_stacked_columns_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reframe the message to focus on totals and one segment; make that segment the baseline segment.
- **Best Fix:** Switch to split bars or small multiples if multiple segments must be compared across totals [@muth_stacked_columns_2018].
