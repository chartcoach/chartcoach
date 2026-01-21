---
id: control-visual-appearance-while-preserving-specified-statistics
title: Constrain Statistics While Directing Points Toward a Target Shape
bibliography: references.bib
description: Generate visually targeted datasets by iteratively perturbing points
  while enforcing invariance of chosen statistics.
labels:
- chart:scatter
- task:generate
- visual:position
- impact:pedagogy
- data:bivariate
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

When you need a plot to take on a specific appearance while keeping selected statistics constant, iteratively perturb points and accept only changes that preserve the statistics while improving proximity to a target shape.

## The Logic <!-- role: reason -->

- **The Principle:** Local point moves can preserve global summaries if changes are small and filtered; repeated steps can significantly change appearance.
- **The Evidence:** Matejka & Fitzmaurice describe generating new datasets from a seed by randomly moving points, checking statistical equivalence, and optimizing visual fitness against a target shape [@matejkaSameStatsDifferent2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Create instructive counterexamples (same stats, different graphs) or craft datasets that encode a recognizable visual pattern.
- **Data Type:** 2D point sets where constraints are expressed as computable statistics (e.g., mean/SD/correlation).
- **Audience:** Visualization educators, researchers, or tooling developers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The seed dataset and the desired target shape are extremely mismatched in coverage or orientation.
- **Reason:** The paper shows coercion can yield undesirable results when forcing incompatible shapes [@matejkaSameStatsDifferent2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Computation time (many iterations) and the need to implement constraint checks and a fitness function.
- **The Risk:** Results can look “clumpy” or sparse along the target if fitness only measures distance-to-shape [@matejkaSameStatsDifferent2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Moving many points aggressively without calibrating step size.
- **Why it fails:** Large perturbations are less likely to preserve the chosen statistics, causing high rejection rates or drift from constraints [@matejkaSameStatsDifferent2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Points cluster in a few regions of the intended shape, leaving gaps.
- **The Test:** Compare the dataset’s computed constraint statistics to the seed (to the required precision) and inspect coverage along the target [@matejkaSameStatsDifferent2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce perturbation magnitude so most moves keep statistics unchanged at the required rounding.
- **Best Fix:** Enhance fitness to discourage clumping (add a separation/coverage goal) while still enforcing statistical equivalence checks [@matejkaSameStatsDifferent2017].
