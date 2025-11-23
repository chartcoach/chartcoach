---
id: limit-bold-weights
title: Use bold text only for emphasis
bibliography: references.bib
description: Restrict bold weights to titles and highlights to maintain readability.
labels:
- visual:typography
- visual:hierarchy
- impact:readability
- task:highlight
---

## The Rule <!-- role: advice -->

Set the majority of your text (descriptions, notes, axis labels) in regular or medium font weights. Use bold text only for titles or to emphasize specific data points.

## The Logic <!-- role: reason -->

Bold (or "black") text feels self-confident and grabs attention. However, for longer text blocks, regular weights are easier to read. Overusing bold reduces its ability to act as a highlighter; if everything is bold, nothing is emphasized.

*   **The Principle:** Visual Hierarchy
*   **The Evidence:** [@muth_fonts_2022] suggests restricting bold to titles or emphasizing a few words in annotations, citing examples from *The Washington Post*.

## Where to Apply <!-- role: context -->

*   **User Goal:** distinguishing important signals from context.
*   **Data Type:** Annotations, chart titles, highlighted values.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Multiplexed fonts in tables.
*   **Reason:** If you need to highlight a number in a table without changing the column width/alignment, bolding is acceptable if the font is multiplexed (uni-width) [@muth_fonts_2022].

## The Price <!-- role: costs -->

*   **The Sacrifice:** You cannot use bold for pure aesthetics if it conflicts with the data hierarchy.
*   **The Risk:** Using bold for all axes and labels makes the chart look "heavy" and distracts from the actual data bars or lines.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Bolding the entire paragraph to make it "readable."
*   **Why it fails:** It increases cognitive load and makes the text block look dense.

## How to Check <!-- role: check -->

*   **Visual Sign:** Does the text compete with the data visualization for attention?
*   **The Test:** Squint at the chart. If the axis labels are as dark/heavy as the bars/lines, the text is likely too bold.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Change font-weight to 400 (Regular) for all non-title text.
*   **Best Fix:** Use a hierarchy: Bold (700) for titles/highlights, Regular (400) for body text, and potentially a lighter shade (gray) for context notes.
