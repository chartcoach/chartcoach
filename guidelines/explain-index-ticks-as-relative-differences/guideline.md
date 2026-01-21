---
id: explain-index-ticks-as-relative-differences
title: Explain Index Values as Relative Differences on the Y-axis
bibliography: references.bib
description: Replace bare index ticks with text that explains values as differences
  from the baseline.
labels:
- chart:line
- task:interpret
- visual:axis
- impact:clarity
- data:temporal
- audience:novice
- concept:index
- source:datawrapper-fix-my-chart
---

## The Rule <!-- role: advice -->

Write y-axis tick labels (or key tick labels) as explicit relative statements (e.g., “−5% from 2023”) instead of only showing numbers.

## The Logic <!-- role: reason -->

Indexed charts often fail because readers can’t map numbers to meaning; adding “from [baseline]” ties each tick to the baseline and clarifies direction and magnitude. This is the specific y-axis fix proposed to make the index readable in [@mintzer_y_axis_2024].

- **The Principle:** Make axis semantics explicit at the point of reading
- **The Evidence:** [@mintzer_y_axis_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly interpret what a value represents (how far above/below a reference point).
- **Data Type:** Relative/normalized/indexed metrics (e.g., “difference vs Q3 2023”).
- **Audience:** Readers unfamiliar with index conventions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart needs very dense y-axis ticks (many tick marks) where long text would overlap.
- **Reason:** Full phrases on every tick can harm legibility more than they help; use fewer annotated ticks instead.

## The Price <!-- role: costs -->

- **The Sacrifice:** Less compact axis labeling.
- **The Risk:** Over-labeling can clutter the chart and reduce space for the data.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Explaining the index only in the subtitle/footnote while keeping numeric ticks generic.
- **Why it fails:** Readers primarily decode meaning from the axis during scanning; they may never read the explanatory text, the core issue addressed in [@mintzer_y_axis_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Tick labels are plain numbers (e.g., −5, −10) with no “from baseline” cue.
- **The Test:** Hide the subtitle; if the axis alone no longer tells you what the numbers mean, the ticks need semantic labeling.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add “from [baseline]” to one prominent tick (e.g., “−5% from 2023”) to establish the rule.
- **Best Fix:** Use the y-axis to repeatedly encode the relationship to the baseline (baseline named at 0 plus at least one “from baseline” tick), following the approach in [@mintzer_y_axis_2024].
