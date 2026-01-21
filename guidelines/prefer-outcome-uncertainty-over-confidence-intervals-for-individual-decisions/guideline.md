---
id: prefer-outcome-uncertainty-over-confidence-intervals-for-individual-decisions
title: Prefer Outcome-Uncertainty Visualizations for Individual Decisions
bibliography: references.bib
description: When readers must reason about individual outcomes, show outcome uncertainty
  (PIs or outcome samples) instead of only inferential uncertainty (CIs).
labels:
- chart:error-bar
- task:decide
- visual:position
- impact:calibration
- data:distribution
- audience:novice
- uncertainty:outcome-vs-inferential
---

## The Rule <!-- role: advice -->

When the reader is deciding for themselves (e.g., “Should I pay for this treatment?”), visualize **outcome uncertainty** (e.g., 95% prediction intervals or samples of individual outcomes), not just **inferential uncertainty** (e.g., 95% confidence intervals).

## The Logic <!-- role: reason -->

Outcome-focused displays make the variability of individual results salient, preventing readers from treating a small uncertainty about the mean as if it implies consistent individual benefit.

- **The Principle:** Distinguish uncertainty in the mean (sampling/inferential) from variability in individual outcomes (outcome uncertainty).
- **The Evidence:** Across two preregistered experiments, CI-oriented visuals caused people to overstate willingness to pay and probability of superiority and to understate outcome variability, while PI- and sample-oriented visuals were closest to normatively correct answers [@hofmanHowVisualizingInferential2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide whether a treatment/intervention is “worth it” for an individual; judge chance of personal benefit (probability of superiority).
- **Data Type:** Two-group experimental results with substantial within-group variability.
- **Audience:** General readers / lay decision makers (and any audience likely to default to “small bars = big effect”).

## When to Break It <!-- role: exceptions -->

- **Scenario:** The communication goal is explicitly about *precision of the estimated mean* (e.g., comparing group means as estimates for a population parameter).
- **Reason:** In that case, inferential uncertainty is the target quantity, so outcome-uncertainty displays may obscure the desired message [@hofmanHowVisualizingInferential2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Outcome-uncertainty visuals often require wider axes or denser marks, making mean differences harder to read at a glance.
- **The Risk:** Readers focused on mean differences may feel the effect is “small” because the variability is visually dominant [@hofmanHowVisualizingInferential2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Show only 95% CIs (or SE bars) and assume readers will mentally “scale up” to infer outcome variability.
- **Why it fails:** The paper finds readers do not reliably infer individual-outcome variation from CI-style bars and consequently overestimate treatment effectiveness [@hofmanHowVisualizingInferential2020].

## How to Check <!-- role: check -->

- **Visual Sign:** The plot shows tight intervals around each mean (CI/SE-style), inviting “near certainty” impressions.
- **The Test:** Ask a pilot reader: “How often would the treatment outperform control?” If estimates cluster near 1.0 for a small effect, your display is likely CI-driven miscalibration [@hofmanHowVisualizingInferential2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace CI/SE error bars with 95% prediction intervals (or SD-based intervals) so the display reflects individual variation.
- **Best Fix:** Use an outcome-sampling visualization (e.g., animated hypothetical outcome samples) to make individual variability and superiority frequency easy to perceive [@hofmanHowVisualizingInferential2020].
