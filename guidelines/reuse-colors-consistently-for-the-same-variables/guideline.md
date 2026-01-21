---
id: reuse-colors-consistently-for-the-same-variables
title: Reuse the Same Colors for the Same Variables
bibliography: references.bib
description: Maintain consistent color assignments across charts so readers can compare
  without relearning the mapping.
labels:
- chart:multiple
- task:compare
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- workflow:style-guide
---

## The Rule <!-- role: advice -->

Assign each key category/variable a color and reuse that same color whenever the same category/variable appears again.

## The Logic <!-- role: reason -->

Inconsistent mappings force readers to relearn color meaning, increasing confusion and reducing comparability across charts; Muth recommends keeping colors “taken” once used for specific variables [@muth_colors_2018].

- **The Principle:** Consistent encoding improves recognition and cross-chart comparison.
- **The Evidence:** [@muth_colors_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare the same category/country/variable across multiple charts in an article or report.
- **Data Type:** Repeated categorical entities across views.
- **Audience:** Readers scanning multiple charts sequentially.

## When to Break It <!-- role: exceptions -->

- **Scenario:** A single-color scheme is used for all charts regardless of variable (monochrome styling).
- **Reason:** If only one color is used everywhere, there’s no competing mapping to confuse readers [@muth_colors_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less freedom to pick “fresh” palettes for each chart.
- **The Risk:** Your first chart’s palette can constrain later designs, especially if many categories appear over time [@muth_colors_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reassigning colors per chart based on what “looks good” locally.
- **Why it fails:** Readers infer continuity from color and get misled when color meaning changes [@muth_colors_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The same category appears in different colors across charts in the same piece.
- **The Test:** List recurring categories and verify their hex codes are identical wherever they reappear [@muth_colors_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Lock a small set of brand/category colors and apply them retroactively to earlier charts.
- **Best Fix:** Create a palette map (category → color) for the whole project and enforce it consistently [@muth_colors_2018].
