---
id: avoid-full-hue-circle-for-intrinsic-order
title: Do not use a full hue-circle ramp when intrinsic color order is required
bibliography: references.bib
description: A hue ramp spanning the full hue circle cannot provide global intrinsic
  order due to hue periodicity.
labels:
- chart:any
- task:rank
- visual:color
- impact:clarity
- data:ordinal
- audience:expert
- complexity:advanced
---

## Avoid full-hue-circle ramps for intrinsic ordering <!-- role: advice -->

Do not use a hue ramp that spans the full hue circle when you need viewers to perceive a globally ordered sequence from color alone. Treat such ramps as unsuitable for intrinsic global order.

## Why full-circle hue breaks global intrinsic order <!-- role: reason -->

Hue is periodic, so a hue path that covers the whole circle necessarily returns to (or repeats) the starting hue, which defeats the perceptual requirements for global intrinsic order. This makes it impossible for all intermediate colors to be perceptually “between” the endpoints in a consistent way without relying on the legend.

**Mechanism:** Periodicity creates endpoints that coincide (or are effectively identical in hue), so perceptual distance relationships cannot support a single consistent global ordering across the entire ramp.

**Evidence:** A hue map that spans the full hue circle does not satisfy global intrinsic order due to periodicity, independent of legend-based ordering considerations. [@bujackOrderingPerceptionsPerceptual2018; @zengReviewCollationGraphical2023]

**Notes:** This does not prohibit using a full hue circle for non-ordered (categorical) purposes; it only blocks it for intrinsic *global* order.

## When this applies <!-- role: context -->

- **User Goal:** Infer a global low-to-high ordering from color without needing to consult a legend.
- **Task:** Global ordering (rank) from color appearance alone.
- **Data:** Ordered values mapped into hue along a ramp that wraps around the hue circle.
- **Chart Setting:** The legend may be absent, hard to access, or not expected to be used.
- **Audience:** Any; especially mixed audiences where intuitive hue ordering cannot be assumed.
- **Success Criterion:** Consistent perceived global order from color alone.

## When you can ignore this <!-- role: exceptions -->

**Break it when:** The ordering is explicitly legend-based and you can guarantee the legend is always used for interpretation. **Why:** Legend-based order can still be well-defined even when intrinsic global order is not. [@bujackOrderingPerceptionsPerceptual2018; @zengReviewCollationGraphical2023]

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some designers prefer full-spectrum ramps for aesthetic or salience reasons. **Risk:** Viewers may treat different ends of the scale as similar or cyclic, undermining global “low-to-high” interpretation without a legend. **Mitigation:** Make ordering explicit through legend placement and supplemental annotations.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a cyclic hue ramp to encode ordered magnitude and expecting a clear global “start-to-end” direction. **Why it fails:** Hue periodicity prevents global intrinsic order across the full circle. [@bujackOrderingPerceptionsPerceptual2018; @zengReviewCollationGraphical2023]

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers interpret the scale as looping/cyclic or cannot identify which end is “lowest” without reading. **Quick Check:** Show only the color ramp (no numbers) and ask which end is lower; hesitation or disagreement indicates failure for intrinsic order. **Stronger Test:** Sample multiple points across the ramp and ask for a total ordering; frequent inversions indicate cyclic perception.

## What to do instead <!-- role: fix -->

- Use a non-cyclic color strategy when intrinsic global ordering is required.
- Provide a prominent legend and do not rely on intrinsic order if you must keep a cyclic hue design.
- Add explicit endpoint labels and directional cues (e.g., “low”/“high”) so order is not inferred from hue alone.
- Change the encoding channel for ordering if color must remain categorical or cyclic for other reasons.
