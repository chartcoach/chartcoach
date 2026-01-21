---
id: avoid-area-charts-for-tiny-differences-use-lines
title: Avoid Area Charts for Tiny Differences; Use Line Charts
bibliography: references.bib
description: Use line charts instead of area charts when differences are small and
  you need a non-zero baseline to make changes visible.
labels:
- chart:area
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Do not use an area chart when differences between values are very small; use a line chart so the y-axis doesn’t need to start at zero.

## The Logic <!-- role: reason -->

Area charts generally require a zero baseline for honest area encoding; that constraint can compress small variations. Line charts can use a tighter y-range, making tiny differences easier to see [@muth_area_charts_2018].

- **The Principle:** Choose an encoding that supports an appropriate axis range for the magnitude of differences
- **The Evidence:** [@muth_area_charts_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Notice small changes and differences over time
- **Data Type:** Time series with small variation relative to the full scale
- **Audience:** Any audience needing to perceive subtle changes

## When to Break It <!-- role: exceptions -->

- **Scenario:** Differences are large enough that the trend is clearly visible in an area chart.
- **Reason:** The post notes area charts work best for considerably large differences, where the trend can be seen well enough [@muth_area_charts_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Switching to lines reduces the immediate “mass” impression that areas can give.
- **The Risk:** A tighter y-axis in a line chart can make changes look more dramatic than a zero-based area chart (even if the intent is to reveal small differences) [@muth_area_charts_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping an area chart and hoping color/labels will reveal tiny differences.
- **Why it fails:** The compressed scale remains the core readability issue; labels don’t restore visual sensitivity to small changes [@muth_area_charts_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The stacked/fill shapes look nearly flat or indistinguishable.
- **The Test:** Temporarily switch to a line chart with a tighter y-range; if differences suddenly become readable, the area chart was the wrong choice [@muth_area_charts_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Change the chart type to a line chart [@muth_area_charts_2018].
- **Best Fix:** Use a line chart and set an appropriate y-axis range that reveals the small differences while keeping the message honest and clear [@muth_area_charts_2018].
