---
id: use-multi-hue-sequential-gradients-to-improve-distinguishability
title: Use multi-hue sequential gradients (with lightness changes) to improve distinguishability
bibliography: references.bib
description: Combine lightness and carefully chosen hue shifts so readers can tell
  nearby values apart more easily.
labels:
- chart:choropleth
- task:distinguish
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- complexity:intermediate
---

## Use two or three hues in a sequential gradient to separate nearby values <!-- role: advice -->

When using a sequential gradient, consider a scale that changes in both lightness and a small number of carefully chosen hues so adjacent values are easier to distinguish.

## Why adding hue can improve separability <!-- role: reason -->

Lightness alone can produce subtle steps that are hard to separate, especially in midtones; a controlled hue shift adds an extra cue while keeping the scale ordered.

**Mechanism:** Dual encoding with lightness plus limited hue variation increases perceptual differences between nearby colors without abandoning the ordered structure.

**Evidence:** Readers can distinguish colors on a gradient better if the gradient is encoded through both lightness and two (or three) carefully selected hues [@muth_colors_2018].

**Notes:** The hues still need a consistent light-to-dark progression.

## When this applies to sequential scales <!-- role: context -->

- **User Goal:** Discern differences across a continuous value range.
- **Task:** Spot local differences and compare nearby values.
- **Data:** Quantitative values mapped to a sequential scale.
- **Chart Setting:** Choropleths and gradient-filled charts with many regions/marks.
- **Audience:** General readers, including those viewing quickly.
- **Success Criterion:** Adjacent value ranges appear more distinct without suggesting false breaks.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The palette must remain strictly single-hue for branding or consistency constraints. **Why:** Hue shifts may conflict with required style constraints even if they aid distinguishability [@muth_colors_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Multi-hue ramps can be harder to design well than single-hue ramps. **Risk:** Poor hue choices can introduce non-monotonic lightness or accidental emphasis. **Mitigation:** Keep hue count low and validate ordering in grayscale.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding many hue changes across the ramp without controlling lightness. **Why it fails:** The gradient can become confusing and stop reading as ordered [@muth_colors_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** Some midrange colors look “lighter” than colors representing lower values. **Quick Check:** Convert the ramp to grayscale to confirm monotonic lightness. **Stronger Test:** Pick several value steps and verify they appear in a clear low-to-high order while still being distinct.

## What to do instead <!-- role: fix -->

- Use a two-hue sequential ramp that still progresses from light to dark.
- Keep hue transitions limited and ensure lightness remains monotonic.
- If design confidence is low, start from an existing proven palette rather than inventing one.
- Add labels or binning if fine distinctions cannot be made reliably by color alone.
