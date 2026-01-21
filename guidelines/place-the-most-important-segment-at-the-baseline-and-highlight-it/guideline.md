---
id: place-the-most-important-segment-at-the-baseline-and-highlight-it
title: Put the Key Segment on the Bottom and Highlight It with Color
bibliography: references.bib
description: Improve comparability in stacked columns by placing the most important
  segment at the bottom baseline and using color to draw attention to it.
labels:
- chart:stacked-column
- task:compare
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
- source:datawrapper
---

## The Rule <!-- role: advice -->

Place the most important segment at the bottom of the stack and use color to make it stand out.

## The Logic <!-- role: reason -->

Only the bottom segment shares a consistent baseline across columns, so it’s the easiest segment to compare precisely. Color emphasis helps readers quickly find the segment you want them to compare [@muth_stacked_columns_2018].

- **The Principle:** Baseline + preattentive emphasis guides accurate comparison
- **The Evidence:** [@muth_stacked_columns_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare one key category’s values across multiple totals
- **Data Type:** Part-to-whole totals where one segment is editorially central
- **Audience:** General audiences scanning for the main message [@muth_stacked_columns_2018]

## When to Break It <!-- role: exceptions -->

- **Scenario:** No single segment is more important than the others.
- **Reason:** Highlighting one segment may introduce unintended emphasis; consider a different chart type if comparisons across many parts matter [@muth_stacked_columns_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to reorder categories away from a “natural” or original data order.
- **The Risk:** Over-emphasis can make secondary segments feel less important than they are [@muth_stacked_columns_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Leaving the key segment in the middle/top and expecting readers to compare it accurately.
- **Why it fails:** The segment floats on different baselines, making comparisons difficult [@muth_stacked_columns_2018].
- **The Wrong Fix:** Highlighting multiple segments equally with strong colors.
- **Why it fails:** Competes for attention and undermines the intended focus [@muth_stacked_columns_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The main story segment is not the one that’s easiest to compare across columns.
- **The Test:** Identify the “one thing” readers should compare; confirm it’s the bottom segment and visually dominant [@muth_stacked_columns_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reorder the stack so the key segment is at the bottom; assign it the strongest, distinct color.
- **Best Fix:** If multiple segments must be compared, switch to split bars or small multiples rather than relying on stack position [@muth_stacked_columns_2018].
