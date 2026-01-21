---
id: do-not-use-animation-to-judge-correlation-in-bar-comparisons
title: Avoid Animation for Judging Correlation Between Two Bar-Chart Series
bibliography: references.bib
description: Animation helps detect a single biggest change, but it does not improve
  accuracy for judging overall correlation/similarity between bar-chart series pairs.
labels:
- chart:bar
- task:compare
- task:judge-correlation
- visual:motion
- impact:accuracy
- data:categorical
- audience:novice
- audience:expert
- comparison:two-series
---

## The Rule <!-- role: advice -->

Do not rely on animated transitions to help users judge which pair of bar-chart series is more correlated (more similar overall).

## The Logic <!-- role: reason -->

The motion signal in transitions directly encodes per-item delta (via velocity) but does not directly encode the global pattern needed for correlation judgments. In the paper’s correlation experiment (bar charts), animation provided no performance benefit over static arrangements.

- **The Principle:** Motion salience does not equal global-structure readability
- **The Evidence:** [@ondovFaceFaceEvaluating2019a]

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which of two series pairs is “more similar overall” (higher correlation)
- **Data Type:** Two bar-chart series compared as a pair (and especially when comparing two such pairs)
- **Audience:** Non-experts (crowdsourced participants) and practitioners needing reliable similarity judgments

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user’s real task is to find the single category with the largest change (MAXDELTA), not correlation.
- **Reason:** For MAXDELTA in bars, animation improved performance substantially in the paper. [@ondovFaceFaceEvaluating2019a]

## The Price <!-- role: costs -->

- **The Sacrifice:** You forgo a potentially engaging transition effect.
- **The Risk:** If you animate anyway, users may overweight salient movers and misjudge overall similarity. [@ondovFaceFaceEvaluating2019a]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Animating both series pairs simultaneously to “show similarity.”
- **Why it fails:** The paper reports no correlation benefit, and its limitations note capacity constraints when processing multiple moving objects/animations. [@ondovFaceFaceEvaluating2019a]

## How to Check <!-- role: check -->

- **Visual Sign:** Users point to a few fast-moving bars as evidence of “low correlation,” ignoring the overall pattern.
- **The Test:** Ask users to choose the “more similar pair” with and without animation; if animation doesn’t reduce errors, remove it for this task (matching the paper’s finding). [@ondovFaceFaceEvaluating2019a]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use static small multiples (adjacent or mirrored) instead of animation for correlation judgments.
- **Best Fix:** Prefer mirrored static bar charts for correlation comparisons, since mirrored outperformed adjacent in the paper’s correlation task. [@ondovFaceFaceEvaluating2019a]
