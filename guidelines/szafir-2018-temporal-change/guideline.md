---
id: szafir-2018-temporal-change
title: Visualize Change Staticly to Overcome Change Blindness
bibliography: references.bib
description: Use static encoding methods like juxtaposition or superposition instead
  of animation for precise temporal analysis.
labels:
- visual:animation
- task:compare
- data:temporal
- impact:memory
- bias:change-blindness
---

## The Rule <!-- role: advice -->
Prioritize static methods—Juxtaposition, Superposition, or Explicit Encoding—over animation when users need to identify and compare changes across time.

## The Logic <!-- role: reason -->
Animation induces "change blindness." Users can only track 3-4 moving points simultaneously. If they aren't looking at a specific point when it changes, they miss the information entirely. Our working memory is too limited to recall precise previous states during an animation.
*   **The Principle:** Change Blindness & Limited Working Memory.
*   **The Evidence:** [@szafir_good_2018] notes that animation helps identify high-level patterns but blinds people to specific changes in the rest of the dataset.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing values across time steps or tracking specific trajectories.
*   **Data Type:** Time-series data or multi-frame datasets.
*   **Audience:** Analysts needing to make precise comparisons.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Narrating a high-level story or guiding attention.
*   **Reason:** Animation is effective for engagement and storytelling (e.g., Hans Rosling's GapMinder) if the presenter verbally directs the audience's attention to the specific area of change [@szafir_good_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Static methods often require more screen space (juxtaposition) or suffer from clutter (superposition).
*   **The Risk:** Over-plotting or "hairballs" if too many time steps are superimposed.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Looping the animation indefinitely.
*   **Why it fails:** Users still have to guess where to look each time; they cannot see the whole picture simultaneously.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the user have to "remember" what the chart looked like 5 seconds ago to answer a question?
*   **The Test:** Pause the animation. Can the user still see the trajectory or the magnitude of change? If not, the design relies on memory.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** **Juxtaposition** (Place time steps side-by-side aka Small Multiples).
*   **Alternative Fix:** **Superposition** (Layer multiple time points on the same axes, using trails/traces).
*   **Best Fix:** **Explicit Encoding** (Calculate the change/difference and visualize that value directly) [@szafir_good_2018].
