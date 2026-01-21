---
id: prefer-cool-warm-or-rainbow-over-viridis-for-gradient-comparison-jnd
title: Prefer Cool-Warm or Rainbow Over Viridis for Gradient-Comparison Sensitivity
bibliography: references.bib
description: For aggregate judgments of average gradient (steepness) in scalar fields,
  use cool-warm or rainbow rather than viridis to reduce JND thresholds.
labels:
- chart:map
- chart:heatmap
- task:aggregate
- task:compare
- visual:color
- visual:position
- impact:sensitivity
- data:quantitative
- audience:general
- metric:jnd
- encoding:colormap
---

## The Rule <!-- role: advice -->

When users must compare **average gradient/steepness** between two color-coded scalar fields, use a **cool-warm** or **rainbow** colormap instead of **viridis** to improve discrimination sensitivity (lower JND).

## The Logic <!-- role: reason -->

People can discriminate smaller differences in gradient magnitude (i.e., achieve lower JND thresholds) when the colormap supports more sensitive judgments for this aggregate task.

- **The Principle:** Lower JND implies higher perceptual sensitivity for discrimination in a forced-choice comparison task.
- **The Evidence:** In an aggregate (gradient comparison) task, **cool-warm (E-1)** and **rainbow (E-3)** both ranked better (lower JND) than **viridis (E-2)**, with significant differences for E-1 > E-2 and E-3 > E-2 [@redaEvaluatingGradientPerception2019]. This finding is collated as a task-and-metric-specific ranking in the graphical-perception knowledge base [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare which of two fields is **steeper on average** (aggregate gradient magnitude).
- **Data Type:** **2D quantitative scalar fields** shown as pixel-based maps (positionX/positionY + color encoding).
- **Audience:** General viewers performing quick comparative judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user is not doing an **aggregate gradient comparison** task (e.g., they need some other judgment not represented here).
- **Reason:** This guideline is only supported for the specific **aggregate/JND** outcome recorded; other tasks/metrics are not evidenced in the provided record [@zengReviewCollationGraphical2023; @redaEvaluatingGradientPerception2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up the option of using viridis even if it is preferred for non-covered goals (not evaluated in this evidence).
- **The Risk:** You may optimize for **JND in aggregate gradient comparison** while inadvertently harming other objectives that are not tested in this extracted result set [@zengReviewCollationGraphical2023; @redaEvaluatingGradientPerception2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing viridis by default for every continuous map, even when the user’s goal is comparing overall steepness.
- **Why it fails:** In the documented aggregate/JND comparison, viridis ranked worst (highest JND) relative to cool-warm and rainbow [@zengReviewCollationGraphical2023; @redaEvaluatingGradientPerception2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Users struggle to tell which of two side-by-side maps looks steeper unless differences are large.
- **The Test:** Run a quick A/B with representative users: can they reliably choose the steeper field when differences are subtle? If not, switch from viridis to cool-warm or rainbow and re-test for improved sensitivity (lower threshold) [@zengReviewCollationGraphical2023; @redaEvaluatingGradientPerception2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace viridis with **cool-warm** (or **rainbow**) for the same scalar-to-color mapping.
- **Best Fix:** If your system can adapt encodings by task, implement a task-aware rule: for **aggregate gradient comparison**, prioritize cool-warm or rainbow over viridis, consistent with the documented ranking [@zengReviewCollationGraphical2023; @redaEvaluatingGradientPerception2019].
