---
id: prefer-scatterplots-for-correlation-judgment-across-ranges
title: Prefer Scatterplots for Correlation Judgment
bibliography: references.bib
description: Use scatterplots when users need to judge correlation precisely across
  a range of correlation strengths.
labels:
- chart:scatter
- task:correlate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- metric:jnd
- source:zengReviewCollationGraphical2023
- source:harrisonRankingVisualizationsCorrelation2014
---

## The Rule <!-- role: advice -->

Prefer scatterplots (point marks with positionX and positionY encodings) when the user task is to judge correlation.

## The Logic <!-- role: reason -->

Scatterplots encode the two quantitative variables directly as 2D position, and the measured just-noticeable difference (JND) for correlation judgments is lower than several alternative visualization designs across tested correlation levels, indicating higher perceptual precision for correlation discrimination.

- **The Principle:** Lower JND implies higher discrimination precision for perceived correlation.
- **The Evidence:** The collated results summarize lower JND rankings for scatterplot designs compared with several non-scatterplot designs for the correlate task across multiple correlation-r values [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Discriminate which of two datasets appears more correlated (correlation judgment / correlate task).
- **Data Type:** Two quantitative variables where correlation strength varies (tested across multiple correlation-r levels, including both positive and negative).
- **Audience:** General audiences performing perception-based correlation comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your intended chart type is outside those compared or ranked in the reported JND results (i.e., you cannot map your design to the tested scatterplot-vs-other designs).
- **Reason:** This rule is only supported for the compared designs and correlation-judgment task as collated from the study; untested designs are not covered by this evidence [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose benefits of other chart forms (e.g., showing additional structure tied to ordering or category sequence) that are not part of the correlation-judgment objective.
- **The Risk:** If your analysis goal is not correlation judgment, optimizing for low JND on correlation may not optimize for the actual task [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using alternative designs (e.g., stacked/colored area-like or other composite encodings) to communicate correlation “because they look familiar.”
- **Why it fails:** The ranked JND results show these alternatives can yield worse perceptual precision for correlation discrimination than scatterplots under the correlate task [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate or disagree when asked which view is more correlated, especially when correlation levels are close.
- **The Test:** Run a quick A/B judgment test (two side-by-side views with nearby correlation strengths) and verify that users can reliably choose the more-correlated view more consistently with the scatterplot design than your alternative, aligning with lower-JND expectations [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a point-mark scatterplot with linear positionX/positionY encodings for the two quantitative fields.
- **Best Fix:** Use scatterplots as the default for correlation-judgment, and only offer alternative designs as secondary options when required by constraints outside the correlate task [@harrisonRankingVisualizationsCorrelation2014; @zengReviewCollationGraphical2023].
