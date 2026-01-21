---
id: use-qq-plots-to-assess-distribution-fit
title: "Use Q\u2013Q Plots to Compare Data Against Statistical Distributions"
bibliography: references.bib
description: "Use Q\u2013Q plots to diagnose whether data matches a candidate distribution\
  \ or mixture model."
labels:
- chart:qq-plot
- task:validate
- visual:position
- impact:correctness
- data:numerical
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

Use a Q–Q plot to compare your data’s distribution to a theoretical or fitted distribution, and look for departures from the diagonal.

## The Logic <!-- role: reason -->

A Q–Q plot graphs quantiles against quantiles: similar distributions fall near the diagonal; structured deviations indicate mismatch and can suggest alternative models (e.g., mixtures).

- **The Principle:** Quantile comparison reveals distributional similarity and model mismatch
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Choose or validate a statistical model during exploratory data analysis
- **Data Type:** Numeric samples compared to candidate distributions (uniform, Gaussian, mixtures)
- **Audience:** Statistically literate analysts

## When to Break It <!-- role: exceptions -->

- **Scenario:** The audience lacks statistical knowledge
- **Reason:** Effective use requires statistical understanding [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Accessibility for non-expert viewers
- **The Risk:** Misinterpretation of deviations without context about quantiles and reference distributions

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Relying only on a histogram shape to “confirm” a model
- **Why it fails:** Q–Q plots provide a more powerful comparison across the full distribution [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** Points bend away from a straight diagonal or form multiple components
- **The Test:** If the plotted points are not roughly linear, your assumed model likely doesn’t fit [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Compare against a few plausible reference distributions
- **Best Fix:** Fit and compare an alternative model (including mixtures) and verify improved linearity in the Q–Q plot [@heerTourVisualizationZoo2010]
