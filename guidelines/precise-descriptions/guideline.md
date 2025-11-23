---
id: precise-descriptions
title: Write Precise Descriptions
bibliography: references.bib
description: Explicitly state units, timeframes, and data scope in the chart description;
  do not assume reader knowledge.
labels:
- visual:text
- impact:clarity
- data:metadata
- audience:novice
---

## The Rule <!-- role: advice -->
Write a description that tells the reader exactly what they are seeing, including units, timeframes, and the specific scope of the data.

## The Logic <!-- role: reason -->
Designers suffer from the "curse of knowledge"—they have spent hours exploring the data, but the reader is seeing it for the first time.
*   **The Principle:** Disambiguation.
*   **The Evidence:** [@muth_better_charts_2017] emphasizes that you cannot assume everyone knows the context. Stating "fiscal quarters" or "selected products" clarifies the data source and reminds readers of the specific time frame (e.g., stopping at 2014).

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurate interpretation of data.
*   **Data Type:** Any chart, especially those with subsets of data ("selected products").
*   **Audience:** General audiences or those outside the specific industry.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Highly specialized internal reports.
*   **Reason:** If every reader works in the same department and knows the standard fiscal year metrics, repetition might be noise.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Vertical space. Descriptions add text density.
*   **The Risk:** If the description is too long, readers might skip it.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Omitting the timeframe because "it's on the x-axis."
*   **Why it fails:** Readers may miss the endpoints (e.g., that the data stops at 2014, not the current year) if it isn't explicitly stated [@muth_better_charts_2017].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart title rely on implied knowledge (e.g., "Sales" instead of "Global Sales in Millions")?
*   **The Test:** Show the chart to someone outside your project. Ask "What products are included?" If they don't know, the description is lacking.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a subtitle summarizing the axes.
*   **Best Fix:** Write a sentence-style description like "Worldwide sales of selected Apple products in million, by fiscal quarter, 2000 to 2014" [@muth_better_charts_2017].
