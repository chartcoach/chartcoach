---
id: prefer-linear-24h-bar-over-radial-rose-for-daily-pattern-tasks
title: Prefer a single 24-hour linear bar chart over radial rose charts for daily-pattern
  analysis tasks
bibliography: references.bib
description: For daily patterns, a continuous 24-hour linear bar chart yields better
  performance and preference than radial rose chart variants across common low-level
  tasks.
labels:
- chart:bar
- chart:radial
- task:filter
- task:retrieve
- task:sort
- task:extremum
- visual:position
- visual:length
- visual:orientation
- impact:accuracy
- impact:speed
- impact:preference
- data:temporal
- audience:novice
- study:experiment
---

## Use a 24-hour linear bar chart for daily patterns <!-- role: advice -->

Use a single 24-hour linear bar chart instead of a radial rose chart when people need to perform common daily-pattern read/compare tasks.

## Linear position/length supports faster and more accurate judgments <!-- role: reason -->

A continuous linear bar chart uses a consistent baseline and position/length judgments that support fast and reliable reading and comparison, while radial rose charts require mapping angle/orientation and curved geometry that can slow down and degrade performance.

**Mechanism:** A shared linear baseline reduces visual-mapping effort for value lookup, ordering, and identifying extremes, improving speed and overall task success versus radial layouts.

**Evidence:** Across low-level daily-pattern tasks (filter, retrieve value, sort, find extremum) and overall user preference, the single 24-hour linear bar chart was top-ranked (or tied-top) versus 12-hour split linear and both radial variants. [@waldnerComparisonRadialLinear2020; @zengReviewCollationGraphical2023]

**Notes:** This guideline targets the specific daily-pattern comparison space tested: 24-hour vs 2×12-hour, linear bars vs radial rose charts.

## Where daily-pattern judgments are needed <!-- role: context -->

- **User Goal:** Read, scan, or compare hourly values in a day to make a decision.
- **Task:** Filter, retrieve-value, sort, or find-extremum.
- **Data:** Periodic daily time (ordered hours) with quantitative magnitude per hour.
- **Chart Setting:** Static, screen-based chart; hour bins shown as bars.
- **Audience:** Non-expert or general audience.
- **Success Criterion:** Higher accuracy, lower completion time, and higher user preference.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your use case is not a 24-bin daily pattern shown as bars (e.g., a different encoding or non-hourly granularity). **Why:** This evidence only covers the four tested bar/rose designs and tasks for daily patterns.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You give up the circular “clock-like” aesthetic and the compact radial form factor.\
**Risk:** If your page layout strongly constrains width, you may be tempted to switch to radial despite worse performance.\
**Mitigation:** Treat radial as a stylistic choice only when analysis performance is not the priority.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Choosing a radial rose chart for daily patterns because the clock metaphor “feels intuitive.” **Why it fails:** In tested tasks, radial variants ranked worse in speed and preference and did not outperform the linear 24-hour bar chart overall. [@waldnerComparisonRadialLinear2020; @zengReviewCollationGraphical2023]

## Quick tests <!-- role: check -->

**Failure Sign:** Readers take noticeably longer to locate hours or misread/hesitate on values in a radial daily chart.\
**Quick Check:** Ask someone to find a specified hour and the maximum hour value; if they pause to orient themselves, prefer the linear 24-hour bar chart.\
**Stronger Test:** Run a small timed task test for retrieve-value and find-extremum on both designs and compare completion times.

## What to do instead <!-- role: fix -->

- Use a single continuous 24-hour linear bar chart for daily patterns.
- If you must show two halves of the day, use a linear split (2×12) rather than switching to a radial rose chart.
- Keep the chart continuous when the task involves scanning for maxima or sorting across the whole day.
