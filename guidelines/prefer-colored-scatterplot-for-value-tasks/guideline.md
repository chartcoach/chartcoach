---
id: prefer-colored-scatterplot-for-value-tasks
title: Use a Colored Scatterplot for Value Tasks in Trivariate Data
bibliography: references.bib
description: For tasks that require reading or comparing individual values, prefer
  scatterplots with both quantitative fields on x/y and categories encoded by color-hue.
labels:
- chart:scatter
- task:retrieve-value
- task:sort
- visual:position
- visual:color
- impact:accuracy
- impact:speed
- data:quantitative
- data:categorical
- complexity:multivariate
---

## The Rule <!-- role: advice -->

For retrieve-value and sort tasks on trivariate (Q1, Q2, N) data, place Q1 and Q2 on x/y and encode N with color-hue (a colored scatterplot).

## The Logic <!-- role: reason -->

Designs that map both quantitative fields to x/y and the nominal field to color-hue (E-5/E-6) appear in the top accuracy/time ranking groups for the value tasks (retrieve-value and sort) relative to alternatives that push a quantitative field into color-saturation or size/area or facet by row [@kimAssessingEffectsTask2018]. These choices are summarized as recommendation-ready evidence in the collation [@zengReviewCollationGraphical2023].

- **The Principle:** Preserve positional decoding for both quantitative variables in value tasks
- **The Evidence:** [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Read or compare individual data point values (retrieve-value, sort/compare-values-like).
- **Data Type:** Two quantitative measures plus one categorical grouping variable.
- **Audience:** Users exploring relationships while still needing accurate point-level read-offs.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary objective is an aggregate task where the study shows the colored-scatterplot family (E-5/E-6) falling into a lower aggregate-accuracy group than many alternatives.
- **Reason:** For aggregate accuracy, E-5/E-6 are ranked worse than a large set of other encodings that share the top group [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Color-hue becomes dedicated to categories, limiting use of hue for other semantics.
- **The Risk:** If categories are numerous, the color legend and discrimination demands may become burdensome (the study varied category cardinality, and performance can depend on data conditions) [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encode the nominal field on an axis (treat it as positional categories) while pushing a quantitative field into a weaker channel for value reading.
- **Why it fails:** In the study, many such mappings are not consistently top-ranked for value-task time/accuracy compared to the x/y+color-hue scatterplot family (E-5/E-6) [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** One of Q1 or Q2 is not on an axis; instead it is expressed by saturation or by dot area.
- **The Test:** Confirm your design matches E-5 or E-6 (Q1/Q2 on x/y; N on color-hue). If not, expect lower rank for retrieve-value/sort in the reported results [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remap the second quantitative field from color-saturation/area into the unused axis; move N to color-hue.
- **Best Fix:** Adopt the E-5/E-6 mapping pattern directly for value-task-heavy recommendations [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].
