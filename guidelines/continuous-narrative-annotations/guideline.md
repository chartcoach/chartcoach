---
id: continuous-narrative-annotations
title: Link Panels with Continuous Text
bibliography: references.bib
description: Write chart titles or annotations that form a coherent sentence or paragraph
  when read across the panels.
labels:
- visual:text
- visual:annotation
- task:storytelling
- impact:narrative
- chart:small-multiples
---

## The Rule <!-- role: advice -->
Write text annotations or headers that read as a continuous narrative across the panels, connecting the charts into a sentence or paragraph.

## The Logic <!-- role: reason -->
Charts alone might look like distinct facts ("two numbers up, two done"). By writing a "strip" of text that runs across the panels, you guide the reader through the visualization as a deliberate sequence, "filling in the narrative" that explains how the data points relate [@mintzer_sequential_storytelling_2024].

## Where to Apply <!-- role: context -->
*   **User Goal:** Increasing the "bonkersness vibes" (emotional impact) of a change.
*   **Data Type:** Sequential data where the relationship between charts is not immediately obvious.
*   **Audience:** General audiences who need context to appreciate the magnitude of the numbers.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Exploratory dashboards.
*   **Reason:** If the user is expected to jump randomly between charts to find specific data points, linear text is distracting.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Neutrality.
*   **The Risk:** By writing a sentence, you force a specific interpretation. The user is less likely to form their own independent conclusions.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using standard, dry metric names as titles (e.g., "Fertility Rate", "Population").
*   **Why it fails:** It labels the data but doesn't explain the connection or the magnitude of the change.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do your chart headers read like a list (Item A, Item B) or a story (First this, then that)?
*   **The Test:** Read the text annotations out loud from left to right. Do they form a coherent grammatical sentence?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a subtitle above each chart that starts with a conjunction or linking verb (e.g., "But...", "And...", "Leading to...").
*   **Best Fix:** Rewrite the chart titles entirely to form a paragraph, using the charts as illustrations for the text.
