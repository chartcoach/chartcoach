---
id: prefer-data-tables-for-fast-multivariate-value-retrieval-over-scatterplots-or-parallel-coordinates
title: Prefer data tables for faster multivariate value retrieval over scatterplots
  or parallel coordinates
bibliography: references.bib
description: For reading an exact value given another value in multivariate data,
  use a data table to minimize response time.
labels:
- chart:table
- chart:scatter
- chart:parallel-coordinates
- task:retrieve-value
- visual:position
- impact:speed
- data:quantitative
- audience:general
- complexity:basic
---

## Use a data table for value lookups across attributes <!-- role: advice -->

Use a data table when users must look up an exact value in one attribute given a value in another attribute. Avoid using a scatterplot or a parallel coordinates plot for this specific lookup task if speed is the priority.

## Why tables speed up cross-attribute value lookup <!-- role: reason -->

This task is a targeted lookup: users must locate a specific record and then read a corresponding cell. A table supports direct row/column search and exact reading, while the visual forms add extra steps (tracing marks/lines across views or axes) that slow the lookup.

**Mechanism:** Tables provide a direct, discrete mapping from attribute-to-cell, reducing tracing and cross-panel integration.

**Evidence:** Response time for value retrieval was fastest with the data table, slower with parallel coordinates, and slowest with scatterplots, with significant differences among all three representations [@kanjanaboseMultitaskComparativeStudy2015]. This task-specific comparative result is included as collated evidence for visualization recommendation scenarios [@zengReviewCollationGraphical2023].

**Notes:** This guideline targets speed; accuracy differences for value retrieval were not distinguished between representations in the extracted ranking.

## When value lookup is the primary goal <!-- role: context -->

- **User Goal:** Read an exact value for one variable given a known value in another variable.
- **Task:** retrieve-value.
- **Data:** Multivariate quantitative data with identifiable records (e.g., rows), where exact values matter.
- **Chart Setting:** Static display where the user answers a single lookup question quickly.
- **Audience:** General audiences, including people not trained on parallel coordinates.
- **Success Criterion:** Faster completion time for the lookup.

## When not to follow the table-first rule <!-- role: exceptions -->

**Break it when:** Users primarily need pattern-based judgments (e.g., cluster membership, anomaly detection, or change detection) rather than exact value lookup. **Why:** Those tasks were better supported by parallel coordinates (and sometimes scatterplots) than tables in the same evidence base.

## Tradeoffs when using tables for lookup <!-- role: costs -->

**Sacrifice:** Tables reduce immediate visibility of geometric patterns across dimensions.\
**Risk:** Users may miss clusters or anomalies while focusing on exact lookup.\
**Mitigation:** Keep the table scoped to lookup workflows, not exploratory pattern finding.

## Common failure modes for lookup tasks <!-- role: mistakes -->

**Mistake:** Forcing users to perform exact value lookups in scatterplots or parallel coordinates without a tabular fallback. **Why it fails:** It increases time due to tracing and cross-view integration compared to direct table reading.

## Quick tests for choosing a table <!-- role: check -->

**Failure Sign:** Users spend noticeable time tracing lines/marks to match identity before reading the requested value.\
**Quick Check:** If the question can be phrased as “when A = x, what is B?”, default to a table view.\
**Stronger Test:** Time a small pilot of the lookup question in both a table and the intended chart and compare median completion times.

## What to do instead if a table is unavailable <!-- role: fix -->

- Add a table view specifically for value lookup tasks.
- Provide a direct “details-on-demand” readout that returns exact values for the selected record and attribute.
- Reduce the need for cross-attribute lookup by precomputing and showing the requested attribute alongside the given one in the same view.
- Switch the workflow so scatterplots/parallel coordinates are used for pattern tasks, while tables handle exact reading.
