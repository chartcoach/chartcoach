---
id: use-colorfield-over-line-for-max-average-in-time-series
title: Use a Colorfield Instead of a Line Chart to Find the Maximum Average in a Time
  Series
bibliography: references.bib
description: For aggregate judgments over time (e.g., which month has the highest
  average), prefer a color-hue colorfield over a position-based line chart to improve
  accuracy.
labels:
- chart:line
- chart:heatmap
- task:aggregate
- visual:color
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- source:graphical-perception
---

## The Rule <!-- role: advice -->

When the task is to identify the time interval with the highest average value, use a colorfield encoding (value → color hue across the time axis) instead of a line chart (value → vertical position).

## The Logic <!-- role: reason -->

Encoding values as color supports efficient perceptual summarization of regions, improving performance on average-over-range judgments compared to reading positions along a line.

- **The Principle:** Perceptual summarization for aggregate judgments via color encoding
- **The Evidence:** In an aggregate task (“select the month with the highest average”), a color-hue colorfield (E-2) was significantly more accurate than a line chart (E-1) (ANOVA, p ≤ 0.001) [@correllComparingAveragesTime2012]. This result is collated as a recommendation-relevant ranking in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which sub-range of time has the maximum average (an aggregate judgment over intervals).
- **Data Type:** Ordered (temporal/ordinal x-axis) series with quantitative values.
- **Audience:** General audiences performing quick aggregate comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user needs precise value reading at specific time points (not aggregate-over-range).
- **Reason:** This guideline is only supported by evidence for an aggregate task; the cited study result does not establish superiority for precise value retrieval [@correllComparingAveragesTime2012; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced emphasis on exact point-by-point values compared to position-based reading.
- **The Risk:** Viewers may focus on local extrema or salient colors rather than the intended interval-average if the goal is not clearly framed as an averaging task.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a line chart and expecting users to accurately “eyeball” interval means.
- **Why it fails:** The evidence shows lower accuracy for the line-chart design than the colorfield design for this aggregate task [@correllComparingAveragesTime2012; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users repeatedly choose the interval containing a prominent peak rather than the interval with the highest average.
- **The Test:** Ask a few users to perform the “max-average interval” task; if they struggle or disagree widely, treat it as a signal that the line chart is a poor fit and consider switching to a colorfield [@correllComparingAveragesTime2012].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a colorfield view (value → color hue) aligned to the same time axis as the existing chart for the aggregate task.
- **Best Fix:** Replace the line chart with a colorfield encoding for the aggregate judgment workflow so the primary encoding supports average-over-range comparison [@correllComparingAveragesTime2012; @zengReviewCollationGraphical2023].
