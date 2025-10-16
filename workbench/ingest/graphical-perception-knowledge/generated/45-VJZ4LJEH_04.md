---
id: use-hue-shape-for-nominal
title: "Use color hue, shape, or texture for nominal (categorical) data"

tags:
  - impact:perceptual
  - impact:logos
  - data:categorical
  - visual:color
  - visual:shape
  - visual:texture
  - visual:size

evidence:
  strength: high
  summary: "Mackinlay's (1986) expressiveness principles state that visual channels for nominal data should not imply a perceptual order. Color hue, shape, and texture are effective because they are perceived as distinct categories. Using ordered channels like size, length, or color saturation can mislead viewers by implying a false ranking or magnitude."

sources:
  - type: research
    ref: Mackinlay, 1986
    url: https://doi.org/10.1145/22949.22950
    note: "Foundational paper on automating visualization design that defines expressiveness criteria. It ranks position, color hue, texture, and shape as highly effective for nominal data."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "Review summarizing Mackinlay's theoretical rules in Table 3, recommending Color Hue (CH), Texture (T), Orientation (O), and Shape (S) for nominal data, while marking Area (Ar) and Color Saturation (CS) as unsuitable (inexpressive)."
    role: supporting

tools:
  - type: implement
    name: Colorgorical
    url: http://vrl.cs.brown.edu/color
    description: "Generates categorical color palettes optimized for perceptual difference and nameability."
---

## Guidance

When representing nominal (categorical) data, use visual channels that are perceived as distinct but unordered, such as color hue, shape, or texture. Avoid using channels that imply magnitude, such as size, length, or color saturation.

## Why

Nominal data consists of distinct categories with no intrinsic order (e.g., 'Apple', 'Orange', 'Banana'). The visual encoding used to represent this data should match this characteristic. Color hues (red, blue, green), shapes (circle, square, triangle), and textures are perceived as different without one being inherently "more" or "less" than another. In contrast, channels like size or color saturation have a strong perceptual ordering, which can cause viewers to incorrectly infer a quantitative relationship or ranking that doesn't exist in the data.

### Core Principle

A visualization is expressive when it encodes all the facts in the data and only the facts in the data. Using an ordered visual variable for unordered data violates this principle.

## When it applies

- When assigning visual properties to categories in any chart type (e.g., colors of bars, shapes of points in a scatterplot).
- When choosing how to differentiate series in a line chart or groups in a bar chart.

## Exceptions

- When categories have a conventional or metaphorical association with an ordered channel. For example, using a small, medium, and large 'T-shirt' icon to represent 'Small', 'Medium', and 'Large' sizes is appropriate because the encoding matches the data's inherent (ordinal) structure.
- When a nominal category has a strong, universally understood color association (e.g., red for 'stop' or 'negative', green for 'go' or 'positive').

## Trade-offs

- **Scalability:** The number of easily distinguishable hues, shapes, or textures is limited. It becomes very difficult to distinguish more than 7-10 distinct categories using color or shape alone. Position (e.g., in a bar chart) scales to many more categories.
- **Interpretive Load:** Shapes or textures can sometimes carry more semantic meaning than color, but they can also add visual clutter and may be harder to decode than simple color patches.

## Signs of Trouble

- **False Ordering:** A chart uses different sizes of bubbles to represent different countries, leading viewers to think that bigger bubbles mean "more" of something, when the size is arbitrary.
- **Saturation Confusion:** A chart uses light blue, medium blue, and dark blue to represent 'Product A', 'Product B', and 'Product C', suggesting that C is somehow more important or has a higher value than A.
- **Categorical Chaos:** Using a single, continuous color gradient (e.g., a blue-to-red gradient) to encode purely categorical data, making it impossible to distinguish individual categories.

## How to Improve

- **Quick Fix: Switch to a Qualitative Palette.** If using a sequential or diverging color palette for nominal data, switch to a qualitative (categorical) palette where each color is a distinct hue, with similar saturation and lightness. Tools like ColorBrewer have pre-built qualitative palettes.

- **Moderate Approach: Use a Redundant Encoding.** Combine two unordered channels to improve discriminability, especially for colorblind users. For example, use both a distinct color hue AND a distinct shape for each category in a scatterplot.

- **Comprehensive Approach: Re-evaluate the Encoding.** If you have many categories (>10), encoding them with color or shape alone will fail. Re-design the chart to use position as the primary way to distinguish categories. For example, instead of a single scatterplot with 20 different colors, use a bar chart with 20 bars, where each category gets its own unique position along the axis.