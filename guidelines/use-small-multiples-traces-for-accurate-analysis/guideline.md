---
id: use-small-multiples-traces-for-accurate-analysis
title: Use Small-Multiples Traces for Accurate Trend Analysis
bibliography: references.bib
description: Use small multiples of per-item traces to reduce errors and speed up
  multi-dimensional trend analysis.
labels:
- chart:small-multiples
- task:detect-anomaly
- visual:position
- impact:accuracy
- data:temporal
- audience:expert
- method:trace-lines
---

## The Rule <!-- role: advice -->

For analysis tasks on multi-dimensional trends, show one trace per entity in a small-multiples grid instead of animating all entities together.

## The Logic <!-- role: reason -->

Separating each entity’s history removes clutter and occlusion, making anomalies easier to spot without replaying time. This improved accuracy and reduced time compared to animation.

- **The Principle:** Clutter reduction improves anomaly detection
- **The Evidence:** Small multiples were significantly more accurate than animation overall, and in analysis they were significantly faster than animation [@robertsonEffectivenessAnimationTrend2008].

## Where to Apply <!-- role: context -->

- **User Goal:** Finding outliers, counter-trends, reversals, or unusual trajectories
- **Data Type:** Many entities with time-varying x/y values (and optionally size), where trajectories matter
- **Audience:** Analysts/explorers working interactively

## When to Break It <!-- role: exceptions -->

- **Scenario:** The core task is to follow interactions among many entities in the same shared coordinate space (e.g., global convergence patterns) rather than per-entity inspection.
- **Reason:** Small multiples require scanning many panels, which can slow holistic comparisons across all items at once [@robertsonEffectivenessAnimationTrend2008].

## The Price <!-- role: costs -->

- **The Sacrifice:** Users must scan across many panels (a more serial process).
- **The Risk:** As the number of entities grows, each panel becomes too small to read effectively, limiting scalability [@robertsonEffectivenessAnimationTrend2008].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping everything in one animated view and asking users to “just watch carefully.”
- **Why it fails:** Users report losing track of moving points, and analysis time increases due to replay [@robertsonEffectivenessAnimationTrend2008].

## How to Check <!-- role: check -->

- **Visual Sign:** In a combined view, paths overlap heavily and anomalies are hard to isolate.
- **The Test:** Ask users to find a counter-trend; if they miss it or need multiple replays, switch to small multiples [@robertsonEffectivenessAnimationTrend2008].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a small-multiples mode that shows each entity’s trace separately with shared axes.
- **Best Fix:** Group and order panels meaningfully (e.g., by region/category) to support systematic scanning, as done in the paper’s small-multiples design [@robertsonEffectivenessAnimationTrend2008].
