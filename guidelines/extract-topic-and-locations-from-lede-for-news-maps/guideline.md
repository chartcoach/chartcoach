---
id: extract-topic-and-locations-from-lede-for-news-maps
title: Extract Topic and Locations from the Lede
bibliography: references.bib
description: "Use the headline and first sentences to infer a news article\u2019s\
  \ topic and geographic anchors for map generation."
labels:
- chart:map
- task:extract
- visual:annotation
- impact:relevance
- data:text
- audience:general
- domain:news
---

## The Rule <!-- role: advice -->

Extract noun-phrase topic terms and seed locations from the title and the first three sentences, and treat them as the primary inputs for selecting data, extent, and annotations.

## The Logic <!-- role: reason -->

This follows the “inverted pyramid” structure of journalism, where the main point and key entities often appear early; using these early cues helps ensure the visualization matches what the story is fundamentally about.

- **The Principle:** Lede-first topic/entity salience in news writing
- **The Evidence:** [@gaoNewsViewsAutomatedPipeline2014]

## Where to Apply <!-- role: context -->

- **User Goal:** See a map that reflects the central topic and places the story is about
- **Data Type:** News article text plus georeferenced datasets
- **Audience:** General news readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** Articles where key places/topics are introduced later (e.g., long-form narratives that delay the thesis)
- **Reason:** Early-sentence extraction may miss the actual focal entities, harming relevance [@gaoNewsViewsAutomatedPipeline2014]

## The Price <!-- role: costs -->

- **The Sacrifice:** Coverage of late-emerging story details
- **The Risk:** Incorrect “primary location” or topic terms that misdirect data selection [@gaoNewsViewsAutomatedPipeline2014]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Extracting from the whole article without prioritizing early cues
- **Why it fails:** It can overweight incidental mentions and dilute the article’s main intended focus [@gaoNewsViewsAutomatedPipeline2014]

## How to Check <!-- role: check -->

- **Visual Sign:** The map depicts a plausible dataset but doesn’t match what the first paragraph clearly emphasizes
- **The Test:** Re-read only the title + first three sentences; if the map’s variable/extent can’t be justified from them, the extraction likely failed [@gaoNewsViewsAutomatedPipeline2014]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust extraction to include the title plus the first three sentences (if only one was used)
- **Best Fix:** Use the extracted early entities as seeds, then validate against later text before finalizing variable and extent [@gaoNewsViewsAutomatedPipeline2014]
