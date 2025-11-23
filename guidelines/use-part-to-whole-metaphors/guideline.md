---
id: use-part-to-whole-metaphors
title: Use Part-to-Whole Metaphors for Proportions
bibliography: references.bib
description: Use pie charts or stacked bars when the goal is to explicitly convey
  that a value is part of a whole.
labels:
- chart:pie
- chart:stacked-bar
- task:part-to-whole
- visual:angle
- visual:area
- impact:clarity
---

## The Rule <!-- role: advice -->
When the primary message is that a value is a portion of a total, prefer charts that explicitly encode this containment (like pie charts or stacked bars) over more "precise" alternatives like separate bar charts.

## The Logic <!-- role: reason -->
While separate bars are more precise for comparing lengths, they fail to visually communicate the concept of a "whole."
*   **The Principle:** **Semantic Resonance/Metaphor**. Specific visual forms carry semantic associations. The pie chart and stacked bar explicitly convey the "part-to-whole" metaphor through containment and summation, which separate bars do not [@bertini_why_2020].
*   **The Evidence:** [@bertini_why_2020] argue that ranking channels purely by precision (where angle/area are lower than position) is misleading here. If the concept to be conveyed is "X is part of Y," the pie chart provides a better cognitive fit than a bar chart, despite being harder to read precisely.

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding the composition of a total (e.g., market share, budget allocation).
*   **Data Type:** Proportions or percentages summing to 100%.
*   **Audience:** Audiences needing to grasp the *concept* of the proportion rather than the exact decimal value.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Precise Comparison of Similar Slices.
*   **Reason:** If the user needs to know if slice A (24%) is strictly larger than slice B (23%), a pie chart fails. Use a bar chart and sacrifice the part-to-whole metaphor for precision [@bertini_why_2020].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision. It is harder to visually estimate the ratio of two areas or angles than two aligned lengths.
*   **The Risk:** Small differences between categories will be indistinguishable.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Exploding the pie chart or using a 3D pie chart.
*   **Why it fails:** This distorts the metaphor and the data.
*   **The Other Wrong Fix:** Replacing all pie charts with bar charts dogmatically.
*   **Why it fails:** You lose the immediate visual signal that "these parts add up to one total" [@bertini_why_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do you have a bar chart where the user has to do mental math to realize the bars represent a composition of a total?
*   **The Test:** Can the user instantly see that the data represents a finite resource (like 100% of a budget)?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Stack the bars (Stacked Bar Chart).
*   **Best Fix:** Use a Pie Chart or Donut Chart if the number of categories is small and the part-to-whole relationship is the primary message.
