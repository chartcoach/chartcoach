---
id: use-samples-uncertainty-distributions-as-kde-kernels
title: "Use Each Sample\u2019s Uncertainty Distribution as the KDE Kernel"
bibliography: references.bib
description: Compute density by summing per-sample statistical distributions so uncertain
  observations contribute broadly and certain observations contribute sharply.
labels:
- chart:scatter
- task:estimate-density
- visual:blur
- impact:trust
- data:uncertainty
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

In KDE density plots of uncertain data, use each observation’s own uncertainty distribution (e.g., its normal with μ and σ) as the kernel rather than a single fixed kernel for all points.

## The Logic <!-- role: reason -->

If the kernel equals the sample’s uncertainty model, the resulting PDF naturally downweights unreliable points by spreading their mass, while reliable points remain concentrated and visually salient. This aligns what “stands out” with what is statistically trustworthy.

- **The Principle:** Uncertainty-proportional contribution to density
- **The Evidence:** [@fengMatchingVisualSaliency2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Summarize uncertain bivariate relationships without letting high-variance points create misleading structure
- **Data Type:** Bivariate uncertain samples where each sample has its own distribution parameters (e.g., σx, σy; optionally correlation ρ)
- **Audience:** Expert analysts working with statistically modeled measurement/estimation uncertainty

## When to Break It <!-- role: exceptions -->

- **Scenario:** You do not have per-sample uncertainty distributions available
- **Reason:** The method depends on quantified uncertainty; without it you must fall back to traditional Parzen windowing (user-chosen kernel) rather than sample-specific kernels [@fengMatchingVisualSaliency2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** More computation than plotting discrete glyphs; requires discretizing the domain into bins/pixels
- **The Risk:** Poor parameterization (wrong σ/ρ assumptions) can misrepresent density structure [@fengMatchingVisualSaliency2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Use a single global kernel width and treat uncertainty as a separate visual encoding
- **Why it fails:** The density no longer reflects confidence; uncertain points can still form visually strong artifacts that should be statistically indistinguishable [@fengMatchingVisualSaliency2010].

## How to Check <!-- role: check -->

- **Visual Sign:** High-variance points appear as sharp “hot spots” comparable to low-variance points
- **The Test:** Pick a known highly uncertain point; verify its contribution appears broad/diffuse rather than point-like in the PDF [@fengMatchingVisualSaliency2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the constant kernel with each sample’s modeled distribution when accumulating density
- **Best Fix:** Support correlation-aware kernels when ρ is available, and use the appropriate bivariate form rather than assuming independence [@fengMatchingVisualSaliency2010].
