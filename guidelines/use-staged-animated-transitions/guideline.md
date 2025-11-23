---
id: use-staged-animated-transitions
title: Stage Complex Animated Transitions
bibliography: references.bib
description: Break complex visual changes into sequential steps to prevent user confusion.
labels:
- chart:scatter
- visual:animation
- impact:cognition
- task:transition
- complexity:advanced
---

## The Rule <!-- role: advice -->
When morphing between different chart types or view perspectives, break the animation into distinct stages rather than changing everything at once.

## The Logic <!-- role: reason -->
Simultaneous changes in position, scale, and shape are difficult for the human brain to track.
*   **The Principle:** Object Constancy. Staging allows the user to track elements as they transform, maintaining the mental link between "Item A in Chart 1" and "Item A in Chart 2."
*   **The Evidence:** [@segel_narrative_2010] highlight the "Gapminder" example (Section 3.4 & Fig. 5), where a transition from a histogram to a scatterplot is explicitly staged: markers move first, then axes change, or vice versa.

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding how one view of data relates to another (e.g., "How does this list of countries relate to this map?").
*   **Data Type:** Multivariate data where the same entities (e.g., countries, players) are represented in different coordinate systems.
*   **Audience:** Users who need to understand the provenance of the data points.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Simple Time Steps.
*   **Reason:** If you are simply updating a line chart for the next year, a direct interpolation is sufficient. Staging is for structural changes (Section 2.2).
*   **Scenario:** "Cut" Transitions.
*   **Reason:** If the two views are unrelated (Section 2.2, "non-sequitur"), a staged morph implies a relationship that doesn't exist.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Time. Staged animations take longer to complete than direct morphs or hard cuts.
*   **The Risk:** Impatience. If users navigate frequently, long transition times can become frustrating.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** A linear interpolation (direct morph) of all properties at once.
*   **Why it fails:** Points fly across the screen in chaos ("spaghetti plot" effect) making it impossible to track individual items.
*   **The Wrong Fix:** Hard Cuts.
*   **Why it fails:** The user loses context and has to re-scan the entire image to find the data points they were looking at.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the transition look like a swarm of bees?
*   **The Test:** Pick one specific data point. Can you easily keep your eyes locked on it during the entire transition without guessing where it went?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Slow down the animation significantly.
*   **Best Fix:** Serialize the transition. For example, if moving from a map to a scatterplot: (1) Move dots to x-positions, (2) Move dots to y-positions, (3) Fade in axes.
