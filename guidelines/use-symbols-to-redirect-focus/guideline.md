---
id: use-symbols-to-redirect-focus
title: Use Symbols to Redirect Focus
bibliography: references.bib
description: Use arrows or pointers to shift fixation to target objects, rather than
  as targets themselves.
labels:
- visual:symbols
- task:locate
- impact:guidance
- visual:annotations
---

## The Rule <!-- role: advice -->
Use learned symbols (like arrows) to direct the eye *away* from the symbol and onto a specific object or location.

## The Logic <!-- role: reason -->
Symbols act as attentional cues. Eye-tracking demonstrates that when a symbol like an arrow is revealed, fixations shift from the symbol itself to the object being pointed at [@faraday_designing_1997]. The viewer processes the meaning of the symbol (direction) and moves their attention accordingly. This makes arrows effective tools for "handing off" attention from one area to another.

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying a specific component in a crowded display.
*   **Data Type:** Dense diagrams, anatomical drawings, or scatterplots.
*   **Audience:** Users who need to find a "needle in a haystack."

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The arrow itself contains data (e.g., a vector field or flow magnitude).
*   **Reason:** In this case, the user needs to study the arrow's properties (length, width), not just where it points.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Adds visual clutter (ink) to the display.
*   **The Risk:** If the arrow points to empty space or an ambiguous group, attention dissipates.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a text label that says "Look at the bottom right."
*   **Why it fails:** This requires high-level cognitive processing (reading + spatial orientation) rather than the rapid, learned response to an arrow.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the user scanning randomly to find the object mentioned in the text?
*   **The Test:** Reveal the arrow. Does the user's eye immediately jump to the target object?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a bold arrow pointing to the target.
*   **Best Fix:** Animate the arrow appearing to actively trigger the attentional shift, then have it fade if it's no longer needed.
