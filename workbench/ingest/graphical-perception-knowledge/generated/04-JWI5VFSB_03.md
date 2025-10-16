---
id: avoid-nested-donut-charts-for-comparison
title: "Avoid using nested donut charts for comparison"
tags:
  - impact:perceptual
  - chart:donut
  - chart:pie
  - chart:radial
  - task:compare
  - data:quantitative
evidence:
  strength: medium
  summary: "Inferred from Skau & Kosara (2016), who identified the importance of arc length and area. Nested donuts force comparisons of these cues across different radii, a task at which humans are known to be inaccurate. The authors state this design is 'likely problematic'."
sources:
  - type: research
    ref: Skau & Kosara, 2016
    url: https://doi.org/10.1111/cgf.12888
    note: "The paper's recommendation: 'Nested donuts...are problematic. Since area and arc length are important, nesting donuts...means comparing circles of different radius and area, which is likely problematic.'"
    role: primary
examples:
  - type: bad
    description: Multiple concentric donut rings are used to compare the composition of different groups. It's nearly impossible to accurately compare the size of a slice in the inner ring to one in the outer ring.
    url: https://i.imgur.com/kS5x87J.png
---

## Guidance

Do not use multiple, concentric donut charts (nested donuts) to compare the composition of different groups. The visual comparison required is unreliable and prone to error.

## Why

Nested donut charts require viewers to compare arc lengths and areas between rings of different sizes. This is a difficult perceptual task. It's analogous to comparing the lengths of bars that don't share a common baseline. Because the scales are not aligned, viewers cannot make accurate judgments about which segment is larger.

### Core Principle

For accurate comparison, visual marks should be encoded along a common, aligned scale. Nested donuts violate this principle by placing comparable marks on unaligned, concentric scales.

## When it applies

- When you need to compare the proportional breakdown (composition) of two or more different groups or datasets.

## Exceptions

If the goal is simply to show hierarchical data (e.g., in a sunburst diagram) where the primary task is understanding the hierarchy itself and not to enable precise comparison between layers, this format might be acceptable. However, for any task involving comparison, it should be avoided.

## Trade-offs

Nested donuts can be a very space-efficient way to show multiple compositions. The trade-off is that this compactness comes at the direct cost of perceptual accuracy. A more accurate alternative, like small-multiple pie charts or stacked bar charts, will require more horizontal or vertical space.

## Signs of Trouble

- **Concentric Confusion:** Your design features multiple donut charts layered on top of each other, sharing a common center.
- **Difficult Comparisons:** When you try to compare a slice on an inner ring to a slice on an outer ring, you find yourself guessing which is larger.

## How to Improve

- **Quick Fix:** Add direct percentage labels to every segment in every ring. This allows for direct numerical comparison, bypassing the flawed visual comparison and serving as an accessibility improvement.
- **Moderate Redesign:** Convert the nested donut chart into small multiples. Show each donut chart side-by-side. This ensures they are all the same size and share the same visual scale, making comparisons more reliable.
- **Comprehensive Redesign:** Convert each ring of the donut into a 100% stacked bar chart and place them one above the other. This uses position along a common scale for each group, making comparisons between groups much more accurate and reliable.
