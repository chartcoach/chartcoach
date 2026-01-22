---
id: treat-hue-monotonicity-as-legend-order-not-intrinsic-order
title: Treat monotonic hue ramps as legend-ordered, not intrinsically ordered
bibliography: references.bib
description: A hue ramp can support legend-based ordering when it changes monotonically,
  but monotonic hue does not guarantee intrinsic perceptual order.
labels:
- chart:any
- task:rank
- visual:color
- impact:clarity
- data:ordinal
- audience:expert
- complexity:advanced
---

## Monotonic hue gives legend-based order, not intrinsic order <!-- role: advice -->

Treat a monotonic hue ramp as supporting order only when viewers can consult a legend or numeric scale. Do not assume that a monotonic hue ramp will be intrinsically (intuitively) ordered without a legend.

## Why monotonic hue only guarantees legend-based order <!-- role: reason -->

A monotonic mapping in any single color attribute ensures that the mapping does not repeat colors, so the legend can define a consistent “before/after” ordering. But intrinsic order depends on perceptual distance relationships between colors, and monotonic hue (even monotonicity in a single attribute more generally) can still violate those distance relationships.

**Mechanism:** Monotonic hue prevents ambiguity in the mapping sequence (good for legend lookup), but it does not ensure that intermediate colors are perceptually “between” endpoint colors (needed for intrinsic order).

**Evidence:** Strict monotonicity in hue is sufficient for local and global legend-based order in the formal framework used for colormap order. [@bujackOrderingPerceptionsPerceptual2018; @zengReviewCollationGraphical2023] Monotonicity in a single attribute (including hue) is not sufficient to guarantee local or global intrinsic order, demonstrated via counterexamples. [@bujackOrderingPerceptionsPerceptual2018; @zengReviewCollationGraphical2023]

**Notes:** This guideline is about *order* of colors, not about discriminability, aesthetics, or accessibility.

## When monotonic-hue-only ordering is the right assumption <!-- role: context -->

- **User Goal:** Determine which values are higher/lower using the legend as the reference.
- **Task:** Rank/order values by color using the provided legend.
- **Data:** Ordered values (ordinal or quantitative) encoded into color hue.
- **Chart Setting:** A visible, readable legend is present and intended to be used.
- **Audience:** Mixed; especially relevant when you cannot assume shared intuitive color ordering.
- **Success Criterion:** Consistent ordering judgments aligned with the legend.

## When not to rely on this <!-- role: exceptions -->

**Break it when:** Viewers must infer ordering without a legend (e.g., “which is larger?” from color alone). **Why:** Monotonic hue does not guarantee intrinsic order, so different viewers may not perceive a consistent “between-ness” relationship among colors. [@bujackOrderingPerceptionsPerceptual2018; @zengReviewCollationGraphical2023]

## Tradeoffs of requiring legend-based ordering <!-- role: costs -->

**Sacrifice:** Faster “at-a-glance” ranking without reference material. **Risk:** If the legend is small, distant, or omitted, ordering accuracy can drop because the hue ramp is not safe to interpret intrinsically. **Mitigation:** Ensure the legend is always visible and readable wherever the color encoding is used.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a monotonic hue ramp and expecting it to read as inherently ordered without a legend. **Why it fails:** Monotonic hue does not guarantee intrinsic perceptual order. [@bujackOrderingPerceptionsPerceptual2018; @zengReviewCollationGraphical2023]

## Quick tests for whether you are over-claiming hue order <!-- role: check -->

**Failure Sign:** People disagree on which of two hues represents “more,” unless they look at the legend. **Quick Check:** Hide the legend and ask someone to rank three colored swatches; inconsistent ordering is a red flag. **Stronger Test:** Run a small internal check where participants rank sampled colors with and without a legend and compare consistency.

## What to do instead <!-- role: fix -->

- Add a clear, continuously visible legend whenever hue is used to convey order.
- Switch to a different encoding channel for ordering when a legend cannot be relied on.
- Add explicit numeric labels at key points (e.g., endpoints and a midpoint) to make the intended order unambiguous.
- Reduce the task demand from precise ordering to categorical grouping if legend use is not feasible.
