---
id: verify-colormap-legend-based-order-with-minimum-speed
title: Ensure continuous colormap legend-based order by requiring positive minimum
  speed
bibliography: references.bib
description: Check that a continuous colormap remains invertible (orderable using
  a legend) by verifying its minimum speed is greater than zero.
labels:
- chart:colormap
- task:rank
- visual:color
- impact:clarity
- data:quantitative
- audience:expert
- complexity:advanced
---

## Require positive minimum speed for legend-based order <!-- role: advice -->

Ensure legend-based order for a continuous colormap by requiring its minimum speed to be greater than zero. Evaluate this locally for adjacent samples and globally for all sampled pairs when you need the entire colormap to be invertible.

## Why minimum speed captures legend-based order <!-- role: reason -->

Legend-based order depends on invertibility: if distinct data values can map to the same perceived color (or become indistinguishably close), users cannot reliably recover ordering even with a legend.

**Mechanism:** Minimum speed detects flat segments (or repeated colors) in the colormap parameterization; a zero minimum speed indicates a loss of invertibility over some interval.

**Evidence:** Legend-based order is tied to invertibility and is evaluated with the minimum local speed (local legend-based order) and minimum global speed (global legend-based order), where zeros indicate violations. [@bujackGoodBadUgly2018; @zengReviewCollationGraphical2023]

**Notes:** Local legend-based order can hold even when global legend-based order fails.

## When to use minimum-speed invertibility checks <!-- role: context -->

- **User Goal:** Ensure viewers can interpret values from a color legend without ambiguity.
- **Task:** Validate colormap ordering properties before use.
- **Data:** Quantitative values encoded with a continuous colormap and a legend.
- **Chart Setting:** Any visualization where viewers read values via a color legend.
- **Audience:** Designers and engineers responsible for encoding correctness.
- **Success Criterion:** Minimum local speed > 0 (local invertibility) and/or minimum global speed > 0 (global injectivity).

## When not to follow it <!-- role: exceptions -->

**Break it when:** The colormap is intentionally non-invertible (e.g., constant segments by design). **Why:** A non-invertible mapping is expected to collapse multiple values into the same perceived color.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Requires computing speeds and taking minima, which can be sensitive to sampling and metric choice.\
**Risk:** A strictly positive minimum can still correspond to changes too small to be useful under practical viewing conditions.\
**Mitigation:** Pair the minimum-speed check with a practical thresholding policy appropriate to your sampling and display assumptions.

## Common mistakes to avoid <!-- role: mistakes -->

**Mistake:** Checking only whether endpoint colors differ and assuming the colormap is invertible. **Why it fails:** Flat regions or repeated colors can exist in the interior even if endpoints differ.

## Quick checks <!-- role: check -->

**Failure Sign:** A range of values appears as an unchanging color band in the legend.\
**Quick Check:** Compute minimum local speed; if it is zero, the colormap is not locally invertible.\
**Stronger Test:** Compute minimum global speed to detect repeated colors anywhere in the map.

## What to do instead <!-- role: fix -->

- Increase sampling density along the colormap and recompute minimum speed to reduce missed flat intervals.
- Compute both minimum local speed and minimum global speed to distinguish local from global invertibility issues.
- If only local invertibility is required, explicitly scope the requirement to local minimum speed rather than global injectivity.
- If global invertibility is required, reject colormaps with zero minimum global speed and replace them with a colormap that has mutually distinct sampled colors.
