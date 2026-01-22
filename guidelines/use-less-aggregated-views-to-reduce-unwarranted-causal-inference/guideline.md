---
id: use-less-aggregated-views-to-reduce-unwarranted-causal-inference
title: Show less-aggregated data (more bins or individual values) when causality is
  not established
bibliography: references.bib
description: "Reducing aggregation in a chart lowers viewers\u2019 tendency to infer\
  \ causation from correlational patterns."
labels:
- chart:bar
- chart:line
- chart:scatter
- task:interpret
- visual:aggregation
- impact:trust
- data:correlational
- audience:novice
- custom:causality
---

## Reduce aggregation to avoid causal overreach <!-- role: advice -->

Show the relationship with less aggregation by using more bins or showing individual observations when you do not want viewers to infer causation from correlational data. Prefer designs that preserve within-group variability instead of collapsing data into a few summary groups.

## Why aggregation increases perceived causality <!-- role: reason -->

Aggregation can make a relationship look simpler and more deterministic, encouraging viewers to explain the pattern with a cause-and-effect story rather than treating it as an association. When variability is hidden, alternative explanations are less salient and the relation can feel more “law-like,” which supports causal interpretations.

**Mechanism:** Collapsing many observations into a few summary values reduces visible noise and makes trend structure easier to narrativize as X producing Y.

**Evidence:** Charts with higher aggregation (fewer bins) produced higher causation agreement ratings, with the most aggregated condition rated most causal and the least aggregated condition rated least causal. [@xiongIllusionCausalityVisualized2020]

**Notes:** This effect was observed even when the underlying relationship was the same and the task was simply judging agreement with causal statements.

## When to apply lower aggregation <!-- role: context -->

- **User Goal:** Avoid misleading viewers into believing an intervention on X will change Y.
- **Task:** Interpret whether a depicted relationship is merely correlational versus plausibly causal.
- **Data:** Observational data with correlation shown between two variables; no experimental or causal identification provided.
- **Chart Setting:** Static charts in reporting, dashboards, education materials, or media-style summaries.
- **Audience:** General audiences or mixed-statistical-literacy audiences.
- **Success Criterion:** Lower unwarranted causation ratings while still communicating that a correlation exists.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The communication goal is to emphasize a coarse group contrast (e.g., “high vs low”) rather than nuance. **Why:** More aggregation can intentionally foreground a simplified comparison and reduce attention to within-group variability.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Less aggregation can increase visual complexity and reduce fast comparability. **Risk:** Viewers may perceive the correlation itself as weaker when more variability is shown. **Mitigation:** Ensure the display remains readable and that viewers can still see the overall direction of association.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Converting continuous data into two groups and showing only group averages. **Why it fails:** Collapsing to two summaries can inflate causal impressions relative to less-aggregated depictions.
- **Mistake:** Treating added binning (e.g., 16-bin summaries) as equivalent to showing raw observations. **Why it fails:** Even moderate aggregation can still increase perceived causality compared to non-aggregated displays.

## Quick tests <!-- role: check -->

**Failure Sign:** Stakeholders interpret the chart as “doing X will make Y happen” even though the data are observational. **Quick Check:** Ask a reviewer to restate the takeaway; if they use intervention language (“if we increase X, Y will increase”), aggregation may be too high. **Stronger Test:** Run a small comprehension check where viewers rate agreement with a causal statement; compare a more-aggregated versus less-aggregated version.

## What to do instead <!-- role: fix -->

- Show more bins or more granular groupings rather than collapsing to two groups.
- Show individual observations (or a minimally summarized view) to preserve variability.
- Provide multiple views (a coarse summary plus a less-aggregated view) when both overview and nuance are needed.
- Replace a highly aggregated comparison chart with a depiction that makes dispersion visible for each level of X.
