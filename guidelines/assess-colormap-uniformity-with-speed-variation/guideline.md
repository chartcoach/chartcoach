---
id: assess-colormap-uniformity-with-speed-variation
title: Assess continuous colormap uniformity using speed variation (standard deviation)
bibliography: references.bib
description: Measure whether equal steps in a continuous colormap look equally different
  by checking the standard deviation of its speed.
labels:
- chart:colormap
- task:evaluate
- visual:color
- impact:consistency
- data:quantitative
- audience:expert
- complexity:advanced
---

## Measure uniformity using speed variation <!-- role: advice -->

Assess the uniformity of a continuous colormap by computing the standard deviation of its speed, using local speed for neighbor steps and global speed for all pairs. Prefer lower speed variation when you want equally sized perceived steps across the colormap.

## Why speed variation captures uniformity <!-- role: reason -->

Uniformity corresponds to equal perceived differences for equal data differences; speed is perceived distance normalized by parameter distance, and its variation directly reflects uneven perceptual step sizes.

**Mechanism:** When speed is constant, each incremental move along the colormap produces a consistent perceived change; when speed varies, some ranges appear to change faster than others.

**Evidence:** Uniformity is formalized as constant speed, and operationalized by the standard deviation of local speed (local uniformity) and the standard deviation of global speed (global uniformity). [@bujackGoodBadUgly2018; @zengReviewCollationGraphical2023]

**Notes:** Global uniformity is a stronger condition than local uniformity and is tied to constant global speed.

## When to use speed-variation uniformity <!-- role: context -->

- **User Goal:** Choose or validate a continuous colormap that changes at a consistent perceptual rate.
- **Task:** Evaluate and compare candidate colormaps during design or QA.
- **Data:** Quantitative values mapped continuously to color.
- **Chart Setting:** Any continuous colormap usage where uneven perceptual steps are undesirable.
- **Audience:** Visualization designers and implementers.
- **Success Criterion:** Low local and/or global speed standard deviation.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You need a deliberately non-uniform mapping that emphasizes some value ranges more than others. **Why:** Uniformity metrics treat intentional emphasis as non-uniformity.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Requires computing speed across the colormap and summarizing its variation.\
**Risk:** Over-focusing on uniformity can down-rank colormaps that are acceptable for specific, context-dependent goals not captured by the metric.\
**Mitigation:** Use the metric as a screening signal, then verify with task-specific checks if needed.

## Common mistakes to avoid <!-- role: mistakes -->

**Mistake:** Using only local uniformity and assuming it guarantees global uniformity. **Why it fails:** A colormap can be locally constant-speed while still having non-constant global speed.

## Quick checks <!-- role: check -->

**Failure Sign:** Some parts of the colormap look like they “change a lot” while others look nearly flat for the same value step.\
**Quick Check:** Plot local speed across the parameter and look for large fluctuations.\
**Stronger Test:** Compute both local and global speed standard deviations and confirm both are low if you need consistency across the entire map.

## What to do instead <!-- role: fix -->

- Compute local speed standard deviation when you care primarily about step-to-step consistency.
- Compute global speed standard deviation when you need consistent differences across non-adjacent values.
- Report both measures to distinguish local-only from global uniformity.
- If global uniformity is unattainable for your constraints, constrain evaluation to local uniformity and document the limitation.
