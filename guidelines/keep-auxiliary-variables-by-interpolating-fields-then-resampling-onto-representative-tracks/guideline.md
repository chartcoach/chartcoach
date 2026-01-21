---
id: keep-auxiliary-variables-by-interpolating-fields-then-resampling-onto-representative-tracks
title: Preserve Multivariate Attributes by Field Interpolation and Resampling
bibliography: references.bib
description: Compute spatial fields for attributes like intensity and size at each
  time step, then sample those fields along representative tracks.
labels:
- chart:trajectory
- task:communicate-multivariate
- visual:color
- impact:clarity
- data:multivariate
- audience:novice
- domain:tropical-cyclone
- source:liu-2019
---

## The Rule <!-- role: advice -->

When representative tracks are reconstructed from an ensemble, encode non-position variables by interpolating a spatial field at each time step from the original ensemble and resampling attribute values onto the representative tracks.

## The Logic <!-- role: reason -->

Representative track construction preserves spatial distribution but does not preserve distributions of other variables; interpolating per-time spatial fields and resampling onto the tracks re-attaches plausible intensity/size information without consuming uncertainty channels.

- **The Principle:** Decouple uncertainty depiction (position spread) from attribute encoding
- **The Evidence:** [@liuVisualizingUncertainTropical2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Read where-when-intensity-size together in a single view
- **Data Type:** Track ensembles with per-point attributes (e.g., storm size, maximum wind speed)
- **Audience:** Public-facing viewers and operational decision makers

## When to Break It <!-- role: exceptions -->

- **Scenario:** The attribute changes sharply due to external constraints (e.g., landfall effects) and smoothing would mislead
- **Reason:** Interpolation can underestimate landfall-driven weakening and can decouple size from intensity (e.g., showing non-zero hurricane-force radius below hurricane strength) [@liuVisualizingUncertainTropical2019]

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional computation per time step (field construction)
- **The Risk:** Interpolation artifacts can produce physically inconsistent combinations of attributes [@liuVisualizingUncertainTropical2019]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Copy attributes from the nearest original member track without regard to spatial distribution
- **Why it fails:** It can reintroduce incoherent member behavior and does not provide a smooth, readable attribute narrative along representative tracks [@liuVisualizingUncertainTropical2019]

## How to Check <!-- role: check -->

- **Visual Sign:** Attribute encodings fluctuate erratically along a smooth track or show implausible attribute combinations
- **The Test:** Compare sampled attribute values against the original ensemble values at the same time step to see if they are consistent with local neighborhood patterns [@liuVisualizingUncertainTropical2019]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce temporal annotation frequency (e.g., fewer size glyphs) while keeping attribute color stable
- **Best Fix:** Use per-time RBF interpolation with density-dependent kernels and resample those fields onto the representative tracks, as specified in the paper [@liuVisualizingUncertainTropical2019]
