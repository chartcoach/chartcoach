---
id: support-angular-and-linear-function-brushing-by-integrating-mass-between-bracketing-lines
title: Implement angular and linear-function brushing by integrating distribution
  mass between bracketing lines in transformed space
bibliography: references.bib
description: For uncertain data, evaluate line-proximity brushes as probability mass
  between two parallel boundaries after normalizing the distribution.
labels:
- chart:parallel-coordinates
- task:select
- visual:interaction
- impact:trust
- data:uncertain
- audience:expert
- complexity:advanced
---

## Make line-based brushing uncertainty-aware via probability mass between parallel bounds <!-- role: advice -->

For angular brushing and linear function brushing, select a distribution only if sufficient probability mass lies between two parallel boundary lines that define the brush width. Compute this mass after translating and scaling the distribution to a standard form so line distance can be evaluated consistently.

## Transforming to standardized space makes line-proximity selection computable and comparable <!-- role: reason -->

Error-function-based integration is axis-aligned, while line brushes can have arbitrary orientation. By translating the distribution mean to the origin and scaling by inverse standard deviations, the distribution becomes isotropic (unit variance), letting selection depend on signed distance from the brush boundaries to the origin (Mahalanobis-style distance), which supports fast evaluation of area between two lines.

**Mechanism:** Standardization converts anisotropic uncertainty into a normalized metric so that “near a line” means “high probability of being near the line,” not just “small Euclidean distance from the mean.”

**Evidence:** Angular brushing is treated as selecting values near a line by integrating the bivariate normal distribution between two parallel lines, using a translate-and-scale transform and an error-function computation based on line distance in transformed coordinates [@fengMatchingVisualSaliency2010].

**Notes:** The approach extends to correlated normals by including a rotation to axis-align the covariance before scaling [@fengMatchingVisualSaliency2010].

## When to use uncertainty-aware line brushing <!-- role: context -->

- **User Goal:** Select relationships or trends (for example, near-linear associations) without over-selecting uncertain samples.
- **Task:** Angular brushing in parallel coordinates and general linear-function brushing that corresponds to line proximity in Cartesian space.
- **Data:** Bivariate normal uncertainty models (uncorrelated or correlated) for the variable pair being brushed.
- **Chart Setting:** Interactive multivariate exploration where line-based selection expresses a hypothesized relationship.
- **Audience:** Expert users comfortable with selecting by functional relationships.
- **Success Criterion:** Selection probability reflects both proximity to the relationship and uncertainty magnitude.

## When not to use this brushing method <!-- role: exceptions -->

**Break it when:** The uncertainty model is not representable in a form that supports the described transform and integration for the interaction latency you need. **Why:** The approach depends on efficient evaluation of probability mass for each distribution under the brush [@fengMatchingVisualSaliency2010].

## Tradeoffs of probability-mass line brushing <!-- role: costs -->

**Sacrifice:** Computation per sample is higher than simple geometric distance tests. **Risk:** Users may perceive the brush as inconsistent if they expect purely geometric behavior. **Mitigation:** Keep interaction feedback tied to probability (for example, show likelihood) rather than implying a hard geometric cutoff.

## Common mistakes with line-based uncertainty brushing <!-- role: mistakes -->

- **Mistake:** Use Euclidean distance from the mean to the brushed line as the selection criterion. **Why it fails:** It ignores the distribution’s variance, so uncertain samples can be selected too aggressively or too conservatively depending on scale [@fengMatchingVisualSaliency2010].
- **Mistake:** Apply axis-aligned integration formulas directly to rotated brushes without transforming coordinates. **Why it fails:** Axis-aligned error-function calculations do not match arbitrary line orientation, producing incorrect membership probabilities [@fengMatchingVisualSaliency2010].

## Quick checks for correctness of line-brush selection <!-- role: check -->

**Failure Sign:** Rotating a line brush changes selections in ways unrelated to data uncertainty. **Quick Check:** In standardized space, selections should depend primarily on the signed distances of the two parallel bounds to the origin [@fengMatchingVisualSaliency2010]. **Stronger Test:** Validate that increasing brush width monotonically increases selected mass for each distribution.

## What to do instead if this is too complex to implement <!-- role: fix -->

- Approximate line-brush selection by sampling from each distribution and estimating the fraction of samples that fall between the bounds [@fengMatchingVisualSaliency2010].
- Restrict interactions to interval queries (axis-aligned boxes/ranges) where separable integration is simpler for uncorrelated normals [@fengMatchingVisualSaliency2010].
- Perform selection computations in data space on parallel hardware and only render results in the client [@fengMatchingVisualSaliency2010].
- Use probabilistic plots for interaction, where repeated sampling over time provides an empirical sense of membership likelihood [@fengMatchingVisualSaliency2010].
