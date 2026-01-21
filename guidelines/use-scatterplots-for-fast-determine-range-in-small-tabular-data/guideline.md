---
id: use-scatterplots-for-fast-determine-range-in-small-tabular-data
title: Use Scatterplots When Determine-Range Speed Matters Most
bibliography: references.bib
description: For determine-range tasks in small datasets, scatterplots were fastest
  in the experiment, even though accuracy differences were not significant.
labels:
- chart:scatter
- task:determine-range
- visual:position
- impact:speed
- data:quantitative
- audience:general-public
- source:empirical
---

## The Rule <!-- role: advice -->

If speed is the dominant objective for determine-range tasks, use a scatterplot.

## The Logic <!-- role: reason -->

- **The Principle:** Range judgments can be sped up by quickly locating min/max positions in a spatial field.
- **The Evidence:** For **determine-range**, scatterplot designs ranked fastest by time among the tested visualization types [@saketTaskBasedEffectivenessBasic2019]. This task-by-metric evidence is part of the collated dataset for recommendation work [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly identify the span of values (range).
- **Data Type:** Small datasets shown with point marks (5–34 marks).
- **Audience:** General public / mixed-expertise users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users must communicate the range precisely and unambiguously (e.g., exact numeric endpoints).
- **Reason:** The speed ranking does not imply best support for exact numeric reporting; tables may better support exact value extraction, but this guideline only claims the time advantage observed in the study [@saketTaskBasedEffectivenessBasic2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Users may still need to estimate exact endpoints without textual values.
- **The Risk:** Dense points or overlapping marks can obscure true minima/maxima.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a pie chart for “range” because it looks like it shows a spread.
- **Why it fails:** In the study’s determine-range timing results, pie designs were slower than scatterplot designs [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users scan for extremes along axes rather than reading many labels.
- **The Test:** Time users on a range question; if they spend time reading values rather than spotting extremes, try a scatterplot for faster range judgments (per the study’s time ranking) [@saketTaskBasedEffectivenessBasic2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use a scatterplot with clear axes and enough separation between points to identify extremes quickly.
- **Best Fix:** Use scatterplot as the primary view for determine-range when speed is paramount, and supplement with exact values only if needed (consistent with the experiment’s time results) [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].
