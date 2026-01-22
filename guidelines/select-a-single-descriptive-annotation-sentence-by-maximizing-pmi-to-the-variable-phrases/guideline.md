---
id: select-a-single-descriptive-annotation-sentence-by-maximizing-pmi-to-the-variable-phrases
title: Select a single descriptive annotation sentence by maximizing PMI to the variable
  phrases
bibliography: references.bib
description: Choose the most topic-specific sentence for a map callout using PMI against
  the variable phrase set.
labels:
- chart:map
- task:annotate
- visual:text
- impact:relevance
- data:text
- audience:novice
- pipeline:annotation
---

## Pick the annotation sentence with the highest PMI to the topic <!-- role: advice -->

From a candidate related article, extract sentences that mention the target location and select the sentence whose noun phrases have the highest mean PMI to the mapped variable phrase set.

## Why PMI-based sentence choice yields topic-specific callouts <!-- role: reason -->

Even within a relevant article, many sentences mentioning a location are not about the mapped topic. Selecting the sentence with the strongest PMI association to the variable phrases increases topical specificity and reduces irrelevant callouts.

**Mechanism:** PMI-based scoring favors sentences whose language co-occurs with the variable descriptors in the corpus, acting as a filter for topic alignment.

**Evidence:** After selecting a related article, the pipeline ranks candidate sentences that mention the location by topic relevance and selects the sentence with the highest mean PMI to the variable phrase set for annotation content [@gaoNewsViewsAutomatedPipeline2014].

**Notes:** This operates after article-level filtering by location and topic.

## When PMI-based sentence selection applies <!-- role: context -->

- **User Goal:** Read a short, relevant explanation tied to a mapped region.
- **Task:** Select a single sentence for an annotation box.
- **Data:** Candidate related articles containing multiple location-mentioning sentences.
- **Chart Setting:** Limited screen space for a small number of callouts.
- **Audience:** General readers; needs concise, relevant snippets.
- **Success Criterion:** Annotation content is judged relevant to the topic and location.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The mapped topic is poorly represented in the corpus language (few co-occurrences). **Why:** PMI scoring may be unstable and choose non-representative sentences.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Potentially ignores stylistically clearer sentences that are slightly less topic-associated. **Risk:** PMI can favor jargon-heavy sentences that co-occur in the corpus but are less readable. **Mitigation:** Constrain candidates to sentences that mention the location and are not overly long.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Selecting the first sentence that mentions the location. **Why it fails:** Early mention does not guarantee topical relevance to the mapped variable.

## Quick tests <!-- role: check -->

**Failure Sign:** Callouts mention the location but not the mapped concept. **Quick Check:** Verify that the selected sentence contains noun phrases strongly aligned with the variable phrases. **Stronger Test:** Compare user relevance ratings between PMI-selected sentences and baseline heuristics.

## What to do instead <!-- role: fix -->

- Re-rank candidate sentences using topic relevance rather than position in the article.
- Require that the chosen sentence include at least one variable phrase term or close match.
- Omit the callout for that location when no sentence clears a relevance threshold.
