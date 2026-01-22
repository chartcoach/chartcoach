---
id: avoid-rainbow-colormaps-for-continuous-or-ordered-data
title: Avoid rainbow colormaps for continuous or ordered data; use sequential or diverging
  palettes instead
bibliography: references.bib
description: Rainbow colormaps distort perceived differences and create false bands,
  so ordered data should use perceptually consistent sequential or diverging palettes.
labels:
- chart:heatmap
- task:estimate
- visual:color
- impact:accuracy
- data:continuous
- audience:general
- risk:misinterpretation
---

## Use sequential or diverging palettes for ordered data, not rainbow hues <!-- role: advice -->

Use a sequential colormap for increasing magnitudes and a diverging colormap only when your data has a meaningful midpoint (such as a baseline or natural zero). Do not use rainbow (red–yellow–green–blue) colormaps for continuous or ordered values.

## Why rainbow hues distort ordered-value judgments <!-- role: reason -->

Rainbow colormaps change hue non-uniformly, so equal steps in data do not look like equal steps in color; viewers perceive artificial gradients, uneven contrasts, and banding that are not present in the data. Rainbow hues also encourage categorical grouping by color name (for example, “all blues”), which introduces false segments into smoothly varying fields and makes some differences look larger or smaller than they are.

**Mechanism:** Non-uniform perceptual steps and categorical color grouping bias magnitude comparisons and create spurious boundaries in continuous fields.

**Evidence:** Switching expert diagnostic tasks from rainbow colormaps to alternative palettes increased correct identification performance substantially in a real interpretation setting [@szafirGoodBadBiased2018]. Rainbow colormaps are documented to create artificial divisions and skew perceived value differences in smoothly varying data fields [@szafirGoodBadBiased2018].

**Notes:** This guideline targets ordered perception; it does not prohibit using many hues for categories.

## When this palette rule applies <!-- role: context -->

- **User Goal:** Read relative magnitude, gradients, hotspots, or smooth spatial variation from color.
- **Task:** Estimate differences, find local maxima/minima, compare regions by value.
- **Data:** Ordered/continuous measures (scalar fields, intensities, densities, probabilities).
- **Chart Setting:** Heatmaps, choropleths, scientific scalar fields, eye-tracking heatmaps, false-color images.
- **Audience:** Mixed audiences, including viewers with color-vision deficiencies.
- **Success Criterion:** Accurate perceived ordering and difference magnitudes without false bands.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The colors encode categories (nominal classes) rather than ordered magnitudes. **Why:** For categories, discrete hue changes are interpreted as separate groups and do not need to preserve ordered magnitude perception [@szafirGoodBadBiased2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Rainbow palettes can look more “vivid” and may appear to show more variation at a glance. **Risk:** Sequential or diverging palettes can feel less visually dramatic and may require more careful legend design. **Mitigation:** Use contrast and annotation to emphasize key ranges without introducing hue banding.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Keeping rainbow palettes because “experts can learn to read them.” **Why it fails:** The perceptual distortions persist even for experienced users and can still bias conclusions [@szafirGoodBadBiased2018].

## Quick tests to catch problems <!-- role: check -->

**Failure Sign:** Smooth data appears to have distinct bands or abrupt boundaries that are not in the underlying field. **Quick Check:** Ask whether equal numeric steps look equally different across the full legend range. **Stronger Test:** Compare viewer judgments of which of two regions differs more from a reference under rainbow vs. sequential palettes.

## What to do instead <!-- role: fix -->

- Replace the rainbow palette with a sequential colormap for monotonic magnitudes.
- Use a diverging colormap centered on a meaningful midpoint when the question is “above vs. below baseline.”
- Ensure the legend reflects a continuous ramp (no repeated hue “families” that create visual grouping).
- Re-encode key thresholds with annotation or contours rather than relying on abrupt hue transitions.
