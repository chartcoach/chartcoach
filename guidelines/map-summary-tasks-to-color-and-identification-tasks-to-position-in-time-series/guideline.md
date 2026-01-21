---
id: map-summary-tasks-to-color-and-identification-tasks-to-position-in-time-series
title: Map Summary Tasks to Color and Identification Tasks to Position
bibliography: references.bib
description: Choose color encodings to support mean/variance judgments and positional
  encodings to support extrema/range judgments in time series.
labels:
- chart:time-series
- task:summarize
- task:identify
- visual:color
- visual:position
- impact:accuracy
- data:temporal
- audience:general
---

## The Rule <!-- role: advice -->

When your primary task is estimating mean or variance, encode values with color; when your primary task is finding extrema or range, encode values with position.

## The Logic <!-- role: reason -->

- **The Principle:** Different visual channels favor different ensemble vs. boundary-based judgments.
- **The Evidence:** A task-driven evaluation of time-series aggregation found mean/variance judgments were more accurate with color encodings, while extrema/range judgments were more accurate with positional encodings, as summarized in [@szafirFourTypesEnsemble2016a].

## Where to Apply <!-- role: context -->

- **User Goal:** Either (a) summarize behavior (mean/variance) or (b) identify extremes (min/max, range) in temporal data.
- **Data Type:** Time series (including aggregated or dense series) where the viewer must visually judge statistics rather than read precise values.
- **Audience:** Analysts scanning many series or many time windows.

## When to Break It <!-- role: exceptions -->

- **Scenario:** When the user must read precise individual values rather than estimate statistics.
- **Reason:** The paper’s described trade-off is about statistical judgments (summary vs. identification) rather than precise point reading [@szafirFourTypesEnsemble2016a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Optimizing for one class of tasks can degrade performance on the other.
- **The Risk:** A color-based design that helps summaries may make it harder for users to reliably spot exact peaks/troughs; a position-based design that helps extrema may make average/variability harder to judge at a glance [@szafirFourTypesEnsemble2016a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a single encoding (only color or only position) and assuming it supports all statistical tasks equally well.
- **Why it fails:** The surveyed results show a clear trade-off: summary tasks and identification tasks do not peak on the same channel [@szafirFourTypesEnsemble2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users accurately find peaks but disagree on “typical value,” or vice versa.
- **The Test:** Run two quick prompts on the same display—“Which window is more variable?” and “Where is the maximum?”—and see if one consistently fails under your chosen encoding [@szafirFourTypesEnsemble2016a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the encoding to match the dominant task (color for summary, position for extrema).
- **Best Fix:** Provide coordinated views or layered encodings where one view prioritizes summary (color-based) and another prioritizes identification (position-based) [@szafirFourTypesEnsemble2016a].
