---
id: reuse-category-colors-in-surrounding-text-to-remind-mappings
title: Reuse category colors in titles, descriptions, or surrounding text to function
  as a color key
bibliography: references.bib
description: Integrate category colors into adjacent text so readers learn and recall
  what each color stands for.
labels:
- chart:multiple
- task:interpret
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:annotation
---

## Use category colors in adjacent text to restate what the colors mean <!-- role: advice -->

Repeat category colors in the title, description, or surrounding article text so the text itself reminds readers which colors correspond to which categories.

## Why textual repetition reinforces the color-category association <!-- role: reason -->

Readers don’t always start at the legend, and long-form reading shifts attention between chart and narrative. When text uses the same category colors, it creates repeated exposure to the mapping and reduces the effort needed to translate colors back into names.

**Mechanism:** Repetition of consistent visual cues across chart and narrative strengthens recognition and reduces reliance on a single legend location.

**Evidence:** Using category colors in titles/descriptions can explicitly teach readers what each color stands for, sometimes allowing the text to serve as the primary color key [@muth_remind_colors_2023]. Reusing colors in surrounding text is also used to deepen integration between narrative and visualization, including in scrollytelling where overlays change with the visualization state [@muth_remind_colors_2023].

**Notes:** Blue-colored text may be perceived as a hyperlink, which can confuse readers if blue is used as a category color.

## When color-coded surrounding text applies <!-- role: context -->

- **User Goal:** Understand the meaning of colors while reading a chart within a narrative.
- **Task:** Map narrative entities (groups, regions, parties, time periods) to colored marks.
- **Data:** Categorical groupings encoded by color.
- **Chart Setting:** Articles, reports, dashboards with descriptive text; scrollytelling with changing states.
- **Audience:** Readers who may enter the content at different points (not necessarily starting at the top).
- **Success Criterion:** Readers can learn or recall the mapping from the text without hunting for a traditional legend.

## When not to follow it <!-- role: exceptions -->

**Break it when:** A category color closely resembles conventional link styling (especially blue text) and the text is not a link. **Why:** Readers may misinterpret category-colored terms as interactive links and get distracted or confused [@muth_remind_colors_2023].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Editorial and design effort to coordinate consistent coloring across chart and text. **Risk:** Text can become visually busy, making the color key feel more prominent than the data. **Mitigation:** Keep colored text limited to category names and avoid coloring long phrases.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using colored text so prominently that it dominates the visualization’s visual hierarchy. **Why it fails:** Readers focus on the “key-like” text styling instead of the data marks, reducing the chart’s readability [@muth_remind_colors_2023].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers comment on the colored text more than the data, or attempt to click category-colored words expecting links. **Quick Check:** Scan the page and verify that the data marks remain the primary focus. **Stronger Test:** Ask a reader to explain the color mapping after reading only the title/description; they should be able to state it correctly.

## What to do instead <!-- role: fix -->

- Add a compact traditional color key near the chart while still using occasional colored category words in the text.
- Use direct labels on key marks/lines so the chart can be read with less legend dependence.
- Replace colored text with subtle colored swatches or chips next to category names to avoid link-like styling.
- If the narrative is long, repeat the mapping summary at section breaks near where the chart is discussed.
