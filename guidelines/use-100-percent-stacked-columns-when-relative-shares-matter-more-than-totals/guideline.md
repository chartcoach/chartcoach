---
id: use-100-percent-stacked-columns-when-relative-shares-matter-more-than-totals
title: Use 100% Stacked Columns When Shares Matter More Than Totals
bibliography: references.bib
description: Normalize stacked columns to 100% when relative composition is the message
  and absolute totals are not important.
labels:
- chart:100-percent-stacked-column
- task:part-to-whole
- visual:position
- impact:clarity
- data:categorical
- audience:novice
- complexity:intermediate
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use 100% stacked column charts when relative shares are more important than absolute values and the totals are not of interest.

## The Logic <!-- role: reason -->

Normalizing all columns to the same height removes total differences and makes compositional differences the focus. It also creates a second consistent reference edge at the top, allowing a second important segment to be compared using that baseline [@muth_stacked_columns_2018].

- **The Principle:** Normalization focuses attention on composition; adds a second baseline
- **The Evidence:** [@muth_stacked_columns_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare proportions across categories without being distracted by different totals
- **Data Type:** Part-to-whole data where totals vary but aren’t meaningful for the question
- **Audience:** Readers who need a clear “share” story [@muth_stacked_columns_2018]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The size of the total is important context.
- **Reason:** 100% stacking hides absolute magnitude differences that readers may need [@muth_stacked_columns_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Absolute totals become invisible in the column heights.
- **The Risk:** Viewers may assume categories are comparable in size when they are not [@muth_stacked_columns_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using 100% stacked columns while still expecting readers to read absolute change.
- **Why it fails:** The chart encodes only proportions, not totals [@muth_stacked_columns_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** All columns are the same height, but the narrative still talks about “more/less in total.”
- **The Test:** If your headline or annotation mentions totals (e.g., “overall increased”), don’t use 100% stacking unless totals are shown elsewhere [@muth_stacked_columns_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Rewrite the framing to explicitly discuss shares (percentages) rather than totals.
- **Best Fix:** If totals matter, use a non-normalized stacked column chart (or another chart type) that preserves magnitude [@muth_stacked_columns_2018].
