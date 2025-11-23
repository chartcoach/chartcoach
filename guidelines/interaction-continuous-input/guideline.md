---
id: interaction-continuous-input
title: Use Continuous Inputs for Distribution Drawing
bibliography: references.bib
description: When asking users to draw distributions, use continuous line-dragging
  tools over discrete item-stacking.
labels:
- interaction:input
- visual:animation
- task:creation
- impact:satisfaction
- impact:speed
---

## The Rule <!-- role: advice -->
When designing interfaces for users to input or sketch probability distributions, use continuous interaction methods (like dragging a line to shape a curve) rather than discrete methods (like clicking to add individual balls to bins).

## The Logic <!-- role: reason -->
Users perceive continuous drawing tools as more expressive and efficient. They allow users to shape a distribution roughly 30% faster and with higher reported satisfaction than discrete "stacking" interfaces. Even if the final output is meant to be discrete, the *input* mechanism should feel continuous [@hullman_imagining_2018].

*   **The Principle:** Interaction Efficiency / Expressiveness.
*   **The Evidence:** In the design space exploration, continuous probability interfaces (e.g., line-drag, pull-up) outperformed discrete interfaces (e.g., balls-and-bins) in terms of satisfaction scores (20 point increase), speed (0.71x the time), and accuracy of replication [@hullman_imagining_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Eliciting priors, asking for predictions, or letting users sketch data shapes.
*   **Data Type:** Probability distributions or frequency histograms.
*   **Audience:** General users (MTurk workers in the study) who may find repetitive clicking (discrete input) tedious.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Teaching the specific concept of "accumulation" or discrete sampling.
*   **Reason:** If the pedagogical goal is to force the user to feel the weight of every single data point (e.g., "building" a dataset one by one), the friction of a discrete interface might be a desirable "desirable difficulty."

## The Price <!-- role: costs -->
*   **The Sacrifice:** Users might create distributions that are "too smooth" or idealized, potentially masking the lumpiness of real small-sample data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "click to add" interface for 50+ items.
*   **Why it fails:** The study found that discrete interfaces with many outcomes (50-100) were slow and tedious. Users preferred dragging handles or lines [@hullman_imagining_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the user have to click 20 times to build a bar?
*   **The Test:** Measure "time to completion" for drawing a standard bell curve. If it requires repetitive distinct actions, it violates this rule.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If using bars/bins, allow "painting" (drag to fill) rather than single clicks.
*   **Best Fix:** Implement a spline-based or handle-based curve manipulation tool that generates the underlying distribution values.
