---
id: use-rainbow-for-value-lookup-with-caution
title: "Use high-contrast rainbow schemes for fast value lookup, but only with caution"

tags:
  # Impact dimensions (select all that apply)
  - impact:perceptual
  - impact:performance
  - impact:accessibility

  # Chart types (use hierarchy with dots for specificity)
  - chart:map
  - chart:map.choropleth
  - chart:map.isarithmic

  # Tasks (what the user is trying to accomplish)
  - task:lookup
  - task:filter

  # Data characteristics
  - data:quantitative
  - data:spatial

  # Visual channels
  - visual:color
  - visual:color.hue

  # Audience characteristics
  - audience:expert
  - audience:general

  # Medium/format
  - medium:static
  - medium:screen

  # Accessibility risks
  - access:color-vision-risk
  - access:cognitive-load-risk

evidence:
  strength: medium # Options: high | medium | low
  summary: "In a study of map-reading tasks (n=534), Gołębiowska & Çöltekin (2020) found that rainbow colormaps could outperform sequential schemes for specific value lookups. For a 'locate' task, the rainbow scheme led to significantly higher accuracy (p<0.001). For a 'retrieve value' task, it was significantly faster (p<0.05), though accuracy was similar. This benefit is limited to value lookups and comes at a high cost to other tasks."

sources:
  - type: research
    ref: Gołębiowska & Çöltekin, 2020
    url: https://doi.org/10.1109/TVCG.2020.3035823
    note: "Study (n=534) found that for a 'locate' task (T6), rainbow was more accurate than sequential. For a 'retrieve value' task (T5), rainbow was faster than sequential. This suggests an advantage for tasks involving matching a specific color to a legend."
    role: primary # Options: primary | supporting | related
  - type: research
    ref: Ware, 1988
    url: https://doi.org/10.1109/2945.8950
    note: "Early work suggesting that hue-varying schemes like rainbow work well for reading specific details from maps."
    role: supporting

tools:
  - type: implement
    name: "d3-scale-chromatic"
    url: https://github.com/d3/d3-scale-chromatic
    description: "Provides various D3 colormaps, including the problematic 'd3.interpolateRainbow'. Use with caution."
---

## Guidance

For the specific and narrow task of looking up a value at a location by matching a color to a legend, a high-contrast rainbow colormap can enable faster or more accurate performance than a standard sequential scheme. However, this approach should be used with extreme caution as it severely impairs other critical tasks like pattern recognition and magnitude comparison.

## Why

The distinct and easily nameable hues in a rainbow colormap (e.g., "blue," "green," "red") can function as categorical labels. This transforms the lookup task into a faster visual search and matching process, where the user quickly finds the target color on the map and matches it to the legend. In contrast, finding a specific shade in a subtle, single-hue sequential gradient can be more difficult and time-consuming.

### Core Principle

Distinct, nameable colors facilitate faster visual search and matching tasks compared to subtle variations in a continuous gradient.

## When it applies

- The **single most important and frequent task** for the user is to determine the value at a specific point (e.g., "What is the temperature at this exact coordinate?").
- The visualization is static and not interactive (e.g., in print).
- Pattern recognition, trend analysis, and comparison of magnitudes between different regions are not important goals.

## Exceptions

- **Interactivity is available:** If users can hover or click to see a tooltip with the exact value, the benefit of the rainbow colormap for lookups becomes irrelevant. An interactive sequential map is superior.
- **Accessibility is a concern:** Standard rainbow colormaps are not perceivable by many users with color vision deficiencies.
- **Pattern detection is needed:** If users need to see trends, clusters, or the overall shape of the data, a rainbow map is a poor choice.

## Trade-offs

- **You sacrifice pattern perception for lookup speed.** This is a major trade-off. Using a rainbow map makes it very difficult to see overall trends, gradients, or the "shape" of the data.
- **You sacrifice accessibility.** Standard rainbow maps are inaccessible to users with common forms of colorblindness (e.g., deuteranopia).
- **You risk misinterpretation of magnitudes.** Users may incorrectly infer relationships between values based on the non-perceptual color ordering.

## Signs of Trouble

- **One-Trick Pony:** The chart is fast for finding a single value but fails when users are asked to describe the overall trend or compare two non-adjacent regions.
- **User Complaints:** Users say, "I can't see the big picture" or "I don't know if red is higher or lower than green without looking at the legend every time."
- **Accessibility Audit Fail:** Colorblindness simulators show that large parts of the map become an indistinguishable mush.

## How to Improve

- **Quick Fix: Enhance the Legend.** If you must use a rainbow colormap, ensure the legend is extremely clear, large, and always visible. Add explicit numerical labels to the color bands in the legend.

- **Moderate Approach: Use a Quantized Sequential Scheme.** Instead of a continuous gradient, use a binned (quantized) sequential scheme with 5-7 distinct, easily distinguishable steps. This provides some of the "categorical" feel that aids lookup while still maintaining a clear perceptual order.

- **Comprehensive Approach: Use a Sequential Scheme with Interactivity.** The best solution is to use a perceptually uniform sequential colormap (like Viridis) and add interactive tooltips. This provides the best of both worlds: the sequential scheme is excellent for pattern recognition, and the tooltips provide fast, precise value lookup on demand without compromising accessibility or perceptual integrity.
