---
id: use-human-scale-number-formats-and-avoid-extra-precision
title: Choose Simple Number Formats and Avoid Unnecessary Precision
bibliography: references.bib
description: "Use readable abbreviations and minimal decimals so numbers don\u2019\
  t overwhelm the chart."
labels:
- chart:general
- task:read-value
- visual:text
- impact:clarity
- data:quantitative
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Format numbers for quick reading: avoid unnecessary decimal places and long thousands-grouped values; use compact formats (e.g., k/m/b) and remove trailing zeros when they add no meaning.

## The Logic <!-- role: reason -->

Over-precise numbers are hard to parse and remember and can make a visualization feel complicated at first sight. Readable rounding and abbreviations keep attention on patterns and comparisons.

- **The Principle:** Reduce numeric noise to improve comprehension and recall
- **The Evidence:** [@muth_text_in_data_visualizations_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand magnitude and differences without getting bogged down in exactness
- **Data Type:** Quantitative values shown as labels, axis ticks, or prominent callouts
- **Audience:** General audiences, especially for explanatory charts [@muth_text_in_data_visualizations_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The exact value is the point (e.g., a specific official figure) and rounding would change interpretation.
  - **Reason:** Precision is required for correctness; keep the exact number visible (or provide it at least in a tooltip) [@muth_text_in_data_visualizations_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced precision in the main view.
- **The Risk:** Poor rounding choices can imply false simplicity or hide small but important differences [@muth_text_in_data_visualizations_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing many decimals by default (e.g., 22.42%).
  - **Why it fails:** Adds complexity and harms scanability and memorability [@muth_text_in_data_visualizations_2022].
- **The Wrong Fix:** Using full large integers everywhere (e.g., 12,831,283) when the chart doesn’t require that precision.
  - **Why it fails:** Makes labels heavy and visually noisy [@muth_text_in_data_visualizations_2022].
- **The Wrong Fix:** Using multipliers in prose (“in millions”) and forcing mental math.
  - **Why it fails:** Adds cognitive work that formatting can avoid [@muth_text_in_data_visualizations_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Numbers dominate the chart visually, or you see many decimals and long digit strings.
- **The Test:** Ask, “Would a reader remember these numbers?” If not, simplify; then verify the chart’s message still holds after rounding [@muth_text_in_data_visualizations_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce decimals, remove trailing zeros, and abbreviate large numbers (k/m/b).
- **Best Fix:** Show rounded numbers in labels/axes, and provide exact values via tooltips, downloadable data, or surrounding text when needed [@muth_text_in_data_visualizations_2022].
