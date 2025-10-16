---
id: avoid-nested-donut-comparisons
title: "Avoid Nested Donut Charts for Comparing Proportions Across Layers"

tags:
  - impact:perceptual
  - chart:donut
  - chart:pie
  - task:compare
  - task:composition
  - visual:area
  - visual:size
  - visual:angle

evidence:
  strength: medium
  summary: "Based on Skau & Kosara (2016) identifying arc length and area as primary perceptual cues, comparing these cues across the different radii of nested donuts is inherently difficult and error-prone. The paper explicitly warns that this chart type is 'likely problematic'."

sources:
  - type: research
    ref: Skau & Kosara, 2016
    url: https://doi.org/10.1111/cgf.12888
    note: "The paper's conclusion that arc length and area are primary cues leads to the recommendation to avoid nested donuts, as comparing these cues across different radii is perceptually difficult."
    role: primary

examples:
  - type: bad
    description: "A nested donut chart showing market share in two different years. It is difficult to accurately compare a segment in the inner ring (2022) with one in the outer ring (2023) because they are on different scales."
  - type: good
    description: "Instead of a nested donut, two separate, side-by-side donut charts are used to show market share in two different years. This small multiples approach allows for easier comparison."

---

## Guidance

Do not use nested donut charts when the primary task is to compare the proportions of segments *between* the different rings (layers).

## Why

Nested donut charts place data on different scales (i.e., different radii). Because viewers rely on arc length and area to judge segment size, it is perceptually difficult and error-prone to compare a segment in the inner ring to one in the outer ring. The same angle will produce a smaller arc length and area on an inner ring, leading to systematic underestimation when comparing its value to a segment on an outer ring.

## When it applies

- When you have part-to-whole data for multiple groups (e.g., market share in 2022 vs. 2023) and are considering how to visualize them for comparison.

## Exceptions

- If the goal is *only* to read proportions *within* each ring and never to compare between them, a nested donut chart might be acceptable as a space-saving device, although small multiples are often still clearer.

## Trade-offs

- Nested donut charts can be very space-efficient. Switching to an alternative like small multiple pie charts or a grouped bar chart will likely require more screen or page real estate.

## Signs of Trouble

- **Apples-to-Oranges Comparison:** The chart design encourages viewers to visually compare a slice in the inner ring with a slice in the outer ring.
- **Misleading Angles:** A viewer might mistakenly assume that two segments with the same angle represent the same quantity, even though they are in different rings and thus have different areas and arc lengths.

## How to Improve

- **Moderate approach: Use Small Multiples.** Instead of nesting the donut charts, place them side-by-side. This allows for easier comparison of segment angles and overall compositions because they share the same scale.
- **Comprehensive approach: Switch to a Bar Chart.** For comparing proportions across multiple categories, a grouped or stacked bar chart is often a more effective choice. It places all data on a common, linear scale (position), which is the most accurate visual encoding for perceptual comparisons.
