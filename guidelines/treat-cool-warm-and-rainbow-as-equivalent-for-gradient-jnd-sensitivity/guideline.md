---
id: treat-cool-warm-and-rainbow-as-equivalent-for-gradient-jnd-sensitivity
title: Treat cool-warm and rainbow as equivalent choices for JND sensitivity in gradient
  comparison
bibliography: references.bib
description: In average-gradient comparison, cool-warm and rainbow achieve similar
  JND thresholds with no significant difference between them.
labels:
- chart:heatmap
- task:compare
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- metric:jnd
- domain:scalar-field
---

## Treat cool-warm and rainbow as interchangeable for JND-driven gradient comparison <!-- role: advice -->

When optimizing for lower JND in average-gradient comparisons between two color-coded scalar fields, consider cool-warm and rainbow as interchangeable choices because neither is reliably more sensitive than the other.

## Similar JND implies no clear sensitivity winner between the two schemes <!-- role: reason -->

If two encodings yield statistically indistinguishable JND thresholds for the same discrimination task, the evidence does not support preferring one over the other on sensitivity grounds alone.

**Mechanism:** Equivalent JND performance means no consistent advantage in the minimum discriminable gradient difference between the two schemes.

**Evidence:** For the aggregate task measuring JND in average-gradient discrimination between two scalar fields, there was no significant difference between cool-warm and rainbow JND thresholds [@redaEvaluatingGradientPerception2019; @zengReviewCollationGraphical2023].

**Notes:** This equivalence is limited to the reported JND metric for this specific task and setup [@redaEvaluatingGradientPerception2019; @zengReviewCollationGraphical2023].

## Context for choosing between cool-warm and rainbow <!-- role: context -->

- **User Goal:** Choose a colormap for side-by-side discrimination of which scalar field has higher average gradient.
- **Task:** Aggregate comparison evaluated via JND thresholds.
- **Data:** 2D quantitative scalar fields shown as color-coded maps.
- **Chart Setting:** Static paired comparison with the same colormap applied to both fields.
- **Audience:** Any audience where perceptual sensitivity is the primary objective.
- **Success Criterion:** Lower or comparable JND (sensitivity), not other outcomes.

## Exceptions for this equivalence claim <!-- role: exceptions -->

**Break it when:** You are optimizing for outcomes other than JND sensitivity (or a different task than average-gradient comparison). **Why:** The evidence only establishes “no significant difference” for JND in this task, not equivalence on other metrics or tasks [@redaEvaluatingGradientPerception2019; @zengReviewCollationGraphical2023].

## Costs of treating them as interchangeable <!-- role: costs -->

**Sacrifice:** You forgo potentially meaningful differences on criteria not measured here.\
**Risk:** You may ignore practical constraints that matter in your environment but are outside the evidence scope.\
**Mitigation:** Decide between the two using project constraints that are independent of JND sensitivity.

## Mistakes when applying this guideline <!-- role: mistakes -->

**Mistake:** Interpreting “no significant difference” as “identical in all situations.” **Why it fails:** The finding is bounded to JND sensitivity for one aggregate gradient-comparison task and does not generalize beyond that scope [@redaEvaluatingGradientPerception2019; @zengReviewCollationGraphical2023].

## Check whether interchangeability is acceptable <!-- role: check -->

**Failure Sign:** You are selecting a colormap for a different task (e.g., point reading, feature detection) but still using this rule.\
**Quick Check:** Confirm your success metric is JND sensitivity for average-gradient discrimination.\
**Stronger Test:** If you care about additional outcomes, measure them separately rather than inferring from JND equivalence.

## Fixes if you need a decision anyway <!-- role: fix -->

- Choose either cool-warm or rainbow based on constraints not tied to JND sensitivity (e.g., existing style requirements).
- Run a small task-matched pilot and use your own measured objective (still focused on gradient discrimination) as the tiebreaker.
- Provide both as user-selectable options if the workflow supports it and colormap choice is not fixed.
- Document that the selection between the two is not justified by JND sensitivity differences for this task.
