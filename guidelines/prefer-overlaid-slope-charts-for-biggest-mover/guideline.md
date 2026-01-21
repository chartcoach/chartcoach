---
id: prefer-overlaid-slope-charts-for-biggest-mover
title: Overlay Slopes to Find the Biggest Change in Slope Charts
bibliography: references.bib
description: For detecting the steepest-changing item in simplified slope displays,
  overlaid charts yield higher precision than animation or small multiples.
labels:
- chart:line
- chart:slope
- task:compare
- task:detect-change
- visual:superposition
- visual:position
- impact:accuracy
- data:categorical
- audience:novice
- audience:expert
- comparison:two-series
---

## The Rule <!-- role: advice -->

For a slope-based MAXDELTA task, use an overlaid (superposed) slope chart rather than animated transitions or separated small multiples.

## The Logic <!-- role: reason -->

Co-locating the two series in the same spatial frame reduces memory and correspondence demands, enabling more precise discrimination of which item changed most. In the paper’s slope-chart experiment, the overlaid condition outperformed all others, including animation.

- **The Principle:** Co-location reduces cross-view comparison load
- **The Evidence:** [@ondovFaceFaceEvaluating2019a]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which item changed the most between two states, represented as slopes
- **Data Type:** Two series encoded as slopes (two-point lines), small number of items
- **Audience:** Analysts or readers doing quick “which changed most?” judgments

## When to Break It <!-- role: exceptions -->

- **Scenario:** Overplotting makes individual slopes hard to distinguish (e.g., too many items for the available space).
- **Reason:** The paper’s slope stimuli used few items; dense overlays can destroy separability and negate the co-location benefit. [@ondovFaceFaceEvaluating2019a]

## The Price <!-- role: costs -->

- **The Sacrifice:** Visual simplicity; overlapping marks can increase clutter.
- **The Risk:** Color/mark confusion if series are not clearly distinguishable when superposed. [@ondovFaceFaceEvaluating2019a]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to animation assuming it will always highlight change.
- **Why it fails:** For slopes, animation was worse than overlay in MAXDELTA performance in the paper. [@ondovFaceFaceEvaluating2019a]

## How to Check <!-- role: check -->

- **Visual Sign:** Users misidentify the steepest slope or repeatedly re-check items in separated views.
- **The Test:** Present a few MAXDELTA trials (which line changed most?) and compare error rates between overlay vs animation; overlay should win in this scenario per the paper. [@ondovFaceFaceEvaluating2019a]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Overlay the two slope states in the same axes with distinct styling for each series.
- **Best Fix:** Use overlaid slopes as the primary view for “biggest mover” tasks and provide interaction (highlight on hover/click) to reduce clutter if needed. [@ondovFaceFaceEvaluating2019a]
