---
id: align-viz-with-mental-schema
title: Align Visualization Structure with Mental Schemas
bibliography: references.bib
description: Choose visualization types that match the user's internal mental model
  and the specific task to reduce working memory load.
labels:
- impact:cognitive-load
- task:decision-making
- psychology:mental-models
- complexity:intermediate
---

## The Rule <!-- role: advice -->
Select a visualization format that spatially matches the user's mental schema for the problem. Minimize the number of "mental transformations" (rotations, sorting, or reinterpretations) the user must perform to answer their question.

## The Logic <!-- role: reason -->
This concept is known as "Cognitive Fit." When a visualization mismatches the user's mental task (e.g., using a distance-based graph for a containment-based logic problem), the user must employ Type 2 processing—slow, effortful, working-memory-intensive thought—to bridge the gap. [@padilla_decision_2018] highlights that performance is fastest and most accurate when the visual structure aligns with the decision-making component, allowing users to rely on faster Type 1 processing.

*   **The Principle:** Cognitive Fit / Schema Matching
*   **The Evidence:** [@padilla_decision_2018] cites Vessey & Galletta (1991) showing that spatial tasks are faster with graphs and symbolic tasks are faster with tables. Similarly, Tversky et al. (2012) showed that route selection improved when the visual links (thickness vs. containment) matched the conceptual definition of the connection (speed vs. security).

## Where to Apply <!-- role: context -->
*   **User Goal:** Solving specific logic problems or making defined comparisons.
*   **Data Type:** Network data, financial data, or spatial routing.
*   **Audience:** All users, but especially those with lower working memory capacity, as they suffer more from mismatches.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Educational contexts or "Desirable Difficulty."
*   **Reason:** If the goal is to force the user to learn a *new* schema or deeply understand the underlying data structure, a mismatch can force them to slow down and engage Type 2 processing deliberatively.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may need to create multiple views of the same data for different tasks (e.g., a table *and* a chart).
*   **The Risk:** A visualization that fits one task perfectly (e.g., comparing trends) may fit another task poorly (e.g., reading specific values), frustrating users with multi-faceted goals.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Teaching the user how to read a mismatched chart through extensive legends or instructions.
*   **Why it fails:** It relies on "knowledge-driven processing" which requires working memory. As soon as the user is stressed or tired, they may revert to the intuitive (but wrong) reading of the graphic.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the user have to write down intermediate numbers or trace lines with their finger?
*   **The Test:** Ask the user to describe the relationship between two data points. If they use words that contradict the visual geometry (e.g., "A is 'inside' B" while looking at a line chart), there is a mismatch.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reorient axes or sort data to match the likely question (e.g., sort a bar chart by value if the task is "find the max").
*   **Best Fix:** Change the chart type entirely to match the metaphor (e.g., switch from a node-link diagram to a Euler diagram if the task involves set containment).
