---
id: prefer-delta-over-individual-for-direction-judgments-in-sort-like-accuracy-tasks
title: Prefer Delta Encodings for Direction Judgments
bibliography: references.bib
description: For accuracy-focused judgments of which relation holds (increase vs decrease),
  delta encodings outperform individual-value encodings for the same visual channel.
labels:
- chart:bar
- chart:dot
- chart:slope
- task:sort
- visual:length
- visual:position
- visual:orientation
- impact:accuracy
- data:quantitative
- audience:general
- design:deltas
- source:study
---

## The Rule <!-- role: advice -->

For tasks that require deciding which relation holds (e.g., increase vs. decrease) with high accuracy, use delta encodings instead of showing the two individual values.

## The Logic <!-- role: reason -->

Delta encodings turn a relational comparison into a single-value perceptual read, which improves correctness versus extracting the relation from two separate marks.

- **The Principle:** Reduce relation inference by explicitly encoding the relation as a single feature.
- **The Evidence:** For the accuracy metric on the relation-judgment task, delta designs significantly outperformed their corresponding individual-value designs (E-2>E-1, E-4>E-3, E-6>E-5) [@nothelferMeasuresBenefitDirect2020], as captured and organized for visualization recommendation in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly judge the relation direction (increase/decrease) across pairs.
- **Data Type:** Quantitative paired values repeated across categories (nominal on x).
- **Audience:** Broad audiences; any user where correctness matters more than showing both base values.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user must also interpret both original values (not just the delta) for each pair.
- **Reason:** Delta encodings remove the individual values, so the display no longer directly supports absolute-value reading [@nothelferMeasuresBenefitDirect2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Context about which absolute values produced the change.
- **The Risk:** Users may over-focus on differences and miss information tied to the individual values [@nothelferMeasuresBenefitDirect2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Mix delta and individual-value displays without clarifying which one should be used for the task at hand.
- **Why it fails:** If users default to the individual-value view, they lose the measured accuracy advantage of delta encodings for relation judgments [@nothelferMeasuresBenefitDirect2020; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users have to compare “left vs right” marks within each pair to decide direction.
- **The Test:** Ask a user to answer “which direction is more prevalent?”; if they must compare two marks per pair, switch to deltas.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide a toggle to a delta chart for relation-direction questions.
- **Best Fix:** Default to delta encodings when the active task is relation-direction judgment (accuracy-focused) [@nothelferMeasuresBenefitDirect2020; @zengReviewCollationGraphical2023].
