---
id: distinguish-hue-recall-from-value-recall
title: "Choose colormaps based on whether users need to recall the color itself or the value it represents"

tags:
  # Impact dimensions (select all that apply)
  - impact:cognitive
  - impact:perceptual

  # Chart types (use hierarchy with dots for specificity)
  - chart:map
  - chart:map.choropleth
  - chart:map.isarithmic

  # Tasks (what the user is trying to accomplish)
  - task:lookup
  - task:compare

  # Data characteristics
  - data:quantitative
  - data:spatial

  # Visual channels
  - visual:color

  # Audience characteristics
  - audience:general

  # Medium/format
  - medium:static

evidence:
  strength: medium # Options: high | medium | low
  summary: "A study by Gołębiowska & Çöltekin (2020, n=534) found a clear dissociation in memory tasks. Rainbow colormaps were significantly better for recalling the specific hue of a region from memory (e.g., 68% vs 24% accuracy on one map type, p<0.001). Conversely, sequential colormaps were better for recalling the quantitative value that the hue represented (e.g., 60% vs 45% accuracy on another map type, p=0.036)."

sources:
  - type: research
    ref: Gołębiowska & Çöltekin, 2020
    url: https://doi.org/10.1109/TVCG.2020.3035823
    note: "Study (n=534) directly tested hue recall (T9) and value recall (T10). Rainbow schemes led to far superior accuracy in hue recall, while sequential schemes were more accurate for value recall, demonstrating a cognitive trade-off."
    role: primary # Options: primary | supporting | related
  - type: research
    ref: Lenneberg, 1961
    url: https://doi.org/10.2466/pms.1961.12.3.375
    note: "Classic work establishing that 'nameable' colors are easier to recognize and discriminate from memory."
    role: related
---

## Guidance

Distinguish between tasks that require recalling a *color's identity* versus recalling the *value it represents*. Use rainbow-like palettes with distinct, nameable hues for hue recall. Use sequential palettes with a clear lightness progression for value recall.

## Why

There is a cognitive dissociation between remembering a color's name and remembering its quantitative meaning.

1.  **Hue Recall:** Rainbow colormaps contain distinct, nameable colors (e.g., "red," "green," "blue"). These categorical labels are easy to encode and retrieve from verbal working memory.
2.  **Value Recall:** Sequential colormaps map data magnitude to a perceptual dimension (lightness). This creates a strong "darker means more" association, making it easier to remember and reconstruct the approximate value a color represented, even if you can't remember the exact shade.

### Core Principle

The 'nameability' of colors aids in recalling the color's identity (hue recall), while the perceptual ordering of colors aids in recalling the color's meaning (value recall).

## When it applies

- When designing static visualizations or animated sequences where a user sees information and must act on it from memory.
- In dashboards where a user might glance at a map and then refer to it mentally while looking at another chart.
- **For Hue Recall:** When the task is "Was Region A the red one?" or requires remembering which of several colored items was in a location.
- **For Value Recall:** When the task is "What was the approximate population density in Region A?"

## Exceptions

- **Interactive Visualizations:** If the user can always refer back to the visualization and its legend, the need for recall is diminished, and other perceptual principles (like using sequential schemes for patterns) should take priority.
- **Annotation is Possible:** If the user can directly label or annotate the chart, they can offload the memory task, making the colormap choice less critical for recall.

## Trade-offs

- **Optimizing for one type of recall hurts the other.** A colormap that is good for hue recall (rainbow) is poor for value recall and pattern recognition. A colormap good for value recall (sequential) is poor for hue recall. You must choose which memory task is more important for the user's goal.

## Signs of Trouble

- **Hue Recall Failure (with sequential):** A user says, "I know the value was high, but I can't remember if it was the dark blue or the even darker blue."
- **Value Recall Failure (with rainbow):** A user says, "I remember that region was green, but I have no idea if that means the value was high, low, or in the middle."

## How to Improve

- **To support HUE RECALL:** If remembering the specific color identity is paramount, use a palette with a small number of distinct, nameable colors. A categorical palette is often better than a full rainbow. For example, use the primary colors from the `d3-scale-category10` palette.

- **To support VALUE RECALL:** If remembering the approximate data value is most important, use a perceptually uniform sequential colormap like Viridis, Cividis, or a single-hue progression from ColorBrewer. The consistent "lightness = value" mapping provides a strong anchor for memory.

- **Combined Approach:** Use a good sequential scheme for the visualization, but add clear, memorable annotations or glyphs for key regions of interest. This allows the overall pattern to be seen, while providing a distinct visual hook for remembering specific locations.
