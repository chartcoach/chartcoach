---
id: provide-visual-progress-tracking
title: Visualize Narrative Progress
bibliography: references.bib
description: Use progress bars, timelines, or checklists to orient the reader within
  the story structure.
labels:
- chart:slideshow
- visual:navigation
- task:orient
- impact:usability
- visual:structure
---

## The Rule <!-- role: advice -->
Explicitly visualize how much of the story remains using a progress bar, timeline slider, or checklist tracker.

## The Logic <!-- role: reason -->
Narrative visualizations often function like slideshows. Users need to know their position in the sequence to feel comfortable exploring.
*   **The Principle:** Orientation and Navigation. These elements act as a map, preventing the feeling of being lost in data.
*   **The Evidence:** [@segel_narrative_2010] identify the "Progress Bar" and "Checklist Progress Tracker" as recurring visual structuring tactics (Section 3.2 Budget Forecasts, Section 3.4 Gapminder). They allow users to "navigate between slides" and provide a "reminder of what each section contains."

## Where to Apply <!-- role: context -->
*   **User Goal:** Consuming a linear or semi-linear data story.
*   **Data Type:** Sequential arguments, temporal data, or distinct topics (e.g., "Income," "Health," "Poverty").
*   **Audience:** Online readers with limited time/attention spans.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Single-Frame Explorers.
*   **Reason:** If the visualization is a single interactive dashboard (like a dashboard of current stock prices) with no narrative sequence, a progress bar is meaningless.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen Real Estate. Progress bars take up space that could be used for data.
*   **The Risk:** Linearity. Strong progress indicators imply a linear path, which might discourage random access exploration if not designed carefully.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Browser "Back/Forward" reliance.
*   **Why it fails:** Browser buttons don't show *how many* steps remain or what the steps are.
*   **The Wrong Fix:** Hidden Navigation.
*   **Why it fails:** "Click next to continue" links that only appear at the end of text paragraphs prevent users from jumping ahead or gauging length.

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you tell how many slides/sections are left at a glance?
*   **The Test:** If you took a screenshot of the middle of the story, could a stranger tell it was the middle?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add simple pagination (e.g., "Slide 3 of 10").
*   **Best Fix:** Use a "Checklist Structure" (Section 3.4) where the progress indicator also serves as a navigation menu, labeling the topics of upcoming sections.
