---
id: avoid-lines-for-discrete-value-retrieval
title: Avoid Line Charts for Precise Value Reproduction
bibliography: references.bib
description: Line charts perform poorly when users need to identify and reproduce
  specific discrete values.
labels:
- chart:line
- task:retrieve-value
- visual:position
- impact:accuracy
- data:quantitative
- audience:analyst
---

## The Rule <!-- role: advice -->
Do not use **Line Charts** if the primary task is to read, remember, and reproduce specific discrete values. Use Bar Charts or Points instead.

## The Logic <!-- role: reason -->
While Line Charts are excellent for trends, they fail at discrete value isolation in memory tasks.
*   **The Evidence:** In controlled experiments measuring reproduction accuracy, **Position-Line** encodings consistently ranked at or near the bottom compared to Area, Angle, and Position-Bar encodings across datasets of 2, 4, and 8 marks [@mccoleman_rethinking_2022].
*   **The Principle:** The connected nature of a line chart emphasizes the *change* (slope) rather than the *nodes* (values), increasing the cognitive load required to extract and store individual data points [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Extracting specific numbers (e.g., "What was the sales figure in March?").
*   **Data Type:** Discrete time series or categorical data where individual values matter more than the trend.
*   **Audience:** General audiences needing to recall stats.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to see the *trend*, rate of change, or correlation between points.
*   **Reason:** Line charts are optimized for connectivity and slopes, not individual value isolation.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the immediate perception of continuity and temporal flow.
*   **The Risk:** The chart may look cluttered if you switch to Bars for a high-density time series.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding markers (dots) to a line chart but keeping the line dominant.
*   **Why it fails:** The line still guides the eye to relationships rather than values.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the user have to trace the grid lines carefully to read a single value?
*   **The Test:** Ask a user to read three random values from the chart. If they hesitate or trace with their finger, the design is inefficient for retrieval.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Replace the line with **Bars** (Position-Bar).
*   **Best Fix:** If the data is sparse, use **Bars** or **Points** (dot plot). If the data is dense and values matter, provide a table or interactive tooltips alongside the visualization.
