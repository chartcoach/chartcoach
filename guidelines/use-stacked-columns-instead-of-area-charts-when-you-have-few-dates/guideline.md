---
id: use-stacked-columns-instead-of-area-charts-when-you-have-few-dates
title: Use stacked column charts instead of area charts when you have fewer than about
  ten dates
bibliography: references.bib
description: With few time points, stacked columns improve labeling and make values
  easier to read than stacked areas.
labels:
- chart:area
- task:trend
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- complexity:foundational
---

## Prefer stacked columns over stacked areas for short time series <!-- role: advice -->

Use a stacked column chart instead of a stacked area chart when you have fewer than about ten dates.

## Discrete bars support clearer labeling and value reading at low temporal density <!-- role: reason -->

When there are only a few time points, discrete stacked columns create separable segments that are easier to label and read than continuous stacked areas.

**Mechanism:** Column segments provide clearer boundaries at each time point, reducing ambiguity about where one time value ends and the next begins.

**Evidence:** For less than about ten dates, stacked column charts are recommended over area charts because labeling is improved and readers can read values more easily, especially with many shares that vary over time [@muth_area_charts_2018].

**Notes:** This guidance targets readability and labeling, not aesthetics.

## When this applies <!-- role: context -->

- **User Goal:** Understand composition at each of a small number of time points.
- **Task:** Compare part-to-whole snapshots across a short timeline.
- **Data:** Time series with low count of dates (roughly under ten) and multiple components.
- **Chart Setting:** Static charts where labels must do more work than tooltips.
- **Audience:** General audiences scanning quickly.
- **Success Criterion:** Labels are legible and readers can estimate values at each time point without confusion.

## When not to follow this <!-- role: exceptions -->

**Break it when:** The time intervals are irregular and you must show the spacing accurately on a continuous time axis. **Why:** Area charts can represent continuous scales with uneven gaps, while column charts do not communicate irregular intervals as naturally [@muth_area_charts_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Columns can feel heavier visually and may require more horizontal space. **Risk:** If there are many components, segments can become thin and hard to label even in columns. **Mitigation:** Consider grouping small components to reduce segment count [@muth_area_charts_2018].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a stacked area chart for five to eight dates and struggling to place readable labels. **Why it fails:** Continuous areas don’t create clean per-date separation, making labeling and value reading harder than necessary [@muth_area_charts_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** Labels overlap or drift ambiguously across adjacent time points. **Quick Check:** Count the dates; if it’s under about ten, try stacked columns. **Stronger Test:** Create both versions and see which allows direct labeling without clutter while keeping the message intact [@muth_area_charts_2018].

## What to do instead <!-- role: fix -->

- Switch to a stacked column chart when the series has a small number of dates [@muth_area_charts_2018].
- Group tiny categories into an “others” segment to reduce label and segment clutter [@muth_area_charts_2018].
- Place labels manually rather than relying on automatic labeling when segments are tight [@muth_area_charts_2018].
