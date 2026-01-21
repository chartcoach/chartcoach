---
id: prefer-24h-linear-bar-over-rose-charts-for-daily-patterns
title: "Prefer a 24\u2011hour Linear Bar Chart Over Radial Rose Charts"
bibliography: references.bib
description: For daily-pattern visualizations, a single 24-hour linear bar chart outperforms
  radial rose charts in accuracy, speed, and user preference across tasks.
labels:
- chart:bar
- chart:radial
- task:compare
- impact:accuracy
- impact:efficiency
- data:temporal
- data:binned
- audience:novice
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use a single 24-hour linear bar chart for daily patterns instead of a radial rose chart.

## The Logic <!-- role: reason -->

- **The Principle:** Cartesian length/position decoding is faster and more accurate than decoding the same binned values in a radial layout.
- **The Evidence:** Across the evaluated tasks, the 24-hour linear bar chart (E-4) ranked best overall on time and user preference, and was top-ranked (or tied top) on accuracy depending on task [@waldnerComparisonRadialLinear2020]. This guidance is captured as a perception-driven rule in the collation effort [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly and accurately interpret daily (24-hour) binned patterns across low-level tasks (filter, retrieve value, find extremum, sort).
- **Data Type:** 24 bins over a day (hourly), quantitative magnitude by bin, temporal/ordinal ordering of hours.
- **Audience:** Non-expert / general-public users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must use a radial layout due to strong non-analytic constraints (e.g., strict stylistic mandate).
- **Reason:** This rule is grounded in measured performance and preference; if performance is not the goal, you may accept the tradeoff [@waldnerComparisonRadialLinear2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up a radial/clock-like aesthetic.
- **The Risk:** If stakeholders expect a “clock” metaphor, the linear chart may feel less thematically aligned even though it performs better [@waldnerComparisonRadialLinear2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching from 24-hour linear to a 24-hour rose chart to “match the clock.”
- **Why it fails:** The radial condition (E-2) ranked below the 24-hour linear chart (E-4) on speed and preference overall, and often lower on accuracy depending on task [@waldnerComparisonRadialLinear2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate when reading values or locating/ordering hours, or report disliking the chart format.
- **The Test:** Run quick timed trials for the same tasks with both layouts; if linear is consistently faster or preferred, the radial choice is likely harming usability (as observed in the study) [@waldnerComparisonRadialLinear2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the rose chart with a 24-hour linear bar chart while keeping the same binning and scale.
- **Best Fix:** Standardize on 24-hour linear bars for daily-pattern views in recommendation outputs for these tasks, as reflected by the collated guideline pathway [@zengReviewCollationGraphical2023; @waldnerComparisonRadialLinear2020].
