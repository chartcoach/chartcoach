---
id: prefer-closed-shapes-for-target-classes-in-single-plot-trend-judgments
title: Prefer closed shapes for target classes in single-plot trend judgments
bibliography: references.bib
description: Closed target shapes are processed faster than open targets for single-plot
  linear relationship judgments, especially when distractors differ in open/closed
  category.
labels:
- chart:scatter
- task:correlate
- visual:shape
- impact:speed
- data:categorical
- audience:general
- targeting:closed-shape
---

## Use closed shapes for the class viewers must track (single-plot trend) <!-- role: advice -->

When a single scatterplot contains multiple symbol classes and the viewer must identify which class shows the linear relationship, assign the “target” class to a closed shape rather than an open shape.

## Closed targets reduce time to isolate the trend class <!-- role: reason -->

Closed shapes can be processed faster than open shapes as targets in heterogeneous symbol displays, improving the speed of identifying the class that carries the trend signal.

**Mechanism:** A closed target symbol strengthens attentional selection and reduces the time needed to isolate the relevant class from distractors.

**Evidence:** In single-plot scatterplot tasks for linear relationship (trend) judgment, closed targets yielded quicker reaction times than open targets, and performance depended on the target/distractor open/closed pairing [@burlinsonOpenVsClosed2018]. This finding is included as structured, reusable evidence for visualization recommendation decisions in a broader graphical-perception collation effort [@zengReviewCollationGraphical2023].

**Notes:** The advantage is reported for the single-plot setting where the viewer must discriminate between symbol classes inside one plot.

## When closed targets are the right choice <!-- role: context -->

- **User Goal:** Identify which category forms a linear relationship in a scatterplot.
- **Task:** Correlate (trend judgment) within a multiclass point plot.
- **Data:** Nominal categories encoded by shape; two symbol sets co-present; trend present in one subset.
- **Chart Setting:** One plot with both target and distractor symbols present together.
- **Audience:** Readers doing fast screening or decision-making from the plot.
- **Success Criterion:** Reduced time to correctly identify the trend-carrying class.

## When to avoid prioritizing closed targets <!-- role: exceptions -->

**Break it when:** Categories are shown in separate homogeneous plots (side-by-side) rather than mixed within a single plot. **Why:** Target open vs. closed did not show a significant effect on response time in the separate-plot baseline setting.

## Tradeoffs of choosing closed targets <!-- role: costs -->

**Sacrifice:** You constrain the symbol vocabulary for the focal class. **Risk:** If many other categories also need closed shapes, within-category closed-shape interference can still occur. **Mitigation:** Keep the number of concurrently displayed closed-shape categories small when the task requires isolating one target class.

## Common mistakes with “closed target” usage <!-- role: mistakes -->

**Mistake:** Making the trend-carrying class an open shape while other classes use closed shapes in the same plot. **Why it fails:** Open targets are slower to process than closed targets for the single-plot linear relationship judgment task.

## Quick checks for whether closed targets are helping <!-- role: check -->

**Failure Sign:** People repeatedly identify the wrong symbol class as the one forming the linear relationship. **Quick Check:** Ask a colleague to answer “which symbol class shows the linear relationship?”; if they need to re-check the legend multiple times, the target symbol may be too slow/confusable. **Stronger Test:** Time a small within-team trial with the same plot using an open vs a closed target symbol and compare completion time.

## What to do instead if closed targets are not feasible <!-- role: fix -->

- Move the target class to a separate panel so the trend judgment does not require within-plot symbol discrimination.
- Reduce simultaneous categories so the target class can be isolated with fewer competing symbol types.
- Change the task presentation so the viewer does not need to select the target symbol class from distractors inside one plot.
- Re-assign which class is treated as the “target” in the task flow so the most important class can take the closed symbol slot.
