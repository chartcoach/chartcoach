---
id: avoid-shape-texture-for-quantitative
title: "Avoid encoding quantitative data with shape or texture"
tags:
  - impact:perceptual
  - impact:ethical
  - visual:shape
  - visual:texture
  - data:quantitative
  - data:ordinal
sources:
  - type: research
    ref: Mackinlay, 1986
    url: https://doi.org/10.1145/22949.22950
    note: "Defined the principle of expressiveness, stating that visual encodings should express all and only the attributes of the data."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Meta-analysis (Table 3) confirms this theoretical principle, marking shape (S) and texture (T) as not recommended for quantitative data (Q)."
---

## Guidance

Do not use visual channels like shape (e.g., circle vs. square) or texture (e.g., cross-hatching vs. dots) to represent ordered (ordinal) or quantitative data. Reserve these channels for purely nominal (categorical) data.

## Why

Shape and texture are not perceptually ordered. A viewer cannot reliably determine if a square is "greater than" or "less than" a circle. Using them to encode magnitude violates the principle of "expressiveness," as it creates a chart that falsely implies an order that cannot be perceived, leading to misinterpretation.

## When it applies

- When choosing visual encodings for any chart that involves quantitative or ordinal data. This is a foundational rule of visualization design.

## Exceptions

- While standard shapes are unordered, some research has explored shapes with *countable* differences (e.g., a 1-spike star vs. a 5-spike star) which can be perceived as ordered. However, this is an advanced and uncommon technique that should be used with extreme caution. For all standard chart marks, the rule holds.
- Use shape and texture to distinguish between different categories of data that have no inherent order.

## Signs of Trouble

- **Unordered Legend:** A chart legend shows a quantitative or ordinal scale (e.g., "1-10," "11-20" or "Low," "Medium," "High") mapped to different shapes (e.g., circle, square, triangle).
- **Ambiguous Encoding:** A chart uses different patterns or shapes, and viewers are unsure how to interpret their relative value.

## How to Improve

- **Comprehensive Redesign: Re-encode the Data.** Replace the shape or texture encoding with a visual channel that is perceptually ordered.
  - **Good choices for quantitative/ordinal data:** Position, length, size (area), color saturation/luminance.
  - **Example:** In a scatterplot, instead of using different shapes for a quantitative value, use the size of the points or a sequential color palette.