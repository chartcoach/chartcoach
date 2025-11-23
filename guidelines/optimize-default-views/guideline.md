---
id: optimize-default-views
title: Select Default Views to Anchor Interpretation
bibliography: references.bib
description: Carefully choose the initial state of an interactive visualization because
  it acts as an anchor for user interpretation.
labels:
- visual:interactivity
- impact:engagement
- task:explore
- visual:layout
---

## The Rule <!-- role: advice -->
Choose the initial, default view of an interactive visualization strategically to emphasize the most critical message or data slice.

## The Logic <!-- role: reason -->
This is based on "procedural rhetoric" and the psychological concept of "anchoring." The default view provides an initial point of interpretation. Users are likely to base their subsequent exploration and conclusions on this initial anchor. Furthermore, default menus often guide users toward specific comparisons that the designer has already deemed interesting, rather than encouraging truly free exploration [@hullman_visualization_2011].

## Where to Apply <!-- role: context -->
*   **User Goal:** When guiding a user through a complex dataset with a specific narrative intent.
*   **Data Type:** High-dimensional data or large datasets requiring filtering/zooming (e.g., maps).
*   **Audience:** Users who may not have the time or expertise to explore every possible combination of variables.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Tools designed for pure, unbiased scientific analysis.
*   **Reason:** If the goal is to avoid biasing the analyst, a neutral or empty starting state (requiring user input to see anything) might be preferable to a curated default.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Neutrality.
*   **The Risk:** Users may never explore beyond the default view, missing other valid interpretations or contradicting data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Defaulting to the first alphabetical variable or a "zoomed out" view that shows nothing significant.
*   **Why it fails:** It fails to utilize the "anchoring" effect to provide immediate insight or engagement [@hullman_visualization_2011].

## How to Check <!-- role: check -->
*   **Visual Sign:** Open the visualization in a fresh window.
*   **The Test:** Does the very first screen communicate the core story without a single click?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Pre-select the most dramatic or representative category in dropdown menus.
*   **Best Fix:** Design a "cover view" that highlights a specific, compelling trend or comparison before allowing open exploration.
