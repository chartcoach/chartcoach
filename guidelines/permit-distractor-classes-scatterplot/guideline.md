---
id: permit-distractor-classes-scatterplot
title: Permit Distractor Classes in Scatterplots
bibliography: references.bib
description: Adding extra data classes does not degrade the ability to compare averages
  of specific groups.
labels:
- chart:scatterplot
- task:aggregate
- task:filter
- visual:distractor
- impact:density
---

## The Rule <!-- role: advice -->
Feel free to include multiple data classes in a scatterplot, even if the user only needs to compare a subset of them at a time.

## The Logic <!-- role: reason -->
Visual selective attention is robust enough to filter out "irrelevant" classes (distractors) when a strong selection cue (like color) is used. The presence of a third or fourth group does not impede the ability to average the positions of the first two groups.
*   **The Principle:** Attentional Selection/Filtering. The visual system can suppress irrelevant items based on features (like color) while processing the target items.
*   **The Evidence:** Experiments comparing 2-class displays (E-1) against 3-class displays (E-4) found no significant difference in accuracy for aggregate tasks [@zeng_review_2023]. The original authors state that adding irrelevant additional classes does not degrade performance [@gleicher_perception_2013].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing Group A vs. Group B in a dataset that also contains Group C.
*   **Data Type:** Multiclass scatterplots.
*   **Audience:** Users exploring complex datasets.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The "distractor" classes share the same visual encoding (e.g., color) as the target classes.
*   **Reason:** The visual system cannot filter out the distractors if they are not visually distinct from the targets.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual simplicity. The chart will appear more complex initially.
*   **The Risk:** If the color palette is not distinct (e.g., Group C is a shade of red similar to Group A), interference will occur.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Creating three separate charts (A vs B, B vs C, A vs C) to avoid showing A, B, and C together.
*   **Why it fails:** It fragments the context. Users can successfully ignore Group C to compare A and B within a single integrated view [@gleicher_perception_2013].

## How to Check <!-- role: check -->
*   **Visual Sign:** A dashboard full of small multiples for every pairwise comparison of a categorical variable.
*   **The Test:** Ask if all categories can fit on one plot with distinct colors.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Combine the data into a single view.
*   **Best Fix:** Use interaction (highlighting) to help focus on specific pairs, but leave the background context (the other classes) visible.
