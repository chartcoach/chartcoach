---
id: use-delta-encodings-to-support-efficient-search-for-a-target-relation
title: Use Delta Encodings to Enable Efficient Search for a Target Relation
bibliography: references.bib
description: For tasks that require finding a single pair with an opposite relation,
  encode deltas so search time does not balloon with more pairs.
labels:
- chart:bar
- chart:dot
- chart:slope
- task:search
- task:detect
- visual:length
- visual:position
- visual:orientation
- impact:efficiency
- data:paired
- audience:expert
- source:nothelfer-franconeri-2020
---

## The Rule <!-- role: advice -->

When the task is “find the one pair that goes the other way,” encode each pair as a single signed delta mark (not two separate values).

## The Logic <!-- role: reason -->

Visual search becomes dramatically less set-size dependent when the target is a single-mark feature rather than a relation between two marks.

- **The Principle:** Relational search tends toward serial attention; single-feature targets can be searched more efficiently.
- **The Evidence:** In Experiment 1, delta encodings produced much lower search rates than individual-value encodings; each additional pair added far less time when encoded as deltas, yielding roughly 49–95% improvement depending on visual channel [@nothelferMeasuresBenefitDirect2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Locate an outlier relation (e.g., the only decrease, or the only increase) among many pairs.
- **Data Type:** Many categories with paired values; the display may grow from small to large set sizes.
- **Audience:** Analysts and operational users doing fast anomaly spotting.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is to identify which *absolute* value is highest/lowest, not which pair differs in direction.
- **Reason:** Delta encoding optimizes relation detection, not absolute-value lookup [@nothelferMeasuresBenefitDirect2020a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Base values are not directly visible if you switch to delta-only.
- **The Risk:** If stakeholders need to verify raw values, they may distrust a delta-only view and request additional context [@nothelferMeasuresBenefitDirect2020a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Add more spacing or stronger colors and keep the same two-value-per-pair encoding, hoping it will “pop.”
- **Why it fails:** The bottleneck is extracting the relation itself; spacing doesn’t remove the need to compare two marks per pair [@nothelferMeasuresBenefitDirect2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must repeatedly look back-and-forth within each pair to decide “increase or decrease.”
- **The Test:** Count the number of pairs; if the expected time-to-find scales roughly linearly with more pairs in informal testing, you’re likely relying on inefficient relational search.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a signed delta indicator per pair (above vs. below baseline, or up vs. down orientation).
- **Best Fix:** Replace paired-value marks with a delta-only encoding for this view, since the task is about relation direction [@nothelferMeasuresBenefitDirect2020a].
