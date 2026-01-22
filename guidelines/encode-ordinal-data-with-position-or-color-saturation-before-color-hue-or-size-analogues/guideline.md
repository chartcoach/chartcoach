---
id: encode-ordinal-data-with-position-or-color-saturation-before-color-hue-or-size-analogues
title: Encode ordinal data with position or color saturation before color hue, texture,
  length, angle, orientation, or area
bibliography: references.bib
description: For ordinal data, prioritize position and then color saturation; avoid
  relying on color hue for ordered interpretation.
labels:
- chart:general
- task:order
- visual:color
- impact:accuracy
- data:ordinal
- audience:general
- complexity:basic
---

## Prefer position, then color saturation, for ordinal order <!-- role: advice -->

Encode ordinal data with position first, and use color saturation as the next choice; avoid using color hue as the primary way to convey order.

## Why saturation beats hue for ordered perception <!-- role: reason -->

Ordered interpretation depends on channels that people can reliably perceive as ordered; within color, saturation is treated as ordered while hue is not consistently ordered across the full spectrum.

**Mechanism:** Ordinal encodings benefit from channels that afford unambiguous ordered comparisons; saturation supports an ordered ramp more directly than hue.

**Evidence:** A theoretical effectiveness ranking for ordinal data places position (X/Y) first, followed by color saturation, then color hue and texture, with length/angle/orientation/area ranked lower for ordinal tasks in that ordering [@mackinlayAutomatingDesignGraphical1986a]. This ordering is included as collated, machine-ingestible guidance for visualization recommendation [@zengReviewCollationGraphical2023].

**Notes:** This guideline is about channel ordering for ordinal data, not about palette design details.

## When this applies for ordinal encodings <!-- role: context -->

- **User Goal:** Determine order, rank, or relative level (low → high).
- **Task:** Ordering or comparing ordered categories.
- **Data:** Ordinal variables.
- **Chart Setting:** Static 2D charts using standard displays.
- **Audience:** General audiences.
- **Success Criterion:** Correct ordering without ambiguity.

## When not to follow the ordinal channel ordering <!-- role: exceptions -->

**Break it when:** The ordinal variable must be shown simultaneously with multiple other fields and position and saturation are already committed to other required encodings. **Why:** The preferred channels may be unavailable in the design.

## Tradeoffs of prioritizing saturation for ordinal values <!-- role: costs -->

**Sacrifice:** Saturation may constrain use of color for other purposes. **Risk:** Overloading saturation can reduce separability if other encodings also depend on luminance-like changes. **Mitigation:** Keep the number of simultaneously encoded fields small.

## Common mistakes with ordinal encodings <!-- role: mistakes -->

**Mistake:** Using arbitrary color hues to imply ordered progression. **Why it fails:** Hue does not guarantee a consistent perceived order across the spectrum.

## Quick tests for ordinal encoding quality <!-- role: check -->

**Failure Sign:** Viewers disagree on which category is “higher” when it is encoded only by hue changes. **Quick Check:** Convert the visualization to grayscale; if order becomes clearer, saturation/position is doing the work you want. **Stronger Test:** Ask a small set of viewers to sort categories by the visual encoding alone.

## What to do instead if hue is currently used for ordinal order <!-- role: fix -->

- Move the ordinal field onto an axis position if feasible.
- Replace hue-only ordering with a saturation-based ramp.
- Use texture as a fallback ordinal encoding when position and saturation are unavailable.
- Reduce the number of ordered levels shown so the ordering signal is easier to perceive.
