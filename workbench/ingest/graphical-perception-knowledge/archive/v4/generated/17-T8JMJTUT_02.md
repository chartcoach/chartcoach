---
id: cartogram-avoid-rectangular-for-comparison
title: "Avoid rectangular cartograms for comparing values between regions"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:map
  - chart:map.cartogram
  - chart:map.cartogram.rectangular
  - task:compare
  - task:rank
  - data:spatial
  - data:quantitative
  - visual:area
  - medium:static

sources:
  - type: research
    ref: Nusrat, Alam, & Kobourov, 2018
    url: https://doi.org/10.1109/TVCG.2016.2642109
    note: "For a 'compare' task, rectangular cartograms were significantly less accurate than contiguous, non-contiguous, and Dorling cartograms, which all performed similarly well."

---

## Guidance

Avoid using rectangular cartograms when the primary task is to compare the data values (i.e., the areas) of different regions.

## Why

Rectangular cartograms are the least accurate type for value comparison tasks. The human visual system is poor at comparing 2D areas, and this weakness is exacerbated by the extreme and varied aspect ratios (long, skinny vs. short, fat rectangles) that often occur in rectangular cartograms. This makes area judgments highly difficult and error-prone. Contiguous, non-contiguous, and Dorling (circle-based) cartograms all provide shapes that are easier to compare by area and perform significantly better.

## When it applies

- When viewers need to judge which of two or more regions has a larger or smaller data value represented by its area.
- When viewers need to rank several regions by their data value.

## Exceptions

- If the primary goal is to create a schematic, topology-preserving diagram and precise value comparison is a secondary concern. In such cases, the inaccurate perception of area can be mitigated with labels.

## Trade-offs

- While poor for comparison, topology-preserving rectangular cartograms perfectly maintain adjacency, a feature that the better-performing Dorling and non-contiguous types lack. You trade perceptual accuracy for topological accuracy.

## Signs of Trouble

- **Large Error Rates:** User feedback or testing reveals that people consistently fail to correctly identify the larger or smaller region.
- **Low Confidence:** Users express uncertainty or say they are "just guessing" when asked to compare region sizes.
- **Aspect Ratio Deception:** A long, thin rectangle is perceived as smaller than a compact, squarish rectangle of the exact same area.

## How to Improve

- **Quick Fix: Add Direct Labels.** If you must use a rectangular cartogram, add data labels directly to each rectangle. This allows users to compare numbers instead of relying on flawed area perception.
- **Moderate Redesign: Switch Cartogram Type.** Change the visualization from a rectangular cartogram to a **Dorling**, **contiguous**, or **non-contiguous** cartogram, all of which are more perceptually accurate for area comparisons.
- **Comprehensive Redesign: Use a Bar Chart.** If the primary goal is accurate comparison and ranking, the best visualization is often not a cartogram. Use a standard bar chart, which leverages the highly accurate visual channel of length on a common baseline. Label the bars with region names to maintain context.
