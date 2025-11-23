---
id: annotate-data-directly
title: Annotate Data Directly
bibliography: references.bib
description: Integrate narrative text directly into the visualization rather than
  relying on separate articles or captions.
labels:
- chart:line
- visual:text
- impact:clarity
- task:explain
- visual:annotation
---

## The Rule <!-- role: advice -->
Place explanations, highlighted observations, and narrative points directly within the chart area (as annotations or tooltips) rather than separating them into a surrounding article.

## The Logic <!-- role: reason -->
Separating text and graphics increases cognitive load, requiring the user to split attention. Integrated messaging ensures the story is connected to the evidence.
*   **The Principle:** Spatial Contiguity / Multi-Messaging. Text clarifies visual elements, while visual elements support the text.
*   **The Evidence:** [@segel_narrative_2010] critique the "Minnesota Employment Explorer" (Section 3.5) because "the graphics are disconnected from the narrative," causing users to miss the story. Conversely, they praise the "Steroids" example (Section 3.1) for using "shaded annotations" and pointers to explicitly link text to data spikes.

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding specific trends, outliers, or causal events in the data.
*   **Data Type:** Time series with specific events (e.g., "War begins," "Policy change") or scatterplots with interesting outliers.
*   **Audience:** Readers who need interpretation, not just raw data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Small Multiples / Sparklines.
*   **Reason:** If you have 50 small charts, annotating every single one creates clutter.
*   **Scenario:** Pure Data Discovery.
*   **Reason:** If the goal is strictly unbiased analysis, editorial annotations might be seen as leading the witness.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Cleanliness. Annotations clutter the chart area.
*   **The Risk:** Occlusion. Text boxes might cover up other data points.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** A long caption below the chart.
*   **Why it fails:** The user has to look down to read, then up to find the data point, then down again.
*   **The Wrong Fix:** Generic "Info" buttons.
*   **Why it fails:** Users often don't click them. The information should be visible by default or triggered by relevant interaction (hover).

## How to Check <!-- role: check -->
*   **Visual Sign:** Is your text in a column on the left and your chart on the right?
*   **The Test:** Remove the text column. Does the chart still make sense? If no, the chart is not self-sufficiently annotated.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use arrows or lines to connect your existing text to the specific data points they describe.
*   **Best Fix:** Embed the text into the coordinate space of the visualization (e.g., "In 2015, Africa will account for...") so it appears at the relevant data coordinates.
