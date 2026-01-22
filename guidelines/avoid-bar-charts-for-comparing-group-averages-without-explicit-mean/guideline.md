---
id: avoid-bar-charts-for-comparing-group-averages-without-explicit-mean
title: Avoid using bar charts to compare group averages unless you explicitly show
  the mean
bibliography: references.bib
description: Bar charts can lead viewers to use summed bar area/length as a proxy
  for an average, reducing accuracy for average comparisons.
labels:
- chart:bar
- task:compare
- visual:position
- impact:accuracy
- data:categorical
- audience:general
- statistic:mean
---

## Prefer explicit mean marks for bar-chart average comparisons <!-- role: advice -->

Avoid relying on the bars alone when the task is to compare group averages; explicitly depict the mean for each group. Use a separate visual mark for the mean so the viewer can compare means directly.

## Why bar charts invite sum-based proxies in average judgments <!-- role: reason -->

When multiple bars represent a group, viewers can shift from reading each value via the bar top (position) to treating the whole set of bars as a single object and judging its total extent (summed length/area). That proxy is correlated with the average only when groups have the same number of items, so it produces low-precision or biased “average” judgments when set sizes differ.

**Mechanism:** Bar fills make each bar feel like an object, encouraging object-based attention and aggregation by total extent (area/length) instead of extracting and averaging bar-top positions.

**Evidence:** For single-value comparisons, normal bars behaved like position encodings (similar precision to dot plots and better than misaligned bars), but for multi-value average comparisons, normal bars behaved like extent encodings (similar precision to misaligned bars), consistent with reliance on summed extent rather than mean-of-positions [@yuanPerceptualProxiesExtracting2019]. Performance dropped substantially when comparing groups with unequal item counts, consistent with an extent/sum proxy that breaks when set sizes differ [@yuanPerceptualProxiesExtracting2019].

**Notes:** This guideline targets tasks where the reader must infer the mean from multiple plotted individual values rather than reading a single displayed summary.

## When this applies to your chart and task <!-- role: context -->

- **User Goal:** Decide which group has the higher average (mean).
- **Task:** Compare averages across groups represented by multiple individual values.
- **Data:** Grouped observations where each group may contain multiple data points; set sizes may be equal or unequal.
- **Chart Setting:** Static or interactive bar-based displays that plot each observation as a bar (including misaligned/stack-like forms).
- **Audience:** Any audience, including viewers familiar with bar charts.
- **Success Criterion:** Accurate, low-bias comparison of mean values across groups.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The bar height already encodes the mean as a single summary bar per group (not multiple bars per group). **Why:** The viewer is not required to extract an average from multiple bars, so the sum-proxy failure mode is not the dominant concern.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Adding explicit mean marks can add visual elements and reduce simplicity.\
**Risk:** If the mean mark is visually weak or ambiguous, viewers may still default to the overall bar mass/extent.\
**Mitigation:** Ensure the mean mark is clearly distinguishable as a summary statistic.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Showing many filled bars per group and expecting viewers to average bar tops. **Why it fails:** Viewers tend to use summed extent as a perceptual proxy, which is less precise and can become misleading when set sizes vary [@yuanPerceptualProxiesExtracting2019].
- **Mistake:** Comparing groups with different numbers of bars without any explicit cue that the task is “average per item.” **Why it fails:** Unequal set sizes make summed extent diverge from average, sharply reducing discrimination precision [@yuanPerceptualProxiesExtracting2019].

## Quick tests before you ship <!-- role: check -->

**Failure Sign:** Users’ judgments flip or become inconsistent when one group has more observations, even if its mean is lower.\
**Quick Check:** Duplicate a group’s observations (same mean, more items) and see whether the display visually suggests a higher “average.”\
**Stronger Test:** Run a small forced-choice pilot where participants pick the higher mean; compare error rates for equal vs unequal set sizes.

## What to do instead <!-- role: fix -->

- Add a distinct mean indicator per group (for example, a line/marker placed at the mean value on the shared axis).
- Replace multiple-bars-per-group with a dot-plot style encoding of individual values plus an explicit mean marker.
- If you must show multiple observations as bars, add an explicit textual mean label per group near the summary mark.
- Separate the task into two views: one for distribution/individual values and one dedicated to mean comparison.
