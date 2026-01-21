---
id: avoid-filled-bars-for-mean-comparisons-with-unequal-group-sizes
title: Avoid Filled Bar Sets for Mean Comparisons When Group Sizes Differ
bibliography: references.bib
description: Filled bar groups strongly bias viewers toward summed area/length, harming
  average comparisons when groups contain different numbers of items.
labels:
- chart:bar
- task:compare
- visual:area
- impact:bias-reduction
- data:categorical
- audience:general
- statistic:mean
- risk:unequal-n
- source:paper-yuan-haroz-franconeri
---

## The Rule <!-- role: advice -->

Do not use filled multi-bar displays to ask viewers to compare group averages when the groups have unequal numbers of items.

## The Logic <!-- role: reason -->

In multivalue comparisons, viewers tend to treat a set of bars as a single object and use summed spatial extent (area/length) as a proxy for “average.” When group sizes differ, summed area becomes a misleading cue, and performance drops sharply; the paper shows worse discrimination (higher JND) for unequal set sizes (e.g., 6vs10) compared to equal set sizes across bar-based encodings.

- **The Principle:** Summed-extent proxy interferes with mean judgments, especially under unequal numerosity
- **The Evidence:** [@yuanPerceptualProxiesExtracting2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare which group’s mean is larger from multiple observations
- **Data Type:** Grouped observations where sample sizes can differ (e.g., 6 points vs 10 points)
- **Audience:** Dashboards/reports where users visually “eyeball” averages

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your intent is to communicate workload/total output (sum) and group size is meaningful
- **Reason:** In that case, the summed-area cue is aligned with the message, so the “bias” becomes a feature [@yuanPerceptualProxiesExtracting2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to change the visual form (e.g., away from bars) or add explicit summary marks
- **The Risk:** Users accustomed to bars may initially resist the alternative format

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping filled bars and assuming viewers will “divide by the count” mentally
- **Why it fails:** The study’s results indicate people often rely on primitive extent proxies rather than computed averages, producing large errors when counts differ [@yuanPerceptualProxiesExtracting2019].

## How to Check <!-- role: check -->

- **Visual Sign:** The group with more observations “looks larger” and is frequently chosen as having the higher mean
- **The Test:** Hold the true means constant and vary only the number of bars; if perceived “average” changes, viewers are being pulled by summed extent/numerosity [@yuanPerceptualProxiesExtracting2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to dot plots so values are carried by position rather than filled extent
- **Best Fix:** Redesign the view so the mean is not inferred from the total filled shape; use a position-only encoding for the underlying observations when unequal group sizes are possible [@yuanPerceptualProxiesExtracting2019].
