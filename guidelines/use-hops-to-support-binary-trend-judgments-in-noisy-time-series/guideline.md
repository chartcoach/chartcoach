---
id: use-hops-to-support-binary-trend-judgments-in-noisy-time-series
title: Use Hypothetical Outcome Plots (HOPs) to Support Binary Trend Judgments in
  Noisy Time Series
bibliography: references.bib
description: Animated draws from the outcome distribution (HOPs) help untrained viewers
  decide which of two trends is more likely when the observed time series is ambiguous.
labels:
- chart:time-series
- task:classify
- visual:animation
- impact:accuracy
- data:temporal
- audience:novice
- uncertainty:sampling
---

## Use HOPs instead of static aggregate uncertainty displays for ambiguous trend classification <!-- role: advice -->

Use Hypothetical Outcome Plots (HOPs) as the uncertainty display when people must choose which of two candidate trends better explains a noisy time series. Prefer HOPs over static aggregate uncertainty displays when the evidence in the observed sample is weak.

## Why HOPs improve sensitivity to evidence in ambiguous trend judgments <!-- role: reason -->

HOPs present uncertainty as repeated hypothetical samples, letting viewers rely on frequency-like impressions of how often samples resemble each candidate trend. This supports perceptual decision-making by strengthening the viewer’s ability to map an ambiguous sample to the more likely generating process.

**Mechanism:** Repeated sampled frames provide an experiential cue to variability from sampling error, making it easier to judge which model would plausibly produce the observed pattern.

**Evidence:** Viewers required less evidence to reach mean accuracy on a two-alternative trend task when using HOPs than when using error bars, reflected in lower just-noticeable differences (JNDs) from psychometric function fits [@kaleHypotheticalOutcomePlots2019]. Viewers also required less evidence with regular-rate line HOPs than with static line ensembles that aggregate the same samples into one view [@kaleHypotheticalOutcomePlots2019].

**Notes:** The benefit was clearest for the regular-rate HOP condition (400 ms/sample) and was attenuated at very fast rates (100 ms/sample) [@kaleHypotheticalOutcomePlots2019].

## When binary trend inference from noisy samples is the core task <!-- role: context -->

- **User Goal:** Decide which of two candidate trends (e.g., “growth” vs “no growth”) is more likely given a noisy observed time series.
- **Task:** Two-alternative forced-choice classification using a reference depiction of uncertainty for each candidate trend.
- **Data:** Temporal sequence with substantial sampling variability relative to the trend magnitude (ambiguous samples common).
- **Chart Setting:** Reference uncertainty visualizations shown alongside an observed sample; animation is feasible (web/app/report).
- **Audience:** Untrained or statistically novice viewers.
- **Success Criterion:** Higher sensitivity to evidence (correct decisions at lower evidence levels).

## When not to rely on HOPs for this decision aid <!-- role: exceptions -->

**Break it when:** The display context cannot support animation (e.g., static-only medium) or users cannot attend to changing frames. **Why:** The HOP advantage depends on integrating information over time from repeated sampled frames [@kaleHypotheticalOutcomePlots2019].

## Tradeoffs of using HOPs for trend judgments <!-- role: costs -->

**Sacrifice:** You give up a single static summary view and require time to watch multiple frames. **Risk:** If viewers do not watch long enough, they may not integrate enough samples to benefit. **Mitigation:** Ensure the animation is presented in a context where viewing time and attention are plausible constraints.

## Common ways HOP deployments fail in practice <!-- role: mistakes -->

- **Mistake:** Playing HOPs so fast that individual samples are hard to register. **Why it fails:** Performance gains were smaller and unreliable at very fast frame rates (100 ms/sample) than at regular rates (400 ms/sample) [@kaleHypotheticalOutcomePlots2019].
- **Mistake:** Assuming HOPs will always increase confidence calibration. **Why it fails:** Confidence fitness (coherence of confidence with modeled accuracy) did not reliably differ by visualization condition [@kaleHypotheticalOutcomePlots2019].

## Quick checks that your HOP is aiding trend discrimination <!-- role: check -->

**Failure Sign:** Users frequently misclassify near-ambiguous samples even after watching, or stop watching early. **Quick Check:** Informally test with a few ambiguous examples and ask users to decide quickly after viewing; look for consistent improvement versus a static alternative. **Stronger Test:** Fit psychometric functions to repeated judgments across evidence levels and verify that JND decreases relative to a static alternative [@kaleHypotheticalOutcomePlots2019].

## Alternatives if HOPs cannot be used <!-- role: fix -->

- Use a static line ensemble showing multiple sampled outcomes when animation is not possible.
- If using a static ensemble, avoid designs that collapse the samples into a purely density-like appearance that obscures discreteness.
- Switch the medium to one that supports animation if the decision hinges on parsing sampling variability from signal.
- If animation must be extremely fast, consider reverting to a static ensemble rather than assuming fast HOPs will retain the benefit.
