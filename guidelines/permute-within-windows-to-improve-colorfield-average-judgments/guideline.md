---
id: permute-within-windows-to-improve-colorfield-average-judgments
title: Permute Values Within Windows to Improve Colorfield Average Judgments
bibliography: references.bib
description: If users compare window averages in a colorfield, shuffle values within
  each window to make perceptual averaging easier.
labels:
- chart:colorfield
- task:compare
- task:rank
- visual:color
- impact:accuracy
- data:temporal
- audience:general
- task:aggregate-judgment
- technique:within-bin-permutation
- source:correll-chi-2012
---

## The Rule <!-- role: advice -->

When using a colorfield to compare averages across predefined time windows, randomly permute (shuffle) the data values within each window block.

## The Logic <!-- role: reason -->

Shuffling within-window colors makes local regions more representative of the whole window, reducing the spatial extent over which the visual system must pool information to perceive an average. In the study, permuted colorfields produced higher accuracy than ordered colorfields, consistent with perceptual averaging predictions [@correllComparingAveragesTime2012a].

- **The Principle:** Local pooling supports more reliable perceptual averaging in colorfields.
- **The Evidence:** Significant interaction of display type × permutation (F(1,1921)=15.951, p\<.0001); within colorfields, permuted outperformed ordered (reported means: permuted µ=.914 vs ordered µ=.815) [@correllComparingAveragesTime2012a].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly select the window with the highest average when windows are known (e.g., months).
- **Data Type:** Time series binned into blocks with explicit boundaries, where within-block ordering is not itself analytically important for the task.
- **Audience:** Users doing rapid overview/summarization rather than pattern tracing within each window [@correllComparingAveragesTime2012a].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users need to see within-window temporal patterns (e.g., trends or sequences inside a month).
- **Reason:** Permutation destroys low-level temporal patterns by design; the paper treats it more as evidence for perceptual theory than as a generally practical design when within-bin structure matters [@correllComparingAveragesTime2012a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Loss of within-window temporal continuity and interpretability of local patterns.
- **The Risk:** Viewers may infer patterns from the shuffled texture that are not present in the true sequence, or miss meaningful within-window structure [@correllComparingAveragesTime2012a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Permuting the entire series globally or permuting across window boundaries.
- **Why it fails:** The study’s rationale depends on preserving known aggregation boundaries while making within-window pooling easier; crossing boundaries undermines the window comparison task [@correllComparingAveragesTime2012a].

## How to Check <!-- role: check -->

- **Visual Sign:** In an ordered colorfield, a window contains large contiguous streaks that require viewers to “mentally integrate” across the full width.
- **The Test:** Compare accuracy on hard stimuli (small difference between top months) with and without within-window permutation; the study found the improvement is especially visible on harder cases [@correllComparingAveragesTime2012a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Shuffle the pixel/mark order within each window block while keeping block boundaries fixed.
- **Best Fix:** Use a permuted (2D) within-window arrangement explicitly to optimize for average judgment, and clearly communicate that within-window order is intentionally not meaningful [@correllComparingAveragesTime2012a].
