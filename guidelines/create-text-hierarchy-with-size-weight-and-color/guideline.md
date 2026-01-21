---
id: create-text-hierarchy-with-size-weight-and-color
title: Create a Clear Text Hierarchy
bibliography: references.bib
description: Use font size, weight, and color contrast to signal what readers should
  read first vs. later.
labels:
- chart:general
- task:emphasize
- visual:text
- impact:clarity
- data:general
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use font size, weight, and contrast to make the most important text stand out (often the title), and de-emphasize supporting text (descriptions, sources) with smaller, lighter, grayer styling.

## The Logic <!-- role: reason -->

Readers follow visual salience: larger, bolder, higher-contrast text is read first. A deliberate hierarchy controls reading order and prevents secondary metadata from competing with the message.

- **The Principle:** Visual salience determines reading sequence
- **The Evidence:** [@muth_text_in_data_visualizations_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand the main message quickly, then drill into details
- **Data Type:** Any chart with multiple text elements (title, subtitle/description, annotations, source)
- **Audience:** General audiences scanning quickly [@muth_text_in_data_visualizations_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** A particular detail (e.g., a critical caveat) must not be missed.
  - **Reason:** The caveat becomes primary information and should be promoted in the hierarchy (e.g., as an annotation or part of the title) [@muth_text_in_data_visualizations_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some information becomes less noticeable by design.
- **The Risk:** If hierarchy is misjudged, readers may miss important context that was styled too quietly [@muth_text_in_data_visualizations_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Making many elements bold/large to ensure they’re “seen.”
  - **Why it fails:** Collapses hierarchy; everything competes and nothing stands out [@muth_text_in_data_visualizations_2022].
- **The Wrong Fix:** Using high-contrast styling for sources/notes equal to the title.
  - **Why it fails:** Distracts from the intended message and slows entry into the chart [@muth_text_in_data_visualizations_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Your eye doesn’t immediately land on a single clear entry point; multiple text blocks compete.
- **The Test:** Start with all text subdued (small/thin/gray), then promote only what must be read first; if you keep promoting many items, the hierarchy isn’t working [@muth_text_in_data_visualizations_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce contrast/weight/size of secondary text (source, notes), and increase emphasis on the title or key annotation.
- **Best Fix:** Define 2–3 explicit hierarchy levels (primary message, secondary explanation, metadata) and apply styling consistently across all text elements [@muth_text_in_data_visualizations_2022].
