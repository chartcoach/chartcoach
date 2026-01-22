---
id: enable-structure-based-keyboard-navigation-for-narrative-and-nested-data
title: "Enable keyboard navigation that follows the chart\u2019s narrative and data\
  \ structure (not only linear tab order)"
bibliography: references.bib
description: Provide keyboard navigation and alternative linear/tabular paths that
  let users traverse a chart in narrative order and by its underlying data structure,
  including nested levels.
labels:
- chart:interactive
- task:navigate
- visual:structure
- impact:accessibility
- data:hierarchical
- audience:assistive-technology-users
- complexity:advanced
- principle:compromising
---

## Structure-based navigation for charts <!-- role: advice -->

Provide keyboard navigation that lets users move through the chart in narrative order (title, description, annotations, then detailed data) and also traverse the underlying data structure (including nested levels and lateral moves), not only a single linear focus order.

## Why structure-based navigation supports accessible understanding <!-- role: reason -->

When navigation mirrors the data and narrative structure, users can build a correct mental model of what the chart is communicating and efficiently move between meaningful groupings (levels, siblings, and summaries) instead of being forced through an arbitrary rendering order.

**Mechanism:** Structure-aligned navigation reduces the work required to locate context (summaries and annotations) and then drill down into the relevant substructures, while still permitting a linear or tabular path when non-linear traversal is difficult.

**Evidence:** Interactive structured exploration (including keyboard and menu-driven approaches that support moving between levels and across related items) enables accessible navigation of complex diagrams and hierarchical/nested content across devices and assistive technologies. [@misc{progressiveaccess_accessible_chemistry_2}] Techniques that enable navigation based on chart structure rather than only linear order support exploring hierarchies and nested data (including moving between levels and across siblings) in chart-like representations. [@inproceedings{unknown_accessible_navigation_2015}] Heuristic guidance for visualization accessibility emphasizes that charts should support navigation aligned to narrative and data structure rather than forcing access through limited interaction paths. [@elavskyHowAccessibleMy2022]

**Notes:** This guideline requires providing both structure-based traversal and an alternative linear or tabular traversal so different users can choose the path that best matches their tools and preferences.

## When structure-following navigation is required <!-- role: context -->

- **User Goal:** Understand the chart’s intended takeaway, then access supporting details at different levels of granularity.
- **Task:** Move between overview context (title/summary/annotations) and detailed values; traverse groups, subgroups, and siblings in nested structures.
- **Data:** Hierarchical, nested, or subgrouped data (for example, multi-level groupings or parent–child relationships).
- **Chart Setting:** Interactive or navigable chart experiences where keyboard access is expected and non-linear exploration is valuable.
- **Audience:** Users who navigate via keyboard interfaces and assistive technologies, plus users who benefit from guided narrative structure.
- **Success Criterion:** Users can reach narrative context first, then traverse both across and between levels of the data structure without being forced into only a long linear focus order.

## When not to follow it exactly <!-- role: exceptions -->

**Break it when:** The chart has no meaningful narrative elements (no title/description/annotations) and no meaningful internal structure beyond a flat list of items. **Why:** There is no narrative or multi-level structure to mirror, so a simple linear or tabular navigation can be comparable to the data.

## Tradeoffs of adding structure-based navigation <!-- role: costs -->

**Sacrifice:** Additional interaction design and implementation effort to model levels, groups, and lateral movement paths. **Risk:** Poorly designed non-linear navigation can confuse users if it is inconsistent or undocumented. **Mitigation:** Ensure a consistent traversal model and preserve a linear/tabular alternative path alongside structure-based traversal.

## Common ways implementations fail <!-- role: mistakes -->

- **Mistake:** Only exposing a single tab order that follows rendering order. **Why it fails:** Rendering order is not necessarily the chart’s narrative or data structure, so users cannot reliably move by levels or across related groups.
- **Mistake:** Providing structure-based traversal without any linear or tabular alternative. **Why it fails:** Some users and tools depend on predictable linear navigation and may not be able to use or discover non-linear traversal.

## Quick tests for structure-aligned navigation <!-- role: check -->

**Failure Sign:** Keyboard users must tab through many elements before reaching context (title/summary/annotations) or cannot move between levels/siblings in nested groupings. **Quick Check:** Use only the keyboard and attempt to access title/description/annotations first, then move laterally among peers and up/down between levels; if you can only move linearly, this fails. **Stronger Test:** Verify that both a structure-based traversal path and a linear/tabular traversal path are available and that both allow reaching the same key information and functionality.

## How to remediate navigation that does not match structure <!-- role: fix -->

- Provide a keyboard-accessible navigation flow that reaches title, description, and annotations before exposing detailed data points.
- Implement keyboard controls that allow moving laterally across peer items and vertically between levels for nested or subgrouped data structures.
- Provide a linear or tabular navigation alternative (for example, a list-like or table-like path) that exposes the same information and can be used instead of non-linear traversal.
- Ensure the traversal model reflects the chart’s data structure even when the structure is novel, so users can navigate by meaningful groupings rather than arbitrary element order.
