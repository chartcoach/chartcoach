---
id: connected-scatterplot-mark-horizontal-axis-polarity
title: Make 'Higher Is to the Right' Obvious
bibliography: references.bib
description: Reduce rare but consequential axis-polarity flips on the connected scatterplot
  x-axis.
labels:
- chart:scatter
- task:read
- visual:axis
- impact:clarity
- data:temporal
- audience:novice
- chart:connected-scatterplot
---

## The Rule <!-- role: advice -->

Visually reinforce the horizontal axis polarity in a connected scatterplot so viewers clearly understand that larger x-values are to the right.

## The Logic <!-- role: reason -->

A subset of viewers may incorrectly map “larger values” to the left side of the connected scatterplot’s x-axis during translation tasks, indicating confusion about x-axis polarity compared with conventional expectations [@harozConnectedScatterplotPresenting2016].

- **The Principle:** Axis polarity confirmation
- **The Evidence:** In CS-to-DALC translation, participants occasionally flipped the connected scatterplot’s horizontal axis, suggesting some read larger values from the left rather than the right [@harozConnectedScatterplotPresenting2016].

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly map position to value on the x-axis.
- **Data Type:** Connected scatterplots intended for broad audiences or format translation (e.g., showing both CS and line-chart versions).
- **Audience:** Viewers new to connected scatterplots.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart is interactive and provides immediate feedback on hover (values shown directly).
- **Reason:** Direct value readout can reduce reliance on polarity inference [@harozConnectedScatterplotPresenting2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional axis decoration may reduce minimalist style.
- **The Risk:** Strong axis embellishment can compete with the path for attention.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming “it’s a Cartesian plot, so everyone knows right means higher.”
- **Why it fails:** Empirical evidence showed occasional x-axis polarity reversals in practice [@harozConnectedScatterplotPresenting2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers’ verbal summaries invert x (e.g., describing right-side points as “lower”).
- **The Test:** Hide tick labels and ask which side implies higher x; if responses vary, polarity is not visually anchored enough.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Strengthen tick labeling and axis title placement; consider adding an explicit “↑/→ = more” cue near axes.
- **Best Fix:** Add point labels or annotations at extremes (“Highest [x-variable]”) to anchor interpretation [@harozConnectedScatterplotPresenting2016].
