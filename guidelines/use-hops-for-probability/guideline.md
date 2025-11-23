---
id: use-hops-for-probability
title: Use Hypothetical Outcome Plots (HOPs) for Probability Tasks
bibliography: references.bib
description: Use animated samples to communicate probability of superiority effectively.
labels:
- chart:animation
- task:estimate-probability
- visual:motion
- impact:comprehension
- data:simulation
- audience:general
---

## The Rule <!-- role: advice -->
Use **Hypothetical Outcome Plots (HOPs)**—animated visualizations that cycle through random draws from the distribution—when asking users to estimate the probability that one group outperforms another (probability of superiority).

## The Logic <!-- role: reason -->
HOPs leverage the human capacity for frequency encoding. Instead of asking users to perform complex mental calculus on static error bars (integrating the overlap of two distributions), HOPs allow users to directly experience the frequency of outcomes.
*   **The Principle:** **Frequency Encoding.** Users can "count" or estimate via ensemble processing how often the treatment bar is higher than the control bar over time.
*   **The Evidence:** In [@hofman_how_2020], participants using HOPs provided estimates for "probability of superiority" that were much closer to the true normative value (e.g., 57%) compared to those viewing 95% Confidence Intervals, who vastly overestimated the probability (e.g., ~86%).

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating the likelihood of a specific event (e.g., "How often will the treatment beat the control?").
*   **Data Type:** Distributions where samples can be generated or simulated.
*   **Audience:** Digital/Web-based audiences where animation is technically feasible.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Static media (Print / PDF).
*   **Reason:** Animation is impossible. In this case, use static 95% Prediction Intervals (Standard Deviation) as a fallback, which perform similarly to HOPs for effect size estimation [@hofman_how_2020].

## The Price <!-- role: costs -->
*   **The Sacrifice:** At-a-glance readability. The user must watch the animation for a duration to gather information.
*   **The Risk:** Distraction or cognitive load if the animation speed is too fast or too slow (the study used 2.5 frames per second).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing a static density plot or violin plot without explaining probability.
*   **Why it fails:** While better than error bars, static distributions still require users to mentally calculate the area of overlap, which is cognitively difficult compared to frequency counting in HOPs.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the chart moving?
*   **The Test:** Can the user answer "How many times out of 100 will A beat B?" by simply watching the chart?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If animation isn't possible, show multiple static samples ("small multiples") to simulate draws.
*   **Best Fix:** Implement an animated GIF or JavaScript loop showing ~2.5 frames per second of random samples from the distributions [@hofman_how_2020].
