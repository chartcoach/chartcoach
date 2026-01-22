---
id: do-not-add-redundant-color-and-shape-encodings-for-class-mean-comparison
title: Do not add redundant color+shape encodings to improve class-mean comparison
  accuracy in multiclass scatterplots
bibliography: references.bib
description: Redundantly encoding class membership with both color and shape does
  not improve accuracy for mean-comparison tasks in multiclass scatterplots.
labels:
- chart:scatter
- task:aggregate
- visual:color
- visual:shape
- impact:accuracy
- data:categorical
- audience:general
- complexity:intermediate
---

## Avoid redundant class encoding (color plus shape) for mean comparison <!-- role: advice -->

Do not expect higher accuracy on class-mean comparisons by redundantly encoding class membership with both color and shape in a multiclass scatterplot.

## Why redundancy does not boost accuracy for this task <!-- role: reason -->

If viewers effectively use one cue to select a class’s points, adding a second, redundant cue may not increase how well they can compute the mean position for that class. In that case, redundancy adds visual complexity without improving the core aggregation step.

**Mechanism:** Mean comparison depends on isolating a class and averaging its positions; once one class cue is sufficient for selection, an additional redundant cue does not improve the underlying averaging judgment.

**Evidence:** In an accuracy-based aggregate task, a color-only scatterplot (E-1) outperformed a design with additional class complexity (E-8) with a significant difference reported for that comparison, and overall results report no general accuracy gain from adding redundant class encodings compared with color cues alone in this task setting [@gleicherPerceptionAverageValue2013; @zengReviewCollationGraphical2023].

**Notes:** This guideline is limited to accuracy for mean-comparison tasks and does not claim effects on other goals (e.g., memorability).

## When this applies to your scatterplot design <!-- role: context -->

- **User Goal:** Decide which class has the higher mean position/value.
- **Task:** Aggregate (mean comparison across classes).
- **Data:** Nominal classes (e.g., 2 classes), many points per class (e.g., ~50).
- **Chart Setting:** Static scatterplot where positionX and positionY encode quantitative variables, and class is encoded visually.
- **Audience:** General audiences.
- **Success Criterion:** Accuracy on the mean-comparison judgment.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your goal is redundancy for non-accuracy reasons (e.g., anticipating color-loss in printing). **Why:** The evidence here targets accuracy on mean-comparison, not robustness to display degradation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may give up a “belt-and-suspenders” feeling of safety from double-encoding. **Risk:** Removing redundancy can reduce resilience if one channel becomes unavailable. **Mitigation:** If robustness is required, treat redundancy as a compatibility requirement rather than an accuracy optimization.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding shape on top of color “to make it more accurate” for mean comparison. **Why it fails:** The redundant cue does not reliably translate into better mean-comparison accuracy for this task.

## Quick checks before shipping <!-- role: check -->

**Failure Sign:** The plot looks busier after adding redundant cues, but users’ answers do not become more consistently correct. **Quick Check:** Remove the redundant cue and see if the judgment is just as accurate for typical questions. **Stronger Test:** Compare accuracy on a small benchmark of mean-comparison questions with and without redundancy.

## What to do instead when this fails <!-- role: fix -->

- Keep a single, clear class cue (preferably color) for the mean-comparison task.
- Use the freed-up channel (e.g., shape) to encode a different variable only if it does not interfere with the mean judgment.
- If robustness is the real requirement, provide a mode switch (color version vs. pattern/shape version) instead of always combining both.
