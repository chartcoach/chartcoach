---
id: prefer-position-or-length-over-slope-for-pairwise-relation-perception
title: Prefer Position or Length Over Slope for Pairwise Relation Perception
bibliography: references.bib
description: For judging relations between paired values (direction, prevalence, or
  search), use position/length encodings instead of slope/orientation.
labels:
- chart:dot
- chart:bar
- chart:slope
- task:compare
- task:search
- task:aggregate
- visual:position
- visual:length
- visual:orientation
- impact:accuracy
- impact:efficiency
- data:paired
- audience:novice
- audience:expert
- source:nothelfer-franconeri-2020
---

## The Rule <!-- role: advice -->

Use position or length encodings (dot/dash distance from baseline, bar height) rather than slope/orientation when the task is perceiving relations between paired values.

## The Logic <!-- role: reason -->

In these experiments, relation perception degraded most with slope encodings, suggesting that orientation was harder to use for these relation tasks in the tested arrangements.

- **The Principle:** Not all channels support the same efficiency for relational judgments in a given layout.
- **The Evidence:** In Experiments 1 and 2, slope encodings showed worse performance overall than position and length; position/length were not significantly different in those tasks, while slope was significantly worse [@nothelferMeasuresBenefitDirect2020a]. (Experiment 3 included only position and length.)

## Where to Apply <!-- role: context -->

- **User Goal:** Fast identification of relation direction, searching for opposite relations, or judging prevalence of relation types.
- **Data Type:** Paired values arranged in compact, repeated structures (e.g., many side-by-side pairs in rows).
- **Audience:** General use; especially when displays must support quick, glanceable judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The design constraints require slope, or the chart form is inherently slope-based and cannot be changed.
- **Reason:** The paper does not evaluate real-world slope-graph variants; it tests controlled slope encodings in specific row arrangements, so generalization may be limited [@nothelferMeasuresBenefitDirect2020a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose an aesthetic or conventional “trend line” look if replacing slopes with bars/dots.
- **The Risk:** Channel choice interacts with layout; a slope encoding might perform differently under different spatial arrangements than those tested [@nothelferMeasuresBenefitDirect2020a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choose slope encodings assuming they will be as easy to parse as bars/dots for these relation tasks.
- **Why it fails:** In the tested tasks, slope produced poorer accuracy/efficiency, possibly due to how slopes group perceptually when arranged in rows [@nothelferMeasuresBenefitDirect2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers struggle to quickly classify direction (up vs. down) or to find the odd relation when using slopes.
- **The Test:** Swap the slope encoding for a position/length encoding while keeping the data and task constant; if performance subjectively improves immediately, slope is likely the wrong channel for this context.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace slope marks with bars (length) or dashes/dots (position) while keeping the same baseline and ordering.
- **Best Fix:** Use delta encodings with position/length so each pair becomes one easily read mark [@nothelferMeasuresBenefitDirect2020a].
