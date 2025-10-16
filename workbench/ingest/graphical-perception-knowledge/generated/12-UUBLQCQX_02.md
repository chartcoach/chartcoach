---
id: prioritize-name-difference
title: "Use color name difference to improve palette discriminability"

tags:
  - impact:perceptual
  - impact:cognitive
  - visual:color
  - data:categorical
  - task:compare
  - task:lookup
  - audience:general

evidence:
  strength: medium
  summary: "In a study of color palette effectiveness (Gramazio et al. 2017, n=77), palettes with higher 'Name Difference' scores showed significantly faster response times (r=-0.89, p<0.005 for 3-color palettes) and lower error rates (r=-0.87, p<0.001) in a discrimination task. The authors suggest it may be a better predictor of performance than standard perceptual distance models like CIEDE2000."

sources:
  - type: research
    ref: Gramazio, Laidlaw, & Schloss, 2017
    url: https://doi.org/10.1109/TVCG.2016.2598918
    note: "Experiment 1 (n=77) found Name Difference to be the most predictive factor for response time and highly predictive of error rate, outperforming Perceptual Distance (CIEDE2000) in some conditions."
    role: primary
  - type: research
    ref: Demiralp, Bernstein, & Heer, 2014
    url: https://doi.org/10.1109/TVCG.2014.2346978
    note: "Gramazio et al. note their finding supports this earlier work, which also suggested Name Difference is a better measure of color distance for visualization."
    role: supporting
  - type: research
    ref: Heer & Stone, 2012
    url: https://doi.org/10.1145/2207676.2208548
    note: "This paper introduced the color naming model and the concept of 'Name Difference' based on crowdsourced data, providing the foundation for its use in palette generation."
    role: related

tools:
  - type: implement
    name: Colorgorical
    url: http://vrl.cs.brown.edu/color
    description: "Directly implements the 'Name Difference' metric as a core scoring function that users can optimize for when generating palettes."
  - type: learn
    name: "Heer & Stone: Color Naming Models"
    url: https://vis.stanford.edu/color-names/
    description: "An interactive visualization and explanation of the color naming data that powers the 'Name Difference' metric."

examples:
  - type: good
    description: "A palette containing 'red', 'blue', and 'green'. These colors have very high name difference; few people would ever call the red 'blue'."
  - type: bad
    description: "A palette containing 'cyan', 'teal', and 'turquoise'. While perceptually distinct in CIELAB space, they share color names and are easily confused in a legend, leading to poor performance."
---

## Guidance

When creating a categorical color palette, choose colors that are not just perceptually distant, but also have different names (a high "Name Difference").

## Why

Humans don't just perceive color; we categorize it with language. The ability to quickly and correctly distinguish colors in a chart is strongly tied to whether we would use different words to describe them. For example, it's much easier to differentiate "red" from "blue" than it is to differentiate "cyan" from "teal," even if the two pairs have a similar mathematical distance in a perceptual color space. Palettes optimized for name difference result in faster and more accurate chart reading.

### Core Principle

Visual encoding should align with cognitive categories. Because we think and communicate with words, aligning color choices with common language categories reduces the cognitive work required to decode a visualization.

## When it applies

- When creating any categorical color palette that will be decoded using a legend.
- Especially important in complex visualizations with many data points, where rapid and accurate identification of categories is crucial.
- For visualizations intended for a general audience that will rely on common color names.

## Exceptions

- **No Legend:** If all items are directly labeled, the need for linguistically distinct colors is reduced, as the viewer is not mapping color to a name via a legend.
- **Expert Audience with Domain Conventions:** If an expert audience has a well-established (and learned) convention for subtle color differences (e.g., geologists interpreting a specific color scale), their domain-specific vocabulary may override general color names.

## Trade-offs

- **Aesthetic Constraints:** Strictly optimizing for name difference might lead to a palette of primary-like colors (e.g., red, green, blue, yellow) that may not fit the desired aesthetic tone of the visualization. You may need to balance it with aesthetic goals.
- **Reduced Color Space:** It can be harder to find a large number of colors (e.g., 7-8) that all have high name difference from each other, potentially limiting your palette size more than a purely perceptual model would.

## Signs of Trouble

- **Verbal Ambiguity:** When describing the chart, people say things like "the light blueish-green one" instead of a simple color name.
- **"Is this blue or green?":** Users express confusion about how to label a color, indicating low name difference between palette entries.
- **High Error Rates:** In testing, you find that users frequently misidentify categories, even when the colors look obviously different to you on the legend. This is a classic sign that the perceptual distance is not translating to cognitive distinctiveness.

## How to Improve

- **Quick Fix: The "Say it Out Loud" Test.** Look at your palette and say the first name that comes to mind for each color. If you hesitate, or if you use the same name for two colors (e.g., "blue" for both navy and sky blue), you have a name difference problem. Replace one of the ambiguous colors.

- **Moderate Approach: Use Basic Color Terms.** Build your palette around the 11 basic color terms identified in linguistic research (black, white, red, green, yellow, blue, brown, orange, pink, purple, and gray). This provides a strong foundation of high name difference. You can then create lighter/darker variants for aesthetic purposes, as long as each color still clearly maps to its base name.

- **Comprehensive Approach: Use a Name-Aware Tool.** Use a tool like Colorgorical that has "Name Difference" built into its optimization algorithm. By giving high weight to this factor, you can algorithmically generate a palette that is optimized for linguistic distinctiveness based on large-scale experimental data.