---
id: avoid-area-encodings-when-accuracy-matters
title: Avoid Area Encoding for Precise Quantitative Judgments
bibliography: references.bib
description: Do not rely on area encodings (especially rectangles/circles) when tasks
  demand accurate comparisons.
labels:
- visual:area
- task:compare
- impact:accuracy
- audience:novice
- source:borner-2019
---

## The Rule <!-- role: advice -->

Do not use area as the primary encoding for quantitative values when precise comparisons are required, especially with rectangular or circular areas.

## The Logic <!-- role: reason -->

The paper summarizes perception studies showing area judgments are less accurate than position and length, with rectangular/circular area encodings performing worst, making such charts harder to read.

- **The Principle:** Low perceptual accuracy of area judgments
- **The Evidence:** [@bornerDataVisualizationLiteracy2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify small differences, rank close values, or compare averages
- **Data Type:** Quantitative measures displayed as bubbles, treemap tiles, or other area marks
- **Audience:** Broad audiences; literacy assessments

## When to Break It <!-- role: exceptions -->

- **Scenario:** When the insight need is coarse (e.g., showing broad magnitude classes) rather than precise discrimination
- **Reason:** Reduced accuracy may be acceptable if precision is not the goal [@bornerDataVisualizationLiteracy2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose compactness or “at-a-glance” visual impact
- **The Risk:** Switching encodings may require a different chart family

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding labels to area marks while keeping area as the main comparison mechanism
- **Why it fails:** It forces serial reading of many labels, negating the intended visual comparison benefit [@bornerDataVisualizationLiteracy2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers argue about which bubble/tile is larger when values are close.
- **The Test:** If the chart’s main task is value comparison, verify the quantitative variable is not primarily encoded by area [@bornerDataVisualizationLiteracy2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remap the value to position or length while keeping other aesthetics similar.
- **Best Fix:** Replace the area-based visualization with a reference system that supports positional comparison for the key measure [@bornerDataVisualizationLiteracy2019].
