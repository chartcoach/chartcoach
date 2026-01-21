---
id: bin-choropleth-values-with-jenks-and-use-sequential-lightness
title: Classify Choropleth Values with Jenks and Sequential Lightness
bibliography: references.bib
description: For thematic maps, bin values using Jenks natural breaks and map bins
  to a sequential light-to-dark color scheme.
labels:
- chart:choropleth
- task:encode
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- domain:news
---

## The Rule <!-- role: advice -->

For choropleth thematic maps, classify the quantitative variable into stepwise classes using Jenks natural breaks (e.g., 7 classes) and encode classes with a sequential scheme where lightness increases with value.

## The Logic <!-- role: reason -->

Natural breaks aims to place boundaries where values naturally separate; sequential lightness-dominant schemes support ordered reading of magnitude in thematic maps.

- **The Principle:** Data-driven binning plus ordered perceptual encoding for choropleths
- **The Evidence:** [@gaoNewsViewsAutomatedPipeline2014]

## Where to Apply <!-- role: context -->

- **User Goal:** See geographic variation in a single quantitative measure (e.g., unemployment, education)
- **Data Type:** County/state-level quantitative variables
- **Audience:** General news readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** When the story requires continuous perception or highlights precise thresholds defined externally
- **Reason:** Stepwise Jenks classes may obscure meaningful fixed cutoffs or smooth gradients [@gaoNewsViewsAutomatedPipeline2014]

## The Price <!-- role: costs -->

- **The Sacrifice:** Precision in reading exact values
- **The Risk:** Class boundaries can suggest categorical differences that are artifacts of binning [@gaoNewsViewsAutomatedPipeline2014]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a non-ordered palette for ordered data
- **Why it fails:** It breaks the implied magnitude ordering needed for thematic comparison [@gaoNewsViewsAutomatedPipeline2014]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers cannot tell whether darker/lighter corresponds to higher/lower values
- **The Test:** Ensure the legend reads from light (low) to dark (high) and that bins correspond to Jenks-derived breaks [@gaoNewsViewsAutomatedPipeline2014]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the palette with a sequential lightness-dominant scheme and verify legend ordering
- **Best Fix:** Recompute Jenks breaks for the current data slice and keep the number of classes consistent (e.g., 7) for readability [@gaoNewsViewsAutomatedPipeline2014]
