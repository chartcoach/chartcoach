---
id: prefer-lines-or-columns-over-area-for-single-series
title: Prefer Lines or Columns Over Area for a Single Series
bibliography: references.bib
description: Avoid area charts for a lone time series; use a line chart (or columns
  for few dates) for easier reading and labeling.
labels:
- chart:area
- task:trend
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Don’t use an area chart to show just one value over time; use a line chart (or a column chart if you have only a few dates).

## The Logic <!-- role: reason -->

With a single series, the filled area adds little beyond what a line already communicates, and it can force a zero baseline. With few dates, columns support clearer value reading and labeling [@muth_area_charts_2018].

- **The Principle:** Avoid unnecessary encodings that reduce labeling and scale flexibility
- **The Evidence:** [@muth_area_charts_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand one metric’s change over time
- **Data Type:** Single time series; sometimes sparse dates
- **Audience:** General readers who benefit from quick interpretation

## When to Break It <!-- role: exceptions -->

- **Scenario:** You explicitly want the y-axis to start at zero and the filled area is integral to your message.
- **Reason:** The post emphasizes line charts especially when you *don’t* want to start at zero; if you do want zero, an area can be acceptable (though still optional) [@muth_area_charts_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose the “filled” emphasis that can make a single series feel more substantial.
- **The Risk:** Switching to columns can overemphasize discrete intervals if the audience expects continuity [@muth_area_charts_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using an area chart for a single series even when the key story is subtle variation.
- **Why it fails:** Area charts constrain axis choices and can make subtle variation harder to see; labeling can also be worse [@muth_area_charts_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The fill dominates but doesn’t add information; the baseline/scale feels overly tall for the variation.
- **The Test:** Toggle to a line chart; if readability improves without losing meaning, the area fill was unnecessary [@muth_area_charts_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a line chart [@muth_area_charts_2018].
- **Best Fix:** If there are only a few dates, use a column chart to improve labeling and value reading [@muth_area_charts_2018].
