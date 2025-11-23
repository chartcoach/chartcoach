---
id: set-hop-frame-rate-for-counting
title: Set HOP Frame Rates to Enable Silent Counting
bibliography: references.bib
description: Calibrate animation speeds in Hypothetical Outcome Plots to allow users
  to perceive and count distinct states.
labels:
- chart:hypothetical-outcome-plot
- visual:animation
- visual:time
- task:count
- impact:readability
- data:temporal
---

## The Rule <!-- role: advice -->
When designing Hypothetical Outcome Plots (HOPs), set the animation frame rate to approximately 400ms per frame (2.5 frames per second). Avoid rates that are fast enough to cause "flicker fusion" or blending.

## The Logic <!-- role: reason -->
The cognitive advantage of HOPs relies on the user's ability to process individual outcomes as finite events. [@hullman_hypothetical_2015] selected a 400ms duration because it provides enough time for eye motion and "silent counting"—allowing the user to consciously register whether a specific condition (like $Value > Threshold$) is met in that frame. If the rate is too fast, the animation merges into a static blur (similar to a gradient plot), forcing the user back into abstract visual integration rather than concrete counting.

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating probabilities based on specific criteria (e.g., "What is the probability the value is above 100?").
*   **Data Type:** Animated visualizations of probability distributions.
*   **Audience:** Users employing counting heuristics to gauge uncertainty.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The goal is to perceive the "shape" or density of the distribution rather than calculate specific probabilities.
*   **Reason:** Faster frame rates (approaching flicker fusion) cause the animation to visually converge into a static gradient plot, which may be preferred for identifying the central tendency or overall spread quickly [@hullman_hypothetical_2015].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Speed of information delivery.
*   **The Risk:** Watching a slow animation requires time and attention; users may become fatigued or impatient if required to watch for long periods to gather a representative sample.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** allowing the animation to run as fast as possible (e.g., 60fps) to look "smooth."
*   **Why it fails:** This turns the plot into a "flickering map" or static blur, preventing the counting strategy that makes HOPs effective for probability estimation.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the bars blur together? Can you verbally count "one, two, three" alongside the changes?
*   **The Test:** Try to count how many times the bar exceeds a certain line in a 10-second window. If the changes happen faster than you can sub-vocalize the count, it is likely too fast.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Hardcode a delay of 400-500ms between frame transitions.
*   **Best Fix:** Provide interactive controls allowing the user to pause, step through manually, or adjust the speed to their preferred counting pace.
