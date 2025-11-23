---
id: label-horizontal-value-direction
title: Reinforce Horizontal Axis Direction
bibliography: references.bib
description: Explicitly annotate that the horizontal axis represents a quantity, not
  time, to prevent misinterpretation.
labels:
- chart:connected-scatterplot
- visual:axes
- task:reading
- impact:accuracy
- audience:novice
---

## The Rule <!-- role: advice -->
Explicitly remind viewers that the horizontal axis represents a value magnitude, not a timeline, and that "left" means "less," not "earlier."

## The Logic <!-- role: reason -->
Because standard line charts map time to the x-axis, viewers bring a strong prior expectation that the horizontal dimension represents time. This leads to errors where viewers misinterpret leftward movements as "going back in time" rather than a decrease in value.
*   **The Principle:** Axis Orientation Bias.
*   **The Evidence:** In drawing tasks, participants occasionally reversed the horizontal axis or confused the temporal flow because they conflated the x-axis with time [@haroz_connected_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Reading specific values for the variable plotted on the x-axis.
*   **Data Type:** Any connected scatterplot, specifically those where the x-variable decreases over time (moving right-to-left).
*   **Audience:** General public or those accustomed to standard time-series charts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Scientific contexts using phase portraits.
*   **Reason:** Expert audiences in physics or dynamics are already trained to read phase spaces where x is state, not time.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Minimalism. You need more forceful axis labels.
*   **The Risk:** Redundancy for expert users.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying on standard axis ticks at the bottom.
*   **Why it fails:** Viewers often ignore standard axis labels when scanning the overall shape; they need cues near the data or high-level titles [@haroz_connected_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** The line moves left, but the narrative implies growth/forward movement.
*   **The Test:** If a user says, "It went back," ask if they mean "back in time" or "value decreased."

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add arrows to the axis line itself pointing right with the label "Higher [Variable Name]."
*   **Best Fix:** Annotate specific points where the line moves left with text like "Income dropped in 2008," reinforcing that the leftward movement is a value change.
