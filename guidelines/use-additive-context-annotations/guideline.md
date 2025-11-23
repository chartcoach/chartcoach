---
id: use-additive-context-annotations
title: Use Additive Context Annotations
bibliography: references.bib
description: Use annotations to inject external information (news, events) rather
  than just describing values, to support narrative interpretation.
labels:
- chart:line
- task:storytelling
- visual:text
- impact:context
- data:textual
---

## The Rule <!-- role: advice -->
Use "additive" annotations that provide external information (such as news events or background context) rather than "observational" annotations that simply restate data values.

## The Logic <!-- role: reason -->
In narrative visualizations, specifically for news, the primary goal is to provide context. A survey of 136 professional visualizations found that 73.5% used additive messaging (referencing external info), whereas only 49.3% used observational messaging (referencing data values like "50% increase"). Additive annotations help the user bridge the gap between the abstract data line and the real-world events that influenced it.
*   **The Principle:** Additive vs. Observational Context
*   **The Evidence:** [@hullman_contextifier_2013]

## Where to Apply <!-- role: context -->
*   **User Goal:** Making sense of news, understanding the "why" behind data movements.
*   **Audience:** General news readers or investors looking for qualitative context alongside quantitative data.
*   **Context:** "Narrative visualizations" intended to tell a story, rather than exploratory dashboards.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Pure statistical analysis.
*   **Reason:** If the user needs to know the exact value of a peak or the precise percent change, "observational" annotations (e.g., labels stating values) are necessary.
*   **Scenario:** The visualization is standalone without a surrounding article.
*   **Reason:** Without an accompanying story, the chart may need to be more self-descriptive regarding its own values.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Direct data reading. By filling space with event descriptions, you may crowd out labels that show the literal Y-axis values.
*   **The Risk:** Information overload. If the external context is complex, the chart becomes a reading exercise rather than a visual pattern recognition task.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Annotations that say "Price dropped to $50."
*   **Why it fails:** This is *observational* (redundant with the axis). An *additive* annotation would say "CEO resigns amid scandal," which explains the drop.

## How to Check <!-- role: check -->
*   **Visual Sign:** Read your annotations. Do they contain numbers that are already visible on the Y-axis?
*   **The Test:** Ask "Does this text tell me *what* happened (data) or *why* it happened (context)?" If it's just *what*, it's observational. If it's *why*, it's additive.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Rewrite labels to describe the real-world event associated with the data point.
*   **Best Fix:** Integrate a query system that pulls headlines or event summaries related to the date of significant data changes.
