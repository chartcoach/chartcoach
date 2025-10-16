---
id: diverging-midpoint-comparison-caution
title: "Use caution with comparisons across the midpoint of a diverging colormap"
tags:
  - impact:perceptual
  - impact:cognitive
  - visual:color
  - data:quantitative
  - task:compare
  - chart:heatmap
  - chart:map.choropleth
evidence:
  strength: low
  summary: "Liu & Heer (2018) found that subjects were more prone to errors when comparing values that straddled the neutral midpoint of a single diverging colormap ('blueorange'). This suggests viewers may struggle to compare hue differences against saturation differences in this specific context."
sources:
  - type: research
    ref: Liu & Heer, 2018
    url: https://doi.org/10.1145/3173574.3174172
    note: "Found that the 'blueorange' diverging colormap 'suffers when values straddle the mid-point', with increased error rates for comparisons across the central boundary."
    role: primary
---
## Guidance

Be aware that viewers may find it harder to accurately judge value differences when comparing colors from opposite sides of a diverging scale's neutral midpoint.

## Why

A diverging scale typically uses two different hues (e.g., blue and orange) that diverge from a neutral center. A comparison across the midpoint requires the viewer to simultaneously judge a change in hue (blue vs. orange) and a change in saturation/luminance. This is a more complex perceptual task than comparing two colors of the same hue, and the paper's experiment showed it can lead to more errors. Viewers may erroneously group chromatic colors as being more different from a neutral color than they actually are.

## When it applies

- When using a diverging colormap (e.g., to show deviation from a mean, a zero value, or a critical threshold).
- When a key task for the viewer is to compare the magnitude of values on opposite sides of the central point (e.g., "Is this positive value larger or smaller in magnitude than this negative value?").

## Exceptions

- This guidance is a caution for a secondary task (cross-midpoint comparison), not a reason to avoid diverging maps altogether. Diverging colormaps remain highly effective for their primary purpose: highlighting where and how much values deviate from a critical central point.
- If the exact comparison of magnitudes across the midpoint is not a primary task, this issue is less critical.

## Trade-offs

- **Task-Appropriateness vs. Perceptual Ambiguity:** Diverging palettes are excellent for showing deviation but may be suboptimal for comparing the magnitudes of those deviations across the center. The choice to use one depends on the primary communication goal.

## Signs of Trouble

- **Midpoint Ambiguity:** When looking at the chart, it's difficult to confidently tell if a light blue value is closer to or further from the gray center than a light orange value is.
- **User Confusion:** Viewers express uncertainty or make errors when asked to compare the absolute values of data points on opposite ends of the scale.

## How to Improve

- **Quick Fix: Add Data Labels or Tooltips.** If precise comparison is needed, provide the exact data values through direct labels or interactive tooltips. This gives viewers an "escape hatch" to verify their perceptual judgment with numerical data.

- **Moderate Redesign: Ensure Symmetric Luminance.** Use a diverging palette that is carefully constructed to have a symmetrical and perceptually linear luminance ramp on both sides of the midpoint (e.g., palettes from ColorBrewer or tools like `d3-scale-chromatic`). This makes saturation/brightness a more reliable cue for magnitude, regardless of hue.
