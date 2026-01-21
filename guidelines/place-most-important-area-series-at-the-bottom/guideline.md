---
id: place-most-important-area-series-at-the-bottom
title: Place the Most Important Series at the Bottom of a Stacked Area Chart
bibliography: references.bib
description: Put the key series on the baseline in a stacked area chart and use color
  to emphasize it for easier comparisons.
labels:
- chart:area
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- visual:color
- source:datawrapper
---

## The Rule <!-- role: advice -->

In a stacked area chart, place the most important value at the bottom and use color to make it stand out.

## The Logic <!-- role: reason -->

Readers compare values more easily when they share the same baseline. The bottom layer is the only series anchored to a consistent baseline across time, so it’s the easiest one to read and compare; color emphasis reinforces attention [@muth_area_charts_2018].

- **The Principle:** Baseline consistency improves comparability
- **The Evidence:** [@muth_area_charts_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Track and compare the most important component over time within a stacked composition
- **Data Type:** Stacked area chart with multiple components
- **Audience:** General readers who may otherwise misread middle layers

## When to Break It <!-- role: exceptions -->

- **Scenario:** Another component must be visually anchored to the baseline because it is the main comparison target.
- **Reason:** If the “most important” series changes based on the story, the baseline position should follow the story, not a fixed ordering [@muth_area_charts_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reordering layers can make it harder for repeat readers to track a category if they expect a conventional order.
- **The Risk:** Emphasizing one series with color may visually downplay other series that some readers still care about [@muth_area_charts_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Leaving the key series in the middle/top and relying on a bright color alone.
- **Why it fails:** Color doesn’t solve the baseline problem; the series is still harder to compare [@muth_area_charts_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The story’s main series is not the one touching the x-axis.
- **The Test:** Ask a reader to estimate the main series at two points; if they struggle, move it to the baseline [@muth_area_charts_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reorder the stack so the key series is at the bottom [@muth_area_charts_2018].
- **Best Fix:** Reorder the stack and apply a distinct, story-consistent color to the key series while keeping others more subdued [@muth_area_charts_2018].
