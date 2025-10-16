---
id: avoid-rainbow-colormaps-for-ordered-data
title: "Avoid rainbow color schemes for ordered quantitative data"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:accessibility
  - impact:ethical
  - chart:map
  - chart:map.choropleth
  - chart:map.isarithmic
  - chart:heatmap
  - task:rank
  - task:compare
  - task:distribution
  - data:quantitative
  - data:ordinal
  - data:spatial
  - visual:color
  - audience:general
  - audience:expert
  - medium:static
  - medium:screen
  - access:color-vision-risk
  - access:cognitive-load-risk

evidence:
  strength: high
  summary: "A 2022 study with 534 participants found that rainbow color schemes are not intuitively ordered, leading to high error rates and variability in interpretation. This confirms decades of research showing that sequential color schemes are more effective for representing ordered data."

sources:
  - type: research
    ref: "Gołębiowska & Çöltekin, 2022"
    url: "https://doi.org/10.1109/TVCG.2020.3035823"
    note: "Found that only 38% of participants could correctly order rainbow hues, and there was high variability (101 unique orderings). In contrast, sequential schemes had over 80% consistency."
    role: primary
  - type: research
    ref: "Borland & Taylor, 2007"
    url: "https://doi.org/10.1109/MCG.2007.323435"
    note: "Classic paper summarizing why rainbow color maps are 'considered harmful' due to creating false boundaries and hiding detail."
    role: supporting
  - type: practitioner
    ref: "ColorBrewer"
    url: "https://colorbrewer2.org/"
    note: "Provides evidence-based sequential and diverging palettes as alternatives to rainbow schemes."
    role: related

tools:
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org/
    description: Provides pre-built, perceptually-uniform sequential color palettes.
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: Check how a color palette appears to people with color vision deficiencies.
  - type: learn
    name: "Why We Use Bad Color Maps and What You Can Do About It"
    url: "https://www.kennethmoreland.com/color-advice/"
    description: A detailed explanation of the problems with rainbow colormaps and better alternatives.

examples:
  - type: bad
    description: "A weather map showing temperature using a full rainbow spectrum. It's impossible to tell at a glance if green is warmer or cooler than yellow, creating ambiguity and requiring constant legend lookups."
  - type: good
    description: "A map of unemployment rates using a single-hue sequential palette (e.g., light blue to dark blue). It's immediately clear that darker regions have higher unemployment, making patterns easy to see."
---

## Guidance

Avoid using rainbow color schemes (also known as jet or spectral schemes) to represent continuous or ordered data. Instead, use a perceptually uniform sequential color scheme.

## Why

The order of hues in a rainbow is not perceptually intuitive. Humans do not naturally order colors by their wavelength (red, green, blue). This creates several problems:
1.  **Inaccurate Comparisons:** Viewers cannot reliably determine if one color represents a higher or lower value than another without constantly consulting the legend.
2.  **False Boundaries:** The abrupt changes between hues (e.g., from yellow to green) create strong visual boundaries where none may exist in the data.
3.  **Hidden Detail:** The non-uniform perceptual steps can obscure detail in some ranges while exaggerating it in others.
4.  **Accessibility Issues:** Rainbow schemes are not friendly to viewers with color vision deficiency, who may be unable to distinguish between certain hues like red and green.

### Core Principle

Visual encodings should match the structure of the data. Ordered data requires a perceptually ordered visual encoding. A sequential color scheme (e.g., light to dark) has a clear perceptual order, while a rainbow scheme does not.

## When it applies

-   When visualizing continuous quantitative data (e.g., temperature, elevation, population density).
-   When visualizing ordinal data (e.g., low, medium, high).
-   When the primary tasks are to compare values, rank regions, or identify overall patterns and distributions.
-   In chart types like heatmaps, choropleth maps, and isarithmic maps.

## Exceptions

-   **Categorical Data:** If the data is purely categorical with no inherent order (e.g., different types of fruit, political parties), a qualitative palette with distinct hues (which may include colors from the rainbow) is appropriate. The key is that there is no implied order.
-   **Highlighting:** In some niche scientific applications, specific hues are used to highlight specific values or ranges by convention. Even in these cases, it is often better to use a more principled palette.

## Trade-offs

-   **Aesthetics vs. Clarity:** Some audiences may find rainbow palettes to be vibrant or engaging. Choosing a sequential palette prioritizes perceptual accuracy and clarity over this subjective aesthetic appeal.
-   **Familiarity vs. Best Practice:** In some scientific fields, rainbow palettes are a familiar convention. Adopting a better palette might require a brief adjustment period for an expert audience, but will ultimately lead to better interpretation.

## Signs of Trouble

-   **The "Yellow-Green Problem":** You cannot tell at a glance if green is a higher or lower value than yellow.
-   **False Contours:** You see sharp lines or "bands" appearing on your map or heatmap that don't correspond to significant changes in the underlying data.
-   **The Squint Test:** If you squint at the visualization, the colors do not resolve into a clear progression from light to dark.
-   **Frequent Legend Checks:** You or your viewers have to constantly look back and forth between the chart and the legend to understand the values.

## How to Improve

-   **Quick Fix: Reduce the Rainbow.** If you must use a rainbow-like palette, discretize it into a small number (3-5) of clearly ordered and labeled bins. This reduces ambiguity but doesn't solve the core perceptual issue.

-   **Moderate Approach: Use a Perceptually-Uniform Multi-Hue Palette.** Replace the rainbow scheme with a palette like Viridis, Magma, or Plasma. These palettes use multiple hues but are designed to be perceptually uniform, meaning they also vary consistently in lightness and are colorblind-safe. This maintains visual richness while improving accuracy.

-   **Comprehensive Approach: Use a Single-Hue Sequential Palette.** The most robust solution is to replace the rainbow scheme with a single-hue sequential palette (e.g., from `light blue` to `dark blue`) or a two-hue sequential palette (e.g., from `light yellow` to `dark green`). This provides the most unambiguous representation of magnitude. Tools like [ColorBrewer](https://colorbrewer2.org/) are the standard for finding these palettes.