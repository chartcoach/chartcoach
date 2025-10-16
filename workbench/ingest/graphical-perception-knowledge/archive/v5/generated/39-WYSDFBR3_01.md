---
id: use-sequential-color-for-pattern-perception
title: "Use sequential color schemes to reveal general patterns and distributions"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:map
  - chart:map.choropleth
  - chart:heatmap
  - task:distribution
  - task:trend
  - task:summary-mean
  - data:quantitative
  - data:spatial
  - visual:color
  - audience:general
  - medium:static
  - medium:screen
  - access:color-vision-risk

evidence:
  strength: medium
  summary: "A 2022 study on choropleth maps found sequential color schemes were superior to rainbow schemes for tasks involving pattern association. The smooth, perceptually-uniform progression helps users correctly interpret overall spatial patterns."

sources:
  - type: research
    ref: "Gołębiowska & Çöltekin, 2022"
    url: "https://doi.org/10.1109/TVCG.2020.3035823"
    note: "For a task requiring association of a visual profile with map regions (T7), sequential schemes led to significantly higher accuracy than rainbow schemes on choropleth maps (over 80% vs. ~60%)."
    role: primary
  - type: research
    ref: "Brewer et al., 1997"
    url: "https://doi.org/10.1111/j.1467-8306.1997.tb00811.x"
    note: "Foundational work on evaluating color schemes for choropleth maps, demonstrating that well-designed schemes improve pattern recognition."
    role: supporting

tools:
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org/
    description: The standard tool for selecting evidence-based sequential, diverging, and qualitative color schemes for maps.
  - type: implement
    name: Datawrapper
    url: https://www.datawrapper.de
    description: Charting tool that provides well-designed sequential palettes as defaults for choropleth maps.

examples:
  - type: good
    description: "The New York Times uses a sequential color palette to show COVID-19 case rates. The clear light-to-dark progression makes it easy to spot hotspots and identify broad regional trends at a glance."
  - type: bad
    description: "A heatmap of website clicks using a rainbow palette. The abrupt color changes make it difficult to identify the overall shape of the primary engagement area, as the eye is drawn to the high-contrast boundaries rather than the data's distribution."
---

## Guidance

To help viewers identify general patterns, trends, and distributions in spatial data, use a perceptually uniform sequential color scheme.

## Why

A sequential color scheme (e.g., progressing from a light to a dark shade of a single hue) creates a smooth and intuitive visual gradient. This allows the human visual system to easily group similar regions and perceive the overall "shape" of the data. Rainbow schemes, with their abrupt hue shifts, break up these patterns and can create misleading visual clusters, hindering the viewer's ability to see the bigger picture.

### Core Principle

Make the most important comparisons the easiest to see. If the goal is to see the overall pattern, the color scheme should facilitate the perception of that pattern, not draw attention to arbitrary boundaries between individual values.

## When it applies

-   When the primary task for the viewer is to understand the overall distribution of data across a map or heatmap.
-   When identifying hotspots, cold spots, or regional clusters is more important than looking up specific values.
-   For tasks like "associate pattern" or "rank regions by average value."

## Exceptions

-   When the primary task is to look up a specific value or locate a specific category, a high-contrast palette might be faster, even if it obscures the overall pattern (see: `consider-high-contrast-for-lookup`).

## Trade-offs

-   **Detail vs. Overview:** A single-hue sequential scheme is excellent for seeing the overall pattern but may make it harder to distinguish between two adjacent values that have very similar light-ness. Multi-hue sequential schemes (like Viridis) can be a good compromise.

## Signs of Trouble

-   **Can't See the Forest for the Trees:** Viewers can read individual values but struggle to describe the overall trend or shape of the data (e.g., "Where are the cases concentrated?").
-   **Misleading Clusters:** The color scheme creates strong visual groupings that are artifacts of the palette (e.g., a "yellow" region next to a "green" region) rather than meaningful clusters in the data.
-   **Difficulty Comparing Regions:** It's hard to tell if one large region has a higher or lower average value than another without mentally averaging all the different colors within it.

## How to Improve

-   **Switch to Sequential:** Replace the non-sequential or rainbow palette with a sequential one from a trusted source like [ColorBrewer](https://colorbrewer2.org/).
-   **Choose Single-Hue for Clarity:** For maximum clarity in pattern perception, use a single-hue sequential palette (e.g., YlOrBr, Blues, Greens).
-   **Use Multi-Hue for More Steps:** If you need to represent many different levels of data and want more visual distinctness than a single hue provides, use a perceptually-uniform multi-hue sequential palette (e.g., YlGnBu from ColorBrewer, or Viridis). This offers a good balance between pattern perception and discriminability.