---
id: generate-distinct-semantic-palettes-by-clustering-in-cielab
title: Generate visually distinct semantic palettes by clustering colors in CIELAB
bibliography: references.bib
description: Improve categorical separability by clustering candidate semantic colors
  in perceptual space and iteratively adjusting assignments.
labels:
- chart:categorical
- task:distinguish
- visual:color
- impact:clarity
- data:categorical
- audience:expert
- complexity:advanced
---

## Cluster candidate semantic colors in CIELAB to produce a distinct categorical palette <!-- role: advice -->

Cluster the set of candidate semantic colors in CIELAB (CIELAB color space) and iteratively adjust assignments so each category ends with a visually discriminable color.

## Why perceptual-space clustering improves categorical palettes <!-- role: reason -->

Clustering in a perceptually oriented color space provides a practical way to detect and reduce near-duplicates that would be hard to distinguish in a legend or in marks, while keeping colors anchored to semantically derived candidates.

**Mechanism:** K-means clustering in CIELAB minimizes within-cluster variance; when clusters contain multiple assigned colors (collisions), reassignment to alternate candidate colors can drive convergence toward singleton-like separability.

**Evidence:** Applying k-means clustering in CIELAB to semantic colors and iteratively swapping in alternate canonical colors yields palettes that better separate categories and supports mapping to fixed palettes for visualization use [@setlurLinguisticApproachCategorical2016].

**Notes:** This is palette-level optimization; it complements term-level semantic retrieval.

## When CIELAB clustering is the right tool <!-- role: context -->

- **User Goal:** Maintain semantic meaning while ensuring categories are separable by color.
- **Task:** Build a categorical palette for a set of labels, not a single label.
- **Data:** A set of semantic candidate colors, often with multiple options for some terms.
- **Chart Setting:** Static or interactive views where color is a primary category key.
- **Audience:** Broad audiences who need easy categorical discrimination.
- **Success Criterion:** The resulting palette avoids visually similar colors within the same view.

## When clustering is insufficient or misaligned <!-- role: exceptions -->

**Break it when:** Many categories legitimately share very similar real-world colors (e.g., many “metals” as grays). **Why:** Perceptual separation cannot be achieved without departing from semantics or changing the encoding strategy [@setlurLinguisticApproachCategorical2016].

## Tradeoffs of clustering-based palette optimization <!-- role: costs -->

**Sacrifice:** Added computation and the need for multiple candidate colors for flexibility. **Risk:** The algorithm may choose colors that are semantically acceptable but less familiar, or may still produce colors that are too light/dark for the chart. **Mitigation:** Optionally quantize to a curated fixed palette after clustering [@setlurLinguisticApproachCategorical2016].

## Common mistakes in clustering semantic palettes <!-- role: mistakes -->

- **Mistake:** Optimizing colors term-by-term without considering the full palette. **Why it fails:** The result can contain collisions (e.g., multiple reds) that undermine categorical distinction [@setlurLinguisticApproachCategorical2016].
- **Mistake:** Assuming clustering alone guarantees visualization-safe colors. **Why it fails:** Some extracted semantic colors can still be too dark or too light even if they are distinct [@setlurLinguisticApproachCategorical2016].

## Quick checks for palette distinctness after clustering <!-- role: check -->

**Failure Sign:** Two or more categories remain hard to tell apart in the legend or on marks. **Quick Check:** Visually scan the palette swatches and identify any same-hue pairs that look interchangeable. **Stronger Test:** Compute pairwise CIELAB distances across assigned colors and verify that the minimum distance exceeds an internal discriminability threshold [@setlurLinguisticApproachCategorical2016].

## What to do instead if clustering cannot produce a usable palette <!-- role: fix -->

- Constrain assignment to a fixed, curated palette by nearest-color matching in CIELAB.
- Reduce the number of categories encoded by color at once and use interaction or facets to separate groups.
- Use context-driven symbols (logos/flags) as additional encodings when identity recognition is the main goal.
- Replace the encoding strategy for the domain (e.g., avoid relying on categorical color when the domain is inherently monochromatic) [@setlurLinguisticApproachCategorical2016].
