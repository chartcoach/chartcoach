---
id: use-hops-for-ambiguous-trend-judgments
title: Use Hypothetical Outcome Plots for Ambiguous Trend Judgments
bibliography: references.bib
description: Prefer HOPs over static aggregate uncertainty charts when audiences must
  infer which underlying trend generated noisy time-series data.
labels:
- chart:uncertainty
- chart:animation
- task:infer
- task:compare
- visual:time
- impact:accuracy
- data:temporal
- audience:novice
- uncertainty:sampling
---

## The Rule <!-- role: advice -->

When users must decide which of two underlying trends most likely produced a noisy time series, show uncertainty with Hypothetical Outcome Plots (HOPs) rather than static aggregate uncertainty summaries.

## The Logic <!-- role: reason -->

HOPs present uncertainty as repeated draws (animated samples) from the generative distribution, letting viewers integrate uncertainty through experienced frequencies rather than interpreting statistical abstractions. In two experiments, participants required less evidence (lower JNDs) to correctly infer the underlying trend when using HOPs vs error bars and vs static line ensembles, indicating higher sensitivity to trend evidence under ambiguity [@kaleHypotheticalOutcomePlots2019].

- **The Principle:** Frequency/experience-based probability supports perceptual decision-making under noise.
- **The Evidence:** [@kaleHypotheticalOutcomePlots2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Choose which of two candidate models/trends (e.g., growth vs no growth) better explains an observed, noisy sample.
- **Data Type:** Time series with sampling error/noise where patterns are visually ambiguous.
- **Audience:** General public or untrained observers encountering uncertainty in news-like contexts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is primarily to read a single best estimate (central tendency) rather than reason about variability and model likelihood.
- **Reason:** The paper’s demonstrated advantage is for applied inference about ambiguous trends; it does not claim universal superiority for all reading/estimation tasks [@kaleHypotheticalOutcomePlots2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires animation and time-on-task to view multiple outcomes.
- **The Risk:** If viewers do not watch long enough or cannot attend across frames, benefits may diminish [@kaleHypotheticalOutcomePlots2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using error bars as the primary uncertainty aid for model-based judgments of noisy time series.
- **Why it fails:** Static summaries can be misinterpreted and do not provide the experiential sampling metaphor that improved sensitivity in the experiments [@kaleHypotheticalOutcomePlots2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers must mentally “translate” an abstract summary (e.g., error bars) into what repeated samples could look like.
- **The Test:** Ask users (informally) to explain what repeated samples would look like under each trend; if they struggle, the display is likely too abstract for the intended inference task [@kaleHypotheticalOutcomePlots2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace static aggregate uncertainty with an animated HOP showing repeated sampled outcomes under each candidate trend.
- **Best Fix:** Use HOPs alongside the decision task (as a decision aid) so users can compare observed samples to distributions of possible outcomes for each trend, as in the paper’s task setup [@kaleHypotheticalOutcomePlots2019].
