---
id: employ-tacit-tutorials
title: Teach Interaction via Tacit Tutorials
bibliography: references.bib
description: Animate interactive elements during the narrative phase to subtly teach
  users how to use them.
labels:
- chart:interactive
- task:onboarding
- impact:usability
- visual:animation
- audience:novice
---

## The Rule <!-- role: advice -->
Do not rely solely on explicit instructions (e.g., "Click here to filter"). Instead, program the narrative introduction to automatically animate the interface controls (sliders, dropdowns) to demonstrate their function.

## The Logic <!-- role: reason -->
Users often ignore explicit help text. A "tacit tutorial" introduces functionality seamlessly by having the story "use" the interface.
*   **The Principle:** Observational Learning. When users see a slider move and the chart update simultaneously during the intro, they learn the cause-and-effect relationship without reading a manual.
*   **The Evidence:** [@segel_narrative_2010] highlight the "Budget Forecasts" example (Section 3.2), where the narrative manipulates the chart and slider. By the time the user takes control, "it is already clear to the user how to do this."

## Where to Apply <!-- role: context -->
*   **User Goal:** Learning to use a new or complex interactive tool.
*   **Data Type:** Interactive time-series, filtered maps, or parameterized simulations.
*   **Audience:** General public or "casual" users who are not familiar with visualization tools.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Standard UI Patterns.
*   **Reason:** If you are using standard web browser controls (like a simple scroll bar or standard hyperlink), a tutorial is unnecessary and patronizing.
*   **Scenario:** Expert Tools.
*   **Reason:** Power users of tools like Spotfire or Tableau do not need narrative animations to understand filtering.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Development complexity. It is harder to script the movement of UI widgets than to simply display a static chart.
*   **The Risk:** If the animation is too fast, the user might miss the connection between the moving slider and the changing data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Explicit Instruction.
*   **Why it fails:** Writing "Use the timebar to see people in Asia" (Section 3.5) is less effective than simply animating that transition first. The paper notes explicit instruction is often "under-utilized" or ignored.
*   **The Wrong Fix:** Static Screenshots.
*   **Why it fails:** Showing a picture of the tool in use doesn't convey the dynamic relationship between control and output.

## How to Check <!-- role: check -->
*   **Visual Sign:** During the "autoplay" or introductory sequence, do the input controls (sliders, buttons) move?
*   **The Test:** Watch the intro with your hands off the mouse. If the chart changes but the UI controls identifying *why* it changed remain static, you have failed this rule.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a "ghost" cursor or highlight effect over the button being "clicked" during the narrative sequence.
*   **Best Fix:** Script the actual UI components to update their state (e.g., move the slider handle) in sync with the narrative data updates.
