---
id: use-indexing-line-plots-instead-of-juxtaposed-linear-for-overall-better-performance
title: Use indexed (percent-based) line plots instead of juxtaposed linear line plots
  when you want both faster and higher-ranked accuracy across tasks
bibliography: references.bib
description: Indexed (percent-based) line plots rank better than juxtaposed linear
  line plots on both time and accuracy across multiple task groupings.
labels:
- chart:line
- task:compare
- visual:position
- impact:overall-quality
- data:temporal
- audience:general
- transformation:indexing
---

## Prefer indexed line plots over juxtaposed linear line plots for overall comparison performance <!-- role: advice -->

Use indexed (percent-based) line plots instead of juxtaposed linear line plots when you need consistently strong performance across comparison tasks, not just for a single metric.

## Why indexing can improve overall task performance <!-- role: reason -->

A single shared comparison scale supports consistent judgments across different comparison subtasks by reducing the need to reconcile different scales or panels.

**Mechanism:** Consolidating comparisons into one normalized frame reduces cognitive overhead across multiple task types, improving end-to-end performance.

**Evidence:** In the extracted results, the indexed line-plot design ranked above the juxtaposed linear design for both overall accuracy and overall time, with a significant pairwise time difference reported (E-2 better than E-1). [@aignerBertinWasRight2011; @zengReviewCollationGraphical2023]

**Notes:** “Overall” here reflects the way results were aggregated in the extracted knowledge, not a guarantee for every possible time-series task.

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Perform multiple time-series comparisons efficiently and correctly.
- **Task:** Correlate; Aggregate; mixed comparison workflows.
- **Data:** Multivariate time-series where relative change comparisons matter.
- **Chart Setting:** Dashboards or reports where one view must support multiple comparison questions.
- **Audience:** General audiences doing repeated analytical comparisons.
- **Success Criterion:** Better combined performance across time and accuracy.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your workflow is dominated by reading original-unit values (e.g., exact prices) rather than relative change. **Why:** Indexing shifts the primary reading task from absolute magnitude to percent-based comparisons.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some interpretability of absolute levels is traded for comparability. **Risk:** Users may over-focus on relative change and miss absolute-level context. **Mitigation:** Pair the indexed view with a separate absolute-value view if absolute context matters.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Replacing the only absolute-value chart with an indexed chart without providing any absolute reference. **Why it fails:** Readers lose access to original-unit context that may still be required for decisions.

## Quick tests <!-- role: check -->

**Failure Sign:** Users switch between panels or use external calculation to compare series. **Quick Check:** Observe one user doing two different comparison questions; if they repeatedly cross-reference scales, indexing is likely beneficial. **Stronger Test:** Time a short task set on your current design vs. an indexed version and compare both completion time and error rate.

## What to do instead <!-- role: fix -->

- Use an indexed (percent-based) line plot as the primary comparison view for multivariate series.
- Provide an adjacent absolute-value line plot when absolute magnitude remains decision-relevant.
- If you must keep juxtaposition, add explicit cues that reduce cross-panel scale confusion (e.g., consistent axis labeling and clear scale communication).
