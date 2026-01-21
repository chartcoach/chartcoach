---
id: do-not-rely-on-bar-height-to-remove-mean-underestimation
title: Do Not Rely on Bar Height to Remove Mean Underestimation
bibliography: references.bib
description: Underestimation of the mean in bar graphs persists across high and low
  bar ranges in aggregate judgments.
labels:
- chart:bar
- task:aggregate
- visual:length
- impact:accuracy
- data:quantitative
- audience:general
- factor:bar-height
- effect:bias-underestimate
---

## The Rule <!-- role: advice -->

Do not assume that using “short” (low) bars vs “tall” (high) bars will eliminate mean-underestimation bias in bar charts.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Mean-estimation bias that is robust to bar-height range
- **The Evidence:** Mean underestimation was observed for both high-bar and low-bar versions in aggregate judgments, as collated in [@zengReviewCollationGraphical2023] from [@godauPerceptionBarGraphs2016].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Estimating the overall mean across bars (aggregate task)
- **Data Type:** Quantitative values shown as bar lengths across categories
- **Audience:** General viewers making fast impressions

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You are not asking viewers to estimate the grand mean (e.g., only comparing specific bars).
- **Reason:** The evidence here is about aggregate mean estimation bias, not other reading/comparison tasks [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** You cannot “tune” bar height range as a simple fix; you may need a different chart or annotation strategy.
- **The Risk:** Time spent tweaking scales/bar ranges won’t address the underlying bias mechanism observed in this task context [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Rescaling the y-axis or choosing a “more comfortable” bar height range to make the mean feel more accurate.
- **Why it fails:** Underestimation was observed in both high and low bar conditions for mean judgments [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].

## How to Check <!-- role: check -->

- **Visual Sign:** After rescaling, viewers still judge the shown mean reference as “too low” (i.e., they want it higher).
- **The Test:** Re-run the same quick mean-estimation prompt after changing the scale; if directional responses don’t change, the rescale didn’t solve the bias [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from bars to points for the same data values when mean estimation matters.
- **Best Fix:** Use a point chart (position-based marks) instead of bars for aggregate mean estimation scenarios, since the bar-height range is not a reliable lever to remove the bias [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].
