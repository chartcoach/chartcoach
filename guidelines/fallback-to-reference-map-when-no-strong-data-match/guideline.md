---
id: fallback-to-reference-map-when-no-strong-data-match
title: Default to a Reference Map When Data Match Is Weak
bibliography: references.bib
description: If no data variable strongly matches the article, present a locator/reference
  map centered on mentioned locations.
labels:
- chart:map
- task:locate
- visual:position
- impact:clarity
- data:geospatial
- audience:general
- domain:news
---

## The Rule <!-- role: advice -->

When no candidate variable clears a relevance threshold, generate a reference/locator map of mentioned locations instead of forcing a thematic map.

## The Logic <!-- role: reason -->

A weak topic-to-data match produces misleading thematic encodings; a reference map still provides spatial context and supports comprehension without implying unsupported quantitative comparisons.

- **The Principle:** Prefer reliable geographic context over low-confidence quantitative encoding
- **The Evidence:** [@gaoNewsViewsAutomatedPipeline2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Orient themselves geographically to the places discussed
- **Data Type:** Articles with locations but unclear quantitative variables
- **Audience:** General news readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** The story clearly implies a measurable variable but uses uncommon wording (so automated matching fails)
- **Reason:** A thematic map could still be appropriate if the variable can be recovered through improved matching or curated mappings [@gaoNewsViewsAutomatedPipeline2014]

## The Price <!-- role: costs -->

- **The Sacrifice:** Loss of data-driven pattern communication
- **The Risk:** Readers may expect quantitative explanation and receive only orientation [@gaoNewsViewsAutomatedPipeline2014]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing a thematic choropleth with an unrelated variable “close enough”
- **Why it fails:** It creates false narrative support and undermines trust in the visualization [@gaoNewsViewsAutomatedPipeline2014]

## How to Check <!-- role: check -->

- **Visual Sign:** Thematic legend/variable title feels disconnected from the article’s first paragraph
- **The Test:** If the selected variable cannot be justified by strong text-variable relevance, switch to a reference map [@gaoNewsViewsAutomatedPipeline2014]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Apply a strict relevance threshold and return a locator map when not met
- **Best Fix:** Improve variable relevance modeling (e.g., better phrase sets for variable labels) so thematic maps are only produced when justified [@gaoNewsViewsAutomatedPipeline2014]
