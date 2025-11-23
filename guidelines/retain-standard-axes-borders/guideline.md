---
id: retain-standard-axes-borders
title: Retain Explicit Axes and Borders
bibliography: references.bib
description: Users prefer standard chart anatomy over extreme minimalist reductions
  that remove structural elements.
labels:
- chart:bar
- visual:layout
- impact:clarity
- impact:preference
- audience:general
- complexity:basic
---

## The Rule <!-- role: advice -->
Do not remove standard structural elements—such as axis lines, ticks, or bounding borders—solely to maximize the data-ink ratio.

## The Logic <!-- role: reason -->
While design theory (specifically Tufte's) suggests that erasing non-data ink improves the graph, empirical evidence shows that users strongly dislike "extreme" minimalism.
*   **The Principle:** **User Preference for Familiarity.** Users associate standard chart anatomy with clarity and beauty.
*   **The Evidence:** In a study evaluating student preferences, a standard bar graph (Graph A) was rated significantly higher in beauty, clarity, and ease of use than Tufte's minimalist version (Graph D), which removed axis lines and used white space for grids. Even after performing tasks with the minimalist graph to gain familiarity, users still preferred the standard layout [@inbar_minimalism_2007].

## Where to Apply <!-- role: context -->
*   **User Goal:** General reporting and presentation where user acceptance and perceived beauty are important.
*   **Data Type:** Quantitative data presented in standard formats (e.g., bar charts).
*   **Audience:** Laymen, students, or general audiences who are not visualization experts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Specialized design for minimalist experts.
*   **Reason:** Designers might appreciate the theoretical elegance of high data-ink ratios, though the paper notes a "chasm" between designer and public preferences [@inbar_minimalism_2007].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You retain "redundant" ink that does not carry data values.
*   **The Risk:** The chart may appear slightly more "cluttered" or "traditional" compared to avant-garde design standards.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Erasing the X and Y axes lines and relying solely on the bars to define the space (Tufte's Graph D).
*   **Why it fails:** Users rated this specific configuration as having lower clarity and beauty, viewing it as "too simple" or unrecognizable [@inbar_minimalism_2007].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart look like it is floating in white space without anchoring lines?
*   **The Test:** Ask a user if the chart looks "unfinished" or "broken."

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Restore the baseline and vertical axis line.
*   **Best Fix:** Use a standard bar chart style with visible axes and tick marks, as this format received the highest subjective ratings [@inbar_minimalism_2007].
