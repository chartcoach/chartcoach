---
id: guide-attention-via-salience
title: Highlight Key Data to Guide Attention
bibliography: references.bib
description: Use visual salience (color, size, contrast) to direct the viewer's eye
  to the most important comparison.
labels:
- visual:color
- visual:contrast
- task:focus
- impact:storytelling
- chart:all
---

## The Rule <!-- role: advice -->

Use visual salience—such as a bright color against neutral colors, or a unique shape—to highlight the specific data points or comparisons that matter most. Combine this with text annotations near the highlight.

## The Logic <!-- role: reason -->

The visual system is drawn to "salient" objects—those that stand out from their neighbors (e.g., a red poppy in a green field). Because viewers don't always know which of the many possible comparisons to prioritize, designers must use salience to guide attention to the relevant information.

*   **The Principle:** Visual Salience / Pop-out Effect
*   **The Evidence:** Salient objects (like a blue bar surrounded by yellow bars) automatically attract attention, allowing designers to "tell viewers what to see" [@zacks_designing_2020].

## Where to Apply <!-- role: context -->

*   **User Goal:** Communicating a specific insight or story within a complex dataset.
*   **Data Type:** Any chart with multiple data points where one subset is more important.
*   **Audience:** Viewers who need to understand the "main point" quickly without exploring the entire dataset.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Exploratory Data Analysis tools.
*   **Reason:** If the goal is to let the user discover their own patterns, enforcing a specific focal point via salience might bias their analysis.

## The Price <!-- role: costs -->

*   **The Sacrifice:** Highlighting one element necessarily pushes others into the background, potentially reducing the visibility of secondary data.
*   **The Risk:** Over-highlighting (making everything bold/bright) results in no salience at all and visual chaos.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Making all bars different colors (rainbow palette) to make them "distinct."
*   **Why it fails:** If everything is distinct, nothing is salient. Salience requires contrast against a uniform background [@zacks_designing_2020].

## How to Check <!-- role: check -->

*   **Visual Sign:** Is the most important data point immediately distinguishable from the rest?
*   **The Test:** Show the graph for 1 second. Ask the viewer what they looked at first. If it wasn't the key data point, the salience is too low.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Gray out the "context" data and use a bright color only for the "signal" data.
*   **Best Fix:** Add a text annotation directly pointing to the highlighted element to explicitly guide the interpretation [@zacks_designing_2020].
