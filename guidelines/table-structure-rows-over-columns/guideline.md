---
id: table-structure-rows-over-columns
title: Structure Data with More Rows Than Columns
bibliography: references.bib
description: Design tables vertically rather than horizontally to facilitate natural
  scanning behavior.
labels:
- chart:table
- visual:layout
- visual:orientation
- impact:readability
- device:mobile
---

## The Rule <!-- role: advice -->
Structure your data so that the table has more rows than columns. If you have a wide dataset, swap (transpose) the rows and columns to create a vertical orientation.

## The Logic <!-- role: reason -->
Humans find it easier to skim through information that is vertically aligned rather than horizontally aligned. This behavior is similar to how we read dictionaries. Additionally, fewer columns make the table significantly more readable on mobile devices [@muth_tables_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Quick skimming and scanning of categories.
*   **Device:** Mobile screens where horizontal space is limited.
*   **Data Type:** Data sets where categories can be pivoted (e.g., comparing regions across months vs. months across regions).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When strict side-by-side horizontal comparison of many attributes for a single entity is the primary use case, and vertical scrolling would separate related data points too much.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The table becomes longer vertically, potentially requiring more scrolling or pagination.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Keeping all available data columns in the view to avoid making the table "tall."
*   **Why it fails:** It forces horizontal scrolling on mobile and makes skimming difficult for the eye.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the table have a horizontal scrollbar on a standard smartphone screen?
*   **The Test:** Count rows and columns. If Columns > Rows, consider transposing.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Hide non-essential columns on mobile views.
*   **Best Fix:** Transpose the dataset so headers become row labels.
