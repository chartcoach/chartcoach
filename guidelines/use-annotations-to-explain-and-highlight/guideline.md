---
id: use-annotations-to-explain-and-highlight
title: Annotate What Needs Explaining
bibliography: references.bib
description: Use annotations to explain unusual patterns, clarify custom elements,
  and guide readers to what matters.
labels:
- chart:general
- task:explain
- visual:text
- impact:clarity
- data:general
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Add annotations to explain non-obvious design elements, highlight important data points/series, and provide necessary context directly on the visualization.

## The Logic <!-- role: reason -->

Annotations guide attention and add interpretation at the point of need, helping readers understand why something matters and how to read custom elements (ranges, connectors, dotted lines). They can also make the visual more engaging by signaling “something worth noticing here.”

- **The Principle:** Guided attention + embedded explanation
- **The Evidence:** [@muth_text_in_data_visualizations_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand the story/insight (outliers, turning points, ranges) rather than only the raw values
- **Data Type:** Explanatory charts/maps, especially with notable events, outliers, or added design elements needing explanation
- **Audience:** General public readers who benefit from guidance on what to look at [@muth_text_in_data_visualizations_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The goal is exploratory/neutral reading where highlighting specific points would bias interpretation.
  - **Reason:** Annotations can steer attention toward an editorial framing that isn’t desired [@muth_text_in_data_visualizations_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** More text and layout complexity.
- **The Risk:** Over-annotation can clutter the chart and compete with the data; on small screens, annotations may need to be hidden or moved [@muth_text_in_data_visualizations_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a long description paragraph instead of targeted on-chart notes.
  - **Why it fails:** Readers must shuttle between text and marks; key insights get missed [@muth_text_in_data_visualizations_2022].
- **The Wrong Fix:** Annotating everything.
  - **Why it fails:** Removes hierarchy and makes the chart feel busy and hard to parse [@muth_text_in_data_visualizations_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Important features (outliers, ranges, unusual lines) are visible but unexplained, leaving readers to guess their meaning.
- **The Test:** Ask, “Could a reader misunderstand this element without extra text?” If yes, add a concise annotation placed next to it [@muth_text_in_data_visualizations_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add 1–3 short annotations pointing to the key insight(s) and any non-standard elements (e.g., “Dotted line represents…”).
- **Best Fix:** Place annotations adjacent to the relevant marks, keep a clear text hierarchy (important notes emphasized, minor notes subdued), and hide/move less important notes on mobile if needed [@muth_text_in_data_visualizations_2022].
