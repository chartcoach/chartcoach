---
id: use-hops-for-trend-judgments
title: Animate Uncertainty for Trend Decisions
bibliography: references.bib
description: Use Hypothetical Outcome Plots (HOPs) instead of static error bars to
  help untrained observers identify trends in noisy data.
labels:
- chart:line
- chart:bar
- task:decision-making
- visual:animation
- impact:accuracy
- data:time-series
- audience:novice
---

## The Rule <!-- role: advice -->
Use Hypothetical Outcome Plots (HOPs) rather than static error bars when asking untrained audiences to identify underlying trends in noisy time-series data.

## The Logic <!-- role: reason -->
Static summary statistics, such as error bars, are often misunderstood by lay audiences and can lead to biases where viewers underweight uncertainty. HOPs work by converting uncertainty into a temporal experience (frequency) rather than a spatial abstraction.
*   **The Principle:** Frequency-oriented framing of probability.
*   **The Evidence:** In controlled experiments, observers required less evidence to correctly distinguish between underlying trends (e.g., growth vs. no growth) when using HOPs compared to error bars [@kale_hypothetical_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Making binary decisions about trends (e.g., "Is the job market growing or not?") in the presence of sampling error.
*   **Data Type:** Time series data or bar charts with significant variance/noise.
*   **Audience:** General public or "untrained observers" who may lack statistical literacy regarding confidence intervals or standard error.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to read a precise value (central tendency) rather than judge the shape or likelihood of a trend.
*   **Reason:** Prior work cited by the authors suggests static plots (like error bars or violin plots) can be superior for estimating specific mean values in high-variance distributions [@kale_hypothetical_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** The viewer cannot see the "summary" at a single glance; they must watch the animation for a period to integrate the information.
*   **The Risk:** Users might report slightly higher confidence in their judgments with HOPs, which—if their judgment is wrong—could lead to overconfidence, although the paper found the relationship between confidence and accuracy to be complex [@kale_hypothetical_2019].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding standard error bars to a trend line.
*   **Why it fails:** Viewers often ignore the error bars or misinterpret them as the range of all possible values, failing to account for the noise in the process that produced the data [@kale_hypothetical_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using static "whiskers" or shaded regions to show uncertainty on a trend line for a general audience?
*   **The Test:** Ask a user to predict the likelihood of the trend. If they struggle to integrate the variance into their decision, the static abstraction is likely failing them.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If animation is impossible, use a static ensemble (showing multiple lines) rather than summary bars, though this is less effective than animation.
*   **Best Fix:** Implement HOPs: Animate the display to loop through disparate samples from the distribution (e.g., 12-month sets of values) to show variability directly.
