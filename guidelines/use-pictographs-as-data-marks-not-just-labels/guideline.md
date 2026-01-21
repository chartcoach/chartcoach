---
id: use-pictographs-as-data-marks-not-just-labels
title: Use Pictographs as Data Marks, Not Just Labels
bibliography: references.bib
description: If you use pictographs, integrate them into the data encoding rather
  than replacing axis labels.
labels:
- chart:bar
- task:read
- visual:glyph
- impact:clarity
- data:categorical
- audience:general
- embellishment:labeling
- source:haroz-chi2015
---

## The Rule <!-- role: advice -->

Do not replace clear text axis labels with pictographs; if you use pictographs, use them to encode the data marks instead.

## The Logic <!-- role: reason -->

Replacing text labels with pictographs increased error in working-memory recall, likely because text labels are recognized quickly and/or bind more effectively to values in memory, while pictograph labels add decoding effort without improving the value encoding.

- **The Principle:** Efficient label recognition supports faster, cleaner encoding
- **The Evidence:** Pictograph x-axis labels produced higher recall error across chart types in Exp. 1, while using pictographs as response prompts did not help [@harozISOTYPEVisualizationWorking2015a].

## Where to Apply <!-- role: context -->

- **User Goal:** Accurately remember recently viewed chart values (working memory)
- **Data Type:** Categorical bar-like charts with a small number of categories
- **Audience:** General audiences under time pressure or cognitive load

## When to Break It <!-- role: exceptions -->

- **Scenario:** The text labels are not succinct/unambiguous (e.g., hard-to-read, unfamiliar, or lengthy labels)
- **Reason:** The paper notes the labels used were succinct and easy to read; the disadvantage of pictograph labels may depend on text being especially efficient in that setting [@harozISOTYPEVisualizationWorking2015a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced “icon-driven” styling on axes
- **The Risk:** Viewers may feel the chart is less playful or thematic [@harozISOTYPEVisualizationWorking2015a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Swapping every category name for an icon to “make it universal”
- **Why it fails:** The tested memory task became less accurate with pictograph axis labels, suggesting added interpretive overhead [@harozISOTYPEVisualizationWorking2015a].

## How to Check <!-- role: check -->

- **Visual Sign:** Categories on the x-axis are icons with little/no text
- **The Test:** Ask a user to recall the three values after a brief glance; compare error with text labels vs pictograph labels (same chart otherwise) [@harozISOTYPEVisualizationWorking2015a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Restore text labels on the axis.
- **Best Fix:** Move pictographs into the marks (e.g., pictograph bars or stacks) while keeping axes unlabeled or text-labeled as appropriate [@harozISOTYPEVisualizationWorking2015a].
