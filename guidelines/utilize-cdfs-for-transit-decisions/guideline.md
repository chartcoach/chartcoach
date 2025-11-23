---
id: utilize-cdfs-for-transit-decisions
title: Use Cumulative Distribution Functions for Decision Tasks
bibliography: references.bib
description: Despite perceived complexity, CDFs support high-quality decision-making
  for laypeople in transit contexts.
labels:
- chart:cdf
- chart:line
- task:decision-making
- task:probability-estimation
- impact:consistency
- audience:general-public
---

## The Rule <!-- role: advice -->
Do not shy away from using **Cumulative Distribution Function (CDF)** plots for general audiences, particularly for "at least/at most" decision tasks.

## The Logic <!-- role: reason -->
While often considered difficult for the public to interpret, CDFs allow for highly accurate extraction of probabilities (e.g., "What is the chance the bus arrives *by* 5:00 PM?"). This accuracy in estimation translates directly to better decision quality.
*   **The Principle:** Direct Probability Read-off.
*   **The Evidence:** CDFs performed nearly as well as the best-performing dotplots and significantly better than text descriptions or interval plots. They led to decisions with higher expected payoffs and lower variance compared to textual displays [@fernandes_uncertainty_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Answering threshold questions, such as "What is the probability X is less than Y?" (e.g., "Will I catch the bus if I arrive at minute 10?").
*   **Data Type:** Continuous probabilistic predictions.
*   **Audience:** General users of transit apps, contrary to the belief that CDFs are expert-only tools.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the user needs to immediately identify the *most likely* single outcome (the mode) without determining a cumulative probability.
*   **Reason:** Identifying the mode (the steepest part of a CDF) is perceptually harder than seeing the highest stack in a dotplot or the peak of a PDF.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Immediate recognition of the distribution's "shape" (skewness/kurtosis) is less intuitive than with a density plot.
*   **The Risk:** Users may require a brief learning period to understand that the y-axis represents cumulative probability, though the study showed effective learning within a single session [@fernandes_uncertainty_2018].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Reverting to simple interval plots (e.g., error bars) to avoid complexity.
*   **Why it fails:** Interval plots often leave out critical information about the tails or the specific probability of a user's chosen threshold, leading to lower decision quality [@fernandes_uncertainty_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the line monotonically increasing from 0 to 1 (or 0 to 100%)?
*   **The Test:** Can a user find a time on the x-axis and immediately read the probability of success on the y-axis without performing mental arithmetic (like summing areas)?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add gridlines connecting the x-axis values to the probability curve.
*   **Best Fix:** Use a Complementary CDF (CCDF) if the user question is "How much chance do I still have?" or a standard CDF if the question is "What is the chance it has already arrived?"
