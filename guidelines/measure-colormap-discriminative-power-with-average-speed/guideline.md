---
id: measure-colormap-discriminative-power-with-average-speed
title: "Quantify a continuous colormap\u2019s discriminative power using average speed"
bibliography: references.bib
description: Assess how strongly a continuous colormap separates values by computing
  its average speed in a perceptual color-difference metric.
labels:
- chart:colormap
- task:evaluate
- visual:color
- impact:clarity
- data:quantitative
- audience:expert
- complexity:advanced
---

## Quantify discriminative power as average speed <!-- role: advice -->

Quantify a continuous colormap’s discriminative power by computing its average speed in a perceptual color-difference metric along the colormap. Use local average speed for neighbor-to-neighbor separability and global average speed for overall separability across the full map.

## Why average speed captures discriminative power <!-- role: reason -->

This works because perceived separability between encoded values can be represented by perceived color distance, and average speed summarizes how much perceived distance accumulates per unit step along the colormap.

**Mechanism:** Higher average speed means larger perceived differences per step (locally) and stronger overall separation among colors (globally), increasing the potential for viewers to distinguish encoded values.

**Evidence:** Discriminative power is formalized using distance-derived speed measures, with local discriminative power corresponding to average local speed and global discriminative power corresponding to average global speed. [@bujackGoodBadUgly2018; @zengReviewCollationGraphical2023]

**Notes:** This guideline concerns continuous colormaps evaluated as curves through a metric space; it does not require a specific visualization task.

## When to use speed-based discriminative power <!-- role: context -->

- **User Goal:** Compare or audit candidate continuous colormaps for how strongly they separate encoded values.
- **Task:** Evaluate colormap quality characteristics before deployment.
- **Data:** Quantitative values mapped through a continuous color scale.
- **Chart Setting:** Any view that uses a continuous colormap (e.g., scalar fields, heatmaps, gradients).
- **Audience:** Designers, visualization engineers, researchers.
- **Success Criterion:** Higher perceptual separability as quantified by the chosen metric.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You are assessing discrete or categorical palettes rather than continuous colormaps. **Why:** The speed-based formulation in this guideline is defined for continuous colormaps sampled along an ordered parameter.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Requires computing pairwise or neighbor distances under a chosen ∆E metric.\
**Risk:** Different ∆E metrics can yield different numeric results for the same colormap.\
**Mitigation:** Report the metric used alongside the computed values.

## Common mistakes to avoid <!-- role: mistakes -->

**Mistake:** Treating a single computed value as universally comparable without naming the underlying color-difference metric. **Why it fails:** The computed speeds depend on the selected perceptual distance model.

## Quick checks <!-- role: check -->

**Failure Sign:** Two colormaps “feel” similarly separating, but your metric reports very different separability without explanation.\
**Quick Check:** Recompute average speed with the same sampling resolution and confirm consistent ordering.\
**Stronger Test:** Compute both local and global average speed and compare whether they agree on the same candidate being more separating.

## What to do instead <!-- role: fix -->

- Compute both local average speed and global average speed and keep them as separate indicators rather than collapsing them into one score.
- Recompute the measures under multiple perceptual distance metrics and report the range of results.
- Increase sampling resolution along the colormap parameter to reduce artifacts from overly coarse sampling.
- If you need to evaluate non-continuous color sets, switch to a palette-oriented assessment instead of speed-based measures.
