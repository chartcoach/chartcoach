---
id: repeat-all-series-as-faint-background-lines-to-enable-cross-panel-comparison
title: Add Faint Background Lines to Enable Cross-Panel Comparisons
bibliography: references.bib
description: Repeat all series as muted background lines in each panel so readers
  can compare ranks at the same time point.
labels:
- chart:line
- task:compare
- visual:layering
- impact:clarity
- data:temporal
- audience:general
- chart:small-multiples
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

In small multiple line charts, repeat all lines as faint background lines in every panel to support cross-panel comparison at the same dates.

## The Logic <!-- role: reason -->

Small multiples hinder point-in-time comparisons across categories because each series is isolated; adding all series as a subdued reference layer provides context for relative ranking without reintroducing full clutter [@muth_small_multiple_line_charts_2024].

- **The Principle:** Provide contextual reference without overpowering the focus
- **The Evidence:** [@muth_small_multiple_line_charts_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare categories’ relative positions at the same time point while still benefiting from faceting
- **Data Type:** Multiple time series displayed as one series per panel
- **Audience:** General readers who want both trend readability and some comparative context

## When to Break It <!-- role: exceptions -->

- **Scenario:** There are so many series that even faint background lines create heavy noise.
- **Reason:** The reference layer can become clutter and defeat the purpose of small multiples [@muth_small_multiple_line_charts_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** More visual elements per panel; slightly higher complexity.
- **The Risk:** If background lines are not muted enough, they compete with the main line and reduce focus [@muth_small_multiple_line_charts_2024].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Repeating all lines at normal weight/contrast.
- **Why it fails:** Recreates the original multi-line clutter inside every panel [@muth_small_multiple_line_charts_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** The main (foreground) line doesn’t stand out immediately within each panel.
- **The Test:** Glance at each panel for one second; if you can’t instantly tell which line is the featured one, the background layer is too strong [@muth_small_multiple_line_charts_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce opacity/contrast of repeated lines so they read as background context.
- **Best Fix:** Keep one prominent line per panel and all other series as clearly muted references to allow ranking context without clutter [@muth_small_multiple_line_charts_2024].
