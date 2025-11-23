---
id: pair-deltas-with-context
title: Preserve Absolute Values When Showing Deltas
bibliography: references.bib
description: Direct delta encodings strip context; designs must balance efficient
  relation perception with the availability of original values.
labels:
- chart:dashboard
- task:contextualize
- impact:comprehension
- design:layout
---

## The Rule <!-- role: advice -->
Do not replace absolute values with delta encodings entirely; provide the original individual data values alongside the differences whenever context is required.

## The Logic <!-- role: reason -->
Direct delta encoding optimizes for the *relation* between values but destroys the information regarding the *state* of values.
*   **The Principle:** Loss of Context. A delta chart shows a change of +10, but hides whether that change was from 0 to 10 or 100 to 110.
*   **The Evidence:** The paper highlights that while deltas improve relational processing by 25-95%, they "remove the context of the individual data values." Insights tied to the absolute values (e.g., filtering by a threshold) are impossible with delta-only displays [@nothelfer_measures_2020].

## Where to Apply <!-- role: context -->
*   **User Goal:** Exploratory data analysis where the viewer does not know ahead of time whether the absolute status or the rate of change is more important.
*   **Application:** Dashboards and detailed reports.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Space-constrained interfaces (e.g., mobile/smartwatch) where the change is the *only* relevant metric (e.g., a stock ticker showing daily gain).
*   **Reason:** If screen real estate does not permit both, and the relation is the primary task, the efficiency gain of the delta outweighs the loss of context.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen Real Estate. Showing both absolute values and differences requires significantly more space.
*   **The Risk:** "Combinatorial explosion." If you have multiple data series, showing deltas for every possible pairing creates visual clutter [@nothelfer_measures_2020].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing only the delta chart to "save space" and removing the base chart.
*   **Why it fails:** Users lose the ability to assess the significance of a change relative to the baseline (e.g., a 5% growth is different for a startup vs. a giant corporation).

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the chart. Can you tell the specific value of the data point *before* the change occurred?
*   **The Test:** Ask, "What was the sales figure for March?" If the chart only shows "March was +$5k compared to February," and you can't answer the question, the rule is broken.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use tooltips to reveal absolute values on hover over delta bars.
*   **Best Fix:** Use a design that visualizes both, such as grouped bars with difference overlays, or juxtaposing the absolute value chart with a smaller difference chart [@nothelfer_measures_2020].
