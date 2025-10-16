---
id: vary-lightness-in-palettes
title: "Vary lightness in categorical palettes to improve both preference and discriminability"
tags:
  - impact:perceptual
  - impact:aesthetic
  - impact:accessibility
  - access:color-vision-risk
  - visual:color
  - data:categorical

evidence:
  strength: medium
  summary: "The Pair Preference model in Gramazio et al. (2016) identifies lightness contrast as a key driver of aesthetic preference. Lightness variation also inherently increases perceptual distance, aiding discriminability. This is a 'win-win' technique that improves both clarity and visual appeal, and is crucial for accessibility."
sources:
  - type: research
    ref: Gramazio et al., 2016
    url: https://doi.org/10.1109/TVCG.2016.2598918
    note: "Identifies lightness contrast (ΔL) as a positive term in the Pair Preference regression model, indicating it contributes to higher preference ratings."
    role: primary
  - type: practitioner
    ref: "Designing for colorblindness by We Are Colorblind"
    url: https://wearecolorblind.com/articles/designing-for-colorblindness-part-1-of-3/
    note: "Emphasizes that relying on hue alone is problematic and that good contrast in lightness and saturation is key for accessibility."
    role: related
tools:
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: Provides tools to check a palette's lightness steps and simulate its appearance for users with color vision deficiencies.
  - type: validate
    name: "Leonardo"
    url: https://leonardocolor.io/
    description: Generates color palettes based on a target contrast ratio, ensuring good lightness variation.

examples:
  - type: good
    description: A palette like ColorBrewer's 'Dark2' which includes colors with noticeably different lightness values (e.g., a light green, a medium orange, and a dark purple).
  - type: bad
    description: A palette where all colors are pastel or all are dark, with very similar lightness levels. The colors might look distinct in hue but become hard to tell apart when viewed in grayscale or by someone with color vision deficiency.
---
## Guidance

When creating a categorical color palette, ensure the colors have a noticeable variation in lightness (some light, some medium, some dark).

## Why

Varying lightness is a powerful, 'win-win' technique. It makes colors easier to tell apart, which improves discriminability. At the same time, the Pair Preference model shows that lightness contrast contributes to more aesthetically pleasing color combinations. Crucially, palettes with good lightness variation are more robust for viewers with color vision deficiencies, who may not be able to distinguish hues but can still perceive differences in lightness.

## When it applies

- Always, when creating a categorical color palette.
- Especially important when accessibility for color-vision-deficient users is a priority.
- When you want to ensure your visualization is still readable when printed in grayscale.

## Exceptions

- None known. Varying lightness is a broadly beneficial practice for categorical palettes.

## Trade-offs

- There are no significant perceptual or aesthetic trade-offs. The main challenge is the effort required to create or select a palette with good lightness variation, but the benefits are substantial.

## Signs of Trouble

- **The Muddy Middle:** All colors in the palette have a similar mid-range lightness, making them appear to blend together.
- **Grayscale Test Fail:** When you convert the visualization to grayscale (or use a colorblindness simulator), you can no longer distinguish the categories.
- **Low Contrast Pairs:** The palette contains pairs of colors that are different in hue but very similar in lightness (e.g., a medium red and a medium green).

## How to Improve

- **Quick approach:** Use the "grayscale" filter on your computer or in design software to check your current chart. If categories become indistinguishable, your palette lacks lightness variation.
- **Moderate approach:** Take your existing palette and use a color picker with HSL/HSB (Hue, Saturation, Lightness/Brightness) sliders. Manually adjust the 'L' or 'B' value for each color to create more separation. Aim for clear steps in lightness across the palette.
- **Comprehensive approach:** Use a tool like Leonardo or Viz Palette that is explicitly designed to create and validate palettes with good lightness (and contrast) variation. Generate a new palette that is demonstrably accessible and perceptually distinct.