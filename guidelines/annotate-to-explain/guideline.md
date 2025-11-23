---
id: annotate-to-explain
title: Annotate to Explain Why
bibliography: references.bib
description: Use text annotations and visual highlights to explain the causes behind
  data trends.
labels:
- visual:annotation
- impact:storytelling
- task:explain
- visual:text
---

## The Rule <!-- role: advice -->
Use annotations (text, ranges, arrows) to highlight specific data points and provide context that explains *why* a trend occurred.

## The Logic <!-- role: reason -->
A chart displays *what* happened, but rarely *why*. Annotations bridge this gap.
*   **The Principle:** Storytelling and Contextualization.
*   **The Evidence:** [@muth_better_charts_2017] suggests that annotations allow you to provide information that "goes beyond our central statement," such as explaining that sales spiked "After Apple announced the iPhone 4."

## Where to Apply <!-- role: context -->
*   **User Goal:** Explaining causality or highlighting specific events.
*   **Data Type:** Time series or trend data affected by external events.
*   **Audience:** Readers who do not know the historical context of the data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Real-time dashboards.
*   **Reason:** Automated data streams cannot easily be manually annotated with context in real-time.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Clutter. Too many annotations can obscure the data trend.
*   **The Risk:** Bias. You choose which events to highlight, potentially framing the narrative subjectively.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Leaving the chart lines bare and putting the explanation in a paragraph of text below the chart.
*   **Why it fails:** Readers might not connect the text description to the specific visual spike it explains.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart rely entirely on the surrounding article text to explain sudden spikes or drops?
*   **The Test:** If you remove the article text, does the chart still explain *why* the line went up?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a text label pointing to the most dramatic change in the data.
*   **Best Fix:** Use visual highlights (like grey ranges) combined with text to lead the eye to the exact moment an event impacted the data [@muth_better_charts_2017].
