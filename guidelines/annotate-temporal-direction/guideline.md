---
id: annotate-temporal-direction
title: Annotate Temporal Direction Explicitly
bibliography: references.bib
description: Provide clear visual cues beyond simple arrows to indicate the flow of
  time in connected scatterplots.
labels:
- chart:connected-scatterplot
- task:reading
- visual:annotation
- impact:comprehension
- data:temporal
- audience:novice
---

## The Rule <!-- role: advice -->
Provide explicit text labels (dates) or visual encodings (gradients, line thickness) to indicate the direction of time; do not rely solely on arrows or reader intuition.

## The Logic <!-- role: reason -->
Readers have a strong bias toward left-to-right reading directions. In a connected scatterplot, time can move right-to-left ("backward") or vertically, violating this expectation.
*   **The Principle:** Directional Bias and Novelty.
*   **The Evidence:** In translation tasks, "reversed time" was a dominant error. Participants frequently struggled with "backward" diagonals, and arrows alone were not always sufficient to prevent misinterpretation of sequence [@haroz_connected_2016].

## Where to Apply <!-- role: context -->
This applies to any connected scatterplot, particularly those used in journalism or public-facing media.
*   **User Goal:** Understanding the sequence of events.
*   **Data Type:** Paired time series where the trend includes reversals (loops or right-to-left movement).
*   **Audience:** General audiences unfamiliar with the technique.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Strictly monotonic data.
*   **Reason:** If both variables only ever increase, the line will naturally move bottom-left to top-right, aligning with standard reading conventions.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual cleanliness. Adding start/end dates or text annotations adds clutter.
*   **The Risk:** Over-annotating can distract from the shape of the data (the loops and L-shapes).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a single arrow at the end of the line.
*   **Why it fails:** Users often miss the arrow or fail to track the path back to the beginning when the line crosses itself or reverses direction [@haroz_connected_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for line segments that move from right to left.
*   **The Test:** Ask a user to identify the starting point and the ending point of the line without reading the caption.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Label the "Start" (Year) and "End" (Year) explicitly directly on the line.
*   **Best Fix:** Use text annotations for key dates along the path, or use a visual gradient (e.g., line gets darker or thicker as time progresses) to reinforce the flow.
