---
id: visualize-confidence-intervals
title: Display Confidence Intervals on Forecasts
bibliography: references.bib
description: Include shaded ranges or error bars to communicate that polls are estimates,
  not results.
labels:
- chart:bar
- chart:column
- task:estimate
- visual:uncertainty
- impact:accuracy
- data:statistical
- audience:general
---

## The Rule <!-- role: advice -->
When showing election forecasts or polling averages, visually include the confidence intervals (ranges of uncertainty) alongside the estimated value.

## The Logic <!-- role: reason -->
Polls are probabilistic estimates, not definitive counts. Visualizing the margin of error "helps to communicate the data's uncertainty and the fact that these are not the final results" [@muth_german_election_2021]. This prevents the audience from interpreting a lead within the margin of error as a guaranteed victory.

*   **The Principle:** Uncertainty Visualization
*   **The Evidence:** [@muth_german_election_2021]

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding the reliability of a prediction.
*   **Data Type:** Polling averages, statistical forecasts, or predictive models.
*   **Audience:** Voters and news consumers who may misinterpret a single percentage point lead as significant.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Visualizing official, certified final election results.
*   **Reason:** Final results are deterministic counts (barring recounts), so uncertainty ranges are no longer applicable.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual simplicity; the chart becomes visually denser with extra markings or shaded areas.
*   **The Risk:** Novice users might find the "fuzzy" lines or error bars confusing if not labeled clearly.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a single thin bar or line for a forecast.
*   **Why it fails:** It implies false precision, suggesting the outcome is certain when it is actually a range of possibilities.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is there a single hard edge to your bar or line?
*   **The Test:** Ask if the value shown (e.g., 25%) could realistically be 23% or 27%. If yes, does the graphic show that possibility?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add error bars ("whiskers") to the tops of bar charts.
*   **Best Fix:** Use a shaded area (e.g., a light background range behind the main value) to represent the likely range of outcomes, as seen in forecasts by The Economist referenced in the text [@muth_german_election_2021].
