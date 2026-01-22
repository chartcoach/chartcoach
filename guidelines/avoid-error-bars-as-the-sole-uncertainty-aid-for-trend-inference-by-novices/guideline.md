---
id: avoid-error-bars-as-the-sole-uncertainty-aid-for-trend-inference-by-novices
title: Avoid Error Bars as the Sole Uncertainty Aid for Novice Trend Inference Under
  Sampling Variability
bibliography: references.bib
description: For choosing between candidate trends from noisy samples, error bars
  led to lower sensitivity than HOPs in the tested task.
labels:
- chart:bar
- task:classify
- visual:interval
- impact:accuracy
- data:temporal
- audience:novice
- uncertainty:sampling
---

## Do not rely on error bars alone when novices must infer which trend produced a noisy time series <!-- role: advice -->

Do not use bar charts with error bars as the only uncertainty display when untrained viewers must decide which of two trend models is more likely given a noisy sample. Use a sampling-oriented uncertainty depiction instead.

## Why error-bar aids underperform for this applied judgment task <!-- role: reason -->

The task requires mapping an observed noisy sample to the more plausible generating process, which depends on understanding variability from sampling error. Sampling-oriented depictions expose variability as outcomes, supporting perceptual inference; error bars summarize uncertainty into an abstract interval that is less effective for this decision.

**Mechanism:** Discrete sampled outcomes provide frequency-like evidence for “could this happen under this trend?”, whereas interval summaries provide weaker support for likelihood comparison in ambiguous cases.

**Evidence:** In the bar-chart trend task, HOPs yielded lower JNDs than error bars, meaning participants needed less evidence to achieve mean accuracy when HOPs were available as a decision aid [@kaleHypotheticalOutcomePlots2019].

**Notes:** The comparison was specific to a two-trend inference task with sampling error in monthly time series values [@kaleHypotheticalOutcomePlots2019].

## When your visualization is a decision aid for “growth vs no growth” style headlines <!-- role: context -->

- **User Goal:** Pick one of two competing interpretations of a noisy temporal sample.
- **Task:** Compare likelihood of an observed sample under two candidate trends with sampling variability.
- **Data:** Time series with per-timepoint uncertainty from sampling error.
- **Chart Setting:** A reference panel shows uncertainty for each trend; the viewer judges a single observed sample.
- **Audience:** General-public or statistically untrained viewers.
- **Success Criterion:** Correct inferences for more ambiguous samples (lower required evidence).

## When error bars may still be acceptable <!-- role: exceptions -->

**Break it when:** The audience is not doing model/trend inference and only needs a compact uncertainty summary for a point estimate. **Why:** The demonstrated advantage is tied to the specific trend-inference decision task rather than all uncertainty reading tasks [@kaleHypotheticalOutcomePlots2019].

## Tradeoffs of moving away from error bars <!-- role: costs -->

**Sacrifice:** Sampling-oriented displays can require more visual space or time (especially if animated). **Risk:** Without careful implementation, sampled outcomes can look cluttered or be ignored. **Mitigation:** Match the display choice to whether the task truly requires reasoning about the generating process.

## Common misuses of error bars in this setting <!-- role: mistakes -->

**Mistake:** Treating overlapping or non-overlapping error bars as sufficient evidence for a trend decision without showing sampling variability as outcomes. **Why it fails:** Participants were less sensitive to evidence with error bars than with HOPs for the same inference task [@kaleHypotheticalOutcomePlots2019].

## Checks that error bars are harming inference sensitivity <!-- role: check -->

**Failure Sign:** Users need very obvious differences in the observed series to choose the correct trend reliably. **Quick Check:** Compare performance on a small set of intentionally ambiguous samples with and without a sampling-oriented display. **Stronger Test:** Fit psychometric functions and confirm error bars lead to higher JNDs than a sampling-oriented alternative [@kaleHypotheticalOutcomePlots2019].

## What to use instead of error bars for this task <!-- role: fix -->

- Replace error bars with HOPs that animate sampled outcomes from each candidate trend.
- Use a line ensemble showing multiple sampled outcomes per trend when animation is not feasible.
- Change the encoding from bars to lines if you want to avoid bar-specific perceptual issues while keeping the same task structure.
- Present the uncertainty display as a reference alongside the observed sample so users can compare plausibility under each trend.
