---
id: use-single-hue-luminance-ramps-only-when-comparisons-are-coarse
title: Use single-hue luminance ramps only when comparisons are coarse
bibliography: references.bib
description: Single-hue sequential colormaps work well for larger value spans but
  can cause high error for small-span comparisons.
labels:
- chart:heatmap
- task:compare
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- complexity:intermediate
---

## Use single-hue sequential colormaps only when users won’t compare very close values <!-- role: advice -->

Use a single-hue sequential colormap (primarily luminance-ramping) when the task involves comparing values that are meaningfully separated on the scale. Avoid relying on it when users must discriminate very small differences along the scale.

## Single-hue ramps can lack resolution for near-neighbor judgments <!-- role: reason -->

When hue stays nearly constant, fine discrimination depends heavily on small luminance changes, which can make “which is closer” judgments error-prone when values are close together.

**Mechanism:** With minimal hue change, small steps may produce distance differences near the just-noticeable difference (JND), so viewers can distinguish the colors but cannot reliably judge which of two differences is smaller.

**Evidence:** Across multiple single-hue colormaps (blues, greens, oranges, greys), error rates were significantly higher for the smallest tested span than for larger spans, with similar response times across hues [@liuSomewhereRainbowEmpirical2018a]. In the assorted comparison, blues matched viridis at larger spans but showed notable accuracy drops for small spans, indicating a resolution limitation rather than a general weakness [@liuSomewhereRainbowEmpirical2018a].

**Notes:** The study’s task was relative distance judgments with a visible legend; the resolution issue still appeared under these aided conditions.

## When this guideline applies <!-- role: context -->

- **User Goal:** Make correct “closer vs farther” comparisons from color.
- **Task:** Compare small differences within a narrow part of the scale.
- **Data:** Continuous quantitative data mapped to a sequential colormap.
- **Chart Setting:** Continuous legend; repeated local comparisons (e.g., scanning a heatmap).
- **Audience:** General audiences; speed and accuracy both matter.
- **Success Criterion:** Low error when values are close.

## Exceptions <!-- role: exceptions -->

**Break it when:** The scale is discretized into a small number of bins such that adjacent bins are not near-neighbors perceptually. **Why:** The “small-span” condition may not occur if bins are widely separated.

## Costs <!-- role: costs -->

**Sacrifice:** Limiting single-hue ramps to coarse comparisons can reduce stylistic consistency across a product that defaults to single-hue palettes. **Risk:** Overcorrecting may push you to multi-hue schemes even when users only need coarse grouping. **Mitigation:** Match the palette choice to the smallest meaningful difference users must judge.

## Common mistakes <!-- role: mistakes -->

- **Mistake:** Using single-hue ramps while also increasing the number of discrete steps (bins) to “add detail.” **Why it fails:** More bins can create near-neighbor comparisons that fall into the high-error small-span regime.
- **Mistake:** Interpreting good performance at large spans as proof the palette is safe everywhere. **Why it fails:** The observed degradation was span-dependent.

## Quick tests <!-- role: check -->

**Failure Sign:** Users confuse adjacent steps or cannot reliably tell which region is closer to a reference within the same hue range. **Quick Check:** Sample triplets corresponding to small differences (like ~15% of the range in the study) and see if choices are near chance. **Stronger Test:** Run a short triplet-judgment test at small spans across multiple reference points.

## What to do instead <!-- role: fix -->

- Switch to a perceptually-uniform multi-hue sequential colormap when fine discrimination is required.
- Reduce the number of discrete bins so adjacent colors are more separated.
- Add interaction or annotation to support precise comparisons where color alone is insufficient.
- Move critical comparisons to a more precise encoding channel when feasible.
