---
id: assign-title-legend-footnote-separate-jobs-and-keep-each-short
title: "Assign title, legend, and footnote separate jobs\u2014and keep each short"
bibliography: references.bib
description: 'Use each text element for a distinct purpose: title for the reader question,
  legend for the mapped measure, and footnote for essential assumptions and sourcing.'
labels:
- chart:map
- task:explain
- visual:text
- impact:clarity
- data:spatial
- audience:novice
- complexity:basic
---

## Give each map text element one job: question in the title, measure in the legend, and only essentials in the footnote <!-- role: advice -->

Make the title state the reader-facing question, make the legend explain the mapped measure directly, and keep the footnote to only what’s necessary to interpret the map plus the data source.

## Why separating the “jobs” of text reduces cognitive load <!-- role: reason -->

When the title, legend, and footnote each do one distinct communication task, readers can form a correct mental model quickly: they learn what the map is for (title), what colors mean (legend), and what caveats matter (footnote) without hunting across long or redundant text.

**Mechanism:** A clear division of labor between text elements removes extra translation steps (like decoding a rating scheme before understanding the underlying metric), and reduces the chance that critical context is buried in dense prose.

**Evidence:** A map critique centered on “strategically divide the work of communication” recommends using the title to spell out the practical question, the legend to directly define the mapped variable (instead of an abstract star system), and the footnote to retain only essential assumptions and the source [@mintzer_fix_my_chart_text_elements_2024].

**Notes:** This approach is especially helpful when the data involves projections, where readers need both a crisp takeaway and minimal, relevant caveats.

## When a map needs a communication plan across title/legend/footnote <!-- role: context -->

- **User Goal:** Understand what the map is answering and how to read it without extra explanation.
- **Task:** Interpret color meaning correctly and connect it to a real-world decision.
- **Data:** Spatial data (e.g., counties) with a quantified measure (e.g., projected number of hot days).
- **Chart Setting:** A thematic map with a color key and limited on-chart space for explanation.
- **Audience:** General readers or tool novices who may not tolerate extra decoding steps.
- **Success Criterion:** Readers can accurately explain what the colors represent and what the map is for after a quick glance.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The graphic has no legend/footnote area (e.g., extremely small embed) and the meaning must be carried by a single text element. **Why:** The separation is constrained by available space, so consolidating becomes necessary.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may omit interesting methodological details that some readers would like. **Risk:** Over-trimming can remove a caveat that changes interpretation (especially for predictions). **Mitigation:** Preserve the single most decision-relevant limitation and a clear source link.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using an abstract rating scheme (e.g., “stars”) in the legend instead of naming the measured quantity. **Why it fails:** Readers must decode an extra layer before they can interpret the map’s colors.
- **Mistake:** Putting long, multi-topic explanations in the footnote. **Why it fails:** Important information becomes hard to find, and the map’s reading flow slows down.

## Quick tests <!-- role: check -->

**Failure Sign:** Readers ask “What do the colors actually measure?” or “What is this map trying to answer?” **Quick Check:** Hide the footnote and ask if the title and legend alone let someone paraphrase the purpose and the metric. **Stronger Test:** Ask a first-time viewer to explain the map in one sentence; if they mention stars/ratings instead of the metric, the legend is too abstract.

## What to do instead <!-- role: fix -->

- Rewrite the title as a direct question that matches the reader’s decision (e.g., “Where can I go to escape extreme summer heat?”).
- Replace rating labels with the actual variable name and units in the legend (e.g., “Days over 90°F expected in summer 2050”).
- Reduce the footnote to a single-scope caveat that affects interpretation plus the data source link.
- Move any extra methodological detail to a separate linked note or description outside the chart.
