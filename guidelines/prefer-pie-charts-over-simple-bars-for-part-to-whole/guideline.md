---
id: prefer-pie-charts-over-simple-bars-for-part-to-whole
title: Use Pie Charts Over Simple Bar Charts for Part-to-Whole Estimation
bibliography: references.bib
description: Pie charts provide better accuracy than simple bar charts for estimating
  percentages due to natural visual anchors.
labels:
- chart:pie-chart
- chart:bar-chart
- task:part-to-whole
- task:estimate-value
- visual:angle
- visual:area
- impact:accuracy
- data:quantitative
- data:proportions
---

## The Rule <!-- role: advice -->
When designing for part-to-whole estimation tasks without explicit scales, choose pie charts over simple horizontal or stacked bar charts.

## The Logic <!-- role: reason -->
Pie charts provide inherent cognitive advantages for estimating proportions. The circular shape offers "natural anchors" at 0%, 25%, 50%, and 75% (corresponding to 0°, 90°, 180°, and 270° angles). Users utilize these imaginary quarters and halves to judge segment size more accurately than they judge length in a bar chart devoid of reference lines.
*   **The Principle:** Perceptual Anchoring
*   **The Evidence:** As detailed in the review by Zeng and Battle [@zeng_review_2023], experiments conducted by Redmond [@redmond_visual_2019] demonstrated that participants estimated values with significantly lower Mean Absolute Error (MAE) using pie charts compared to baseline bar charts.

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapidly estimating the percentage of a whole (e.g., "Is this about 30% or 40%?").
*   **Data Type:** Single-variable proportional data (percentages summing to 100%).
*   **Audience:** General audiences relying on visual intuition rather than precise reading of axes.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When a quantitative axis/scale is available and space permits.
*   **Reason:** Redmond found that bar charts equipped with a full quantitative scale outperform standard pie charts [@redmond_visual_2019].
*   **Scenario:** When comparing slight differences across multiple charts.
*   **Reason:** While not the focus of this specific estimation experiment, comparative tasks often suffer in pie charts due to spatial arrangement.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Pie charts generally require more layout space than a simple horizontal bar to be legible.
*   **The Risk:** Deviating from "best practices" touted by some data visualization experts (like Tufte or Few) who discourage pie charts, though the empirical evidence suggests this criticism may be unfounded for estimation tasks [@redmond_visual_2019].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a stacked bar chart without an axis to save space.
*   **Why it fails:** Without a scale, the bar chart lacks the "natural anchors" of the circle, leading to higher error rates in estimation [@zeng_review_2023].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using a floating rectangular bar to represent a percentage without an axis?
*   **The Test:** Ask a user to estimate the value. If they struggle to define "halfway" or "quarter-way" on the bar, the design is failing.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Convert the visualization to a pie chart.
*   **Best Fix:** If keeping the bar chart, add a clear quantitative axis or percentage markers (see related guideline).
