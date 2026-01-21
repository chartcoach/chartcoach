---
id: use-outcome-sampling-visualizations-to-support-probability-of-superiority-judgments
title: Use Outcome Sampling to Support Probability-of-Superiority Judgments
bibliography: references.bib
description: When users must judge how often one condition beats another, show samples
  of individual outcomes (e.g., HOPs) or PIs.
labels:
- chart:animation
- task:probability-estimation
- visual:frequency
- impact:decision-support
- data:distribution
- audience:novice
- metric:probability-of-superiority
---

## The Rule <!-- role: advice -->

For questions of the form “How often will treatment beat control?”, use an outcome-uncertainty visualization such as individual outcome samples (HOP-style) or prediction intervals—not CI error bars.

## The Logic <!-- role: reason -->

Probability of superiority depends on overlap between outcome distributions; outcome-sampling and PI displays surface that overlap directly, whereas CI displays can mask overlap and cue near certainty.

- **The Principle:** Match the visualization to the probabilistic quantity (superiority depends on outcome distributions, not sampling precision).
- **The Evidence:** Participants shown CIs reported much higher probability of superiority than those shown PIs or outcome samples; in Experiment 2, PIs and HOPs yielded similar (and closer-to-true) superiority judgments, while CI conditions were biased high and showed ceiling effects [@hofmanHowVisualizingInferential2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimate chance of winning/benefiting (probability of superiority) and make value judgments (e.g., willingness to pay).
- **Data Type:** Two distributions with overlap; small-to-moderate mean differences.
- **Audience:** General public / applied decision settings.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The only task is to assess whether the mean difference is estimated precisely (inferential question), not to predict individual outcomes.
- **Reason:** Superiority-focused encodings may distract from inferential precision goals [@hofmanHowVisualizingInferential2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Outcome samples/animations require more time/space (and potentially motion support) than static error bars.
- **The Risk:** Some contexts (e.g., static print) may not support animation, requiring alternative outcome-uncertainty encodings [@hofmanHowVisualizingInferential2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Use CI bars and ask readers to infer “how often” from the distance between means.
- **Why it fails:** The paper shows CI displays drive large overestimates of superiority, especially for small effects [@hofmanHowVisualizingInferential2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Readers’ superiority estimates cluster near 0.9–1.0 even when the effect is small and distributions should overlap heavily.
- **The Test:** Compare a CI-based design vs a PI/sample-based design in a quick A/B read test; if CI readers give much higher superiority estimates, the CI design is likely misleading [@hofmanHowVisualizingInferential2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch CI bars to 95% PIs so overlap is visible.
- **Best Fix:** Provide outcome samples over time (HOP-like) so readers can intuit superiority by observing/counted dominance across samples [@hofmanHowVisualizingInferential2020].
