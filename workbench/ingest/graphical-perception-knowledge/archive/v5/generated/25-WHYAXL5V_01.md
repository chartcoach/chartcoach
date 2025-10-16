---
id: avoid-hue-for-ordered-data
title: "Avoid using color hue or orientation to encode ordered quantitative data"

tags:
  - impact:perceptual
  - impact:ethical
  - task:rank
  - task:find-extremum
  - task:correlation
  - data:quantitative
  - data:ordinal
  - visual:color
  - visual:orientation
  - audience:general

evidence:
  strength: medium
  summary: "A 2016 study found that color hue and orientation were the least accurate visual channels for finding min/max values. Hue was also perceived as less ordered than the underlying data, making it poor for judging data trends or correlation."

sources:
  - type: research
    ref: "Chung et al., 2016"
    url: "https://doi.org/10.1111/cgf.12889"
    note: "Across two experiments, color hue and orientation consistently ranked at or near the bottom for both accuracy in finding extrema (Experiment 2) and for creating a perception of order (Experiment 1)."
    role: primary
  - type: research
    ref: "Cleveland & McGill, 1984"
    url: "https://doi.org/10.2307/2288400"
    note: "Foundational work that established perceptual hierarchies, placing channels like position and length far above color and angle (related to orientation) for quantitative tasks."
    role: supporting

---
## Guidance
Do not use color `hue` (e.g., red, green, blue) or `orientation` (the angle of a line or shape) to represent ordered quantitative or ordinal data. These channels are not perceptually ordered and lead to high error rates.

## Why
The human visual system does not naturally perceive an intrinsic order in color hues (e.g., is green "more" or "less" than blue?) or in the rotation of an object. When a viewer sees a sequence of different hues, their brain treats them as distinct categories, not as a progression along a scale. This makes it very difficult and error-prone to judge rank, order, or identify extreme values.

### Core Principle
Visual encodings should match the structure of the data. Ordered data requires a perceptually ordered visual channel (like position, length, size, or saturation). Using a categorical channel (like hue or shape) for ordered data creates a perceptual mismatch.

## When it applies
- When encoding any quantitative or ordinal data (e.g., temperature, revenue, survey ratings).
- When the user needs to perform tasks like ranking, comparing magnitudes, judging trends, or finding the smallest/largest values.
- This applies to glyphs, points in a scatterplot, lines, bars, and any other visual mark.

## Exceptions
- `Hue` is an excellent channel for **categorical** (nominal) data, where the goal is to distinguish between separate, unordered groups.
- A very limited, culturally conventional set of hues might imply order (e.g., a traffic light red-yellow-green for "bad-neutral-good"), but this is not generalizable and is highly context-dependent.
- `Orientation` or `angle` can be effective in specific chart types where it is mapped to a common scale, such as in a pie chart (though angle is still less accurate than position). The guideline applies to its use as an encoding for individual glyphs in a sequence.

## Trade-offs
There are few trade-offs to following this rule for ordered data. Sticking to perceptually ordered channels like position, size, or color value/saturation will almost always improve clarity and reduce errors. The main "cost" is giving up the use of multiple colors, but the gain in interpretability is worth it.

## Signs of Trouble
- **Rainbow Legend:** The chart's legend shows a sequence of distinct hues (red, orange, yellow, green, blue...) for a continuous or ordered variable.
- **Inability to Rank:** When looking at two marks, a viewer cannot immediately say which one represents a larger value without consulting the legend.
- **Slow, Error-Prone Interpretation:** Viewers have to constantly refer back to the legend to decode the values, and they frequently make mistakes when judging order or magnitude.
- **"What does this color mean?"** If this question is frequently asked, it's a sign the color encoding is not intuitive.

## How to Improve
- **Quick Fix: Switch to a Sequential Palette.** If you are using a rainbow `hue` scale, replace it with a sequential color scale. This can be a single hue that varies in lightness/saturation (e.g., light blue to dark blue) or a grayscale ramp. This changes the encoding from `hue` to `value` and/or `saturation`, which are perceptually ordered.
- **Moderate Redesign: Switch the Visual Channel.** Instead of color, encode the ordered data using a more effective channel like `size` (for glyphs) or `position` (by switching to a bar or dot plot). Reserve color `hue` for an important categorical variable if one exists.
- **Comprehensive Approach: Re-evaluate Encodings Holistically.** Review all data attributes and user tasks. Assign the most effective visual channels (like position, length, size) to the most important quantitative comparisons. Use less effective channels like `hue` for secondary or categorical information.
