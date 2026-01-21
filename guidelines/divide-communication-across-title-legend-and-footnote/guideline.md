---
id: divide-communication-across-title-legend-and-footnote
title: Assign Clear Jobs to Title, Legend, and Footnote
bibliography: references.bib
description: Use the title to state the question, the legend to define the encoded
  measure, and the footnote to disclose only essential assumptions and sourcing.
labels:
- chart:map
- task:explain
- visual:text
- impact:clarity
- data:geospatial
- audience:novice
- source:datawrapper-fix-my-chart
---

## The Rule <!-- role: advice -->

Give each text element one job: use the **title** to state the reader question, the **legend/color key** to define what color means, and the **footnote** to include only the minimum context and source needed to interpret the map.

## The Logic <!-- role: reason -->

Separating responsibilities across text elements reduces cognitive load and prevents readers from hunting for definitions or wading through irrelevant detail; it also ensures the key interpretation steps appear where readers look for them first (title for purpose, legend for decoding, footnote for provenance), as demonstrated in the redesign decisions in [@mintzer_fix_my_chart_text_elements_2024].

- **The Principle:** Strategic text hierarchy (purpose → decoding → provenance)
- **The Evidence:** [@mintzer_fix_my_chart_text_elements_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly understand what the visualization is for, how to read it, and what assumptions/sources underpin it
- **Data Type:** Predictive or modeled data shown on a choropleth (or similar map with a color scale)
- **Audience:** General or mixed audiences who won’t infer methodology or encoding details on their own

## When to Break It <!-- role: exceptions -->

- **Scenario:** A technical report where methodology is the primary content, not just supporting context
- **Reason:** The “minimum footnote” approach can under-serve readers who must audit model inputs and assumptions in-place rather than via a link, which goes beyond the lightweight framing recommended in [@mintzer_fix_my_chart_text_elements_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less room for nuanced caveats directly on the graphic
- **The Risk:** If you cut too much, readers may over-trust projections or miss important limitations

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Stuffing the title, legend, and footnote with overlapping explanations of purpose, encoding, and methodology
- **Why it fails:** Redundancy and long blocks of text bury the decoding instructions and make the map feel harder than it is, the exact problem addressed in [@mintzer_fix_my_chart_text_elements_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** The title reads like a paragraph, the legend uses coded labels that need explanation, and the footnote is longer than a couple of concise lines
- **The Test:** Ask a reader to answer: (1) “What question does this map answer?” (2) “What does color mean?” (3) “What do I need to know about the data/source?” If they search across multiple places for each answer, the jobs aren’t separated.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Rewrite the title as a single question; rewrite the legend so it directly defines the measured variable; trim the footnote to the essential limitation(s) plus a source link, as in [@mintzer_fix_my_chart_text_elements_2024].
- **Best Fix:** Rebuild the text hierarchy intentionally: one-sentence title question, legend phrased in units/timeframe, and a short footnote that only covers what’s necessary to interpret the map (with the full methodology kept in the source link), following the approach in [@mintzer_fix_my_chart_text_elements_2024].
