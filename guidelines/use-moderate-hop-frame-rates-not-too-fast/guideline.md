---
id: use-moderate-hop-frame-rates-not-too-fast
title: Set HOP Frame Rates to Moderate Speeds
bibliography: references.bib
description: Use moderate HOP frame rates; very fast updates can attenuate performance
  gains for trend inference under uncertainty.
labels:
- chart:animation
- chart:uncertainty
- task:infer
- visual:time
- impact:accuracy
- data:temporal
- audience:novice
- uncertainty:sampling
---

## The Rule <!-- role: advice -->

Use a moderate HOP playback speed rather than an extremely fast one when the goal is accurate inference of an underlying trend from noisy time series data.

## The Logic <!-- role: reason -->

In Experiment 2, regular-speed line HOPs (400 ms per sample) produced a reliable reduction in JNDs versus static line ensembles, while fast HOPs (100 ms per sample) showed a smaller, unreliable improvement—suggesting that pushing frame rates too high can reduce the benefit of animation for perceptual decision-making [@kaleHypotheticalOutcomePlots2019].

- **The Principle:** Ensemble processing over time has practical limits; too-rapid temporal presentation can weaken evidence integration.
- **The Evidence:** [@kaleHypotheticalOutcomePlots2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which generative trend is more likely given noisy observed data.
- **Data Type:** Temporal series where uncertainty is shown as sequences of sampled outcomes.
- **Audience:** Untrained observers who may not track individual frames but can integrate impressions over time [@kaleHypotheticalOutcomePlots2019].

## When to Break It <!-- role: exceptions -->

- **Scenario:** You explicitly want a “gist-only” animation where individual samples are not meant to be cognitively accessible.
- **Reason:** The paper tests fast playback as a limit case and finds attenuated gains; if gist is the only goal, you may accept that tradeoff [@kaleHypotheticalOutcomePlots2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Moderate speeds take longer to communicate uncertainty than very fast cycling.
- **The Risk:** If too slow, viewers may become impatient or stop attending before integrating enough samples (the paper flags attention/time as a design consideration) [@kaleHypotheticalOutcomePlots2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Maximizing frame rate to “show more samples quickly.”
- **Why it fails:** The paper’s results indicate that very fast presentation can weaken performance improvements relative to moderate-speed HOPs [@kaleHypotheticalOutcomePlots2019].

## How to Check <!-- role: check -->

- **Visual Sign:** The animation looks like flicker where individual outcomes cannot be apprehended.
- **The Test:** Ask a few users to describe a single sampled outcome they just saw; if they cannot, the speed may be beyond the useful range for this inference task [@kaleHypotheticalOutcomePlots2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Slow the HOP playback toward a moderate sample duration (the paper’s effective condition used 400 ms per sample) [@kaleHypotheticalOutcomePlots2019].
- **Best Fix:** Pilot multiple playback speeds with the target audience and choose the slowest speed that still maintains attention while preserving sensitivity improvements for ambiguous-trend judgments [@kaleHypotheticalOutcomePlots2019].
