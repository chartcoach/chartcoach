---
id: balance-color-discriminability-and-preference
title: "Balance Discriminability and Preference in Categorical Color Palettes"

impact:
  - perceptual
  - aesthetic
  - cognitive
  - accessibility
  - ethos
  - pathos
tags:
  - color
  - color-palette
  - categorical-data
  - aesthetics
  - discriminability
  - comparison
  - identification

sources:
  - type: research
    ref: Gramazio et al., 2017
    url: https://doi.org/10.1109/TVCG.2016.2598918
    note: "Presents Colorgorical, a tool and model for generating palettes that balance user-defined weights for discriminability (Perceptual Distance, Name Difference) and aesthetic preference (Pair Preference). Experiments show these palettes can be as effective and more preferable than industry standards."

tools:
  - type: implement
    name: Colorgorical
    url: http://vrl.cs.brown.edu/color
    description: "Generates custom categorical color palettes by balancing sliders for discriminability and aesthetic preference. The tool from the source paper."
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: "Lets you test color palettes on sample charts and simulate for various forms of color vision deficiency."
  - type: learn
    name: "Datawrapper: A detailed guide to colors in data vis"
    url: https://blog.datawrapper.de/beautiful-colors-for-your-data-visualizations/
    description: "A practical guide to choosing and using colors effectively in data visualization."

examples:
  - type: good
    description: "A palette where colors are clearly distinct yet visually harmonious, making it easy to identify categories without being jarring. The colors are balanced for both discriminability and aesthetic preference."
  - type: bad
    description: "A palette of several similar shades of blue. While aesthetically pleasing due to its harmony, the lack of distinction makes it nearly impossible to tell the categories apart, defeating the purpose of the encoding."
  - type: bad
    description: "A palette using highly saturated, disparate colors like bright red, lime green, magenta, and cyan. While highly discriminable, the combination is visually jarring and unpleasant, reducing engagement."
---

## Guidance

When creating a color palette for categorical data, intentionally balance the need for colors to be easily told apart (discriminability) with the need for them to be visually pleasing (aesthetic preference). Don't maximize one at the expense of the other.

## Why

There is an inherent tension between color discriminability and preference.
-   **Preference** often increases with hue similarity (e.g., different shades of blue). However, too much similarity makes colors hard to distinguish.
-   **Discriminability** often increases with hue distance (e.g., red, green, and blue). However, highly distinct colors can create a chaotic or visually jarring effect.

Finding a balance ensures your visualization is both effective (viewers can accurately decode the data) and engaging (viewers find it pleasant to look at). Research shows that algorithmically generated palettes that balance these factors can be as effective as, and often more preferable than, expert-curated industry standards.

## When it applies

- When using color to encode distinct categories (i.e., nominal data).
- For any chart type that relies on categorical color, such as grouped bar charts, stacked area charts, line charts with multiple series, or scatter plots where points are colored by category.
- When you need to create a custom palette with a specific number of colors that goes beyond standard sets like ColorBrewer.

## Exceptions

- **Purely functional, high-density plots:** If the primary goal is expert analysis where speed and accuracy are paramount and aesthetics are irrelevant, you can prioritize discriminability above all else.
- **Branded or artistic visualizations:** If the color is primarily decorative or must adhere to a strict brand palette, aesthetic concerns may override the need for optimal data discriminability. In this case, consider using other channels (like shape, labels, or position) to distinguish categories.

## Trade-offs

- **Clarity vs. Aesthetics:** The central trade-off. Pushing for maximum aesthetic harmony can make your chart unreadable. Pushing for maximum discriminability can make it ugly. You must find a "good enough" point for both.
- **Flexibility vs. Simplicity:** Using pre-made palettes (like ColorBrewer) is simple but limiting. Creating a custom-balanced palette offers more flexibility but requires more effort or the use of specialized tools.

## Evaluate

- [ ] Are any two colors in the palette difficult to tell apart, especially when used for small points, thin lines, or adjacent areas?
- [ ] Does the overall color combination feel visually chaotic, jarring, or unpleasant?
- [ ] Does the palette rely on hue alone, making it difficult for users with color vision deficiency to interpret? (e.g., using a red and green of similar brightness).

## Repair

1. **If colors are too similar:** Increase the perceptual distance between the most similar pairs. The easiest way is to adjust their lightness or saturation, not just their hue.
2. **If colors are jarring:** Reduce the distance between hues. Try creating an "analogous" palette (with colors near each other on the color wheel) and differentiate them primarily with lightness.
3. **Use a tool:** Use a palette generation tool like **Colorgorical** to create a new palette. Start with the default settings, then adjust the sliders for "Pair Preference" (aesthetics) and "Perceptual Distance" (discriminability) until you find a suitable balance. Always test the final palette with a colorblindness simulator.
