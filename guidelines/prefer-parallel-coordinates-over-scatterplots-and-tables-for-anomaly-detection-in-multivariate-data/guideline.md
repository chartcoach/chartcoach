---
id: prefer-parallel-coordinates-over-scatterplots-and-tables-for-anomaly-detection-in-multivariate-data
title: Prefer parallel coordinates over scatterplots and tables for anomaly detection
  in multivariate data
bibliography: references.bib
description: For finding outliers/anomalies in multivariate data, parallel coordinates
  improved accuracy over scatterplots and tables.
labels:
- chart:parallel-coordinates
- chart:scatter
- chart:table
- task:find-anomalies
- visual:position
- impact:accuracy
- impact:speed
- data:multivariate
- data:quantitative
- audience:general
- complexity:intermediate
---

## Use parallel coordinates to find anomalies more accurately <!-- role: advice -->

Use a parallel coordinates plot when users must identify outliers or anomalies in multivariate data. Prefer it over scatterplots and data tables to improve anomaly-detection accuracy.

## Why parallel coordinates support multivariate outlier judgments <!-- role: reason -->

Outliers in multivariate data can emerge from unusual combinations across several attributes. Parallel coordinates show each record across all dimensions simultaneously, making unusual profiles easier to compare against the rest than scanning a table or reconciling multiple pairwise scatter views.

**Mechanism:** A single polyline per record enables holistic comparison across axes, supporting detection of unusual shapes or deviations across multiple dimensions.

**Evidence:** For the find-anomalies task, accuracy ranked parallel coordinates highest, then scatterplots, then data tables, and all pairwise differences were marked significant in the extracted results [@kanjanaboseMultitaskComparativeStudy2015]. The same outcome is part of a broader collation aimed at turning perception evidence into recommendation constraints and rules [@zengReviewCollationGraphical2023].

**Notes:** For time on find-anomalies, parallel coordinates and scatterplots were grouped together as faster than tables in the extracted ranking.

## When anomaly detection is the goal <!-- role: context -->

- **User Goal:** Identify the record(s) that are unusual relative to others across multiple variables.
- **Task:** find-anomalies.
- **Data:** Multivariate quantitative datasets where anomalies may not be visible in any single bivariate projection.
- **Chart Setting:** Static, single-question or short diagnostic workflow.
- **Audience:** General audiences; may include mixed familiarity with parallel coordinates.
- **Success Criterion:** Higher accuracy (and optionally faster completion compared to tables).

## When not to use parallel coordinates for anomalies <!-- role: exceptions -->

**Break it when:** The primary task is exact value lookup under time pressure. **Why:** Tables were fastest for value retrieval compared with both scatterplots and parallel coordinates in the same evidence base.

## Tradeoffs of parallel coordinates for anomaly detection <!-- role: costs -->

**Sacrifice:** Some viewers may require acclimation to reading polylines across axes.\
**Risk:** If many lines overlap, the display can become difficult to parse, undermining anomaly visibility.\
**Mitigation:** Ensure the display remains readable for the expected number of records in the task.

## Common failure modes in anomaly displays <!-- role: mistakes -->

**Mistake:** Relying on a data table alone to find outliers in multivariate data. **Why it fails:** It had the lowest accuracy and was slowest compared with scatterplots and parallel coordinates for anomaly finding.

## Quick tests for anomaly-readiness <!-- role: check -->

**Failure Sign:** Users can’t justify why a record is anomalous without repeatedly cross-checking many attributes.\
**Quick Check:** If anomalies depend on multi-attribute profiles, test a parallel coordinates view first.\
**Stronger Test:** Have users find anomalies under a time limit across candidate charts and compare accuracy.

## What to do instead when parallel coordinates are not an option <!-- role: fix -->

- Use scatterplots as the next-best option when you can’t present parallel coordinates.
- Provide a table as a secondary view for confirming exact values once a potential anomaly is spotted.
- Reduce the number of simultaneously considered attributes to those most relevant to the anomaly definition.
- Add interactive selection/highlighting so a suspected anomalous record can be traced consistently across views.
