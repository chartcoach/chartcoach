---
id: use-filled-marks-for-color
title: "Use filled marks over unfilled marks to improve color distinction in scatterplots"

tags:
  - impact:perceptual
  - impact:accessibility
  - chart:scatter
  - task:compare
  - task:lookup
  - task:cluster
  - data:categorical
  - visual:color
  - visual:shape
  - medium:screen
  - access:color-vision-risk

evidence:
  strength: medium
  summary: "Smart & Szafir (2019) conducted experiments with 606 participants, finding that colors were significantly more discriminable for filled shapes (e.g., ■) than their unfilled counterparts (e.g., □) across all three axes of the CIELAB color space (p < .001)."

sources:
  - type: research
    ref: Smart & Szafir, 2019
    url: https://doi.org/10.1145/3290605.3300899
    note: "Experiment 1 (n=606) found filled shapes outperformed unfilled shapes for color discrimination tasks. For example, filled squares (■) led to significantly better color perception than unfilled squares (□) (p < .001)."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.48550/arXiv.2109.01271
    note: "Synthesizes this finding (Section 5.1.2), stating 'CH is generally more discriminable with filled shapes than with unfilled ones.'"
    role: supporting

tools:
  - type: learn
    name: "From Data to Viz: Scatterplot"
    url: https://www.data-to-viz.com/graph/scatter.html
    description: Provides a guide on scatterplot creation, with examples often using filled marks for clarity.

examples:
  - type: good
    description: "This scatterplot uses filled circles. The distinct colors for each category are easy to perceive, even for small marks, facilitating quick identification and comparison."
  - type: bad
    description: "This scatterplot uses unfilled circles (outlines only). The colors are harder to distinguish, especially where marks are small or close together, because the colored area is minimal. This increases cognitive load and error rates."
---

## Guidance

When using color to distinguish between categories in a scatterplot, use filled shapes (e.g., ●, ■) instead of unfilled, outlined shapes (e.g., ○, □).

## Why

Filled shapes present more colored pixels to the eye than outlined shapes of the same size. This larger area of color makes it perceptually easier for viewers to discriminate between different hues, even when the differences are subtle or the marks are small. Using filled shapes increases the accuracy and speed of identifying categories based on color.

### Core Principle

The perceptual salience of a color encoding is proportional to its area. Larger, denser color marks are easier to see and distinguish than smaller, sparser ones.

## When it applies

- In any scatterplot where color is used to encode categorical data (e.g., distinguishing different groups, series, or clusters).
- When you have many categories and need to ensure colors in your palette are as distinct as possible.
- When marks may be small, dense, or overlapping, as the added color area of filled marks helps them stand out.

## Exceptions

- If scatterplot marks are very large, the difference in color perception between filled and unfilled shapes may be negligible.
- In cases of extreme overplotting, using semi-transparent unfilled shapes might be a deliberate choice to reveal density patterns, sacrificing individual mark clarity for an aggregate view. However, other techniques like density plots or changing mark size are often better for this.

## Trade-offs

- **Clarity vs. Overplotting:** Filled marks are clearer individually but can obscure each other more in dense plots (overplotting) compared to semi-transparent or outlined marks.
- **Aesthetics:** Style guides may sometimes call for outlined or "ghost" marks for aesthetic reasons, but this comes at the cost of perceptual performance.

## Signs of Trouble

- **The Squint Test:** If you squint at the chart, do different color categories blur together into a single mass?
- **Color Confusion:** Do viewers have trouble telling apart two similar colors in the plot (e.g., a light green and a light blue)?
- **Legend-Chart Disconnect:** Do the colors look distinct in the large legend swatches but become indistinguishable as small marks in the plot?

## How to Improve

- **Quick Fix: Fill the Marks.** The most direct improvement is to change the rendering property of your marks from outlined to filled. Most plotting libraries have a simple setting for this (e.g., in D3.js, set the `fill` attribute instead of just the `stroke`).

- **Moderate Approach: Increase Stroke Width.** If you must use unfilled marks for stylistic reasons, significantly increasing the stroke width can improve color perception by increasing the total colored area. However, this also makes the mark's inner area smaller and can create a "chunky" look.

- **Comprehensive Approach: Re-evaluate Encodings.** If filling the marks is not enough, reconsider the entire encoding scheme. You may need to choose a more perceptually distant color palette, or reduce the number of categories to make them more distinct.
