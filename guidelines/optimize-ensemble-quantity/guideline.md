---
id: optimize-ensemble-quantity
title: Display a Moderate Number of Ensemble Members
bibliography: references.bib
description: When visualizing uncertainty with ensemble paths, use a moderate number
  of lines (approx. 33) to reduce bias.
labels:
- chart:ensemble-plot
- chart:spaghetti-plot
- visual:density
- impact:bias-reduction
- task:risk-assessment
- data:geospatial
- audience:novice
---

## The Rule <!-- role: advice -->
When using ensemble displays to show uncertainty (such as hurricane tracks), plot a moderate number of ensemble members (approximately 30 to 35). Avoid displaying very few tracks (e.g., 9) or an excessive amount (e.g., 65+).

## The Logic <!-- role: reason -->
People suffer from a "collocation effect," where they perceive a location intersected by a specific line as having higher risk than a location just slightly off the line, even when both are equally deep within the probability distribution.
*   **The Principle:** Deterministic Construal and Visual Weight. Increasing the number of lines helps override the assumption that each line is a deterministic prediction.
*   **The Evidence:** [@padilla_powerful_2020] found that increasing the number of lines from 9 to 33 significantly reduced the collocation bias. However, increasing it further to 65 tracks caused the bias to creep back up because users began to believe the display showed *all* possible paths.

## Where to Apply <!-- role: context -->
*   **User Goal:** Assessing risk or damage potential based on probabilistic forecasts.
*   **Data Type:** Ensemble forecasting data (e.g., hurricane paths, stock market projections).
*   **Audience:** Novice users or the general public who may interpret individual lines as specific, deterministic outcomes.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the display medium has extremely low resolution.
*   **Reason:** 30+ lines might merge into a solid blob, losing the "ensemble" characteristic and resembling a confidence envelope or summary cone, which carries its own set of biases (e.g., the containment bias).

## The Price <!-- role: costs -->
*   **The Sacrifice:** A moderate number of lines increases visual clutter compared to a simple summary statistic or a 9-line plot.
*   **The Risk:** If the lines are too thick or the screen too small, the distribution may become illegible.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Plotting only a handful of lines (e.g., 9 or fewer) to keep the chart "clean."
*   **Why it fails:** [@padilla_powerful_2020] demonstrated that sparse displays elicit the strongest collocation effect, causing users to irrationally favor locations in the gaps between lines.
*   **The Over-Correction:** Plotting hundreds of lines to show "total" uncertainty.
*   **Why it fails:** Users may incorrectly assume that "all possible outcomes" are represented, leading to false confidence if an event occurs in a micro-gap between dense lines.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do large gaps exist between lines in the high-probability zones? (Too few). Does the chart look like a solid shape with no visible separation between lines? (Too many).
*   **The Test:** Ask a user: "Does this chart show every possible path the storm could take?" If they say yes, you likely have too many lines.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Adjust the sampling rate of your ensemble data to render approximately 30 lines.
*   **Best Fix:** Use a moderate number of lines (approx. 33) and pair it with instructions that explicitly state the lines are a subset of many possibilities.
