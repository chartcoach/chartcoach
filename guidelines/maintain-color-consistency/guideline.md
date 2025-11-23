---
id: maintain-color-consistency
title: Reuse Colors for the Same Variables Across Charts
bibliography: references.bib
description: Maintain color consistency for the same variables throughout a document
  or article.
labels:
- impact:consistency
- visual:color
- task:identify
- scope:multi-chart
---

## The Rule <!-- role: advice -->
If you use a specific color for a variable in one chart (e.g., blue for "unemployment rate"), use that same color for the same variable in subsequent charts. Conversely, if you change variables, change colors.

## The Logic <!-- role: reason -->
When a color is assigned to a variable, it becomes "taken" in the reader's mind for that context. Changing the meaning of a color mid-article confuses readers and decreases comparability. Consistent usage allows readers to carry their understanding from one visualization to the next without relearning the legend [@muth_colors_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Reading a report, dashboard, or article with multiple visualizations.
*   **Data Type:** Recurring metrics or categories (e.g., GDP, specific countries).
*   **Audience:** Readers consuming a narrative or multi-part report.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The charts are completely unrelated and appear in different, disconnected sections.
*   **Reason:** If there is no narrative flow connecting them, the cognitive link might not form.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You have a limited palette available for new variables in the same document.
*   **The Risk:** You might run out of distinct colors if tracking many variables.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using the same nice blue for Unemployment in Chart 1 and GDP in Chart 2.
*   **Why it fails:** The reader subconsciously assumes the blue line in Chart 2 is still Unemployment.

## How to Check <!-- role: check -->
*   **Visual Sign:** Two charts side-by-side using the same color for different things.
*   **The Test:** Review the entire document. If "France" is blue in chart A, is it blue in chart B? If "France" is blue in chart A, is "Germany" blue in chart B?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Pick a different hue for the new variable in the second chart.
*   **Best Fix:** Define a project-wide style guide assigning specific hex codes to specific recurring metrics.
