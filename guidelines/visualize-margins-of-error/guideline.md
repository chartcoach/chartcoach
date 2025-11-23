---
id: visualize-margins-of-error
title: Report Margins of Error in Polls
bibliography: references.bib
description: Include visual representations of statistical uncertainty in election
  poll graphics.
labels:
- chart:bar
- chart:dot-plot
- task:estimate
- visual:error-bars
- impact:accuracy
- data:statistical
- audience:public
---

## The Rule <!-- role: advice -->
Always highlight the margin of error when visualizing election poll results. Do not present poll numbers as absolute, precise outcomes.

## The Logic <!-- role: reason -->
Election polls are based on samples (commonly 1,000 to 3,000 people) extrapolated to represent a whole country. This process inherently includes uncertainty.
*   **The Principle:** Statistical Probability. A poll result is a range, not a point. For example, a 50% outcome with a ±3% margin means the actual number is likely between 47% and 53% [@jockers_election_polls_2021].
*   **The Consequence:** In tight races, the margin of error can determine whether a lead is statistically significant or merely noise. Ignoring this misleads the audience into believing the data is more precise than it actually is.

## Where to Apply <!-- role: context -->
*   **User Goal:** Informing the public about the current standing of political candidates or parties.
*   **Data Type:** Election polling data derived from sample groups.
*   **Audience:** General news readers who may not intuitively understand statistical sampling.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The source text provides no specific exceptions to this rule, implying it is a fundamental requirement for accurate reporting [@jockers_election_polls_2021].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual simplicity. Adding error bars, faint ranges, or explanatory text adds graphical elements to the chart.
*   **The Risk:** Readers unfamiliar with error bars might find the chart slightly harder to decode initially.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Reporting the exact percentage (e.g., "29%") without qualification.
*   **Why it fails:** It frames a probability estimate as an "actual election result," which it is not [@jockers_election_polls_2021].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart show a single, hard edge for the value (e.g., a standard bar) without any whiskers, shaded areas, or text ranges?
*   **The Test:** If a candidate has 30% and another has 32%, does the chart make it look like the second candidate is definitely winning? If so, and the margin is ±2%, the chart is misleading.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a subtitle or annotation stating the margin (e.g., "Margin of error: +/- 2.5%").
*   **Best Fix:** Visualize the range directly using error bars or shaded confidence intervals on top of the bars or dots.
