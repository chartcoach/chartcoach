---
id: match-row-height-to-table-length
title: Adjust Row Height to Table Length
bibliography: references.bib
description: Use roomy rows for short tables and compact rows for long tables to improve
  comfort and comparison.
labels:
- chart:table
- task:compare
- visual:layout
- impact:readability
- data:mixed
- audience:general
- complexity:basic
---

## The Rule <!-- role: advice -->

Use wider row spacing for tables with only a few rows, and a compact row height for tables with many rows.

## The Logic <!-- role: reason -->

Short tables benefit from a more pleasant, airy layout, while long tables need compact rows to fit more information and make cross-row comparison easier; this tradeoff is described in [@muth_tables_2019].

- **The Principle:** Balance density and legibility
- **The Evidence:** [@muth_tables_2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing values across multiple rows efficiently
- **Data Type:** Tables that are either very short (few rows) or very long (many rows)
- **Audience:** Readers viewing tables on limited screen space [@muth_tables_2019]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Rows contain multi-line text that needs space to remain readable
- **Reason:** Over-compacting can harm legibility of longer content [@muth_tables_2019]

## The Price <!-- role: costs -->

- **The Sacrifice:** Either space (if using roomy rows) or comfort (if using compact rows)
- **The Risk:** Wrong density can make the table feel either sparse and scrolling-heavy or cramped and hard to read [@muth_tables_2019]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a single default row height for all tables
- **Why it fails:** The layout won’t match the table’s length and harms either readability or efficient comparison [@muth_tables_2019]

## How to Check <!-- role: check -->

- **Visual Sign:** Long tables feel like they “waste space,” or short tables look cramped
- **The Test:** Ask whether the intended portion of the table fits comfortably on one screen while remaining readable [@muth_tables_2019]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase row height for short tables; decrease it for long ones [@muth_tables_2019]
- **Best Fix:** Tune row height until key comparisons are easy and the table’s visible density matches its length and medium [@muth_tables_2019]
