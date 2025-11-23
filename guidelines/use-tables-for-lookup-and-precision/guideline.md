---
id: use-tables-for-lookup-and-precision
title: Use Tables for Data Lookup and Precision
bibliography: references.bib
description: Choose tables over charts when readers need to find specific data points
  or see precise numbers for decision-making.
labels:
- chart:table
- task:lookup
- task:compare
- impact:precision
- audience:general
---

## The Rule <!-- role: advice -->
Use tables when you want to enable readers to look up specific information relevant to them (such as location, age, or income) or when precise numbers are required for decision-making. Do not use tables if the primary goal is to show broad patterns or outliers.

## The Logic <!-- role: reason -->
According to [@muth_tables_2019], readers interact with tables differently than charts. They rarely read a whole table; instead, they scan for the specific data that applies to them. Furthermore, tables act as "decision tools" because precise numbers (like interest rates or prices) are necessary for taking action, whereas charts are better for providing an overall picture or highlighting trends.

## Where to Apply <!-- role: context -->
*   **User Goal:** When the user needs to find their specific team, state, or demographic bucket.
*   **User Goal:** When the user needs to make a decision based on exact figures (e.g., choosing a bank or a job).
*   **Data Type:** Structured text data (names, teams) or precise numerical values.
*   **Data Type:** Standardized measurements we are accustomed to reading as numbers (e.g., age, drink sizes like 0.33l vs 0.5l).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** You need to highlight a pattern, trend, or outlier.
*   **Reason:** Tables are read sequentially (row by row). In a long table, readers may give up before finding the most important value, whereas charts make outliers and trends immediately visible [@muth_tables_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the immediate visual impact of the "overall picture."
*   **The Risk:** Readers might miss global trends or the relationship between the smallest and largest values if they are not explicitly looking for them.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Visualizing data that is already intuitive as text (like age or rank).
*   **Why it fails:** Visualizing ranks (e.g., 1 vs 2) can be misleading because rank 1 is not "half as good" as rank 2. Similarly, visualizing age is often unnecessary as we have strong associations with the numbers themselves [@muth_tables_2019].

## How to Check <!-- role: check -->
*   **The Test:** Ask: "Does the user need to know the general trend, or the exact value for 'row X'?"
*   **The Test:** If the user needs the exact value, use a table. If they need the trend, use a chart.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If precise values are buried in a text block, extract them into a structured table.
*   **Best Fix:** If the goal is mixed (precision + overview), use a table with embedded visual elements like sparklines or bars.
