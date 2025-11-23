---
id: prefer-aligned-over-stacked
title: Prefer Aligned Bars Over Stacked Bars
bibliography: references.bib
description: Stacked bars introduce distractor elements and unaligned baselines that
  degrade comparison accuracy.
labels:
- chart:stacked-bar
- chart:bar
- task:compare
- visual:position
- impact:clarity
---

## The Rule <!-- role: advice -->
Use aligned bar charts (side-by-side or small multiples) instead of stacked bar charts when the user needs to compare the values of individual segments.

## The Logic <!-- role: reason -->
Stacked bar charts force users to compare lengths without a common baseline (unaligned). This is fundamentally harder than comparing positions on an aligned scale. Furthermore, the "distractor" bars (the other segments in the stack) interfere with length estimation by changing visually salient bar corners into less salient T-junctions.
*   **The Principle:** Alignment vs. Length Perception / Visual Interference
*   **The Evidence:** Talbot et al. confirmed that unaligned comparisons in stacked charts are significantly harder than aligned comparisons [@talbot_four_2014]. Their experiments showed that "distractors" (the surrounding stack segments) substantially increase difficulty in stacked configurations. This reinforces the hierarchy of effectiveness collated in graphical perception reviews, where position on a common scale outranks length [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the magnitude of specific sub-categories across different groups (e.g., "Sales of Product A in Q1 vs. Q2").
*   **Data Type:** Multidimensional quantitative data (Category + Sub-category).
*   **Audience:** Users requiring precise values rather than just an impression of "total" size.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The primary user goal is comparing the *totals* of the stacks, with segment breakdown being secondary.
*   **Reason:** Stacked bars are effective for showing the whole; aligned bars make comparing totals difficult.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Aligned grouped bars take up more horizontal space or require more complex small multiple layouts.
*   **The Risk:** Users may lose the sense of the "whole" or the sum of the parts.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding data labels inside the stack segments to compensate for the difficulty.
*   **Why it fails:** This turns the visualization into a reading exercise (looking up numbers) rather than a perceptual one, slowing down processing.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are users trying to compare the middle green segment of Bar A with the middle green segment of Bar B?
*   **The Test:** Cover the "total" of the bars. Is it easy to tell if the middle segment of Bar A is larger than Bar B? If they are visually similar, unalignment makes this impossible to judge accurately.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Unstack the bars into a "Grouped Bar" chart.
*   **Best Fix:** Use "Small Multiples" (faceting), presenting each sub-category as its own aligned bar chart sharing a common axis.
