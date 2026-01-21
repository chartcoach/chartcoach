---
id: label-the-index-baseline-in-words
title: Label the Index Baseline in Words
bibliography: references.bib
description: Make indexed charts understandable by naming the y-axis baseline in plain
  language, not just with a number.
labels:
- chart:line
- task:explain
- visual:axis
- impact:clarity
- data:temporal
- audience:novice
- concept:index
- source:datawrapper-fix-my-chart
---

## The Rule <!-- role: advice -->

Label the y-axis zero baseline with a verbal description of what “0” represents (e.g., “Employment as of Q3 2023”), not only a numeric tick.

## The Logic <!-- role: reason -->

A named baseline turns an abstract index into a concrete reference point, reducing ambiguity about what values are relative to and preventing readers from inferring the wrong “zero meaning.” This directly addresses confusion about indexed employment values noted in the redesign advice in [@mintzer_y_axis_2024].

- **The Principle:** Anchor abstract quantities to an explicit reference
- **The Evidence:** [@mintzer_y_axis_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand what changes are measured relative to (what “0” means).
- **Data Type:** Indexed or relative measures over time (e.g., differences vs a chosen quarter/year).
- **Audience:** Mainstream/general readers who may not be comfortable with indices.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart is already explicitly non-indexed (absolute units shown) and the baseline is self-evident from the unit (e.g., “% employed” with a standard 0%).
- **Reason:** Adding a verbal baseline label can be redundant and compete with the unit labeling.

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra axis text and visual space.
- **The Risk:** A long baseline description can clutter the axis or collide with ticks/gridlines.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Leaving “0” as a bare number on an indexed chart.
- **Why it fails:** Readers don’t know what the index is anchored to and may misread the chart as showing equal current levels across categories, a confusion highlighted in [@mintzer_y_axis_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** The y-axis shows “0” but nowhere states “0 = [baseline situation/time].”
- **The Test:** Ask a non-expert to explain what “0” means in one sentence; if they can’t, the baseline isn’t labeled clearly.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Rename the zero tick label to “Employment as of Q3 2023” (or your baseline equivalent).
- **Best Fix:** Combine a named zero baseline with consistent y-axis annotations that describe how to interpret values relative to that baseline, as recommended in [@mintzer_y_axis_2024].
