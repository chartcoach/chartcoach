---
id: use-3d-cross-tab-bars-when-comparisons-are-needed-in-both-dimensions
title: Use 3D cross-tab bars when comparisons are needed in both dimensions
bibliography: references.bib
description: Use 3D bar grids for two categorical variables when users must compare
  bar lengths across both axes rather than along a single shared baseline.
labels:
- chart:bar
- task:compare
- visual:position
- impact:clarity
- data:categorical
- audience:expert
- custom:crosstab
---

## Use 3D bar crosstabs to support bidirectional comparison <!-- role: advice -->

Use a 3D bar arrangement for a cross-tabulation when users must compare magnitudes along both categorical directions and a 2D grid would privilege only one shared-baseline direction.

## Why a shared base plane can balance comparison directions <!-- role: reason -->

In a 2D grid of bars, only one direction typically has a common baseline, making comparisons in the orthogonal direction perceptually harder; a 3D base plane can provide a consistent reference for both directions.

**Mechanism:** A 3D base plane lets bars rise from the same ground surface across both axes, reducing the “floating baseline” effect that hinders comparisons across columns/rows in 2D bar grids.

**Evidence:** 2D bar grids facilitate comparison in the direction with a common baseline but hinder the other direction, while a 3D bar grid can facilitate comparisons in both directions though it can introduce occlusion [@brath3DInfoVisHere2014].

**Notes:** This approach is most robust when occlusion is limited by the data distribution.

## When to apply 3D crosstab bars <!-- role: context -->

- **User Goal:** Compare cell magnitudes across both row and column categories.
- **Task:** Cross-category comparison and scanning for highs/lows across a table-like structure.
- **Data:** Two categorical variables and one quantitative measure.
- **Chart Setting:** A view where users can see enough of the grid from a stable angle; optional interaction.
- **Audience:** Users comfortable reading bar charts and cross-tabs.
- **Success Criterion:** Users can compare values across both dimensions without switching to separate charts.

## When not to use it <!-- role: exceptions -->

- **Break it when:** The dataset is dense and produces heavy mutual occlusion across the grid. **Why:** Hidden bars prevent reliable comparison and may require constant navigation [@brath3DInfoVisHere2014].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Occlusion risk increases versus a flat table-like display. **Risk:** Users may over-rely on visible front rows/columns and miss occluded values. **Mitigation:** Keep the default view optimized and consider pairing with a precise 2D slice.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using 3D bars for a fully populated grid where most bars are similar height. **Why it fails:** Occlusion increases while the comparison benefit decreases [@brath3DInfoVisHere2014].
- **Mistake:** Using 2D bars and expecting equally easy comparison across both axes. **Why it fails:** One axis lacks a shared baseline, increasing perceptual difficulty [@brath3DInfoVisHere2014].

## Quick tests <!-- role: check -->

**Failure Sign:** Users only compare values in the front row/column and ignore the rest. **Quick Check:** Verify that a user can compare two cells that are far apart in both axes without rotating. **Stronger Test:** Time and accuracy test for cross-row and cross-column comparisons against a 2D bar grid.

## What to do instead <!-- role: fix -->

- Use a 2D heatmap-like grid when relative comparison is sufficient and precision is not required.
- Use two linked 2D bar charts (row-wise and column-wise) when comparisons are primarily one-dimensional at a time.
- Provide an interactive slice/selection that surfaces the chosen row/column in 2D for precise comparison.
- Filter or aggregate categories to reduce the grid density that causes occlusion.
