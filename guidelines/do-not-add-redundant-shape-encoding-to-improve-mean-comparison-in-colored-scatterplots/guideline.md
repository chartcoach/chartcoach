---
id: do-not-add-redundant-shape-encoding-to-improve-mean-comparison-in-colored-scatterplots
title: Avoid Redundant Shape Encoding When Color Already Encodes Class
bibliography: references.bib
description: Adding shape redundantly to a color-encoded multiclass scatterplot does
  not improve mean-comparison accuracy.
labels:
- chart:scatter
- task:aggregate
- visual:color
- visual:shape
- impact:accuracy
- data:categorical
- data:quantitative
- audience:general
- custom:redundant-encoding
- source:collated
---

## The Rule <!-- role: advice -->

If class membership is already encoded with color hue for mean-comparison in a multiclass scatterplot, do not add shape as a redundant second encoding to “boost accuracy.”

## The Logic <!-- role: reason -->

Redundant encoding does not translate into better performance for this specific aggregate judgement.

- **The Principle:** Adding a second, redundant cue does not necessarily improve selective attention or aggregation accuracy.
- **The Evidence:** The color+hue+shape design (E-5) was grouped as performing about the same as color-hue designs without redundant shape (E-1–E-4, E-6–E-9) in the aggregate accuracy ranking [@gleicherPerceptionAverageValue2013]. This finding is captured in the structured comparison dataset used for recommendation-oriented rules [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which class has the higher mean position (aggregate comparison).
- **Data Type:** Scatterplot with two quantitative axes and a nominal class variable.
- **Audience:** General users performing aggregate comparisons without time pressure (as in the study setup).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need shape for a different semantic reason (e.g., to encode a separate variable), and you accept that it may not improve mean-comparison accuracy.
- **Reason:** The evidence only supports “no accuracy gain” from redundancy for this task; it does not say shape must never be used for other goals [@gleicherPerceptionAverageValue2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up an opportunity to add a second cue that some stakeholders may expect (e.g., “use both color and shape”).
- **The Risk:** Overcomplicating the legend/encoding scheme without improving the target task performance.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding shapes to each color group “for accessibility” without checking whether it helps the targeted task.
- **Why it fails:** In the recorded aggregate task comparisons, redundant shape did not outperform color alone (it was not separated as better in the rank grouping) [@gleicherPerceptionAverageValue2013; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The plot looks busier (more symbol variation) but users are not more accurate at deciding which group’s average is higher.
- **The Test:** A/B test: remove redundant shape while keeping colors; if accuracy is unchanged for the mean-comparison question, the redundancy is not helping (consistent with the study’s ranking) [@gleicherPerceptionAverageValue2013].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove the redundant shape encoding and keep color hue for class.
- **Best Fix:** Reallocate shape to encode another variable only if that variable is needed; otherwise keep a single, clear class cue (color hue) for the mean-comparison task [@gleicherPerceptionAverageValue2013; @zengReviewCollationGraphical2023].
