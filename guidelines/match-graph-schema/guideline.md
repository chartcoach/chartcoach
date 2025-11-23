---
id: match-graph-schema
title: Match Graph Type to Data Relationships
bibliography: references.bib
description: 'Respect viewer expectations: use lines for trends and bars for discrete
  comparisons.'
labels:
- chart:line
- chart:bar
- visual:schema
- impact:interpretation
- audience:general
---

## The Rule <!-- role: advice -->

Use line graphs to depict trends (continuous changes) and bar graphs to depict discrete comparisons. Do not violate these standard conventions without a compelling reason.

## The Logic <!-- role: reason -->

Viewers possess "graph schemas"—implicit knowledge and expectations about what specific graph formats communicate. Research shows that simply changing the format from bar to line changes the viewer's description of the data from "X is larger than Y" (discrete comparison) to "As X increases, Y increases" (trend), even for the same dataset [@zacks_designing_2020].

*   **The Principle:** Graph Schemas / Conceptual Expectations
*   **The Evidence:** In studies, 15% of viewers interpreted a line graph of male/female heights as "the more male you are, the taller you are," because line graphs imply continuous trends [@zacks_designing_2020].

## Where to Apply <!-- role: context -->

*   **User Goal:** Communicating a specific relationship (Comparison vs. Trend).
*   **Data Type:** Discrete categories (Gender, Country) vs. Continuous variables (Time, Temperature).
*   **Audience:** General audiences with standard educational backgrounds who have learned these conventions.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** When plotting a frequency distribution (histogram).
*   **Reason:** Histograms use bars but represent a continuous variable (bins). This is a specific, learned schema that differs from the standard bar chart rule.

## The Price <!-- role: costs -->

*   **The Sacrifice:** You may be limited in the aesthetic choices available (e.g., you cannot use a line chart for categorical data just because it looks "cleaner").
*   **The Risk:** Misinterpretation of the data's nature (e.g., inferring values exist between discrete categories in a line chart).

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Using a line chart to connect discrete, unordered categories (e.g., Apples connected to Oranges connected to Bananas).
*   **Why it fails:** It implies a functional relationship or trend between unrelated distinct entities [@zacks_designing_2020].

## How to Check <!-- role: check -->

*   **Visual Sign:** Are distinct categories (names, countries) connected by a line? Are time-series data represented by separate, unconnected bars?
*   **The Test:** Ask a viewer to describe the graph in one sentence. If they describe a "trend" for categorical data, or "separate values" for time-series data, the schema is mismatched.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Change the mark type (Line to Bar, or Bar to Line).
*   **Best Fix:** Ensure the x-axis variable matches the graph choice (Continuous axis = Line; Categorical axis = Bar).
