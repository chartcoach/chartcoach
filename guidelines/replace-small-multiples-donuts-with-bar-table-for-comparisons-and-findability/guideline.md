---
id: replace-small-multiples-donuts-with-bar-table-for-comparisons-and-findability
title: Replace small-multiple donut charts with a bar-table to enable comparison and
  state lookup
bibliography: references.bib
description: "When many similar donut charts hide differences, switch to a table with\
  \ mini 0\u2013100 bars plus search and sorting so readers can compare categories\
  \ and find their own row."
labels:
- chart:table
- task:compare
- visual:position
- impact:clarity
- data:categorical
- audience:general
- pattern:small-multiples
---

## Use a table of mini bars instead of many similar donuts <!-- role: advice -->

Replace a grid of donut charts with a table that contains mini bar charts on a shared 0–100 scale, and add search plus sortable columns so readers can compare and find their own entry.

## Donuts reduce comparability; bar-tables support scanning and self-location <!-- role: reason -->

When many donuts look visually identical, readers can’t efficiently detect differences across categories or across items, so the display fails to produce a “big picture” pattern. Converting each donut to a bar on a common 0–100 scale makes magnitude comparisons more direct, and placing these bars in a table supports two reading modes: scanning across a row to understand one item’s composition, or scanning down a column to compare one category across items; search and sorting then help readers quickly locate the row that matters to them.

**Mechanism:** A shared linear scale and aligned bars reduce the effort needed to compare proportions, while a table layout plus search/sort changes the interaction from “take everything in at once” to “find myself, then compare.”

**Evidence:** A redesign that “unrolls” donuts into bars and embeds them in a searchable, sortable table made it easier to compare condition categories within and between U.S. states and helped readers focus on their own state when no single overarching pattern stood out [@mintzer_donuts_into_bars_2025].

**Notes:** Keeping a default sort (for example, by the “problem” category) preserves the original emphasis while still enabling other comparisons via resorting [@mintzer_donuts_into_bars_2025].

## Situations where donut small multiples fail to reveal differences <!-- role: context -->

- **User Goal:** Understand the breakdown of categories for a chosen item and see how that item compares to others.
- **Task:** Compare proportions within items and rank items by one category.
- **Data:** Many entities (for example, states) with 2–4 share categories that sum to 100%, plus an optional count/total per entity.
- **Chart Setting:** A dense display with many small multiples; interactive web context where search and sorting are possible.
- **Audience:** Broad audience, including readers who primarily care about “their own” row (for example, their state).
- **Success Criterion:** Readers can quickly find a specific item and accurately compare category shares across items.

## When donuts might be acceptable <!-- role: exceptions -->

**Break it when:** You only need to highlight a single entity (or a very small number of entities) and precise between-entity comparison is not the point. **Why:** The table and interaction overhead may be unnecessary when there’s no need to scan, rank, or look up a specific row [@mintzer_donuts_into_bars_2025].

## What you trade away by switching to a bar-table <!-- role: costs -->

**Sacrifice:** You give up the compact “badge-like” donut aesthetic and may use more vertical space to support labels, bars, and interaction. **Risk:** A table can feel utilitarian and may reduce immediate visual novelty. **Mitigation:** Keep the table focused (few columns, clear labels, sensible default sort) so the utility is obvious at a glance [@mintzer_donuts_into_bars_2025].

## Common ways this redesign still goes wrong <!-- role: mistakes -->

**Mistake:** Converting donuts to bars but letting each row use its own scale. **Why it fails:** Without a shared 0–100 scale, bar lengths can’t be compared reliably across rows, defeating the main benefit of the redesign [@mintzer_donuts_into_bars_2025].

**Mistake:** Publishing the table without search or sortable columns. **Why it fails:** Readers can’t quickly “find themselves in the data,” so the format loses a key advantage when there’s no single overarching story [@mintzer_donuts_into_bars_2025].

## Fast ways to tell if you should switch formats <!-- role: check -->

**Failure Sign:** Many donuts “all look the same,” and readers must work hard to see differences or locate a specific item. **Quick Check:** If you can’t easily rank the top and bottom items for one category by scanning the display, the donuts are not supporting comparison. **Stronger Test:** Ask a few readers to find their own row (for example, their state) and identify whether it is above or below average for one category; if they struggle, add table search/sort and aligned bars [@mintzer_donuts_into_bars_2025].

## Practical alternatives when donuts aren’t working <!-- role: fix -->

- Convert each donut into a horizontal stacked bar with a shared 0–100 scale and place one bar per row in a table.
- Add a search box so readers can immediately locate the item relevant to them.
- Enable sorting by any category column, and keep a meaningful default sort that reflects the main focus category.
- Include a “total” column (counts) alongside shares when magnitude/context matters, rather than trying to encode counts inside the donut hole [@mintzer_donuts_into_bars_2025].
