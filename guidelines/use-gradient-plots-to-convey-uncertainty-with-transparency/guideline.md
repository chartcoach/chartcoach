---
id: use-gradient-plots-to-convey-uncertainty-with-transparency
title: Use Gradient Plots to Encode Uncertainty with Transparency
bibliography: references.bib
description: Represent uncertainty around a mean using a symmetric opacity gradient
  rather than discrete error bars.
labels:
- chart:gradient
- task:infer
- visual:transparency
- impact:bias-reduction
- data:uncertainty
- audience:novice
- source:correll-gleicher-2014
---

## The Rule <!-- role: advice -->

When showing a mean with uncertainty for inferential reading, use a symmetric gradient plot where opacity decreases as values become less plausible.

## The Logic <!-- role: reason -->

Transparency provides a continuous cue of uncertainty and avoids the bar’s containment metaphor. In the paper’s studies, continuous/symmetric alternatives increased adherence to expected strategies and improved calibration of confidence compared to bar charts.

- **The Principle:** Continuous uncertainty cueing via alpha reduces categorical cutoff reasoning and containment bias.
- **The Evidence:** Gradient plots mitigated within-the-bar bias and were associated with higher, more statistically-aligned confidence than bar charts in one-sample tasks [@correllErrorBarsConsidered2014].

## Where to Apply <!-- role: context -->

- **User Goal:** Assessing how plausible outcomes are at varying distances from the mean; comparing overlap of uncertain estimates.
- **Data Type:** Means with confidence intervals or distributional assumptions (e.g., t-based inference as in the paper).
- **Audience:** General audiences; settings where you want to discourage overly precise readings.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Display conditions make transparency unreliable (e.g., reproduction variability) and the audience must extract precise numeric uncertainty levels.
- **Reason:** The paper notes viewers are not proficient at extracting precise alpha values and display reproduction can vary, making gradients less suitable for precision reading [@correllErrorBarsConsidered2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Precise decoding of uncertainty levels; gradients are intentionally imprecise.
- **The Risk:** Poor display/printing can compress visible transparency differences.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a gradient that is not centered on the mean or that creates a hard opaque block with unclear meaning.
- **Why it fails:** It can reintroduce binary “in/out” thinking or obscure where the mean is [@correllErrorBarsConsidered2014].

## How to Check <!-- role: check -->

- **Visual Sign:** The plot does not clearly show the mean, or the fade does not look symmetric around it.
- **The Test:** Flip the chart vertically; the uncertainty pattern should look the same above and below the mean [@correllErrorBarsConsidered2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a clear mean marker and enforce symmetry of the opacity profile around it.
- **Best Fix:** Implement the paper’s approach: fully opaque within the chosen CI and decaying opacity outside to convey decreasing plausibility [@correllErrorBarsConsidered2014].
