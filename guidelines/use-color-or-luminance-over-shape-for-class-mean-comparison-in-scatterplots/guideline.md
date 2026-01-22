---
id: use-color-or-luminance-over-shape-for-class-mean-comparison-in-scatterplots
title: Use color encoding (hue or luminance) instead of shape to compare class means
  in multiclass scatterplots
bibliography: references.bib
description: For mean-comparison (aggregate) tasks in multiclass scatterplots, color-based
  class encodings yield higher accuracy than shape-based encodings.
labels:
- chart:scatter
- task:aggregate
- visual:color
- impact:accuracy
- data:categorical
- audience:general
- complexity:basic
---

## Prefer color (hue/lightness) over shape for class identification during mean comparisons <!-- role: advice -->

Use color encoding (hue or luminance/lightness) for class membership instead of shape when viewers must judge which class has the higher mean position in a scatterplot.

## Why color helps mean comparisons more than shape here <!-- role: reason -->

When classes are easier to visually separate, viewers can more reliably aggregate (mentally average) the positions belonging to each class and then compare those averages. More salient class cues reduce confusion between points from different classes during this aggregation.

**Mechanism:** Stronger class segmentation makes it easier to isolate each class’s points while estimating average position, improving correctness on aggregate judgments.

**Evidence:** In an accuracy-based aggregate task, scatterplots using color (hue or luminance) for class membership performed better than scatterplots using shape for class membership, with significant differences between the color-encoded designs (E-1…E-9) and the shape-encoded designs (E-10, E-11) [@gleicherPerceptionAverageValue2013; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about class encodings (color vs. shape) while position encodings carry the quantitative values.

## When this applies to your scatterplot design <!-- role: context -->

- **User Goal:** Choose which group/class has the higher average value (mean) in a scatterplot.
- **Task:** Aggregate (mean comparison across classes).
- **Data:** Two or more nominal classes (e.g., 2 classes; can extend to 3), with many points per class (e.g., ~50–75).
- **Chart Setting:** Static multiclass scatterplot using positionX and positionY for quantitative variables.
- **Audience:** General audiences doing visual comparison without special training.
- **Success Criterion:** Higher accuracy in mean-comparison judgments.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You cannot rely on color differences (e.g., monochrome-only rendering). **Why:** The rule assumes color is available as the class cue.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may consume the color channel, leaving fewer options for encoding additional variables. **Risk:** Overloading color for multiple purposes can make class identity ambiguous. **Mitigation:** Keep color dedicated to class membership if mean comparison is the primary task.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Encoding class with shape alone for mean-comparison tasks. **Why it fails:** Shape-based class separation is less accurate than color-based separation for this aggregate judgment.

## Quick checks before shipping <!-- role: check -->

**Failure Sign:** Viewers confuse which points belong to which class while trying to decide which class has the higher mean. **Quick Check:** Convert the class encoding from shape-only to color-only and see whether the answer becomes easier to judge at a glance. **Stronger Test:** Run a small accuracy check with representative users on a mean-comparison question set.

## What to do instead when this fails <!-- role: fix -->

- Use color hue (or luminance/lightness) as the primary class encoding.
- Reduce reliance on shape as the sole class cue by reserving shape for a different variable or not using it.
- If color cannot be used, simplify the comparison by reducing the number of classes shown at once.
