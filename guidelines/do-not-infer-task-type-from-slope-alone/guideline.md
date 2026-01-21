---
id: do-not-infer-task-type-from-slope-alone
title: Do Not Infer Search Task Type from Slope Alone
bibliography: references.bib
description: "Avoid reverse-inference from an RT\xD7set-size slope to the underlying\
  \ search category because slope distributions overlap."
labels:
- chart:histogram
- task:classify
- visual:position
- impact:validity
- data:experimental
- audience:expert
- domain:visual-search
---

## The Rule <!-- role: advice -->

Do not infer that a task is “feature,” “conjunction,” or “spatial-configuration” search solely because its slope is in a certain range.

## The Logic <!-- role: reason -->

Although average slopes differ across task categories, their slope distributions overlap substantially, making reverse inference unreliable (“if slope is X, then task is Y” does not follow).

- **The Principle:** Overlapping distributions invalidate single-metric classification of category membership.
- **The Evidence:** The paper shows different mean slopes by category but overlapping histograms of target-present slopes across feature, conjunction, and spatial-configuration tasks [@wolfeWhatCan11998].

## Where to Apply <!-- role: context -->

- **User Goal:** Labeling a task class or claiming a feature “pops out” based on efficiency.
- **Data Type:** Slopes derived from RT×set-size across multiple set sizes.
- **Audience:** Researchers writing results/discussion, reviewers evaluating claims.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are comparing tasks within the same experiment and using slope differences only to claim “Task A is more efficient than Task B.”
- **Reason:** The paper critiques categorical inference, not relative comparisons of efficiency [@wolfeWhatCan11998].

## The Price <!-- role: costs -->

- **The Sacrifice:** You must justify task labels with more than a single number.
- **The Risk:** Reporting becomes more complex (may require ratios, additional analyses, or benchmarks).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using “low slope = feature search” and “high slope = conjunction/serial.”
- **Why it fails:** Many tasks share overlapping slope ranges; the same slope value can occur in different task classes [@wolfeWhatCan11998].

## How to Check <!-- role: check -->

- **Visual Sign:** Statements that map slope ranges directly onto task categories.
- **The Test:** Ask whether the inference would still hold given overlapping distributions shown in the paper; if not, it’s broken.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Rephrase conclusions to describe observed efficiency without categorical labeling.
- **Best Fix:** Use combined diagnostics (slopes + ratios) and compare against empirical benchmarks for established task classes [@wolfeWhatCan11998].
