---
id: avoid-bar-charts-for-mean-estimation
title: Avoid Bar Charts for Estimating the Mean
bibliography: references.bib
description: Bar charts can systematically bias viewers toward underestimating the
  grand mean when performing aggregate judgments.
labels:
- chart:bar
- task:aggregate
- visual:length
- impact:accuracy
- data:quantitative
- audience:general
- effect:bias-underestimate
---

## The Rule <!-- role: advice -->

Avoid bar charts when your audience must estimate the overall mean (grand average) of a set of values.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Systematic bias in perceived central tendency from bar marks
- **The Evidence:** Bar graphs led to systematic underestimation of the mean in an aggregate judgment task; the finding is collated for visualization recommendation contexts in [@zengReviewCollationGraphical2023] and originates from [@godauPerceptionBarGraphs2016].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Estimating the grand mean / central tendency across multiple values (aggregate task)
- **Data Type:** Quantitative values across categories (shown as bars)
- **Audience:** General viewers making quick judgments

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** The task is not mean estimation (e.g., focusing on individual category values rather than the grand average).
- **Reason:** The evidence summarized here concerns aggregate mean estimation bias specifically, not other tasks [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** You may lose the familiar “standard” presentation many stakeholders expect for category comparisons.
- **The Risk:** Switching away from bars may make the chart feel less conventional for categorical comparisons, even if it reduces mean-estimation bias [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Keeping the bar chart and assuming viewers will still accurately infer the mean from the bar heights.
- **Why it fails:** The evidence indicates the mean inferred from bars can be systematically underestimated during aggregate judgments [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers’ estimated “average level” seems consistently lower than the true average when discussing the chart.
- **The Test:** Ask a few people (unprimed) to state whether a shown mean reference should be higher/lower; compare their direction to the correct mean—systematic “should be higher” responses indicate underestimation bias risk [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the bar display with a point-based display for the same values.
- **Best Fix:** Use a point chart instead of bars when mean estimation is central to the task, since bar charts are associated with underestimation bias for the mean in this context [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].
