---
id: use-ensembles-for-uncertainty-spread
title: Use Ensemble Displays to Communicate Probability Distributions
bibliography: references.bib
description: Ensemble displays allow users to correctly interpret increasing spread
  as increasing uncertainty, rather than changing physical intensity.
labels:
- chart:ensemble
- chart:spaghetti-plot
- task:assess-uncertainty
- visual:position
- impact:comprehension
- data:geospatial
- audience:novice
---

## The Rule <!-- role: advice -->
Use ensemble displays (plotting multiple individual data points or tracks) rather than summary statistics when you need novice users to accurately perceive probability distributions and decreasing certainty over time.

## The Logic <!-- role: reason -->
Ensemble displays allow users to utilize "ensemble coding"—the ability to mentally summarize visual features to perceive the gist of the data. The salient feature in an ensemble display is the relative spread of the members.
*   **The Principle:** Ensemble Coding. Viewers correctly map the "spreading out" of individual lines to "lower certainty" or "lower intensity" rather than misinterpreting it as a change in size [@padilla_effects_2017].
*   **The Evidence:** Participants viewing ensemble hurricane tracks correctly judged that intensity decreased as the tracks spread further apart. They also correctly identified that the forecast was less certain over time, unlike cone viewers who associated the visual expansion with increased storm size [@padilla_effects_2017].

## Where to Apply <!-- role: context -->
*   **User Goal:** Assessing the range of possible outcomes or the certainty of a prediction.
*   **Data Type:** Predictive models generating multiple potential outcomes (e.g., weather tracks, financial projections).
*   **Audience:** Non-experts who need to understand that a prediction is becoming less reliable further into the future.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset is extremely large, causing severe visual crowding (occlusion).
*   **Reason:** If individual lines cannot be differentiated, the "spread" becomes a solid mass, which may re-introduce the "size" bias or make the chart unreadable.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Ensemble displays are visually "busy" and complex compared to clean summary statistics.
*   **The Risk:** Visual crowding makes it difficult to trace individual lines, though the overall distribution is usually still perceivable.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Averaging the ensemble into a single "mean" line.
*   **Why it fails:** This removes the uncertainty information entirely, giving a false sense of precision.

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you see distinct lines spreading apart as uncertainty increases?
*   **The Test:** Show the chart to a user and ask, "Are the forecasters more sure or less sure about the data on the right side?"

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Plot a random subset of the ensemble members (e.g., 50 representative lines) to reduce crowding while maintaining the visual spread.
*   **Best Fix:** Use an ensemble display for the general pattern, but switch to different techniques if the user needs to judge specific point locations (see specific point-risk guidelines).
