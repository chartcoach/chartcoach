---
id: use-a-bar-chart-instead-of-stacked-columns-for-one-total
title: Use a Bar Chart Instead of Stacked Columns When Showing One Total
bibliography: references.bib
description: For part-to-whole breakdowns of a single total, use a bar chart to use
  space efficiently and improve segment comparison.
labels:
- chart:bar
- task:part-to-whole
- visual:position
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
- source:datawrapper
---

## The Rule <!-- role: advice -->

If you’re showing parts of one total, use a bar chart instead of a stacked column chart.

## The Logic <!-- role: reason -->

With only one total, stacked columns waste horizontal space and make it harder to compare parts; a bar chart uses available space better and supports easier part-to-part comparison [@muth_stacked_columns_2018].

- **The Principle:** Choose the simplest layout that maximizes readable comparisons
- **The Evidence:** [@muth_stacked_columns_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand the composition of a single total and compare its parts
- **Data Type:** One whole split into multiple categories
- **Audience:** Readers who need quick comprehension [@muth_stacked_columns_2018]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You actually have multiple totals and need to compare those totals.
- **Reason:** Then stacked columns can be appropriate for showing totals plus a key baseline segment [@muth_stacked_columns_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose the “multiple totals” framing that stacked columns provide (which you don’t need for one total).
- **The Risk:** If you switch to a bar chart without rethinking labeling, small parts may still be hard to read [@muth_stacked_columns_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** For one total, still using stacked columns because the data is “part-to-whole.”
- **Why it fails:** The form suggests comparisons across multiple totals that don’t exist and reduces readability of parts [@muth_stacked_columns_2018].
- **The Wrong Fix:** Creating a chart when you only need to state one share.
- **Why it fails:** The chart adds little; the number may be better communicated as text [@muth_stacked_columns_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** A single narrow column with multiple segments and lots of unused horizontal space.
- **The Test:** Count totals: if it’s 1, default to a bar chart; if you’re communicating one share, consider using text instead [@muth_stacked_columns_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the stacked column with a bar chart using the same categories.
- **Best Fix:** If only one key number matters, remove the chart and write the number in text [@muth_stacked_columns_2018].
