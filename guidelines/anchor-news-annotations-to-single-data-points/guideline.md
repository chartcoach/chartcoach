---
id: anchor-news-annotations-to-single-data-points
title: Anchor Annotations to Single Data Points by Default
bibliography: references.bib
description: Attach annotations to specific points in the chart (e.g., a date on a
  time series) rather than broad regions, unless you have a clear reason not to.
labels:
- chart:line
- task:annotate
- visual:position
- impact:clarity
- data:temporal
- audience:general
- domain:journalism
---

## The Rule <!-- role: advice -->

Anchor annotations to single, specific data points (e.g., individual dates) as the default strategy.

## The Logic <!-- role: reason -->

Point-anchored callouts provide precise reference, reducing ambiguity about what the text refers to; professional narrative graphics frequently use point anchoring, suggesting it is a robust convention for quick comprehension.

- **The Principle:** Precise anchoring reduces referential ambiguity in narrative charts.
- **The Evidence:** In a sample of 136 professional news visualizations, single-datum anchoring was the most prevalent anchor type (74.3%), exceeding group/region (50.0%) and entire-view anchoring (35.3%) [@hullmanContextifierAutomaticGeneration2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Understand “what happened here?” at a particular moment in a time series.
- **Data Type:** Time series where external events can be assigned a date/week (e.g., stock closing price).
- **Audience:** Readers skimming for key moments rather than performing extended analysis.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The annotation describes a sustained period (e.g., a multi-week trend) rather than a moment.
- **Reason:** For period-based phenomena, region/group anchoring may better match the semantics than forcing a single-point reference [@hullmanContextifierAutomaticGeneration2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some narratives that are inherently interval-based may be oversimplified.
- **The Risk:** Users may infer that a multi-day event occurred on one exact day because the annotation is pinned to a single point.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Pinning annotations to arbitrary points just to “fit” them on the chart.
- **Why it fails:** It creates misleading referents and weakens trust in the annotation-to-data mapping [@hullmanContextifierAutomaticGeneration2013].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers can’t tell which point the text refers to (e.g., callout appears between points or could apply to multiple features).
- **The Test:** Hover/selection test: ensure each annotation highlights exactly one point in the series (or one clearly designated time bucket).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Snap each annotation to the nearest explicit time point (e.g., end-of-week).
- **Best Fix:** If the underlying event is interval-based, switch that specific annotation to a region/group anchor rather than forcing a single point [@hullmanContextifierAutomaticGeneration2013].
