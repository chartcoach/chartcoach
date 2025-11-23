---
id: guide-visual-routine-entry
title: Guide the User's Starting Anchor Point
bibliography: references.bib
description: Direct attention to specific data points first to control how the user
  frames the relationship.
labels:
- task:compare
- impact:comprehension
- visual:position
- audience:student
- audience:novice
---

## The Rule <!-- role: advice -->
Design your chart to force the eye to the "Target" of the comparison first, rather than the "Referent." Use visual cues to designate which data point should be the starting anchor.

## The Logic <!-- role: reason -->
Extracting relationships from graphs (e.g., "Are there more blueberries than oranges?") is a serial process, not a parallel one. It functions like a "visual routine" where the viewer attends to items in a sequence. The item attended to first (the anchor point) frames the mental sentence. For example, looking at the taller bar first leads to the interpretation "The tall bar is on the left," whereas looking at the left bar first leads to "The left bar is taller." To ensure the "right" relationship is extracted, you must guide this order [@michal_visual_2017].

## Where to Apply <!-- role: context -->
*   **User Goal:** Verifying specific claims or learning specific relationships (e.g., STEM education).
*   **Data Type:** Comparison between two or more discrete values.
*   **Audience:** Students or audiences who need to extract a specific causal or relational narrative (e.g., "X is larger than Y").

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Open-ended data exploration.
*   **Reason:** If the goal is for the user to discover their own relationships or patterns, forcing a specific visual routine (and thus a specific sentence structure) biases the analysis.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Neutrality. By guiding the anchor point, you are heavily framing the interpretation.
*   **The Risk:** If you guide the user to an anchor point that makes the comparison computationally difficult (e.g., forcing them to start at a complex, low-saliency outlier), the visual routine may fail.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assuming users read graphs left-to-right like text.
*   **Why it fails:** Users often have idiosyncratic feature preferences (e.g., naturally looking at the *tallest* thing first, regardless of position). Relying solely on left-to-right positioning fails to override these strong natural biases [@michal_visual_2017].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the most visually dominant element the subject of your intended sentence?
*   **The Test:** Ask a user to describe the relationship in the chart. If you want them to say "A is bigger than B," but they say "B is smaller than A," you have likely failed to set 'A' as the primary anchor point.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the visual weight (contrast, saturation, or size) of the "subject" data point.
*   **Best Fix:** Use explicit annotations or directional cues (e.g., an arrow or a sentence header) to prime the visual routine before the user even saccades to the data bars.
