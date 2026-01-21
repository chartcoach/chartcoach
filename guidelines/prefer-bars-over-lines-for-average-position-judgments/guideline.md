---
id: prefer-bars-over-lines-for-average-position-judgments
title: Use Bars Instead of Lines for Average Position Judgments
bibliography: references.bib
description: Bars yield less biased and more precise average-position estimates than
  lines in short-delay averaging tasks.
labels:
- chart:bar
- chart:line
- task:average
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- bias:under-over-estimation
---

## The Rule <!-- role: advice -->

Use bars rather than lines when you expect viewers to estimate an average height/level from a graph after a brief look.

## The Logic <!-- role: reason -->

People’s remembered/estimated average positions are systematically biased: average line positions are underestimated while average bar positions are overestimated, and bar judgments were also more precise than line judgments in this paradigm.

- **The Principle:** Systematic bias in positional averaging (even for “precise” position encodings)
- **The Evidence:** Across experiments, average line position estimates were biased downward and average bar position estimates biased upward, with bars showing smaller biases and tighter (less variable) estimates than lines in the reported comparisons [@xiongBiasedAveragePosition2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating the typical/overall level (average) of a series from a quick glance (especially with a short delay before responding).
- **Data Type:** Quantitative values where “average position” is a meaningful summary (e.g., a series distributed across x).
- **Audience:** General audiences and non-expert viewers (and any context where quick perceptual averaging is likely).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not asking viewers to judge an average position (e.g., you need to emphasize shape, continuity, or local fluctuations rather than average level).
- **Reason:** This guideline is specifically about average position estimation bias; the paper does not test other tasks.

## The Price <!-- role: costs -->

- **The Sacrifice:** Bars can reduce perceived continuity compared to a line.
- **The Risk:** Switching to bars may change what patterns viewers focus on (e.g., less emphasis on trend smoothness).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming “position is most accurate” means average judgments from lines will be unbiased.
- **Why it fails:** The paper shows systematic under/overestimation can occur even with position encodings, specifically in average judgments after a brief delay [@xiongBiasedAveragePosition2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers’ reported “average level” of a line tends to come out lower than the true mean; for bars it tends to come out higher.
- **The Test:** Run a quick internal study: show the chart for ~500ms, mask/blank it, then ask viewers to place a horizontal probe at the perceived average; compare to the true mean [@xiongBiasedAveragePosition2020a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** If you must keep a line, add an explicit average reference (e.g., a marked mean line) so the task is less dependent on remembered averaging (the paper motivates this need via bias, though it does not test specific interventions) [@xiongBiasedAveragePosition2020a].
- **Best Fix:** Change the encoding to bars when the core task is “estimate the average level” [@xiongBiasedAveragePosition2020a].
