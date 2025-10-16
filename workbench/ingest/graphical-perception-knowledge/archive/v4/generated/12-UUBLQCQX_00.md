---
id: balance-color-discriminability-preference
title: "Balance color discriminability and aesthetic preference for categorical palettes"

tags:
  - impact:perceptual
  - impact:aesthetic
  - impact:cognitive
  - visual:color
  - data:categorical
  - chart:bar
  - chart:scatter
  - chart:line
  - chart:map
  - task:compare
  - task:lookup
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Gramazio, Laidlaw, & Schloss, 2017
    url: https://doi.org/10.1109/TVCG.2016.2598918
    note: "The paper's central thesis is a model for balancing these two competing goals. Experiments 1 and 2 demonstrate this trade-off in practice."

tools:
  - type: implement
    name: Colorgorical
    url: http://vrl.cs.brown.edu/color
    description: Generates categorical color palettes with sliders to balance discriminability and preference.
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: Lets you see how a color palette looks on different chart types and check for colorblind safety.

examples:
  - type: good
    description: A palette using analogous hues (e.g., blues and greens) but with significant differences in lightness and saturation. This maintains some harmony while ensuring categories are distinguishable.
  - type: bad
    description: A palette with highly saturated, disparate hues (like a default "rainbow" scheme). While highly discriminable, it's aesthetically jarring and lacks harmony.
  - type: bad
    description: A palette with very similar hues (e.g., multiple shades of pastel blue and green). This may feel harmonious but makes categories very difficult to tell apart, especially for small marks.
---

## Guidance

When creating categorical color palettes, intentionally balance the need for colors to be easily distinguishable (discriminability) with the need for them to be visually pleasing (aesthetic preference). Do not optimize for one at the total expense of the other.

## Why

These two goals are often in conflict. Aesthetic preference tends to increase with hue similarity (e.g., analogous colors), while discriminability decreases. Research shows that relying solely on maximizing discriminability can lead to jarring, unappealing palettes. Conversely, relying only on aesthetics can lead to palettes that are confusing and increase interpretation errors. The Colorgorical paper demonstrates a model for successfully navigating this trade-off.

## When it applies

- When using color to encode distinct categories in a visualization (e.g., different groups in a bar chart, different series in a line chart).
- When both data clarity and visual appeal are important for audience engagement and trust.

## Exceptions

- **Purely analytical tasks:** If the primary goal is rapid, accurate analysis by experts, prioritize discriminability above all else. Aesthetic appeal is secondary.
- **Primarily artistic or branding:** If the visualization is more of an art piece or a brand statement and data accuracy is less critical, aesthetic preference may take priority. However, ensure the chart does not become misleading.

## Trade-offs

- **Clarity vs. Appeal:** Optimizing for discriminability (e.g., using colors from opposite ends of the color wheel) may result in a less harmonious or "pretty" palette. Optimizing for aesthetics (e.g., using similar hues) may make it harder for viewers to tell categories apart, increasing cognitive load and error rates.

## Signs of Trouble

- **The "Circus" Palette:** The colors feel jarring, overly saturated, and disconnected, resembling a default rainbow scheme. This prioritizes discriminability over preference and can be visually overwhelming.
- **The "Muddy" Palette:** Colors are too similar in hue and lightness, making them hard to tell apart, especially for small marks like dots in a scatterplot or thin lines. This prioritizes preference over discriminability.
- **User Feedback:** Viewers complain that the chart is "ugly" or "hard to look at," or they express confusion about "which category is which."

## How to Improve

- **Quick Fix: Adjust Lightness/Saturation.** If your hues are too similar, try making some significantly lighter or darker to increase contrast. If your hues are too disparate (a rainbow), try desaturating some of the colors to reduce the jarring effect.

- **Moderate Approach: Use a Perceptually-Aware Tool.** Use a tool like Colorgorical to generate a palette. Start with its "preferable" settings and then manually tweak individual colors that are too similar, or start with "low error" settings and adjust for aesthetics.

- **Comprehensive Approach: Define Your Priority & Generate.** Use a tool with explicit controls for discriminability and preference (like Colorgorical's sliders). If clarity is key, weigh discriminability metrics higher. If appeal is key, weigh preference higher. Generate multiple options and test them using colorblindness simulators and by looking at them on actual chart examples.