---
id: analyze-synthesis-predictions-by-mean-and-variance
title: Analyze Prediction Tasks Using Mean and Variance
bibliography: references.bib
description: For Synthesis-level prediction questions, compare both average predictions
  and how dispersed they are across designs.
labels:
- task:predict
- impact:insight
- data:temporal
- custom:blooms-taxonomy
---

## The Rule <!-- role: advice -->

When using **Synthesis** tasks (predictions), evaluate design effects on both the **mean** prediction and the **variance** (spread) of predictions.

## The Logic <!-- role: reason -->

The paper treats Synthesis as “create something new” via prediction and shows that redesigns can affect not only the central tendency of predicted values but also the dispersion (e.g., different variances for market trade deficit predictions; reduced variance for Canada immigration predictions). This reveals affordances that earlier levels may miss [@burnsHowEvaluateData2020].

- **The Principle:** Design can shape both expected value and uncertainty in user forecasts
- **The Evidence:** [@burnsHowEvaluateData2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand how a chart supports extrapolation beyond shown data
- **Data Type:** Ordered sequences/time series or any chart inviting extrapolation
- **Audience:** General audiences making forecasts from displayed trends [@burnsHowEvaluateData2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Predictions are not meaningful because the chart does not imply an ordered progression
- **Reason:** Without a coherent basis for extrapolation, prediction variance may reflect guessing rather than chart affordance [@burnsHowEvaluateData2020]

## The Price <!-- role: costs -->

- **The Sacrifice:** More statistical/analytical work and decisions about excluding non-numeric answers (ranges, qualitative trends)
- **The Risk:** Excluding responses can bias results if exclusions differ by condition [@burnsHowEvaluateData2020]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reporting only the average predicted value
- **Why it fails:** You can miss meaningful differences in how consistently a design supports prediction (variance differences) [@burnsHowEvaluateData2020]

## How to Check <!-- role: check -->

- **Visual Sign:** Two designs have similar averages, but one produces wildly inconsistent predictions
- **The Test:** Plot distributions (or compute variance) of predictions per design, not just a mean [@burnsHowEvaluateData2020]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a dispersion metric (variance/SD) alongside the mean when comparing designs
- **Best Fix:** Predefine response handling (single numeric vs ranges) and compare both mean and variance across designs as in the paper’s analyses [@burnsHowEvaluateData2020]
