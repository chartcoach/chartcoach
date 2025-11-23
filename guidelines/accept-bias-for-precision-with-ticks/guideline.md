---
id: accept-bias-for-precision-with-ticks
title: Add Reference Marks to Increase Precision
bibliography: references.bib
description: Add ticks and gridlines to improve overall precision, even though it
  introduces some bias.
labels:
- chart:bar
- visual:gridlines
- visual:ticks
- impact:precision
- impact:bias
---

## The Rule <!-- role: advice -->
Include reference marks (ticks, gridlines, or frames) to divide the visual space, accepting that this trade-off introduces minor biases around those marks in exchange for higher overall precision.

## The Logic <!-- role: reason -->
Visual references allow humans to categorize continuous space into smaller chunks (categorical perception), which increases memory capacity and reduces random error.
*   **The Principle:** Categorical Perception. Humans handle metric values better when they can divide continuous values into discrete categories (e.g., "above the half-mark").
*   **The Evidence:** The study suggests that while references cause "repulsion" (values are remembered as farther from the tick mark than they really are), the overall absolute error decreases because the references serve as anchors [@mccoleman_no_2021].

## Where to Apply <!-- role: context -->
*   **User Goal:** When the priority is minimizing the magnitude of error (precision).
*   **Data Type:** Continuous variables where exact recall is difficult.
*   **Audience:** General purpose visualization.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When avoiding specific directional bias is more important than general precision.
*   **Reason:** If it is politically or analytically dangerous for a value of 51% to be perceived as 55% (due to repulsion from the 50% tick mark), remove the reference to reduce the systematic bias [@mccoleman_no_2021].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Neutrality. You trade random noise (general error) for systematic bias (directional error).
*   **The Risk:** Data points will seem to "repulse" away from your grid lines.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Removing all gridlines to make the chart "clean."
*   **Why it fails:** This forces the user to rely solely on the start point of the bar, leading to larger estimation errors (roughly 10% of the value) [@mccoleman_no_2021].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the data area an empty void without guide rails?
*   **The Test:** Can you accurately guess the value of a bar in the middle of the chart without tracing your finger back to the axis?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a 50% grid line or major axis ticks.
*   **Best Fix:** Ensure tick marks are frequent enough to provide context but sparse enough to avoid excessive visual clutter.
