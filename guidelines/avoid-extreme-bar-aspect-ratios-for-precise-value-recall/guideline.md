---
id: avoid-extreme-bar-aspect-ratios-for-precise-value-recall
title: Avoid Extreme Bar Aspect Ratios When Users Must Recall Exact Values
bibliography: references.bib
description: Reduce bias in recalling bar-encoded values by avoiding extreme wide
  or tall bar aspect ratios.
labels:
- chart:bar
- task:retrieve-value
- visual:length
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Avoid extreme wide or tall bar aspect ratios when the user task is to retrieve a quantitative value from a bar and reproduce/recall it.

## The Logic <!-- role: reason -->

When bar marks have extreme aspect ratios, people’s recalled position/height judgments become systematically biased.

- **The Principle:** Aspect-ratio-driven bias in recalled position encodings
- **The Evidence:** This guideline is derived from collated graphical perception evidence [@zengReviewCollationGraphical2023], specifically experiments showing aspect ratio biases in recalled bar position [@cejaTruthSquareAspect2021].

## Where to Apply <!-- role: context -->

- **User Goal:** Retrieve a specific quantitative value and remember/reproduce it (value recall).
- **Data Type:** Quantitative values shown as single bars (rectangular marks) with a linear scale.
- **Audience:** General audiences (applies broadly when recall is required).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users do not need to recall values (they only read them while the bar remains present).
- **Reason:** The evidence captured here targets bias in recall/reproduction during a retrieve-value task; if recall is not required, this specific risk may not apply based on the provided evidence [@cejaTruthSquareAspect2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less flexibility in layout (you may need to change chart sizing, spacing, or container design to avoid extreme shapes).
- **The Risk:** Forcing certain aspect ratios can constrain responsive designs or dense dashboards.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Changing only bar area/size while keeping an extreme aspect ratio.
- **Why it fails:** The collated result highlights aspect ratio as the driver of bias in this context, not simply that the mark is “big” or “small” [@zengReviewCollationGraphical2023; @cejaTruthSquareAspect2021].

## How to Check <!-- role: check -->

- **Visual Sign:** Bars appear extremely “flat and wide” or “thin and tall.”
- **The Test:** Resize the chart container: if bars become dramatically wider-than-tall or taller-than-wide, you have entered a higher-risk zone for biased recall in retrieve-value scenarios [@cejaTruthSquareAspect2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust chart sizing (width/height) so bars are not extreme in aspect ratio.
- **Best Fix:** Redesign the layout so bars maintain non-extreme aspect ratios across contexts where users must recall values (e.g., across views/screens in the same workflow), consistent with the risk flagged in the collated evidence [@zengReviewCollationGraphical2023; @cejaTruthSquareAspect2021].
