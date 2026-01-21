---
id: reuse-category-colors-in-annotations-to-reinforce-meaning
title: Reuse Category Colors in Annotations
bibliography: references.bib
description: Color the category words in annotations to reinforce color meanings right
  next to the relevant data points.
labels:
- chart:multi
- task:explain
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- component:annotation
---

## The Rule <!-- role: advice -->

When annotating a specific data point, color only the category word(s) in the annotation using the same category color used in the chart, and place the annotation right next to that data point.

## The Logic <!-- role: reason -->

Annotations sit closer to the marks than a legend, so reusing the same category color in annotation text reinforces the mapping without forcing readers to look back and forth between data and key. It also directs attention to the intended category by repeating its visual cue.

- **The Principle:** Reinforce categorical color associations at the point of attention
- **The Evidence:** [@muth_remind_colors_2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand what a highlighted data point represents and why it matters
- **Data Type:** Categorical series (lines, stacked segments, groups) where color encodes category identity
- **Audience:** Broad audiences reading a narrative or explanatory chart [@muth_remind_colors_2023]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The category color is too bright to be legible as thin text and you can’t adjust it (e.g., strict brand constraints).
- **Reason:** The post cautions that colors readable as marks can become illegible as text; readability must come first. [@muth_remind_colors_2023]

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra design effort to selectively color parts of text and manage contrast.
- **The Risk:** If contrast is poor, colored words become hard to read and the annotation fails its primary job. [@muth_remind_colors_2023]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Coloring the whole sentence (or coloring words that describe the trend, like “decreased”) with the category color.
- **Why it fails:** It miscommunicates what the color stands for—category identity, not the direction of change. [@muth_remind_colors_2023]

## How to Check <!-- role: check -->

- **Visual Sign:** Colored annotation text that is hard to read or that seems to encode “increase/decrease” rather than the category name.
- **The Test:** Ask: “If I only read the colored word(s), do I get the category name?” If not, the color is applied to the wrong text. [@muth_remind_colors_2023]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Limit color to the category name only, and darken the text color slightly relative to the mark color to improve legibility.
- **Best Fix:** Use the category color as a background highlight behind the category word(s) (instead of coloring the letters) to preserve readability while maintaining the association. [@muth_remind_colors_2023]
