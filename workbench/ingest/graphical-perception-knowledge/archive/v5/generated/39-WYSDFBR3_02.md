---
id: consider-high-contrast-for-lookup
title: "For rapid value lookup, consider high-contrast multi-hue palettes"

tags:
  - impact:perceptual
  - impact:performance
  - chart:map
  - chart:map.choropleth
  - chart:map.isarithmic
  - task:lookup
  - task:filter
  - data:quantitative
  - visual:color
  - audience:general
  - medium:static
  - medium:screen

evidence:
  strength: medium
  summary: "In a 2022 study with 534 participants, rainbow color schemes were faster than sequential schemes for retrieving specific values from a map, and led to higher accuracy when locating values in a specific range."

sources:
  - type: research
    ref: "Gołębiowska & Çöltekin, 2022"
    url: "https://doi.org/10.1109/TVCG.2020.3035823"
    note: "For a 'retrieve value' task (T5), rainbow colors were significantly faster with no loss of accuracy. For a 'locate' task (T6), rainbow colors led to higher accuracy."
    role: primary
  - type: research
    ref: "Ware, 1988"
    url: "https://doi.org/10.1109/38.7760"
    note: "Early work suggesting that hue-varying color schemes (like rainbow) work well for reading specific details from maps because the visual system is sensitive to hue differences."
    role: related

tools:
  - type: implement
    name: Colorgorical
    url: http://vrl.cs.brown.edu/color
    description: Generates palettes of maximally distinct colors, which can be useful when lookup is the priority.
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: Useful for checking if the high-contrast colors chosen are still distinguishable for users with color vision deficiency.

examples:
  - type: good
    description: "A public transit map where each subway line is a distinct, high-contrast color. The goal is to quickly locate a specific line (e.g., 'the red line'), not to interpret an order. The distinct hues make this lookup task easy."
  - type: bad
    description: "A map of income levels using a rainbow palette. While it might be fast to 'find the green area,' it's very difficult to know what 'green' means in relation to 'yellow' or 'blue', hindering any task beyond simple location."
---

## Guidance

If the primary and most critical user task is to quickly locate a specific value or range on a map, consider using a palette with high-contrast, distinct hues (which may include rainbow-like schemes).

## Why

High contrast between distinct hues makes it easier for the visual system to find and segment regions of a specific color. This can speed up "search and find" tasks compared to using a sequential palette, where adjacent values may be represented by very similar shades. The user can quickly find "the red area" or "the blue area" without needing to perceive subtle differences in lightness.

### Core Principle

Optimize the visual encoding for the most important task. If speed of lookup is more critical than accuracy of comparison or pattern perception, the encoding should prioritize discriminability over perceptual ordering.

## When it applies

-   When the main user goal is to locate a known value or range (e.g., "Find all areas where the value is between 10-15%").
-   When the speed of finding a specific region is more important than understanding its value relative to others.
-   This is a narrow exception to the general rule of avoiding rainbow palettes.

## Exceptions

-   This guidance does not apply if the user also needs to understand the order of values, compare regions, or identify overall patterns. In those common cases, a sequential palette is superior.
-   This approach is still problematic for users with color vision deficiency. If accessibility is a priority, this exception should be avoided.

## Trade-offs

-   **Speed vs. Understanding:** You gain speed for lookup tasks but sacrifice the user's ability to intuitively understand the data's order, see patterns, or make accurate comparisons. This is a significant trade-off and should be made consciously.
-   **Inclusivity:** This approach is generally not accessible to users with color vision deficiencies, who may not be able to distinguish the hues.

## Signs of Trouble

-   **One-Trick Pony:** The visualization is fast for finding specific colors, but users are making errors when asked to compare values or describe trends.
-   **Accessibility Complaints:** Users with color vision deficiencies report that they cannot distinguish between different colored regions.
-   **Misleading Interpretations:** Users incorrectly assume an order to the colors (e.g., "green is more than yellow") or see false patterns due to the high-contrast boundaries.

## How to Improve

-   **Combine with Other Channels:** If you use a high-contrast palette for lookup, consider adding redundant encodings like patterns, textures, or clear labels to help mitigate the loss of understanding.
-   **Use a Discretized Palette:** Instead of a continuous rainbow, use a small number of distinct, named colors. This reinforces the "lookup" nature of the task and discourages attempts to interpret it as a continuous scale. For example, use 5 distinct colors for 5 distinct ranges and provide a clear legend.
-   **Prioritize a Better Palette:** In most cases, the small gain in lookup speed is not worth the significant loss in interpretation and accessibility. Revert to a perceptually-uniform sequential palette and use other methods (like direct labels or interactive highlighting) to support lookup tasks.