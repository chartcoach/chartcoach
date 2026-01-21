---
id: replace-legends-with-direct-labels-for-color-coded-series
title: Directly Label Series Instead of Using a Color Legend
bibliography: references.bib
description: Remove reliance on color keys by labeling lines/areas/slices directly,
  improving readability for colorblind readers and everyone else.
labels:
- chart:line
- task:identify
- visual:text
- visual:color
- impact:clarity
- impact:accessibility
- data:categorical
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Label chart elements directly (e.g., label lines at their ends) and avoid using a color legend when color is the only link between label and data.

## The Logic <!-- role: reason -->

Legends require readers to map color swatches to marks; if colors are hard to distinguish, that mapping fails. Direct labels eliminate the lookup step and reduce dependence on hue discrimination, saving time for all readers [@muth_colorblindness_2020].

- **The Principle:** Reduce indirect decoding and color-dependent lookup
- **The Evidence:** The post states that color keys are a problem for colorblind readers and recommends directly labeling in line/area/pie charts, calling it a major time-saver for everyone [@muth_colorblindness_2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which series/category a mark represents
- **Data Type:** Multi-series line/area charts and segmented charts where labels can sit near marks
- **Audience:** General audiences, including colorblind readers [@muth_colorblindness_2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** There isn’t enough space to place unambiguous labels (e.g., many series tightly packed)
- **Reason:** Labels may overlap or become illegible; another strategy (reducing series, interaction) may be needed [@muth_colorblindness_2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** More layout work and potentially more chart space
- **The Risk:** Poorly placed labels can clutter and harm readability [@muth_colorblindness_2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a legend but making it bigger or moving it closer
- **Why it fails:** The reader still must match colors, which is exactly where colorblind confusion occurs [@muth_colorblindness_2020].

## How to Check <!-- role: check -->

- **Visual Sign:** You need to look back and forth between legend and marks to decode the chart
- **The Test:** Hide the legend; if you can’t identify series immediately, add direct labels [@muth_colorblindness_2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Label only the most important series directly and fade others
- **Best Fix:** Direct-label every series (or the relevant subset) and remove the legend entirely [@muth_colorblindness_2020].
