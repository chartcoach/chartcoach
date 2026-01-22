---
id: define-visual-target-shapes-as-line-segments-and-optimize-by-distance-to-the-shape
title: Define visual target shapes as line segments and optimize by point-to-shape
  distance
bibliography: references.bib
description: "Direct the dataset\u2019s appearance by minimizing the average distance\
  \ from points to a target shape represented by line segments."
labels:
- chart:scatter
- task:generate
- visual:position
- impact:clarity
- data:quantitative
- audience:expert
- custom:target-shape
- complexity:advanced
---

## Optimize toward a target drawing using a distance-based fitness function <!-- role: advice -->

Represent the desired visual outcome as a collection of line segments and use fitness as the average distance from each point to its nearest location on the target shape.

## Why distance-to-shape fitness steers appearance while constraints hold stats <!-- role: reason -->

A distance-based fitness provides a continuous signal that improves as points move closer to the intended structure, enabling gradual coercion of a scatterplot into a recognizable pattern while a separate statistical gate keeps chosen statistics unchanged.

**Mechanism:** Each accepted perturbation slightly reduces typical point-to-shape distance, so the point cloud progressively aligns with the target geometry even though individual moves are small.

**Evidence:** Target shapes specified as line segment collections were used to coerce a seed scatterplot into multiple distinct shapes while maintaining the same summary statistics to two decimal places [@matejkaSameStatsDifferent2017]. A progression over iterations demonstrated convergence toward the target as the annealing temperature cooled [@matejkaSameStatsDifferent2017].

**Notes:** Fitness based only on point-to-shape distance can create uneven coverage along the target (clumps and gaps) [@matejkaSameStatsDifferent2017].

## When you want specific, recognizable structures in a scatterplot <!-- role: context -->

- **User Goal:** Create datasets whose scatterplots resemble a chosen icon, letter, or geometric motif while preserving selected statistics.
- **Task:** Coerce a dataset into a specific visual pattern (not just “different”).
- **Data:** 2D point sets where point locations can be moved iteratively.
- **Chart Setting:** Demonstrations, teaching materials, or test corpora of controlled datasets.
- **Audience:** Viewers who need an unmistakable difference in appearance across datasets.
- **Success Criterion:** The final plot visibly approximates the target shape and matches the selected statistics to the defined precision.

## When not to expect clean results from a target-shape coercion <!-- role: exceptions -->

**Break it when:** The seed dataset’s structure is very different from the target shape and has limited coverage of the target’s coordinate space. **Why:** The optimization can yield undesirable outputs in this mismatch case [@matejkaSameStatsDifferent2017].

## Tradeoffs of shape coercion via distance minimization <!-- role: costs -->

**Sacrifice:** You may need many iterations to make the shape legible while still satisfying the statistical constraint. **Risk:** The resulting shape can be sparse in some regions and overly dense in others. **Mitigation:** Treat the output as an optimization result that may require changing the target or adding additional objectives [@matejkaSameStatsDifferent2017].

## Common failure modes when steering toward a shape <!-- role: mistakes -->

- **Mistake:** Using only a point-to-shape distance objective and expecting uniform coverage of the target. **Why it fails:** The method can produce clumping because it does not explicitly encourage separation or coverage [@matejkaSameStatsDifferent2017].
- **Mistake:** Choosing a complex target that occupies little of the coordinate space compared with the seed. **Why it fails:** The optimization may settle into visually unsatisfying configurations under the constraints [@matejkaSameStatsDifferent2017].

## Quick ways to test if the target is being reached <!-- role: check -->

**Failure Sign:** Points concentrate in a few parts of the target while other parts remain empty, or the shape remains illegible late in the run. **Quick Check:** Track the mean point-to-shape distance over time and confirm it decreases across the cooling schedule. **Stronger Test:** Visually inspect intermediate snapshots at multiple iterations to confirm the structure emerges progressively rather than abruptly or not at all [@matejkaSameStatsDifferent2017].

## What to do instead when the coerced shape looks wrong <!-- role: fix -->

- Choose a simpler target pattern with broader coverage of the coordinate space.
- Pre-scale or reposition the target shape to better align with the seed dataset’s extent.
- Modify the fitness to incorporate an additional goal beyond distance-to-shape (such as discouraging clumps).
- Start from a seed dataset whose overall extent and density better matches the target’s footprint [@matejkaSameStatsDifferent2017].
