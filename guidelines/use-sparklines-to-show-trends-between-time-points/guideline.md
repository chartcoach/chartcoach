---
id: use-sparklines-to-show-trends-between-time-points
title: Add Sparklines to Show In-Between Development
bibliography: references.bib
description: Use sparklines to show trends over time inside tables when two or three
  time points would hide the development between them.
labels:
- chart:table
- task:trend
- visual:position
- impact:clarity
- data:temporal
- audience:general
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When a table would otherwise show only a few time points, add sparklines to show the development in-between; do not treat sparklines as directly comparable across rows unless you use a consistent y-axis range.

## The Logic <!-- role: reason -->

Sparklines compactly communicate trend direction and shape between endpoints, but their default per-row y-axis scaling means they communicate general trends rather than comparable magnitudes across entities. This constraint is explicitly noted in [@muth_tables_2019].

- **The Principle:** Trend cueing under constrained space (with scaling caveats)
- **The Evidence:** [@muth_tables_2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding how values evolved between two reported time points
- **Data Type:** Temporal series per row (mini time series for many entities)
- **Audience:** Readers who need a quick sense of direction/change without leaving the table [@muth_tables_2019]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Cross-row comparability of magnitude is essential
- **Reason:** With different y-axis ranges per sparkline, rows are not comparable; [@muth_tables_2019] recommends a line chart if consistent scaling is important

## The Price <!-- role: costs -->

- **The Sacrifice:** Column width and design simplicity
- **The Risk:** Readers may incorrectly compare sparkline heights across rows when axes differ [@muth_tables_2019]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using sparklines to imply precise cross-entity comparisons
- **Why it fails:** The default varying y-axis ranges mean only general trends are shown, not comparable magnitudes [@muth_tables_2019]

## How to Check <!-- role: check -->

- **Visual Sign:** Readers could plausibly compare sparkline heights across rows to judge “who is higher”
- **The Test:** Verify whether sparklines share a consistent y-axis range; if not, treat them as trend-only cues [@muth_tables_2019]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add context in the table design by relying on sparklines only for direction/trend and keeping the numbers for magnitude [@muth_tables_2019]
- **Best Fix:** If consistent y-axis range is required for comparability, use a line chart instead of (or in addition to) sparklines in the table [@muth_tables_2019]
