---
id: use-bar-charts-for-cluster-counting-in-small-aggregated-categorical-data
title: Use bar charts for cluster counting tasks in small aggregated categorical data
bibliography: references.bib
description: For cluster tasks in small aggregated charts, bar charts provide the
  highest accuracy and highest user preference among basic visualization types.
labels:
- chart:bar
- task:cluster
- visual:length
- impact:accuracy
- data:categorical
- audience:general
- scale:small-n
---

## Use bar charts to count or identify clusters <!-- role: advice -->

Use a bar chart when the user’s task is to detect or count clusters (groups) in small aggregated categorical summaries.

## Cluster judgments benefit from discrete grouped magnitudes <!-- role: reason -->

When the task is to identify group structure, discrete, comparable magnitudes across categories can support grouping judgments.

**Mechanism:** Bars provide a repeated, aligned set of marks where differences across categories are easily scanned, supporting group counting or grouping judgments.

**Evidence:** For the cluster task, bar-chart designs ranked best on accuracy and ranked best on user preference among the tested basic visualization designs; pie-chart designs ranked best on time but not on accuracy or preference [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].

**Notes:** This guideline emphasizes accuracy and preference, not fastest time.

## Context: Cluster tasks on small aggregated charts <!-- role: context -->

- **User Goal:** Determine how many groups/clusters exist or recognize clustered group structure.
- **Task:** cluster.
- **Data:** Aggregated categorical groups with a limited number of marks (roughly 5–34).
- **Chart Setting:** Static 2D chart in a standard display.
- **Audience:** General readers or mixed visualization literacy.
- **Success Criterion:** Higher accuracy and stronger user preference.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** Completion time is the only dominant success criterion and small differences in speed matter more than preference/accuracy. **Why:** Pie designs ranked fastest for the cluster task in the evidence.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Bars can take more space than a compact part-to-whole display. **Risk:** If users interpret the task as part-to-whole comparison rather than clustering, they may apply the wrong mental model. **Mitigation:** Phrase prompts and annotations as “count groups” or “identify groups” rather than “compare proportions.”

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Using a line chart for cluster counting. **Why it fails:** Line-chart designs ranked lowest for accuracy and user preference for the cluster task in the study evidence.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Users disagree on the number of clusters or take unusually long to answer. **Quick Check:** Ask a user to answer a cluster-count question using your bar chart; if they instead describe trends, the chart-task fit is off. **Stronger Test:** Run a short A/B comparing bar vs line for cluster questions and check error rates.

## Fix: What to do instead <!-- role: fix -->

- Switch from line to bar when the question is about clusters/groups rather than trends.
- If you keep a pie for speed, validate that accuracy remains acceptable for your use case.
- Create separate views for clustering vs correlation to avoid forcing one chart type to serve both tasks.
