---
id: clarify-interactive-context-and-announce-status-messages
title: Explain Interactive Context and Announce Status Changes
bibliography: references.bib
description: Clearly describe how an interactive chart affects (or is affected by)
  other UI elements, and provide programmatically detectable status messages for resulting
  changes.
labels:
- chart:interactive
- task:interact
- visual:layout
- impact:accessibility
- data:multivariate
- audience:screen-reader
- principle:understandable
- source:chartability
---

## The Rule <!-- role: advice -->

If an interactive chart can change the page’s logic or layout, or is controlled by other UI inputs/parameters, explicitly describe those relationships in text, and emit status messages for resulting updates that assistive technologies can detect without requiring the user to navigate.

## The Logic <!-- role: reason -->

Interactive visualizations can create hidden dependencies (controls → chart, chart → other content) that are ambiguous unless made explicit; users—especially screen reader users—also need to be informed of dynamic updates without losing their place or moving focus. Chartability frames this as an Understandable requirement for minimizing ambiguity and cognitive load in interactive contexts [@elavskyHowAccessibleMy2022]. WCAG’s guidance on status messages explains that important updates must be programmatically conveyed so assistive technologies can announce them without forced navigation [@w3c_understanding_status].

- **The Principle:** Make interaction effects and state changes explicit and programmatically perceivable.
- **The Evidence:** [@elavskyHowAccessibleMy2022], [@w3c_understanding_status]

## Where to Apply <!-- role: context -->

This advice is designed for interactive, stateful data experiences where actions or controls change what is shown elsewhere.

- **User Goal:** Understanding what changed after an interaction, and why.
- **Data Type:** Any chart driven by external parameters (filters, dropdowns, sliders) or that triggers updates (filtering, re-sorting, updating text/summary panels, changing other views).
- **Audience:** Users who need explicit instructions and feedback, including screen reader users relying on programmatic notifications [@w3c_understanding_status].

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** The chart is purely static and does not receive parameters or trigger any updates.
- **Reason:** There is no interactive context or dynamic status change to communicate.

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Additional text and notification plumbing increases authoring and implementation effort.
- **The Risk:** Poorly written explanations or overly frequent messages can create clutter and make the experience harder to follow, undermining clarity (the very goal of the guideline) [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Relying on visual-only cues (e.g., highlights, animated transitions, or subtle layout changes) to imply that other content updated.
- **Why it fails:** The dependency and update may not be communicated in text or detectable by assistive technologies without navigation [@w3c_understanding_status].
- **The Wrong Fix:** Making the user navigate elsewhere to discover that something changed (e.g., expecting them to tab around to find updated numbers).
- **Why it fails:** Status updates should be monitorable programmatically without requiring navigation [@w3c_understanding_status].

## How to Check <!-- role: check -->

- **Visual Sign:** Interactions change other regions (filters applied, panels update, layout reflows) but nothing on-screen explains the relationship or confirms what happened.
- **The Test:** Trigger a chart interaction (or change an external control) and verify that an explicit textual explanation exists for the relationship, and that an appropriate status message is emitted for the update in a way assistive technologies can detect without moving focus [@w3c_understanding_status].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add concise on-page text describing the interaction model (what controls affect the chart, and what chart interactions affect elsewhere) and add a status message for key updates (e.g., “Filter applied: Category A; results updated.”) that is programmatically conveyed [@w3c_understanding_status].
- **Best Fix:** Provide a complete, consistently located textual description of chart-control dependencies and state, and ensure all significant updates caused by chart interactions or external inputs generate programmatically detectable status messages so assistive technologies can announce them without requiring navigation [@elavskyHowAccessibleMy2022], [@w3c_understanding_status].
