---
id: avoid-size-for-secondary-quant-when-primary-on-position
title: Use Color-Saturation (Not Size/Area) for the Secondary Quantitative Field When
  Q1 Is Positional
bibliography: references.bib
description: When the primary quantitative field is on x/y, encode the secondary quantitative
  field with color-saturation rather than size to reduce interference and preserve
  performance.
labels:
- chart:scatter
- task:retrieve-value
- task:sort
- visual:color
- visual:area
- visual:position
- impact:speed
- impact:accuracy
- data:quantitative
- data:categorical
- complexity:multivariate
---

## The Rule <!-- role: advice -->

If Q1 is encoded on x or y, encode Q2 with color-saturation rather than size/area.

## The Logic <!-- role: reason -->

Across value-oriented tasks in the evaluated trivariate point designs, conditions with Q2 encoded as color-saturation (E-1/E-2) are consistently top-ranked for time and accuracy, while conditions with Q2 encoded as size/area (E-3/E-4) are slower and/or less accurate (e.g., retrieve-value time ranks place E-1/E-2 above E-3/E-4) [@kimAssessingEffectsTask2018]. The collation captures this as actionable encoding guidance for recommendation engines [@zengReviewCollationGraphical2023].

- **The Principle:** Cross-channel interference from size variations
- **The Evidence:** [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Fast, accurate reading/comparing of Q1 when a secondary quantitative context (Q2) is also shown.
- **Data Type:** Trivariate: Q1 (primary quantitative) + Q2 (secondary quantitative) + N (nominal), point marks.
- **Audience:** Users doing quick value judgments (retrieve-value, sort).

## When to Break It <!-- role: exceptions -->

- **Scenario:** The main goal is an aggregate task where the study’s aggregate-accuracy results do not clearly penalize Q2:size/area versus Q2:color-saturation for your chosen design family.
- **Reason:** For aggregate accuracy, many encodings fall into the same top rank group, reducing the certainty that Q2:color-saturation will outperform Q2:size/area in that specific objective [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You consume a continuous color channel for Q2, which may limit other uses of color.
- **The Risk:** If color-saturation is already needed for another quantitative variable, you may need a different design strategy to avoid overloading color [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encode Q2 via point size/area (E-3/E-4) while keeping Q1 on x/y and expecting “more quantitative” size to help overall.
- **Why it fails:** The study’s task rankings show poorer time/accuracy profiles for these mappings than for Q2:color-saturation mappings (E-1/E-2) in value tasks [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Q2 differences appear as large/small bubbles while users are being asked to read/compare Q1 from position.
- **The Test:** Compare your mapping to the study’s closest designs: if it matches E-3/E-4 rather than E-1/E-2, expect a performance penalty for retrieve-value/sort speed [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move Q2 from size/area to color-saturation and keep Q1 positional.
- **Best Fix:** Prefer the E-1/E-2 family (Q1 positional, Q2 color-saturation, N on the remaining positional axis) when your system expects value-task usage [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].
