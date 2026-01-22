---
id: avoid-splitting-radial-daily-patterns-into-two-12h-rose-charts
title: Avoid splitting daily patterns into two 12-hour radial rose charts when users
  must read or select time intervals
bibliography: references.bib
description: "In daily-pattern tasks, the split 2\xD712-hour radial rose chart performs\
  \ worse than linear alternatives and is not a good default for time-interval selection."
labels:
- chart:radial
- chart:bar
- task:retrieve
- task:filter
- task:sort
- task:extremum
- visual:orientation
- visual:column
- impact:speed
- impact:accuracy
- impact:preference
- data:temporal
- audience:novice
- study:experiment
---

## Do not use split 12-hour rose charts as the default daily-pattern display <!-- role: advice -->

Avoid a split 2×12-hour radial rose chart as the default for daily patterns, especially when users need to quickly read, compare, or pick specific hours.

## Splitting plus radial mapping increases decoding burden <!-- role: reason -->

Splitting the day into two separate radial charts adds an extra “which half?” decision on top of radial decoding, increasing the chance of slower or less reliable performance compared to linear bar charts.

**Mechanism:** Two separate views create an additional navigation/selection step that can slow tasks that require locating hours or comparing across the day; radial geometry further increases mapping complexity.

**Evidence:** The 2×12-hour radial rose chart was consistently lowest-ranked for accuracy and/or time in the collated task results (filter, retrieve value, sort, find extremum) and was lowest in overall user preference among the four tested designs. [@waldnerComparisonRadialLinear2020; @zengReviewCollationGraphical2023]

**Notes:** This guideline is specific to the tested “2×12 radial rose” design relative to the tested linear and 24-hour radial variants.

## Where split radial charts become a liability <!-- role: context -->

- **User Goal:** Identify or act on specific hours (e.g., pick an hour, compare morning vs evening values).
- **Task:** Retrieve-value, filter, sort, or find-extremum.
- **Data:** Hourly bins across one day (ordered categories) with quantitative values.
- **Chart Setting:** Static dashboard/report context where the chart is meant to be read quickly.
- **Audience:** General or non-expert readers.
- **Success Criterion:** Fast, correct selections and higher subjective suitability.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your primary requirement is stylistic/engagement and you are not optimizing for task speed/accuracy. **Why:** The evidence here is about performance and preference in analysis tasks, not about aesthetics goals.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You lose the explicit AM/PM separation in a clock-like layout.\
**Risk:** Keeping a single continuous chart may require more horizontal space than two compact radial forms.\
**Mitigation:** If space forces a split, use a split linear bar layout rather than a split radial rose chart.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Splitting the day into AM/PM rose charts to “match how people read clocks.” **Why it fails:** In tested daily-pattern tasks, the split radial option ranked worst overall and did not gain an advantage from the clock-like split. [@waldnerComparisonRadialLinear2020; @zengReviewCollationGraphical2023]

## Quick tests <!-- role: check -->

**Failure Sign:** Users hesitate about whether a target hour is in the AM or PM half, or they slow down when switching between the two halves.\
**Quick Check:** Time a simple “find this hour” or “which hour is the maximum” task; if performance is slower than a linear bar alternative, drop the split rose chart.\
**Stronger Test:** Run a within-subject A/B on retrieve-value and find-extremum and compare median completion time.

## What to do instead <!-- role: fix -->

- Use a single continuous 24-hour linear bar chart for daily patterns.
- If you need an AM/PM split, use two linear bar charts (2×12) rather than two radial rose charts.
- Prefer layouts that keep the full day scannable without cross-panel switching when sorting or searching for extremes.
