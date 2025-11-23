---
id: explicitly-state-inferences-for-novices
title: Explicitly Represent Inferences for Low-Skilled Audiences
bibliography: references.bib
description: Low-graphicacy users struggle to derive main effects or complex inferences
  regardless of chart type; these must be stated explicitly.
labels:
- chart:any
- task:communicate
- visual:annotation
- impact:accessibility
- audience:novice
- complexity:basic
---

## The Rule <!-- role: advice -->
Do not rely on the chart format alone to convey main effects or complex inferences to low-skilled audiences; explicitly represent or state the inference.

## The Logic <!-- role: reason -->
Graphicacy (graphical literacy) acts as a filter for comprehension. High-skilled viewers can use the visual features of a graph (like bar groupings) to perform mental computations, such as calculating averages (main effects). Low-skilled viewers, however, often cannot make these inferences even when the format (like a bar graph) theoretically supports it.
*   **The Evidence:** [@shah_bar_2011] found that low-skilled viewers failed to identify main effects even when viewing bar graphs that facilitated the necessary mental averaging.

## Where to Apply <!-- role: context -->
*   **User Goal:** The user needs to understand a summary trend (e.g., "Overall performance increased") from a complex multivariate dataset.
*   **Audience:** General public, students, or audiences with low-to-moderate data literacy.
*   **Data Type:** Multivariate data containing interactions or noise that hides the main trend.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When testing the user's ability to read graphs (e.g., in an educational assessment).
*   **Reason:** Explicitly stating the inference removes the cognitive work required to derive it.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may clutter the display with additional text or annotation layers.
*   **The Risk:** If the explicit inference contradicts a visual illusion in the graph (e.g., a Simpson's paradox), the user may become confused by the mismatch between what they see and what they are told.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Simply switching from a line graph to a bar graph to help novices understand "averages."
*   **Why it fails:** Format changes mainly benefit users who already have the skills to exploit that format. Novices need the answer provided directly [@shah_bar_2011].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart require the user to mentally combine three or more bars to answer the question "Which group is better overall?"
*   **The Test:** Show the chart to a non-expert without the title/caption. Can they tell you the main takeaway? If not, you need explicit annotations.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a clear title or annotation summarizing the main effect (e.g., "Group A is faster on average").
*   **Best Fix:** Plot the specific inference (e.g., a separate bar showing the average) alongside the detailed data so no mental calculation is required.
