---
id: stack-bars-for-total-trends
title: Stack Bars for Aggregate Trends
bibliography: references.bib
description: Use stacked bar charts when the primary goal is to highlight the overall
  trend of the total sum.
labels:
- chart:stacked-bar
- task:identify-trend
- visual:length
- impact:clarity
- data:categorical
---

## The Rule <!-- role: advice -->
Use stacked bar charts rather than grouped (side-by-side) or unstacked charts when your primary objective is to ensure users notice the trend of the **total** values (the aggregate sum of the segments).

## The Logic <!-- role: reason -->
The visual envelope created by the total height of a stacked bar makes the aggregate trend immediately salient. When bars are unstacked or grouped, the user must mentally sum the parts to perceive the total, which often leads to missing the overall trend entirely.
*   **The Principle:** Visual summation / Gestalt continuity.
*   **The Evidence:** In a study on immigration data, participants viewing a stacked bar chart were significantly more likely to correctly describe the trend as "increasing" compared to those viewing a redesigned unstacked version, even though the unstacked version was theoretically "cleaner" [@burns_how_2020].

## Where to Apply <!-- role: context -->
*   **User Goal:** communicating a change in the total magnitude over time (e.g., "Total Immigration is rising").
*   **Data Type:** Part-to-whole data over time.
*   **Audience:** General audience needing the "big picture" trend.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Comparing individual segment values.
*   **Reason:** If the user needs to compare the size of the middle segments across bars accurately, stacked bars make this difficult due to shifting baselines. In that case, unstacking is better.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision in reading the values of individual categories (segments) within the stack.
*   **The Risk:** Users might ignore the internal composition changes if the total trend is too dominant.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Unstacking bars to "clean up" a chart when the main message is about the total volume.
*   **Why it fails:** It forces the user to perform mental arithmetic to recover the total trend, which they often fail to do [@burns_how_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the top edge of your bars. Do they form a shape that matches your headline (e.g., "Sales are up")?
*   **The Test:** Ask a user, " Is the total amount increasing or decreasing?" If they hesitate or start adding numbers, the design is failing.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Stack the bars.
*   **Best Fix:** If you need both segment comparison and total trends, consider a stacked area chart or adding a "Total" line overlay to a grouped bar chart.
