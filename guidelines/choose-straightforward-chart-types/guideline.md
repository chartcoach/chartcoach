---
id: choose-straightforward-chart-types
title: Choose Chart Types Your Audience Can Read
bibliography: references.bib
description: Prefer chart types that your intended audience can accurately interpret,
  not those chosen by habit, convention, or aesthetics.
labels:
- chart:general
- task:communicate
- visual:position
- impact:clarity
- data:multivariate
- audience:general
- complexity:avoid-unnecessary
---

## The Rule <!-- role: advice -->

Choose the simplest chart type that your intended audience can correctly interpret; do not default to complex or trendy charts out of convention.

## The Logic <!-- role: reason -->

Complex or high-dimensional chart forms can overwhelm viewers, increase cognitive load, and invite incorrect pattern-matching, which raises the risk of misinterpretation and wrong conclusions. In particular, interviews and study findings show that viewers struggled with complex formats like Sankey diagrams and stacked bar charts, leading to misreads and incorrect inferences (e.g., using Sankey diagrams for voter-behavior narratives) [@knoll_gulf_2025].

- **The Principle:** Reduce cognitive load by minimizing unnecessary visual complexity
- **The Evidence:** [@knoll_gulf_2025]

## Where to Apply <!-- role: context -->

This advice is designed for situations where comprehension and correct takeaway matter more than novelty.

- **User Goal:** Understand relationships or comparisons without confusion; reach the correct conclusion
- **Data Type:** Multivariate or flow/part-to-whole data where complex encodings are tempting (e.g., flows, compositions, many categories)
- **Audience:** General audiences, cross-functional stakeholders, or any group unfamiliar with specialized chart types

## When to Break It <!-- role: exceptions -->

Use a more complex chart type only when the added structure is essential and the audience is prepared for it.

- **Scenario:** Expert audiences who regularly work with a specialized chart type (e.g., analysts trained on Sankey flow conventions)
- **Reason:** The audience’s prior knowledge offsets interpretation cost, and the specialized form may reveal structure that simpler charts would hide.

## The Price <!-- role: costs -->

Simplifying chart types can trade richness for readability.

- **The Sacrifice:** Less information density; fewer dimensions shown at once
- **The Risk:** Oversimplification may obscure important nuance or interactions unless paired with small multiples, filters, or drill-downs

## Common Mistakes <!-- role: mistakes -->

Missteps usually come from treating convention or aesthetics as proof of clarity.

- **The Wrong Fix:** Using Sankey diagrams or stacked bar charts because they are common in reports/media or “look explanatory”
- **Why it fails:** Viewers may feel overwhelmed and infer incorrect causal or comparative stories from hard-to-parse encodings [@knoll_gulf_2025]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers ask “What am I looking at?”, misread the direction/meaning of flows, or disagree on the basic takeaway.
- **The Test:** Run a 30-second read test with representative users: ask them to state (1) the main message and (2) one specific value/ordering. If answers vary or are wrong, the chart type is not straightforward enough.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of categories/segments shown; simplify encodings (remove stacked segments, reduce crossings, add direct labels and clear ordering).
- **Best Fix:** Switch to a more interpretable form aligned with the question (e.g., grouped bars or dot plots for comparisons; small multiples for multi-category patterns; simple before/after bars for change; tables when exact reading matters).
