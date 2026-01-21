---
id: use-position-position-scatterplots-to-assess-bivariate-correlation
title: "Use Position\u2013Position Scatterplots to Judge Bivariate Correlation"
bibliography: references.bib
description: For correlation estimation tasks, use scatterplots with x/y position
  encodings to achieve higher precision than alternative chart types.
labels:
- chart:scatter
- task:correlate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- metric:jnd
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use a scatterplot with quantitative values encoded by position on both axes (x and y) when users need to judge correlation.

## The Logic <!-- role: reason -->

- **The Principle:** Position–position encodings support more precise perception for correlation judgments than the other tested visualization types.
- **The Evidence:** In the collated correlate task results, the scatterplot design(s) rank in the top group for JND-based precision (lower JND is better) and outperform the remaining designs in pairwise significance comparisons [@kayWebersLawSecond2016]. This guideline is derived from the structured collation of the finding [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating or comparing the strength of correlation between two quantitative variables.
- **Data Type:** Two quantitative attributes where correlation is meaningful (positive or negative).
- **Audience:** General audiences where consistent performance matters.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user’s primary goal is not correlation judgment (e.g., category composition or time-series trend reading).
- **Reason:** This guideline only covers the correlate task evidence; it does not claim superiority for other tasks [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose the ability to emphasize categories or stacked composition if those are also important.
- **The Risk:** If the task shifts away from correlation, a scatterplot may not match the user’s intent as well as other encodings.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using stacked or area-based chart designs to “show correlation” without a position–position mapping.
- **Why it fails:** Those designs are ranked lower for correlation precision (higher JND) than the position–position scatterplot group in the extracted results [@kayWebersLawSecond2016; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users struggle to tell which of two displays is “more correlated,” or require large changes in correlation to notice differences.
- **The Test:** Ask viewers to choose which of two views is more correlated; if they need very large differences to answer confidently, you likely aren’t using the top-ranked approach for this task [@kayWebersLawSecond2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a scatterplot mapping the two quantitative variables to x and y position.
- **Best Fix:** Use the position–position scatterplot as the primary view for correlation judgment and move other encodings (e.g., stacked/area forms) to secondary views if needed [@kayWebersLawSecond2016; @zengReviewCollationGraphical2023].
