---
id: use-delta-encodings-to-improve-average-change-estimates-across-pairs
title: Use Delta Encodings to Improve Average Change Estimates Across Pairs
bibliography: references.bib
description: When users need the average difference across multiple paired comparisons,
  show deltas directly to reduce estimation error.
labels:
- chart:bar
- chart:dot
- task:aggregate
- task:estimate
- visual:length
- visual:position
- impact:accuracy
- data:paired
- audience:expert
- source:nothelfer-franconeri-2020
---

## The Rule <!-- role: advice -->

If the task is to estimate the average delta across multiple paired values, present the deltas directly (one mark per pair) instead of requiring viewers to subtract each pair mentally.

## The Logic <!-- role: reason -->

Averaging is more precise when the input set already consists of the to-be-averaged quantities (deltas) rather than requiring an additional subtraction step per pair before averaging.

- **The Principle:** Remove intermediate computations before ensemble estimation.
- **The Evidence:** In Experiment 3, delta encodings reduced absolute error in average-delta judgments compared to individual-value encodings (about a 25% reduction in error in ensemble trials) [@nothelferMeasuresBenefitDirect2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimate typical/average change across categories (not identify a single pair).
- **Data Type:** Paired measurements across multiple categories; the study used 6 pairs shown briefly.
- **Audience:** Analysts and decision-makers making summary judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must preserve base-value context because average change alone is insufficient for interpretation.
- **Reason:** Delta-only views can hide whether changes came from high baselines or low baselines [@nothelferMeasuresBenefitDirect2020a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Context for absolute levels unless separately shown.
- **The Risk:** Delta encodings may introduce systematic bias in perceived averages; the study observed a tendency to underestimate average delta in many delta-encoding conditions [@nothelferMeasuresBenefitDirect2020a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Show only paired absolute bars/dots and expect accurate “average difference” estimates at a glance.
- **Why it fails:** Users must compute differences before averaging, increasing error relative to directly encoded deltas [@nothelferMeasuresBenefitDirect2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Different viewers give widely different “average change” answers from the same chart.
- **The Test:** Ask multiple users for an average-delta estimate after a brief exposure. High variance (or consistent underestimation) indicates the encoding may be hindering ensemble estimation.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a delta representation per pair so the average is taken over visible deltas.
- **Best Fix:** Provide a dedicated delta-only summary view for estimating average change, and add base values only if required for interpretation [@nothelferMeasuresBenefitDirect2020a].
