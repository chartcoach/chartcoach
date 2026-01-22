---
id: prefer-angle-over-area-but-not-over-position-for-sorting
title: Prefer angle over area (but not over position) for sorting when you must use
  a radial form
bibliography: references.bib
description: For sort judgments, angle encodings were more accurate than area encodings,
  but still worse than position on a common scale.
labels:
- chart:pie
- task:sort
- visual:angle
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception
---

## Choose angle instead of area when forced into a radial comparison for sorting <!-- role: advice -->

If you must use a radial form for a sorting judgment, encode magnitude with angle rather than area. Still prefer a non-radial, shared-axis position design when you are free to choose.

## Why angle is a less-bad fallback than area for sorting <!-- role: reason -->

Angle comparisons preserve a single extent to judge (opening angle) while area requires integrating two dimensions, which increases perceptual noise and reduces ordering accuracy.

**Mechanism:** Sorting based on one-dimensional angular extent is typically easier than sorting based on two-dimensional area extent, but both remain less direct than shared-axis position.

**Evidence:** In a sort (proportional judgment) task, the angle-based design ranked above the area-based designs (circle area, rectangle/treemap-like area), while position-based designs ranked above angle, and multiple significant pairwise comparisons showed position-based designs outperforming the angle-based design [@heerCrowdsourcingGraphicalPerception2010]. This ordering is recorded as reusable comparative guidance in a graphical perception knowledge collation for recommendation systems [@zengReviewCollationGraphical2023].

**Notes:** This guideline is only about accuracy for sorting, not about audience preference.

## When this applies to your chart choice <!-- role: context -->

- **User Goal:** Sort or rank values by magnitude.
- **Task:** Sort.
- **Data:** Quantitative values that might otherwise be shown as part of a radial display.
- **Chart Setting:** Static chart where a radial design is required by format or convention.
- **Audience:** General audiences.
- **Success Criterion:** Better sorting accuracy than an area-based radial alternative.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The design requires sizing marks by area to convey spatial allocation (for example, packed layouts where the area itself is the key concept). **Why:** Angle encoding may not fit the intended layout or metaphor.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Angle-based designs can constrain labeling and may reduce comparability across many items. **Risk:** Even with angle, sorting accuracy can still lag behind shared-axis position. **Mitigation:** Provide a supplementary aligned view for accurate ordering when decisions are high-stakes.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using area (bubble size or rectangle size) as the primary cue in a radial-style sorting task. **Why it fails:** Area adds perceptual error compared with angle and may produce more incorrect orderings.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers can tell “big vs small” but cannot reliably order mid-range values. **Quick Check:** Swap the radial sizing from area to angle and see if informal sorting becomes more consistent. **Stronger Test:** Compare sorting accuracy between an angle encoding and a shared-axis position encoding on the same data.

## What to do instead <!-- role: fix -->

- Replace area sizing with angle encoding if a radial form must remain.
- Provide an aligned position-based chart as a companion view for accurate sorting decisions.
- Add direct value labels for the compared elements to reduce reliance on angular estimation.
- Limit sorting prompts to a small number of items when using angle to reduce confusion.
