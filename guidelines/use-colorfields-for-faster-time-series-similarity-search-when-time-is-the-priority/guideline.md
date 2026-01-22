---
id: use-colorfields-for-faster-time-series-similarity-search-when-time-is-the-priority
title: Use colorfields instead of line charts or horizon graphs to reduce time in
  time-series similarity selection
bibliography: references.bib
description: When people must pick the most similar time series among candidates,
  colorfields can reduce completion time compared to line charts and horizon graphs.
labels:
- chart:heatmap
- chart:line
- task:cluster
- task:compare
- visual:color
- visual:position
- impact:speed
- data:temporal
- audience:novice
- complexity:intermediate
---

## Prefer colorfields for speed in time-series similarity selection <!-- role: advice -->

Use colorfields (value encoded by color over time) instead of line charts or horizon graphs when your primary goal is faster time-series similarity judgments.

## Why colorfields can be faster for similarity judgments <!-- role: reason -->

Encoding values as color across time can enable quick, coarse pattern matching without tracing precise vertical positions, which can reduce decision time in similarity selection tasks.

**Mechanism:** Color-based pattern matching supports rapid scanning for regions of similar hue sequences, reducing the need for detailed shape-following and point-by-point alignment.

**Evidence:** In a time-series similarity-selection task, colorfields had significantly lower completion time than both line charts and horizon graphs (bootstrap comparisons; colorfields ranked fastest) [@gogolouComparingSimilarityPerception2019; @zengReviewCollationGraphical2023].

**Notes:** This guidance is about speed (time), not about which similarity invariances the visualization emphasizes.

## When this applies to your visualization setting <!-- role: context -->

- **User Goal:** Quickly select the most similar time series from a small set of candidates.
- **Task:** Similarity-based selection (recorded under a clustering-related task category).
- **Data:** Temporal quantitative sequences displayed as small multiples; time is ordered.
- **Chart Setting:** Static views where multiple candidate series are shown simultaneously.
- **Audience:** General audience or mixed-experience analysts.
- **Success Criterion:** Faster completion time for the similarity selection.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The decision requires careful discrimination of time-warping differences or precise shape matching beyond coarse pattern cues. **Why:** Faster scanning may come with more reliance on broad color regions rather than detailed temporal alignment.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Colorfields may reduce access to exact values and fine-grained shape details compared to position-based traces. **Risk:** Viewers may overweight broad color patches and underweight subtle timing differences. **Mitigation:** Treat speed gains as situational and validate with a small pilot if decision quality matters.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using colorfields for similarity selection and assuming they support the same notion of similarity as position-based charts. **Why it fails:** Similarity judgments can shift with the encoding, so the fastest view may not align with the intended similarity criterion.

## Quick tests <!-- role: check -->

**Failure Sign:** Users hesitate or repeatedly re-check candidates because the color patterns feel ambiguous.\
**Quick Check:** Time a few representative comparisons; if users complete choices faster with colorfields while still feeling confident, the condition likely holds.\
**Stronger Test:** Run a small within-subject comparison of completion times across candidate encodings on your own data.

## What to do instead <!-- role: fix -->

- Use a line chart when users must follow detailed waveform shape and timing precisely.
- Use a horizon graph when you want to preserve some shape cues while compacting vertical space, accepting slower judgments.
- Provide both a colorfield and a line-chart view if users need both fast triage and detailed verification.
