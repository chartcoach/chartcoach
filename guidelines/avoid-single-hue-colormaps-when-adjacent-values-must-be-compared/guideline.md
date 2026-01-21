---
id: avoid-single-hue-colormaps-when-adjacent-values-must-be-compared
title: Avoid Single-Hue Colormaps for Near-Neighbor Comparisons
bibliography: references.bib
description: Single-hue luminance ramps can suffer accuracy losses when users compare
  very small differences along the scale.
labels:
- chart:heatmap
- task:compare
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- colormap:single-hue
---

## The Rule <!-- role: advice -->

Do not rely on single-hue (primarily luminance-ramping) colormaps when users must accurately judge very small differences between nearby values.

## The Logic <!-- role: reason -->

- **The Principle:** Near-neighbor comparisons can collapse to near-threshold perceptual differences, making “which is closer?” judgments unreliable.
- **The Evidence:** Across multiple single-hue schemes (blues/greens/oranges/greys), the smallest span condition produced significantly higher error than larger spans; the paper links these failures to small differences in perceptual distance (around ~5 ΔE in their analysis) [@liuSomewhereRainbowEmpirical2018a].

## Where to Apply <!-- role: context -->

- **User Goal:** Make fine-grained similarity judgments from color.
- **Data Type:** Continuous quantitative data where many values are close together (or where you use many bins on a “sequential” palette).
- **Audience:** Any audience where small errors change conclusions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users mainly compare broad low-vs-high regions (large spans) rather than adjacent values.
- **Reason:** The paper finds single-hue can be fast and accurate for larger spans; the degradation was concentrated in small-span comparisons [@liuSomewhereRainbowEmpirical2018a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Single-hue ramps are simple, familiar, and can look clean; avoiding them may complicate design choices.
- **The Risk:** Switching palettes may introduce other issues (e.g., boundary effects in diverging schemes if used incorrectly).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Increasing the number of discrete bins in a single-hue palette to “add detail.”
- **Why it fails:** More bins can push adjacent colors into the low-span/low-difference regime where errors increase [@liuSomewhereRainbowEmpirical2018a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users struggle to tell which of two close legend ticks is nearer to a reference, even when values differ.
- **The Test:** Create a few near-neighbor triplets around multiple reference points; if accuracy drops sharply at small spans, the palette lacks effective resolution (as observed for single-hue maps) [@liuSomewhereRainbowEmpirical2018a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of bins / avoid encoding extremely small differences with color alone.
- **Best Fix:** Use a perceptually-designed multi-hue sequential colormap that improves discrimination while maintaining ordering [@liuSomewhereRainbowEmpirical2018a].
