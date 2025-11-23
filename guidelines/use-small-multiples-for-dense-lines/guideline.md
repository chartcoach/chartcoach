---
id: use-small-multiples-for-dense-lines
title: Split Overlapping Line Charts into Small Multiples
bibliography: references.bib
description: When line charts become cluttered 'spaghetti monsters,' split them into
  individual grids to improve readability.
labels:
- chart:line
- chart:small-multiples
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:general
---

## The Rule <!-- role: advice -->
When a line chart contains too many categories that overlap and create a "spaghetti monster," split the chart into a grid of separate, smaller charts (small multiples) rather than keeping them on a single axis.

## The Logic <!-- role: reason -->
Standard line charts become unreadable when many lines overlap significantly. By giving each line its own little panel, you preserve the trend information without the visual noise of intersection. According to [@muth_chart_types_guide_2025], this layout helps tidy up messy data while allowing the reader to see the shape of each category's development.

## Where to Apply <!-- role: context -->
*   **User Goal:** Showing developments over time for many entities simultaneously.
*   **Data Type:** Time series data with multiple categories (e.g., 5+ lines) that have similar value ranges or intersect frequently.
*   **Audience:** Mainstream audiences who need to distinguish individual trends clearly.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The goal is to compare specific values at a specific point in time across categories.
*   **Reason:** Splitting the axes makes it harder to compare the exact height of one line against another at the same distinct time point compared to a shared axis.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to instantly compare the absolute vertical position of lines against each other (e.g., seeing exactly when Line A crossed above Line B).
*   **The Risk:** It requires more screen space (a grid) compared to a single compact chart.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using different colors or symbols on a single crowded chart.
*   **Why it fails:** It turns into a "spaghetti monster" where individual lines are impossible to follow despite the colors [@muth_chart_types_guide_2025].

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you follow a single line from start to finish without your eye getting lost in other lines?
*   **The Test:** If you describe the chart as "messy" or "spaghetti," it needs splitting.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Convert the single chart into a "multiple lines" chart (small multiples) layout.
*   **Alternative:** If you only care about the start and end points, convert it to a slope chart or an arrow plot [@muth_chart_types_guide_2025].
