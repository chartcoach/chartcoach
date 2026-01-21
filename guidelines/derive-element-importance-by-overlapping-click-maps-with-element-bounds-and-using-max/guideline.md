---
id: derive-element-importance-by-overlapping-click-maps-with-element-bounds-and-using-max
title: Compute Element Importance by Overlapping Click Maps with Element Bounds
bibliography: references.bib
description: "Rank design or chart elements by taking the maximum smoothed click-map\
  \ value inside each element\u2019s region."
labels:
- task:rank
- visual:attention
- impact:measurement
- audience:researcher
- method:BubbleView
- output:importance-ranking
- source:kimBubbleView2017
---

## The Rule <!-- role: advice -->

To rank elements by importance, overlay the (normalized, smoothed) BubbleView click map with each element’s region and use the maximum map value inside the region as that element’s importance score.

## The Logic <!-- role: reason -->

The paper uses this “max within element bounds” approach to score visualization elements and graphic-design elements, showing strong agreement with eye-fixation-based rankings (e.g., Spearman 0.96 for visualization element types) and reasonable agreement with explicit importance annotations for graphic designs [@kimBubbleViewInterfaceCrowdsourcing2017].

- **The Principle:** Element-level scoring from spatial importance fields
- **The Evidence:** [@kimBubbleViewInterfaceCrowdsourcing2017]

## Where to Apply <!-- role: context -->

- **User Goal:** Produce a ranked list of which components are most attended/important.
- **Data Type:** Images where elements have bounding boxes/segmentations (titles, legends, text blocks, logos, etc.).
- **Audience:** Designers and researchers evaluating layouts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Elements are large and should be treated as uniformly important (e.g., long text blocks where fixation/click density varies internally).
- **Reason:** Max scoring emphasizes peaks and may not reflect uniform “importance” across the whole element [@kimBubbleViewInterfaceCrowdsourcing2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires element annotations (bounding boxes or segmentations).
- **The Risk:** Max can over-emphasize a small hotspot inside a large element [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Comparing raw BubbleView heatmaps directly to uniform importance masks without element-level aggregation.
- **Why it fails:** Different methods encode importance at different granularities; element-level scoring makes comparisons more meaningful [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Element rankings look inconsistent with obvious focal items (e.g., title/logo not near top).
- **The Test:** Visualize element boxes with their computed scores overlaid (as in the paper’s examples) to verify the scoring matches map hotspots [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Ensure maps are normalized consistently before scoring elements.
- **Best Fix:** Improve element definitions (tighter boxes/accurate segmentations) so the max statistic reflects the intended element region [@kimBubbleViewInterfaceCrowdsourcing2017].
