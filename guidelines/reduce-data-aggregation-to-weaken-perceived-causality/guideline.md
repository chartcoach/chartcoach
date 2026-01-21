---
id: reduce-data-aggregation-to-weaken-perceived-causality
title: Reduce Data Aggregation to Weaken Perceived Causality
bibliography: references.bib
description: Avoid heavy binning/averaging when your goal is to prevent correlation-from-looking-like-causation.
labels:
- task:interpret
- impact:clarity
- data:bivariate
- custom:aggregation
- risk:causality
- audience:novice
---

## The Rule <!-- role: advice -->

If you want to avoid prompting causal conclusions, reduce aggregation: show more bins/groups or show unaggregated values rather than collapsing data into a few group averages.

## The Logic <!-- role: reason -->

- **The Principle:** Aggregation simplifies patterns into coarse contrasts that invite stronger causal narratives.
- **The Evidence:** In Experiment 2, higher aggregation (fewer bins, e.g., 2 groups) increased causation ratings compared to less aggregation (more bins, e.g., 16 groups) across encoding types, with a large main effect of aggregation level on perceived causality [@xiongIllusionCausalityVisualized2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Assess association strength without inferring intervention effects.
- **Data Type:** Continuous/ordered X and Y where binning into a few groups is optional.
- **Audience:** Viewers making quick judgments from media-style summaries.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must communicate a high-level summary and the audience cannot process finer-grained displays.
- **Reason:** Reduced aggregation can lower immediate interpretability; the paper’s focus is on causal misinterpretation, not on summarization needs [@xiongIllusionCausalityVisualized2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Simplicity and fast “headline” comparability.
- **The Risk:** More detailed displays can feel noisier and may reduce perceived strength/clarity of the relationship.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the same two-group aggregation but changing only the mark type (e.g., bars → dots).
- **Why it fails:** Aggregation itself strongly drives causality impressions; mark changes alone may not counteract the causal cue from coarse grouping [@xiongIllusionCausalityVisualized2020].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart reads like a simple “Group A vs Group B” contrast rather than a distribution/relationship.
- **The Test:** Count the number of groups/bins shown; if it’s very small relative to the data, you are in the high-aggregation regime associated with higher causality ratings [@xiongIllusionCausalityVisualized2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase the number of bins/groups (e.g., from 2 to 8 or 16).
- **Best Fix:** Show unaggregated (or minimally aggregated) observations so viewers see variability rather than only group averages [@xiongIllusionCausalityVisualized2020].
