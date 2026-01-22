---
id: avoid-bar-charts-for-mean-estimation-when-bias-free-aggregate-is-required
title: Avoid bar charts when readers must estimate the overall mean accurately
bibliography: references.bib
description: Bar charts can systematically bias viewers to underestimate the overall
  mean during aggregate judgments.
labels:
- chart:bar
- task:aggregate
- visual:length
- impact:accuracy
- data:quantitative
- audience:general
- risk:bias
---

## Avoid bar charts for bias-free mean estimation <!-- role: advice -->

Avoid bar charts when the user’s task is to estimate the grand average (overall mean) and you need that estimate to be as bias-free as possible.

## Why bar charts bias mean estimation <!-- role: reason -->

Mean estimation from a set of bars can be systematically biased, leading viewers to perceive the overall mean as lower than it truly is even when the “correct mean” is shown as a reference.

**Mechanism:** Viewers’ perceptual estimate of the mean from multiple bars is systematically shifted downward, producing underestimation bias during aggregate judgments.

**Evidence:** In aggregate (mean-judgment) tasks, bar-based designs showed systematic underestimation bias across multiple bar conditions, while point-based designs did not show this same underestimation pattern in the reported tests [@godauPerceptionBarGraphs2016]. This bias finding is captured as actionable recommendation knowledge in a broader collation for visualization recommendation scenarios [@zengReviewCollationGraphical2023].

**Notes:** The underestimation persisted even when a numerical mean was shown alongside the bar chart.

## When this guideline applies <!-- role: context -->

- **User Goal:** Estimate the overall average of a set of values shown in a chart.
- **Task:** Aggregate (mean estimation).
- **Data:** Quantitative values across multiple categories/groups.
- **Chart Setting:** Static chart intended for quick interpretation (e.g., reports, dashboards, slides).
- **Audience:** General audiences (no assumption of specialized statistical training).
- **Success Criterion:** Minimize systematic bias in the viewer’s mean estimate.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The reader does not need to estimate the grand average from the marks (e.g., the goal is comparing individual categories rather than summarizing the overall mean). **Why:** The guideline targets bias in mean estimation specifically, not all bar-chart use.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose the familiarity and simplicity of bars for category-based displays. **Risk:** Avoiding bar charts may reduce readability for audiences expecting bars for category comparisons. **Mitigation:** Keep the same categorical x-axis structure while changing the mark type used to support mean estimation.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding a mean reference (line or numeric mean) to a bar chart and assuming that removes mean-estimation bias. **Why it fails:** Underestimation bias persisted even when a numerical mean was provided in the bar-chart condition.

## Quick tests <!-- role: check -->

**Failure Sign:** Users systematically judge that the correct mean “should be lower” when it is actually correct. **Quick Check:** Show a few representative charts and ask users to estimate whether a displayed mean reference is correct; look for consistent directional bias. **Stronger Test:** Run a small within-subject pilot comparing bar vs point presentations for the same data and measure directional error rates.

## What to do instead <!-- role: fix -->

- Use a point-based chart (point marks with position encodings) when the key requirement is bias-free estimation of the grand average.
- If you must keep bars for other reasons, avoid relying on viewers to visually estimate the grand mean from the bars and present the mean as an explicit value intended to be read rather than inferred.
- Reframe the display so the primary judgment is not “estimate the overall mean from the bars,” such as by changing the analytic prompt to focus on category comparisons instead of aggregation.
