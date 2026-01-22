---
id: test-colormap-intuitive-order-with-triangle-side-difference
title: Test intuitive order in continuous colormaps using triangle side difference
bibliography: references.bib
description: Evaluate whether colors can be intuitively ordered without a legend by
  checking triangle side differences across sampled points.
labels:
- chart:colormap
- task:rank
- visual:color
- impact:interpretability
- data:quantitative
- audience:expert
- complexity:advanced
---

## Use triangle side difference to validate intuitive order <!-- role: advice -->

Test whether a continuous colormap supports intuitive ordering by computing triangle side differences for triples of sampled colors and requiring the minimum to be positive. Apply this locally for consecutive triples and globally for arbitrary triples across the colormap when you need intuitive order everywhere.

## Why triangle side difference captures intuitive order <!-- role: reason -->

Intuitive order can be approximated by whether a middle color is perceptually between two outer colors; in distance terms, the outer-to-outer distance should exceed each outer-to-middle distance.

**Mechanism:** Triangle side difference measures whether the longest side of the triangle in perceptual distance space connects the two outer points; negative values indicate a middle point that is not perceptually between the endpoints, breaking intuitive ordering.

**Evidence:** Local and global intuitive order are defined through inequalities on perceptual distances among triples, and are evaluated using local and global triangle side difference with positivity indicating orderability. [@bujackGoodBadUgly2018; @zengReviewCollationGraphical2023]

**Notes:** A colormap can satisfy legend-based order while failing intuitive order.

## When to use triangle-based intuitive order checks <!-- role: context -->

- **User Goal:** Select a colormap whose colors can be ordered consistently without consulting a legend.
- **Task:** Rank or filter continuous colormaps by intuitive orderability.
- **Data:** Quantitative values mapped along a continuous colormap.
- **Chart Setting:** Situations where viewers may need to interpret order directly from color appearance.
- **Audience:** Designers optimizing interpretability of color sequences.
- **Success Criterion:** Minimum triangle side difference > 0 (local and/or global, depending on requirement).

## When not to follow it <!-- role: exceptions -->

**Break it when:** The intended use assumes legend consultation for ordering. **Why:** Triangle-based intuitive order targets ordering without relying on a legend.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Computing global triangle side differences can be computationally heavier because it involves many triples.\
**Risk:** Results depend on the perceptual distance metric and sampling strategy.\
**Mitigation:** Keep the evaluation protocol fixed (metric and sampling) when comparing multiple candidates.

## Common mistakes to avoid <!-- role: mistakes -->

**Mistake:** Assuming that invertibility guarantees intuitive order. **Why it fails:** A colormap can be injective (legend-orderable) while still having triples that violate intuitive betweenness.

## Quick checks <!-- role: check -->

**Failure Sign:** Viewers disagree on which of three colors represents a middle value even when values are equally spaced.\
**Quick Check:** Compute local triangle side difference for consecutive triples and confirm its minimum is positive.\
**Stronger Test:** Compute global triangle side difference to locate specific regions where intuitive order breaks.

## What to do instead <!-- role: fix -->

- If global intuitive order is required, evaluate the minimum global triangle side difference and reject candidates with negative minima.
- If only local intuitive order is required, constrain evaluation to consecutive triples and use the minimum local triangle side difference.
- Visualize where violations occur by locating which middle sample causes the most negative triangle side difference for each endpoint pair.
- If intuitive order is not achievable under constraints, fall back to ensuring legend-based order via minimum-speed checks.
