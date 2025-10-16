---
id: use-distinct-hues-for-value-lookup
title: "For rapid value lookup, consider perceptually distinct hues, but understand the risks"

tags:
  - impact:perceptual
  - impact:performance
  - visual:color
  - data:quantitative
  - task:lookup
  - task:filter
  - chart:map
  - chart:map.choropleth
  - chart:map.isarithmic

sources:
  - type: research
    ref: Gołębiowska & Çöltekin, 2022
    url: https://doi.org/10.1109/TVCG.2020.3035823
    note: "In tasks requiring users to locate specific value ranges (e.g., T6: 'locate'), rainbow colormaps (RC) led to faster or comparable performance than sequential colormaps (SC), likely because the large hue contrasts facilitate visual search for a specific color patch."

tools:
  - type: implement
    name: IWantHue
    url: https://medialab.github.io/iwanthue/
    description: Generates palettes of perceptually distinct colors.
  - type: implement
    name: Color-Culled palettes
    url: https://github.com/Demiralp/Perceptual-Kernels
    description: Palettes from Demiralp et al. (2014) designed to maximize perceptual distance for specific encodings.
  - type: learn
    name: "Why to use a rainbow color scale"
    url: https://www.youtube.com/watch?v=pBuI2t-kDoI
    description: A contrarian take by data scientist Matt Hall arguing for the utility of rainbow-like scales in specific expert contexts, particularly for spotting anomalies.

examples:
  - type: good
    caption: Interactive Highlighting
    description: An ideal approach is to use a proper sequential colormap by default, but provide an interactive control (like a slider or legend hover) that highlights a specific value range. This supports both accurate comparison and rapid lookup.
  - type: bad
    caption: Rainbow Colormap used for General Analysis
    description: This chart uses a rainbow colormap. While a user might be ableto quickly find the 'yellow' regions, they cannot easily tell if yellow is a higher or lower value than the adjacent green, harming overall analysis.
---

## Guidance

If the primary and most critical user task is the rapid location of a specific, known data range (e.g., "Find all areas where the value is between 10 and 15%"), a colormap with highly distinct, high-contrast hues (such as a rainbow scheme) can sometimes improve performance speed. However, this is a significant trade-off that harms most other analytical tasks.

## Why

When a user is searching for a specific value range, the task becomes one of visual search: finding all instances of a target color. Colormaps with large perceptual steps between adjacent colors (e.g., the jump from green to yellow in a rainbow) make each color category "pop," making it easier and faster to spot and isolate the target color across the visualization. In contrast, in a smooth sequential scheme, the subtle differences between adjacent steps can make it harder to precisely identify the boundaries of the target range.

## When it applies

- The user's primary, time-sensitive task is to **locate** or **filter** for a specific data range.
- **Speed** of locating these specific ranges is more important than the ability to compare, rank, or see overall trends.
- The audience consists of experts who may have been trained on this convention (a common but problematic practice in some scientific fields).
- You have provided other means (like tooltips or direct labels) to compensate for the colormap's poor comparability.

## Exceptions

- Do **not** apply this if the user needs to understand trends, compare values, or rank different regions. A sequential color scheme is far superior for these tasks.
- Do **not** apply this if the visualization is for a general audience or if accessibility for colorblind users is a requirement. Rainbow colormaps are not accessible and are broadly unintuitive.
- This guidance is an exception to the primary, more important rule: [Avoid rainbow colormaps for ordered data](avoid-rainbow-colormaps-for-ordered-data).

## Trade-offs

- **Speed for Clarity:** You gain potential speed on a single task (lookup) at the major expense of clarity, comparability, and interpretability for all other tasks.
- **Performance for Accessibility:** You optimize for a potential speed gain for some users while making the visualization unreadable for users with color vision deficiency.
- **Risk of Misinterpretation:** By choosing a colormap that is poor for comparison, you increase the risk that users will draw incorrect conclusions about the data's structure, even if they can find specific values quickly.

## Signs of Trouble

- **Fast but Wrong:** Users can quickly point to a color but make errors when asked to compare it to another color (e.g., "Is the red area higher or lower than the blue area?").
- **Analysis Paralysis:** When asked to describe the overall pattern, users are unsure where to start because the colors provide no intuitive sense of order or magnitude.
- **Over-reliance on Legend:** Despite the "pop" of the colors, users still have to constantly check the legend to decode the meaning, defeating the purpose.

## How to Improve

- **Quick Fix: Add Interactive Tooltips.** If you must use a rainbow-like scheme, ensure that hovering over any part of the visualization displays a tooltip with the exact data value. This provides an "escape hatch" for users who need to make precise comparisons.

- **Moderate Redesign: Use a Binned (Discretized) Sequential Scheme.** Instead of a smooth sequential gradient, use a sequential scheme with a few distinct bins (e.g., 5-7 steps). This gives you clearly delineated color categories that are easier to spot than a smooth gradient, while still maintaining a clear perceptual order.

- **Comprehensive Redesign: Implement Interactive Filtering.** Use a proper sequential or diverging colormap as the default. Then, add an interactive element like a range slider or clickable legend that allows the user to **highlight** their desired data range on demand. This provides the best of both worlds: a clear, interpretable base visualization and a powerful tool for rapid lookup.