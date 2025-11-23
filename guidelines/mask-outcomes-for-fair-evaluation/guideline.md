---
id: mask-outcomes-for-fair-evaluation
title: Mask Outcomes When Evaluating Decisions
bibliography: references.bib
description: To fairly evaluate a past decision or forecast, hide the subsequent outcome
  data to prevent hindsight bias.
labels:
- data:temporal
- task:assessment
- impact:bias-reduction
- chart:line
---

## The Rule <!-- role: advice -->
When using a visualization to evaluate the quality of a past decision or prediction (e.g., a stock trade, a medical diagnosis, or a project timeline), initially hide the data representing the eventual outcome. Reveal the outcome only after the user has assessed the situation based on the data available at the time.

## The Logic <!-- role: reason -->
*   **The Principle:** Hindsight Bias.
*   **The Evidence:** @camerer_curse_1989 notes that "when one looks backward, events seem to have been more predictable than they were." Knowing the outcome causes people to exaggerate what was knowable at the time. This bias interferes with decision quality evaluation because "principals will tend to think that ex ante optimal decisions with unfavorable outcomes were nonoptimal."

## Where to Apply <!-- role: context -->
*   **User Goal:** Post-mortem analysis, performance reviews, or educational storytelling (e.g., "Can you spot the crash?").
*   **Data Type:** Time-series data or progressive project states.
*   **Audience:** Managers, auditors, or students learning to diagnose patterns.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Showing historical trends for general context.
*   **Reason:** If the goal is simply to show "what happened" rather than to judge "was the decision correct at the time," the bias is irrelevant.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Narrative flow. Hiding the ending requires interaction or stepped reveals (animation), which is slower than a static image.
*   **The Risk:** The user may feel frustrated by the lack of immediate closure or the "quiz" format.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing the full timeline and asking the user to "ignore what they know" about the crash/success at the end.
*   **Why it fails:** The paper argues that agents are "unable to ignore their better information when they should" [@camerer_curse_1989]. Once the outcome is seen, it cannot be cognitively ignored.

## How to Check <!-- role: check -->
*   **Visual Sign:** A line chart showing a drop in sales at $t=10$, where the user is asked to evaluate a decision made at $t=5$.
*   **The Test:** Cover the right side of the chart. Does the decision at $t=5$ look different without the future knowledge?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use a "curtain" or annotation to physically block the future data on the chart until the evaluation is made.
*   **Best Fix:** Design an interactive "stepper" where data points are plotted one by one, forcing the viewer to experience the uncertainty of the historical moment before seeing the result.
