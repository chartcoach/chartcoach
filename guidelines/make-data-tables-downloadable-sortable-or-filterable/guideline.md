---
id: make-data-tables-downloadable-sortable-or-filterable
title: Make Data Tables Downloadable, Sortable, or Filterable
bibliography: references.bib
description: Ensure any provided data table is at least downloadable, sortable, or
  filterable so users can flexibly consume and manipulate the underlying data.
labels:
- chart:table
- task:explore
- visual:text
- impact:accessibility
- data:tabular
- audience:expert
- principle:compromising
- source:community-practice
---

## The Rule <!-- role: advice -->

Do not provide a static data table; ensure the table is at least **downloadable (e.g., CSV)**, **sortable**, or **filterable** (ideally with search) so users can manipulate the data.

## The Logic <!-- role: reason -->

Static tables constrain how people can access and reshape information; downloadable, sortable, or filterable tables increase user control over the information flow and make it easier to use external tools that already support diverse access needs, aligning with Chartability’s Compromising principle for robust, tolerant information access [@elavskyHowAccessibleMy2022].

- **The Principle:** Flexible, user-moldable access to underlying data (avoid rigid, single-path information delivery)
- **The Evidence:** Guidance to make data tables sortable or downloadable for flexibility and correct data-table usage [@misc{inclusive-components_inclusive_components}]; synthesized as a Chartability heuristic from community practice [@elavskyHowAccessibleMy2022]

## Where to Apply <!-- role: context -->

This advice is designed for cases where you provide a data table as part of a data visualization or data interface.

- **User Goal:** Reuse, inspect, or analyze values (including reshaping data outside the visualization)
- **Data Type:** Tabular data presented as a table accompanying or substituting chart views
- **Audience:** Users who benefit from adapting the data to their own tools and workflows (including data experts and users of assistive technologies) [@elavskyHowAccessibleMy2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You do not provide a data table at all.
- **Reason:** This rule only applies when a table is present; it evaluates whether that provided table is unnecessarily static [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** More implementation and design effort (adding download, sorting, filtering/search UI).
- **The Risk:** Additional controls can increase interface complexity and require careful integration with the table structure [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Providing a table but leaving it static (no download, no sorting, no filtering).
- **Why it fails:** Users cannot reshape or interrogate the data in the way that suits their needs; it blocks the “moldable” low-level access that this heuristic targets [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** The table looks like a fixed, read-only grid with no visible sorting controls, filtering/search controls, or download option.
- **The Test:** Try to (1) download the table (e.g., as CSV), (2) sort by a column, or (3) filter/search within the table; if none are possible, the table is static and fails this guideline [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a **CSV download** option for the table so users can open and manipulate the data in their own tools [@elavskyHowAccessibleMy2022].
- **Best Fix:** Implement a **proper data table** and make it **sortable and filterable** (ideally with a search feature) to support flexible, user-controlled interrogation of the dataset [@misc{inclusive-components_inclusive_components}][@elavskyHowAccessibleMy2022].
