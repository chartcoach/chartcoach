---
id: explain-chart-purpose-and-how-to-read
title: "Explain the chart\u2019s purpose and how to read it (in visible supporting\
  \ text)"
bibliography: references.bib
description: Add a clear purpose statement and a brief reading guide so viewers can
  interpret the visualization correctly with less cognitive effort.
labels:
- chart:any
- task:interpret
- visual:text
- impact:clarity
- data:any
- audience:novice
- accessibility:understandable
- chartability:critical
---

## Explain the chart’s purpose and how to read it <!-- role: advice -->

Explain what the chart is for and how to read, use, and interpret it in visible supporting text near the visualization. Keep the explanation specific to the encodings and interaction needed to understand the message.

## Purpose-and-reading guidance reduces misinterpretation <!-- role: reason -->

Adding explicit purpose and reading guidance makes the intended takeaway and the decoding steps available without relying on the viewer to infer them, which reduces ambiguity and cognitive load when interpreting a visualization.

**Mechanism:** A descriptive title and supporting text externalize the “how to decode” and “what matters” knowledge that creators often assume viewers already have.

**Evidence:** Visualizations with descriptive titles and supporting text were more likely to be correctly recognized and recalled in a study of recognition and recall across many visualizations [@xiong_curse_of_2020]. A critical accessibility heuristic for understandable visualizations is to explain purpose and how to read the chart so people are not left guessing how to interpret even simple visuals [@elavskyHowAccessibleMy2022].

**Notes:** This guideline targets interpretation failures that can occur even when a visualization is technically compliant with labeling or purpose-identification requirements.

## Where purpose-and-reading explanations are needed <!-- role: context -->

- **User Goal:** Understand what the visualization is communicating and extract the intended takeaway.
- **Task:** Interpret encodings and map marks, axes, categories, and interactions to meaning.
- **Data:** Any data where decoding requires domain assumptions or non-obvious mappings.
- **Chart Setting:** Static or interactive visualizations where meaning depends on how to read the chart or how to use interaction.
- **Audience:** Mixed or general audiences, especially people unfamiliar with the chart type, domain, or interaction patterns.
- **Success Criterion:** Viewers can accurately explain what the chart shows and how to read it without additional guidance.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization is not intended to be interpreted on its own (for example, it is always presented with an accompanying narrative that already explains purpose and reading). **Why:** Adding a second, redundant explanation can be unnecessary and may distract from the primary narrative.

## Tradeoffs of adding purpose-and-reading text <!-- role: costs -->

**Sacrifice:** Additional space in the layout for explanatory text. **Risk:** Overlong or overly detailed guidance can increase reading burden. **Mitigation:** Keep the text brief and tightly tied to what the viewer must know to decode the visualization.

## Common ways this fails in practice <!-- role: mistakes -->

**Mistake:** Using a generic title (for example, a dataset or metric name) with no supporting explanation. **Why it fails:** Viewers must infer the intended takeaway and may misinterpret what the chart is “for” [@xiong_curse_of_2020].\
**Mistake:** Assuming the encoding is self-evident and providing no “how to read” guidance. **Why it fails:** Even simple visualizations can be hard to interpret without explicit decoding instructions and purpose framing [@elavskyHowAccessibleMy2022].

## Quick tests for missing explanations <!-- role: check -->

**Failure Sign:** A viewer can describe what is drawn but cannot explain what it means or what conclusion to take away. **Quick Check:** Hide the visualization and read only the title and supporting text; if you cannot tell what the chart is about and how to read it, the explanation is insufficient. **Stronger Test:** Ask a small set of viewers to summarize the chart’s takeaway and explain how they read it; frequent confusion indicates missing or unclear guidance [@xiong_curse_of_2020].

## Ways to fix a chart with no purpose or reading guidance <!-- role: fix -->

- Add a descriptive title that states the intended takeaway rather than only naming the topic or dataset [@xiong_curse_of_2020].
- Add short supporting text that explains what the viewer should look at and how the encodings map to meaning [@elavskyHowAccessibleMy2022].
- Add a brief instruction for any required interaction needed to interpret the chart (for example, what happens when selecting or hovering) [@elavskyHowAccessibleMy2022].
- If the visualization depends on assumed domain knowledge, add a short definition of the key measure or concept needed to interpret it [@elavskyHowAccessibleMy2022].
