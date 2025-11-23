---
id: elicit-prediction-transfer
title: Elicit Graphical Predictions Before Showing Results
bibliography: references.bib
description: Ask users to draw their expectations of uncertainty to improve their
  reasoning about future scenarios.
labels:
- task:prediction
- interaction:drawing
- impact:learning
- impact:transfer
- audience:novice
---

## The Rule <!-- role: advice -->
Require users to graphically sketch their prediction of an experiment's uncertainty (the expected distribution of results) *before* revealing the actual observed data.

## The Logic <!-- role: reason -->
Active prediction forces users to confront their prior knowledge and assumptions. The act of drawing a distribution creates an implicit "gap" between their expectation and the reality when the data is revealed. This process specifically improves "transfer"—the ability to accurately estimate uncertainty in *new, unrelated* experiments later on [@hullman_imagining_2018].

*   **The Principle:** Active Learning / Prediction Effect.
*   **The Evidence:** Participants who graphically predicted the results of one study were significantly more accurate at estimating the replication uncertainty of a *different* study in a new domain compared to those who just viewed the results [@hullman_imagining_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Educational settings or scientific communication where the goal is to improve statistical reasoning and understanding of "replication crisis" or reliability.
*   **Audience:** Non-experts or readers of scientific reports who might otherwise ignore uncertainty measures.
*   **Interaction:** Interactive articles, dashboards, or educational tools.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Quick information retrieval.
*   **Reason:** Prediction adds friction and time. The study showed it helps with deep understanding (transfer), but it did not significantly improve simple *recall* of the specific chart shown compared to just viewing it [@hullman_imagining_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Time and effort. It requires active engagement from the user.
*   **The Risk:** High variance in efficacy. The study noted that the benefit varied between participants; some benefited greatly, others less so.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Asking for text-based predictions (e.g., "Type the mean").
*   **Why it fails:** The paper specifically focuses on *graphical* prediction of the full distribution. Text predictions do not force the user to think about the shape and spread of uncertainty in the same way.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the visualization static, or is there an input state?
*   **The Test:** Does the interface block the view of the "true" data until the user has interacted with the canvas?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a prompt asking "What do you think the range of values is?" before showing the chart.
*   **Best Fix:** Implement a "draw-your-guess" interface where users drag a curve or stack markers to define a distribution, then overlay the real data for comparison.
