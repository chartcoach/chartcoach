---
id: use-area-charts-only-for-change-over-time
title: Use Area Charts Only for Change Over Time
bibliography: references.bib
description: Choose area charts only when your main message is how values (and often
  their total) develop over time.
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

Use an area chart only to show how values develop over time; if your goal is to compare categories, use bars/columns (or split bars) instead.

## The Logic <!-- role: reason -->

Area charts encode values as filled regions across a time axis; they are meant to communicate temporal development rather than static differences between categories. Using them for category comparison makes reading and interpretation harder, so a chart type optimized for comparing categories is clearer [@muth_area_charts_2018].

- **The Principle:** Match chart type to the comparison task (change-over-time vs. category comparison)
- **The Evidence:** [@muth_area_charts_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** See how one or more values evolve over time (optionally as parts of a total)
- **Data Type:** Temporal series (dates on the x-axis), often multiple series that may form a total
- **Audience:** General readers who need fast, intuitive reading

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need to show temporal development.
- **Reason:** This is exactly when the rule applies; use an area chart (subject to the other constraints in the post) [@muth_area_charts_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a chart type that can show both totals and composition at once if you switch away from area.
- **The Risk:** Using bars/columns instead may reduce emphasis on continuous time development (especially when dates are irregular) [@muth_area_charts_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using an area chart for “how categories differ” at a single point or across a few categories.
- **Why it fails:** Area charts are harder to read for category comparisons than (stacked) bars/columns or split bars [@muth_area_charts_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart reads like a category comparison (“Which category is bigger?”) more than a time story (“How did this change?”).
- **The Test:** State your key question to a colleague; if it’s primarily “compare categories,” you picked the wrong chart type [@muth_area_charts_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a (stacked) bar or column chart, or split bars, if the intent is category comparison [@muth_area_charts_2018].
- **Best Fix:** Reframe the visualization around the intended task: bars/columns for category differences; area/lines for change over time [@muth_area_charts_2018].
