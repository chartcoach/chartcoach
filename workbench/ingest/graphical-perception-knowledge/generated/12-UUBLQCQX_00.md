---
id: balance-color-discriminability-preference
title: "Balance color discriminability with aesthetic preference"

tags:
  - impact:perceptual
  - impact:aesthetic
  - impact:pathos
  - impact:ethos
  - visual:color
  - data:categorical
  - task:compare
  - task:lookup
  - audience:general

evidence:
  strength: medium
  summary: "Gramazio et al. (2017, n=137) found a direct trade-off: palettes optimized for perceptual distance (discriminability) were rated as less preferable, while palettes optimized for preference (based on hue similarity) had worse performance on discrimination tasks (e.g., error rates for 3-color palettes increased from 11% to 15% when switching from a 'Low-Error' to a 'Preferable' setting, p<0.005)."

sources:
  - type: research
    ref: Gramazio, Laidlaw, & Schloss, 2017
    url: https://doi.org/10.1109/TVCG.2016.2598918
    note: "Exp 1 (n=137) demonstrated the inverse relationship between palettes optimized for discriminability (based on perceptual/name distance) and those optimized for aesthetic preference (based on hue similarity). Both RT/error rates and preference ratings were significantly affected by this trade-off (p<0.01)."
    role: primary
  - type: research
    ref: Schloss & Palmer, 2011
    url: https://doi.org/10.3758/s13414-010-0081-8
    note: "Established the underlying model of aesthetic preference for color pairs, finding that people generally prefer pairs with similar hues and contrasting lightness."
    role: supporting
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "This survey paper's methodology involves collating such perception findings to inform visualization recommendation systems, highlighting the importance of balancing competing principles."
    role: related

tools:
  - type: implement
    name: Colorgorical
    url: http://vrl.cs.brown.edu/color
    description: "Generates categorical color palettes by allowing users to directly balance the weights of 'Pair Preference' (aesthetics) and 'Perceptual/Name Distance' (discriminability)."
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: "Allows you to see your chosen palette in various chart types and simulate how it appears to users with color vision deficiencies, helping you evaluate both aesthetic and discriminability trade-offs."

examples:
  - type: good
    description: "A palette using distinct but harmonious colors, like a triad of a primary color and two analogous secondary colors (e.g., blue, with orange-yellow and orange-red). The hues are related but different enough to be distinguished."
  - type: bad
    description: "A rainbow palette. While it has high perceptual distance between distant colors (red vs. blue), the adjacent colors (yellow vs. green) are hard to distinguish and the overall effect is often considered aesthetically jarring and lacks a natural order."
  - type: bad
    description: "A monochrome palette with very subtle lightness steps. While aesthetically pleasing and harmonious, the low perceptual distance makes it very difficult for viewers to accurately distinguish between categories, especially in complex charts."
---

## Guidance

When creating a categorical color palette, consciously balance the goal of discriminability (making colors easy to tell apart) with the goal of aesthetic preference (making the color combination visually pleasing). These two goals are often in conflict.

## Why

Colors that are perceptually far apart (e.g., red and green) are highly discriminable but can be aesthetically jarring and are often rated as less preferable. Conversely, colors that are harmoniously related (e.g., analogous or similar hues) are often rated as more aesthetically pleasing but can be difficult to distinguish from one another, leading to higher error rates and slower task performance. Finding a good balance is key to creating a chart that is both effective and engaging.

### Core Principle

Effective visualization design must satisfy both perceptual requirements (clarity, accuracy) and aesthetic/rhetorical goals (engagement, trust). A palette that fails at either can undermine the entire visualization.

## When it applies

- When choosing colors for categorical data, where each color represents a distinct group (e.g., different product lines, political parties, or survey respondents).
- In any chart type that uses color to distinguish categories, such as bar charts, line charts, scatter plots, and choropleth maps.
- When creating visualizations for a general audience, where aesthetic appeal can significantly impact engagement and trust in the data.

## Exceptions

- **Labeling is Primary:** If every colored element is directly labeled and color is used only for redundant grouping, high discriminability is less critical. You can prioritize aesthetics more heavily.
- **Highlighting/Accent Colors:** When using a palette of neutral grays with one or two "accent" colors to draw attention, the primary goal is emphasis, not balanced comparison. The accent colors should be highly discriminable from the gray, but the grays themselves can be subtle.
- **Branding Constraints:** If you are required to use a specific brand palette, you may have limited ability to optimize for both goals. In this case, the priority is to work within the given constraints, perhaps by selecting a subset of the brand colors that offer the best possible balance.

## Trade-offs

- **Prioritizing Discriminability:** You may sacrifice some aesthetic harmony. The resulting palette might feel less cohesive or visually "louder."
- **Prioritizing Aesthetics:** You will likely reduce perceptual performance. Viewers may take longer and make more errors when trying to identify and compare categories, especially if colors are not adjacent.

## Signs of Trouble

- **The Squint Test:** If you squint your eyes and look at the chart, do different color categories blur together into a single visual mass? This indicates low discriminability.
- **Back-and-Forth:** Do you find yourself (or your users) repeatedly glancing between the legend and the chart to tell which color is which? This suggests the colors are not distinct enough.
- **Aesthetic Revulsion:** Does the chart feel visually chaotic, jarring, or "ugly"? This might indicate that colors with high perceptual distance were chosen without regard for aesthetic harmony.
- **"Muddy" Palette:** Do the colors look desaturated and similar, making the chart feel washed out and hard to read? This suggests an over-correction towards harmony at the expense of discriminability.

## How to Improve

- **Quick Fix: Adjust Lightness/Saturation.** Take your preferred aesthetic palette and try increasing the lightness difference between similar hues. Or, take a highly discriminable palette and slightly desaturate the colors to reduce their intensity and make them more harmonious.

- **Moderate Approach: Use a Smart Tool.** Use a tool like Colorgorical that explicitly models the trade-off. Start with a high weight on "Pair Preference" to get an aesthetic base, then gradually increase the weight on "Perceptual Distance" or "Name Difference" until you find a palette that is both acceptable to you and has no two colors that are too similar.

- **Comprehensive Redesign: Adopt a Principled Color Strategy.** Instead of picking individual colors, choose a color scheme based on color theory, such as a "split-complementary" or "triadic" scheme. These models are designed to provide both contrast and harmony. Select a primary color, then use the model to find contrasting but related colors, and adjust their lightness and saturation for optimal balance.