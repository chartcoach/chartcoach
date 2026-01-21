---
id: prefer-pie-over-plain-stacked-bar-for-part-to-whole-estimation
title: Prefer a Pie Chart Over a Plain Stacked Bar for Part-to-Whole Estimation
bibliography: references.bib
description: "For estimating a part\u2019s percentage of a whole, a basic pie chart\
  \ produced lower error than a basic stacked bar in the tested condition."
labels:
- chart:pie
- chart:stacked-bar
- task:estimate
- visual:angle
- visual:length
- impact:accuracy
- data:part-to-whole
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When the goal is to estimate a part’s percentage of a whole, use a pie chart instead of a plain stacked bar.

## The Logic <!-- role: reason -->

Using a pie chart (angle-based encoding) can yield lower estimation error than using a plain stacked bar (length-based encoding) for this part-to-whole judgment task.

- **The Principle:** Lower estimation error via the tested encoding choice (angle vs. length) in part-to-whole judgments.
- **The Evidence:** The structured collation reports pie (E-2) ranked above baseline bar (E-1) with a significant difference for the characterized-distribution task in this study [@redmondVisualCuesEstimation2019], as collated in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating the value of the highlighted segment (1–100%) in a two-part, part-to-whole chart.
- **Data Type:** Part-to-whole proportion (quantitative percentage) with two segments.
- **Audience:** General users (crowdsourced participants).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need the additional accuracy benefit of an explicit quantitative scale on the bar (i.e., you are willing/able to show a scaled bar variant).
- **Reason:** In the same paper, a bar-with-scale condition outperformed the plain bar (and is ranked above it) in the tested comparisons [@redmondVisualCuesEstimation2019], as collated by [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You forgo a linear axis/scale presentation typical of bars.
- **The Risk:** If your design environment or style guide requires consistent axis-based charts, switching to a pie may reduce visual consistency.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the plain stacked bar and assuming viewers will estimate accurately without additional support.
- **Why it fails:** In the reported results, the plain bar was significantly worse than the pie for the same estimation task [@redmondVisualCuesEstimation2019], as summarized in [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers hesitate or give widely varying estimates for the same segment size.
- **The Test:** Run a quick internal check with a few representative segment sizes and compare mean absolute error for your current bar vs. a pie alternative (the study used mean absolute error) [@redmondVisualCuesEstimation2019]; the collation shows pie should win over baseline bar in this scenario [@zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the plain stacked bar with a pie chart for the part-to-whole estimate view.
- **Best Fix:** If you must stay with bars, switch to a scaled bar variant (see separate guideline on adding a scale) [@redmondVisualCuesEstimation2019; @zengReviewCollationGraphical2023].
