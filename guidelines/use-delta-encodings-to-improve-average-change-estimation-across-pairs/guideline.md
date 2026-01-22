---
id: use-delta-encodings-to-improve-average-change-estimation-across-pairs
title: Use Delta Encodings to Improve Average-Change Estimation Across Paired Values
bibliography: references.bib
description: When users must estimate the average magnitude of change across multiple
  paired comparisons, delta encodings reduce estimation error.
labels:
- chart:bar
- chart:dot
- task:aggregate
- task:estimate
- visual:length
- visual:position
- impact:accuracy
- data:paired
- audience:novice
- audience:expert
- custom:ensemble-coding
---

## Show deltas directly when users estimate the mean change <!-- role: advice -->

When the user must estimate the average difference across multiple paired values, encode each pair as a delta value rather than forcing viewers to subtract two values per pair before averaging.

## Why direct deltas reduce average-estimation error <!-- role: reason -->

Estimating an average delta from individual values requires two steps: extracting a delta for each pair and then combining them into a mean, which compounds perceptual and memory error. Delta encodings remove the first step by presenting the delta explicitly for each pair, improving the precision of the ensemble summary.

**Mechanism:** Reducing multi-step computations (derive each delta, then average) lowers accumulated error in ensemble coding of relation magnitudes.

**Evidence:** In brief displays of six pairs, mean absolute error in estimating the average delta was significantly lower with delta encodings than with individual-value encodings, with about a 25% reduction in error. [@nothelferMeasuresBenefitDirect2020a]

**Notes:** Responses showed a tendency to underestimate in many conditions, including in delta-encoding conditions.

## When this applies in “average change” questions <!-- role: context -->

- **User Goal:** Estimate typical or average change between two conditions across categories.
- **Task:** Ensemble estimate of the mean delta magnitude over multiple pairs.
- **Data:** Paired comparisons with varying delta magnitudes; relation direction may be consistent within a view.
- **Chart Setting:** Single-glance or time-limited assessment; summary panels.
- **Audience:** Any; especially when numeric precision is not required but directional magnitude matters.
- **Success Criterion:** Lower absolute error in average-change estimation.

## When to break this rule <!-- role: exceptions -->

**Break it when:** The analysis requires connecting deltas back to constraints on the original values (e.g., “average delta only for pairs above a value threshold”). **Why:** Delta-only views do not preserve the necessary original-value context.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Immediate visibility of the original paired values.\
**Risk:** Viewers may systematically bias estimates (e.g., underestimation) depending on task and response method.\
**Mitigation:** Treat the delta view as a summary layer and keep the base values accessible when calibration matters.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Asking for an average change from a chart that only encodes the two raw values per pair. **Why it fails:** Users must infer each delta before averaging, increasing error.\
**Mistake:** Assuming delta encoding eliminates bias in mean judgments. **Why it fails:** Systematic underestimation was observed even when deltas were directly encoded.

## Quick tests <!-- role: check -->

**Failure Sign:** Users’ average-change estimates vary widely or drift systematically low.\
**Quick Check:** Ask multiple users to estimate the average change from the same display and compare spread across encodings.\
**Stronger Test:** Measure absolute error against known deltas for both individual-value and delta encodings using a short lab-style task.

## What to do instead <!-- role: fix -->

- Provide a delta-encoded summary view specifically for average-change estimation tasks.
- Add a control or calibration element (e.g., a known reference delta) when users must estimate mean deltas quickly.
- Reduce the number of pairs shown simultaneously if you must use individual-value encodings.
- Provide separate panels for “average change” and “absolute levels” so users do not have to choose one at the expense of the other.
