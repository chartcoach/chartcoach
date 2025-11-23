---
id: augment-incidental-aspect-ratios
title: Explicitly Label Marks in Variable Aspect Ratio Charts
bibliography: references.bib
description: Charts that incidentally vary aspect ratio (like Treemaps) require text
  labels to counteract position/size estimation biases.
labels:
- chart:mekko
- chart:treemap
- visual:area
- impact:clarity
- task:identify
---

## The Rule <!-- role: advice -->
When using charts that algorithmically or incidentally vary the aspect ratio of marks (such as Marimekko charts or Treemaps), you must reinforce the data with explicit text labels or tooltips.

## The Logic <!-- role: reason -->
In charts like Marimekko (Mosaic) plots or Treemaps, the aspect ratio of a mark is often a byproduct of the layout algorithm or a secondary variable, not the primary data encoding. However, this incidental shape influences how users perceive and remember the primary value (height or position).
*   **The Principle:** Shape-Induced Distortion. Because wide marks are overestimated and tall marks are underestimated, users may perceive data values incorrectly based solely on the mark's resulting shape [@ceja_truth_2021].
*   **The Implication:** A wide rectangle in a Mekko chart might be recalled as having a higher vertical position than a tall rectangle, even if they are identical in height.

## Where to Apply <!-- role: context -->
*   **Chart Types:** Marimekko charts, Variable-width bar charts, Treemaps.
*   **Data Type:** Hierarchical data or multi-variable distributions where width and height vary independently.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** "Banking to 45 degrees" in line charts.
*   **Reason:** While aspect ratio affects slope perception in line charts, that is a separate perceptual mechanism aimed at optimizing slope discrimination, which may conflict with the square-prototype bias for position recall [@ceja_truth_2021].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Cleanliness. Adding data labels adds ink and potential clutter to the visualization.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on a Y-axis.
*   **Why it fails:** Users subject to the categorical prototype effect will misinterpret the position relative to the axis once they look away or move to a comparison task. The visual encoding itself is what is biased in memory.

## How to Check <!-- role: check -->
*   **Visual Sign:** Identify marks within the same chart that represent similar values but have vastly different width-to-height ratios.
*   **The Test:** If a wide mark and a tall mark have the same vertical value, ask if a viewer would recall them as equal. (The evidence suggests they would not).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add direct value labels inside or near the marks.
*   **Best Fix:** Use reporting methods that do not rely on visual estimation alone, such as a verbal report or a table alongside the chart, or unify chart aspect ratios in dashboards to ensure consistent biases [@ceja_truth_2021].
