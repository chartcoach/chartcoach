---
id: map-summary-statistics-to-color-not-position-when-the-task-is-mean-or-variance-estimation
title: Map mean and variance judgments to color encodings rather than position encodings
  (when summarizing time-series values)
bibliography: references.bib
description: Color encodings can support more accurate mean and variance extraction
  than position encodings in time-series aggregation tasks.
labels:
- chart:time-series
- task:summarize
- visual:color
- impact:accuracy
- data:temporal
- audience:general
- complexity:intermediate
---

## Use color for mean/variance summaries in time-series displays <!-- role: advice -->

Map values to color when you expect viewers to estimate mean or variance over a set of time-series values. Use positional encodings for other tasks that require pinpointing specific extrema.

## Why color can outperform position for mean/variance summaries <!-- role: reason -->

When values are encoded in color, viewers can more readily integrate many samples into an overall impression of the distribution, supporting aggregate judgments like mean and variance.

**Mechanism:** Color supports efficient pooling of distributed values into an ensemble-style summary representation, which can favor aggregate estimation over reading off individual points.

**Evidence:** In aggregation tasks on time-series visualizations, mean and variance were estimated more accurately from color encodings than from positional encodings, while the opposite pattern held for extrema and range [@szafirFourTypesEnsemble2016a].

**Notes:** This guideline targets summary judgments over many marks, not precise retrieval of single values.

## When you should apply this mapping choice <!-- role: context -->

- **User Goal:** Rapidly understand “typical value” and “stability/variability” over a series or subset of series.
- **Task:** Estimate or compare mean and variance across groups or time windows.
- **Data:** Temporal series with enough samples that reading individual points is inefficient.
- **Chart Setting:** Static or lightly interactive time-series summaries; multiple series or small multiples.
- **Audience:** Mixed audiences, including analysts who want quick distributional insight.
- **Success Criterion:** Higher accuracy and speed for mean/variance judgments.

## When not to follow this guideline <!-- role: exceptions -->

- **Break it when:** The primary question is “what is the minimum/maximum?” or “what is the range?” **Why:** Positional encodings better support identification of extrema and range in these tasks.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Viewers may lose the ability to precisely read individual values when color replaces position. **Risk:** If viewers attempt single-value lookup from color, their estimates can be less precise than position-based reads. **Mitigation:** Ensure the workflow does not require precise per-point readout for the same encoded dimension.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using color for tasks that require finding minima/maxima or exact ranges. **Why it fails:** Viewers are less accurate at extracting extrema/range from color compared with position in the studied time-series aggregation setting.

## Quick tests <!-- role: check -->

**Failure Sign:** People disagree on which time window has the greatest variability or which group has the higher average even when differences are substantial. **Quick Check:** Ask a colleague to answer mean/variance questions from the display in a few seconds and compare answers across people. **Stronger Test:** Run a small task-based evaluation comparing a color-encoded vs position-encoded variant for mean/variance questions.

## What to do instead when this fails <!-- role: fix -->

- Use positional encodings for the dimensions where viewers must identify extrema or estimate range.
- Separate tasks across coordinated views, using color for summary judgments and position for identification judgments.
- Provide interactive subset selection so viewers can compute summaries over chosen subsets without relying on precise single-point reads.
