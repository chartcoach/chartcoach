---
id: prefer-hops-over-error-bars-for-public-uncertainty
title: Replace Error Bars with Sampling-Oriented Uncertainty for Lay Audiences
bibliography: references.bib
description: Avoid error bars for public-facing uncertainty reasoning tasks; use sampling-oriented
  depictions like HOPs instead.
labels:
- chart:error-bars
- chart:uncertainty
- task:infer
- visual:position
- impact:interpretability
- data:temporal
- audience:novice
- uncertainty:sampling
---

## The Rule <!-- role: advice -->

For public-facing uncertainty communication where users must reason from noisy data, avoid error bars and use sampling-oriented uncertainty displays (e.g., HOPs).

## The Logic <!-- role: reason -->

The paper motivates that error bars are frequently misunderstood and can draw attention to expected value over variability; in Experiment 1, participants using HOPs achieved correct trend judgments at lower evidence levels than participants using error bars (lower JNDs), indicating better support for uncertainty-based inference [@kaleHypotheticalOutcomePlots2019].

- **The Principle:** Concrete samples of outcomes reduce reliance on opaque statistical conventions.
- **The Evidence:** [@kaleHypotheticalOutcomePlots2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Make a yes/no or A/B judgment about what the data implies (e.g., which trend is more likely) under sampling error.
- **Data Type:** Noisy measurements over time where uncertainty is part of the message.
- **Audience:** General audiences with limited statistical training (e.g., news readers) [@kaleHypotheticalOutcomePlots2019].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your audience is trained and the task explicitly requires reading the specific interval statistic (e.g., a confidence interval) as presented.
- **Reason:** The paper’s demonstrated benefit targets untrained observers and inference-from-noise tasks, not specialist statistical workflows [@kaleHypotheticalOutcomePlots2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Sampling-oriented displays may require more viewing time or space (if shown statically as many samples) than a compact error bar.
- **The Risk:** If implemented poorly (too many marks or too fast animation), the intended “frequency” interpretation may degrade [@kaleHypotheticalOutcomePlots2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more explanatory text to error bars instead of changing the representation.
- **Why it fails:** The experiments show a perceptual sensitivity advantage from changing the encoding to sampled outcomes, not from additional description [@kaleHypotheticalOutcomePlots2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers treat uncertainty as an accessory rather than as variability in possible outcomes.
- **The Test:** Ask users what the uncertainty mark *means* in terms of potential repeated outcomes; if they cannot describe outcomes/samples, the encoding is likely too abstract [@kaleHypotheticalOutcomePlots2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap error bars for an animated HOP that cycles through sampled outcomes from the distribution.
- **Best Fix:** Structure the display so uncertainty is encountered as repeated draws tied to the generating process (show multiple outcomes for each candidate explanation), matching the paper’s successful decision-aid framing [@kaleHypotheticalOutcomePlots2019].
