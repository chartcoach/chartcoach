---
id: functional-color-usage-small-multiples
title: Use Color for Categories or Highlights
bibliography: references.bib
description: In small multiples, repurpose color to highlight trends or groups rather
  than for differentiation.
labels:
- chart:small-multiples
- visual:color
- impact:highlight
- task:categorize
---

## The Rule <!-- role: advice -->
Do not use different colors to distinguish lines (e.g., "Blue is A, Red is B") because the panels already do that job. Instead, use color to categorize lines into groups (e.g., "Red for downwards trending") or to highlight specific panels of interest.

## The Logic <!-- role: reason -->
*   **The Principle:** Functional Minimalism.
*   **The Evidence:** Since each line has its own titled panel, a color legend is redundant. [@muth_small_multiple_line_charts_2024] advises repurposing the color channel to add an extra layer of information, such as grouping by behavior (rising vs. falling) or drawing the eye to outliers.

## Where to Apply <!-- role: context -->
*   **User Goal:** Seeing patterns across the whole dataset (e.g., "Most lines are trending down").
*   **Data Type:** Multiple categories that can be logically grouped.
*   **Audience:** Readers needing high-level summary insights.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** You are using "shadow lines" (background lines).
*   **Reason:** The foreground line usually needs a single consistent, high-contrast color to stand out against the gray background.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to assign a specific brand identity color to every single entity.
*   **The Risk:** Using too many semantic colors (e.g., 4 different groups) can confuse the reader without a legend.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assigning a unique random color to every single panel.
*   **Why it fails:** It creates a "fruit salad" effect that adds no meaning.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is every panel a different color of the rainbow for no data-driven reason?
*   **The Test:** If you turn the chart black and white, do you lose any *meaning*? If no, the rainbow colors were unnecessary.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Make all lines the same color (e.g., blue).
*   **Best Fix:** Color code by performance (e.g., Green for growth, Red for decline).
