---
id: use-data-tables-over-scatter-or-parallel-coordinates-for-value-retrieval
title: Use a Data Table for Value Retrieval Instead of Scatterplots or Parallel Coordinates
bibliography: references.bib
description: Prefer data tables when users must retrieve an exact value given another
  value in multivariate data.
labels:
- chart:table
- chart:scatter
- chart:parallel-coordinates
- task:retrieve-value
- visual:text
- impact:speed
- data:multivariate
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use a data table rather than a scatterplot-based view or a parallel coordinates plot when users need to retrieve an exact value from multivariate data.

## The Logic <!-- role: reason -->

Value retrieval is fundamentally a lookup task; tables support direct cell access, while scatterplots and PCPs require visual tracing and cross-referencing, adding search steps and slowing response time.

- **The Principle:** Direct textual lookup outperforms visual tracing for exact-value retrieval.
- **The Evidence:** In the experiment, value retrieval response time ranked data table fastest, then PCP, then scatterplot (DT > PCP > SP for time), with statistically significant differences between all pairs for time [@kanjanaboseMultitaskComparativeStudy2015]. This finding is captured as recommendation-relevant evidence in the collation review [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Given one attribute value for a specific item, retrieve the corresponding value in another attribute (exact lookup).
- **Data Type:** Multivariate data shown as table vs scatterplot vs PCP (the study used 4 dimensions and 8 items) [@kanjanaboseMultitaskComparativeStudy2015].
- **Audience:** Any audience prioritizing speed and correctness in lookup tasks.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user goal is clustering, anomaly detection, or change detection (pattern-based tasks).
- **Reason:** For those tasks, PCPs (and sometimes scatterplots) outperformed tables in accuracy and/or time in the same study [@kanjanaboseMultitaskComparativeStudy2015], as summarized in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Tables reduce support for rapid perceptual pattern finding across dimensions.
- **The Risk:** Users may miss clusters/outliers/changes if they stay in a table view for tasks that require holistic pattern recognition.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Forcing value retrieval through a PCP by asking users to trace a polyline between axes.
- **Why it fails:** The added tracing and correspondence costs make it slower than direct table lookup; the study’s time results show DT faster than PCP for value retrieval [@kanjanaboseMultitaskComparativeStudy2015].

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate, trace lines/marks repeatedly, or time out while trying to read exact values from a plot.
- **The Test:** Measure time-to-answer on a few lookup questions; if a plot view is consistently slower than a table, switch to table for that step.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide a table view (or table-on-demand) for lookup tasks.
- **Best Fix:** Use a table as the primary representation for value retrieval tasks and use plots only for tasks where pattern detection is the goal.
