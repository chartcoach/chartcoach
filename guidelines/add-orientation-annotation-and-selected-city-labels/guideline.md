---
id: add-orientation-annotation-and-selected-city-labels
title: Add a Brief Orientation Annotation and Targeted Place Labels
bibliography: references.bib
description: "Use a short annotation to communicate the author\u2019s perspective\
  \ and add select city labels to guide readers to actionable locations."
labels:
- chart:map
- task:orient
- visual:text
- impact:clarity
- data:geospatial
- audience:novice
- custom:annotation
- source:datawrapper-fix-my-chart
---

## The Rule <!-- role: advice -->

Add one short annotation that states the viewpoint or use-case, and add a small set of city labels to help readers locate relevant places.

## The Logic <!-- role: reason -->

A map can be hard to “enter” without anchors; a concise annotation frames the reader’s perspective (why this map exists), and targeted labels provide recognizable reference points that turn a pattern into potential answers—an explicit “bonus text” recommendation in [@mintzer_fix_my_chart_text_elements_2024].

- **The Principle:** Orientation and wayfinding through textual anchors
- **The Evidence:** [@mintzer_fix_my_chart_text_elements_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Translate a geographic pattern into an actionable shortlist of locations
- **Data Type:** County-/region-level choropleths where many small areas are hard to recognize
- **Audience:** Readers unfamiliar with the geography or who need quick bearings

## When to Break It <!-- role: exceptions -->

- **Scenario:** Extremely dense labeling would clutter the map or compete with the color pattern
- **Reason:** If labels dominate the visual, they defeat the map’s primary encoding; the post suggests adding labels to help, not overwhelm [@mintzer_fix_my_chart_text_elements_2024].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less visual simplicity and some additional design time
- **The Risk:** Too many labels/long annotations can create clutter and reduce readability

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Labeling many cities/counties “for completeness”
- **Why it fails:** Labels become noise, obscuring the choropleth and undermining the orienting benefit described in [@mintzer_fix_my_chart_text_elements_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Labels overlap or pull attention away from the color pattern; the annotation reads like a paragraph
- **The Test:** Step back (or zoom out). If you notice labels before you notice the color regions, you’ve over-labeled.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Keep only a handful of widely recognized cities and one short perspective annotation (e.g., where the “sunbird” starts) as in [@mintzer_fix_my_chart_text_elements_2024].
- **Best Fix:** Choose labels that directly support the user question (candidate destinations + the origin city) and position a concise annotation near the relevant area so it reads as guidance, aligning with [@mintzer_fix_my_chart_text_elements_2024].
