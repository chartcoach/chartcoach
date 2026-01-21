---
id: include-observational-annotations-for-extreme-values
title: Annotate Extreme Values as Observational Callouts
bibliography: references.bib
description: Add simple callouts that point to highest/lowest locations to help readers
  notice key extremes in the map.
labels:
- chart:map
- task:highlight
- visual:annotation
- impact:attention
- data:quantitative
- audience:general
- domain:news
---

## The Rule <!-- role: advice -->

Add observational annotations that explicitly point out extreme (highest/lowest) locations when a small set of outliers provides useful context for the mapped variable.

## The Logic <!-- role: reason -->

Extreme-value callouts direct attention to salient points that readers may otherwise miss in dense geographic displays, supporting narrative emphasis in news maps.

- **The Principle:** Salience through explicit extreme-value marking
- **The Evidence:** [@gaoNewsViewsAutomatedPipeline2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly identify notable highs/lows in a geographic distribution
- **Data Type:** Choropleths where extremes are meaningful to the story
- **Audience:** General news readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** When extremes are noise (e.g., known measurement artifacts) or distract from the story’s intended comparison
- **Reason:** Pointing to extremes can misframe interpretation by overemphasizing anomalies [@gaoNewsViewsAutomatedPipeline2014]

## The Price <!-- role: costs -->

- **The Sacrifice:** Adds annotation elements that may compete with additive context annotations
- **The Risk:** Readers may overgeneralize from highlighted outliers [@gaoNewsViewsAutomatedPipeline2014]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Highlighting many “top” places instead of a minimal extreme set
- **Why it fails:** It dilutes the purpose of observational annotation and increases clutter [@gaoNewsViewsAutomatedPipeline2014]

## How to Check <!-- role: check -->

- **Visual Sign:** The map contains many callouts that feel redundant with the color encoding
- **The Test:** Count observational callouts; if they are not a small set focused on extremes, reduce them [@gaoNewsViewsAutomatedPipeline2014]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Limit to the single highest and/or lowest location (or a very small number)
- **Best Fix:** Only add extreme-value callouts when they support the article’s topic and do not crowd out more relevant explanatory annotations [@gaoNewsViewsAutomatedPipeline2014]
