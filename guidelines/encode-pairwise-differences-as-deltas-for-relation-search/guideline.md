---
id: encode-pairwise-differences-as-deltas-for-relation-search
title: Encode Pairwise Differences as Deltas for Relation Search
bibliography: references.bib
description: When users must find a specific relationship among many value pairs,
  directly encode the difference (delta) rather than two separate values.
labels:
- chart:bar
- chart:dot
- chart:slope
- task:filter
- visual:length
- visual:position
- visual:orientation
- impact:speed
- data:quantitative
- audience:general
- design:deltas
- source:study
---

## The Rule <!-- role: advice -->

When users need to find a specific “increase vs. decrease” relationship among many paired values, show each pair as a single delta mark rather than two separate value marks.

## The Logic <!-- role: reason -->

Direct delta encodings reduce a two-mark relationship judgment into a single-mark feature judgment, improving visual processing efficiency for relation search.

- **The Principle:** Reduce relational extraction by collapsing pairs into single perceptual units.
- **The Evidence:** Delta charts were faster than individual-value charts for the filter/search task across position, length, and slope encodings [@nothelferMeasuresBenefitDirect2020], as collated for recommendation use in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Filter/search for a target relation among many pairs (e.g., “find the one decrease among increases”).
- **Data Type:** Quantitative paired comparisons (two values per category/instance).
- **Audience:** General audiences or analysts doing rapid scanning.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task requires reading or comparing the original absolute values for each member of the pair.
- **Reason:** A delta-only display removes the underlying value context (the study contrasts delta vs. individual-value depictions; the delta depiction omits the original values) [@nothelferMeasuresBenefitDirect2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Loss of base-value context for each pair.
- **The Risk:** Viewers may be unable to answer questions about absolute levels, even if they can find the direction/magnitude of change well [@nothelferMeasuresBenefitDirect2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keep only the two original values and expect users to “just compare them.”
- **Why it fails:** Relation search from two separate values is substantially slower than when the delta is directly encoded [@nothelferMeasuresBenefitDirect2020; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers must repeatedly compare two marks per category to decide increase/decrease.
- **The Test:** Count the “mental steps”: if each pair requires looking back-and-forth between two marks to determine the relation, you are not using a delta encoding.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a delta-only version of the view for relation-search moments.
- **Best Fix:** Replace the paired-value depiction with a delta chart (one mark per pair) during filter/search tasks [@nothelferMeasuresBenefitDirect2020; @zengReviewCollationGraphical2023].
