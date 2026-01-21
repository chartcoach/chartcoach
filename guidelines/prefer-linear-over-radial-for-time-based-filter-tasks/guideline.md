---
id: prefer-linear-over-radial-for-time-based-filter-tasks
title: Use Linear Charts for Filter Tasks Over Daily Patterns
bibliography: references.bib
description: For filter tasks on daily patterns, linear bar charts outperform radial
  rose charts in both accuracy and time.
labels:
- chart:bar
- chart:radial
- task:filter
- impact:accuracy
- impact:efficiency
- data:temporal
- data:binned
- audience:novice
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

For filtering in daily-pattern charts, choose a linear bar chart over a radial rose chart.

## The Logic <!-- role: reason -->

- **The Principle:** Linear layouts reduce search and decoding cost when identifying bins that match a condition.
- **The Evidence:** For the filter task, accuracy ranks linear (E-3, E-4) above radial (E-2, E-1), and time ranks the 24-hour linear (E-4) fastest overall [@waldnerComparisonRadialLinear2020]. This paper’s findings are part of the systematically collated evidence base [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Filter—find bins meeting a specified condition (e.g., identify times meeting a threshold).
- **Data Type:** Daily (24-hour) binned values.
- **Audience:** General users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Filtering is not required (the view is purely decorative or narrative without lookup).
- **Reason:** The guideline is supported by task-based performance data specific to filtering [@waldnerComparisonRadialLinear2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less visually novel presentation than radial.
- **The Risk:** If stakeholders overvalue novelty, they may resist the more effective option.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a rose chart because it “matches the daily cycle,” then expecting it to support filtering well.
- **Why it fails:** Radial variants (E-1/E-2) rank below linear variants on both accuracy and time for filter [@waldnerComparisonRadialLinear2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Users struggle to quickly identify which hour bins satisfy the condition.
- **The Test:** Run the filter task with timed trials; compare completion times between radial and linear; linear should win as observed [@waldnerComparisonRadialLinear2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a linear 24-hour bar chart while keeping the same binning.
- **Best Fix:** In recommendation logic, bias toward linear bar charts for filter tasks on daily patterns, consistent with the collated task-to-design evidence [@zengReviewCollationGraphical2023; @waldnerComparisonRadialLinear2020].
