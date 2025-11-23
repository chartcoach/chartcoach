---
id: navigate-by-data-structure
title: Align Navigation with Narrative and Data Structure
bibliography: references.bib
description: Ensure keyboard navigation follows the logical hierarchy of the chart
  (Title > Description > Data) and allows structural movement through grouped or nested
  data.
labels:
- impact:accessibility
- impact:structure
- task:explore
- visual:layout
- chart:stacked-bar
- chart:treemap
- audience:screen-reader-users
---

## The Rule <!-- role: advice -->
Design keyboard navigation that strictly follows the narrative and data structure of the visualization. Ensure the focus order proceeds hierarchically: first the Title, then the Description, then Annotations, and finally the lower-level Data Structures. For complex data containing sub-groupings (such as stacked bars) or nesting (such as treemaps), you must provide non-linear navigation that allows users to move between levels and laterally across siblings.

## The Logic <!-- role: reason -->
Standard linear navigation (like the default DOM order found in basic HTML) is often insufficient for complex data visualizations.
*   **The Principle:** **Compromising** (Understandable, yet Robust). This principle requires providing information flows that tolerate different consumption preferences and reduce cognitive load for assistive technology users [@elavsky_how_2022].
*   **The Evidence:** Research indicates that navigating hierarchically allows users to understand the context before diving into details, mimicking the way visual users scan a chart. Work by Sorge et al. on progressive access demonstrates that features like menu-driven exploration and structural navigation are critical for accessible diagrams [@progressiveaccess_accessible_chemistry_2]. Furthermore, specifically for hierarchical data, methods that allow users to move between levels and across siblings are necessary to effectively explore charts like treemaps and grouped bar charts [@unknown_accessible_navigation_2015]. Existing standards like WCAG 2.4.3 (Focus Order) often fall short for these specific spatial data needs [@elavsky_how_2022].

## Where to Apply <!-- role: context -->
This advice applies to any data-driven interface that renders complex or grouped data.
*   **User Goal:** Exploring data relationships, such as understanding the composition of a stack or the hierarchy of a tree, without visual overview.
*   **Data Type:** Grouped data (e.g., stacked bar charts), nested data (e.g., treemaps), or any chart with a specific narrative flow.
*   **Audience:** Users of screen readers and keyboard-only users who rely on structured navigation to build a mental model of the data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Simple, single-series charts with very few data points (e.g., a bar chart with 3 items).
*   **Reason:** In very simple cases, a purely linear navigation (tabbing through items) may be sufficient, and implementing complex 2D navigation might introduce unnecessary interaction overhead. However, the hierarchy of Title -> Description -> Data should typically remain.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Significant development effort is required to implement custom keyboard event handlers (e.g., managing arrow keys for spatial navigation) rather than relying on native browser tab order.
*   **The Risk:** If the navigation logic is not intuitive or documented (e.g., users don't know they can use arrow keys to dive into a stack), users may miss the deeper data entirely.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on linear `tabindex` order for grouped data.
*   **Why it fails:** Tabbing through every segment of every stacked bar linearly forces the user to traverse the entire dataset to find a specific group, making comparison difficult or impossible [@elavsky_how_2022].
*   **The Wrong Fix:** placing the data entry point before the summary.
*   **Why it fails:** Users encounter individual data points without first receiving the context (Title/Description) needed to interpret them.

## How to Check <!-- role: check -->
*   **Visual Sign:** As you tab through the interface, the focus ring should appear on the container/title first, then the description/summary, and finally the chart area.
*   **The Test:** Using only a keyboard:
    1. Verify focus lands on the Title, Description, and Annotations before the Data.
    2. For a stacked or grouped chart, verify you can navigate *vertically* (between stacks/groups) and *laterally* (between items within a stack/group) using appropriate keys (typically arrows), rather than just one long linear list [@elavsky_how_2022].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Ensure the DOM order of your SVG or HTML elements places text containers (Title, Desc) before the data container, ensuring screen readers announce context first.
*   **Best Fix:** Implement a "roving tabindex" or specific key-handling strategy that models the data structure. Allow arrow keys to traverse the data structure spatially (e.g., up/down for hierarchy, left/right for siblings) while keeping a linear tabular fallback available [@unknown_accessible_navigation_2015].
