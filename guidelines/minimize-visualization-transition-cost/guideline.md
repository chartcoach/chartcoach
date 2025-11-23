---
id: minimize-visualization-transition-cost
title: Minimize Attribute Changes Between Slides
bibliography: references.bib
description: Maintain consistency across linear visualization sequences by changing
  only one data attribute at a time to reduce cognitive load.
labels:
- task:storytelling
- task:presentation
- visual:transition
- impact:comprehension
- audience:general
- source:academic-research
---

## The Rule <!-- role: advice -->
When sequencing visualizations in a linear presentation (like a slideshow), ensure that consecutive slides differ by as few data attributes as possible. Ideally, change only one dimension (e.g., time, independent variable, or dependent variable) per transition.

## The Logic <!-- role: reason -->
This guideline is based on the principle of *maintaining consistency* to preserve mental models. 
*   **The Principle:** Transformation Cost.
*   **The Evidence:** [@hullman_deeper_2013] propose a "transformation cost" function, where cost is the number of changes required to convert one visualization state to another. Their user studies confirmed that audiences consistently prefer transitions with lower transformation costs (e.g., changing only the time period is preferred over changing the time period *and* the region simultaneously). Lower costs make it easier for users to infer the connection between steps without explicit explanation.

## Where to Apply <!-- role: context -->
This applies to linear, slideshow-style narrative visualizations where the creator controls the sequence.
*   **User Goal:** Understanding the connection between two distinct visualization states.
*   **Data Type:** Multidimensional data presented sequentially (e.g., changing years, changing filters, switching measures).
*   **Audience:** Non-expert audiences or scenarios where explicit verbal narration is minimal.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Dramatic Rhetorical Shifts.
*   **Reason:** If the goal is to surprise the audience or emphasize a total disconnect between two scenarios, a high-cost transition (changing everything at once) might be rhetorically appropriate, provided explicit guidance (text or audio) bridges the gap [@hullman_deeper_2013].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may need more slides to tell the same story. Instead of jumping from "2010 Sales in US" to "2011 Profit in Asia," you must introduce intermediate steps.
*   **The Risk:** The presentation may feel slower or repetitive if the incremental steps are not meaningful.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Changing the chart type, the time period, and the measure simultaneously to "save space."
*   **Why it fails:** This creates a high transformation cost (e.g., Cost = 3), forcing the audience to re-orient completely, increasing the difficulty of inferring the narrative connection [@hullman_deeper_2013].

## How to Check <!-- role: check -->
*   **Visual Sign:** Place two consecutive slides side-by-side.
*   **The Test:** Count the differences. Did the time change? (1). Did the X-axis variable change? (1). Did the Y-axis measure change? (1). Did the filter/granularity change? (1). If the sum is greater than 1, the transition is "high cost."

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Duplicate the first slide and change only one attribute (e.g., keep the year, change the measure) before moving to the final state.
*   **Best Fix:** Decompose the narrative into single-step transitions. For example, to go from "US GDP" to "China Population," first transition to "China GDP" (change region), then to "China Population" (change measure).
