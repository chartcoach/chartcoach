---
id: choose-readable-font-defaults
title: Use Readable, Familiar Fonts for Chart Text
bibliography: references.bib
description: Use font choices and sizes that match what readers comfortably read on
  screens.
labels:
- chart:general
- task:read
- visual:text
- impact:accessibility
- data:general
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use an easy-to-read font style for chart text: familiar sans-serif, regular weight, sentence case, not too narrow/wide, at comfortably readable sizes (around 12px or larger) with near-black text for key copy.

## The Logic <!-- role: reason -->

Readers process text fastest when it matches common on-screen reading patterns. Prioritizing familiarity and legibility prevents the “it won’t fit” spiral that leads to tiny, condensed, hard-to-read labels.

- **The Principle:** Optimize for habitual on-screen reading comfort
- **The Evidence:** [@muth_text_in_data_visualizations_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Read labels, titles, and annotations without strain
- **Data Type:** Any visualization with textual elements (titles, axis labels, annotations, sources)
- **Audience:** Broad audiences, including readers on mobile devices [@muth_text_in_data_visualizations_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** A constrained brand system requires a different typeface.
  - **Reason:** Brand consistency may be a hard requirement; compensate with size, weight, contrast, and reduced text density [@muth_text_in_data_visualizations_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less typographic “flair” or extreme styling.
- **The Risk:** If space is tight, readable defaults may force you to remove text, shorten labels, or redesign layout [@muth_text_in_data_visualizations_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Shrinking text or switching to very narrow fonts just to make everything fit.
  - **Why it fails:** Legibility collapses; the chart becomes unpleasant to read [@muth_text_in_data_visualizations_2022].
- **The Wrong Fix:** Keeping dense tiny labels instead of using tooltips or reducing what’s shown.
  - **Why it fails:** Prioritizes completeness over readability [@muth_text_in_data_visualizations_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Labels feel cramped, thin, or tiny; you have to zoom to read them comfortably.
- **The Test:** View at typical embed size and on a phone-width layout; if you need to squint or zoom, increase legibility or reduce text load [@muth_text_in_data_visualizations_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase font size and contrast for essential text; remove or hide the least important labels.
- **Best Fix:** Reduce label length, enlarge the visualization where possible, and move secondary detail to tooltips or below-chart notes (especially for mobile) [@muth_text_in_data_visualizations_2022].
