---
id: avoid-area-encodings-for-sorting-when-accuracy-matters
title: Avoid area-based encodings for sorting tasks
bibliography: references.bib
description: For sorting judgments, do not rely on area encodings such as bubbles,
  rectangles, or treemaps when accuracy is important.
labels:
- chart:treemap
- chart:scatter
- task:sort
- visual:area
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Do not use area encodings (e.g., circles, rectangles, treemap-like rectangles) to support sorting by magnitude when accuracy matters.

## The Logic <!-- role: reason -->

Area judgments introduce more error for proportional comparison than position-based judgments in the reported sort task ranking.

- **The Principle:** Area comparisons are less accurate for ordering than position-based comparisons.
- **The Evidence:** Area-based designs (E-8 center-aligned rectangles, E-9 treemap rectangles, E-7 circles) are ranked lowest for sort accuracy, below position, length, and angle designs in the study results [@heerCrowdsourcingGraphicalPerception2010]. This ordering is captured as actionable evidence in the collation [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Rank categories/items by size/value (sorting).
- **Data Type:** Quantitative values being compared across items.
- **Audience:** General audiences performing quick “visual judgments.”

## When to Break It <!-- role: exceptions -->

- **Scenario:** Sorting is not a core requirement (the chart is primarily for other purposes and only incidental ordering is needed).
- **Reason:** The evidence summarized here is explicitly about a sort task accuracy ranking; it does not claim area encodings are worst for all possible tasks [@heerCrowdsourcingGraphicalPerception2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose compact “space-filling” layouts that area charts/treemaps provide.
- **The Risk:** Switching away from area may require more screen space or a different layout.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a treemap or bubble chart and assuming users can accurately sort items by comparing areas.
- **Why it fails:** In the reported ranking, these area conditions are the bottom performers for sort accuracy [@heerCrowdsourcingGraphicalPerception2010], and this is preserved in the collation [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The only way to compare values is by judging filled area (circle size or rectangle area).
- **The Test:** Temporarily replace areas with a position-aligned bar chart; if ordering becomes noticeably easier, your original chart likely suffered from area-based comparison limits consistent with the low ranking [@heerCrowdsourcingGraphical2023; @heerCrowdsourcingGraphicalPerception2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide an accompanying ranked list or a bar chart view for ordering.
- **Best Fix:** Replace the area encoding with a position-aligned encoding (e.g., bars on a shared axis), which is top-ranked for sort accuracy in the study [@heerCrowdsourcingGraphicalPerception2010] and highlighted for recommendation use in [@zengReviewCollationGraphical2023].
