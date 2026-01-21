---
id: avoid-same-family-shapes-in-single-plot-numerosity-and-trend-tasks
title: Avoid Same Open/Closed Family Shapes When Judging Numerosity or Trend in One
  Plot
bibliography: references.bib
description: For numerosity and linear relationship judgments in a single scatterplot,
  do not pair symbols from the same open/closed family.
labels:
- chart:scatter
- task:count
- task:trend
- visual:shape
- impact:accuracy
- data:categorical
- audience:general
- source:paper
---

## The Rule <!-- role: advice -->

In a single scatterplot where users must judge **numerosity** or **linear trend** by class, ensure the two relevant classes use **different open/closed families**, not two open or two closed shapes.

## The Logic <!-- role: reason -->

When two symbol types share the same open/closed family, they create stronger perceptual interference during class-based ensemble judgments; reaction times increase (and errors can increase), especially in numerosity and trend judgments.

- **The Principle:** Feature-category interference in heterogeneous displays.
- **The Evidence:** In Experiment 3 single-plot displays, same-feature (same open/closed) distractors lengthened RTs for numerosity, and both target-feature and distractor-feature effects were strong for linear relationship judgments [@burlinsonOpenVsClosed2018a].

## Where to Apply <!-- role: context -->

- **User Goal:** “Which class has more points?” and “Which class shows a linear relationship?” within the same plot.
- **Data Type:** Two-class (or focal two-class) scatterplots with mixed symbols in one panel.
- **Audience:** Any audience doing fast visual inference rather than precise reading.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is not class-discriminative within one panel (e.g., users only need an overall trend regardless of class).
- **Reason:** The reported interference mechanism depends on having to attend to one symbol type while ignoring the other [@burlinsonOpenVsClosed2018a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Limits aesthetic flexibility; you may need to abandon a preferred symbol pair.
- **The Risk:** If many classes must be shown, you may still be forced into within-family choices for some class pairs.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using two closed shapes (e.g., circle vs. square) for “clean” appearance in a dense plot.
- **Why it fails:** Same-family pairings produced more interference than cross-family pairings in the paper’s numerosity and trend single-plot conditions [@burlinsonOpenVsClosed2018a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can see “there are many points,” but struggle to decide which symbol class is larger or which class forms the line.
- **The Test:** Replace one class symbol with an open/closed opposite (e.g., square → plus) and see if the judgment becomes noticeably faster/easier.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Change one of the two focal class symbols to the opposite open/closed family.
- **Best Fix:** Reserve cross-family symbol pairs specifically for tasks involving class-wise numerosity or trend judgments in mixed-symbol panels [@burlinsonOpenVsClosed2018a].
