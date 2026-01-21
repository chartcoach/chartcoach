---
id: add-a-summary-column-and-message-first-in-compact-tables
title: Add a Summary Column and Message First
bibliography: references.bib
description: Make compact tables feel like designed visuals by surfacing the takeaway
  with a clear title and an explicit summary column.
labels:
- chart:table
- task:rank
- visual:text
- impact:clarity
- data:categorical
- audience:general
- format:compact-table
- source:datawrapper-fix-my-chart
---

## The Rule <!-- role: advice -->

Write the table’s takeaway in the title and add a dedicated summary column that explicitly answers the main question (e.g., “X games” per city), rather than expecting readers to infer it from scattered columns.

## The Logic <!-- role: reason -->

A table is not a neutral spreadsheet; it’s a narrative device. By stating the point in the title and repeating the key metric in one place, you reduce search and integration effort and tell readers why the other columns exist in the first place, as described in the compact-table redesign in [@mintzer_compact_tables_2024].

- **The Principle:** Make the message explicit (interpretation, not raw listing)
- **The Evidence:** [@mintzer_compact_tables_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly identify/compare which category is “most” (top ranks) and by how much.
- **Data Type:** Small-to-medium categorical lists where details (e.g., dates/stages) support a primary metric.
- **Audience:** General readers skimming on desktop and mobile.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The table is intended as a reference lookup where no single “main question” exists.
- **Reason:** Forcing a single summary can misrepresent a multi-purpose table and add redundant clutter.

## The Price <!-- role: costs -->

- **The Sacrifice:** Uses extra horizontal space and can increase repetition.
- **The Risk:** If the summary metric is poorly defined, it can oversimplify and mislead.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding decorative colors while leaving the key comparison implicit.
- **Why it fails:** Visual styling can’t compensate for an unclear message; readers still must compute the “most games” conclusion themselves (the exact problem called out in [@mintzer_compact_tables_2024]).

## How to Check <!-- role: check -->

- **Visual Sign:** Readers must scan multiple columns to understand what the table is “about.”
- **The Test:** Hide all but the first column and your proposed summary column—if the main claim (“who hosted the most”) is no longer obvious, the summary/title aren’t doing their job.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Rewrite the title to state the question and add one summary column (e.g., “Berlin — 6 games”).
- **Best Fix:** Structure the table so the primary ranking metric is prominent and the remaining columns read as supporting detail, matching the “explain why it’s there” approach in [@mintzer_compact_tables_2024].
