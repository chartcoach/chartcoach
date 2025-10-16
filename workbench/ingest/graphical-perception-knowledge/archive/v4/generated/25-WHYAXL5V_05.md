---
id: use-countable-shape-features-for-ordered-data
title: "Use shapes with countable features to encode ordered data"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:any
  - chart:scatter
  - task:rank
  - data:quantitative
  - data:ordinal
  - data:cardinality.low
  - visual:shape
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Chung et al., 2016
    url: https://doi.org/10.1111/cgf.12889
    note: "This paper found that shape could be perceived as ordered, contrary to some theories. The reason was that the shapes used had countable, systematic features (number of spikes on a star), which effectively encoded a quantitative value."

tools:
  - type: learn
    name: "Visualizing with Glyphs"
    url: https://serialmentor.com/dataviz/visualizing-with-glyphs.html
    description: "A chapter from 'Fundamentals of Data Visualization' discussing the use of glyphs, including shape, to encode data."

examples:
  - type: good
    description: "A scatterplot where the shape of each point represents a rating from 1 to 4, encoded as a star with 3, 4, 5, or 6 points. The increasing number of points provides a clear, ordered visual cue."
  - type: bad
    description: "A scatterplot where the same 1-4 rating is encoded with arbitrary shapes: a circle, a square, a triangle, and a cross. There is no intuitive order to these shapes, forcing the user to constantly consult the legend."
---

## Guidance

To encode low-cardinality ordered data, you can use a set of shapes that vary systematically along a countable dimension (e.g., number of sides, number of points). Avoid using a set of arbitrary, non-ordered shapes for quantitative or ordinal data.

## Why

While arbitrary shapes (like circles, squares, and triangles) are excellent for categorical data, they do not have an inherent perceptual order. However, research shows that if shapes are designed to have a clear, countable feature that increases or decreases, they can be effectively used to represent ordered data. The act of counting (e.g., "this star has more points than that one") creates the perception of order. This provides an extra visual channel for encoding data when more effective channels like position, size, and color are already in use.

## When it applies

- When you need to encode a second or third ordered variable with low cardinality (e.g., 3-5 steps like "low, medium, high").
- When other, more effective visual channels (position, size, color value) are already being used for other data variables.
- In scatterplots or maps where you need an additional channel to encode information on each glyph.

## Exceptions

- **High Cardinality:** This method is not suitable for data with many distinct values, as counting features becomes difficult and slow. It works best for 3-5 distinct steps.
- **High Cognitive Load:** Using shape is more cognitively demanding than using size or color value. If the task needs to be very fast or effortless, prefer a different channel.
- **Primary Comparison:** Shape should not be the *primary* channel for important quantitative comparisons. It is best used as a secondary or tertiary encoding.

## Trade-offs

- **Flexibility vs. Cognitive Load:** This technique gives you an additional ordered channel to work with, but at the cost of increased cognitive effort for the viewer compared to channels like size or color.
- **Design Effort:** Creating a good, systematic set of shapes requires more design consideration than simply picking from a default set of arbitrary shapes.

## Signs of Trouble

- **Arbitrary Shapes:** The legend shows shapes like 'circle', 'plus', 'diamond', and 'triangle' mapped to ordered data like '1', '2', '3', '4'.
- **Constant Legend-Checking:** Viewers have to repeatedly look back and forth between the chart and the legend to understand the order of the shapes.
- **Complex Shapes:** The shapes are too complex or the countable feature is too subtle, making it difficult for viewers to quickly perceive the order.

## How to Improve

- **Quick Fix: Switch to a Different Channel.** If possible, the easiest fix is to encode the ordered variable using a more effective channel, such as `size` or `color saturation`.

- **Moderate Approach: Use a Simple Countable Feature.** Redesign your shapes to use a simple, obvious, and countable feature. For example:
  - Polygons with an increasing number of sides (triangle, square, pentagon).
  - Stars with an increasing number of points.
  - A set of lines (one, two, three parallel lines).
  Keep the number of steps low (ideally under 5).

- **Comprehensive Redesign: Re-evaluate Your Encodings.** Step back and consider if all the visual channels are being used effectively. It might be better to create small multiples of the chart, where each chart shows a different value of the ordered variable, rather than trying to pack too much information into a single chart using complex shape encodings.