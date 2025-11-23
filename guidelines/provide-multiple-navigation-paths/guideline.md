---
id: provide-multiple-navigation-paths
title: Provide Multiple Paths to Information
bibliography: references.bib
description: Ensure complex data interfaces offer at least two distinct methods to
  locate content or reach specific states.
labels:
- impact:accessibility
- impact:navigation
- task:explore
- complexity:advanced
- audience:impaired
---

## The Rule <!-- role: advice -->
Ensure that there is always more than one process available to reach the same information or interface state. Do not force users to rely on a single navigation path, such as a specific sequence of interactions, to access content.

## The Logic <!-- role: reason -->
This guideline falls under the **Compromising** principle (Understandable, yet Robust), which prioritizes transparency and tolerance in information flows [@elavsky_how_2022].
*   **The Principle:** Cognitive and Functional Flexibility. Users with different disabilities or cognitive preferences may find one method of navigation (e.g., visual exploration) difficult but another (e.g., text search) accessible.
*   **The Evidence:** This heuristic aligns with the WCAG 2.1 "Multiple Ways" criterion, which encourages providing mechanisms like search functions, sitemaps, or navigation menus alongside standard browsing to reduce reliance on memory and ease information retrieval [@w3c_understanding_multiple_2].

## Where to Apply <!-- role: context -->
*   **User Goal:** Deep exploration of data where the user must transition between views, states, or pages.
*   **Data Type:** Complex analytical dashboards and applications that suffer from high information density [@elavsky_how_2022].
*   **Context:** Interfaces involving complex flows, such as interacting with filters to reveal data or moving between hierarchical pages.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Simple, single-view static visualizations.
*   **Reason:** If all information is immediately present and visible without the need for navigation, filtering, or state changes, alternative paths are unnecessary.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Creating parallel UI controls (such as adding a search feature alongside a visual drill-down) increases design and development effort.
*   **The Risk:** Without careful Information Architecture (IA), adding multiple navigation methods can clutter the interface. As noted in the source material, this is ultimately an IA problem [@elavsky_how_2022].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** relying solely on "scrollytelling" or linear "wizard" flows where the user cannot jump to specific sections.
*   **The Failure:** This forces users to traverse unwanted content to find specific data, which can be cognitively exhausting or physically difficult.
*   **The Oversight:** assuming that a visual interaction (e.g., clicking a bar to filter) is sufficient navigation without providing a text-based alternative (e.g., a dropdown or search box).

## How to Check <!-- role: check -->
*   **The Test:** Identify a specific piece of information or a specific view state within the visualization.
*   **The Procedure:** Attempt to reach that state using the primary method (e.g., clicking through the chart). Then, attempt to reach the exact same state using a different method (e.g., a search bar, a sidebar menu, or a sitemap).
*   **Visual Sign:** If a specific view can *only* be reached by clicking a specific sequence of data points, the design fails this heuristic.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a sitemap or a clear table of contents that links directly to different sections or states of the dashboard.
*   **Best Fix:** Implement parallel UI controls, such as a search feature or a filter panel, that allows users to reach the same filtered state as the direct visual interactions [@elavsky_how_2022].
