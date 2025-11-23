---
id: smooth-polling-lines
title: Smooth Noisy Polling Data
bibliography: references.bib
description: Apply averaging to polling line charts to reduce visual noise and clarify
  trends.
labels:
- chart:line
- task:trend-analysis
- visual:shape
- impact:clarity
- data:temporal
- audience:general
- context:election-polls
---

## The Rule <!-- role: advice -->
Apply smoothing algorithms, such as moving averages or Loess, to line charts visualizing election polls over time.

## The Logic <!-- role: reason -->
Raw polling data often results in "ragged" lines due to frequency and statistical noise. Smoothing averages these data points to reveal the underlying trend rather than the noise of individual data points. As noted in the text, "the more polls are averaged, the less ragged the lines become," facilitating easier comparison between competing entities [@muth_german_election_2021].

*   **The Principle:** Signal-to-Noise Ratio
*   **The Evidence:** [@muth_german_election_2021]

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying broad shifts in public opinion over weeks or months.
*   **Data Type:** High-frequency polling data from multiple institutes.
*   **Audience:** General news readers who need to understand the "race" without getting lost in daily fluctuations.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Analyzing specific outliers or individual poll methodology.
*   **Reason:** If the goal is to critique specific polls or show the volatility/discrepancy between different polling institutes, smoothing obscures the raw data points required for that analysis.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the precision of specific data points and dates.
*   **The Risk:** Over-smoothing can lag behind real-time shifts or hide sudden, genuine changes in public opinion.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Plotting every single poll as a raw line without transparency or aggregation.
*   **Why it fails:** It creates a "spaghetti chart" where crossing lines and jagged edges make it impossible to discern who is leading.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the line look jagged, jittery, or "nervous"? Can you clearly see the direction of the trend, or is the eye distracted by up-and-down spikes?
*   **The Test:** Compare your chart to the "ragged" Guardian lines versus the "smooth" Economist lines mentioned in the text [@muth_german_election_2021].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Apply a simple moving average (e.g., 10-day rolling average).
*   **Best Fix:** Use a statistical smoothing method like Loess (locally weighted scatterplot smoothing) to create a fluid trend line while retaining the data's integrity.
