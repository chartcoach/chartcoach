---
id: encode-correlation-in-uncertainty-when-ordering-matters
title: Show Correlation Explicitly When Ordering Depends on Joint Behavior
bibliography: references.bib
description: Use uncertainty depictions that preserve correlation when users must
  reason about comparative outcomes across variables.
labels:
- chart:animation
- task:compare
- visual:position
- impact:truthfulness
- data:multivariate
- audience:novice
- uncertainty:correlation
---

## The Rule <!-- role: advice -->

When comparative judgments depend on correlation between variables, use a depiction (such as HOPs) that visibly represents correlation rather than separate marginal summaries.

## The Logic <!-- role: reason -->

Separate univariate uncertainty summaries (error bars, violin plots) can omit correlation structure; viewers then cannot correctly infer ordering probabilities that change under correlation. HOPs animate paired draws, preserving joint structure frame-by-frame, and the experiment included a high-correlation condition where HOPs remained accurate while static marginal depictions did not.

- **The Principle:** Preserve joint distribution information needed for inference
- **The Evidence:** [@hullmanHypotheticalOutcomePlots2015]

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating Pr(B > A) (or similar comparisons) where correlation could increase or decrease ordering reliability.
- **Data Type:** Multivariate uncertainty with nontrivial correlation.
- **Audience:** Viewers who are unlikely to infer correlation from context or statistical training.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Variables are known independent (or correlation is irrelevant to the task) and you only need marginal statements about each variable.
- **Reason:** If joint structure doesn’t affect the intended inference, preserving correlation in the depiction is unnecessary overhead. [@hullmanHypotheticalOutcomePlots2015]

## The Price <!-- role: costs -->

- **The Sacrifice:** More complex display (animation or explicit joint encoding).
- **The Risk:** Viewers may under-sample frames and get a noisier estimate of joint effects unless enough outcomes are observed. [@hullmanHypotheticalOutcomePlots2015]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing two separate error bars/violins and assuming viewers can infer how co-movement affects Pr(B > A).
- **Why it fails:** Those plots can communicate only marginals; the paper demonstrates large errors for ordering tasks and notes that correlation is not conveyed in such static summaries. [@hullmanHypotheticalOutcomePlots2015]

## How to Check <!-- role: check -->

- **Visual Sign:** Two displays with the same marginals but different correlation look identical (or nearly so) to the user.
- **The Test:** A/B test with correlated vs independent data holding marginals constant; if users’ Pr(B > A) estimates don’t change appropriately, your depiction isn’t encoding correlation. [@hullmanHypotheticalOutcomePlots2015]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a HOPs “paired-draw” animation mode for the variables being compared.
- **Best Fix:** Choose a representation that directly shows joint outcomes per draw (HOPs frames with stable scales), so correlation is perceptually available through co-variation over frames. [@hullmanHypotheticalOutcomePlots2015]
