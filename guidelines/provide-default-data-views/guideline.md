---
id: provide-default-data-views
title: Provide Default Data Views
bibliography: references.bib
description: Ensure analytic environments provide a default, opinionated view rather
  than forcing users to build charts from scratch to reduce cognitive load.
labels:
- impact:accessibility
- impact:cognitive-load
- task:exploration
- task:analysis
- audience:novice
- audience:general
---

## The Rule <!-- role: advice -->
Provide a default, opinionated view of the data as a starting point when users enter an analytic environment. Do not present a blank canvas or require users to combine variables immediately to see a visualization.

## The Logic <!-- role: reason -->
"Build your own" analytical experiences impose a high cognitive burden on users, particularly when intersecting with other access needs. By requiring users to manually craft a chart before seeing any data, the system creates an unnecessary barrier to entry.
*   **The Principle:** Assistive (Chartability Principle)
*   **The Evidence:** This guideline is derived from the "Assistive" principle of the Chartability framework, which aims to reduce the functional and cognitive labor required for access. Empirical observations in product testing found that empty states are difficult for users with disabilities to navigate [@elavsky_how_2022].

## Where to Apply <!-- role: context -->
This advice applies specifically to interactive tools and analytic environments where users are expected to explore data.
*   **User Goal:** Analyzing data by combining variables or filtering.
*   **Data Type:** Complex datasets requiring user input to structure (e.g., BI tools, dashboard creators).
*   **Audience:** Users with cognitive disabilities, novices, or anyone using assistive technology who benefits from reduced interaction costs.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Purely creative or drawing-based data art tools where the canvas must be blank by definition.
*   **Reason:** In these specific cases, an opinionated default might hinder the specific creative intent, though a "template" is still often preferred over a blank slate.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The "opinionated" default view implies a specific narrative or perspective that might not match the user's immediate question.
*   **The Risk:** Users might rely solely on the default view and fail to explore other variables if the default seems sufficiently comprehensive.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Providing a blank screen with a list of available variables (e.g., a sidebar of drag-and-drop fields) but no rendered chart.
*   **Why it fails:** It forces the user to understand the data structure and the tool's mechanics before they can access any information.

## How to Check <!-- role: check -->
*   **Visual Sign:** When the interface loads, is the main content area empty?
*   **The Test:** Launch the analytic environment as a new user. If you must perform an action (drag, click, type) before a visualization appears, the design fails this heuristic.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Pre-select the first two variables in the dataset to render a basic bar or line chart immediately upon load.
*   **Best Fix:** Design an "intelligent" default that analyzes the dataset's properties and renders the most statistically significant or common visualization type automatically.
