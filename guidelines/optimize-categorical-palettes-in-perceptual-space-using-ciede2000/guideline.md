---
id: optimize-categorical-palettes-in-perceptual-space-using-ciede2000
title: Optimize Categorical Palettes in a Perceptual Color Space Using CIEDE2000
bibliography: references.bib
description: Compute and optimize categorical color separations using a perceptual
  distance metric (CIEDE2000) rather than RGB/HSV distances.
labels:
- chart:generic
- task:distinguish
- visual:color-hue
- impact:clarity
- data:categorical
- audience:general
- method:perceptual-metric
---

## The Rule <!-- role: advice -->

When optimizing a categorical palette for distinctness, compute distances with **CIEDE2000** (in a perceptually-oriented space) rather than raw RGB/HSV distances.

## The Logic <!-- role: reason -->

Perceptual difference is not linear in common device-centric spaces (e.g., RGB). A perceptual metric aims to better align “numeric distance” with “seen difference,” so optimization pressure is applied where humans actually confuse colors.

- **The Principle:** Perceptual distance alignment for discriminability
- **The Evidence:** The method chooses CIEDE2000 as the distance function for optimization and discusses distortions introduced by RGB→Lab conversion and by the non-Euclidean nature of CIEDE2000, motivating its use as closer to perceived difference than simpler measures [@fangCategoricalColormapOptimization2017]. This type of extracted knowledge is exactly what the collation pipeline captures for downstream recommendation rules [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Ensure categories are perceptually distinguishable when encoded by color.
- **Data Type:** Nominal/categorical encodings mapped to distinct colors.
- **Audience:** Any; especially teams depending on defaults (system palettes) and wanting a principled optimization.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your engineering environment cannot compute CIEDE2000 (performance or dependency constraints) and you must use a simpler metric.
- **Reason:** The paper’s approach depends on perceptual-distance computation for the fitness function; without it you are no longer following the evidenced optimization approach [@fangCategoricalColormapOptimization2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** More computation and implementation complexity than simple Euclidean distances in RGB/HSV.
- **The Risk:** “Perceptual” metrics are still imperfect and can depend on assumed parameters/conditions; numeric improvements may not always translate to best subjective preference in-context [@fangCategoricalColormapOptimization2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** “Spreading colors out” by maximizing Euclidean RGB distance.
- **Why it fails:** RGB distances do not reliably correspond to perceived differences, so optimization can create pairs that are far numerically but still confusable visually [@fangCategoricalColormapOptimization2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Palette pairs that are “far apart” in code still look similar in the chart.
- **The Test:** Verify your optimizer’s fitness uses CIEDE2000 distances (not RGB/HSV distances) when evaluating pairwise separations [@fangCategoricalColormapOptimization2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the distance computation in your palette evaluation to CIEDE2000.
- **Best Fix:** Re-run the palette optimization using a CIEDE2000-based fitness function, consistent with the perceptual-knowledge operationalization goal described in the collation work [@zengReviewCollationGraphical2023; @fangCategoricalColormapOptimization2017].
