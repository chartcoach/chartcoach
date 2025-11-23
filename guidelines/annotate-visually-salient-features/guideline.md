---
id: annotate-visually-salient-features
title: Annotate Visually Salient Features
bibliography: references.bib
description: Prioritize annotating peaks, troughs, and sharp changes to help users
  explain observed trends in the data.
labels:
- chart:line
- task:explain
- visual:saliency
- impact:comprehension
- data:quantitative
---

## The Rule <!-- role: advice -->
Select data points for annotation that are visually salient, such as global maximums, minimums, or moments of rapid change (high delta).

## The Logic <!-- role: reason -->
Visualizations that account for "visual saliency" (statistical prominence) are perceived as better at explaining trends and oscillations in performance. Users naturally gravitate toward visual outliers like peaks and troughs; providing text at these locations satisfies the user's need to understand "what happened here?" In evaluations, graphs annotated based on visual saliency were rated significantly higher for explaining trends than those based solely on topic relevance.
*   **The Principle:** Observational Annotation / Visual Saliency
*   **The Evidence:** [@hullman_contextifier_2013]

## Where to Apply <!-- role: context -->
*   **User Goal:** Explaining performance, volatility, or significant shifts in data.
*   **Data Type:** Time-series data (e.g., stock prices, trade volume).
*   **Audience:** Users trying to make sense of visual anomalies or extremes in a line graph.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The salient feature is irrelevant to the current narrative.
*   **Reason:** A massive spike caused by a system error or an unrelated event might distract from the specific story (e.g., a management change) the user is investigating.
*   **Scenario:** The data is flat/stable.
*   **Reason:** If there are no peaks or troughs, forcing saliency-based annotations may highlight noise.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Topical relevance. A visually salient point (e.g., a market crash) might not be semantically related to the specific news article or topic the user is currently reading about.
*   **The Risk:** The "Context Blind" problem. The graph explains the *data* well, but might fail to connect to the *story* or *context* surrounding the data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Annotating random points or purely periodic intervals (e.g., every January 1st).
*   **Why it fails:** This ignores the "visual manifestations of features of the data," leaving the user to wonder about the unexplained peaks and valleys.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the highest peaks and lowest valleys unlabeled?
*   **The Test:** Look at the chart's geometry. If your eye is drawn to a sharp spike, is there text explaining it?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Manually identify the global max/min and largest day-over-day changes and add labels to them.
*   **Best Fix:** Use a "feature generator" algorithm that calculates statistical saliency (peaks, troughs, deltas) to automatically suggest candidate points for annotation.
