---
id: remove-deterministic-centerlines
title: Remove the Centerline from Uncertainty Plots
bibliography: references.bib
description: Remove the central mean line from forecast visualizations to prevent
  users from overestimating risk at the center and underestimating it elsewhere.
labels:
- chart:map
- visual:line
- task:risk-assessment
- impact:bias-reduction
- data:geospatial
- audience:novice
---

## The Rule <!-- role: advice -->
Do not include a specific centerline (mean track) inside a cone or area of uncertainty.

## The Logic <!-- role: reason -->
A salient centerline anchors the user's attention, causing them to interpret the middle of the distribution as the "definite" path or the location of highest intensity. This leads to a sharp drop-off in risk perception as distance from the center increases.
*   **The Principle:** The Distance Heuristic. Users utilize the distance from the visible line as a primary proxy for risk, ignoring the broader probability distribution.
*   **The Evidence:** Visualizations including a centerline resulted in significantly higher damage ratings at the center and steeper drop-offs in ratings at the edges compared to visualizations without the line (such as fuzzy cones or ensembles) [@ruginski_non-expert_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** encouraging users to consider the full range of possible outcomes, not just the "most likely" one.
*   **Data Type:** Spatial uncertainty or forecast cones.
*   **Audience:** General public or decision-makers who need to prepare for low-probability, high-impact events (edge cases).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the specific task requires identifying the statistically most probable point estimate rather than assessing general risk area.
*   **Reason:** The centerline accurately represents the mean or median track, which is necessary for precise point estimation tasks.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Users lose a clear "anchor" for the eye, which can make the visualization feel less precise or authoritative.
*   **The Risk:** Users might feel the forecast is "vague" without a specific line to follow.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Keeping the line but making it dashed or thinner.
*   **Why it fails:** As long as a central line is visible, users tend to anchor on it as the "location of impact" [@ruginski_non-expert_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is there a dark, sharp line running through the middle of your shaded region?
*   **The Test:** Cover the shaded area. Does the remaining line look like a definitive path? If so, it will bias the user.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Delete the centerline layer completely, leaving only the uncertainty bounds (cone-only) or a gradient (fuzzy-cone).
*   **Best Fix:** Replace the centerline and the cone with an ensemble of tracks to show distribution without a single "correct" path.
