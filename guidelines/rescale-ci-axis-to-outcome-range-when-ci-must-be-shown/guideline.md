---
id: rescale-ci-axis-to-outcome-range-when-ci-must-be-shown
title: Rescale the axis to the outcome range when you must show 95% CIs
bibliography: references.bib
description: If you show confidence intervals, scale the axis to include the outcome
  variability range to reduce exaggerated effect impressions.
labels:
- chart:errorbar
- task:compare
- visual:scale
- impact:accuracy
- data:uncertainty
- audience:novice
- domain:scientific-reporting
---

## Put CI error bars on an axis that spans the outcome range, not just the mean range <!-- role: advice -->

When you must display 95% Confidence Intervals (CIs), scale the plotting range to accommodate the full outcome spread (as if you were showing prediction intervals) rather than zooming tightly around the means.

## Wider framing reduces visual magnification of small mean differences <!-- role: reason -->

A tight axis range makes small mean differences and narrow CI bars look large and decisive. Expanding the axis to the outcome range reduces perceptual magnification of the mean difference, partially counteracting CI-driven overconfidence while retaining the CI encoding.

**Mechanism:** Axis rescaling changes the perceived signal-to-uncertainty ratio by reducing the apparent separation of means relative to the displayed range.

**Evidence:** A rescaled-CI condition produced responses between conventional CIs and outcome-uncertainty displays: it improved willingness-to-pay and probability-of-superiority judgments relative to conventional CI plots, but was still generally less accurate than 95% PIs or HOPs in the tested tasks [@hofmanHowVisualizingInferential2020]. Rescaled CIs reduced (but did not eliminate) underestimation of outcome variability relative to conventional CI plots [@hofmanHowVisualizingInferential2020].

**Notes:** This is a partial mitigation, not a substitute for showing outcome uncertainty when individual outcomes matter.

## When CI plots are required but readers still need calibrated effect impressions <!-- role: context -->

- **User Goal:** Interpret the practical importance of a treatment effect without being misled by visual magnification.
- **Task:** Compare treatment vs control; form beliefs about how strong the advantage is.
- **Data:** Two-group outcomes with sizable within-group variance; effect may be small.
- **Chart Setting:** Publication norms or stakeholders require CI display; limited space for multiple panels.
- **Audience:** Readers likely to use visual heuristics from error bars.
- **Success Criterion:** Reduced overestimation of probability of superiority and willingness to pay compared with a tightly zoomed CI plot.

## When not to rely on rescaling <!-- role: exceptions -->

**Break it when:** The main task is precise reading of small differences in means from the plot. **Why:** Rescaling can make mean differences harder to visually discriminate, potentially increasing reading error even if it reduces bias [@hofmanHowVisualizingInferential2020].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** Sensitivity for small mean differences decreases when the axis spans the full outcome range. **Risk:** Readers may miss meaningful but small shifts in the mean if they only eyeball distances. **Mitigation:** Keep mean markers prominent and consider pairing with an outcome-uncertainty encoding when space allows.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Zooming the y-axis to the CI extent to “make the difference visible.” **Why it fails:** It visually amplifies the apparent effect and encourages overestimation of treatment effectiveness [@hofmanHowVisualizingInferential2020].
- **Mistake:** Treating rescaling as equivalent to showing outcome uncertainty. **Why it fails:** Rescaling helps somewhat but did not match the accuracy of PIs or HOPs across measures [@hofmanHowVisualizingInferential2020].

## Quick tests <!-- role: check -->

**Failure Sign:** The mean gap looks large relative to the plotted range, but readers still underestimate outcome variability or give near-certain superiority judgments. **Quick Check:** Compare the plotted range to the implied outcome spread; if the axis barely extends beyond the CI bars, the plot is likely visually magnifying the effect. **Stronger Test:** A/B test conventional vs rescaled CI with a probability-of-superiority question.

## What to do instead <!-- role: fix -->

- Expand the axis range to match the scale you would use to show outcome variability for the same data.
- Use a PI or HOP visualization when the audience must reason about individual outcomes or probability of superiority.
- If both constructs matter, show outcome uncertainty visually and report inferential uncertainty in accompanying text.
- Validate the figure with a small reader check focused on probability-of-superiority and perceived variability.
