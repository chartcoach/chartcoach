---
id: avoid-bar-charts-for-mean-estimation
title: Avoid Bar Charts for Visual Mean Estimation
bibliography: references.bib
description: Users systematically underestimate the average value of data presented
  in bar charts.
labels:
- chart:bar
- task:aggregate
- visual:length
- impact:accuracy
- data:quantitative
- source:empirical
---

## The Rule <!-- role: advice -->
Do not use bar charts if the primary user task is to visually estimate the mean (average) of the dataset.

## The Logic <!-- role: reason -->
Bar charts create a systematic perceptual bias where users perceive the aggregate mean to be lower than it actually is.
*   **The Principle:** Underestimation Bias. The visual weight of the bar (the filled area) pulls the perceived center of gravity downwards.
*   **The Evidence:** As reviewed by Zeng and Battle [@zeng_review_2023], experiments by Godau et al. [@godau_perception_2016] demonstrate that participants consistently underestimate the mean value in bar graphs, regardless of whether the bars are high or low.

## Where to Apply <!-- role: context -->
*   **User Goal:** When the user needs to look at a distribution and intuitively grasp the "average" or "center" value without explicit annotation.
*   **Data Type:** Quantitative data distributions presented as bar charts (area-rect marks).
*   **Audience:** General users performing summary tasks.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the exact mean is explicitly plotted as a line or written as text on the chart.
*   **Reason:** Explicit annotation overrides the perceptual estimation bias.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the familiar "volume" metaphor of bars that helps with comparing individual magnitudes.
*   **The Risk:** Alternative charts (like strip plots) may be harder to read if the data density is extremely high.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding a grid or a numerical scale without marking the mean.
*   **Why it fails:** Godau et al. [@godau_perception_2016] found that while scales help slightly (Design E-3 performed better than E-1), the systematic underestimation bias persists.

## How to Check <!-- role: check -->
*   **Visual Sign:** A bar chart used for a summary dashboard where the user is expected to judge the overall performance (mean) of a group.
*   **The Test:** Ask a user to point to where they think the average value is on the Y-axis. Check if they point below the mathematical mean.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Draw a reference line indicating the actual mean on top of the bars.
*   **Best Fix:** Switch to a point-based visualization (dot plot) or a box plot that explicitly encodes summary statistics.
