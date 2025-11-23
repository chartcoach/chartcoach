---
id: match-color-scale-to-narrative-focus
title: Match Color Scale to Narrative Focus
bibliography: references.bib
description: Choose sequential scales to highlight high values, and diverging scales
  to highlight extremes at both ends.
labels:
- visual:color
- impact:storytelling
- task:emphasize
- chart:map
---

## The Rule <!-- role: advice -->
Choose your color scale based on the story you want to tell: use a **sequential scale** to emphasize only the highest values, and use a **diverging scale** to emphasize both the lowest and highest values simultaneously.

## The Logic <!-- role: reason -->
Color scales are an editorial choice that dictate where the eye is drawn.
*   **The Principle:** Visual Weight.
*   **The Evidence:** As noted by Gregor Aisch in the source text, "Sequential tells a different story." A sequential map of internet usage highlights only the "winners" (high usage), whereas a diverging map highlights the disparities by visually pushing the low-usage areas into a contrasting color (e.g., red for low, blue for high), making both extremes equally visible [@muth_diverging_vs_sequential_2021].

## Where to Apply <!-- role: context -->
*   **User Goal:** Editorializing or emphasizing specific data points.
*   **Audience:** Readers who need to understand specific patterns (e.g., "Where is usage highest?" vs. "Where is the divide?").

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Neutral Reporting.
*   **Reason:** If the goal is strictly to show magnitude without emphasizing the lack of magnitude, a sequential scale is the standard default.

## The Price <!-- role: costs -->
*   **The Risk:** Using a diverging scale to emphasize low values (e.g., coloring low internet usage red) adds a value judgment (red = bad/danger) that might not be intended.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a sequential scale when the story is about the *lack* of something.
*   **Why it fails:** On a light background, low values in a sequential scale often fade into the background (becoming white or light grey), causing the reader to overlook the "empty" areas [@muth_diverging_vs_sequential_2021].

## How to Check <!-- role: check -->
*   **The Test:** Look at the "low" values in your visualization. Are they important to your story?
    *   If yes, and they are invisible/faded: You need a diverging scale.
    *   If no, and they are distracting: You need a sequential scale.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Swap the palette type in your tool settings.
*   **Best Fix:** Re-evaluate the chart title. If the title discusses "The Digital Divide," use diverging. If the title is "High Internet Adoption," use sequential.
