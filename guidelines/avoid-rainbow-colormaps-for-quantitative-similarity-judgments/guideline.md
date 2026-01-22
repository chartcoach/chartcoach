---
id: avoid-rainbow-colormaps-for-quantitative-similarity-judgments
title: Avoid rainbow colormaps for quantitative similarity judgments
bibliography: references.bib
description: Do not use rainbow colormaps (e.g., jet) for continuous quantitative
  encodings when users must compare relative differences.
labels:
- chart:heatmap
- task:compare
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- complexity:beginner
---

## Avoid rainbow colormaps for continuous quantitative scales <!-- role: advice -->

Avoid rainbow colormaps (such as jet) when encoding a continuous quantitative variable, especially when users must judge which of two values is closer to a reference. Use a sequential design that preserves perceptual ordering instead.

## Rainbow designs increase judgment time and error overall <!-- role: reason -->

Rainbow ramps introduce non-uniform perceptual steps and hue-boundary artifacts that make relative distance judgments less consistent across the scale.

**Mechanism:** Hue transitions create uneven perceptual intervals and can cause apparent “bands” that do not correspond to equal data steps, increasing ambiguity in comparing distances.

**Evidence:** In triplet similarity judgment experiments, the rainbow colormap jet was the slowest and most error-prone overall among tested colormaps, while perceptually-designed sequential alternatives performed better [@liuSomewhereRainbowEmpirical2018a]. Even though jet had a localized low-error case near a color-name boundary, its overall performance was worse than the other evaluated schemes [@liuSomewhereRainbowEmpirical2018a].

**Notes:** A few isolated regions can appear easy due to categorical color-name boundaries, but this does not generalize across the full scale.

## When this rule applies <!-- role: context -->

- **User Goal:** Reliably compare “which is closer” or “which is more similar” values using color.
- **Task:** Relative distance judgments across many points on a continuous legend.
- **Data:** Scalar quantitative data mapped to a continuous colormap.
- **Chart Setting:** Any view where the colormap must support comparisons across the full range.
- **Audience:** Broad audiences; variable displays and viewing conditions.
- **Success Criterion:** Low error rate across the full scale, not just at select transitions.

## When you might break this rule <!-- role: exceptions -->

**Break it when:** The visualization intentionally leverages categorical banding by named colors as the primary communication goal rather than a faithful continuous scale. **Why:** In that case, categorical perception (name boundaries) may be the point, not a distortion.

## Costs of avoiding rainbow <!-- role: costs -->

**Sacrifice:** You give up the familiar “spectrum” look some users expect. **Risk:** Stakeholders may perceive the alternative as less vivid or less “detailed.” **Mitigation:** Validate with task-based checks focused on the decisions users need to make.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Keeping jet because “it separates values more.” **Why it fails:** Overall, it increased both response time and error in relative distance judgments.
- **Mistake:** Trusting one good-looking region of the rainbow as proof it works. **Why it fails:** Local pockets of good performance do not prevent poor performance elsewhere on the scale.

## Quick tests <!-- role: check -->

**Failure Sign:** Users report false edges/bands or make inconsistent “closer” choices across different parts of the scale. **Quick Check:** Compare small-span triplets sampled from multiple reference locations; rainbow maps will show uneven difficulty. **Stronger Test:** Measure error rates across reference positions; look for spikes aligned with hue transitions.

## What to do instead <!-- role: fix -->

- Replace the rainbow with a perceptually-uniform multi-hue sequential colormap.
- Use a single-hue luminance-ramping colormap if the task focuses on coarse comparisons.
- If you need a central reference point, switch to a diverging colormap and test midpoint-crossing comparisons explicitly.
- Provide direct numeric readout (e.g., tooltip) when users must make precise comparisons.
