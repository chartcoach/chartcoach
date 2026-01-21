---
id: use-summarization-framing-for-ensemble-aggregate-questions
title: Frame Aggregate Questions As Summarization Over Sets
bibliography: references.bib
description: Treat mean/variance and other aggregate judgments as set-level summarization
  tasks that rely on ensemble coding.
labels:
- task:aggregate
- task:summarize
- impact:clarity
- data:quantitative
- audience:designer
- complexity:foundational
---

## The Rule <!-- role: advice -->

When the user needs a mean/variance-style aggregate judgment, treat it as a **summarization** task over a collection of marks.

## The Logic <!-- role: reason -->

Summary tasks require extracting properties that describe the collection in aggregate (e.g., mean position, mean size, variance), which is a distinct perceptual operation from identifying individual values.

- **The Principle:** Ensemble Summarization vs. Itemwise Reading
- **The Evidence:** [@szafirFourTypesEnsemble2016], collated as task-relevant knowledge for recommendation settings in [@zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Estimate/compare averages, variability, or other descriptive summaries from many marks (e.g., average position in a scatterplot, variability in a line region).
- **Data Type:** Quantitative data shown as multiple marks or a dense depiction.
- **Audience:** Designers and recommenders deciding how to support aggregate judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user needs an exact computed statistic (e.g., exact mean with decimals) rather than a visual estimate.
- **Reason:** The rule is about perceptual summarization; exact statistics are not an ensemble judgment task [@szafirFourTypesEnsemble2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Summarization-optimized designs may not support precise point-level inspection equally well.
- **The Risk:** Users may over-trust a visually inferred “average” when they need a computed value.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating “aggregate” as just “retrieve value, but for many points,” and optimizing only for individually readable marks.
- **Why it fails:** Summarization depends on set-level processing and can behave differently than single-value extraction [@szafirFourTypesEnsemble2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can pick out points but give inconsistent or slow answers for “average/variability” questions.
- **The Test:** Ask users to estimate mean/variance quickly; if they need to count or serially inspect many marks, the display may not be supporting summarization well.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce obstacles to perceiving the set as a whole (e.g., simplify the mark set or reduce competing encodings).
- **Best Fix:** In a recommender, treat “aggregate” as a distinct task type (summarization) and select/score candidates accordingly, as encouraged by the task-aware collation approach in [@zengReviewCollationGraphical2023].
