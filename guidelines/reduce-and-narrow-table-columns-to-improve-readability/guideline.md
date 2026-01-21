---
id: reduce-and-narrow-table-columns-to-improve-readability
title: Narrow and Reduce Table Columns
bibliography: references.bib
description: "Make tables easier to read\u2014especially on mobile\u2014by limiting\
  \ the number and width of columns."
labels:
- chart:table
- task:read
- visual:layout
- impact:clarity
- data:mixed
- audience:general
- complexity:basic
---

## The Rule <!-- role: advice -->

Keep tables to the essential columns and actively narrow columns using icons, abbreviations, shorter number formats, or rounding; consider showing fewer columns on mobile than on desktop.

## The Logic <!-- role: reason -->

Fewer and narrower columns reduce horizontal scanning and improve legibility, which is especially important on small screens; this is recommended directly in [@muth_tables_2019].

- **The Principle:** Reduce horizontal scan burden
- **The Evidence:** [@muth_tables_2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly scanning and finding relevant entries without excessive side-to-side reading
- **Data Type:** Tables with many candidate fields/metrics, long labels, or large/precise numbers
- **Audience:** Mobile and general readers in storytelling contexts [@muth_tables_2019]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The audience must see all fields at once to make a decision
- **Reason:** Removing or hiding columns could omit required decision inputs [@muth_tables_2019]

## The Price <!-- role: costs -->

- **The Sacrifice:** Some detail, precision, or explicitness (via rounding/abbreviations)
- **The Risk:** Abbreviations or icons may be unclear if not self-evident [@muth_tables_2019]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Dumping all available columns “for completeness”
- **Why it fails:** The table becomes hard to read, particularly on mobile, and readers are less likely to find what they need [@muth_tables_2019]

## How to Check <!-- role: check -->

- **Visual Sign:** The table requires horizontal scrolling or columns look cramped with wrapped text
- **The Test:** View on a phone-sized width: if key columns don’t fit comfortably, reduce/narrow columns [@muth_tables_2019]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Round numbers and shorten formats (e.g., 1.3m instead of 1,300,000); abbreviate repeating terms into headers [@muth_tables_2019]
- **Best Fix:** Redesign to include only essential columns and adapt column visibility by device (desktop vs. mobile) [@muth_tables_2019]
