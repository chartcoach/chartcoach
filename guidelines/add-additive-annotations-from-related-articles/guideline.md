---
id: add-additive-annotations-from-related-articles
title: Add Additive Annotations from Related News Articles
bibliography: references.bib
description: Provide extra context by attaching short, location- and topic-matched
  text snippets from other articles as map annotations.
labels:
- chart:map
- task:annotate
- visual:annotation
- impact:context
- data:text
- audience:general
- domain:news
---

## The Rule <!-- role: advice -->

Augment thematic maps with additive annotations by retrieving other articles that match both the location and the mapped topic, then extracting the most topic-relevant sentence to attach at that location.

## The Logic <!-- role: reason -->

Additive annotations supply context not present in the source article or dataset; selecting text that matches both location and topic increases the chance the annotation explains the mapped variation rather than distracting.

- **The Principle:** Contextual scaffolding through topic- and location-aligned annotation
- **The Evidence:** [@gaoNewsViewsAutomatedPipeline2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand why certain places look high/low and explore story-relevant details
- **Data Type:** News corpus + georeferenced topic variable
- **Audience:** General news readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** When no sufficiently relevant related articles exist for a location-topic pair
- **Reason:** Forced annotations can become noise and reduce perceived relevance [@gaoNewsViewsAutomatedPipeline2014]

## The Price <!-- role: costs -->

- **The Sacrifice:** More screen space and cognitive load
- **The Risk:** Annotations may bias interpretation toward a few places and away from the overall pattern [@gaoNewsViewsAutomatedPipeline2014]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Pulling random or location-only-matched snippets as “context”
- **Why it fails:** It reduces annotation relevance compared to topic+location matching (as tested via cosine similarity selection) [@gaoNewsViewsAutomatedPipeline2014]

## How to Check <!-- role: check -->

- **Visual Sign:** Annotations read like non sequiturs relative to the article topic or mapped variable
- **The Test:** For each annotation, confirm it mentions the target location and aligns with the mapped topic terms [@gaoNewsViewsAutomatedPipeline2014]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Re-rank candidate articles by similarity to the input article and require topic term overlap before extracting a sentence
- **Best Fix:** Select the annotation sentence by maximizing PMI with the variable phrase set (VarP) after retrieving top similar location-topic articles [@gaoNewsViewsAutomatedPipeline2014]
