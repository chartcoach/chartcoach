---
id: generate-additive-annotations-by-retrieving-related-articles-matching-location-and-variable-topic
title: Generate additive annotations by retrieving related articles matching location
  and variable topic
bibliography: references.bib
description: Create map callouts from other articles that mention both a related location
  and the mapped variable topic.
labels:
- chart:map
- task:annotate
- visual:text
- impact:context
- data:text
- audience:novice
- pipeline:annotation
---

## Pull annotation text from related location–topic articles <!-- role: advice -->

For each related location, retrieve articles that mention both the location and the mapped variable topic, then extract a topic-relevant sentence to use as an additive annotation on the map.

## Why additive annotations help explain mapped patterns <!-- role: reason -->

Maps can show variation but often lack the narrative context needed to interpret why regions differ. Additive annotations supplement the map with external, location-specific context that is not present in the input article or the mapped dataset.

**Mechanism:** Linking regions to short, topical explanatory text provides narrative scaffolding that can guide attention and interpretation of spatial patterns.

**Evidence:** The pipeline searches a news corpus for articles matching each related location and the variable phrase set, ranks candidate articles by cosine similarity to the input article, and selects a descriptive sentence for annotation [@gaoNewsViewsAutomatedPipeline2014].

**Notes:** These are additive annotations rather than “read-off-the-chart” observational statements.

## When additive annotation retrieval applies <!-- role: context -->

- **User Goal:** Understand why certain places stand out on a thematic map.
- **Task:** Read short context snippets tied to specific locations.
- **Data:** A news corpus plus a mapped variable and a set of related locations.
- **Chart Setting:** Annotated thematic map shown alongside an article.
- **Audience:** General readers; limited time and uneven domain knowledge.
- **Success Criterion:** Annotations are judged relevant to the article topic and location.

## When not to follow it <!-- role: exceptions -->

**Break it when:** No related articles exist that mention both the location and the topic. **Why:** Forced annotations risk being off-topic or misleading.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional retrieval and text processing complexity. **Risk:** Retrieved text can be relevant to the location but not the article’s framing, reducing perceived relevance. **Mitigation:** Rank candidate articles by similarity to the input article before extracting sentences.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a random related article for annotation without similarity ranking. **Why it fails:** The annotation may not match the input story’s topic or context, decreasing usefulness.

## Quick tests <!-- role: check -->

**Failure Sign:** Annotations feel generic or unrelated to the story’s specifics. **Quick Check:** Confirm the source article mentions both the location and the variable phrase terms. **Stronger Test:** Have readers rate annotation relevance on a sample set.

## What to do instead <!-- role: fix -->

- Rank candidate articles using cosine similarity to the input article and select the top match.
- Extract only sentences that contain the location mention and score them for topic relevance.
- Skip additive annotations when confidence is low and rely on observational annotations instead.
