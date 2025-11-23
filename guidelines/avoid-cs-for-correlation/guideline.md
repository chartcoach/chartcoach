---
id: avoid-cs-for-correlation
title: Avoid Connected Scatterplots for Correlation
bibliography: references.bib
description: Use dual-axis line charts instead of connected scatterplots when the
  user needs to recognize positive or negative correlations.
labels:
- chart:connected-scatterplot
- chart:dual-axis-line
- task:correlate
- impact:clarity
- data:multivariate
---

## The Rule <!-- role: advice -->
Use standard line charts (dual-axis or small multiples), not connected scatterplots, if the viewer needs to identify correlations between the two variables.

## The Logic <!-- role: reason -->
Viewers are trained to see parallel lines as positive correlation and crossing lines (X-shapes) as negative correlation in line charts. In connected scatterplots, correlations appear as diagonals, which users rarely describe using correlational language.
*   **The Principle:** Learned Perceptual Heuristics.
*   **The Evidence:** Participants frequently used terms like "inverse relationship" or "correlated" for dual-axis charts (28 mentions) but almost never for connected scatterplots (3 mentions) regarding the same data [@haroz_connected_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Determining if Variable A moves in sync with Variable B.
*   **Data Type:** Two variables that share a strong linear relationship.
*   **Audience:** Analytical audiences looking for statistical relationships.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Teaching advanced chart literacy.
*   **Reason:** If the goal is to *teach* how diagonals represent correlation in 2D space, this chart is the appropriate tool.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to show specific "states" or "shapes" defined by the intersection of values (like the Phillips curve in economics).
*   **The Risk:** Viewers might miss the fact that the two variables are related.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assuming a diagonal line is intuitive.
*   **Why it fails:** Even though a diagonal line *is* a correlation, users without training do not spontaneously use correlational vocabulary to describe it [@haroz_connected_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** The data forms a straight diagonal line.
*   **The Test:** Ask a user, "How are these two variables related?" If they describe the shape ("it goes up and right") rather than the relationship ("they grow together"), the correlation is lost.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add text explicitly stating the correlation (e.g., "As X increases, Y increases").
*   **Best Fix:** Switch to a Dual-Axis Line Chart or two stacked area charts.
