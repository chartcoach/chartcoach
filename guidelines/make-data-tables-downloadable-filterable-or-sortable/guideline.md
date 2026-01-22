---
id: make-data-tables-downloadable-filterable-or-sortable
title: Make provided data tables downloadable, filterable, or sortable (not static)
bibliography: references.bib
description: If you provide a data table alongside a visualization, ensure the table
  can be downloaded (for example as CSV) and/or interacted with through filtering
  or sorting.
labels:
- chart:table
- task:explore
- visual:text
- impact:accessibility
- data:tabular
- audience:expert
- principle:compromising
- format:csv
---

## Make the table flexible (download, filter, or sort) <!-- role: advice -->

Make any provided data table downloadable, filterable, or sortable rather than leaving it as a static table. If possible, offer a CSV download so people can use their own tools to reshape and inspect the data.

## Flexible tables support alternative information flows <!-- role: reason -->

A static table can trap people in one fixed way of reading and navigating the data, which is especially limiting for users who prefer different information flows or who rely on assistive technologies and their own data workflows. Making the table downloadable or interactive (filter/sort) increases tolerance and user control, enabling users to re-order, search, subset, and reformat data in ways that match their access needs.

**Mechanism:** Flexibility shifts the burden of navigation and transformation from the visualization’s fixed presentation to user-controlled operations, letting users choose the interaction and representation that best supports their access needs.

**Evidence:** Flexible data tables that are sortable or downloadable are recommended to support accessible consumption patterns and user-controlled exploration of tabular data. [@inclusive-components_inclusive_components; @elavskyHowAccessibleMy2022]

**Notes:** A CSV is a low-level representation that can be remolded in external tools, which can satisfy diverse access needs when the chart itself cannot. [@elavskyHowAccessibleMy2022]

## When a table is part of the visualization experience <!-- role: context -->

- **User Goal:** Inspect, verify, or re-use the underlying chart data in a user-preferred environment.
- **Task:** Search for specific rows, compare values across categories, or extract a subset for further analysis.
- **Data:** Tabular data that users may want to reorder, subset, or export.
- **Chart Setting:** A visualization that includes a table as a companion view or alternative representation.
- **Audience:** Users with disabilities and assistive-technology users, including people who prefer to work with data in dedicated tools.
- **Success Criterion:** Users can obtain and reshape the data without being constrained by a fixed, static table rendering.

## When a static table is acceptable <!-- role: exceptions -->

**Break it when:** The table is not actually provided (no tabular alternative is present). **Why:** The guideline is triggered only when a table is part of the delivered experience.

## Tradeoffs of adding table interactivity or downloads <!-- role: costs -->

**Sacrifice:** Additional implementation effort to support download, sorting, or filtering. **Risk:** Added controls can increase interface complexity. **Mitigation:** Keep the table interactions limited to the core operations needed for access: download, filter, and sort.

## Common ways this fails in practice <!-- role: mistakes -->

- **Mistake:** Providing a table that is visually present but cannot be downloaded, filtered, or sorted. **Why it fails:** Users remain locked into a single, fixed information flow and cannot remold the data to match their access needs.
- **Mistake:** Treating the presence of any table as sufficient, even when it is static. **Why it fails:** The table does not provide the flexibility needed for alternative consumption patterns.

## How to tell if the table is too static <!-- role: check -->

**Failure Sign:** Users can view the table but cannot change its order, narrow it, or obtain it for use elsewhere. **Quick Check:** Try to sort by a column or filter rows using built-in controls; if neither exists, look for a download option such as CSV. **Stronger Test:** Attempt to reproduce a basic subset-and-compare task (for example, isolate one category and sort by value) using only the provided table features.

## Ways to restore flexibility <!-- role: fix -->

- Provide a CSV download option for the table’s underlying data.
- Add column sorting so users can reorder the table by key fields.
- Add filtering, ideally including a search feature to quickly narrow rows.
- Ensure the table remains a data table (not a layout table) so it can serve as a robust alternative representation. [@inclusive-components_inclusive_components]
