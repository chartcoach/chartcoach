---
id: color-by-narrative-role
title: Color Code by Narrative Function
bibliography: references.bib
description: Use color to group metrics based on their effect on the outcome (e.g.,
  increasing vs. decreasing factors).
labels:
- visual:color
- task:group
- impact:clarity
- chart:line
- data:categorical
---

## The Rule <!-- role: advice -->
Use distinct colors to identify the *role* a metric plays in your story (e.g., factors that increase values vs. factors that decrease them), rather than assigning random colors to every line.

## The Logic <!-- role: reason -->
Color clarifies the function of each panel in the sequence. For example, using orange for a trend that *reduces* population (lower fertility) and green for trends that *increase* population (lower mortality, higher life expectancy) creates a visual grouping that reinforces the narrative logic [@mintzer_sequential_storytelling_2024].

## Where to Apply <!-- role: context -->
*   **User Goal:** showing opposing forces or contributing factors.
*   **Data Type:** Metrics that have positive or negative impacts on a total.
*   **Audience:** Viewers who need to distinguish between conflicting or compounding trends.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-cardinality categorical data.
*   **Reason:** If you are comparing 10 distinct items that don't share a "role," grouping them by role is impossible.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Unique identity for specific metrics.
*   **The Risk:** Readers might confuse two different metrics (e.g., Life Expectancy and Infant Mortality) as being the same thing because they share a color.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Giving every single line a different, high-contrast color.
*   **Why it fails:** It creates visual noise and fails to show which metrics are conceptually related or working together.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do charts with similar impacts share the same color?
*   **The Test:** If you removed the text, could you still see which charts belong to the "positive influence" group and which belong to the "negative"?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Apply a shared color (e.g., Green) to all "positive" metrics and a contrasting color (e.g., Orange) to "negative" metrics.
*   **Best Fix:** Create a color palette based on the *function* of the data (e.g., Inputs=Blue, Output=Black; or Increase=Green, Decrease=Red).
