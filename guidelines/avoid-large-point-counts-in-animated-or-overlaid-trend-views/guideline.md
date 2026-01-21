---
id: avoid-large-point-counts-in-animated-or-overlaid-trend-views
title: Avoid Large Point Counts in Animated or Overlaid Trend Views
bibliography: references.bib
description: Keep animated bubble trends and overlaid traces to modest numbers of
  entities to prevent clutter and tracking failures.
labels:
- chart:scatter
- task:overview
- visual:motion
- impact:clarity
- data:temporal
- audience:general
- constraint:scalability
---

## The Rule <!-- role: advice -->

Do not use animated bubble charts or overlaid trace views when the number of entities produces heavy clutter; reduce the number of entities or change the design.

## The Logic <!-- role: reason -->

As the number of data points rises, motion and overplotting create clutter that makes anomalies hard to observe and makes it difficult to track individual items.

- **The Principle:** Visual crowding undermines tracking and anomaly detection
- **The Evidence:** The paper reports clutter and tracking problems increasing with larger datasets; participants reported difficulty “tracking objects in animation,” and the authors state all three techniques fail to scale beyond about 200 data points [@robertsonEffectivenessAnimationTrend2008].

## Where to Apply <!-- role: context -->

- **User Goal:** Seeing overall movement plus spotting exceptions
- **Data Type:** Many entities moving over time in the same x/y space
- **Audience:** Presentation audiences and analysts

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally aggregate entities into higher-level groups and accept that individual anomalies may be hidden.
- **Reason:** The paper notes aggregation can reduce clutter but may hide anomalies of interest [@robertsonEffectivenessAnimationTrend2008].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may have to omit entities, filter, or redesign to fit the constraint.
- **The Risk:** Filtering or aggregation can remove or hide the very anomalies the user cares about [@robertsonEffectivenessAnimationTrend2008].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more entities and hoping “motion will make patterns pop out.”
- **Why it fails:** Participants reported confusion (“dots flew everywhere”) and losing track of points; clutter rises sharply with dataset size [@robertsonEffectivenessAnimationTrend2008].

## How to Check <!-- role: check -->

- **Visual Sign:** The display looks like a dense cloud/bundle where individual points or traces cannot be followed.
- **The Test:** Ask users to follow one entity for several seconds; if they frequently lose it, the point count is too high for this design [@robertsonEffectivenessAnimationTrend2008].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Filter to fewer entities relevant to the question (or allow selecting a subset and grey out others).
- **Best Fix:** Use small multiples for analysis to remove clutter, or introduce careful aggregation with awareness that anomalies may be hidden [@robertsonEffectivenessAnimationTrend2008].
