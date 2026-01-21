---
id: avoid-stacked-small-multiples-for-correlation-in-bar-charts
title: Prefer Side-by-Side Over Stacked Bar Small Multiples for Correlation Judgments
bibliography: references.bib
description: For judging similarity/correlation between two bar-chart series, adjacent
  small multiples outperform stacked ones.
labels:
- chart:bar
- task:compare
- task:judge-correlation
- visual:position
- impact:accuracy
- data:categorical
- audience:novice
- audience:expert
- comparison:two-series
---

## The Rule <!-- role: advice -->

When showing two bar charts for correlation/similarity judgment, place them adjacent (side-by-side) rather than stacked vertically.

## The Logic <!-- role: reason -->

Vertical stacking increases the effort of mapping corresponding items across charts, reducing precision in similarity judgments. In the paper’s correlation experiment, adjacent small multiples significantly outperformed stacked ones (requiring a lower target correlation to reach the same performance).

- **The Principle:** Easier correspondence mapping improves comparison precision
- **The Evidence:** [@ondovFaceFaceEvaluating2019a]

## Where to Apply <!-- role: context -->

- **User Goal:** Judge which pair of series is more similar (more correlated)
- **Data Type:** Two categorical series with consistent categories across charts
- **Audience:** General audiences and analysts

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must fit the layout into a narrow vertical container where adjacency is impossible.
- **Reason:** The rule assumes you can choose layout; forced constraints may require stacking despite accuracy costs. [@ondovFaceFaceEvaluating2019a]

## The Price <!-- role: costs -->

- **The Sacrifice:** Horizontal screen space.
- **The Risk:** In dense dashboards, adjacency can shrink charts and reduce legibility. [@ondovFaceFaceEvaluating2019a]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Stacking while assuming a shared baseline alone guarantees good comparison.
- **Why it fails:** The paper’s results show stacked underperformed adjacent for correlation despite aligned baselines. [@ondovFaceFaceEvaluating2019a]

## How to Check <!-- role: check -->

- **Visual Sign:** Users lose their place when bouncing between top and bottom charts to compare matching categories.
- **The Test:** If users need noticeably larger differences in similarity to make correct choices in stacked layouts, switch to adjacent (as reflected by higher titers for stacked in the paper). [@ondovFaceFaceEvaluating2019a]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move from stacked to side-by-side placement with aligned categories.
- **Best Fix:** Use a mirrored side-by-side layout to further improve precision for correlation judgments. [@ondovFaceFaceEvaluating2019a]
