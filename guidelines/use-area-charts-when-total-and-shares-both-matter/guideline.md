---
id: use-area-charts-when-total-and-shares-both-matter
title: Use Area Charts Only When the Total and Its Shares Matter
bibliography: references.bib
description: Prefer area charts when you need to show both the total and how each
  component contributes to it over time.
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

Use an area chart only when the total (the full stack height) is as important as the component shares; if the total is not important, use a line chart instead.

## The Logic <!-- role: reason -->

Stacked areas naturally emphasize the cumulative total plus composition. If viewers only need individual series, stacked fills add unnecessary complexity; lines are typically easier for readers to understand in that case [@muth_area_charts_2018].

- **The Principle:** Don’t add part-to-whole structure if the whole isn’t part of the message
- **The Evidence:** [@muth_area_charts_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand both (1) overall total change and (2) how parts contribute over time
- **Data Type:** Multiple time series that form a meaningful sum per date
- **Audience:** Broad audiences who benefit from intuitive encoding of “total + shares”

## When to Break It <!-- role: exceptions -->

- **Scenario:** Values add up to 100% at every date (pure shares).
- **Reason:** An area chart (or stacked columns) can still be the most intuitive option for showing composition over time even when a “total” is fixed at 100% [@muth_area_charts_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Using an area chart commits you to showing the stack and (often) a zero baseline, which can reduce flexibility compared to lines.
- **The Risk:** Readers may struggle more than with a line chart if the total isn’t actually relevant to the story [@muth_area_charts_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a stacked area chart when you only care about one component’s trend.
- **Why it fails:** The stacked fill and total height add decoding work without adding information the reader needs [@muth_area_charts_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Your headline and annotations never mention the total, only individual series.
- **The Test:** Ask: “If I removed the stacked total, would the message stay the same?” If yes, switch to a line chart [@muth_area_charts_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the area chart with a line chart when the total is not part of the message [@muth_area_charts_2018].
- **Best Fix:** If composition is the message (e.g., always 100%), keep a share-focused area/stacked column and label/annotate accordingly [@muth_area_charts_2018].
