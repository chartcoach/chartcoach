---
id: account-for-shape-induced-size-bias
title: "Account for shape-induced size biases in scatterplots"
tags:
  - impact:perceptual
  - impact:ethical
  - chart:scatter
  - task:compare
  - task:lookup
  - data:categorical
  - visual:size
  - visual:shape
  - medium:screen
sources:
  - type: research
    ref: Smart & Szafir, 2019
    url: https://doi.org/10.1145/3290605.3300899
    note: "Experiment 3 found that a mark's shape significantly biases its perceived size. Shapes with greater visual density along the top or bottom edges (like 'T' or a square '■') were consistently perceived as larger than other shapes of the same pixel dimensions (like '+' or '★')."
examples:
  - type: bad
    description: "A scatterplot encodes a quantitative value using size and a categorical value using shape. A 'T' shape and a '+' shape are rendered at the same size to represent the same value. However, viewers will likely perceive the 'T' as being larger, creating a perceptual error."
  - type: good
    description: "To correct for the bias, the '+' shape is rendered at a slightly larger pixel dimension than the 'T' shape. This counteracts the perceptual bias, so that viewers perceive them as representing the same size/value."
---
## Guidance

When using `shape` and `size` to encode data in a scatterplot, be aware that a mark's shape systematically biases its perceived size. Do not assume that shapes of the same pixel dimensions will be perceived as the same size.

## Why

The human visual system does not judge size by pixel area or bounding box alone. Certain geometric properties, such as having strong horizontal or vertical mass at the top or bottom, cause shapes to be perceived as larger than other shapes with the same dimensions. For example, a 'T' shape is consistently perceived as larger than a '+' shape. Using them to encode the same value without correction can lead to misinterpretation. This demonstrates that shape and size are not fully "separable" visual channels.

## When it applies

- When creating multiclass scatterplots that use `shape` for categorical data and `size` for quantitative data.
- In any visualization where the relative size of different shapes is meant to be compared.

## Exceptions

- When `size` is not used to encode a value and all marks are the same size.
- When `shape` is the only encoding used and all shapes are the same size.
- When the size differences being encoded are very large and coarse, making the subtle perceptual bias from shape less impactful on the overall interpretation.

## Trade-offs

- **Complexity vs. Perceptual Accuracy:** Actively correcting for size bias adds complexity to the visualization rendering logic. However, ignoring it sacrifices perceptual accuracy and risks misleading the viewer.
- **Uniformity vs. Correction:** A "correctly" rendered chart may have shapes with different pixel dimensions that are *intended* to be perceived as the same size, which may seem counter-intuitive or inconsistent from a purely geometric standpoint.

## Signs of Trouble

- **Inconsistent Judgements:** When asked to compare values, viewers' judgements are inconsistent and depend on which shapes are being compared. For example, they may overestimate the value of a category represented by '■' and underestimate the value of a category represented by '★'.
- **Visual Dominance:** Certain shape categories appear to visually dominate the plot, drawing more attention and seeming more "important" or "larger" even when their underlying values are not.
- **Outlier Illusion:** A data point may appear to be an outlier (or not an outlier) simply because of the perceptual size bias introduced by its shape.

## How to Improve

- **Quick Fix: Limit Shape Variation.** If possible, reduce the number of shapes used, and choose shapes that are geometrically similar (e.g., use only filled shapes like circle, square, triangle). Avoid mixing shapes with very different visual densities, like '■' and '+'.

- **Moderate Redesign: Use a Single Shape.** If size is a critical encoding channel for conveying a quantitative value, the best approach is to use a single shape (e.g., circles) for all data points. This completely eliminates the shape-induced size bias. Use a different visual channel, like color, for the categorical data.

- **Comprehensive Approach: Implement Perceptual Adjustment.** For advanced applications, implement a model that adjusts the rendered pixel size of each shape to counteract the known perceptual bias. For example, based on the findings, a '+' shape would need to be rendered physically larger than a 'T' shape for them to be perceived as equal in size. This normalizes the perceptual, rather than the physical, size of the marks.