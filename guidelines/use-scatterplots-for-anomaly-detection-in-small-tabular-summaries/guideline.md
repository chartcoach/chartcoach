---
id: use-scatterplots-for-anomaly-detection-in-small-tabular-summaries
title: Use scatterplots for anomaly detection in small aggregated tabular data
bibliography: references.bib
description: For anomaly-finding tasks in small aggregated datasets, scatterplots
  provide higher accuracy and are most preferred compared with other basic chart types.
labels:
- chart:scatter
- task:find-anomalies
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- scale:small-n
---

## Use scatterplots to spot anomalies <!-- role: advice -->

Use a scatterplot when the user’s task is to identify anomalous points or categories in a small aggregated dataset.

## Anomaly detection benefits from spatial outlier salience <!-- role: reason -->

Anomalies are often detected by noticing points that deviate from an expected spatial pattern, which position encodings can make salient.

**Mechanism:** Position-based displays can make unusual values stand out as spatially separated from the rest, supporting anomaly spotting.

**Evidence:** For the find-anomalies task, scatterplot designs ranked highest on accuracy and user preference among the tested basic visualization designs in a crowdsourced experiment on small (5–34 mark) aggregated charts [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].

**Notes:** The time ranking for find-anomalies differs from accuracy and preference; this guideline is about choosing for effectiveness (accuracy/preference) in anomaly spotting.

## Context: Anomaly finding on small aggregated charts <!-- role: context -->

- **User Goal:** Identify unusual data points/categories relative to an expectation.
- **Task:** find-anomalies.
- **Data:** Aggregated chart with limited marks (roughly 5–34), often involving quantitative values over categories or another quantitative axis.
- **Chart Setting:** Static 2D chart in a standard display.
- **Audience:** General readers or mixed visualization literacy.
- **Success Criterion:** Higher accuracy at spotting anomalies and better user preference.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The anomaly task is explicitly about aggregated totals or exact numeric sums rather than spotting a deviating point/category. **Why:** The evidence shows different top-ranked designs for aggregate tasks.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some viewers may find point-based charts less familiar than bars or tables. **Risk:** If anomalies are defined by exact thresholds, a scatterplot may not support precise threshold reading as directly as a table. **Mitigation:** Keep the task framed as anomaly identification rather than exact value retrieval.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Using a pie chart for anomaly finding. **Why it fails:** Pie designs ranked lowest for accuracy and user preference on find-anomalies in the study evidence.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Users miss the intended anomaly or disagree on which mark is anomalous. **Quick Check:** Ask a colleague to point to the “odd one” in a scatterplot vs a pie chart built from the same summarized data. **Stronger Test:** Time-box a small pilot with find-anomalies questions and compare error rates across chart options.

## Fix: What to do instead <!-- role: fix -->

- Replace pie charts with scatterplots for find-anomalies questions.
- If a scatterplot is not feasible, prioritize a position-based alternative over a pie chart for anomaly tasks.
- Split anomaly tasks into their own view rather than combining them with part-to-whole summaries.
