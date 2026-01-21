---
id: prefer-mirrored-small-multiples-over-standard-small-multiples-for-bar-comparisons
title: Mirror Two Bar Charts Around a Central Axis for Direct Comparison
bibliography: references.bib
description: When comparing exactly two bar-chart series, mirror the charts to improve
  perceptual precision for both biggest-change and correlation tasks.
labels:
- chart:bar
- task:compare
- task:detect-change
- task:judge-correlation
- visual:position
- impact:accuracy
- data:categorical
- audience:novice
- audience:expert
- comparison:two-series
---

## The Rule <!-- role: advice -->

When you must use two bar-chart small multiples, arrange them as a mirrored pair (center-aligned, with opposing x-axis directions) instead of standard side-by-side or stacked small multiples.

## The Logic <!-- role: reason -->

Mirror symmetry reduces comparison burden by placing corresponding items in a symmetric relationship that the visual system detects efficiently, improving discrimination between paired regions. In the paper, mirrored bar-chart small multiples improved threshold performance versus non-mirrored small multiples for both MAXDELTA and CORRELATION tasks.

- **The Principle:** Symmetry-facilitated visual comparison
- **The Evidence:** [@ondovFaceFaceEvaluating2019a]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare two series across categories (either identify the biggest change or judge similarity/correlation)
- **Data Type:** Two series, same categories, shown as bars
- **Audience:** Anyone doing pairwise comparison (dashboards, reports) where accuracy matters

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need to compare more than two datasets at once.
- **Reason:** Mirroring is inherently pairwise and does not scale cleanly to many series, as noted in the paper’s limitations. [@ondovFaceFaceEvaluating2019a]

## The Price <!-- role: costs -->

- **The Sacrifice:** A conventional left-to-right reading direction and a standard axis orientation.
- **The Risk:** Some viewers may be confused by opposing axis directions unless the design clearly signals the mirroring. [@ondovFaceFaceEvaluating2019a]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Mirroring without clear correspondence, so users don’t know which bar matches which.
- **Why it fails:** The benefit depends on easy symmetric pairing; ambiguity forces memory-based comparison, undermining the advantage. [@ondovFaceFaceEvaluating2019a]

## How to Check <!-- role: check -->

- **Visual Sign:** Users’ eyes repeatedly jump back and forth between charts to match categories.
- **The Test:** Ask a few users to point to the “biggest mover” or to pick the “more similar pair”; if mirrored layout reduces back-and-forth scanning and errors, it matches the paper’s findings. [@ondovFaceFaceEvaluating2019a]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Center the two bar charts and reverse one x-axis so corresponding bars face each other.
- **Best Fix:** Use mirrored small multiples as the default two-series comparison layout when overlay is not feasible. [@ondovFaceFaceEvaluating2019a]
