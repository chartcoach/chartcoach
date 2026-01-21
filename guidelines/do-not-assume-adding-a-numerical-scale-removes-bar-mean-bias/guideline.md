---
id: do-not-assume-adding-a-numerical-scale-removes-bar-mean-bias
title: Do Not Assume a Numerical Scale Removes Mean Bias in Bar Charts
bibliography: references.bib
description: Mean underestimation in bar graphs can persist even when a numeric scale
  is present during aggregate judgments.
labels:
- chart:bar
- task:aggregate
- visual:length
- impact:accuracy
- data:quantitative
- audience:general
- design:axis-scale
- effect:bias-underestimate
---

## The Rule <!-- role: advice -->

Do not rely on adding a numerical scale to a bar chart as a fix for mean-estimation bias.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Persistent mean-underestimation bias despite numeric reference
- **The Evidence:** Underestimation of the mean in bar graphs was still observed in a condition with a numerical scale/presentation during an aggregate judgment task; this is collated by [@zengReviewCollationGraphical2023] based on [@godauPerceptionBarGraphs2016].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Estimating the grand mean across displayed values (aggregate task)
- **Data Type:** Quantitative values displayed as bar lengths
- **Audience:** General viewers (including fast/low-effort readers)

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** The audience is not being asked to infer a mean from the visual display (e.g., they only need exact labeled values per category).
- **Reason:** The evidence summarized here is about perceptual mean estimation from the chart, not value lookup tasks [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** You may need to change chart type rather than just “decorate” the bar chart with more reference information.
- **The Risk:** Adding axes/scales can increase clutter while failing to address the bias observed for mean estimation [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** “Just add a y-axis scale (or numeric mean) and the bar chart will be interpreted correctly.”
- **Why it fails:** The underestimation effect persisted even with numeric reference/scaling in the summarized results [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers still say the true mean “should be higher” even when the chart is clearly scaled.
- **The Test:** Ask users to judge whether a displayed mean reference is too high/low; persistent directional bias indicates the numeric scale isn’t resolving the perceptual issue [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Present the same values with point marks instead of bars when mean estimation is required.
- **Best Fix:** Use a point-based chart for the values so mean estimation relies on point position rather than bar length, aligning with the paper’s observed difference between bar and point displays in mean judgments [@zengReviewCollationGraphical2023; @godauPerceptionBarGraphs2016].
