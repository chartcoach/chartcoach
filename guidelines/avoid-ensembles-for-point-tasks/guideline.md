---
id: avoid-ensembles-for-point-tasks
title: Avoid Ensemble Displays for Point-Specific Risk Judgments
bibliography: references.bib
description: Users over-weight individual ensemble members when they intersect with
  specific points of interest, leading to biased risk assessment.
labels:
- chart:ensemble
- task:risk-assessment
- task:locate
- visual:intersection
- impact:bias
- data:geospatial
- audience:novice
---

## The Rule <!-- role: advice -->
Do not rely on raw ensemble displays (spaghetti plots) if the user's primary task is to determine the risk level of a specific point location (e.g., a specific city or building).

## The Logic <!-- role: reason -->
Ensemble displays suffer from a "deterministic bias" where users overweight the importance of individual lines. If a specific line visually overlaps with a point of interest, users perceive that point as having much higher risk than a point located in the gap between lines, even if the gap-point is closer to the center of the probability distribution.
*   **The Principle:** The "Far Rig On Line" Effect. The visual intersection of a track and a point is a highly salient feature that overrides probabilistic reasoning (distance from center) [@padilla_effects_2017].
*   **The Evidence:** In Experiments 2 and 3, participants frequently judged a location far from the storm center as being at higher risk simply because an ensemble track passed directly over it, ignoring locations closer to the center that sat between tracks [@padilla_effects_2017].

## Where to Apply <!-- role: context -->
*   **User Goal:** Making binary decisions (e.g., evacuate/stay) or risk assessments for specific, granular locations.
*   **Data Type:** Ensemble forecast tracks overlaid on a map with specific points of interest.
*   **Audience:** Users who may believe the displayed lines are an exhaustive list of all possible outcomes rather than a statistical sample.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The task requires judging general areas or regional patterns rather than specific points.
*   **Reason:** Biases regarding individual tracks are less prevalent when users summarize patterns over larger areas [@padilla_effects_2017].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to show the underlying distribution structure (like bimodality) that ensembles excel at.
*   **The Risk:** By removing the lines, you might revert to summary displays (cones) which introduce size biases.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding more lines to fill the gaps.
*   **Why it fails:** This leads to visual crowding and eventually creates a solid shape, which users may interpret as a physical object (the size bias).

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the display look like a plate of spaghetti with gaps between the noodles?
*   **The Test:** Place a point of interest in a gap between two lines near the center. Place another point on a line far from the center. Ask the user which is at higher risk. If they choose the "on-line" point, the display is misleading them.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Instruct users explicitly that the lines are a sample and not an exhaustive list of paths.
*   **Best Fix:** For point-based tasks, use a visualization that encodes risk as a continuous field (e.g., color-coded risk maps or probabilistic surfaces) rather than discrete lines, to prevent the "gap" safety bias.
