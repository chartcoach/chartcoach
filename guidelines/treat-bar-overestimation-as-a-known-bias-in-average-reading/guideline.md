---
id: treat-bar-overestimation-as-a-known-bias-in-average-reading
title: Assume Bar Averages Will Be Overestimated
bibliography: references.bib
description: Viewers tend to report average bar positions higher than the true average
  after brief viewing.
labels:
- chart:bar
- task:average
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- bias:overestimation
---

## The Rule <!-- role: advice -->

When designing around average-level judgments, assume a bar set’s average position will be perceived/recalled as higher than it truly is.

## The Logic <!-- role: reason -->

Across experiments, average position reports for bars showed systematic positive error (overestimation), and this held for both noisy and uniform bar sets, indicating a consistent directional bias rather than reliance on extreme bars.

- **The Principle:** Directional bias in remembered average position for bars
- **The Evidence:** Participants overestimated average bar position in single-bar conditions, with the effect persisting for uniform bars and in multi-series contexts [@xiongBiasedAveragePosition2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating/recalling the typical level (mean) of a distribution of bars after brief viewing.
- **Data Type:** Bar charts used as a series over x (many bars).
- **Audience:** General audiences; the bias appeared reliably in the paper’s experiments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users have direct numeric labels or explicit mean markers and are not estimating an average from memory.
- **Reason:** The paper evaluates memory-based/short-delay average position estimation, not labeled read-offs.

## The Price <!-- role: costs -->

- **The Sacrifice:** Accounting for this bias may require extra annotation or alternative presentation.
- **The Risk:** Added scaffolding can reduce simplicity.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming the bias comes from viewers focusing on the tallest bar and “fixing” it by reducing variability.
- **Why it fails:** Overestimation occurred even for uniform bar sets, and analyses suggest estimates were not simply based on the maximum bar [@xiongBiasedAveragePosition2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers’ indicated “average” for the bars lands above the true average position.
- **The Test:** Briefly show the bars, mask/blank, then ask users to place a bar/marker at the perceived average; compute signed error [@xiongBiasedAveragePosition2020a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Display an explicit average reference (e.g., a mean indicator) to reduce reliance on recalled averaging (motivated by the observed bias) [@xiongBiasedAveragePosition2020a].
- **Best Fix:** If precise average estimation is critical, avoid multi-series overlays that can further shift estimates via perceptual pull and validate with a quick user test [@xiongBiasedAveragePosition2020a].
