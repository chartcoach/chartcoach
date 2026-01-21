---
id: prefer-scatterplots-over-parallel-coordinates-for-correlation-judgment
title: Prefer Scatterplots Over Parallel Coordinates for Correlation Judgments
bibliography: references.bib
description: When the task is to judge correlation, use scatterplots rather than parallel
  coordinates because they yield better performance.
labels:
- chart:scatter
- chart:parallel-coordinates
- task:correlate
- visual:position
- impact:accuracy
- impact:efficiency
- data:quantitative
- audience:expert
- source:graphical-perception
---

## The Rule <!-- role: advice -->

Use a scatterplot (points with x/y position) instead of a parallel coordinates plot when users need to judge correlation.

## The Logic <!-- role: reason -->

This works because the scatterplot design supports more accurate and faster correlation judgments than the parallel coordinates design in the reported experiment.

- **The Principle:** Choose the encoding that yields higher task performance for the target task.
- **The Evidence:** In a controlled comparison, scatterplots were ranked better than parallel coordinates for correlation judgment in both accuracy and time measures [@liJudgingCorrelationScatterplots2010]. This guideline is derived from the collated graphical perception record intended to inform visualization recommendation rules [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Judge/estimate correlation between two variables.
- **Data Type:** Two quantitative variables.
- **Audience:** Users performing analytic assessment of correlation (e.g., trained analysts).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot use a scatterplot because the visualization format is constrained to parallel coordinates in the application context.
- **Reason:** The rule is about relative performance between two chart options; if one option is not available, the comparison cannot be acted on [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up using a parallel coordinates plot as the display form for the correlation task.
- **The Risk:** If the broader workflow requires parallel coordinates for reasons not evaluated here, the rule may conflict with those needs because this evidence only covers the correlation-judgment task [@liJudgingCorrelationScatterplots2010; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using parallel coordinates for correlation judgment even when a scatterplot is available.
- **Why it fails:** It selects the lower-ranked design for both accuracy and time in the reported experimental results [@liJudgingCorrelationScatterplots2010; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart uses two vertical axes with connecting line segments between them (parallel coordinates), even though the goal is simply to assess correlation between two variables.
- **The Test:** If you can redraw the same two variables as x/y positioned points (scatterplot), you are in the decision space this rule targets; prefer the scatterplot for the correlation task [@liJudgingCorrelationScatterplots2010; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap the parallel coordinates view for a scatterplot of the same two variables.
- **Best Fix:** Provide the scatterplot as the primary view for correlation judgment (and only use parallel coordinates if required for other, unevaluated purposes) [@liJudgingCorrelationScatterplots2010; @zengReviewCollationGraphical2023].
