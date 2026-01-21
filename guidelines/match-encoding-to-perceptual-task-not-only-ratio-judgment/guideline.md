---
id: match-encoding-to-perceptual-task-not-only-ratio-judgment
title: Match Encodings to the Perceptual Task (Not Only Ratio Judgment)
bibliography: references.bib
description: Select visual encodings based on the specific perceptual operation users
  must perform, not only on two-value ratio precision.
labels:
- task:compare
- task:summarize
- task:detect
- visual:position
- visual:color
- impact:clarity
- audience:designer
- source:bertini-why-not-scatterplots
---

## The Rule <!-- role: advice -->

Choose chart types and encodings by the viewer’s perceptual task (e.g., trend, outlier, average, clustering), not by a single ranking derived from two-point ratio judgments.

## The Logic <!-- role: reason -->

The paper argues that the classic effectiveness ranking (where common-axis position wins) is grounded in a narrow operationalization of perceptual performance—two-value ratio judgments—and does not necessarily transfer to other perceptual tasks (e.g., “big picture,” ensemble/aggregate judgments, filtering, shape/trend) [@bertiniWhyShouldntAll2020].

- **The Principle:** Task-specific perceptual performance
- **The Evidence:** [@bertiniWhyShouldntAll2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Seeing the “big picture,” judging patterns across N points, summarizing, detecting outliers, judging trend/shape, filtering, or correlation-like judgments.
- **Data Type:** Dense matrices, multi-year/month grids, multi-series time series, and any view where users reason over many marks at once.
- **Audience:** Analysts and general viewers doing exploratory or summary reasoning.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is explicitly value lookup or precise pairwise comparison (retrieve values, compute ratio).
- **Reason:** The paper accepts that position on a common axis is highly effective for those specific tasks [@bertiniWhyShouldntAll2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may reduce the user’s ability to read exact values from individual marks.
- **The Risk:** If the actual task is misidentified, the chosen encoding can feel “wrong” or misleading [@bertiniWhyShouldntAll2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating “can people read the value?” as the only evaluation question.
- **Why it fails:** It ignores other perceptual operations the paper highlights (ensemble judgments, trend/shape comparisons, filtering) that can dominate real usage [@bertiniWhyShouldntAll2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Users ask for a different view because they “can’t see the pattern,” even though values are readable.
- **The Test:** List the intended perceptual operation (e.g., “compare averages across years”). If your chart primarily supports value retrieval instead, you likely mismatched task and encoding [@bertiniWhyShouldntAll2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace task wording like “read values” with a specific operation (trend, average, cluster, outlier) and reassess the design.
- **Best Fix:** Prototype multiple encodings for the same data and pick the one that best supports the target operation(s), as motivated by the paper’s Figure 2 discussion [@bertiniWhyShouldntAll2020].
