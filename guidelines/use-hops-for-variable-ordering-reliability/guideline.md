---
id: use-hops-for-variable-ordering-reliability
title: Use Hypothetical Outcome Plots for Variable-Ordering Reliability Judgments
bibliography: references.bib
description: Prefer Hypothetical Outcome Plots (HOPs) over error bars or violin plots
  when users must judge how often one variable exceeds another.
labels:
- chart:animation
- task:compare
- visual:position
- impact:accuracy
- data:multivariate
- audience:novice
- uncertainty:distribution
---

## The Rule <!-- role: advice -->

Use Hypothetical Outcome Plots (HOPs)—animated draws from the distribution—when the user’s key question is “How often is B > A?” (or B is the largest among several variables).

## The Logic <!-- role: reason -->

HOPs turn a probability question into a frequency/counting task (“count frames where B > A”), avoiding the need to decode abstract uncertainty encodings (intervals or density shapes) and supporting more direct integration over outcomes. In the study, HOPs produced much lower mean absolute error for bivariate and trivariate ordering probabilities than both error bars and violin plots.

- **The Principle:** Concrete frequency reasoning and direct outcome comparison
- **The Evidence:** [@hullmanHypotheticalOutcomePlots2015]

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating ordering reliability (e.g., Pr(B > A), Pr(B > A and B > C)) rather than just comparing means.
- **Data Type:** Two or more uncertain quantities (including correlated variables) where joint behavior matters.
- **Audience:** General/lay audiences or anyone not expected to correctly infer joint probabilities from static uncertainty summaries.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The only question is a univariate summary like the mean with high variance, and you need a quick, static read.
- **Reason:** HOPs require integration over many frames and performed worse for estimating the mean when variance was high. [@hullmanHypotheticalOutcomePlots2015]

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires animation/interaction support and time to view multiple frames.
- **The Risk:** Viewers may see only a finite number of frames, introducing sampling error and potentially noisier impressions if they don’t watch enough outcomes. [@hullmanHypotheticalOutcomePlots2015]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using error bars or violin plots and expecting users to accurately infer Pr(B > A) from overlap, distance between means, or density silhouettes.
- **Why it fails:** The paper shows very large errors for ordering-probability judgments with these static encodings, even under favorable normal-distribution conditions. [@hullmanHypotheticalOutcomePlots2015]

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate or give implausible ordering probabilities (e.g., \<50% when B’s mean is clearly higher).
- **The Test:** User test: show the chart and ask for Pr(B > A) out of 100; if average absolute error is large or responses cluster at wild extremes, the encoding is not supporting the task. [@hullmanHypotheticalOutcomePlots2015]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a HOPs view (even as an optional animated mode) alongside the existing static plot for ordering questions.
- **Best Fix:** Make HOPs the primary representation for multivariate ordering reliability tasks, with stable axes and repeated frames that allow visual counting/integration. [@hullmanHypotheticalOutcomePlots2015]
