---
id: implement-angular-brushing-by-mahalanobis-transform-and-erf
title: Compute Line-Proximity Selection for Normals via Mahalanobis Distance and Error
  Functions
bibliography: references.bib
description: For angular or linear function brushes, transform the distribution to
  isotropic space and use erf-based integration between parallel lines.
labels:
- chart:parallel-coordinates
- task:select
- visual:interaction
- impact:performance
- data:uncertainty
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

For angular brushing (selecting points near a line) on normally distributed uncertain data, compute selection by transforming the distribution to zero-mean, unit-variance space and integrating probability between the brush’s bounding lines using erf.

## The Logic <!-- role: reason -->

erf-based integrals are axis-aligned; by translating to the mean and scaling by (1/σx, 1/σy), an uncorrelated normal becomes isotropic. In that space, selection reduces to distances from parallel lines to the origin (Mahalanobis-distance logic), enabling fast analytic integration instead of slow numerical methods.

- **The Principle:** Transform-then-integrate for efficient probabilistic brushing
- **The Evidence:** [@fengMatchingVisualSaliency2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Interactive angular/linear brushing that respects uncertainty in scatter plots and PC plots
- **Data Type:** Bivariate normal uncertainty (ρ=0 directly; extendable to ρ≠0 with an added rotation step)
- **Audience:** Expert analysts requiring responsive interaction

## When to Break It <!-- role: exceptions -->

- **Scenario:** Uncertainty distributions are non-normal or lack an analytic integral for the brush geometry
- **Reason:** The erf-based closed form is specific to normals; general distributions require numerical integration [@fengMatchingVisualSaliency2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Implementation complexity (coordinate transforms, line representation, thresholds)
- **The Risk:** Incorrect transforms (e.g., ignoring correlation when present) yield wrong selection probabilities [@fengMatchingVisualSaliency2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Use Euclidean distance to the line in original coordinates as if uncertainty were uniform
- **Why it fails:** It ignores anisotropic variance; uncertain directions should “count less” in proximity, which the transform accounts for [@fengMatchingVisualSaliency2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Points with large σ in the perpendicular direction to the line are selected too easily
- **The Test:** Compare selection likelihoods for two points with same mean but different σ; the larger σ should require a wider brush to reach the same probability threshold [@fengMatchingVisualSaliency2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Apply the three-step process: translate to origin, scale by inverse σ, then compute signed line distance and integrate between bounds
- **Best Fix:** If ρ≠0, rotate to axis-align the covariance before scaling, then apply the same erf-based integration [@fengMatchingVisualSaliency2010].
