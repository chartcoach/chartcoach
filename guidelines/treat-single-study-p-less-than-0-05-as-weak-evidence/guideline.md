---
id: treat-single-study-p-less-than-0-05-as-weak-evidence
title: Treat a single-study p < 0.05 claim as weak evidence unless pre-study odds
  and power are high
bibliography: references.bib
description: A statistically significant result from one study is often more likely
  false than true when prior odds are low or power is limited.
labels:
- chart:forest
- task:evaluate
- visual:annotation
- impact:trust
- data:inferential
- audience:expert
- domain:research-evidence
---

## Single-study significance needs prior-odds and power context <!-- role: advice -->

Treat a single-study p < 0.05 result as tentative unless the display also communicates the study’s power and the pre-study odds that the relationship is true. If those inputs are unknown or plausibly low, present the claim as low-confidence rather than definitive.

## Why p < 0.05 alone often misleads <!-- role: reason -->

Statistical significance only controls a Type I error rate (false positives) conditional on the null, but the chance that a significant finding is true (the positive predictive value) depends strongly on pre-study odds and power; with low pre-study odds or low power, most “significant” findings can be false.

**Mechanism:** Adding pre-study odds and power shifts interpretation from “is it significant?” to “how likely is it true?”, reducing overconfidence in isolated significant results.

**Evidence:** The post-study probability that a claimed relationship is true (positive predictive value) is a function of pre-study odds, power, and α, and can be below 50% in many realistic settings even with α = 0.05 [@ioannidisWhyMostPublished2005]. Simulations across study designs show low positive predictive value for underpowered or exploratory settings, implying many published significant claims are false [@ioannidisWhyMostPublished2005].

**Notes:** This guidance targets claims of existence of relationships (positive findings), not the value of well-reported null results.

## When this applies in evidence displays <!-- role: context -->

- **User Goal:** Decide how much to trust a reported “significant” effect.
- **Task:** Assess probability a finding is true given study properties and research setting.
- **Data:** Study results with p-values or significance flags; available or inferable power and pre-study plausibility.
- **Chart Setting:** Evidence summary visuals (e.g., forest plots, evidence tables, “significance” dashboards).
- **Audience:** Researchers, clinicians, policy analysts, peer reviewers.
- **Success Criterion:** Reduced false certainty; calibrated confidence aligned with true-likelihood.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The display is restricted to reporting a pre-registered confirmatory test with high power and high pre-study odds as part of a broader synthesis. **Why:** In those cases, the positive predictive value can be high enough that a significant result is less likely to be false than true.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Extra space and cognitive load to show power and pre-study odds assumptions. **Risk:** Readers may dispute priors or misread them as subjective. **Mitigation:** Frame priors as explicit scenarios (plausible ranges) rather than a single asserted value.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Encoding “p < 0.05” as a binary badge of truth (e.g., green checkmark). **Why it fails:** It hides dependence on pre-study odds and power, inflating confidence in many settings where most significant claims are false.
- **Mistake:** Showing only point estimates with a “significant/non-significant” label. **Why it fails:** It implies conclusiveness without communicating the conditions that drive the probability the claim is true.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers can conclude “this is true” from significance alone without seeing power or plausibility. **Quick Check:** Remove the p-value column—if the display becomes unusable, it was over-dependent on significance. **Stronger Test:** Ask a pilot reader to estimate how likely the claim is true; if they answer near-certain based on p < 0.05, the design is miscalibrating trust.

## What to do instead <!-- role: fix -->

- Add an annotation or side panel that states assumed pre-study odds (or a range) and the study’s power for the target effect size.
- Replace binary “significant” styling with a graded confidence display tied to positive predictive value scenarios.
- Group findings by research setting (confirmatory vs exploratory; massive testing vs limited testing) and visually downweight exploratory single-study claims.
- Provide a small “what would change my mind” note indicating the need for replication or higher-powered confirmation when priors are low.
