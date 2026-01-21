---
id: use-color-to-encode-classes-for-mean-comparison-in-multiclass-scatterplots
title: Encode Classes with Color Hue for Mean Comparison
bibliography: references.bib
description: For mean-comparison aggregation in multiclass scatterplots, use color
  hue rather than shape to encode class membership.
labels:
- chart:scatter
- task:aggregate
- visual:color
- visual:shape
- impact:accuracy
- data:quantitative
- data:categorical
- audience:general
- source:collated
---

## The Rule <!-- role: advice -->

Encode class membership with color hue (not shape) when users need to compare average (mean) position across classes in a scatterplot.

## The Logic <!-- role: reason -->

Using a stronger, more salient class cue improves mean-comparison accuracy for this aggregation task.

- **The Principle:** Salient feature-based selection improves extracting aggregates from a selected subset.
- **The Evidence:** In the collated results, all color-hue–encoded designs (E-1–E-9) were significantly more accurate than shape-only designs (E-10–E-11) for the aggregate task [@gleicherPerceptionAverageValue2013], as recorded and operationalized for recommendation contexts by the collation schema [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Pick which class has the higher mean/average value (comparative average judgement).
- **Data Type:** Two quantitative axes (PX, PY) with a nominal class variable (color groups).
- **Audience:** Any audience where accuracy of the class-mean comparison matters.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot use color hue to distinguish classes (e.g., color is unavailable in the medium/workflow).
- **Reason:** This rule requires color hue as the primary class cue; without it, you must rely on other channels that were less accurate in this evidence set [@gleicherPerceptionAverageValue2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Uses up the color-hue channel, leaving fewer options to encode additional categorical variables.
- **The Risk:** If too many classes must be encoded via hue, classes may become harder to distinguish (not evaluated in this extracted result set).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding classes primarily with shape while keeping color hue unused.
- **Why it fails:** Shape-only class encoding was significantly less accurate than color-hue encoding for this aggregate mean-comparison task in the recorded comparisons [@gleicherPerceptionAverageValue2013; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers hesitate or misidentify which colored group is “higher on average,” especially when many points overlap.
- **The Test:** Produce a shape-only version of the same plot; if it becomes noticeably harder to answer “which group’s mean is higher?” you are depending on a weak class cue.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the class encoding from shape to color hue.
- **Best Fix:** Use color hue as the primary class encoding and keep shape for something else (or omit it) so the grouping remains driven by hue [@gleicherPerceptionAverageValue2013; @zengReviewCollationGraphical2023].
