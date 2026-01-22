---
id: use-visually-symmetric-uncertainty-encodings-to-avoid-within-the-bar-bias
title: Use visually symmetric uncertainty encodings to prevent within-the-bar bias
bibliography: references.bib
description: Symmetric encodings around the mean remove a containment cue that makes
  outcomes inside the bar seem more likely.
labels:
- chart:bar
- chart:violin
- chart:gradient
- task:estimate
- task:infer
- visual:symmetry
- impact:accuracy
- data:uncertainty
- audience:novice
---

## Encode uncertainty symmetrically around the mean for likelihood judgments <!-- role: advice -->

When showing a mean with uncertainty, use an encoding that is visually symmetric around the mean so equal distances above and below the mean look equally plausible. Avoid filled shapes that occupy only one side of the mean.

## Why symmetry fixes a key bias in interpreting uncertainty <!-- role: reason -->

Inferential uncertainty around a mean is conceptually symmetric, but an asymmetric filled bar introduces a directional cue that changes perceived likelihood. Symmetry removes the “contained vs. not contained” interpretation and better matches the mental model that plausibility decreases as distance from the mean increases.

**Mechanism:** Symmetric shapes eliminate the visual containment region that makes viewers treat one side of the mean as privileged, aligning perceptual cues with the intended symmetric uncertainty.

**Evidence:** In a one-sample judgment task, bar charts produced an interaction where outcomes below the mean (inside the bar’s filled region) were judged more likely than outcomes above the mean, while symmetric encodings did not show this asymmetry [@correllErrorBarsConsidered2014]. Symmetric encodings also increased adherence to the expected “follow the sample mean” strategy compared to bars [@correllErrorBarsConsidered2014].

**Notes:** The bias affected not only perceived likelihood but could flip the direction of inference for some viewers.

## When symmetric uncertainty depiction matters most <!-- role: context -->

- **User Goal:** Judge how plausible a proposed outcome is given a mean and uncertainty.
- **Task:** Assess likelihood/surprise of an outcome relative to the mean.
- **Data:** A mean estimate with an uncertainty interval (for example, a t-confidence interval or margin of error).
- **Chart Setting:** A single-group display with a highlighted candidate outcome or threshold.
- **Audience:** General audiences or mixed expertise.
- **Success Criterion:** Outcomes equally distant from the mean are judged equally likely, independent of direction.

## When symmetry is not the primary concern <!-- role: exceptions -->

**Break it when:** The visualization is intentionally one-sided because the uncertainty is conceptually one-sided for the decision (for example, only exceedance risk is relevant). **Why:** Symmetric depiction may add irrelevant visual structure that does not match the one-sided inference goal [@correllErrorBarsConsidered2014].

## Tradeoffs of symmetric encodings <!-- role: costs -->

**Sacrifice:** Symmetric uncertainty displays can take more horizontal space than a thin error bar. **Risk:** Viewers unfamiliar with the shape may need guidance on what width/transparency means. **Mitigation:** Pair the encoding with a clear label such as “uncertainty around mean.”

## Common symmetry failures <!-- role: mistakes -->

**Mistake:** Using a bar chart and assuming that placing the mean line inside the bar makes interpretation symmetric. **Why it fails:** The filled area still creates a containment region on one side of the mean that shifts likelihood judgments [@correllErrorBarsConsidered2014].

## Quick checks for within-the-bar bias risk <!-- role: check -->

**Failure Sign:** The chart has a large filled region extending from a baseline up to the mean, with the mean not centered in the filled area. **Quick Check:** Visually test whether “distance above mean” and “distance below mean” look like they have equivalent visual status; if not, the display is asymmetric. **Stronger Test:** Ask viewers to rate the likelihood of two equidistant outcomes on opposite sides of the mean and compare responses.

## What to use instead of an asymmetric filled bar <!-- role: fix -->

- Use a gradient plot whose transparency decays symmetrically away from the mean.
- Use a violin plot centered on the mean to show decreasing plausibility with distance.
- Use a modified box plot centered on the mean if you need discrete regions while preserving symmetry.
