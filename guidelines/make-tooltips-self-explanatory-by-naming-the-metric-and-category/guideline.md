---
id: make-tooltips-self-explanatory-by-naming-the-metric-and-category
title: Make tooltips self-explanatory by naming the metric and category
bibliography: references.bib
description: Write tooltips so values include what they refer to, not just the number.
labels:
- chart:general
- task:interpret
- visual:text
- impact:clarity
- data:quantitative
- audience:novice
- complexity:basic
---

## Write tooltips that restate what the number represents <!-- role: advice -->

In tooltips, include the metric and/or category alongside the value (for example, “3.4% unemployed” rather than “3.4%”). Ensure the tooltip teaches or reminds readers what they are looking at.

## Tooltips are read in isolation from surrounding context <!-- role: reason -->

Hover states often appear away from titles, legends, and axis labels, and readers may encounter them while focusing on a single mark. If the tooltip shows only a number, the meaning can be ambiguous; adding short descriptive text anchors the value to the variable and category.

**Mechanism:** Contextual tooltip phrasing reduces ambiguity and prevents readers from needing to look elsewhere to interpret the value.

**Evidence:** Tooltips should repeat what the visualization shows by including the category/metric in addition to numbers, helping readers understand and remember what they’re seeing [@muth_text_in_data_visualizations_2022].

**Notes:** This is especially important when multiple measures, series, or units exist.

## Use when tooltips provide precise values <!-- role: context -->

- **User Goal:** Learn exact values for specific marks without losing meaning.
- **Task:** Hover-and-read value lookup; compare points across series.
- **Data:** Quantitative values where the same numeric format could apply to multiple measures.
- **Chart Setting:** Interactive charts with hover tooltips.
- **Audience:** General audiences; readers who did not study the title/legend first.
- **Success Criterion:** A tooltip can be understood correctly even if read alone.

## When bare numbers can be enough <!-- role: exceptions -->

**Break it when:** The tooltip appears immediately adjacent to an already-explicit label that unambiguously names the metric and category. **Why:** Repeating the same words may add noise without improving understanding.

## Trade brevity for clarity <!-- role: costs -->

**Sacrifice:** Slightly longer tooltips and more writing effort. **Risk:** Overly wordy tooltips can slow scanning. **Mitigation:** Use short noun phrases (“Unemployment: 3.4%”) rather than sentences.

## Common tooltip anti-patterns <!-- role: mistakes -->

**Mistake:** Tooltips that show only a number (and maybe a date) without naming the metric. **Why it fails:** Readers must infer meaning from memory or hunt for context elsewhere.

## Quick tests <!-- role: check -->

**Failure Sign:** A tooltip value could be misread as a different measure (percent vs. currency, change vs. level). **Quick Check:** Screenshot a tooltip alone; if it’s unclear what it refers to, it needs text. **Stronger Test:** Ask someone to interpret a tooltip without seeing the title; errors indicate missing context.

## Fixes that preserve space <!-- role: fix -->

- Add a short metric label before the value (for example, “Revenue change: +16%”).
- Include the category name in the tooltip when multiple series exist.
- Repeat units in the tooltip even if they appear on the axis.
- Remove nonessential tooltip fields so the remaining text can name the metric clearly.
