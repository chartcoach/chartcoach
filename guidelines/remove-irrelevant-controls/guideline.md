---
id: remove-irrelevant-controls
title: Remove Irrelevant Interactive Controls
bibliography: references.bib
description: Eliminate interactive elements and controls that do not add direct value
  to the user's task to reduce cognitive load and ambiguity.
labels:
- impact:accessibility
- impact:cognitive-load
- visual:interaction
- tool:tableau
- audience:general
---

## The Rule <!-- role: advice -->
Ensure that every control, widget, and interactive component provided in the visualization adds value to the specific message, question, or task. Remove any functionality or interactive scope that is irrelevant or too broad for the user's needs.

## The Logic <!-- role: reason -->
Providing controls that are effectively useless or excessively taxing to use creates cognitive barriers. By limiting functionality to only what is necessary, you reduce the cognitive and functional labor required of the user.
*   **The Principle:** Add Value (Inclusive Design).
*   **The Evidence:** Designs should avoid unnecessary options and complexity to ensure interactive elements support the task rather than distracting from it [@inclusivedesignprinciples_add_value]. This minimizes cognitive load and presents data without ambiguity [@elavsky_how_2022].

## Where to Apply <!-- role: context -->
This advice applies to interactive data interfaces, particularly those built with tools that provide default interactivity.
*   **User Goal:** Analyzing data without distraction or confusion regarding interface mechanics.
*   **System Type:** Dashboards and interactive visualizations where users can click, hover, or drag.
*   **Tooling:** Environments like Tableau where interaction often exists by default.

## When to Break It <!-- role: exceptions -->
There are rare instances where consistency overrides specific utility.
*   **Scenario:** Global Navigation or Standardized Toolbars.
*   **Reason:** If a specific control appears in the same location across an entire application, removing it for a single chart might confuse users who rely on interface consistency, even if it is disabled or inactive for that specific view.

## The Price <!-- role: costs -->
Adhering to this rule often requires fighting against software defaults.
*   **The Sacrifice:** You lose "free" interactivity provided by tools out-of-the-box.
*   **The Effort:** Practitioners must invest significant effort to reverse engineer or deconstruct default behaviors in closed-box tools (e.g., Tableau) to remove unwanted interactivity [@elavsky_how_2022].

## Common Mistakes <!-- role: mistakes -->
A frequent failure occurs when authors leave default tool behaviors enabled because they seem harmless.
*   **The Wrong Fix:** Leaving default "drag-select," "click," or "hover" interactions enabled on charts where they provide no new information or filtering capability.
*   **Why it fails:** As seen in many Tableau dashboards, this "interaction-by-default" approach suggests functionality exists where there is none, confusing the user and increasing the scope of the interface unnecessarily [@elavsky_how_2022].

## How to Check <!-- role: check -->
Audit the interface for "orphan" interactions.
*   **The Test:** Click, hover, and drag on every element of the chart.
*   **The Question:** "Does this specific action provide new information or help answer the user's question?" If the answer is no, the control is inappropriate.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Disable tooltips, selection states, and highlighters on static data points that do not require drill-down.
*   **Best Fix:** Curate the experience by explicitly designing the interaction layer. Only include controls (buttons, filters, drill-downs) that are strictly relevant to the chart's defined task.
