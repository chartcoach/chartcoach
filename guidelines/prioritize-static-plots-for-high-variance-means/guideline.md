---
id: prioritize-static-plots-for-high-variance-means
title: Prioritize Static Plots for Mean Estimation in High-Variance Data
bibliography: references.bib
description: Use static error bars instead of animations when the user must estimate
  the mean of a highly variable distribution.
labels:
- chart:error-bar
- chart:violin-plot
- chart:hypothetical-outcome-plot
- task:estimate-mean
- data:high-variance
- impact:precision
---

## The Rule <!-- role: advice -->
If the primary user task is to strictly estimate the mean value of a single variable with high variance, use static representations (like error bars or violin plots) instead of animated Hypothetical Outcome Plots (HOPs).

## The Logic <!-- role: reason -->
[@hullman_hypothetical_2015] found that while HOPs are superior for probability estimates, they performed worse than static error bars for estimating the mean ($\mu$) when the standard deviation ($\sigma$) was high. This is because HOPs require the user to visually integrate the average position of a line that is "jumping" around a large vertical range. Static plots explicitly mark the central tendency or provide a stable shape, making interpolation between axis ticks significantly easier.

## Where to Apply <!-- role: context -->
*   **User Goal:** Reading the specific average value (mean) of a distribution.
*   **Data Type:** Univariate distributions with high standard deviation (spread).
*   **Audience:** Users who need to report a specific number for the central tendency.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The variance is low.
*   **Reason:** When the standard deviation is small, HOPs performance is comparable to static plots because the visual integration required is minimal [@hullman_hypothetical_2015].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to easily communicate joint probabilities or cumulative densities, which HOPs excel at.
*   **The Risk:** Static plots (especially error bars) are frequently misinterpreted as ranges of uniform probability or non-significance boundaries by lay readers.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using HOPs for every uncertainty task "because they are better."
*   **Why it fails:** Visualization effectiveness is task-dependent. Animation adds cognitive load that impedes simple mean extraction in noisy data.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the animated object moving erratically over a large portion of the y-axis?
*   **The Test:** Pause the animation. Can you estimate the mean better now than when it was playing? If yes, the motion is hindering the estimation.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Allow the user to toggle the animation off to see a static summary (mean + error bar).
*   **Best Fix:** Combine representations: Show a static marker for the mean (to support precise reading) superimposed over the animated HOPs (to support uncertainty perception).
