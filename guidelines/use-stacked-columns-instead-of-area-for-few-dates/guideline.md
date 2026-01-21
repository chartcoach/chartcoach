---
id: use-stacked-columns-instead-of-area-for-few-dates
title: Use Stacked Column Charts Instead of Area Charts for Few Dates
bibliography: references.bib
description: Prefer stacked columns over stacked areas when there are fewer than about
  ten time points for easier labeling and value reading.
labels:
- chart:area
- task:part-to-whole
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

If you have fewer than about ten dates, use a stacked column chart instead of an area chart.

## The Logic <!-- role: reason -->

With few time points, discrete columns make it easier to label and help readers read values and shares, especially when shares vary a lot over time [@muth_area_charts_2018].

- **The Principle:** Use discrete marks when the time axis is sparse to improve labeling and value reading
- **The Evidence:** [@muth_area_charts_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Read values/shares at a small number of time points
- **Data Type:** Stacked composition over time with < ~10 dates
- **Audience:** General public; situations where labels must do a lot of work

## When to Break It <!-- role: exceptions -->

- **Scenario:** The time intervals between dates are irregular and must be shown proportionally.
- **Reason:** The post notes area charts use continuous scales that show dates at the right intervals, while column charts don’t [@muth_area_charts_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Stacked columns may not represent uneven temporal spacing accurately.
- **The Risk:** Readers may infer equal spacing between columns even when intervals differ [@muth_area_charts_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping an area chart with only a handful of dates and piling on labels.
- **Why it fails:** The chart remains harder to label cleanly than stacked columns for sparse time points [@muth_area_charts_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Labels collide or the chart feels underpopulated along the x-axis.
- **The Test:** Count the time points; if it’s under ~10, prototype a stacked column version and compare label readability [@muth_area_charts_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a stacked column chart [@muth_area_charts_2018].
- **Best Fix:** If you must reflect irregular intervals, keep an area chart but explicitly label/annotate the uneven spacing to prevent misreading [@muth_area_charts_2018].
