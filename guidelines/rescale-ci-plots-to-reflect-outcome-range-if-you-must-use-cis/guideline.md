---
id: rescale-ci-plots-to-reflect-outcome-range-if-you-must-use-cis
title: Rescale CI Plots to Reflect Outcome Range When Using CIs
bibliography: references.bib
description: If you must plot CIs, expand the axis to match the outcome-uncertainty
  range to reduce inflated effect impressions.
labels:
- chart:error-bar
- task:compare
- visual:scale
- impact:bias-reduction
- data:experimental
- audience:novice
- uncertainty:hybrid
---

## The Rule <!-- role: advice -->

If you choose to show 95% confidence intervals, set the axis range to accommodate the plausible individual outcome range (i.e., do not let the CI plot’s tight axis make effects look larger than they are).

## The Logic <!-- role: reason -->

A tight axis around means can amplify perceived separation; expanding the axis to include the broader outcome range partially counters this by making the small mean shift visually smaller relative to variability.

- **The Principle:** Axis scaling changes perceived magnitude; including outcome range provides a hybrid cue about effect size vs variability.
- **The Evidence:** In Experiment 2, “rescaled 95% CI” plots reduced error relative to conventional 95% CI plots, though they still did not match the accuracy of PIs or HOPs [@hofmanHowVisualizingInferential2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare conditions while still seeing inferential uncertainty, but avoid overstating practical impact.
- **Data Type:** Mean-with-interval displays where outcome variability is large.
- **Audience:** Mixed audiences where CIs are expected but miscalibration is a concern.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Space-constrained small multiples where expanded axes would make mean comparisons illegible.
- **Reason:** The rescale may prevent users from reading differences at all, trading one error for another [@hofmanHowVisualizingInferential2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Mean differences become visually subtle and may require more effort to compare.
- **The Risk:** Readers may miss small-but-real differences because the plot no longer visually foregrounds them [@hofmanHowVisualizingInferential2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keep the tight CI axis and add outcome range numbers only in text.
- **Why it fails:** Text does not reliably counteract the perceptual amplification of a tight axis and CI bars [@hofmanHowVisualizingInferential2020].

## How to Check <!-- role: check -->

- **Visual Sign:** The y-axis spans only a few units around the means, and the CI bars occupy much of the plot height.
- **The Test:** Re-render the same chart with an axis spanning the plausible outcome range; if the “effect” visually shrinks dramatically, the original likely exaggerated perceived magnitude [@hofmanHowVisualizingInferential2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Expand the axis to cover the outcome-uncertainty range used in a PI depiction (or otherwise justified individual-outcome range).
- **Best Fix:** Replace the CI display with an outcome-uncertainty visualization (PI or outcome samples), keeping CIs as secondary if needed [@hofmanHowVisualizingInferential2020].
