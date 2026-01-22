---
id: avoid-single-bar-plus-difference-overlays-for-finding-extremes-in-source-series
title: Avoid single-bar charts with difference overlays when finding extremes in the
  source series
bibliography: references.bib
description: For identifying extreme values in the source series, single-bar-with-overlays
  reduces accuracy compared to designs that show both series directly.
labels:
- chart:bar
- task:find-extremum
- visual:position
- visual:length
- impact:accuracy
- data:categorical
- audience:novice
- comparison:multi-series
---

## Avoid SB+D for source-series extremes <!-- role: advice -->

Do not use a single bar chart with difference overlays when people need to find the minimum or maximum in the source series. Prefer a design that directly shows the source series (such as a grouped bar chart, with or without difference overlays).

## Why SB+D fails for source-series extremes <!-- role: reason -->

A single-bar-with-overlays design forces viewers to infer the source series rather than read it directly, which increases error for source-series judgments.

**Mechanism:** When the source series is not directly encoded as bars, viewers must mentally reconstruct source values from target values plus overlays, increasing cognitive load and error risk.

**Evidence:** For finding extremes in the source series, the single bar chart with difference overlays ranked worst in accuracy, and it was significantly less accurate than both the grouped bar chart and the grouped bar chart with difference overlays (with large reported effect size for chart design) [@srinivasanWhatsDifferenceEvaluating2018; @zengReviewCollationGraphical2023].

**Notes:** This guideline targets the “source-series extremum” task specifically, not general preference or other tasks.

## When source-series extreme finding applies <!-- role: context -->

- **User Goal:** Identify which category has the minimum or maximum value in the source series.
- **Task:** Find extremum in the source series.
- **Data:** Two-series categorical data where the source series is a meaningful reference (e.g., prior period).
- **Chart Setting:** Static, single-view dashboard comparison.
- **Audience:** People who need quick, reliable source-series judgments.
- **Success Criterion:** Higher correctness in choosing the extreme category in the source series.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The source series is never queried directly (only differences or target values are used). **Why:** The SB+D limitation is specific to tasks requiring accurate source-series extrema.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Showing both series directly (e.g., grouped bars) can consume more visual space and add clutter. **Risk:** If the chart becomes too dense, comparisons may slow down even if accuracy improves. **Mitigation:** Keep the number of categories manageable or provide filtering to reduce density.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using single-bar-with-overlays while expecting users to accurately “read back” source-series values. **Why it fails:** The source series is not directly encoded, so the task becomes indirect and error-prone.

## Quick tests <!-- role: check -->

**Failure Sign:** Readers hesitate or do mental arithmetic when asked “Which category is highest in the source series?” **Quick Check:** Ask a reader to find the source-series maximum without calculating; if they start computing, the encoding is a poor fit. **Stronger Test:** Compare accuracy on the source-extreme task between SB+D and a grouped-bar alternative.

## What to do instead <!-- role: fix -->

- Use a grouped bar chart when source-series values must be read or compared directly.
- Use a grouped bar chart with difference overlays when both source-series extrema and differences are important tasks.
- Provide a separate source-series-only bar chart if showing both series together is too visually complex in the available space.
