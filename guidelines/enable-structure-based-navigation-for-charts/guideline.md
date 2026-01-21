---
id: enable-structure-based-navigation-for-charts
title: Enable Structure-Based Navigation for Chart Narratives and Data
bibliography: references.bib
description: "Provide keyboard and assistive-technology navigation that follows the\
  \ chart\u2019s narrative and underlying data structure, not just a linear focus\
  \ order."
labels:
- chart:interactive
- task:explore
- visual:structure
- impact:accessibility
- data:hierarchical
- audience:assistive-technology-users
- principle:compromising
- input:keyboard
- navigation:nonlinear
---

## The Rule <!-- role: advice -->

Make the chart navigable by keyboard in the same order and shape as its narrative and data structure: title → description → annotations → lower-level data, and for grouped/nested charts provide non-linear navigation that moves between levels and laterally across siblings, plus a linear/tabular alternative.

## The Logic <!-- role: reason -->

This works because linear focus order alone cannot express the meaningful structure of many charts (e.g., groups, stacks, nesting), so users who navigate via keyboard and assistive technologies need interaction paths that mirror the data model and the intended narrative sequence to understand and traverse the content effectively [@elavskyHowAccessibleMy2022]. Systems that offer structure-aware navigation (including hierarchical movement and menu-driven exploration) demonstrate how mapping navigation to underlying structure enables comparable access across devices and assistive technologies [@unknown_accessible_navigation_2015; @progressiveaccess_accessible_chemistry_2].

- **The Principle:** Structure- and narrative-aligned navigation
- **The Evidence:** [@elavskyHowAccessibleMy2022; @unknown_accessible_navigation_2015; @progressiveaccess_accessible_chemistry_2]

## Where to Apply <!-- role: context -->

This advice is designed for charts where meaning depends on structure beyond a simple linear list of marks.

- **User Goal:** Navigate the chart in the same conceptual order it’s explained and compare related items across groups/levels.
- **Data Type:** Grouped, stacked, nested, or hierarchical data (e.g., stacked bars, treemaps, hierarchies) [@elavskyHowAccessibleMy2022].
- **Audience:** Keyboard and assistive-technology users who need comparable navigation paths to the chart’s structure [@elavskyHowAccessibleMy2022; @progressiveaccess_accessible_chemistry_2].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization contains no meaningful structure beyond a single, short linear sequence of content.
- **Reason:** Additional non-linear navigation paths may not add value relative to the structure present, and a single linear path may already match the content’s organization [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** More design and engineering effort to define and implement multiple navigation paths (narrative order, structure-aware traversal, and a linear/tabular alternative) [@elavskyHowAccessibleMy2022].
- **The Risk:** If implemented inconsistently, users may face confusing or mismatched navigation compared to the chart’s structure [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Relying only on default tab order (render order) for all marks and controls.
- **Why it fails:** A default linear focus path does not allow moving laterally within groups or between hierarchy levels, so navigation is not comparable to the data structure or narrative flow [@elavskyHowAccessibleMy2022; @unknown_accessible_navigation_2015].
- **The Wrong Fix:** Providing only one navigation method (only hierarchical OR only linear).
- **Why it fails:** Users may need both structure-aware traversal and a linear/tabular option to consume information in different ways [@elavskyHowAccessibleMy2022; @progressiveaccess_accessible_chemistry_2].

## How to Check <!-- role: check -->

- **Visual Sign:** Keyboard focus can only advance forward/backward through items; you cannot move between grouped items or up/down hierarchy levels in a way that reflects the chart’s structure [@elavskyHowAccessibleMy2022].
- **The Test:** Using only the keyboard, verify you can (1) reach title/description/annotations before lower-level data, (2) move between levels and laterally across siblings for grouped/nested data, and (3) access a linear/tabular representation (e.g., a table or list) that supports linear navigation [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a linear/tabular navigation alternative (e.g., a table or list) that provides access to the lower-level data in a straightforward linear order [@elavskyHowAccessibleMy2022].
- **Best Fix:** Implement keyboard navigation that mirrors the chart’s narrative and data structure—title/description/annotations first, then structured traversal that supports both lateral (between siblings) and vertical (between levels) movement—while also providing a linear/tabular navigation mode for users who prefer it [@elavskyHowAccessibleMy2022; @unknown_accessible_navigation_2015; @progressiveaccess_accessible_chemistry_2].
