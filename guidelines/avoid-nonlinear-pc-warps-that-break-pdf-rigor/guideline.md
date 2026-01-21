---
id: avoid-nonlinear-pc-warps-that-break-pdf-rigor
title: Treat Curved Parallel Coordinates as a Trade-off Against PDF Correctness
bibliography: references.bib
description: If you warp parallel coordinates with nonlinear curves, acknowledge it
  no longer represents a formal PDF.
labels:
- chart:parallel-coordinates
- task:explore
- visual:shape
- impact:trust
- data:uncertainty
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

If you use nonlinear curved parallel coordinates (e.g., sigmoid warps) with density/PDF rendering, treat the result as perceptual guidance—not a mathematically rigorous PDF.

## The Logic <!-- role: reason -->

A nonlinear change of variables warps area non-uniformly; the transformed density no longer preserves the formal PDF property (e.g., unit integral), creating a trade-off between perceptual benefits of curves and statistical rigor.

- **The Principle:** Nonlinear warps break PDF invariants
- **The Evidence:** [@fengMatchingVisualSaliency2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Improve perceptual readability of PC plots while still conveying uncertainty structure
- **Data Type:** PC density plots where designers consider curved polylines (sigmoid)
- **Audience:** Expert analysts who may assume density has probabilistic meaning

## When to Break It <!-- role: exceptions -->

- **Scenario:** Mathematical correctness of probability density (e.g., interpretability as a PDF) is required
- **Reason:** Nonlinear warps invalidate formal PDF interpretation [@fengMatchingVisualSaliency2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Statistical interpretability of the rendered density as a true PDF
- **The Risk:** Users may over-trust quantitative meaning of brightness/area after warping [@fengMatchingVisualSaliency2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Present a warped density PC plot as “the PDF” without qualification
- **Why it fails:** The mapping is no longer probability-preserving, so the display can mislead about relative likelihoods [@fengMatchingVisualSaliency2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Density brightness appears redistributed by the curve even where data uncertainty is unchanged
- **The Test:** Compare straight-axis density vs warped density; large differences suggest the warp is altering probabilistic meaning [@fengMatchingVisualSaliency2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use straight (unwarped) PC density when PDF rigor matters
- **Best Fix:** If you keep curves for perception, explicitly treat/label the view as a warped visualization and avoid quantitative claims based on area/brightness [@fengMatchingVisualSaliency2010].
