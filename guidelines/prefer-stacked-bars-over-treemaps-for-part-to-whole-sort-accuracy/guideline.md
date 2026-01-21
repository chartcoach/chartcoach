---
id: prefer-stacked-bars-over-treemaps-for-part-to-whole-sort-accuracy
title: Prefer Stacked Bars Over Treemaps for Accurate Part-to-Whole Sorting
bibliography: references.bib
description: For part-to-whole sorting judgments, stacked bars produced higher accuracy
  than treemaps in an empirical comparison.
labels:
- chart:stacked-bar
- chart:treemap
- chart:pie
- task:sort
- visual:length
- visual:area
- data:categorical
- data:quantitative
- impact:accuracy
- audience:general
---

## The Rule <!-- role: advice -->

For part-to-whole **sort** judgments, use a **stacked bar chart** instead of a **treemap**.

## The Logic <!-- role: reason -->

- **The Principle:** In a part-to-whole setting, designs that support more accurate magnitude discrimination will reduce estimation error in ordering judgments.
- **The Evidence:** In a controlled experiment comparing five part-to-whole chart designs, the **stacked bar** condition ranked ahead of the **treemap** for accuracy on a sort task, with treemap performing worst among the compared designs [@kosaraImpactDistributionChart2019]. This finding is captured as an actionable recommendation in the collation dataset and review [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Sorting/ordering part-to-whole segments by size (e.g., “which category is larger?” in ranked/ordered comparisons).
- **Data Type:** Nominal categories forming a whole with quantitative percentages (part-to-whole).
- **Audience:** General audiences performing quick comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your design must be space-filling or must visually emphasize enclosure/tiling (a treemap-specific presentation need).
- **Reason:** This rule only speaks to accuracy for a part-to-whole sort task; it does not evaluate other objectives beyond that task [@kosaraImpactDistributionChart2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose the compact, space-filling layout treemaps provide.
- **The Risk:** If your categories are many or labels are long, stacked bars may become harder to label/read (not evaluated in this evidence).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching from a pie chart to a treemap assuming it is “more accurate by default.”
- **Why it fails:** In the tested part-to-whole sorting scenario, treemaps produced worse accuracy than the other tested designs, including the pie chart and stacked bar [@kosaraImpactDistributionChart2019; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Readers frequently mis-order segments or appear uncertain when comparing similarly sized rectangles.
- **The Test:** Ask a few users to rank the segments from largest to smallest; if they repeatedly mis-rank with the treemap, switch to stacked bars.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the treemap with a stacked bar while keeping the same category colors.
- **Best Fix:** Use a stacked bar specifically when the interaction/question is explicitly “sort/rank these parts,” reserving treemaps for other needs not covered by this evidence [@kosaraImpactDistributionChart2019; @zengReviewCollationGraphical2023].
