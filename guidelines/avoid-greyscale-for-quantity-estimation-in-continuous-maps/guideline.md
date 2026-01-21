---
id: avoid-greyscale-for-quantity-estimation-in-continuous-maps
title: Avoid Greyscale for Quantity Estimation in Continuous Maps
bibliography: references.bib
description: Greyscale ranked worst for pointwise quantity lookup accuracy in continuous
  quantitative maps; prefer any of the tested color schemes instead.
labels:
- chart:heatmap
- task:retrieve-value
- visual:color
- impact:accuracy
- data:spatial-continuous
- audience:general
- encoding:colormap
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Do not use a greyscale colormap when users must retrieve/estimate a quantitative value at a specific location in a continuous map.

## The Logic <!-- role: reason -->

In the extracted retrieve-value accuracy results, greyscale is ranked last, and every other tested colormap is ranked above it; the recorded significance pairs also indicate each other colormap significantly outperformed greyscale for retrieve-value.

- **The Principle:** Colormap choice affects the discriminability of quantitative levels for pointwise reading.
- **The Evidence:** [@redaGraphicalPerceptionContinuous2018] as collated and encoded for recommendation contexts in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Retrieve a target value (pointwise lookup on the map).
- **Data Type:** Continuous quantitative spatial field.
- **Audience:** General audiences or analysts performing value lookups.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not doing pointwise value lookup (i.e., retrieve-value is not the goal).
- **Reason:** This rule is only supported by the retrieve-value entry in the extracted results; other tasks have different outcomes. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up the neutral aesthetic of greyscale.
- **The Risk:** Switching away from greyscale may require choosing among multiple color strategies depending on task. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping greyscale and adding more tick labels to compensate for difficulty reading values.
- **Why it fails:** The extracted evidence compares colormaps directly and shows greyscale underperforms other colormaps for retrieve-value. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## How to Check <!-- role: check -->

- **Visual Sign:** Users frequently miss target-value locations or show large pointwise lookup error.
- **The Test:** A/B test greyscale vs. a non-greyscale colormap from the tested set on the same lookup task. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace greyscale with any non-greyscale colormap from the tested set.
- **Best Fix:** If retrieve-value is the primary task, use the highest-ranked scheme (rainbow) from the extracted ranking. [@redaGraphicalPerceptionContinuous2018; @zengReviewCollationGraphical2023]
