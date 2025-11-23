---
id: separate-series-to-avoid-perceptual-pull
title: Separate Data Series to Avoid Perceptual Pull
bibliography: references.bib
description: Plotting multiple series on one graph causes the perceived average of
  one to be pulled toward the other.
labels:
- chart:line
- chart:bar
- task:compare
- visual:position
- impact:accuracy
- complexity:multivariate
---

## The Rule <!-- role: advice -->
Do not plot two different data series on the same graph if the user needs to accurately perceive the average position of either series. Use small multiples (separate plots) instead.

## The Logic <!-- role: reason -->
When two data series (lines or sets of bars) appear in the same display, they distort the perception of each other.
*   **The Principle:** Perceptual Pull. The estimated average position of a target series is "pulled" toward the location of the irrelevant series. For example, a line at the top of a chart will make a line at the bottom appear higher than it is, and vice versa.
*   **The Evidence:** Study results showed that "position estimates for a target data series... were 'pulled' toward the irrelevant position values present in the same graph" [@xiong_biased_2020]. This effect can exaggerate or diminish existing estimation biases.

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurate estimation of the average level of a specific metric without interference from secondary metrics.
*   **Data Type:** Two or more continuous data series (e.g., Revenue vs. Expenses).
*   **Audience:** Users performing analytical tasks where visual accuracy of the mean is critical.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Direct Point-to-Point Comparison.
*   **Reason:** If the user needs to compare value X at time T against value Y at time T, superimposing the series is necessary despite the bias in average estimation.
*   **Scenario:** Limited Screen Real Estate.
*   **Reason:** Small multiples may reduce the chart size too much to be legible.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Direct comparison of individual data points becomes harder when charts are spatially separated.
*   **The Risk:** Users may struggle to see the correlation or interaction between the two series.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Plotting a "reference" line or "background" series to provide context.
*   **Why it fails:** Even an irrelevant or background series acts as an anchor, magnetically pulling the user's perception of the main data's average toward itself [@xiong_biased_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Two or more lines or bar sets share the same x/y-axis space.
*   **The Test:** Check if the series are vertically distinct (one high, one low). If so, the "pull" effect will be maximized.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Toggle visibility so users can view one series at a time.
*   **Best Fix:** Use "Small Multiples" (faceting) to give each data series its own independent y-axis frame, vertically aligned for easy scanning.
