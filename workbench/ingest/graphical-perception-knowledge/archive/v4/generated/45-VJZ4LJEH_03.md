---
id: diverging-midpoint-comparison-risk
title: "Use caution with comparisons across the midpoint of a diverging colormap"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:heatmap
  - chart:bar
  - chart:map.choropleth
  - task:compare
  - data:quantitative
  - visual:color
sources:
  - type: research
    ref: Liu & Heer, 2018
    url: https://doi.org/10.1145/3173574.3174172
    note: "The study found that users were significantly more prone to errors when making comparisons that crossed the central boundary of the 'blueorange' diverging colormap."
---

## Guidance

Be aware that comparisons between values on opposite sides of a diverging colormap's neutral midpoint can be less accurate than comparisons made within a single hue on one side.

## Why

When a viewer compares two values that straddle the neutral midpoint of a diverging colormap (e.g., a light blue vs. a light orange), the shift in hue interferes with the perceptual judgment of magnitude. The brain has to compare two different colors to a central, often achromatic (white or gray), point. This is a more complex perceptual task than comparing two shades of the same color, and research shows it leads to higher error rates.

## When it applies

- When using a diverging colormap (e.g., blue-orange, red-blue) to show deviation from a central value.
- When the user's task requires making precise comparisons of values that are close to, and on opposite sides of, the midpoint (e.g., determining if -2 is closer to 0 than +3 is).

## Exceptions

- If the primary task is simply to **categorize** values as positive or negative (i.e., which side of the midpoint they fall on), rather than precisely comparing their distance from the center, this effect is less of a concern.
- When the midpoint is a critical and meaningful threshold, the color change can be beneficial for highlighting this separation, even if it harms precise comparisons across it.

## Trade-offs

- **Clarity of Separation vs. Comparison Accuracy:** The distinct hue change in a diverging colormap is excellent for clearly separating two opposing concepts (e.g., above/below average). This clarity comes at the cost of reduced accuracy when comparing values across that very separation.

## Signs of Trouble

- **Midpoint Ambiguity:** Viewers express uncertainty when asked to compare two values on opposite sides of the center (e.g., "Is this light red value further from the middle than this light blue one?").
- **Analysis focuses on "how far from zero":** If the key question users are trying to answer involves comparing the magnitude of deviation (e.g., "which region has the most extreme opinion, positive or negative?"), they may struggle.

## How to Improve

- **Quick Fix: Add Direct Labels.** If precise comparisons are needed, add data labels to the visualization. This provides an "escape hatch" for users to read the exact values instead of relying solely on color perception.

- **Moderate Redesign: Use a Different Chart Type.** If comparing deviation magnitude is the primary task, switch to a chart that uses position instead of color. A diverging bar chart, where bars extend left and right from a central baseline, makes these comparisons much more accurate and intuitive.
