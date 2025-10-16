---
id: recognize-shape-interferes-with-color
title: "Recognize that shape significantly interferes with color perception"
tags:
  - impact:perceptual
  - chart:scatter
  - task:compare
  - task:cluster
  - data:categorical
  - visual:shape
  - visual:color
  - medium:screen
sources:
  - type: research
    ref: Smart & Szafir, 2019
    url: https://doi.org/10.1145/3290605.3300899
    note: "The study found a strong, asymmetric relationship between shape and color. The choice of mark shape had a significant effect on a viewer's ability to discriminate between colors (Experiment 1). Conversely, the mark's color had a very small, almost negligible effect on shape perception, only occurring at extreme lightness values (Experiment 2)."
---
## Guidance

When designing visualizations that use both shape and color (e.g., multiclass scatterplots), recognize that these channels are not independent. The choice of `shape` has a much stronger influence on `color` perception than `color` has on `shape` perception.

## Why

Conventionally, shape, size, and color are treated as "separable" channels, meaning one can be interpreted without interference from another. This research demonstrates this is not true; there is an asymmetric interference. The geometry of a shape (e.g., filled vs. unfilled, dense vs. sparse) changes how effectively we perceive its color. However, changing a shape's color (unless it's nearly invisible against the background) does not significantly impact our ability to identify the shape itself. Therefore, shape decisions should be made with their impact on color perception in mind.

## When it applies

- In any chart, particularly scatterplots, that uses `shape` to encode one variable (typically categorical) and `color` to encode another.
- When selecting a shape palette for a visualization where color discrimination is an important task.

## Exceptions

- When color is not used to encode data (e.g., all marks are the same color).
- When shapes are very large, the interference effect may be reduced as there is ample color information regardless of the shape's geometry.

## Trade-offs

- **Design Freedom vs. Perceptual Performance:** Prioritizing perceptually optimal shapes (e.g., all filled circles) to maximize color performance may limit design variety or the ability to encode a categorical variable with shape. You are trading expressive range for perceptual accuracy.

## Signs of Trouble

- **Inconsistent Color Perception:** Users' ability to distinguish between two colors changes depending on the shapes the colors are applied to. For example, they can easily tell light green and teal apart on filled circles, but not on hollow plus signs.
- **Shape-Dependent Color Palettes:** A color palette that works well for one set of shapes fails when applied to a different set of shapes in another chart.
- **Over-reliance on Color:** The design relies heavily on color to distinguish important categories, but uses shapes (e.g., thin, open shapes) that are known to weaken color perception.

## How to Improve

- **Quick Fix: Choose Better Shapes.** When using color, prioritize shapes that support color perception. As a general rule, opt for filled shapes over unfilled ones, and prefer shapes with higher visual density (more pixels for a given size).

- **Moderate Redesign: Prioritize the Encoding.** Decide which variable is more important. If the color-encoded variable is primary, use a single, perceptually optimal shape (like a filled circle) for all marks to ensure color is perceived accurately. If the shape-encoded variable is primary, ensure the shapes are highly discriminable and accept that the color encoding may be less effective.

- **Comprehensive Approach: Test Your Encodings.** If using a novel set of shapes or if perceptual accuracy is paramount, conduct a small user test. Check if viewers can reliably distinguish the colors in your chosen palette when applied to your chosen shapes at the target size.