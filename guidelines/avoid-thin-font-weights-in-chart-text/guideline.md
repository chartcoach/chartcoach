---
id: avoid-thin-font-weights-in-chart-text
title: Avoid Very Thin Font Weights
bibliography: references.bib
description: "Don\u2019t use thin/light weights for chart text because they reduce\
  \ perceived contrast and become hard to read."
labels:
- chart:general
- task:read
- visual:typography
- impact:accessibility
- data:general
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Avoid very thin or light font weights for chart and table text; use them only in large sizes and high-contrast colors (typically titles).

## The Logic <!-- role: reason -->

Thin strokes reduce perceived darkness (they can look like a lighter color) and become difficult to read, especially at small sizes common in visualization labels and annotations [@muth_fonts_2022].

- **The Principle:** Stroke thickness drives legibility and perceived contrast
- **The Evidence:** [@muth_fonts_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Reading labels, notes, and axis ticks quickly and accurately
- **Data Type:** Any visualization with small text elements
- **Audience:** Broad audiences, including readers on smaller or lower-quality screens

## When to Break It <!-- role: exceptions -->

- **Scenario:** Large, display-sized titles where thin weight is part of the intended aesthetic.
- **Reason:** The post notes thin weights can be used when the color is high-contrast and the size is big—often for titles only [@muth_fonts_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less “airy/minimal” look if you move from thin to regular.
- **The Risk:** If you insist on thin weights, text may fail basic readability expectations for many readers and contexts [@muth_fonts_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using thin weights to make text feel “less important” instead of adjusting color/size/hierarchy.
- **Why it fails:** Thin text quickly becomes illegible, especially in small annotation sizes [@muth_fonts_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Text looks gray even when set to black; small labels feel faint or disappear at a glance.
- **The Test:** View the chart at typical reading size and distance; if labels are hard to read without effort, the weight is too thin [@muth_fonts_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Change thin/light text to regular (normal) weight and keep the same font size [@muth_fonts_2022].
- **Best Fix:** Use regular/medium weights for most text and reserve thin weights for large, high-contrast titles if you truly need the style [@muth_fonts_2022].
