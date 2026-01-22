---
id: match-row-height-to-table-length
title: Adjust table row height to table length so comparisons stay easy
bibliography: references.bib
description: Use roomier rows for short tables and compact rows for long tables to
  balance comfort and comparability.
labels:
- chart:table
- task:compare
- visual:layout
- impact:readability
- data:tabular
- audience:general
---

## Scale row height to how many rows you show <!-- role: advice -->

Use taller, airier rows when showing only a few rows, and switch to a compact row height when the table contains many rows.

## Spacing trades off comfort against density and comparability <!-- role: reason -->

Row spacing affects both aesthetic comfort and the ability to compare many entries within a fixed viewport.

**Mechanism:** Larger row heights improve legibility and visual comfort for small tables, while compact rows increase information density so more rows fit on screen, supporting across-row comparisons.

**Evidence:** Wider layouts are more pleasant for tables with few rows, while compact layouts help when tables have many rows by making comparisons easier and increasing the chance the full table fits on one screen/page [@muth_tables_2019].

**Notes:** Row height is a layout control that should respond to content volume.

## When to apply row-height tuning <!-- role: context -->

- **User Goal:** Read comfortably (short tables) or compare many entries efficiently (long tables).
- **Task:** Scanning and comparing values across many rows.
- **Data:** Either a small curated set or a large list.
- **Chart Setting:** Screen- or page-constrained layouts where visible rows matter.
- **Audience:** General; especially relevant for quick-reading contexts.
- **Success Criterion:** Readers can see enough rows to compare without feeling cramped or overwhelmed.

## When a fixed row height may be necessary <!-- role: exceptions -->

**Break it when:** Row height is constrained by included content (e.g., multiline text, images, or embedded visuals) that cannot be compressed without losing readability. **Why:** Compressing rows would reduce legibility or truncate essential content [@muth_tables_2019].

## Tradeoffs of changing row height <!-- role: costs -->

**Sacrifice:** Airier rows reduce how much information fits at once; compact rows reduce breathing room. **Risk:** Over-compact rows can make scanning tiring; over-tall rows can hide too much of the table. **Mitigation:** Choose the smallest height that keeps text and key symbols comfortably readable at the intended device size [@muth_tables_2019].

## Common row-height mistakes <!-- role: mistakes -->

**Mistake:** Using a spacious row height for a long table. **Why it fails:** Too few rows fit on screen, making comparisons harder and increasing scrolling [@muth_tables_2019].

## Quick checks for row-height fit <!-- role: check -->

**Failure Sign:** Readers must scroll constantly to compare nearby rows or lose context when moving through the list. **Quick Check:** If only a small handful of rows are visible in a long table, the rows are likely too tall. **Stronger Test:** Confirm whether the full table (or a meaningful chunk) fits within a screen/page for the intended reading device [@muth_tables_2019].

## Fixes when row height is working against you <!-- role: fix -->

- Reduce row height for long tables so more entries are visible at once [@muth_tables_2019].
- Increase row height for short tables to improve visual comfort and perceived quality [@muth_tables_2019].
- Reduce columns or shorten text/number formats so rows don’t need extra height due to wrapping [@muth_tables_2019].
