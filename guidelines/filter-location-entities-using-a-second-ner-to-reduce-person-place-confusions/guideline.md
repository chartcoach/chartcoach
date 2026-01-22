---
id: filter-location-entities-using-a-second-ner-to-reduce-person-place-confusions
title: "Filter candidate locations using a second NER to remove person\u2013place\
  \ confusions"
bibliography: references.bib
description: Use a second classifier to suppress entities tagged as locations that
  are likely people.
labels:
- chart:map
- task:classify
- visual:none
- impact:accuracy
- data:text
- audience:novice
- pipeline:ner
---

## Cross-check location tags with a second NER <!-- role: advice -->

When an entity linker tags a mention as a location, filter it out if a second named-entity recognizer labels the same mention as a person.

## Why cross-checking reduces false location anchors <!-- role: reason -->

False positive locations can distort map extent, annotations, and perceived relevance. Using a second recognizer as a sanity check removes a common class of errors where a name is misinterpreted as a place.

**Mechanism:** Agreement between independent detectors increases confidence; disagreement (location vs person) flags likely misclassification that harms downstream map decisions.

**Evidence:** The pipeline combines Wikifier output with OpenCalais, filtering entities tagged as locations by Wikifier but persons by OpenCalais to improve location tagging accuracy [@gaoNewsViewsAutomatedPipeline2014].

**Notes:** This is a precision-oriented step; it may reduce recall.

## When cross-check filtering applies <!-- role: context -->

- **User Goal:** Avoid misleading map framing due to incorrect location extraction.
- **Task:** Improve precision of location tagging in article text.
- **Data:** Article text with entity names that can refer to people or places.
- **Chart Setting:** Automated map generation where extracted locations drive extent and annotations.
- **Audience:** General readers; errors are highly visible and trust-damaging.
- **Success Criterion:** Fewer incorrect mapped locations.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The system’s priority is maximum recall of possible places for exploratory browsing. **Why:** Filtering disagreements can remove legitimate locations that one recognizer mislabels.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Recall of true locations in edge cases. **Risk:** Over-filtering can yield too few extracted locations, forcing weak extents. **Mitigation:** Keep filtered entities as low-confidence candidates rather than discarding outright.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Treating any single NER’s “location” label as authoritative. **Why it fails:** Single-model errors propagate into highly salient map mistakes.

## Quick tests <!-- role: check -->

**Failure Sign:** People’s names appear as map points or drive zoom. **Quick Check:** Spot-check extracted “locations” that are capitalized names and verify they are places in context. **Stronger Test:** Compare precision/recall with and without cross-check filtering on a labeled article set.

## What to do instead <!-- role: fix -->

- Retain a confidence score per extracted location and penalize disagreements instead of hard filtering.
- Restrict location-driven extent setting to only high-confidence locations.
- Fall back to a reference map when too few high-confidence locations remain.
