---
id: directly-encode-pairwise-deltas-for-relation-judgments
title: Directly Encode Pairwise Deltas for Relation Judgments
bibliography: references.bib
description: When users need to judge increases/decreases or differences between paired
  values, explicitly encode the delta rather than forcing pairwise comparison of absolute
  values.
labels:
- chart:bar
- chart:dot
- chart:slope
- task:compare
- task:search
- task:aggregate
- visual:length
- visual:position
- visual:orientation
- impact:clarity
- impact:efficiency
- data:paired
- audience:novice
- audience:expert
- source:nothelfer-franconeri-2020
---

## The Rule <!-- role: advice -->

Directly encode the difference (delta) between each pair of data values when the user’s task is to perceive pairwise relations (increase vs. decrease, or magnitude of change).

## The Logic <!-- role: reason -->

Direct delta encodings turn a two-mark relation judgment into a single-mark feature judgment, reducing the need for serial, attention-demanding relational extraction.

- **The Principle:** Single-feature decoding is more efficient than extracting relations between separate objects.
- **The Evidence:** Across visual search for a target relation, proportion judgments of relation direction, and average-delta estimation, delta encodings consistently outperformed individual-value encodings, with improvements ranging from ~25% to ~95% depending on task [@nothelferMeasuresBenefitDirect2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Detect which pairs increased/decreased; find an anomalous pair; decide which relation direction is more prevalent; estimate average change across pairs.
- **Data Type:** Naturally paired measurements (before/after, group A vs. group B per category) where the *difference* is the primary analytic object.
- **Audience:** Any audience; especially useful when time/attention is limited and displays include many pairs.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user must reason about the original absolute values (e.g., apply thresholds on the raw values, or interpret deltas in the context of base magnitude).
- **Reason:** Delta-only displays remove value context and can hide insights tied to the individual data points [@nothelferMeasuresBenefitDirect2020a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Loss of context for base values; reduced ability to spot patterns in the original series.
- **The Risk:** If you show only deltas, viewers may misinterpret changes without knowing starting levels; adding deltas can increase layout complexity and space usage [@nothelferMeasuresBenefitDirect2020a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assume viewers can “just compare the pairs” in a grouped bar/dot display when the real question is change direction or change amount.
- **Why it fails:** Pairwise relation perception from individual values is highly inefficient and scales poorly as the number of pairs increases [@nothelferMeasuresBenefitDirect2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** The display shows two marks per category, but the intended takeaway is “up vs. down” or “how much change.”
- **The Test:** Ask a reviewer to answer “which pairs decreased?” quickly without tracing each pair; if they must scan pair-by-pair, you’re relying on inefficient relational extraction.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a delta layer/mark per pair (a single bar/dash/line encoding signed difference).
- **Best Fix:** Make delta the primary encoding for the task (a dedicated delta chart), and only add base values if the task explicitly needs them [@nothelferMeasuresBenefitDirect2020a].
