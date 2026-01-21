---
id: make-tooltips-self-explanatory-with-category-text
title: Write Tooltips That Restate What the Value Means
bibliography: references.bib
description: In tooltips, include the metric and context (not just the raw number)
  to reinforce what the chart shows.
labels:
- chart:interactive
- task:inspect
- visual:text
- impact:clarity
- data:quantitative
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

In tooltips, show values together with what they represent (metric + direction/context), not numbers alone.

## The Logic <!-- role: reason -->

Tooltips are a teaching moment: by restating the metric (e.g., “3.4% unemployed” instead of “3.4%”), you reduce ambiguity and repeatedly anchor readers to what the visualization encodes.

- **The Principle:** Reinforce meaning at the moment of interaction
- **The Evidence:** [@muth_text_in_data_visualizations_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Hover/inspect a mark to learn the exact value without misreading it
- **Data Type:** Any chart/map with hover tooltips; especially where multiple measures could be confused
- **Audience:** General readers, first-time viewers, or anyone encountering the chart out of surrounding article context [@muth_text_in_data_visualizations_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Tooltips are extremely space-constrained and already repeat the context elsewhere at the exact hover location.
  - **Reason:** Additional words may cause truncation or reduce scan speed; the tooltip must remain legible [@muth_text_in_data_visualizations_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Tooltips get longer.
- **The Risk:** Wordy tooltips can feel heavy, wrap awkwardly, or obscure nearby marks [@muth_text_in_data_visualizations_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing only a number (e.g., “+16%”).
  - **Why it fails:** Readers may forget what “+16%” refers to (revenue? unemployment? change since when?) [@muth_text_in_data_visualizations_2022].
- **The Wrong Fix:** Copying axis labels verbatim into tooltips without making a readable phrase.
  - **Why it fails:** Tooltips become cryptic instead of reinforcing meaning [@muth_text_in_data_visualizations_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** A tooltip value could be pasted into a chat message and become unclear (“3.4%” of what?).
- **The Test:** Read the tooltip out loud without looking at the rest of the chart; if it doesn’t make sense alone, add the missing context words [@muth_text_in_data_visualizations_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Append the metric noun to the value (e.g., “3.4% unemployed,” “+16% revenue”).
- **Best Fix:** Rewrite tooltip content as short, human-readable statements that restate the encoded measure and, where needed, the comparison baseline [@muth_text_in_data_visualizations_2022].
