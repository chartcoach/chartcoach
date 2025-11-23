---
id: use-text-axis-labels
title: Use Text for Axis Labels
bibliography: references.bib
description: Use text labels for axes instead of pictographs to ensure faster recognition
  and better memory of data values.
labels:
- chart:bar
- chart:isotype
- visual:text
- visual:icons
- impact:readability
---

## The Rule <!-- role: advice -->
Use text to label the categories on your axes. Do not replace text labels with icons or pictographs.

## The Logic <!-- role: reason -->
Text reading is a highly automatic, over-learned process for most adults. [@haroz_isotype_2015] found that using pictographs as axis labels resulted in significantly higher error rates in memory tasks compared to simple text labels. Text labels may facilitate better memory links between the category and the data value.

*   **The Principle:** Automaticity of Reading
*   **The Evidence:** Experiment 1 in [@haroz_isotype_2015] showed that regardless of the chart type (stacked or stretched), using icon-only labels increased error.

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying categories and remembering associated values.
*   **Data Type:** Categorical axes.
*   **Audience:** Literate users.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Illiterate audiences or language-agnostic international signage.
*   **Reason:** While [@haroz_isotype_2015] tested university students, populations unable to read the text would naturally necessitate pictorial labels.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual compactness (sometimes icons are smaller than long words) and language independence.
*   **The Risk:** Users might misinterpret the icon if the metaphor is ambiguous.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using an icon *and* text when space is tight, or using just the icon to save space.
*   **Why it fails:** The study suggests the text is the primary driver of efficient encoding. Removing it hurts performance.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there pictures at the base of your bars instead of words?
*   **The Test:** Ask a user to read the chart out loud. If they hesitate to name the category, the icon is likely slowing them down.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add the text label back.
*   **Best Fix:** Remove the axis icon entirely and rely on clear, legible typography for the category labels.
