---
id: avoid-ci-error-bars-when-the-takeaway-is-effect-size
title: Avoid CI Error Bars When the Takeaway Is Effect Size
bibliography: references.bib
description: CI-focused error bars systematically push readers toward inflated perceptions
  of effectiveness, especially for small effects.
labels:
- chart:error-bar
- task:estimate
- visual:position
- impact:truthfulness
- data:experimental
- audience:novice
- effect-size:small
---

## The Rule <!-- role: advice -->

When communicating how big an effect is (not just whether it’s statistically distinguishable), do not use CI-style error bars as the primary visual—use outcome-uncertainty encodings.

## The Logic <!-- role: reason -->

CI displays shrink with larger sample sizes and emphasize precision about the mean, which readers can misread as “the treatment works reliably for most individuals,” inflating perceived effect.

- **The Principle:** CI width reflects inferential precision, not individual variability; readers conflate the two.
- **The Evidence:** CI-oriented visuals produced the largest overstatements of willingness to pay and probability of superiority, and the greatest underestimation of outcome variability; biases were most concerning for smaller effects (≈ Cohen’s d 0.25) [@hofmanHowVisualizingInferential2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Understand practical magnitude/impact of a treatment or intervention.
- **Data Type:** Two-group comparisons where within-group variance is large relative to mean difference (common in behavioral/medical settings).
- **Audience:** Lay readers and mixed audiences where “effect size” is the intended message.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The intended message is explicitly “how precisely have we estimated the mean?” (e.g., methodological emphasis on estimation precision).
- **Reason:** CIs are appropriate for inferential precision; the mismatch occurs when the intended takeaway is individual-level impact [@hofmanHowVisualizingInferential2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Outcome-uncertainty visuals can make small mean shifts harder to see quickly.
- **The Risk:** You may need to spend more annotation effort to help readers locate and compare means [@hofmanHowVisualizingInferential2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Use conventional CI bars because they are “standard,” assuming they are a neutral uncertainty display.
- **Why it fails:** In the experiments, CI displays consistently biased effect judgments upward relative to PI and outcome-sampling displays [@hofmanHowVisualizingInferential2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Narrow bars around means plus a tight y-range that visually amplifies separation.
- **The Test:** Ask: “Could a reader infer how much individual outcomes overlap?” If not, you’re likely signaling significance/precision rather than effect size [@hofmanHowVisualizingInferential2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace CI/SE bars with PI (SD-based) intervals to expose overlap and variability.
- **Best Fix:** Show individual-outcome samples (e.g., HOPs) or otherwise encode the distribution of outcomes so overlap is perceptually available [@hofmanHowVisualizingInferential2020].
