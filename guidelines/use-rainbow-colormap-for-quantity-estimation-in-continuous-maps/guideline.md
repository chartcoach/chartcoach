---
id: use-rainbow-colormap-for-quantity-estimation-in-continuous-maps
title: Use a rainbow colormap for value lookup in continuous quantitative maps
bibliography: references.bib
description: For retrieving a numeric value from a continuous pseudocolor map, a rainbow
  colormap yields the highest accuracy among tested schemes.
labels:
- chart:heatmap
- task:retrieve-value
- visual:color
- impact:accuracy
- data:spatial
- audience:general
- domain:continuous-map
---

## Quantity estimation with a rainbow colormap <!-- role: advice -->

Use a rainbow colormap when the task is to retrieve (estimate) a quantitative value at a location in a continuous pseudocolor map. Prefer rainbow over the tested greyscale, single-hue, spiral, sequential, and diverging alternatives.

## Why rainbow supports value lookup here <!-- role: reason -->

The choice of colormap changes how distinctly nearby numeric levels appear, which affects how precisely people can match a target value on the map to a location.

**Mechanism:** Larger hue variation can make it easier to discriminate adjacent values during value-to-color and color-to-value matching.

**Evidence:** In a quantity estimation (retrieve-value) task for continuous quantitative maps, rainbow had the best accuracy ranking among nine tested colormaps and was significantly better than greyscale in the reported pairwise comparisons [@redaGraphicalPerceptionContinuous2018]. This finding is captured as an actionable recommendation in a structured collation intended for visualization recommendation and rule extraction [@zengReviewCollationGraphical2023].

**Notes:** This guideline is about accuracy for retrieving a value, not about detecting shapes/patterns.

## When to apply this rule <!-- role: context -->

- **User Goal:** Estimate a numeric value at a specific location on a continuous map.
- **Task:** Retrieve value (quantity estimation from a color-coded field).
- **Data:** Continuous spatial field (quantitative values varying over 2D position).
- **Chart Setting:** Static pseudocolor/heatmap-like display with a legend.
- **Audience:** General audiences with normal color vision (as screened in the study setting).
- **Success Criterion:** Higher accuracy in value estimation.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary goal is to perceive longitudinal patterns in high-spatial-frequency maps rather than retrieve values. **Why:** Rainbow is not the top-ranked option for the high-frequency pattern-perception condition in the extracted results.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may give up performance on some non-lookup tasks in complex maps. **Risk:** Applying a single colormap choice to all tasks can harm task-specific performance. **Mitigation:** Treat this as a task-triggered rule (use only when the active task is value lookup).

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using the same colormap choice for value lookup and for pattern-focused reading of complex maps. **Why it fails:** The extracted rankings differ by task and condition, so a one-size choice can be suboptimal for at least one task.

## Quick tests <!-- role: check -->

**Failure Sign:** People struggle to pick locations matching a requested value even with the legend present. **Quick Check:** Ask a few readers to estimate several prompted values and note systematic misses. **Stronger Test:** Run a small task-based accuracy pilot comparing your chosen palette to rainbow for the same value-lookup prompts.

## What to do instead <!-- role: fix -->

- Use the spectral colormap if you need a non-rainbow alternative while staying near the top of the retrieve-value ranking.
- Use a diverging colormap (such as cool-warm) if the task shifts away from value lookup toward one of the extracted conditions where diverging schemes rank higher.
- Split workflows: provide one view optimized for value lookup (rainbow) and another view optimized for other tasks (based on the relevant task-conditioned ranking).
