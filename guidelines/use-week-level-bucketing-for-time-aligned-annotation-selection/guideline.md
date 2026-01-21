---
id: use-week-level-bucketing-for-time-aligned-annotation-selection
title: Aggregate Time into Weekly Buckets for Annotation Selection
bibliography: references.bib
description: Choose annotation moments using weekly aggregation to align news events
  and time-series behavior at a readable granularity.
labels:
- chart:line
- task:summarize
- visual:annotation
- impact:readability
- data:temporal
- audience:general
- domain:finance
---

## The Rule <!-- role: advice -->

Aggregate both candidate annotations and time-series salience signals into weekly buckets before selecting which moments to annotate.

## The Logic <!-- role: reason -->

Weekly aggregation reduces volatility/noise in day-level signals and produces a manageable set of candidate time windows that fit the spatial constraints of annotated charts, while maintaining alignment between dated text and chart behavior.

- **The Principle:** Temporal aggregation supports concise selection under limited annotation space.
- **The Evidence:** Contextifier clusters articles and salience measures by week, computes weekly averages, and then selects a small number of top weeks to annotate to satisfy concision and usability constraints in an embedded visualization [@hullmanContextifierAutomaticGeneration2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly scan a time series with a small number of contextual callouts.
- **Data Type:** Daily time series with many possible annotation candidates (e.g., daily stock prices and daily news).
- **Audience:** Readers interacting briefly with an embedded chart.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The key events and the chart response are known to be intraday or tightly tied to specific dates (e.g., a single-day shock).
- **Reason:** Weekly aggregation can blur the event-to-effect mapping and hide precise timing [@hullmanContextifierAutomaticGeneration2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less temporal precision in annotations.
- **The Risk:** Users may attribute an effect to the wrong day within the week or miss fast event dynamics.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Mixing daily annotations with weekly salience ranking (or vice versa).
- **Why it fails:** Inconsistent granularity makes it unclear why some annotations appear and can misalign text with plotted changes.

## How to Check <!-- role: check -->

- **Visual Sign:** Annotation dates appear overly dense or inconsistent, or multiple annotations land in the same narrow time span.
- **The Test:** Count the number of distinct time windows being annotated; if it exceeds what the layout comfortably supports, increase aggregation.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert annotation selection to “top N weeks” rather than “top N days.”
- **Best Fix:** Keep weekly selection, but display an annotation’s specific date within that week while maintaining week-level ranking and spacing [@hullmanContextifierAutomaticGeneration2013].
