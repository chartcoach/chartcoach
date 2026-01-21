---
id: sample-uncertain-kde-mixture-by-randomly-choosing-a-point-then-sampling-its-distributions
title: Sample Mixture PDFs by Picking a Random Observation Then Sampling Its Variables
bibliography: references.bib
description: Exploit equal-weight mixtures and independent per-variable uncertainty
  to generate fast probabilistic plot samples.
labels:
- chart:parallel-coordinates
- task:sample
- impact:performance
- data:uncertainty
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

To generate probabilistic plot samples from a KDE mixture of uncertain points, first pick a random observation uniformly, then sample each of its independent per-variable distributions to form one multivariate sample.

## The Logic <!-- role: reason -->

When the KDE is an equal-weight mixture over observations and each observation’s uncertainty factorizes across variables, the global PDF can be sampled by mixture sampling: choose a component (a data point) then sample from that component. This avoids storing or computing an intractable N-dimensional discretized PDF.

- **The Principle:** Efficient mixture sampling from factorized uncertainty models
- **The Evidence:** [@fengMatchingVisualSaliency2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Create fast animated probabilistic scatter/PC plots for very large uncertain datasets
- **Data Type:** Multivariate KDE where each sample has independent normal distributions per variable (as in the paper’s MRS case)
- **Audience:** Expert implementers building interactive uncertainty visualizations

## When to Break It <!-- role: exceptions -->

- **Scenario:** Observations have unequal weights or strong inter-variable dependence not captured by independent marginals
- **Reason:** Uniform component selection and independent sampling would not match the true PDF [@fengMatchingVisualSaliency2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires access to the underlying uncertainty model per observation (μ, σ per variable)
- **The Risk:** If independence is assumed incorrectly, sampled plots can misrepresent correlation structure [@fengMatchingVisualSaliency2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Attempt to discretize and store the full N-dimensional PDF for sampling
- **Why it fails:** The ND grid is intractable for modest N; the paper’s approach avoids this by sampling the mixture directly [@fengMatchingVisualSaliency2010].

## How to Check <!-- role: check -->

- **Visual Sign:** The probabilistic plot’s long-run accumulation does not resemble the expected density structure
- **The Test:** Accumulate many samples into a histogram buffer; it should converge toward the PDF approximation described in the paper [@fengMatchingVisualSaliency2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Implement two-step mixture sampling (random point, then sample its per-variable distributions)
- **Best Fix:** If correlations (ρ≠0) matter, extend the per-point sampling step to draw from the appropriate correlated multivariate distribution before plotting [@fengMatchingVisualSaliency2010].
