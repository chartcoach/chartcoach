---
id: expect-overestimation-in-average-bar-position-estimates
title: Anticipate Overestimation in Average Bar Position Judgments
bibliography: references.bib
description: Average position judgments from bar charts can be systematically overestimated.
labels:
- chart:bar
- task:aggregate
- visual:length
- impact:accuracy
- data:quantitative
- audience:general
- phenomenon:systematic-bias
---

## The Rule <!-- role: advice -->

Anticipate that viewers will overestimate the average vertical position of bars when they report an average from a bar chart.

## The Logic <!-- role: reason -->

- **The Principle:** Systematic bias in positional averaging for bars (overestimation).
- **The Evidence:** In the collated dataset described by [@zengReviewCollationGraphical2023], experimental results indicate average position reports for a single bar series (length encoding with rect marks) are biased toward overestimation [@xiongBiasedAveragePosition2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating an “overall level” (average) from a bar series.
- **Data Type:** Quantitative values encoded as bar length/extent in a bar chart.
- **Audience:** Any audience doing quick perceptual averaging (e.g., business dashboards).

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user is not estimating an average from the bar series (e.g., they read a labeled mean directly, or focus on a single highlighted bar).
- **Reason:** The evidence is specifically about aggregate (average) position estimation bias as represented in the collation [@xiongBiasedAveragePosition2020; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need additional annotation or validation if accurate “average” impressions are important.
- **The Risk:** Overemphasizing bias could distract from other more important analytic goals.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating the perceived “average bar height” as a reliable proxy for the true mean without checking.
- **Why it fails:** The experimental findings summarized in [@zengReviewCollationGraphical2023] report systematic overestimation for bar-series average position judgments [@xiongBiasedAveragePosition2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Users consistently report an average level higher than the computed mean of the bar values.
- **The Test:** Run a quick user check: ask for a perceived average from the chart and compare to the true mean.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide an explicit average reference so the “average” is not inferred only from eyeballing bar positions.
- **Best Fix:** Redesign the display so users do not need to rely on memory-based average bar position estimation, given the overestimation bias reported in [@xiongBiasedAveragePosition2020] and collated in [@zengReviewCollationGraphical2023].
