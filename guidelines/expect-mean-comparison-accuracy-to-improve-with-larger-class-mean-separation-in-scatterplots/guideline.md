---
id: expect-mean-comparison-accuracy-to-improve-with-larger-class-mean-separation-in-scatterplots
title: Increase class mean separation to improve accuracy of class-mean comparisons
  in multiclass scatterplots
bibliography: references.bib
description: Larger differences between class means make mean-comparison judgments
  more accurate in multiclass scatterplots.
labels:
- chart:scatter
- task:aggregate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- complexity:basic
---

## Increase separation between class means for more accurate mean comparisons <!-- role: advice -->

Increase the difference between classes’ average positions (mean separation) when you want viewers to accurately judge which class has the higher mean in a multiclass scatterplot.

## Why larger mean separation improves performance <!-- role: reason -->

When class means are closer together, viewers must estimate two averages with higher precision and compare them, which increases the chance of error. Greater separation lowers the precision burden and makes the comparison more reliable.

**Mechanism:** Larger between-class distance reduces perceptual ambiguity in locating and comparing the average position of each class.

**Evidence:** In an accuracy-based aggregate task, performance improved as the difference between class means (task difficulty parameterized as the distance between class centers) increased [@gleicherPerceptionAverageValue2013; @zengReviewCollationGraphical2023].

**Notes:** This concerns the underlying data configuration (or how it is sampled/filtered), not a specific styling change.

## When this applies to your scatterplot design <!-- role: context -->

- **User Goal:** Decide which class has the higher mean value/position.
- **Task:** Aggregate (mean comparison).
- **Data:** Two or more classes whose mean positions may be close.
- **Chart Setting:** Multiclass scatterplot using position for quantitative values.
- **Audience:** General audiences.
- **Success Criterion:** Higher accuracy on mean-comparison questions.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You must show the full data distribution even when means are close. **Why:** You cannot increase mean separation without changing what data is shown.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may need to filter, subset, or otherwise change the displayed data to increase separation. **Risk:** Making means look more separated than they are can mislead if achieved by selective inclusion. **Mitigation:** If you change the shown subset, disclose the filtering or sampling explicitly.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Expecting high accuracy on mean comparisons when class means are nearly identical. **Why it fails:** The comparison requires finer perceptual discrimination than the display supports for many viewers.

## Quick checks before shipping <!-- role: check -->

**Failure Sign:** Many viewers disagree on which class has the higher mean for the same chart. **Quick Check:** Ask a colleague to answer “which class is higher on average?” without measuring—if they hesitate, separation is likely too small. **Stronger Test:** Create a small set of trials with varying separations and verify that accuracy rises with separation.

## What to do instead when this fails <!-- role: fix -->

- Reduce the number of classes shown so the key comparison is clearer.
- Add a secondary view or summary that supports the mean comparison without requiring extremely fine discrimination.
- Reframe the task away from mean comparison if means are inherently very close and must remain so in the display.
