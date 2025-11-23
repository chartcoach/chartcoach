---
id: optimize-table-columns
title: Narrow and Simplify Table Columns
bibliography: references.bib
description: Techniques to reduce column width and clutter for better readability
  on all devices.
labels:
- chart:table
- visual:typography
- impact:conciseness
- device:mobile
---

## The Rule <!-- role: advice -->
Reduce the width and number of your columns to strictly essential information. Use icons, abbreviations, and rounded numbers. Move repeating words from cells into the column header.

## The Logic <!-- role: reason -->
Narrower columns improve readability, especially on mobile devices. Repeating words inside every cell (e.g., "1.3 million," "1.4 million") creates visual clutter; moving the unit to the header or using a shorter format (e.g., "1.3m") makes the unique data stand out [@muth_tables_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Scanning values quickly without reading repetitive text.
*   **Data Type:** Large numbers, currencies, or repetitive categorical text.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Legal or scientific data where exact precision (no rounding) is mandatory.
*   **Reason:** Rounding `0.1129302` to `0.1` may be unacceptable in high-precision contexts [@muth_tables_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Loss of extreme precision when rounding numbers.
*   **The Risk:** Abbreviations (e.g., headers or units) must be universally understood by the audience, or clarity is lost.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** keeping full words in every cell (e.g., "50% increase," "20% increase").
*   **Why it fails:** It forces the column to be wider than necessary and creates visual noise.

## How to Check <!-- role: check -->
*   **The Test:** Scan a column. If you read the same word more than twice in a row, move it to the header.
*   **The Test:** Check numerical columns. Are there more than 2-3 distinct digits? If yes, consider rounding (e.g., change 1,300,000 to 1.3m).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Round numbers and use standard abbreviations (k, m, %).
*   **Best Fix:** Move repeated units to the header and replace lengthy text labels with intuitive icons where appropriate.
