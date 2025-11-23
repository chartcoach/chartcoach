---
id: prioritize-clarity-over-convention
title: Prioritize Clarity Over Convention
bibliography: references.bib
description: Select chart types based on audience comprehension rather than habit,
  aesthetics, or media trends to prevent misinterpretation.
labels:
- impact:clarity
- audience:novice
- chart:sankey
- chart:stacked-bar
- task:communicate
- complexity:low
---

## The Rule <!-- role: advice -->

Choose chart types based on audience comprehension, not habit, aesthetics, or industry convention.

## The Logic <!-- role: reason -->

Widely used or visually impressive charts do not guarantee understanding. High-dimensional visualizations often introduce cognitive load that obscures the data rather than revealing it.

*   **The Principle:** **Cognitive Fit.** Viewers must be able to map the visual representation to their mental model of the data without excessive effort.
*   **The Evidence:** Interviews and study findings demonstrate that complex chart types, such as Sankey diagrams or stacked bar charts, often overwhelm viewers. This complexity leads not just to confusion, but to active misinterpretation and wrong conclusions, particularly when applied to topics like voter behavior [@knoll_gulf_2025].

## Where to Apply <!-- role: context -->

Apply this rule when the primary goal is accurate information transfer rather than exploration or entertainment.

*   **User Goal:** Grasping the main insight quickly without training.
*   **Data Type:** Multi-dimensional data (e.g., flow data, part-to-whole over time) that tempts the use of complex visualizations.
*   **Audience:** General audiences, stakeholders with limited time, or viewers unfamiliar with advanced data visualization techniques.

## When to Break It <!-- role: exceptions -->

There are scenarios where convention or complexity is necessary.

*   **Scenario:** Domain-specific reporting (e.g., financial candlestick charts, scientific box plots).
*   **Reason:** The audience is trained to read these specific formats, and simplifying them would remove necessary technical nuance.

## The Price <!-- role: costs -->

Prioritizing simple clarity over complex conventions comes with social and aesthetic costs.

*   **The Sacrifice:** Visual novelty and "wow factor." The chart may look less sophisticated or "boring" compared to media-style graphics.
*   **The Risk:** Stakeholders may perceive the analysis as less rigorous because the presentation is less complex.

## Common Mistakes <!-- role: mistakes -->

Designers often conflate popularity with effectiveness.

*   **The Wrong Fix:** Using a Sankey diagram or complex stacked bar because it looks "data-rich" or resembles high-end journalism.
*   **Why it fails:** It forces the user to untangle the visual encoding before they can read the data, often resulting in the wrong conclusion.

## How to Check <!-- role: check -->

*   **Visual Sign:** Does the chart require a multi-paragraph caption or a complex legend to be understood?
*   **The Test:** Show the chart to a user for 10 seconds and ask them to state the conclusion. If they describe the *structure* ("It's a flow chart") rather than the *insight* ("Voters moved left"), the chart type has failed.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Add explicit annotations that narrate the data, guiding the user through the complexity.
*   **Best Fix:** Switch to a lower-dimensional chart type. Break a stacked bar into small multiple line charts, or convert a Sankey diagram into a simple bar chart comparing start and end states.
