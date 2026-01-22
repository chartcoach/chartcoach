---
id: separate-core-restatements-from-context-in-simple-gap-charts
title: Attach core data restatements as chart annotations, and move context to subtitle
  or footnote
bibliography: references.bib
description: Keep the main message close to the marks by annotating direct restatements
  of the data and relocating extra context to supporting text.
labels:
- chart:area
- task:communicate
- visual:annotation
- impact:clarity
- data:temporal
- audience:general
- complexity:basic
---

## Keep restatements on-chart and push context outward <!-- role: advice -->

Write direct restatements of what the chart already shows as annotations on the chart, and move added contextual information to the subtitle or footnote. Keep the chart area focused on what viewers must notice first.

## Why proximity of text to marks clarifies interpretation <!-- role: reason -->

When the most important interpretation is placed right where viewers look to read values and patterns, the chart communicates the takeaway without forcing people to shuttle between the plot and supporting text. Separating “what the data says” from “what we add about the data” also prevents secondary details from competing with the core message.

**Mechanism:** On-chart annotations act as a built-in explanation tied to the marks, while subtitle/footnote placement delays secondary context until after the main pattern is understood.

**Evidence:** Distinguishing between restatements of the core data and added information, then keeping restatements closer to the chart (as annotations) while moving other information to subtitle or footnote, helps the simplicity of the data “shine through” and makes the key gap easier to grasp [@mintzer_simple_data_2024].

**Notes:** Use the subtitle for context that should shape interpretation early, and the footnote for details that can wait until later.

## When to use proximity-based text hierarchy <!-- role: context -->

- **User Goal:** Understand the chart’s main takeaway quickly and correctly.
- **Task:** Interpret a stark difference or gap (e.g., reported vs. solved) over time.
- **Data:** Simple series with a large, visually obvious disparity; low need for multi-step analysis.
- **Chart Setting:** Static chart in an article/report where text can be layered as title/subtitle/annotations/footnote.
- **Audience:** Broad audience, including readers with limited time or domain knowledge.
- **Success Criterion:** Readers can state the main takeaway after a brief glance without reading surrounding paragraphs.

## When not to use this text hierarchy <!-- role: exceptions -->

**Break it when:** The chart’s interpretation depends on substantial methodological caveats or definitions that must be understood before reading the marks. **Why:** Delaying essential definitions to subtitle/footnote can cause readers to form the wrong interpretation first.

## Tradeoffs of annotation-first messaging <!-- role: costs -->

**Sacrifice:** You give up some visual space inside the plotting area for text. **Risk:** Too many annotations can clutter the chart and become a second layer of noise. **Mitigation:** Keep annotations to the minimum needed to express the single key restatement.

## Common ways this goes wrong <!-- role: mistakes -->

- **Mistake:** Putting key takeaways only in a legend, caption, or surrounding paragraph. **Why it fails:** Readers may not connect the text to the marks at the moment they need it, weakening the takeaway.
- **Mistake:** Mixing core restatements and extra context together in the same prominent on-chart callout. **Why it fails:** Secondary details compete with the primary message and reduce the perceived simplicity of the data.

## Quick ways to verify the hierarchy works <!-- role: check -->

**Failure Sign:** A reader can describe the topic but cannot state the chart’s main quantitative takeaway (e.g., the small solved share) after a short glance. **Quick Check:** Hide the subtitle and footnote and see whether the on-chart annotation still communicates the core point. **Stronger Test:** Ask a colleague to summarize the chart in one sentence after viewing it briefly; verify they mention the intended restatement.

## Practical fixes if the message still feels muddy <!-- role: fix -->

- Add a short on-chart annotation that directly restates the key relationship the marks show (e.g., the solved percentage) in plain language.
- Convert the legend into a direct, in-plot explanation (a text key) so readers don’t have to search for what areas/colors mean.
- Move interpretive-but-nonessential details (e.g., background facts about suspects or locations) from the plot area to subtitle or footnote.
- Remove or shorten any on-chart text that does not restate the data or explain encodings.
