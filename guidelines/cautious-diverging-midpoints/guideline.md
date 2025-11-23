---
id: cautious-diverging-midpoints
title: Monitor Accuracy at the Midpoint of Diverging Scales
bibliography: references.bib
description: Diverging colormaps may suffer from reduced accuracy when comparing values
  across the central neutral point.
labels:
- visual:color
- chart:heatmap
- type:diverging
- task:compare
---

## The Rule <!-- role: advice -->
Be cautious when users must compare values that straddle the neutral center of a diverging colormap (e.g., crossing from blue to orange).

## The Logic <!-- role: reason -->
While diverging maps are composed of two single-hue maps, the transition point introduces a hue boundary that can hinder relative distance judgments.
*   **The Principle:** Categorical Perception / Hue Boundaries.
*   **The Evidence:** The diverging *BlueOrange* colormap exhibited increased error rates specifically for comparisons that straddled the mid-point, performing worse than the pure single-hue colormaps it was composed of [@liu_somewhere_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurately judging whether a value slightly above the mean is closer to the mean than a value slightly below the mean.
*   **Data Type:** Data with a meaningful zero-point or average (diverging data).
*   **Audience:** General users.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The primary task is distinct categorization (Positive vs. Negative) rather than precise distance measurement across zero.
*   **Reason:** If the user only needs to know "is it A or B?" rather than "how far is A vs B?", the hue distinctness helps.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Prioritizing distance accuracy across the center might require using a continuous multi-hue map, which loses the semantic meaning of the "neutral" center.
*   **The Risk:** Users might lose the immediate "good vs bad" or "above vs below" signal provided by distinct hues.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a hard, sharp cut between hues at the center.
*   **Why it fails:** This exacerbates the categorization effect, making it even harder to judge distances near the boundary.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is there a "dead zone" or confusing transition in the middle of the chart?
*   **The Test:** Select a value slightly positive and a value slightly negative. Is it easy to tell which one is further from zero?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Ensure the central neutral color (often white or gray) spans a wide enough luminance range to soften the hue transition.
*   **Best Fix:** If distance judgment across the center is critical, consider if a sequential colormap might be more appropriate, or ensure the diverging arms ramp linearly in luminance.
