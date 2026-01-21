---
id: do-not-rely-on-name-uniqueness-to-improve-categorical-palettes
title: Do Not Rely on Name Uniqueness to Improve Categorical Palettes
bibliography: references.bib
description: Avoid depending on Name Uniqueness as a key control because it showed
  little behavioral impact in evaluation.
labels:
- chart:categorical
- task:optimize
- visual:color
- impact:efficiency
- data:categorical
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

Do not prioritize Name Uniqueness as a primary criterion for categorical palette design; focus on Perceptual Distance, Name Difference, and Pair Preference instead.

## The Logic <!-- role: reason -->

In Colorgorical’s evaluation, Name Uniqueness had little to no relationship with discrimination errors or preference ratings and was ultimately removed from the model because it had minimal effect on behavior, making it a weak lever for improving palette outcomes [@gramazioColorgoricalCreatingDiscriminable2017a].

- **The Principle:** Prefer criteria with demonstrated behavioral impact
- **The Evidence:** [@gramazioColorgoricalCreatingDiscriminable2017a]

## Where to Apply <!-- role: context -->

- **User Goal:** Simplify palette optimization and avoid ineffective constraints
- **Data Type:** Categorical palette generation/scoring pipelines
- **Audience:** Tool builders and advanced practitioners

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are experimenting with naming-related objectives beyond the tasks tested (e.g., specific labeling workflows not measured in the paper).
- **Reason:** The paper’s evidence is tied to their discrimination and preference tasks; other tasks could value different properties [@gramazioColorgoricalCreatingDiscriminable2017a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may miss niche benefits of Name Uniqueness in untested scenarios.
- **The Risk:** Overconfidence—removing it doesn’t guarantee best results if your context differs from the study [@gramazioColorgoricalCreatingDiscriminable2017a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding Name Uniqueness constraints hoping it will “make colors clearer.”
- **Why it fails:** Name Uniqueness is a single-color property and showed weak behavioral effects compared to pair-based measures [@gramazioColorgoricalCreatingDiscriminable2017a].

## How to Check <!-- role: check -->

- **Visual Sign:** Tuning Name Uniqueness doesn’t noticeably change confusions or liking.
- **The Test:** Run an A/B where only Name Uniqueness changes; if errors and preference stay flat, drop it from your primary controls [@gramazioColorgoricalCreatingDiscriminable2017a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove Name Uniqueness from your optimization objective.
- **Best Fix:** Reallocate weight/budget to pairwise discriminability (ΔE00, Name Difference) and pairwise preference modeling (Pair Preference) [@gramazioColorgoricalCreatingDiscriminable2017a].
