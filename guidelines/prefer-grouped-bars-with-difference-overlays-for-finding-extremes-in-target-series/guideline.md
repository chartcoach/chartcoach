---
id: prefer-grouped-bars-with-difference-overlays-for-finding-extremes-in-target-series
title: Prefer grouped bars with difference overlays to improve accuracy when finding
  extremes in the target series
bibliography: references.bib
description: For identifying minimum/maximum values in the target series, grouped
  bars with difference overlays improve accuracy over a plain grouped bar chart.
labels:
- chart:bar
- task:find-extremum
- visual:position
- visual:length
- visual:color
- impact:accuracy
- data:categorical
- audience:novice
- comparison:multi-series
---

## Prefer difference overlays for target-series extremes <!-- role: advice -->

Use a grouped bar chart with difference overlays when people need to identify the minimum or maximum value in the target series. This improves accuracy compared to a grouped bar chart without overlays.

## Why difference overlays help target-series extremes <!-- role: reason -->

Adding difference overlays supplies an extra visual signal that can help viewers verify which bars are extreme without mentally comparing two adjacent bars per category.

**Mechanism:** Difference overlays add an additional, directly visible comparison cue that can reduce uncertainty when scanning for the most extreme target-series value.

**Evidence:** For finding extremes in the target series, both the grouped bar chart with difference overlays and the single bar chart with difference overlays were more accurate than the grouped bar chart, with statistically significant pairwise differences reported for each overlay design versus the grouped bar chart [@srinivasanWhatsDifferenceEvaluating2018; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about accuracy (not speed) for the target-series extreme-value task.

## When target-series extreme finding applies <!-- role: context -->

- **User Goal:** Identify which category has the minimum or maximum value in the target series.
- **Task:** Find extremum in the target series.
- **Data:** Two-series data by category (e.g., time periods or categories), where a “target” series is compared against a “source” series.
- **Chart Setting:** Static dashboard-like view where comparison must be made within a single chart.
- **Audience:** People with mixed visualization literacy, including casual dashboard readers.
- **Success Criterion:** Higher correctness for selecting the extreme category in the target series.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Only the target series exists (no source series to define a difference). **Why:** Difference overlays require two series to compute and show differences.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Added visual elements increase chart complexity. **Risk:** Viewers may misinterpret overlays as another data series if the encoding is not clearly differentiated. **Mitigation:** Ensure overlays are clearly distinct from bars as a separate mark type.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding difference overlays but styling them so similarly to bars that they look like a second bar series. **Why it fails:** The overlay no longer acts as a distinct comparison cue and can increase confusion.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers confuse the overlay mark with the bar encoding or report uncertainty about what the overlay means. **Quick Check:** Ask a reader to explain what the overlay represents in one sentence and then find the target-series maximum. **Stronger Test:** Run a small timed correctness check comparing grouped bars versus grouped bars with overlays for the target-extreme task.

## What to do instead <!-- role: fix -->

- Use a plain grouped bar chart when there is no valid or meaningful difference to compute between two series.
- Use a difference-only chart when the only goal is to read differences and original values are not needed.
- Provide a separate view of the target series alone if overlays are visually overwhelming in a dense dashboard layout.
