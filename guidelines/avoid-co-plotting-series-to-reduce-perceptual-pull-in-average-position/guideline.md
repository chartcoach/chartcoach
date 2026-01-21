---
id: avoid-co-plotting-series-to-reduce-perceptual-pull-in-average-position
title: Avoid Co-Plotting Multiple Series When Users Must Estimate Averages
bibliography: references.bib
description: When multiple series are shown together, average position estimates can
  be pulled toward the other series.
labels:
- chart:line
- chart:bar
- task:aggregate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- phenomenon:perceptual-pull
---

## The Rule <!-- role: advice -->

Avoid presenting multiple data series in the same view when the user task is to estimate the average position of one target series.

## The Logic <!-- role: reason -->

- **The Principle:** Perceptual pull between series during average position estimation.
- **The Evidence:** The collation in [@zengReviewCollationGraphical2023] records experimental findings that, in displays with two lines, two bar series, or a line-plus-bar combination, perceived average position of a target series is pulled toward the other series [@xiongBiasedAveragePosition2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating the average level of one series (aggregate task) rather than comparing series directly.
- **Data Type:** Quantitative series where “average vertical position” is the intended takeaway.
- **Audience:** General viewers doing quick, perceptual summarization.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary goal is explicitly to compare the series against each other (not to estimate an absolute average of one).
- **Reason:** This guideline targets the aggregate (average estimation) situation described in the collated evidence [@xiongBiasedAveragePosition2020; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced direct comparability if series are separated into different views.
- **The Risk:** If you separate series, users may need more effort to compare them.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Overlaying or stacking series and assuming users can mentally “ignore” the non-target series while estimating the target’s average.
- **Why it fails:** The recorded evidence indicates the non-target series can still pull the target’s perceived average position [@xiongBiasedAveragePosition2020], as collated by [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users’ estimated average for a target series shifts depending on what other series are shown nearby, even when the target series is unchanged.
- **The Test:** Keep the target series constant, vary the presence/position of a second series, and see whether users’ average estimates for the target change.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove the non-target series in views intended for average estimation, or provide a separate view focused on the target series.
- **Best Fix:** Use separate displays for each series when average estimation accuracy matters, to avoid perceptual pull effects documented in [@xiongBiasedAveragePosition2020] and summarized in [@zengReviewCollationGraphical2023].
