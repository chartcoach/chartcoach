---
id: use-line-or-scatter-not-area-for-trend-estimation
title: Use Line or Scatter Plots Instead of Area Charts for Trend Estimation
bibliography: references.bib
description: For visually estimating bivariate trends, prefer line graphs or scatterplots
  over area charts to improve accuracy.
labels:
- chart:line
- chart:scatter
- chart:area
- task:correlate
- visual:position
- visual:area
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When people must visually estimate a trend in bivariate data, use a line chart or a scatterplot—not an area chart.

## The Logic <!-- role: reason -->

Line charts and scatterplots encode values primarily with position, while area charts add a filled region that changes what viewers perceive as the “signal,” reducing trend-estimation accuracy.

- **The Principle:** Encoding choice affects the accuracy of visual trend inference.
- **The Evidence:** In an experimental ranking for the correlate task, line and scatter designs (E-2 and E-1) were grouped as more accurate than the area design (E-3), and both E-2 > E-3 and E-1 > E-3 were significant [@correllRegressionEyeEstimating2017]. This extracted ranking is collated for visualization recommendation in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating the direction/strength of a trend by eye (a correlate-style task).
- **Data Type:** Two fields where Y is quantitative and X is ordered (ordinal axis), shown with position encodings.
- **Audience:** General audiences or mixed-expertise viewers who will infer trends directly from the plot.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not asking viewers to estimate trends (e.g., you need to emphasize magnitude as filled area or show cumulative quantity).
- **Reason:** The evidence only supports the preference for line/scatter over area specifically for the correlate (trend estimation) task, not for other objectives [@correllRegressionEyeEstimating2017; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up the filled-area emphasis that can make “mass” or “volume” feel more salient.
- **The Risk:** A line or scatter may feel less visually prominent or less “area-like” for audiences expecting an area presentation.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping an area chart and assuming it’s equivalent to a line chart “but prettier.”
- **Why it fails:** The experimental result indicates area charts (E-3) were significantly less accurate than line/scatter for trend estimation [@correllRegressionEyeEstimating2017], as recorded in the collation [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart uses a filled region under the curve (area mark) for bivariate trend reading.
- **The Test:** If your task prompt can be answered as “estimate the trend/slope,” verify you are using line or point marks rather than an area mark; otherwise you are violating the rule [@correllRegressionEyeEstimating2017; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the mark from area to line while keeping axes and scales the same.
- **Best Fix:** Use a standard line chart (for ordered X) or a scatterplot (for discrete points) to support trend estimation accuracy, matching the higher-ranked designs (E-2 or E-1) over E-3 [@correllRegressionEyeEstimating2017; @zengReviewCollationGraphical2023].
