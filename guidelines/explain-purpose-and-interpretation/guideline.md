---
id: explain-purpose-and-interpretation
title: Explicitly explain chart purpose and reading instructions
bibliography: references.bib
description: Provide text that defines the visualization's purpose and instructs the
  user on how to interpret the visual encodings.
labels:
- impact:accessibility
- impact:clarity
- audience:novice
- task:interpret
- complexity:cognitive
---

## The Rule <!-- role: advice -->
Do not assume your visualization is intuitive. You must explicitly explain the purpose of the chart and provide clear instructions on how to read, use, and interpret the specific visual design.

## The Logic <!-- role: reason -->
Visualizations often suffer from the "Curse of Knowledge," where creators overestimate the audience's ability to understand a design because the creator already understands the underlying logic [@xiong_curse_of_2020]. Standard accessibility guidelines often fail to necessitate explaining *how* to read a complex data visualization, focusing instead on simple labels [@elavsky_how_2022].
*   **The Principle:** Cognitive Accessibility (Understandable).
*   **The Evidence:** Research indicates that even simple data visualizations can present interpretation barriers; descriptive titles and supporting text significantly improve recognition and recall [@xiong_curse_of_2020].

## Where to Apply <!-- role: context -->
This guideline is a "Critical" heuristic within the Chartability framework and applies broadly to data interfaces [@elavsky_how_2022].
*   **User Goal:** Reducing cognitive load and ambiguity.
*   **Data Type:** Any data visualization, particularly those with complex encodings or interactive elements.
*   **Audience:** Users with cognitive disabilities, novices, or any user encountering a specific chart type for the first time.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Strictly none provided in the source context.
*   **Reason:** The source identifies this as a critical heuristic because standard compliance checkers often miss the gap between "labeled" and "understandable" [@elavsky_how_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate. Explanatory text, captions, or "how-to" overlays require space that might otherwise be used for the data graphic itself.
*   **The Risk:** If the explanation is verbose or poorly written, it may increase visual clutter rather than reducing cognitive load.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on standard WCAG criteria like "Identify Purpose" (1.3.6) or "Labels or Instructions" (3.3.2).
*   **Why it fails:** These standards often ensure elements are identified, but do not mandate an explanation of the *visual mechanics* (e.g., "The width of the bar represents X") necessary to interpret the data structure [@elavsky_how_2022].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for the absence of a descriptive title, subtitle, or help text.
*   **The Test:** Ask a user unfamiliar with the data: "How do you read this?" If they cannot immediately explain the relationship between the visual shapes and the data values, the heuristic is failed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a descriptive subtitle that summarizes the main takeaway (purpose).
*   **Best Fix:** Include a dedicated text section or annotation layer that explicitly describes how to read the chart (e.g., "Read this chart by comparing the height of the bars; taller bars indicate higher revenue") [@elavsky_how_2022].
